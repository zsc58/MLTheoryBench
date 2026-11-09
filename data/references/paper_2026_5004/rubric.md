# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the fixed finite-feature setup and the supplied posterior-variance and logarithmic-ratio definitions. Justifies the inverses and positive logarithm arguments using the joint Gram structure and positive observation noise, or an equivalent valid argument. The public formulas are definitions for this task: do not require their rederivation from GP conditioning or Gaussian entropy.
- **2 points:** Obtains the uniform high-noise expansion for the gain criterion, including the coefficient \(a(S)/(2k_{**}\tau)\) and an \(O(\tau^{-2})\) remainder. An inverse expansion followed by a justified logarithm expansion is sufficient; equivalent estimates are accepted.
- **4 points:** Derives the matching loss expansion with the same coefficient and a uniform \(O(\tau^{-2})\) remainder. For the reference route, establish the leave-subset-out identity by block algebra and control its asymptotic factors; merely naming block inversion does not establish an otherwise unproved identity. A complete alternative derivation receives the same credit. In particular, directly expanding \(v(D\setminus S)\) and \(v(D)\), using \(\|b_D\|^2-\|b_{D\setminus S}\|^2=\|b_S\|^2\), and controlling the resulting logarithm is sufficient without a leave-subset-out identity.
- **2 points:** Uses a common uniform remainder bound and, when competitors exist, a strictly positive leading-term gap to obtain a finite threshold beyond which both maximizers are uniquely \(S^\dagger\). The reasoning must cover a singleton subset family without taking a maximum over an empty competitor set.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular matrix identity. Here \(\tau=\sigma^2\), so \(O(\tau^{-2})=O(\sigma^{-4})\). Constants and thresholds may depend on the fixed dataset, query, features, and subset size, but not on \(S\) or the varying noise level. Finiteness can make finitely many valid bounds uniform; it does not replace the individual asymptotic estimates.

The allowed cases include \(D=\varnothing\), \(M=0\), \(M=|D|\), singular Gram matrices, and zero kernel correlations. A proof may cover these through valid conventions or direct observations; separate lengthy case discussions are unnecessary. Do not demand a positive gap when the subset family has only one element, and do not demand a maximizer conclusion when the leading coefficient lacks a unique maximizer.

Propagate a missing variance identity or expansion only when the corresponding loss conclusion is unsupported. Score later maximizer reasoning independently when its premises are correctly established. Do not penalize omission of an identity that a valid alternative proof does not use. An eventual strict inequality must support all \(\sigma^2\ge\sigma_0^2\); a threshold may always be chosen strictly above any intermediate critical value.
