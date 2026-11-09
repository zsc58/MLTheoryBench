# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Posterior-sampling reduction (2 points).** Establish conditional equality of the true and sampled GP laws, with fresh posterior randomization and the independent initial state, and derive the sampled-versus-true value representation of Bayesian regret. Establish the exchangeability identity before inserting any full-trajectory event.
2. **Unbounded-state confinement (2 points).** Justify measurable/separable supremum bounds under the Holder kernel assumption, including correct vector Gaussian mean factors. Prove the logarithmic radius bound by a first-exit argument, give admissible recursive radii, verify their domination by the displayed R using the T condition, and control the complement probability. Do not treat the uncentered posterior process as conditionally satisfying a zero-mean prior supremum tail.
3. **Bellman-to-dynamics reduction (2 points).** Telescope the Bellman equations along the true trajectory; account for action randomization as well as transition randomness. Control event-weighted total martingale sums without assuming the event is predictable. Derive the Gaussian KL/Pinsker bound, or a valid equivalent, reducing value error to cumulative dynamics discrepancy. Bounded rewards must also control the complement event.
4. **Chaining and information-gain estimation (3 points).** Derive the cumulative sampled/true GP error bound on the confined ball using a finite cover, conditional concentration, Holder interpolation, valid observed-transition posterior-variance control, and chaining. Preserve the confinement indicator in truncation; never move it through a conditional expectation without measurability. Posterior regression contains H-1 responses per episode, whereas gamma_T contains all H visited inputs. Distinguish any episode-representative information gain from the public trajectory quantity, justify its needed asymptotic bound at the growing radius, and respect the fixed-model limit. Marginal equality of GP laws may bound prior-marginal suprema, but does not establish joint equality at dependent visited inputs. Merely naming chaining, elliptical potential, or information gain is insufficient.
5. **Combination and final rate (1 point).** Combine the event and complement bounds, insert the explicit radii and T condition, and obtain the stated fixed-model Bayesian-regret order. Justify absorption of additive terms, for example by proving gamma_T is eventually bounded below by a positive constant. Handle H=1 and make the discretization choice admissible rather than assuming its asymptotic formula is valid for every small T.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental notation, exact auxiliary quantities, or numerical slack choices. The central confinement and estimation arguments must be mathematically justified, but an alternative valid method need not reproduce the reference's intermediate lemmas.

The target is the asymptotic order for the fixed finite-horizon model. Do not require a joint uniform-in-H estimation lemma or a joint limit with H=H(T), neither of which follows from the source's representative-information-gain simplification. Conversely, merely calling a horizon-dependent expression lower order without specifying and checking the fixed-model limit does not close the argument.

Do not award a completed estimation step for a bound that uses responses at terminal inputs, for an unjustified indicator/tower identity, or for a sample-size-dependent cutoff inside a limit. A correct unsimplified variance bound is useful partial progress but must still be combined with a justified asymptotic estimate. Do not import source derivation errors into scoring expectations.
