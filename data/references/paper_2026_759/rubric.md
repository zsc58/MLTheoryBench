# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Fixes an arbitrary time/prefix, defines omega=p^alpha/q, and proves its conditional mean is the proposal-independent Z=sum_v p(v)^alpha.
2. **(3 points)** Derives the unique minimizer of the conditional second moment over support-compatible proposals, including zero-probability tokens or an equivalent argument, obtaining q*=p^alpha/Z.
3. **(3 points)** Verifies that q* makes omega constant on the support, so conditional variance is zero and globally minimal, and establishes uniqueness.
4. **(2 points)** Derives the logits/temperature representation q*=softmax(ell/tau) with tau=1/alpha.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award credit for mathematically established achievements, not for naming a method.
