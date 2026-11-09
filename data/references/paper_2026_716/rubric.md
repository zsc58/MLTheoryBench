# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly models first absorption through the transient block, deriving `p_theta(t | q)=e_q^T M^(t-1)R` and identifying the role of `R=(I-M)1_{S_y}`.
- **3 points:** Uses `rho(M)<1` to justify the Neumann fundamental matrix, the ordinary generating function with its leading factor `z`, almost-sure absorption, and the stated first and second moments/variance. Weighted series or equivalent recurrences must be justified; the second-moment coefficients are `(k+1)^2`, not `(k+1)(k+2)`.
- **3 points:** Derives the log-linear kernel derivatives, specifies the transient-block and absorption-vector derivatives, and propagates them through matrix powers and the resolvent to obtain the correct pmf and generating-function sensitivities.
- **2 points:** Correctly differentiates the fundamental-matrix moment expressions to obtain mean, second-moment, and variance sensitivities, with all dimensions and parameter dependencies consistent.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices; equivalent recurrence or generating-function derivations are acceptable when they justify every requested identity.

All-ones vectors in moment expressions belong to the transient coordinate space. Nonedge transition derivatives are zero. The kernel formula is required on edges, where the features are defined.

The `t=1` power derivative is an empty sum. The generating-function domain includes `z=0` and `rho(M)=0`; a proof must not exclude these cases by dividing by the spectral radius. No positivity assumption on every entry of `R` or every hitting-time probability is permitted. Periodicity is allowed.

Parameter derivatives hold the graph, base weights, features, class set, starting vertex, and `z` fixed. Differentiating already established smooth finite matrix formulas is sufficient; no separate interchange of differentiation with an infinite expectation is required. Ambient derivatives of the displayed log-linear extension are valid even when `Theta` is not open. Identifiability need not be used in the proof.

No spectral expansion, Fisher-information calculation, Lyapunov equation, quotient geometry, or betweenness argument is required.
