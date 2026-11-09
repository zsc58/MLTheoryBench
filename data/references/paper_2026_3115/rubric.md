# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs the Cartesian-product HMM and correctly derives the product-form initial distribution and transition matrix (including the Kronecker ordering/indexing).
- **2 points:** States and justifies the ordinary HMM forward-filtering recursion, normalization constants, and likelihood factorization from the Markov property.
- **4 points:** Proves the tensorized recursion is exactly equivalent by verifying the vectorization/Kronecker/mode-contraction and Hadamard identities and carrying out the induction over time. Merely naming tensorization or Kronecker products earns little credit.
- **2 points:** Counts each mode contraction as O(M M^k), obtains O(N M sum_k M^k), compares it with O(N M^2)=O(N M product_k M^k), and identifies the ratio as a constant-factor asymptotic comparison of transition-update costs for N>=2. States the equal-size specialization for fixed K and does not claim a transition-update speedup at N=1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct for treating the tensorized recursion or complexity bound as an unsupported assumption, for incorrect Kronecker ordering that changes the update, or for omitting the normalization/equality claim. Do not require exact arithmetic constants for the cost ratio.
