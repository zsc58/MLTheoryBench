# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the fixed-design ridge least-squares problem, the same fixed regular nondegenerate selection for original and replaced responses, and the trained quantities $G$, residual curvature, $H$, and $d_{\rm eff}$. Handles the stated moment assumptions sufficiently to justify the expectations used.
- **4 points:** Proves the averaged prediction-stability bound with the trace effective dimension and the stated constant $4/(\alpha n)$, or a stronger bound implying it. For the reference route, derives the response derivative through $H^{-1}$, verifies applicability of the product Brascamp-Lieb inequality, justifies replace-one centering, and performs the trace calculation with every factor of $n$ accounted for. A logically complete alternative route earns equivalent credit.
- **3 points:** Establishes the fresh-response/replace-one identity for the fixed-design experiment and rigorously obtains the square-root generalization bound. For the reference route, expands the square-loss difference with residual $h_i(Y)-Y_i$ and prediction change $h_i(Y^{(i)})-h_i(Y)$, then applies Cauchy-Schwarz in probability and across indices to obtain $\sqrt{2\,\mathbb E\widehat L\,S}+S/2$, where $S$ is averaged squared prediction instability.
- **1 point:** Applies Young's inequality correctly to obtain the stated bound for every $\eta>0$.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental notation, presentation choices, or exact route. In particular, a valid sharper stability bound is acceptable if it implies all requested conclusions.

For a proof following the reference route, an unsupported sensitivity formula, an unverified application of the variance inequality, or a missing effective-dimension trace calculation is a theorem-critical gap unless replaced by another justified argument. Merely quoting the desired stability or generalization statement is not a proof.

The two fitted predictions share the unreplaced coordinates and need not be unconditionally independent. Likewise, the residual and prediction change need not be independent. The replace-one identity must use a fresh response independent of the entire training vector and the same selection map in both samples. Coordinate laws need not be identical or centered.

The product Brascamp-Lieb inequality is permissible standard background when stated in an applicable form and its hypotheses are checked. Its proof need not be reproduced. The square-loss exchangeability identity and quadratic calculation can be justified directly as in the reference proof; they should not be replaced by an unspecified paper-specific theorem.

Do not impose Gaussian noise, zero residual curvature, $\|\Delta_Y\|_{\rm op}<\lambda$, invertibility of $G_Y$, a uniform Hessian lower bound, or $\lambda>0$. Global continuous second differentiability is not required beyond the task's selected-point differentiability. The proof must not exclude zero training loss or zero effective dimension by dividing by either quantity.
