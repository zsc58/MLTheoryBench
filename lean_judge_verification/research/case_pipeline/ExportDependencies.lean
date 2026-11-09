import Lean

/-!
Export elaborated declaration dependencies, not identifier matches in tactic source.
Project declarations are expanded to closure. External declarations form an explicit
background boundary, while `collectAxioms` checks the complete target dependency closure.
This file is imported by a generated driver after the original target module is built.
-/

open Lean Elab Command Meta

namespace CaseDependencies

def kind (c : ConstantInfo) : String :=
  match c with
  | .axiomInfo _ => "axiom"
  | .defnInfo _ => "definition"
  | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque"
  | .quotInfo _ => "quotient"
  | .inductInfo _ => "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"

def value (c : ConstantInfo) : Option Expr :=
  match c with
  | .defnInfo v => some v.value
  | .thmInfo v => some v.value
  | .opaqueInfo v => some v.value
  | _ => none

def namesJson (ns : Array Name) : Json :=
  toJson (ns.map Name.toString)

def moduleName (env : Environment) (n : Name) : String :=
  match env.getModuleIdxFor? n with
  | some i => (env.header.moduleNames[i.toNat]!).toString
  | none => ""

elab "#export_case " target:ident " prefix " prefArg:str " to " output:str : command => do
  let root := target.getId
  let pref := prefArg.getString
  let env ← getEnv
  let _ ← getConstInfo root
  let mut todo := #[root]
  let mut seen : NameSet := {}
  let mut nodes : Array Json := #[]
  let mut external : NameSet := {}
  while !todo.isEmpty do
    let n := todo[todo.size - 1]!
    todo := todo.pop
    if seen.contains n then continue
    seen := seen.insert n
    let c ← getConstInfo n
    let mod := moduleName env n
    let td := c.type.getUsedConstants
    let vd := match value c with
      | some v => v.getUsedConstants
      | none => #[]
    let md := c.getUsedConstantsAsSet.toArray.filter fun d =>
      d != n && !td.contains d && !vd.contains d
    let ranges ← findDeclarationRanges? n
    let rangeJson := match ranges with
      | some r => Json.mkObj [
          ("start_line", toJson r.range.pos.line),
          ("start_column", toJson r.range.pos.column),
          ("end_line", toJson r.range.endPos.line),
          ("end_column", toJson r.range.endPos.column)]
      | none => Json.null
    let statement ← liftTermElabM do
      withOptions (fun o => o.setBool `pp.fullNames true) do
        return (← ppExpr c.type).pretty
    nodes := nodes.push <| Json.mkObj [
      ("name", toJson n.toString), ("kind", toJson (kind c)),
      ("module", toJson mod), ("range", rangeJson),
      ("elaborated_statement", toJson statement),
      ("type_dependencies", namesJson td),
      ("value_dependencies", namesJson vd),
      ("declaration_metadata_dependencies", namesJson md),
      ("proof_or_definition_body_available", toJson (value c).isSome)]
    for d in td ++ vd ++ md do
      let dm := moduleName env d
      if dm == pref || (pref ++ ".").isPrefixOf dm then
        if !seen.contains d then todo := todo.push d
      else
        external := external.insert d
  let mut boundaries : Array Json := #[]
  for n in external.toArray do
    let c ← getConstInfo n
    boundaries := boundaries.push <| Json.mkObj [
      ("name", toJson n.toString), ("kind", toJson (kind c)),
      ("module", toJson (moduleName env n))]
  let axioms ← collectAxioms root
  let result := Json.mkObj [
    ("schema_version", toJson "1.1"),
    ("extraction_method", toJson "elaborated_type_proof_term_and_declaration_metadata"),
    ("target", toJson root.toString),
    ("project_module_prefix", toJson pref),
    ("project_declaration_closure", Json.arr nodes),
    ("external_background_boundary", Json.arr boundaries),
    ("transitive_axioms", namesJson axioms),
    ("scope_note", toJson "Type/proof terms and inductive/recursor metadata are distinguished; constructors preserve structure-field contracts. This is not a minimal mathematical dependency graph. External bodies stop at the background boundary; collectAxioms obtains complete transitive axiom dependencies.")]
  liftIO <| IO.FS.writeFile output.getString (result.pretty ++ "\n")
  logInfo m!"Exported {nodes.size} project declarations and {boundaries.size} external boundary declarations for {root}."

end CaseDependencies
