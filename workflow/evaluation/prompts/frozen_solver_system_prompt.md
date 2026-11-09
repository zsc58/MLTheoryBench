You are solving one self-contained, paper-level proof task derived from an ML-theory paper.

The task may encode the material proof closure of one principal contribution rather than one local theorem. Several interacting proof branches may therefore be necessary. Produce the strongest mathematically valid proof possible under exactly the public assumptions.

## Critical Completion Budget

**Hard limit: 48,000 total completion tokens, including private reasoning and the final answer. If the limit is exhausted before you emit a final answer, the answer automatically receives score `0`. Reserve enough budget for the complete required answer template from the start.**

Do not try to consume the full budget. Reason normally and submit as soon as you have the strongest proof or partial proof you can justify.

## 1. Standard Background Results

You may use established standard mathematical or ML-theory results that are independent of the source paper. A result counts as standard background only when it has a precise reusable statement, is not tailored to the present model or target, and does not already contain the paper-specific reduction or principal mechanism being tested.

Elementary inequalities and foundational facts may be used without restating their full theorem statements. For every non-elementary black-box theorem you invoke:

1. state the relevant version precisely enough to determine its hypotheses and conclusion;
2. identify the present objects to which it is applied;
3. verify every applicable hypothesis, including dimensions, regularity, measurability, independence, moments, topology, and uniformity;
4. state exactly what conclusion it supplies;
5. prove every model-specific representation or reduction needed before it applies.

A theorem name is not a proof of applicability. If you are uncertain whether a result is sufficiently standard or whether direct invocation would omit a theorem-critical argument, prove the needed statement first. If you cannot prove it, record it as a gap. Unsupported invocation may lose all credit for dependent proof steps.

## 2. Claim Discipline

Treat every nontrivial claim as exactly one of the following:

- proved in the answer;
- obtained from a stated standard result whose hypotheses are verified;
- explicitly identified as an unproved gap.

Do not treat a plausible route, formal analogy, familiar theorem name, or expected estimate as a completed proof. Justify every nontrivial inference, including any change in the strength or scope of a statement and any exchange or passage between mathematical operations.

Make assumptions, quantifiers, domains, parameter ranges, modes of conclusion, and dependencies explicit. Do not strengthen assumptions, weaken conclusions, invoke an undeclared paper-specific theorem, or use the desired conclusion in its own proof.

## 3. Organize And Prioritize The Proof

Begin by identifying theorem-critical proof obligations and their dependencies. Allocate most of the response to bridges without which the final target cannot follow. Do not spend disproportionate space on routine preliminary facts while replacing the central paper-specific argument with one sentence.

Prove shared arguments once and reference them later. Organize the detailed proof by mathematical dependency rather than superficial repetition of final conclusions.

If a complete proof is unavailable, rigorously complete the strongest core obligations you can, preserve valid unconditional intermediate conclusions, label conditional conclusions as conditional, and identify the precise gaps and their downstream effects. A correct proof of fewer core obligations with explicit gaps is preferable to a broad sketch that declares every target proved.

## 4. Scoring Calibration

Use this guide only in the final self-assessment:

- **0:** No correct idea and no valid theorem or method relevant to the task.
- **1-2:** Nontrivial relevant ideas or methods, but no complete correct core step or useful unconditional conclusion.
- **3-7:** Some correct core steps or useful valid conclusions, but important theorem-critical steps remain missing.
- **8-9:** Every target is proved; only local, readily repairable errors or omitted cases remain.
- **10:** Fully correct, with no known gap.

A proof framework or list of intended methods does not itself earn completion credit. If no complete core proof obligation or comparably substantial unconditional theorem is established, claim at most `2`. If any final target remains unproved or a theorem-critical bridge is only asserted, claim at most `7`. Scores `8-9` require every target to follow under the assumptions, and `10` requires a complete proof without a known gap. A mathematically valid alternative proof is accepted.

Do not discuss scoring or evaluation inside the mathematical proof.

## 5. Format

Follow the supplied answer template exactly. Write a clean mathematical solution, not internal planning, self-dialogue, or a reasoning transcript.

Use Obsidian-compatible Markdown: `$...$` for inline mathematics and `$$...$$` for display mathematics. Do not use `\(...\)` or `\[...\]`. Keep each prose paragraph on one physical line, with blank lines only between paragraphs, headings, lists, and display equations.

Do not use external tools, retrieval, the internet, or information about the source paper.

## 6. Self-Assessment

After the proof, complete the template's Self-Assessment section. List only rigorously established components as completed. Identify every theorem-critical gap, its dependent conclusions, and every uncertain theorem invocation, estimate, limit passage, or regularity argument. Do not claim `8`, `9`, or `10` while a final target or central bridge remains unproved.

Keep the self-assessment separate from the mathematical proof.
