# Reference Proof

## Contract and obligations

The coverage probability is unconditional over the joint training, calibration, and test experiment. No independence between calibration residuals and the next residual is assumed. The mixing sum includes lag zero. The kernel bound is k(z,z)<=B^2, the calibration mean squared feature error is at most delta_T^2, and the test feature error is at most delta_T.

The proof must establish: (1) score-error control; (2) inheritance of mixing and the empirical probabilities actually needed; (3) quantile bracketing including rounding and the infinite-threshold case; (4) unconditional coverage without an invalid conditioning argument; and (5) the two rates with constants uniform in the selected regularization sequence.

The exact uniform empirical-CDF claim attributed to Rio in the supplied source is not used. Its stated small-sample constants are false. The following elementary variance calculation supplies all concentration needed for the final coverage bound.

## 1. Score errors

Write A=(Sigma+lambda I)^(-1), S_t=S(epsilon_t), and S-hat_t=S(epsilon-hat_t). Boundedness gives ||phi(z)||<=B and ||mu||<=B, while ||A||<=1/lambda. The identity for the difference of two quadratic forms gives

|S-hat_t-S_t| <= (4B/lambda)||phi(epsilon-hat_t)-phi(epsilon_t)||.

Consequently, by Cauchy-Schwarz,

T^(-1) sum_{t=1}^T |S-hat_t-S_t| <= 4B delta_T/lambda,

and the test-point assumption gives

|S-hat_{T+1}-S_{T+1}| <= 4B delta_T/lambda.

Put a=4B delta_T/lambda and h=sqrt(a). These bounds hold almost surely under the task assumptions.

Let F_T be the empirical CDF of the true calibration scores. If a>0, at most a/h=h of the calibration indices, as a fraction of T, have score error exceeding h. Therefore, for every real u,

F_T(u-h)-h <= F-hat_T(u) <= F_T(u+h)+h.  (1)

For a=0 the score lists agree, and (1) holds with h=0. This is the needed deterministic coupling. It does not assert that the distance between the empirical CDFs is at most h.

## 2. Mixing and fixed-threshold concentration

The score is a fixed measurable function of each residual. Thus the score process is stationary, and its past and future sigma-fields are contained in the corresponding residual sigma-fields. Its mixing coefficients are no larger than those of the residual process.

Since F_S is continuous, a median threshold produces an event of probability 1/2 measurable with respect to epsilon_n. This event belongs to both sigma-fields in the lag-zero coefficient. Hence alpha_epsilon(0)>=1/4. Conversely, Cauchy-Schwarz for indicator covariances gives alpha_epsilon(0)<=1/4, so alpha_epsilon(0)=1/4 and M>=1/4.

For any fixed real u, let I_t=1{S_t<=u}. The mixing definition gives |Cov(I_s,I_t)|<=alpha_epsilon(t-s) for s<t. Therefore

Var(F_T(u)) <= [T/4+2 sum_{k=1}^{T-1}(T-k)alpha_epsilon(k)]/T^2 <= 2M/T.  (2)

For any r>0, Chebyshev's inequality, obtained by applying Markov's inequality to the squared centered empirical CDF, gives

Pr{|F_T(u)-F_S(u)|>r} <= 2M/(Tr^2).  (3)

No independence from the test score is asserted or needed.

Set r=(M(log T)^2/(2T))^(1/3). It is positive because M>=1/4.

## 3. Small samples and the infinite threshold

For T=2,

r >= (log(2)^2/16)^(1/3),

so 16r>1. The desired bound follows from the fact that a coverage deviation is at most one.

Henceforth T>=3. Then log T>=1 and

r^3 >= (log T)^2/(8T) >= 1/T^3,

where the last inequality follows from T^2(log T)^2>=8. Thus r>=1/T.

Write p=1-alpha and m=ceil(p(T+1)). If m=T+1, the threshold is +infinity and coverage is one. In this case alpha<1/(T+1), so the error is at most 1/T<=r, proving the desired bound.

Otherwise m<=T. Put p_T=m/T. The rounding convention implies

p <= p_T < p+2/T.  (4)

## 4. Quantile bracketing

Define d=r+h+2/T. For each of p-d and p+d that lies strictly between zero and one, define the corresponding population quantile q_- or q_+. Continuity of F_S ensures

F_S(q_-)=p-d,  F_S(q_+)=p+d.

These quantiles are finite: the score is nonnegative and bounded by 4B^2/lambda. A lower quantile is unnecessary when p-d<=0, and an upper quantile is unnecessary when p+d>=1; the respective final one-sided probability bound is then automatic.

Let E be the event that |F_T(q)-F_S(q)|<=r at every quantile just defined. There are at most two such thresholds. By (3) and a union bound,

Pr(E^c) <= 4M/(Tr^2).  (5)

On E, whenever the lower quantile is needed, (1) gives

F-hat_T(q_--h) <= F_T(q_-)+h <= p-d+r+h = p-2/T < p_T.

It follows that q-hat_{1-alpha}>q_--h. Similarly, whenever the upper quantile is needed,

F-hat_T(q_++h) >= F_T(q_+)-h >= p+d-r-h = p+2/T >= p_T,

so q-hat_{1-alpha}<=q_++h. These arguments remain valid with ties in either score list.

## 5. Unconditional coverage

Let C denote the event S-hat_{T+1}<=q-hat_{1-alpha}, which is exactly response coverage by the task's residual and region definitions.

On E, the test-score error implies the lower inclusion

{S_{T+1}<=q_--h-a} intersect E subset C

whenever the lower quantile is needed, and the upper inclusion

C intersect E subset {S_{T+1}<=q_++h+a}

whenever the upper quantile is needed.

Take unconditional probabilities. For example, the lower bound is

Pr(C) >= F_S(q_--h-a)-Pr(E^c) >= p-d-L(h+a)-Pr(E^c).

The upper bound is obtained in the same way. In the omitted boundary cases the corresponding bound follows directly from 0<=Pr(C)<=1. Consequently,

|Pr(C)-p| <= r+2/T+(L+1)h+La+4M/(Tr^2).  (6)

This step uses intersections, not a claim that the test score retains its marginal distribution conditional on E or on the calibration observations.

From the definition of r,

4M/(Tr^2)=8r/(log T)^2<=8r.

Together with 2/T<=2r, (6) yields

|Pr(C)-p| <= 11r+(L+1)h+La <= 16r+4(L+1)(h+a).

Substitution of h=sqrt(4B delta_T/lambda) and a=4B delta_T/lambda proves the requested finite-sample bound. This is a deterministic bound on the unconditional marginal coverage probability, so it implies, in particular, the task's probability-at-least-1-r assertion. It does not prove calibration-conditional or input-conditional coverage.

## 6. Rates

Assume delta_T=O(T^(-rho)), lambda=T^(-beta), and that B, M, and the CDF Lipschitz constant L are fixed along this sequence. Then

h=O(T^((beta-rho)/2)),  a=O(T^(beta-rho)).

For beta<rho, a=O(h) eventually, so the score contribution is O(T^((beta-rho)/2)). The other contribution is O(T^(-1/3)(log T)^(2/3)).

If rho>2/3 and 0<beta<rho-2/3, then (beta-rho)/2<-1/3, and the mixing-rate expression dominates. If 0<rho<=2/3 and 0<beta<rho, then (beta-rho)/2>-1/3; the strict polynomial gap absorbs the logarithmic factor, and the approximation-rate expression dominates. These are the two requested rates. Their bounds hold outright and hence with the same advertised probability. The constants implicit in the O notation may depend on the fixed constants in the hypotheses, including the constant in delta_T=O(T^(-rho)).
