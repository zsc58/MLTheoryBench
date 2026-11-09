# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the oracle update using Bayes' rule and obtains the multiplicative ratio \(\pi_{t+1}(z)/\pi_t(z)=\mathbb E_{q(\cdot\mid z)}[m^\star/m_t]\). Justifies that the posterior is defined \(m^\star\)-almost everywhere and the updated prior is normalized, using the absolute continuity supplied by finite current prior KL.
- **4 points:** Derives the prior-KL descent inequality \(D_t-D_{t+1}\ge A_t\) by expressing the KL difference, applying Jensen's inequality, and identifying the induced marginal law as \(m^\star\), or by a complete equivalent argument. Justifies finiteness/integrability sufficiently to avoid undefined KL subtraction. Merely naming Jensen or an EM argument without a derivation is insufficient.
- **3 points:** Uses \(\lambda\)-strong prior-identifiability to show \(D_{t+1}\le(1-\lambda)D_t\), and correctly iterates this inequality from finite \(D_0\) to obtain the geometric prior bound for every \(t\ge0\). The argument must cover \(\lambda=1\), \(t=0\), and \(D_0=0\), whether explicitly or through a recurrence and conventions that already include them.
- **1 point:** Applies KL data processing through the common simulator kernel to deduce the stated geometric bound for \(A_t=\mathrm{KL}(m^\star\|m_t)\).

# Evaluator Notes

Accept a complete valid alternative proof and allocate the core-step credit to its corresponding mathematical achievements. Do not require the reference proof's incidental presentation choices, auxiliary notation, or particular negative-part estimate. The two geometric conclusions, a valid descent or equivalent contraction argument, and the identifiability-to-contraction step are theorem-critical.

Finite initial KL is sufficient; do not demand strictly positive densities everywhere, bounded likelihood ratios, finite separate entropies, or additional moment assumptions. Posterior versions on null sets do not affect the update once the relevant absolute continuity is established. A routine omitted integrability justification is a readily repairable omission, not evidence that the theorem is false; an argument that actually subtracts two infinite quantities is not a valid descent proof.
