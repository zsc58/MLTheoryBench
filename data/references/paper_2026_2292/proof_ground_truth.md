# Reference Proof

## Obligations and standard background

The obligations are: population projection and centering; empirical calibration; the isotonic L2 rate; labeled and unlabeled remainder bounds; the influence expansion; variance domination and the two efficiency cases; and the conditional-mean post-processing rate and equivalence. All are proved below.

Write T=m(X), let Q be its law, write P=P_0, and put P_X=P_{0,X}. Population integrals of fitted functions hold the labeled training sample fixed and integrate a fresh observation. Set S_n=m_n^* and H_n=widehat m_0.

We use the following standard independent empirical-process facts, indexed privately by theory_024. A class of monotone functions with a fixed uniform bound has log L2 bracketing entropy at most A/epsilon under any probability law on an ordered real domain. A class with fixed uniform and total-variation bounds has the same entropy order, by decomposition into two bounded monotone functions. Fixed finite sums and bounded Lipschitz products preserve this order. Thus the bracketing integral to radius r is at most C sqrt(r).

The local maximal inequality for a bounded class, or its Bernstein-bracketing version, gives

    E* sup_{h in H_r} |(P_n-P)h|
      <= C { n^(-1/2) r^(1/2) + n^(-1) r^(-1) },                 (A)

when the localized class has L2 or Bernstein radius at most a fixed multiple of r, fixed envelope or Bernstein scale, and log bracketing entropy at most A/epsilon. Here r lies in a fixed bounded range; constants do not depend on n or r. We retain the second term. At r >= n^(-1/3), it is no larger than the first term, up to constants.

Here are the checks for unbounded outcome multipliers. The public conditional exponential-moment assumption implies E[|Y|^k|T] <= k! B^k for a fixed B, since eta is bounded. If d is uniformly bounded, then

    E[ |d(T)(Y-a(T))|^k ]
      <= k! B_1^k ||d||_infinity^(k-2) E[d(T)^2]

for every uniformly bounded a, with constants depending only on the deterministic bounds. This supplies a fixed Bernstein scale and Bernstein radius bounded by a constant times ||d||_2. Bracket widths of products of bounded coefficient functions and Y are bounded by a constant times (|Y|+1) times the sum of the coefficient bracket widths. The same conditional moment calculation transfers the L2 brackets to Bernstein brackets. Consequently (A) applies to the excess-loss and calibration-product classes below. This checks the multiplier hypotheses rather than inferring them merely from the name of a tail condition.

For envelope localization, fix an arbitrary epsilon>0. Boundedness in probability supplies a deterministic C and n_0 with Pr(A_{n,C}) >= 1-epsilon for n>=n_0, where A_{n,C}={sup_x|S_n(x)|<=C}. Enlarge C to dominate the bound on eta. Use unconditional empirical-process bounds for deterministic C-bounded classes and intersect their conclusions with A_{n,C}; do not condition the labeled empirical process on this event. Finally let epsilon be arbitrary. This, not the outcome-tail condition, removes envelope localization.

## 1. Population projection and empirical calibration

The square-integrable nondecreasing functions of T form a closed convex cone in L2(Q), interpreted modulo Q-null sets. Conditional-mean orthogonality gives

    E[(Y-f(T))^2]
      = E[(Y-eta(T))^2] + E[(eta(T)-f(T))^2].

Therefore f_0 is the projection of eta onto this cone. Clipping a candidate to the range bound of eta preserves monotonicity and cannot increase the second term. We can thus choose f_0 bounded by that same constant. For every admissible u,

    P[(eta(T)-m_0)(u-m_0)] <= 0.                                (B)

The cone is closed under arbitrary additive shifts. Differentiating the population risk along m_0+c at c=0 gives

    P(Y-m_0)=0,   P_X m_0=psi_0.                               (C)

For the empirical fit, order the distinct observed T values and group equal fitted values into maximal consecutive groups. A sufficiently small positive or negative shift of one such group's fitted value remains feasible. The derivative of the squared loss therefore vanishes on each group, so its residual sum is zero. This also handles ties in T and the case of only one fitted group. Consequently, pathwise,

    P_n^L[h(S_n)(Y-S_n)]=0                                    (D)

for every h finite at the observed fitted values. Off-sample choices of the monotone minimizer do not affect this statement. Taking h=1 shows that the pooled plug-in estimator equals widehat psi(S_n).

## 2. Isotonic L2 rate

On A_{n,C}, put g=S_n-m_0 and consider the deterministic class of differences u-m_0 with u a C-bounded nondecreasing function of T. For a generic difference g define

    ell_g=(Y-m_0-g)^2-(Y-m_0)^2
         =g^2-2(Y-m_0)g.

Empirical minimization gives P_n^L ell_g<=0 for the fitted difference. By (B),

    P ell_g=||g||_2^2-2P[(eta-m_0)g] >= ||g||_2^2.

Hence the fitted difference satisfies

    ||g||_2^2 <= |(P_n^L-P)ell_g|.                            (E)

For differences with ||g||_2<=r, boundedness and the conditional moment check preceding (A) give a Bernstein radius O(r). The entropy is O(1/epsilon), not O(r/epsilon). Apply (A).

Let a_n=n^(-1/3). On the shell 2^s a_n<=||g||_2<2^(s+1)a_n, (E) implies that the supremum of the excess-loss empirical process over radius 2^(s+1)a_n is at least 2^(2s)a_n^2. Markov's inequality and (A) bound the probability of that shell intersected with A_{n,C} by

    C {2^(-3s/2)+2^(-3s)}.

Only radii up to the deterministic diameter of the class are needed. Summing over s>=S and then letting S increase proves ||S_n-m_0||_2=O_p(n^(-1/3)) on the envelope event. Removing that event as described above proves

    ||S_n-m_0||_2^2=O_p(n^(-2/3)).                            (F)

## 3. Empirical-process remainders and influence expansion

For any fixed K, the bounded difference class localized at K n^(-1/3) satisfies (A). Its labeled empirical-process supremum is O_p(n^(-2/3)). By (F), first choose K to contain the random difference with arbitrarily high probability. Thus

    (P_n^L-P_X)(S_n-m_0)=O_p(n^(-2/3)).                       (G)

Conditional on the labeled sample, S_n-m_0 is fixed and the unlabeled observations are independent with law P_X. Its conditional empirical-mean variance is at most ||S_n-m_0||_2^2/N. Conditional Chebyshev, localized also on (F), gives

    (P_N^U-P_X)(S_n-m_0)=O_p(n^(-1/3)N^(-1/2)).              (H)

Direct subtraction of the AIPW formulas gives the exact identity

    widehat psi(S_n)-widehat psi(m_0)
      =(1-rho_n)(P_N^U-P_n^L)(S_n-m_0).                      (I)

The population integrals cancel in the difference of empirical measures, even though the fitted function is random. Combining (C), (G), (H), and (I) yields

    widehat psi_iso-psi_0
      =rho_n(P_n^L-P){m_0-psi_0+rho_n^(-1)(Y-m_0)}
       +(1-rho_n)(P_N^U-P_X){m_0-psi_0}
       +O_p(n^(-2/3))+O_p(n^(-1/3)N^(-1/2)).

Because n and N are both of order M, both remainder orders are o_p(M^(-1/2)). Replacing rho_n^(-1) by rho_0^(-1) in the leading labeled term changes it by

    (1-rho_n/rho_0)(P_n^L-P)(Y-m_0)=o_p(M^(-1/2)).

This replacement is asserted only at first-order precision, not at the sharper displayed remainder precision. Equation (C) makes each limiting influence component mean zero. Finite second moments and the independent two-sample central limit theorem give asymptotic variance

    V(m_0)=rho_0 Var(D^L)+(1-rho_0)Var(D^U).

Zero variance is permitted; no studentization is requested.

## 4. Variance comparison and efficiency

For a fixed square-integrable g, let tilde g=g-P_Xg+psi_0. An additive shift cancels exactly in widehat psi(g), so its influence pair is obtained with tilde g. Write A=mu_0-psi_0, e=Y-mu_0, and b=tilde g-mu_0. Then E[b]=0, E[e|X]=0, and the labeled and unlabeled influence components are

    A+rho_0^(-1)e+(1-rho_0^(-1))b,    A+b.

In the weighted sum of their variances, the covariance of A and b cancels because rho_0(1-rho_0^(-1))+(1-rho_0)=0. All covariances with e vanish by conditional centering. Therefore

    V(g)=Var(mu_0)+rho_0^(-1)E Var(Y|X)
         +(1-rho_0)rho_0^(-1)E[(tilde g-mu_0)^2].             (J)

If g is a nondecreasing transform of m, so is tilde g. By population projection optimality and the conditional-mean squared-loss identity,

    E[(m_0-mu_0)^2] <= E[(tilde g-mu_0)^2].

Together with (C) and (J), this proves the asserted variance domination. Using the uncentered g on the right would not suffice.

To verify full efficiency, use the standard canonical-gradient characterization stated in theory_024. Scores of unrestricted joint-law submodels have the form a(X)+b(X,Y), with E[a]=0 and E[b|X]=0; their unlabeled marginal scores are a(X). In the weighted product L2 space, the pair

    (mu_0-psi_0+rho_0^(-1)(Y-mu_0), mu_0-psi_0)

has inner product with (a+b,a) equal to

    E[(mu_0-psi_0)a]+E[(Y-mu_0)b],

which is the derivative of E[Y] along that submodel. The pair belongs to the closure of the score space, by approximating its square-integrable components with bounded scores. It is thus the canonical gradient, whose squared norm is the unrestricted two-sample efficiency bound. This verifies efficiency, rather than deducing it solely from minimization over AIPW scores. If m_0=mu_0, the estimator has this pair and attains that bound.

The identical argument with covariate T instead of X gives the reduced-experiment canonical gradient with regression eta(T). If eta is nondecreasing Q-almost surely in the stated version sense, it belongs to the isotonic cone; the squared-loss identity then gives m_0=eta(T) almost surely. The influence pair therefore equals the reduced-experiment canonical gradient and attains its efficiency bound.

## 5. Variation control for the fitted-score oracle

All statements in this section hold with the labeled sample fixed and population expectations taken over a fresh draw. Write eta=u-v, where u and v are bounded nondecreasing functions whose total variations sum to the total variation of eta. Such a decomposition exists for a bounded finite-total-variation function on the real line.

For a nondecreasing fitted f_n, its nonempty level sets B_s={t:f_n(t)=s} are ordered intervals or singletons: if s<s', every point of B_s precedes every point of B_s'. On positive-Q-mass level sets, the oracle averages eta over B_s. On zero-mass level sets it uses eta at the representative specified in the task. Apply this averaging or evaluation separately to u and v. Each resulting function of s is nondecreasing, since all points in successive level sets are ordered; its range is contained in the range of its original Jordan component. This proves that their difference, the oracle function of s, has total variation at most that of eta and is bounded by its uniform bound. The convention also handles atomless singleton fibers; the at most countably many non-singleton zero-mass fibers have no effect on the population conditional expectation.

Composition with f_n preserves this variation bound. Hence H_n, as a function of T, belongs to a deterministic bounded-total-variation class, while S_n belongs to a deterministic bounded monotone class on A_{n,C}. This derives the specialized variation claim directly rather than invoking an external calibration theorem.

## 6. Calibration-error rate

Set Delta_n=H_n-S_n. Since it is a function of S_n, (D) gives

    P_n^L[Delta_n(Y-S_n)]=0.

Fresh-draw conditional expectation gives

    P[Delta_n(Y-S_n)]=P[Delta_n E(Y-S_n|S_n)]
                       =P[Delta_n^2].

Thus the exact identity is

    ||Delta_n||_2^2=(P-P_n^L)[Delta_n(Y-S_n)].                 (K)

On A_{n,C}, use the deterministic localized class

    {(h_1(T)-h_2(T))(Y-h_2(T)):
       h_1 bounded with the fixed variation bound,
       h_2 bounded and nondecreasing,
       ||h_1-h_2||_2<=r}.

The variation argument puts the fitted product in this class at radius ||Delta_n||_2. The conditional moment calculation gives Bernstein radius O(r). Jordan decomposition, finite products, and the bracket-width check preceding (A) give entropy O(1/epsilon). Applying (A) to (K), the same dyadic argument as in Section 2 bounds shell probabilities by C{2^(-3s/2)+2^(-3s)} at radii 2^s n^(-1/3). Consequently

    ||H_n-S_n||_2^2=O_p(n^(-2/3)).                           (L)

This derivation uses empirical orthogonality and the population inner-product identity; it does not assume that the oracle is an empirical least-squares minimizer.

## 7. Oracle equivalence and interpretation

The difference Delta_n is a bounded-total-variation function of T on A_{n,C}. Localize it by (L) and use the bounded version of (A), exactly as in Section 3. Independence and conditional Chebyshev handle the unlabeled sample. Thus

    (P_n^L-P_X)Delta_n=O_p(n^(-2/3)),
    (P_N^U-P_X)Delta_n=O_p(n^(-1/3)N^(-1/2)).

The exact AIPW difference is

    widehat psi(H_n)-widehat psi_iso
      =(1-rho_n)(P_N^U-P_n^L)Delta_n.

Its population means cancel exactly. The two process bounds prove that this difference is o_p(M^(-1/2)); there is no additional population inner-product term in this estimator difference.

For a fixed realization of the fitted map, H_n is the conditional-mean projection onto functions of its output. It minimizes fresh-draw prediction error and, after the irrelevant additive centering, the score-only AIPW variance functional. The displayed equivalence therefore establishes the stated absence of first-order gain relative to that oracle benchmark. It does not assert a comparison with arbitrary overfitted or irregular procedures. All requested conclusions are now established.
