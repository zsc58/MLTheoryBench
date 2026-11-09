# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the softmax gradient and the correct logit/probability dynamics, and correctly distinguishes the two flows. In the orthonormal case the probability equation is p_y'=p_y[p_y A_y-sum_z p_z^2 A_z]. Handles positivity and the relevant hitting-time definitions consistently.
- **3 points:** Establishes the ground-truth attraction and escape argument, or a valid alternative yielding the same explicit lower bound. For the reference route, proves monotonicity through the two reward thresholds, obtains q(t_gamma)<=m_0^2 gamma/(8 A_star(0)), derives 1-m(t_gamma)<=(1+8 Delta_1)gamma/[8 Delta_1 r_G(y_med)], and integrates the gradient/complementary-mass bounds with the positive-denominator restriction and its complementary case. These concentration bounds are endpoint statements, not assertions valid from time zero.
- **3 points:** Establishes a positive quadratic growth lower bound for optimal probability on a correctly specified pre-target interval, integrates it to obtain the displayed inverse-linear upper bound U_epsilon, and proves the probability guarantee for every t>=U_epsilon. A valid reference route uses the first proxy-objective hitting time sigma, proves t_epsilon^{no-med}<=sigma<=U_epsilon, and uses monotonicity of the proxy objective thereafter.
- **2 points:** Proves the arbitrarily large time separation with rewards, features, output set, and epsilon fixed. Controls the apparently initialization-dependent proxy coefficient, for example through r_P(y_star)-V_{r_P}(theta_0)=(Delta_1+Delta_2)(1-q_0), and compares q_0^(-14/13) with q_0^(-1). Handles an infinite ground-truth hitting time consistently.

# Evaluator Notes

Accept any complete valid alternative proof, including stronger intermediate estimates that imply the requested constants. Do not require the reference proof's presentation, threshold notation, or exact derivative estimates.

Theorem-critical missing differential inequalities, unsupported attraction claims, or an unexplained assertion of the explicit lower-bound constant are major gaps. A proof must not replace the Euclidean softmax-gradient dynamics by the replicator equation p_y'=p_y A_y.

The required probability guarantee starts at U_epsilon. It does not start at the first ground-truth-reward hitting time on the proxy trajectory. Ground-truth target attainment does not imply proxy target attainment or the stated optimal-probability threshold. At the ground-truth hitting time, the positive mediocre mass makes the latter inference false.

For the escape argument, substituting an upper bound into an integral preserves an inequality, not equality. Treat an isolated equality-sign typo as locally repairable when the intended valid inequality and all ensuing conclusions are clear; do not treat a genuinely unsupported equality or missing comparison as proof closure.

The reference proof has no remaining unresolved obligation and requires no unproved paper-specific dependency.
