# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the normalized terminal-tilted optimizer, verifies preservation of the prescribed initial law, and derives the optimal off-diagonal rate formula. A conditional-kernel calculation must use the starting-time normalizer.
- **2 points:** Establishes the backward dynamics of the value transform and its terminal condition, with the correct generator orientation and a valid terminal-value interpretation under every starting law.
- **4 points:** Rigorously proves the conditional-expectation adjoint representation. For the Dynkin route, verifies cancellation for exp(V_t(r)), not for the full exponential value difference; identifies the adjoint by its backward equation and terminal condition; and obtains its conditional expectation. An equally complete proof by conditional terminal tilting receives full credit.
- **2 points:** Proves the analytic adjoint formula through the base transition kernel or an equivalent backward-system verification, including all starting states and the terminal condition.

# Evaluator Notes

Accept a complete valid alternative proof and any valid reordering of the steps. Do not require the reference proof's incidental presentation choices or require Dynkin's formula when conditioning gives a complete proof. Allocate the core-step credit by the mathematical obligations discharged, not by whether a solver follows the reference sequence.

For f_t(r;y)=exp(-V_t(y)+V_t(r)), the drift is generally
\[
(\partial_t+L_t^\star)f_t(r;y)
=-\sum_z u_t^{\rm base}(z,y)f_t(r;z),
\]
not zero. The zero-drift function used in the reference proof is exp(V_t(r)). Treat an asserted zero drift for the full value-difference function as a major mathematical error unless it is independently corrected. A terminal-only expectation of exp(-g(y)+g(X_1)) is not generally the time-t value ratio.

Equality of expectations does not identify samplewise backward ODEs. The adjoint must be verified by solving or checking its terminal-value system, or by another valid argument. Treat an asserted adjoint representation without such justification as a major gap.

With U(z,y)=u(z,y) and P(z,y)=p(z|y), column terminal functions evolve using P transposed. Do not accept exp(integral U) as a general solution for time-dependent generators without a valid commutativity argument or an explicitly ordered propagator. Componentwise calculations avoid this issue.

The model specifies ordinary jump intensities on compact intervals and X_{1-}=X_1 almost surely under every starting law. These are the relevant grounds for using the rate generator and passing to the terminal observation. Right infinitesimal rates, nonexplosion, or a well-posed adjoint ODE alone do not exclude an additional terminal reset. A proof using bounded convergence at time 1 must have X_s converging to X_1, not merely to X_{1-}. A succinct invocation of the explicit terminal assumption suffices; do not require a redundant lengthy argument. The terminal tilt preserves this property by absolute continuity. If Dynkin's formula is used under the tilted process, its rate-generated nature must be justified, for example by the conditional tilted law and the resulting jump intensities.

Check that the proof does not divide by a zero transition rate, condition on a zero-probability event, or confuse an arbitrary intensity version with an infinitesimal rate. The analytic adjoint must cover states unreachable under the prescribed initial law. At time 1, the adjoint identity is literal; rate identities use the stated finite-left-limit convention on positive-terminal-mass states. No forward transition after time 1 is required. Finite-state boundedness of the exponential quantities supplies the relevant expectation bounds, but global boundedness or global integrability of all rates must not be silently assumed.
