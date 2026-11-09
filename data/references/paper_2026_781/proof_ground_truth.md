# Reference Proof

## Contract and obligations

All integrals are population integrals. The critic is weighted by the discounted state-action occupancy law, while the feature covariance is measured under its fixed initial law beta. Policies have uniformly bounded log densities. The actor objective uses the previous policy's log density.

The theorem-critical obligations are: well-defined policy and Bellman updates; occupancy-based TD coercivity; the critic norm recursion; coupled policy/critic stability under the exact displayed step range; uniform Bellman and realizable-parameter bounds; consecutive-policy and target-movement bounds; accumulated critic-error control; and performance telescoping with constants uniform over h, rho, and n. Each is derived below.

## 1. Bellman and policy definitions

For probability measures r absolutely continuous with respect to mu and bounded measurable Q, let Z=int exp(-Q/tau)dmu and let r_Q have density exp(-Q/tau)/Z. Direct substitution gives

`int Q dr+tau KL(r||mu)=-tau log Z+tau KL(r||r_Q)`.

Thus the infimum defining T is attained by r_Q. Since Q is bounded, this density has bounded logarithm. Integration against a probability kernel and the preceding variational formula show that T and every T^pi are gamma contractions on bounded measurable functions. For T^pi, the entropy term is bounded by admissibility. Iterating either contraction gives its unique bounded fixed point. The Gibbs policy associated with V* satisfies T^{pi*}V*=V*, hence V^{pi*}=V*. Also TV<=T^pi V for every pi; monotonicity and iteration give V*<=V^pi. Comparing with the admissible policy mu and using nonnegative KL gives `||V*||_infty<=C_c/(1-gamma)`.

At an actor step put `f_n=q_{theta^{n+1}}+tau log p_n`. Applying the same variational calculation with reference pi^n and temperature 1/lambda gives

`p_{n+1}=p_n exp(-lambda f_n)/int exp(-lambda f_n)dpi^n`.

Equivalently, it is proportional to `p_n^(1-tau lambda)exp(-lambda q_{theta^{n+1}})`. This is a jointly measurable density with uniformly bounded logarithm whenever theta^{n+1} is finite and pi^n is admissible. Induction therefore makes every update well defined and admissible.

## 2. Occupancy coercivity and gradient bounds

Fix pi and write `K=K_pi` and `m=d_beta^pi`. The occupancy series directly gives

`m=(1-gamma)beta+gamma mK`.

Consequently `gamma mK<=m` and `m>=(1-gamma)beta` as measures. For bounded f, Jensen gives

`gamma int (Kf)^2 dm<=gamma int K(f^2)dm<=int f^2dm`.

Cauchy-Schwarz then gives

`int f(f-gamma Kf)dm >=(1-sqrt(gamma))int f^2dm`.

For f=q_theta this is at least `Gamma||theta||_2^2`. For f=q_theta-Q_tau^pi, exact realizability and the Bellman equation show that the residual equals f-gamma Kf. Thus

`<g(theta,pi),theta-theta_pi> >=Gamma||theta-theta_pi||_2^2`.

The covariance is invertible, so theta_pi is unique. Moreover,

`||g(theta,pi)||_2^2 <=int(f-gamma Kf)^2dm <=2(1+gamma)int f^2dm <=2(1+gamma)||theta-theta_pi||_2^2`.

These calculations close the externally cited TD-coercivity and occupancy-domination obligations directly.

## 3. Critic norm recursion

Write `K_n=sup_s KL(pi^n(.|s)||mu)`, `X_n=||theta^n||_2^2`, and `b=(1+gamma)^2`. The residual for a general theta can be written

`q_theta-gamma K_pi q_theta-c-tau gamma P KL(pi||mu)`.

The forcing vector obtained by multiplying the last two terms by phi and integrating has norm at most C_c+tau gamma K_n. The preceding coercivity and Young's inequality imply

`<g(theta^n,pi^n),theta^n> >=Gamma X_n/2-(C_c^2+tau^2 gamma^2 K_n^2)/Gamma`.

Bounded features also give

`||g(theta^n,pi^n)||_2^2 <=3b X_n+3C_c^2+3tau^2 gamma^2 K_n^2`.

Expanding the update yields

`X_{n+1}<=(1-hGamma+3h^2b)X_n+(3h^2+2h/Gamma)(C_c^2+tau^2 gamma^2 K_n^2)`.

Because lambda_beta<=1, Gamma<=1, and h<=Gamma/(6b), the scalar coefficient lies in (0,1). Summing the geometric recursion gives

`X_{n+1}<=X_0+alpha(h)[C_c^2+tau^2 gamma^2 max_{r<=n}K_r^2]`,

where `alpha(h)=(3h+2/Gamma)/(Gamma-3hb)`. This function is positive and increasing on the relevant interval.

## 4. Coupled stability under the main-text step range

Let h_bar be exactly the bound displayed in the public task and put `a=alpha(h_bar)`. Its definition and Gamma^2>32gamma^2 imply h_bar>0. Moreover,

`h_bar(24gamma^2+3b)<=(Gamma^2-16gamma^2)/(2Gamma)<(Gamma^2-16gamma^2)/Gamma`,

which is equivalent to `8gamma^2 a<1`. In particular `r=2gamma sqrt(a)<1`.

Define

`l_n(s,a)=log p_n(a|s)-int log p_n(a'|s)mu(da')`,

and `L_n=max_{0<=j<=n}||l_j||_infty`. Normalization gives `p_n=exp(l_n)/int exp(l_n)dmu`. Since int l_n dmu=0, Jensen gives log int exp(l_n)dmu>=0. Therefore

`0<=K_n<=||l_n||_infty`.

Also `||log p_n||_infty<=2||l_n||_infty`.

Centering the explicit policy update yields

`l_{n+1}=(1-tau lambda)l_n-lambda(q_{theta^{n+1}}-int q_{theta^{n+1}}dmu)`.

Let `B=X_0+C_c^2 a`. The critic recursion implies

`||theta^{n+1}||_2<=sqrt(B)+tau gamma sqrt(a)L_n`.

Hence

`||l_{n+1}||_infty<=[1-tau lambda(1-r)]L_n+2lambda sqrt(B)`.

The coefficient lies in (0,1). Induction gives

`L_n<=L=max{||l_0||_infty,2sqrt(B)/[tau(1-r)]}`.

It follows that K_n<=L and all critic norms are bounded by

`T=max{||theta^0||_2,sqrt(B)+tau gamma sqrt(a)L}`.

Thus R=T+L proves the first conclusion. These constants are independent of h and lambda. This unsquared argument avoids the erroneous squaring in the source and retains the whole main-text step range.

## 5. Uniform Bellman bounds and consecutive-policy movement

The policy Bellman equation gives

`||Q_tau^{pi^n}||_infty<=Q_bar=(C_c+tau gamma L)/(1-gamma)`.

Realizability and covariance inversion give

`theta_pi=G_beta^(-1)int Q_tau^pi phi dbeta`,

so `||theta_{pi^n}||_2<=Q_bar/lambda_beta` and

`||theta_pi-theta_pi'||_2<=||Q_tau^pi-Q_tau^pi'||_infty/lambda_beta`.

For the consecutive-policy estimate, the omitted centering term in the source must not be dropped. Proximal comparison with pi^n gives, statewise,

`(1/lambda-tau)KL(pi^{n+1}||pi^n)<=2||theta^{n+1}||_2+tau KL(pi^n||mu)`.

A stronger estimate follows directly from the same explicit update. Set `u_n=q_{theta^{n+1}}+tau l_n`; subtracting the statewise constant from f_n does not change its tilt. We have `|u_n|<=H=T+tau L`. At a fixed state define

`F(t)=log int exp(-t u_n)dpi^n`.

Boundedness permits differentiation under the integral, and F''(t) is the variance of u_n under its t-tilted law. Thus `0<=F''(t)<=H^2`. Since F(0)=0,

`KL(pi^{n+1}||pi^n)=lambda F'(lambda)-F(lambda)=int_0^lambda tF''(t)dt<=lambda^2H^2/2`.

Consequently `D_n=sup_s KL(pi^{n+1}||pi^n)<=lambda^2H^2/2`.

Subtract the two policy Bellman equations and add and subtract the mixed-policy Q term. The entropy identity is

`KL(pi^{n+1}||mu)-KL(pi^n||mu)=KL(pi^{n+1}||pi^n)+int log p_n d(pi^{n+1}-pi^n)`.

The statewise constant in log p_n cancels. Pinsker, in the total-variation convention ||r-r'||_TV=int|dr-dr'|, gives `||r-r'||_TV<=sqrt(2KL(r||r'))`. Therefore

`||Q_{n+1}-Q_n||_infty<=gamma/(1-gamma)[sqrt(2)(Q_bar+tau L)sqrt(D_n)+tau D_n]`.

Using lambda<1/tau yields

`||Q_{n+1}-Q_n||_infty<=N lambda`,

where `N=gamma[(Q_bar+tau L)H+H^2/2]/(1-gamma)`. Thus

`||theta_{pi^{n+1}}-theta_{pi^n}||_2<=M lambda`,

with M=N/lambda_beta. All these constants are independent of h and lambda.

## 6. Accumulated critic errors

Let `x_k=||theta^{k+1}-theta_{pi^k}||_2`. The estimates in Section 2 and h<=Gamma/[6(1+gamma)^2] imply

`x_k^2<=(1-hGamma)||theta^k-theta_{pi^k}||_2^2`.

For k>=1, add and subtract theta_{pi^{k-1}} and use Young's inequality with epsilon=hGamma/[2(1-hGamma)]. This gives

`x_k^2<=(1-hGamma/2)x_{k-1}^2+2M^2lambda^2/(hGamma)`.

Iterating and averaging gives

`(1/n)sum_{k<n}x_k^2<=2x_0^2/(nhGamma)+4M^2lambda^2/(h^2Gamma^2)`.

Since `x_0<=T+Q_bar/lambda_beta`, Cauchy-Schwarz yields

`(1/n)sum_{k<n}x_k<=A/sqrt(nh)+(2M/Gamma)lambda/h`,

with `A=sqrt(2/Gamma)(T+Q_bar/lambda_beta)` independent of h and lambda.

## 7. Performance difference and telescoping

For policies pi,pi' define

`b(s)=int[Q_tau^{pi'}+tau log p_pi']d(pi-pi')+tau KL(pi||pi')`.

The Bellman equations give

`V^pi-V^{pi'}=b+gamma P_pi(V^pi-V^{pi'})`.

Expanding the bounded resolvent therefore proves, without an external citation,

`V^pi(rho)-V^{pi'}(rho)=(1-gamma)^(-1)int b d_rho^pi`,

where `d_rho^pi=(1-gamma)sum_{j>=0}gamma^j rho P_pi^j`.

For each pointwise proximal step the three-point inequality is also obtained directly: because log(p_{k+1}/p_k)=-lambda f_k minus a statewise normalizer, substitution into KL differences gives, for every admissible comparison policy pi,

`[KL(pi||pi^{k+1})-KL(pi||pi^k)]/lambda<=int f_k d(pi-pi^k)-int f_k d(pi^{k+1}-pi^k)-KL(pi^{k+1}||pi^k)/lambda`.

In fact equality holds for this linear objective. Define

`F_k=int f_k d(pi^{k+1}-pi^k)+tau KL(pi^{k+1}||pi^k)`.

Proximal optimality and tau<1/lambda give F_k<=0. Replacing the approximate Q by the true Q in a signed-policy integral costs at most 2x_k. The performance identity and the occupancy series for a nonpositive F_k consequently give

`V^{k+1}(s)-V^k(s)<=F_k(s)+2x_k/(1-gamma)`.

Let `m*=d_rho^{pi*}` and `y_k=int KL(pi*||pi^k)dm*`. Comparing with pi*, integrating the three-point inequality against this fixed measure, and using performance difference gives

`(y_{k+1}-y_k)/lambda<=-(1-gamma)(V^k(rho)-V*(rho))-tau y_k-int(V^{k+1}-V^k)dm*+c_err x_k`,

where `c_err=2+2/(1-gamma)`. The advantage centering terms cancel in the signed-policy integrals; no false pointwise equality of approximate and true advantages is used.

Summation, nonnegative y_k, and V^n>=V* give

`(1/n)sum_{k<n}(V^k(rho)-V*(rho))<=[y_0/lambda+int(V^0-V*)dm*]/[(1-gamma)n]+c_err[(1/n)sum_{k<n}x_k]/(1-gamma)`.

The initial value term is integrated against m*, not rho. It is bounded uniformly in rho by `B_0=(2C_c+tau K_0)/(1-gamma)`. Also `y_0<=Y_0=||log p_*||_infty+||log p_0||_infty`, a finite constant uniformly over rho; the Gibbs formula gives a bound for log p_* depending only on C_c, gamma, and tau.

For n>=1 and h<=h_bar,

`1/n<=sqrt(h_bar)/sqrt(nh)`.

Combining the accumulated-error estimate with the telescope proves the averaged bound with

`C=max{sqrt(h_bar)(Y_0/lambda+B_0)/(1-gamma)+c_err A/(1-gamma),2c_err M/[(1-gamma)Gamma]}`.

This constant is independent of h, rho, and n, although it may depend on lambda, as permitted by the source constant expression. The minimum is no greater than the average, proving the second conclusion.

Every theorem-critical obligation is closed. No GT quality warning is required.
