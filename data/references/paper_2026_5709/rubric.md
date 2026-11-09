# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly expands one output channel and isolates the output-position factor \(b_i^{(h)}\), kernel factor, and input-position factor \(a_j^{(h)}\).
- **2 points:** Shows that \(T_{ij}^{(h)}=\kappa^{(h)}((i-j)/n)\) depends only on \(i-j\), and therefore is Toeplitz.
- **4 points:** Constructs the two diagonal matrices and verifies entrywise that the induced summand matrix is exactly \(D_{\mathrm{out}}^{(h)}T^{(h)}D_{\mathrm{in}}^{(h)}\). Merely asserting the factorization without deriving its entries does not earn full credit.
- **1 point:** Connects the matrix entries back to the row-sum formula for the output and observes that the argument applies independently to every channel.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental notation. The matrix being factorized must represent the requested channelwise summands with both input-dependent diagonal factors correctly identified. A missing Toeplitz justification or an unsupported factorization is a material gap.
