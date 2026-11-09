# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Reference-Proof Status

The previously disclosed private proof gap is closed. The reference now proves the Gaussian noise-sensitivity/surface-area inequality using the distance-based Lipschitz approximation and Gaussian-rotation derivation supplied in the downstream report and independently checked during audit. The original source states and cites that inequality but does not contain this derivation. No additional public hypothesis has been introduced.

# Core Steps

1. **Hermite smoothing and truncation (3 points):** Defines or correctly uses the Ornstein-Uhlenbeck smoothing, its Hermite eigenvalues, and Parseval to construct a degree-at-most-d polynomial whose truncation error is at most rho^(d+1) in L1. The Gaussian Hermite basis theorem is acceptable standard independent background. The eigenvalue calculation and extension to L2 are supplied in the reference proof.
2. **Smoothing error identity (2 points):** Proves the Boolean-function identity ||f-T_rho f||_1=2GNS_{1-rho}(f), including the correlated Gaussian coupling. Conditional on X, the difference of the two Boolean values has a fixed sign, justifying equality rather than merely an inequality.
3. **Surface-area control (2 points):** Establishes the dimension-free bound GNS_{1-rho}(f)<=sqrt(pi)*sqrt(1-rho)*GSA(f), or a valid bound with another universal constant sufficient for the target. The relevant domain consists of Borel Boolean functions whose positive set has Gaussian-null boundary and an existing finite outer Gaussian surface area. The reference proves this by setting h_r=max(0,1-dist(.,K)/r), bounding E||grad h_r|| by gamma_n(K^{(r)}\K)/r, integrating along a Gaussian rotation, and passing to the limit using the boundary-null and surface-area hypotheses. Rademacher's theorem is acceptable standard independent background when its Lipschitz hypothesis and the passage to Gaussian-almost-everywhere differentiability are checked. The rotation argument must justify the almost-everywhere chain rule and exploit independence of position and velocity to avoid a dimension factor. A different valid derivation or independently justified applicable result is equally acceptable. A bare specialized citation is not, by itself, closure of this proof obligation.
4. **Parameter balancing and degree conclusion (3 points):** Chooses rho and a nonnegative integer d so both errors are at most epsilon/2, handles zero and small positive surface area using a constant polynomial, handles infinite surface area by polynomial density, and derives d=O(GSA(f)^2*log(1/epsilon)/epsilon^2). In the positive finite case one may choose delta=min{1,epsilon^2/(16*pi*GSA(f)^2)} and rho=1-delta. When delta<1, d=ceil(log(2/epsilon)/delta)-1 satisfies d<=log(2/epsilon)/delta; when delta=1, d=0. A valid alternative balance is equally acceptable.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or numerical constants. Treat omission of the parameter balance or an unsupported truncation estimate as theorem-critical. Likewise, do not label a proof fully closed when its needed surface-area control remains unsupported, unless a valid alternative argument avoids that dependency. Evaluate any proposed derivation or independently justified application on its mathematical merits rather than by agreement with the reference presentation. Readily repairable omissions in routine endpoint handling should be distinguished from missing substantive estimates. The formerly incomplete private GT was not evidence that the public theorem was false and must not be attributed to a solver; its missing estimate is now supplied explicitly.
