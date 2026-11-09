# Reference Proof

## Source audit and proof obligations

The model is deterministic and pointwise in the base input. The continuous coordinates do not provide a discrete paraphrase witness. The budget is positive, the proxy metric is positive definite, the readout direction is unit length, and all nonlinear evaluations take place inside an explicitly controlled part of the chart.

One source-local correction is applied to theory_007. The source fixes sign(0)=+1, but its strict boundary-crossing criterion is described as an iff criterion for prediction flips. At positive base margin, a negative base score changes its predicted label upon reaching zero. The corrected proof preserves the strict-crossing formula and treats that equality endpoint separately.

The theorem-critical obligations are: quadratic attainment and value; directional attainment and zero sensitivity; strict crossing and binary-label endpoints; positivity and spectral comparison for T; the target Taylor estimate and both nonlinear implications; and the proxy-distance estimate with justified feasible-set comparisons. All are derived below.

The independent finite-dimensional background used is the spectral theorem: a real symmetric matrix has an orthonormal eigenbasis, its Rayleigh quotient lies between its smallest and largest eigenvalues, and a positive-definite matrix has an invertible symmetric positive square root. Compact subsets of Euclidean space support maxima of continuous real functions. Euclidean Cauchy–Schwarz is used for vectors in the stated finite-dimensional spaces. These facts apply here because A and B are real symmetric Gram matrices and B is positive definite. The Taylor remainder is derived from the fundamental theorem of calculus rather than left as an external obligation.

## 1. Quadratic optimization

Suppress the fixed x-dependence. Since A=J^TJ, u^TAu=||Ju||_2^2 is nonnegative. Positive definiteness of B gives a smallest eigenvalue b_min>0, so every u in Q_eta satisfies ||u||_2<=eta/sqrt(b_min). Thus Q_eta is closed and bounded, hence compact, and the continuous objective attains its maximum.

Let H=B^{-1/2}AB^{-1/2}. This is symmetric positive semidefinite. With v=B^{1/2}u,

u^TAu=v^THv,  and  u^TBu=||v||_2^2.

The quotient defining Lambda is therefore the ordinary Rayleigh quotient of H, so Lambda=lambda_max(H). For ||v||_2<=eta,

v^THv<=Lambda ||v||_2^2<=eta^2 Lambda.

Choose a unit eigenvector v_max of H with eigenvalue Lambda and set u_max=eta B^{-1/2}v_max. Then

u_max^TBu_max=eta^2,
Au_max=Lambda Bu_max,
u_max^TAu_max=eta^2 Lambda.

This proves the value and attainment. If A=0, then H=0 and Lambda=0; every feasible point maximizes the objective, and the same construction using any unit v_max provides a boundary maximizer. If A is nonzero, the maximum is positive, and scaling shows that any maximizing point must lie on the boundary: an interior point with positive objective could be scaled outward to increase that objective.

## 2. Directional displacement and prediction endpoints

Fix a unit w and set a=J^Tw. Since B^{-1} is positive definite,

sigma_w=a^TB^{-1}a>=0.

For u in Q_eta, Cauchy–Schwarz gives

|a^Tu|=|(B^{-1/2}a)^T(B^{1/2}u)|
<=sqrt(a^TB^{-1}a) sqrt(u^TBu)
<=eta sqrt(sigma_w).

When sigma_w>0, the two vectors

u_+=eta B^{-1}J^Tw/sqrt(sigma_w),
u_-=-eta B^{-1}J^Tw/sqrt(sigma_w)

have B-norm eta and satisfy w^TJu_+=eta sqrt(sigma_w) and w^TJu_-=-eta sqrt(sigma_w). Hence they attain the two extreme displacements. If sigma_w=0, then B^{-1/2}a=0, so a=0 and every linearized displacement is zero.

Write d=eta sqrt(sigma_w). The full achievable score interval is [s_0-d,s_0+d]: the endpoints are attained, every feasible displacement is bounded by d, and scaling either endpoint optimizer fills the intervening values. In the zero-sensitivity case this interval is the singleton {s_0}.

Assume gamma_w=|s_0|>0, and put tau=sign(s_0), so tau is either +1 or -1. When sigma_w>0 the boundary-directed optimizer is

u_*=-tau eta B^{-1}J^Tw/sqrt(sigma_w),

and its signed linearized score is tau s_lin(u_*)=gamma_w-d. Thus an opposite nonzero score is attainable exactly when d>gamma_w. This proves the strict sign-reversal criterion.

For actual binary predictions, the endpoint matters. If s_0>0, a flip requires a negative score, so the condition is s_0-d<0, equivalently d>gamma_w. If s_0<0, a flip requires a nonnegative score because sign(0)=+1, so the condition is s_0+d>=0, equivalently d>=gamma_w. At d=gamma_w, zero is attainable but an opposite nonzero score is not; reaching zero flips a negative base prediction and does not flip a positive one. If sigma_w=0, then d=0<gamma_w, so neither kind of flip occurs.

## 3. The sensitivity matrix and its spectrum

Set C=JB^{-1/2}. Then T=CC^T is symmetric, and for every vector z,

z^TTz=||C^Tz||_2^2>=0.

Also C^TC=H. To verify the needed spectral correspondence directly, if Hv=lambda v with lambda>0, then Cv is nonzero and

T(Cv)=C(Hv)=lambda Cv.

Conversely, if Tz=lambda z with lambda>0, then C^Tz is nonzero and

H(C^Tz)=C^T(Tz)=lambda C^Tz.

Thus the positive eigenvalues on the two sides have the same possible values. If C=0, both matrices are zero; otherwise both have a positive largest eigenvalue, and those largest eigenvalues agree. Therefore

||T||_op=lambda_max(T)=lambda_max(H)=Lambda.

For a unit w, the symmetric-matrix Rayleigh bound gives sigma_w=w^TTw<=Lambda. A top eigenvector attains equality, although identifying this equality case is not an additional public proof obligation.

## 4. Target-map remainder and finite-radius flips

Fix 0<=t<=rho and u in Q_t. For every s in [0,1], su belongs to Q_t and hence to Q_rho, which is contained in U_x. The curve phi(s)=F(su) is therefore C^2 along the entire segment. Applying the fundamental theorem of calculus twice componentwise gives

F(u)-F(0)-Ju
=integral_0^1 (1-s) D^2F(su)[u,u] ds.

By the stated bilinear derivative bound,

||F(u)-F(0)-Ju||_2<=C_M ||u||_2^2/2.

Since B>=beta I and u belongs to Q_t,

beta ||u||_2^2<=u^TBu<=t^2.

Using ||w||_2=1 and taking the supremum proves

r_{M,w}(t)<=C_M t^2/(2 beta).

All values in this supremum are defined. Its finiteness also follows from continuity on the compact set Q_t. At t=0 the remainder is zero.

For the flip implications at radius eta, write

epsilon(u)=w^T(F(u)-F(0)-Ju),

so |epsilon(u)|<=r_{M,w}(eta) on Q_eta. With tau=sign(s_0) and d=eta sqrt(sigma_w),

tau s_ex(u)=gamma_w+tau w^TJu+tau epsilon(u).

If d>gamma_w+r_{M,w}(eta), then sigma_w>0 and the boundary-directed optimizer from part 2 satisfies

tau s_ex(u_*)<=gamma_w-d+r_{M,w}(eta)<0.

It gives a strict sign reversal and therefore a prediction flip under the specified tie convention.

If d<gamma_w-r_{M,w}(eta), then for every u in Q_eta,

tau s_ex(u)>=gamma_w-d-r_{M,w}(eta)>0.

Thus every feasible score has the same nonzero sign as the base score and no prediction flip occurs. The strict hypotheses already imply the necessary positivity of their gaps; no additional assumption is needed. Neither displayed sufficient condition resolves its equality boundary in general.

## 5. Exact proxy feasibility and radius corrections

Apply the same integral calculation to G, considered as a map into R^p. For u in Q_rho, let R_P(u)=G(u)-G(0)-Ku. Then

||R_P(u)||_2<=C_P ||u||_2^2/2.

The reverse triangle inequality and K^TK=B imply

| ||G(u)-G(0)||_2-sqrt(u^TBu) |
<=||R_P(u)||_2
<=C_P ||u||_2^2/2.

In particular, on Q_t with 0<=t<=rho, this discrepancy is at most C_P t^2/(2 beta). The second-order error concerns the unsquared distance used for the budget.

For an explicit uniform comparison on the specified region, put

Delta=C_P rho^2/(2 beta),
t_-=max{0,eta-Delta},
t_+=min{rho,eta+Delta}.

Then

Q_{t_-} subseteq P_{eta,rho} subseteq Q_{t_+}.

Indeed, if eta>=Delta and u belongs to Q_{eta-Delta}, its exact proxy distance is at most sqrt(u^TBu)+Delta<=eta. If eta<Delta, the lower set is Q_0={0}, which is exactly proxy-feasible. Conversely, any u in P_{eta,rho} satisfies sqrt(u^TBu)<=eta+Delta and already belongs to Q_rho, proving the upper inclusion.

It follows that an exact local flip on P_{eta,rho} is guaranteed by

t_- sqrt(sigma_w)>gamma_w+r_{M,w}(t_-),

and a flip on P_{eta,rho} is ruled out by

t_+ sqrt(sigma_w)<gamma_w-r_{M,w}(t_+).

These are direct applications of the preceding signed-score arguments on the inner and outer ellipsoids. The remainder terms can be bounded by C_M t_-^2/(2 beta) and C_M t_+^2/(2 beta), respectively. If t_-=0, the sufficient-flip inequality cannot hold at positive margin, as expected.

This uniform comparison is conservative. One can instead check an individual candidate using sqrt(u^TBu)+(C_P/2)||u||_2^2<=eta, or use any sharper justified local bound. When the control radius is chosen proportional to eta inside a fixed chart neighborhood with bounded derivatives, the proxy radius correction is O(eta^2/beta). No statement here identifies the exact feasible set throughout an unrestricted chart with Q_eta, or assumes that a small proxy distance excludes distant returns of G elsewhere in the chart.
