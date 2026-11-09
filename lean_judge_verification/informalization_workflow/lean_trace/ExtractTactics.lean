import Lean

/-!
Re-elaborate an unchanged source file and serialize its InfoTree tactic nodes.
This driver uses APIs shared by Lean 4.13.0-rc3 and 4.32.0. The Python launcher
validates retained source bytes and adds hashes, exact commands, and provenance.
-/

open Lean Elab

namespace InformalizationTrace

structure TraceState where
  tactics : Array Json := #[]
  missingSource : Nat := 0
  holes : Nat := 0
  filtered : Nat := 0

def syntaxSpan (fileMap : FileMap) (stx : Syntax) : Option Json := do
  let start ← stx.getPos?
  let stop ← stx.getTailPos?
  let a := fileMap.toPosition start
  let b := fileMap.toPosition stop
  return Json.mkObj [
    ("start", Json.mkObj [("line", toJson a.line), ("column", toJson a.column),
      ("byte", toJson start.byteIdx)]),
    ("end", Json.mkObj [("line", toJson b.line), ("column", toJson b.column),
      ("byte", toJson stop.byteIdx)])]

def sourceKind (stx : Syntax) : String :=
  match stx.getHeadInfo with
  | .original .. => "original"
  | .synthetic _ _ true => "synthetic_canonical"
  | .synthetic .. => "synthetic"
  | .none => "none"

def goalState (ctx : ContextInfo) (mctx : MetavarContext) (goals : List MVarId) : IO Json := do
  let ctx := { ctx with mctx }
  let records ← goals.toArray.mapM fun goal => do
    try
      let pretty ← ctx.runMetaM {} do
        return (← Meta.ppGoal goal).pretty
      return Json.mkObj [("goal_id", toJson goal.name.toString), ("pretty", toJson pretty)]
    catch e =>
      return Json.mkObj [("goal_id", toJson goal.name.toString),
        ("pretty", Json.null), ("render_error", toJson e.toString)]
  return Json.mkObj [("goal_count", toJson goals.length), ("goals", Json.arr records)]

partial def visit (fileMap : FileMap) (tree : InfoTree) (ctx? : Option ContextInfo)
    (parent : Option Nat) (commandSpan : Option Json) (originalOnly : Bool) : StateRefT TraceState IO Unit := do
  match tree with
  | .context partialCtx child =>
    visit fileMap child (partialCtx.mergeIntoOuter? ctx?) parent commandSpan originalOnly
  | .hole _ => modify fun s => { s with holes := s.holes + 1 }
  | .node info children =>
    let mut childParent := parent
    let mut childCommandSpan := commandSpan
    if let .ofCommandInfo command := info then
      childCommandSpan := syntaxSpan fileMap command.stx
    if let .ofTacticInfo tactic := info then
      if originalOnly && sourceKind tactic.stx != "original" then
        modify fun s => { s with filtered := s.filtered + 1 }
      else if let some ctx := ctx? then
        if let some span := syntaxSpan fileMap tactic.stx then
          let index := (← get).tactics.size
          let before ← goalState ctx tactic.mctxBefore tactic.goalsBefore
          let after ← goalState ctx tactic.mctxAfter tactic.goalsAfter
          let record := Json.mkObj [
            ("index", toJson index), ("parent_index", toJson parent),
            ("source_span", span), ("command_span", toJson childCommandSpan),
            ("syntax_kind", toJson tactic.stx.getKind.toString),
            ("source_kind", toJson (sourceKind tactic.stx)),
            ("elaborator", toJson tactic.elaborator.toString),
            ("declaration_name", toJson (ctx.parentDecl?.map Name.toString)),
            ("namespace", toJson ctx.currNamespace.toString),
            ("before", before), ("after", after)]
          modify fun s => { s with tactics := s.tactics.push record }
          childParent := some index
        else
          modify fun s => { s with missingSource := s.missingSource + 1 }
      else
        modify fun s => { s with missingSource := s.missingSource + 1 }
    for child in children do
      visit fileMap child (info.updateContext? ctx?) childParent childCommandSpan originalOnly

unsafe def run (sourceFile outputFile moduleName : String) (originalOnly : Bool) : IO UInt32 := do
  initSearchPath (← findSysroot)
  enableInitializersExecution
  let input ← IO.FS.readFile sourceFile
  let inputCtx := Parser.mkInputContext input sourceFile
  let options := ({} : Options).setBool `Elab.async false
  let (header, parserState, messages) ← Parser.parseHeader inputCtx
  let (env, messages) ← processHeader header options messages inputCtx
  IO.FS.writeFile (outputFile ++ ".progress") "imports_processed\n"
  let env := env.setMainModule moduleName.toName
  let commandState := { Command.mkState env messages options with
    infoState := { enabled := true } }
  let frontend ← IO.processCommands inputCtx parserState commandState
  IO.FS.writeFile (outputFile ++ ".progress") "commands_elaborated_extracting_states\n"
  let (_, collected) ← (do
    for tree in frontend.commandState.infoState.trees do
      visit inputCtx.fileMap tree none none none originalOnly).run ({} : TraceState)
  let messages ← frontend.commandState.messages.toList.toArray.mapM fun message => do
    return Json.mkObj [
      ("severity", toJson (match message.severity with
        | .error => "error" | .warning => "warning" | .information => "information")),
      ("line", toJson message.pos.line), ("column", toJson message.pos.column),
      ("text", toJson (← message.data.toString))]
  let hasErrors := frontend.commandState.messages.hasErrors
  let result := Json.mkObj [
    ("has_errors", toJson hasErrors), ("messages", Json.arr messages),
    ("tactics", Json.arr collected.tactics),
    ("filtered_synthetic_tactic_nodes", toJson collected.filtered),
    ("unanchored_tactic_nodes", toJson collected.missingSource),
    ("unresolved_info_tree_holes", toJson collected.holes)]
  IO.FS.writeFile outputFile (result.compress ++ "\n")
  IO.FS.writeFile (outputFile ++ ".progress") "trace_written\n"
  return if hasErrors then 1 else 0

end InformalizationTrace

unsafe def main (args : List String) : IO UInt32 := do
  match args with
  | [sourceFile, outputFile, moduleName] => InformalizationTrace.run sourceFile outputFile moduleName false
  | [sourceFile, outputFile, moduleName, "original_only"] => InformalizationTrace.run sourceFile outputFile moduleName true
  | _ =>
    IO.eprintln "usage: lean --run ExtractTactics.lean SOURCE_FILE OUTPUT_JSON MODULE_NAME"
    return 2
