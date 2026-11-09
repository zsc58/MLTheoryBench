# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly sets up the quadratic Gaussian dynamics, identifies \(\mu=N(0,P^{-1})\), proves or justifies invertibility of \(A=(D+Q)P\), and establishes moment control sufficient for the endpoint and oracle estimates, uniformly through \(\lfloor\eta^{-2}\rfloor\) steps. A uniform second-moment argument suffices; a full p-moment proof is also acceptable. The argument must handle the stated state-dependent conditional oracle bound. If using drift absorption, retain the higher stepsize orders or otherwise justify absorption; an arbitrary \(C\eta\|X_k\|^p\) cannot be absorbed merely by taking \(\eta\) small.
2. **3 points:** Explicitly solves the linear Poisson equation \(\mathcal L\phi=h\) with \(\phi(x)=-(A^{-1})^\top u\cdot x\), or supplies an equivalent direct linear-algebra argument, and derives \(V(h)=2u^\top A^{-1}D(A^{-1})^\top u\), including the reversible specialization when \(Q=0\).
3. **3 points:** Derives the correctly normalized telescoping decomposition, or an equivalent representation, and rigorously proves that the endpoint term and the centered stochastic-gradient term vanish. Uses adaptedness and conditional centering to justify orthogonality, and combines the state-dependent oracle bound with chain moment control. Handles the floor normalization exactly or proves its replacement error is negligible.
4. **2 points:** Identifies the Gaussian limit of the Brownian-increment term, verifies covariance convergence to \(V(h)\), and concludes convergence in distribution by Slutsky or an equivalent valid argument. A martingale CLT may be used with its hypotheses verified, but is unnecessary because the relevant coefficients are deterministic. The proof must also cover \(u=0\), either automatically or explicitly.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a proof of diffusion invariance beyond what the solution needs, a full p-moment estimate when second moments suffice, or an explicit invocation of a Poisson equation when direct summation performs the same calculation. The central requirements are the linear representation, correct normalization, and negligibility of stochastic-gradient noise under the actual state-dependent conditional moment assumption. Merely naming a Poisson equation, telescoping, or a martingale CLT without carrying out the necessary argument is insufficient.

The source's Markovian oracle and initialization assumptions are part of the public contract. A proof may validly establish the result under weaker assumptions; it need not use every stated assumption. Do not require independence between the oracle sum and the Gaussian sum for Slutsky's theorem. No general bounded-observable Poisson regularity result is needed for this task.
