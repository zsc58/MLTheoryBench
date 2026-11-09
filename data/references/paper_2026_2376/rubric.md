# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establish C0-vague subsequential compactness with subprobability limits and pass the kernel and weighted first-moment convolutions to a specified cluster limit. Justify the C0 test functions, include the zero-mass case, and normalize a nonzero limit without imposing moments on the probability measures.
2. **4 points:** Prove the block-separable field-identifiability bottleneck. For the reference route, derive the companion identities and the necessary convolution/Sobolev regularity; handle lambda_{1,alpha}=0 algebraically; and for lambda_{1,alpha}>0 define the Wronskian J_alpha, its divergence s_alpha, and the embedded full-space velocity. Derive J_alpha=-lambda_{1,alpha}b_alpha s_alpha, verify the hypotheses of local Sobolev renormalization for rho=exp(t/lambda_{1,alpha})s_alpha, and use integrable flux and compact cutoffs to prove that ||rho(t)||_1 is constant, forcing s_alpha and J_alpha to vanish. Establish fiberwise constancy of each block companion ratio, transfer it through that block's elliptic operator to the common ratio u_p/u_r, and only then deduce global constancy. Fix the convolution proportionality by integrating and justify deconvolution through nonvanishing factor Fourier transforms and finite-measure uniqueness.
3. **2 points:** Conclude that each cluster point is cp. Show u_p is a valid C0 overlap test and Z_p(p)>0; use the subsequential overlap limit, the full-sequence liminf hypothesis, and c<=1 to force c=1, including exclusion of c=0.
4. **2 points:** Use an arbitrary-subsequence argument to obtain full C0-vague convergence to p, then justify tightness by compactly supported cutoffs and convergence against every bounded continuous test function.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, notation, or order of independent steps. Standard independent results may be invoked with a correct relevant statement and verification of their hypotheses; reproducing the proof of the standard Sobolev renormalization theorem, compact-space probability compactness, or Fourier uniqueness is not required.

The paper-specific identifiability theorem is not a standard independent result and cannot simply be asserted as an unexplained black box. A complete derivation of the bottleneck, or a complete valid alternative, is required for its four points. Do not credit the incorrect inference that grad_alpha(Psi_{alpha,p}/Psi_{alpha,r})=0 for each alpha immediately makes every such ratio globally constant: the ratios are different functions, and the common smoothed-density ratio must be identified first. In the continuity-equation route it is the density's L1 norm, not the flux's L1 norm, that is conserved.

Do not require tightness or finite first moments as extra assumptions. Deduct substantially for unexplained identifiability, Wronskian vanishing, or scale fixing. The source sign convention is V_{p,q}=a_p-a_q; an explicitly consistent opposite sign within a proof is harmless for a hypothesis of convergence to zero.
