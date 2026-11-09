# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes the INT8 scale relations, inactive clipping, and the first residual bound $\|r\|_\infty\le\alpha/2$.
- **2 points:** Correctly proves the INT8 residual is in the second-pass range and derives the final $M/64516$ infinity-norm error.
- **3 points:** For MXFP4, justifies the power-of-two scale bound $|x_{b,i}/\alpha|\le1.859375$, justifies the nearest-rounding bound from the stated grid, and handles both normal and clipped first-pass values to obtain $\|r\|_\infty\le\alpha/8$.
- **3 points:** Handles both normal and clipped second-pass MXFP4 values after showing $|r_i/\beta|\le2$, and derives the blockwise $\alpha/64$ bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A brief observation that the grid spacing is $0.25$ and nearest rounding has error at most half that spacing is sufficient justification of the in-range bound. A unified estimate covering rounding and clipping is acceptable in place of explicit case splits. Deduct for theorem-critical gaps, especially failure to cover clipping cases or failure to propagate the first residual bound. Either nearest choice at a rounding tie is valid; no input-distribution or clipping-proportion assumption is required.
