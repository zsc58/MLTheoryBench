# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Pointwise optimizer.** Establishes maximality of the normalized positive-part density for \(p>1\), including its zero-density region and mass multiplier, by a valid concavity or KKT argument; handles \(p=1\) using the Gibbs/KL identity. Merely naming KKT or Gibbs without justifying the maximizing inequality receives limited credit.
- **4 points: Monotone policy improvement.** Applies regime-switching Itô calculus to the old value along the updated projected dynamics, identifies the drift after adding the updated running payoff as the nonnegative difference of pointwise objectives, and passes from stopped expectations to values. Accounts for Brownian and compensated jump martingales, retains \(J\) at preterminal stopping times, and supplies moment and integrability justification.
- **3 points: Fixed-point optimality.** Uses the fixed point's pointwise maximizing property and its fixed-policy equation to obtain the verification inequality for every admissible competitor, then uses a valid localized Itô and limiting argument to establish domination of every competitor's value.

# Evaluator Notes

Accept any complete alternative proof under the stated assumptions. The optimizer formulas require derivatives only for \(t<T\); policy values at \(T\) do not affect the claim. Do not require projected coefficients to be Lipschitz or require a separate HJB uniqueness theorem. A proof of monotonicity alone earns no fixed-point points; an independently valid fixed-point verification can earn those points despite a localized error in the improvement argument. Omitted localization or expectation-limit justification is material when the passage to values remains unsupported.
