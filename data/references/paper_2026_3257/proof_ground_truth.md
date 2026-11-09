# Reference Proof

## Proof Structure

1. Establish uniform inner-loop second- and fourth-moment accuracy, including the scalar comparison constants.
2. Calculate both post-inner mean biases and the conditional variance of the implemented stochastic queries.
3. Derive the projected regularized outer stability estimate and convert distance into the original residual.
4. Substitute the raw schedule and count all primitive samples.
5. Substitute the corrected schedule and establish the fixed-epsilon total-sample conclusions.

## Complete Proof

All constants below are independent of the horizon, outer index, inner length, and admissible initializations. They may depend on the fixed problem and oracle parameters and the fixed inner stepsize constants. Constants in the final horizon bounds may additionally depend on the fixed exponent b.

### 1. Inner-loop moments

Put rho=1-mu>0, D_x=diam(X), and D_y=diam(Y). Freeze the outer point y and write x_star=x^*(y), e_t=X_t-x_star, and Delta_{t+1}=F(X_t,y)-f(X_t,y). Conditional on the pre-sample inner history, Delta_{t+1} has mean zero and second and fourth moments at most sigma^2 and sigma^4. Define

`a_t=(1-eta_t)e_t+eta_t[f(X_t,y)-f(x_star,y)]`.

For 0<=eta_t<=1, contraction gives

`||a_t|| <= (1-rho eta_t)||e_t||`.

Since x_star belongs to X, projection cannot increase its distance: the projection variational inequality `<z-Pi_X(z),x_star-Pi_X(z)><=0` implies `||Pi_X(z)-x_star||<=||z-x_star||`. Consequently,

`E_t||e_{t+1}||^2 <= (1-rho eta_t)^2||e_t||^2+sigma^2 eta_t^2`.

Choose c_2<2rho with a_2=c_2 eta_0>1. For sufficiently small eta_t, `(1-rho eta_t)^2<=1-c_2 eta_t`. This can be enforced uniformly by taking t_0 sufficiently large. With s_t=t+t_0 and u_t=E||e_t||^2,

`u_{t+1} <= (1-a_2/s_t)u_t+B_2/s_t^2`,

where B_2=sigma^2 eta_0^2. Choose K_2 large enough that K_2>=t_0 D_x^2 and `(a_2-1)K_2>=B_2`. If u_t<=K_2/s_t, then

`u_{t+1} <= K_2/s_t-(a_2 K_2-B_2)/s_t^2 <= K_2/s_t-K_2/s_t^2 <= K_2/(s_t+1)`.

This proves the second-moment bound.

For the fourth moment, let a be measurable before a centered observation Delta, and write M_q=E_t||Delta||^q. Expanding the fourth power, the term linear in Delta has conditional mean zero. The quadratic terms are bounded by `6 eta^2||a||^2 M_2`. The cubic term satisfies

`4 eta^3 E_t[|<a,Delta>| ||Delta||^2] <= 4 eta^3||a|| sqrt(M_2 M_4) <= 2 eta^2||a||^2 M_2+2 eta^4 M_4`.

Thus

`E_t||a+eta Delta||^4 <= ||a||^4+8 eta^2||a||^2 M_2+3 eta^4 M_4`.

Apply this to a_t, use projection and the moment bounds, and choose c_4<4rho with a_4=c_4 eta_0>2. Enlarging t_0 if necessary ensures `(1-rho eta_t)^4<=1-c_4 eta_t`. Therefore

`E_t||e_{t+1}||^4 <= (1-c_4 eta_t)||e_t||^4+C eta_t^2||e_t||^2+C eta_t^4`.

The second-moment bound gives, for v_t=E||e_t||^4,

`v_{t+1} <= (1-a_4/s_t)v_t+B_4/s_t^3`.

Choose K_4>=t_0^2 D_x^4 and `(a_4-2)K_4>=B_4`. The induction closes because

`v_{t+1} <= K_4/s_t^2-2K_4/s_t^3 <= K_4/(s_t+1)^2`.

The argument also applies conditionally on the history before each inner loop: Y_m is then fixed and the initialization is bounded in X. All constants are uniform. At the inner endpoint,

`E||X_{m,n}-x^*(Y_m)||^2 <= C/(n+t_0)`,

`E||X_{m,n}-x^*(Y_m)||^4 <= C/(n+t_0)^2`.

### 2. Mean biases and sampling noise

Let G_m be the history after the inner loop and before the fresh outer observations. Both X_{m,n} and Y_m are G_m-measurable. For the selected deterministic query H, define

`b_m=H(X_{m,n},Y_m)-h(Y_m)`,

`xi_m=H_m-H(X_{m,n},Y_m)`.

The implemented queries and freshness assumptions give `E[xi_m|G_m]=0` and `E[H_m|G_m]=h(Y_m)+b_m`. The relevant bias condition is the unconditional bound on E||b_m||^2; no almost-sure post-inner accuracy bound is asserted.

For the raw scheme, fast-coordinate Lipschitz continuity gives

`||H^raw(x,y)-h(y)|| <= L_g||x-x^*(y)||`.

Hence `E||b_m||^2<=C/n`. Its centered sampling noise is `G(X_{m,n},Y_m)-g(X_{m,n},Y_m)`, whose conditional second moment is at most sigma^2.

For the corrected scheme, put e=x-x^*(y). The segment from x^*(y) to x lies in X and therefore in the smoothness neighborhood. Taylor expansion in x, with the uniform Jacobian Lipschitz constants, gives

`g(x,y)=h(y)+C(y)e+R_g`,

`f(x,y)-x=-A(y)e+R_f`,

with `||R_g||<=(L_g^nabla/2)||e||^2` and `||R_f||<=(L_f/2)||e||^2`. The definition of P^* implies `P^*A=C`. Therefore

`H^corr(x,y)-h(y)=R_g+P^*(y)R_f`,

and `||H^corr(x,y)-h(y)||<=L_c||e||^2` for a horizon-independent constant L_c. The fourth-moment bound yields `E||b_m||^2<=C/n^2`.

Writing the two fresh centered primitive observations as Delta_g and Delta_f, the corrected sampling noise is

`xi_m=Delta_g+P^*(Y_m)Delta_f`.

If P_max bounds ||P^*||, then

`E[||xi_m||^2|G_m] <= 2 sigma^2(1+P_max^2)`.

Thus both schemes have a uniform conditional variance bound sigma_H^2. No primitive samples used in an inner update are reused as outer observations.

### 3. Outer stability and residual conversion

For 0<lambda<=1, define

`T_lambda(y)=[h(y)+lambda u]/(1+lambda)`.

This map takes Y into Y by convexity and contracts distances by r=(1+lambda)^(-1)<1. To justify its fixed point directly, iterate T_lambda from any point of Y. Successive distances are bounded by r^j times the first successive distance, so the sequence is Cauchy. Closedness of Y and continuity of T_lambda yield a fixed point y_lambda. The contraction inequality makes it unique. Its defining equation gives

`h(y_lambda)-y_lambda=lambda(y_lambda-u)`,

so `||h(y_lambda)-y_lambda||<=lambda D_y`.

Define `q_lambda(y)=h(y)-y+lambda(u-y)`. For e=y-y_lambda, non-expansiveness gives

`<e,q_lambda(y)> <= -lambda||e||^2`,

`||q_lambda(y)|| <= (2+lambda)||e|| <= 3||e||`.

Write the outer observation as `H_m=h(Y_m)+b_m+xi_m`, using the post-inner conditioning from the preceding section. Projection relative to y_lambda and conditional mean zero imply

`E[||Y_{m+1}-y_lambda||^2|G_m] <= ||e_m||^2+2 beta<e_m,q_lambda(Y_m)>+2 beta<e_m,b_m>+beta^2||q_lambda(Y_m)+b_m||^2+beta^2 sigma_H^2`,

where e_m=Y_m-y_lambda. Since `||q_lambda+b_m||^2<=18||e_m||^2+2||b_m||^2` and

`2 beta||e_m||||b_m|| <= (beta lambda/2)||e_m||^2+(2 beta/lambda)||b_m||^2`,

for beta<=lambda/36 the preceding inequality becomes

`E[||Y_{m+1}-y_lambda||^2|G_m] <= (1-beta lambda)||e_m||^2+(4 beta/lambda)||b_m||^2+beta^2 sigma_H^2`.

Here `2 beta/lambda+2 beta^2<=4 beta/lambda`, since beta lambda<=1. Let epsilon_H^2 bound E||b_m||^2 for every outer step and put D_m=E||Y_m-y_lambda||^2. Taking expectations and summing the geometric recursion gives

`D_N <= exp(-N beta lambda)D_y^2+4 epsilon_H^2/lambda^2+beta sigma_H^2/lambda`.

The residual map p=h-I is 2-Lipschitz. Therefore

`||p(Y_N)|| <= lambda D_y+2||Y_N-y_lambda||`,

and consequently

`E||h(Y_N)-Y_N||^2 <= 2 lambda^2 D_y^2+8 D_N <= C[lambda^2+exp(-N beta lambda)+beta/lambda+epsilon_H^2/lambda^2]`.

This proves the outer estimate without invoking a paper-specific theorem as an unproved dependency. It also covers singleton stabilized sets and zero observation noise.

### 4. Raw schedule and sample count

Fix b in (0,3/4). The chosen schedules satisfy

`lambda^2=N^(-2b/3)`,

`beta/lambda=N^(-2b/3)`,

`N beta lambda=N^(1-4b/3)`.

In particular beta<=lambda/36 for all sufficiently large N. With `n=ceil(N^(4b/3))` and the raw bias bound,

`epsilon_H^2/lambda^2 <= C n^(-1) N^(2b/3) <= C N^(-2b/3)`.

Set delta=1-4b/3>0. Because `N^delta/log N` tends to infinity, `exp(-N^delta)<=N^(-2b/3)` for sufficiently large N. Substitution proves

`E||h(Y_N)-Y_N||^2 <= C_b N^(-2b/3)`.

Each outer step uses n inner F calls and one outer G call, so `T_N=N(n+1)=Theta(N^(1+4b/3))`. Hence the fixed-b total-sample bound is

`E||h(Y_N)-Y_N||^2 <= C_b' T_N^(-q_raw(b))`,

where `q_raw(b)=(2b/3)/(1+4b/3)=2b/(3+4b)`.

### 5. Corrected schedule and epsilon quantifiers

For `n=ceil(N^(2b/3))`, the corrected bias bound gives

`epsilon_H^2/lambda^2 <= C n^(-2) N^(2b/3) <= C N^(-2b/3)`.

All other outer terms and the stepsize condition are the same as in the raw scheme. Thus

`E||h(Y_N)-Y_N||^2 <= C_b N^(-2b/3)`.

Each outer step uses n inner F calls, one additional fresh outer F call, and one fresh outer G call. Therefore `T_N=N(n+2)=Theta(N^(1+2b/3))`. The exact structured P^* evaluation is excluded from this count. The fixed-b total-sample exponent is

`q_corr(b)=(2b/3)/(1+2b/3)=2b/(3+2b)`.

As b increases to 3/4 from below, q_raw(b) tends to 1/4 and q_corr(b) tends to 1/3. Given any fixed epsilon>0, choose a fixed b<3/4 sufficiently close to 3/4 that both exponents are at least their respective limits minus epsilon. The bounds then imply

`E||h(Y_N)-Y_N||^2 <= C_epsilon T_N^(-1/4+epsilon)` for the raw scheme,

`E||h(Y_N)-Y_N||^2 <= C_epsilon T_N^(-1/3+epsilon)` for the corrected scheme,

for sufficiently large horizons. The constants and horizon thresholds may depend on epsilon through this fixed choice of b. No uniform bound as b approaches the endpoint, and no horizon-dependent choice b=b(N), is needed or asserted.
