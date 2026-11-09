# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the normalized aggregate and its zero-mean convention correctly, and proves A0 non-negativity and both directions of A1, including laws supported on proper faces of the simplex.
- **3 points:** Proves strict A3 for the stated coupling: establishes preservation of means and increase of coordinate variances, and explains why a positive-variance spread coordinate must have positive mean. A valid equivalent argument receives full credit.
- **2 points:** Derives C_k(Q)<= (1/2)(1-mu_k) for mu_k>0 and explains that its right-hand side tends to 1/2, not zero, as mu_k approaches zero from above. This is an upper-bound statement, not a universal positive lower bound or a claim that every C_k has a nonzero limit. The reference proof's attainability example and global aggregate maximum are useful supporting results, not additional required conclusions.
- **2 points:** Establishes failure of A2 for the arbitrary fixed K>=2 by showing that the uniform simplex law has strictly smaller aggregate than some admissible law. The reference proof computes its moments and compares with a vertex mixture; a valid strict comparison without the exact uniform value or a global maximization argument also receives full credit.
- **1 point:** Supplies a feasible deterministic translation with preserved variances and unequal aggregate values for the arbitrary fixed K>=2, establishing failure of A5. A binary construction embedded in a simplex face by appending zero coordinates suffices; those coordinates must be interpreted using the zero-mean convention.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact counterexample values, global maximum calculation, or exact uniform-simplex moment calculation when the requested conclusions are otherwise established. The formula for EU is supplied by the problem and need not be independently derived from an information-theoretic approximation.

A counterexample stated only for K=2 leaves the arbitrary-dimension A5 conclusion incomplete unless its extension is made clear. Appending zero coordinates is a routine repair; assess an omitted embedding as an omitted case rather than rejecting the entire proof.

Award downstream steps when independently justified, even if an earlier calculation contains a localized error; theorem-critical unsupported claims remain major gaps. Standard elementary probability and integration facts may be used, and correctly stated standard simplex or Dirichlet moment formulas are acceptable. No specialized external uncertainty theorem is needed.
