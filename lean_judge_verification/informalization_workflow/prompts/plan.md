# Author phase 1: select the boundary and submit the sketch

Use a fresh case-local author thread. Follow author.md and the job's boundary policy. Your responsibility includes selecting the mathematical boundary; do not request a hand-written expanded/permitted list from the parent.

1. Read the complete target and its formal context. Use declaration_index.json and the original dependency export to navigate actual type, proof-body and declaration-metadata edges. Read referenced source interfaces; inspect substantive project proofs before deciding where to stop.
2. Build a target-rooted dependency sketch and foundational-to-target presentation. Decide which project results to expand, which to grant as named tools, and which implementation facts belong to explained context. Write the retained proof obligations in mathematical language.
3. Save exactly four files in plan/: boundary.json, sketch.json, pf_sketch.md and standard_lemmas.md. Do not write the detailed proof yet.

boundary.json records expanded_obligations, background_lemmas with complete interfaces, exact lean_declarations, source anchors and stopping reasons, and context_groups with exact declarations and grouping reasons. Keep one classification per declaration. Non-theorem definitions and constructors are traversed by code automatically; an encountered project theorem must be expanded, explicitly granted, or explicitly grouped as routine context. Grouping context never stops the dependency traversal. The external export stops proof bodies, so external standard interfaces must be checked in retained source files rather than inferred from names.

Every expanded sketch declaration must be a real project declaration from the compiled registry. Use each mathematical node once and reference shared nodes. Background declarations may be bundled under one B-interface, but do not claim a stronger bundled theorem than those sources support.

Use pipeline.py check-plan to find missing classifications, invalid IDs, unreachable nodes or absent sources. Correct accounting defects in the plan and repeat the check. If a needed source/declaration is not in the prepared inventory, record a limitation and report the required extraction; do not manufacture an anchor or silently omit it. Only the external runner records thread/turn IDs and freezes the plan.

End by handing off the four planning files, summarizing stopping decisions and any resource limitations. The runner then freezes the plan and extracts the requested expanded-file traces. This same author thread will receive the writing phase; the independent reviewer comes later.
