# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly formulate the KL-constrained maximin problem over all measurable conditional joint densities, express the information-gain utility through the auxiliary outcome marginal, and justify the Lagrange-dual decomposition with the -beta rho penalty. Verify effective-domain strict feasibility and explain why using beta>0 also covers a zero-multiplier boundary. Justify separation using admissible measurable pointwise optimizers, rather than assuming an arbitrary convex kernel class is separable.
2. **3 points:** Carry out the central variational minimization over the joint law and auxiliary marginal, including the normalized geometric-mixture optimizer and identification of the pointwise value with a Renyi divergence/Sibson alpha-mutual information. The minimized joint log-partition value has coefficient -(1+beta), not -beta. Handle zero overlap as infinite divergence rather than dividing by a zero normalizer.
3. **2 points:** Derive the optimized tilted marginal p_alpha(x|xi) and substitute it to obtain the robust-value representation in alpha, including alpha=beta/(1+beta). Verify that the optimized joint law has this outcome marginal and that its measurable assembly is admissible. Taking the supremum over policies requires no interchange of optimization order.
4. **3 points:** Prove the worst-case joint-law formula and, by conditioning, the alpha-tempered posterior on outcomes of positive marginal probability. Prove that an interior dual-optimal multiplier yields a feasible constrained optimizer; invoking strong duality or complementary slackness alone without verifying the primal law is insufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Deduct for treating the variational identity, geometric-mixture calculation, or posterior characterization as unexplained named methods. A properly stated standard duality theorem is acceptable when its hypotheses are verified for the kernel optimization. Do not require existence or uniqueness of an interior dual maximizer for every radius: constrained optimality is conditional on attainment. No arbitrary restriction of the joint-density domain is part of the repaired task.
