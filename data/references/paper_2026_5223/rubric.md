# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the forgotten-RLS one-step potential identity from the exact unprojected recursion and controls the residual/gradient term using D = B_y + B_z R. The initialization and matrix inverses must be justified, explicitly or by an immediately applicable positive-definiteness argument.
- **4 points:** Proves the discounted leverage/log-determinant estimate and the moving-comparator potential bound, obtaining every term of Psi_h with the stated coefficients. Allocate 2 points to the leverage estimate, including the discount contribution dT log(1/gamma) <= 2dT/h, and 2 points to initialization and path-length control. The terminal potential can be discarded without imposing stability on the terminal update.
- **1 point:** Establishes that clipping each scale prediction to [-B,B] does not increase squared loss when |y_t| <= B, and correctly transfers the idealized scale bound to the experts entering the pool.
- **3 points:** Fully justifies the finite-pool aggregation bound and combines both oracle alternatives. Allocate 2 points to the aggregation argument: a valid positive-part potential increment estimate, cancellation of its linear term including the zero-denominator case, bounded pseudo-regrets, and conversion from cumulative pseudo-regret to squared-loss regret. Allocate 1 point to combining the clipped raw alternative with every clipped scale bound and minimizing over the nonempty scale set.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the particular universal constant 8; any valid universal constant is acceptable.

Merely naming an aggregation method or citing the paper-specific finite-pool claim does not discharge its proof obligation. An independently justified applicable result or a direct derivation must establish the required bound for the update in the task.

Do not impose B >= B_y: the task separately bounds outcomes by B_y for the tracking calculation and by B for clipping and aggregation. Do not require delta <= B_z^2 h, a geometric grid, positive path length, a causal comparator, stochastic assumptions, persistence of excitation, coefficient projection, or a bound on v_{T+1}.

The first oracle alternative is the loss of the clipped raw forecasts. The tracking calculation concerns the idealized unprojected coefficients and their unclipped predictions before applying the clipping comparison. An argument for a modified projected or covariance-inflated recursion is not sufficient unless it also proves the stated result for the exact recursion in the task.

A proof whose calculations already cover T = 1, B = 0, R = 0, zero path length, and h = 2 need not discuss these cases separately. Do not require the optional simplified path-length estimate or the distributional and local-band refinements, which are not public targets.
