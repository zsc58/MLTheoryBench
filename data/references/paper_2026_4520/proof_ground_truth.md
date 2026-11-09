# Reference Proof

## Proof obligations

The proof must establish uniform deviations for fixed classes that include all candidate predictors, compare the estimator with every member of F, prove that the MCR estimator is a pooled empirical minimizer, and calculate the probability for each of the two requested guarantees separately. No population minimizer is assumed to exist.

Write N=n+m and B=B_g B_xz. Let pi_X be the feature marginal. For s=n or N, put pi_s^f=(1/s)sum_{i=1}^s delta_(X_i,f(X_i)) and D_s(f)=d_G(pi_l,pi_s^f). Thus D_n is the labeled criterion and D_N is the pooled criterion. Also put D_u(f)=d_G(pi_l,pi_u^f).

## 1. Uniform-deviation inequality and its hypotheses

We use the following standard empirical Rademacher inequality in its oscillation form. Let T_1,...,T_s be independent observations with law P, and let C be a fixed measurable class such that |c(t)-c(t')|<=b for every c in C and every t,t'. Then, with probability at least 1-eta,

sup_{c in C}(Pc-P_s c) <= 2 Rhat_s(C)+3b sqrt(log(1/eta)/(2s)).

Here Rhat_s(C)=E_sigma sup_{c in C}(1/s)sum_i sigma_i c(T_i). For a symmetric class, the left side equals sup_{c in C}|Pc-P_s c|.

For completeness, the oscillation formulation follows by the usual symmetrization argument and the bounded-differences inequality. The latter says that if changing input i changes an integrable statistic Q by at most c_i, then P(Q-EQ>=t)<=exp(-2t^2/sum_i c_i^2). Define A_C(S)=sup_c(Pc-P_s c) and r_C(S)=Rhat_s(C). An independent ghost sample S' gives

E A_C(S) <= E sup_c(P_s'c-P_s c)
= E_{S,S',sigma} sup_c (1/s)sum_i sigma_i(c(T_i')-c(T_i))
<= 2 E r_C(S).

Replacing one observation changes A_C by at most b/s and r_C by at most b/s. Thus Q=A_C-2r_C has bounded differences 3b/s and expectation at most zero. Applying the displayed concentration inequality proves the stated deviation bound, including its exact logarithm and constant.

Each g in G has oscillation at most B on X x Z, by the diameter and Lipschitz assumptions. Each h(x)=g(x,f(x)) has oscillation at most B as well, because f takes values in Z. Both G and H are symmetric, and H includes every f in F. The class H is fixed even though the trained predictors are sample-dependent.

There is no need to assume |g|<=B. To justify integrability in the preceding argument, fix a joint-domain point w_0. If sup_g|g(w_0)| is finite, the common oscillation bound supplies a finite envelope for G and H, and all the statistics above are integrable. If sup_g|g(w_0)| is infinite, symmetry makes sup_g g(w_0) infinite. On the sign vector with all signs positive, the Rademacher supremum is then infinite on every nonempty sample; on every other sign vector it is nonnegative by symmetry. Thus Rhat_n(G)=+infinity for every sample, and both requested inequalities are immediate. We may therefore work in the finite-envelope case without adding a public assumption.

Define

A=sup_{g in G}|pi g-pi_l g|,
B_s=sup_{f in F,g in G}|pi^f g-pi_s^f g|
    =sup_{h in H}|pi_X h-(1/s)sum_{i=1}^s h(X_i)|.

The deviation inequality gives events E_G and E_s, each of probability at least 1-delta, on which respectively

A <= 2 Rhat_n(G)+Delta/(2 sqrt(n)),
B_s <= 2 Rhat_s(H)+Delta/(2 sqrt(s)).

The second assertion is used with s=n for the vanilla guarantee and with s=N for the MCR guarantee. Independence between these events is not required.

## 2. Excess-risk comparison against arbitrary predictors

For every f in F, the elementary inequality |sup a-sup b|<=sup|a-b|, together with the triangle inequality for real numbers, yields

|R(f)-D_s(f)| <= A+B_s.

If f_hat minimizes D_s over F, then, for every u in F,

R(f_hat)-R(u)
= [R(f_hat)-D_s(f_hat)]
  +[D_s(f_hat)-D_s(u)]
  +[D_s(u)-R(u)]
<= 2A+2B_s.

The middle term is nonpositive by empirical optimality. In particular, u need not interpolate. Taking the supremum over u on the left gives

R(f_hat)-inf_{u in F}R(u) <= 2A+2B_s.

This step does not require attainment of the population infimum. The risk is finite because each discriminator has oscillation at most B, so d_G between any two probability measures on the joint domain is at most B.

## 3. Vanilla estimator

Since f_V belongs to F1=F2, it minimizes D_n. On E_G intersect E_n, the preceding comparison gives

R(f_V)-inf_{u in F}R(u)
<= 4 Rhat_n(G)+4 Rhat_n(H)+2Delta/sqrt(n).

The union bound gives P(E_G intersect E_n)>=1-2delta. The perfect-training assumptions hold almost surely under the stated sampling experiment, so their use introduces no additional probability loss and no conditioning of the data law.

## 4. Pooled-minimizer inclusion

For every f in F2=F*, interpolation gives pi_l^f=pi_l. Consequently,

pi_ul^f=(n/N)pi_l+(m/N)pi_u^f,
D_N(f)=(m/N)D_u(f).

These are private proof identities, not public assumptions.

Choose f_0 in F* intersect F4, whose existence is assumed. Since f_M belongs to F2 intersect F3, both f_M and f_0 interpolate, and global unlabeled optimality gives D_u(f_M)<=D_u(f_0). Therefore

D_N(f_M)=(m/N)D_u(f_M)
<= (m/N)D_u(f_0)=D_N(f_0)=inf_{f in F}D_N(f).

It follows that f_M belongs to F4. This proves the required inclusion without any additional minimizer-existence hypothesis.

## 5. MCR estimator and probability accounting

Apply the comparison from Section 2 to f_M with s=N. On E_G intersect E_N,

R(f_M)-inf_{u in F}R(u)
<= 4 Rhat_n(G)+4 Rhat_N(H)
   +Delta(1/sqrt(n)+1/sqrt(N)).

Again P(E_G intersect E_N)>=1-2delta. This is the second requested probability guarantee. The two claims are separate: this argument does not assert that E_G, E_n, and E_N have a common intersection of probability at least 1-2delta.

The argument also covers B=0: all discriminator differences between probability measures vanish, so every risk is zero. Positive n and m ensure that every empirical measure is defined. For delta>=1/2 the stated probability lower bound is nonpositive but still valid. No monotonicity of the realized empirical complexities across the two sample sizes is asserted.
