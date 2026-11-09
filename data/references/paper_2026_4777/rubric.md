# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derive the unique scalar minimizer tau=(|x|/epsilon+1)^2 on tau>=1 and its minimum value log(|x|/epsilon+1), including the derivative or an equivalent valid argument.
- **3 points:** Establish the alpha->infinity endpoint by proving the coordinatewise lower bound and showing that the vector of scalar minimizers is feasible for every sufficiently large TV budget, or by an equivalent valid argument.
- **2 points:** Handle alpha=0 by proving all latent variables are equal, minimizing the resulting scalar objective at the average of the squared factors, and evaluating it as the stated global logarithmic l2 expression.
- **2 points:** Prove lim_{alpha->0+} Psi_{alpha,epsilon}(x)=Psi_{0,epsilon}(x). For example, place positive-budget minimizers or approximate minimizers in a common bounded sublevel, extract a limit feasible at budget zero, and combine the resulting lower bound with the upper bound supplied by a zero-budget competitor. Merely evaluating the objective at alpha=0 does not establish this convergence.
- **1 point:** Justify the well-defined latent minimum by attainment or an equivalent elementary argument, and state both endpoint conclusions with the correct quantifiers and parameter dependence, including the right-hand limit at zero. Handle boundary cases without adding assumptions such as x!=0 or N>1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A missing justification of feasibility, scalar optimality, the common-latent reduction, or convergence as alpha decreases to zero is theorem-critical. Compactness is one acceptable route to the zero-budget limit, not a required method. A proof using approximate minimizers may establish the limiting inequalities before verifying attainment separately. Do not award the convergence points solely for an assertion that the constraint at alpha=0 forces a constant vector. No proof of specialized general minimizer-existence results is required for this explicit integrand.
