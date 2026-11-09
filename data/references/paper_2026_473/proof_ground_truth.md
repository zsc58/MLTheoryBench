# Reference Proof

## Proof Structure

Conditioning on the test observation gives the conditional-binomial representation of every rank probability. Under absolute continuity, quantile change of variables identifies its normalized coordinates as Beta averages of the density ratio. Jensen proves the continuous upper bound. Independently deleting one reference observation gives an adjacent-resolution stochastic kernel preserving the uniform reference laws, and finite-weight Jensen proves the required data-processing inequality. Affinity of rank probabilities gives convexity; continuity of their bounded test functions gives weak lower semicontinuity. Finally, explicit Beta second-moment estimates prove uniform approximation, convergence, and all three rates. No unresolved proof obligation remains.

## Complete Proof

### 1. Quantile representation and well-definedness

Fix nu and f as in the task. For 0<u<1, let q_nu(u)=inf{y in R:F_nu(y)>=u}. This is a measurable finite-valued quantile on (0,1). Its pushforward of Lebesgue measure is nu: the set of u with q_nu(u)<=y has Lebesgue measure F_nu(y). Since nu is atomless, F_nu is continuous. Its limits at the two ends of R and continuity then give F_nu(q_nu(u))=u for 0<u<1.

When mu<<nu, choose a nonnegative measurable version g=dmu/dnu and define rho=g composed with q_nu almost everywhere on (0,1). Quantile pushforward gives integral_0^1 rho(u)du=integral g dnu=1. It also gives integral_0^1 f(rho(u))du=Delta(mu||nu).

We use the standard extended-valued Jensen inequality: if a random variable X is nonnegative and integrable and f is proper, convex, and lower semicontinuous on [0,infinity), then f(EX)<=E f(X). The expectation on the right is well-defined because such an f has an affine minorant, whose negative part is integrable for integrable X. Here f is proper because f(1)=0. These hypotheses hold for every Beta-weighted occurrence of rho: its expectation is finite because its density is bounded for each fixed K and rho is integrable. The same affine-minorant observation makes the continuous divergence well-defined as an extended-valued integral.

For b_{n,K}(u)=binom(K,n)u^n(1-u)^(K-n), understood as a polynomial at the endpoints, independence gives A_K conditional on Y=y distributed as Bin(K,F_nu(y)). Therefore, for every mu,

p_K(n)=integral_R b_{n,K}(F_nu(y))dmu(y).

For K=0 this reads b_{0,0}=1 and p_0(0)=1. Under mu<<nu, quantile pushforward and F_nu(q_nu(u))=u give

p_K(n)=integral_0^1 b_{n,K}(u)rho(u)du.

The Bernstein identities used below are sum_{n=0}^K b_{n,K}(u)=1 and integral_0^1 b_{n,K}(u)du=1/(K+1). Consequently, (K+1)b_{n,K} is the Beta(n+1,K-n+1) density. Its parameters are strictly positive even when K=0. If S_{n,K} has this distribution, then

c_{n,K}:=(K+1)p_K(n)=E rho(S_{n,K}).

### 2. Continuous upper bound

For mu<<nu, Jensen and the partition identity give

Delta_K=(1/(K+1))sum_{n=0}^K f(c_{n,K})
<= (1/(K+1))sum_{n=0}^K E f(rho(S_{n,K}))
= integral_0^1 f(rho(u))du
= Delta(mu||nu).

These statements remain valid when the right side is infinite. The finite sum and integral identity can also be justified by subtracting an affine minorant of f, leaving nonnegative integrands. When mu is not absolutely continuous with respect to nu, the task defines Delta(mu||nu)=+infinity, so the upper bound is immediate.

### 3. Monotonicity for arbitrary mu

Generate Y and K+1 independent reference observations, and delete a reference observation using an independent uniform index. The retained observations have the same joint law as K iid reference observations independent of Y. Conditional on the original rank m, the deleted observation is one of the m successes with probability m/(K+1), and otherwise is a failure. Define the kernel from {0,...,K+1} to {0,...,K} by

T_K(n|m)=m/(K+1) if n=m-1;
T_K(n|m)=(K+1-m)/(K+1) if n=m;
T_K(n|m)=0 otherwise.

Every column sums to one. At m=0 only the transition to 0 has positive probability, and at m=K+1 only the transition to K has positive probability. Thus this is a stochastic kernel, including K=0, and the deletion experiment proves p_K=T_K p_{K+1} for arbitrary mu.

For each output n in {0,...,K},

(T_K u_{K+1})(n)
= (1/(K+2))[(K+1-n)/(K+1)+(n+1)/(K+1)]
= 1/(K+1).

Hence T_K u_{K+1}=u_K.

For completeness, the relevant finite-alphabet data-processing inequality follows directly from convexity. Let P,Q be input probability vectors with Q_m>0, let T be stochastic, and assume Q'_n=(TQ)_n>0. Set P'=TP and lambda_{n,m}=T(n|m)Q_m/Q'_n. For each n these are nonnegative weights summing to one, and P'_n/Q'_n=sum_m lambda_{n,m}(P_m/Q_m). Finite-weight Jensen therefore gives

sum_n Q'_n f(P'_n/Q'_n)
<= sum_n sum_m T(n|m)Q_m f(P_m/Q_m)
= sum_m Q_m f(P_m/Q_m).

The finite-weight inequality holds also for extended-valued f; zero-weight terms are omitted. In the present application both input and output reference vectors are strictly positive. Taking P=p_{K+1}, Q=u_{K+1}, and T=T_K gives Delta_K<=Delta_{K+1}. Combining this with the upper bound at K+1 proves the claimed chain for every mu and K>=0. Also, Jensen on the uniform weights in the definition gives Delta_K>=f(sum_n p_K(n))=0, and Delta_0=f(1)=0.

### 4. Convexity and weak lower semicontinuity

For fixed K, every coordinate p_K(n)=integral b_{n,K}(F_nu(y))dmu(y) is affine in mu. Convexity of f and summation therefore prove convexity of Delta_K, as an extended-valued functional.

If F_nu is continuous, each function y maps to b_{n,K}(F_nu(y)) is bounded and continuous. Thus weak convergence of probability measures implies convergence of every rank coordinate. Every normalized coordinate lies in [0,K+1]. The lower-semicontinuous function f has a finite lower bound on this compact interval: otherwise a sequence of values tending to minus infinity would have a convergent subsequence and contradict lower semicontinuity and the exclusion of minus infinity from its codomain. Subtracting that lower bound makes the finitely many summands nonnegative. Coordinate convergence and lower semicontinuity of f now prove weak lower semicontinuity of Delta_K.

### 5. Uniform approximation for arbitrary continuous rho

Assume the almost-everywhere density ratio admits the continuous representative on [0,1] in the task, and use that representative. Its nonnegativity and integral one follow from continuity and its almost-everywhere density properties. Set J=ran(rho). Since rho is continuous on the connected compact interval [0,1], J is a compact interval. Every c_{n,K}=E rho(S_{n,K}) belongs to J.

Let I_{n,K}=[n/(K+1),(n+1)/(K+1)), putting the final endpoint in the last interval, and set rho_K(u)=c_{n,K} on I_{n,K}. Then

Delta_K=integral_0^1 f(rho_K(u))du,
Delta=integral_0^1 f(rho(u))du.

For K>=1 define

h_K=1/(K+1), d_K=1/(K+2), v_K=1/[4(K+3)],
V_K=v_K+(d_K+h_K)^2.

The Beta mean and variance are

a_{n,K}=E S_{n,K}=(n+1)/(K+2),
Var(S_{n,K})=(n+1)(K-n+1)/[(K+2)^2(K+3)]<=v_K.

Indeed, the two factors in the variance numerator sum to K+2, so their product is at most (K+2)^2/4. For x_{n,K}=n/K,

|a_{n,K}-x_{n,K}|=|K-2n|/[K(K+2)]<=d_K.

Every u in I_{n,K}, including the final endpoint, satisfies |u-x_{n,K}|<=h_K. It follows that

|a_{n,K}-u|<=d_K+h_K,
E|S_{n,K}-u|^2=Var(S_{n,K})+|a_{n,K}-u|^2<=V_K.

In particular V_K=O(K^-1), uniformly in n and u.

Let R=||rho||_infinity and omega_rho(eta)=sup{|rho(s)-rho(t)|:s,t in [0,1], |s-t|<=eta}. For any fixed eta>0, splitting according to |S_{n,K}-u|<=eta and using Markov's inequality on its squared distance yields

|c_{n,K}-rho(u)|
<= E|rho(S_{n,K})-rho(u)|
<= omega_rho(eta)+2R P(|S_{n,K}-u|>eta)
<= omega_rho(eta)+2R V_K/eta^2.

This bound is uniform. For each eta, taking the limit superior as K tends to infinity gives a bound by omega_rho(eta); uniform continuity then permits eta to decrease to zero. Therefore ||rho_K-rho||_infinity tends to zero. No concavity assumption on the modulus is used.

Lipschitzness of f on J means it is finite there and |f(s)-f(t)|<=L_f|s-t| for s,t in J. Both rho and rho_K take values in J, so all divergences in this part are finite and

0<=Delta-Delta_K<=L_f||rho_K-rho||_infinity.

This proves convergence.

### 6. Holder rate

If |rho(s)-rho(t)|<=H|s-t|^alpha with 0<alpha<=1, then the preceding second-moment estimate and Jensen for the concave power alpha/2 give

|c_{n,K}-rho(u)|
<= H E|S_{n,K}-u|^alpha
<= H(E|S_{n,K}-u|^2)^(alpha/2)
<= H V_K^(alpha/2).

Consequently, 0<=Delta-Delta_K<=L_f H V_K^(alpha/2)<=C K^(-alpha/2), with C independent of K>=1.

### 7. C2 density-ratio rate

Suppose rho is C2 on [0,1]. Put R_1=||rho'||_infinity and R_2=||rho''||_infinity. Taylor's theorem at u, with its bounded second-order remainder, gives

|E rho(S_{n,K})-rho(u)|
<= R_1|E S_{n,K}-u|+(R_2/2)E|S_{n,K}-u|^2
<= R_1(d_K+h_K)+(R_2/2)V_K.

The right side is O(K^-1), uniformly. Multiplication by L_f proves 0<=Delta-Delta_K<=C K^-1 for K>=1.

### 8. Lipschitz density ratio and C2 generator rate

Suppose rho is Lipschitz with constant L_rho and f is C2 with |f''|<=M_f on an interval containing J. For fixed n,K, set Z=rho(S_{n,K}) and c=EZ. Both Z and c belong to J. Taylor's theorem along the segment between Z and c gives

|f(Z)-f(c)-f'(c)(Z-c)|<=(M_f/2)(Z-c)^2.

Taking expectations cancels the linear term. Jensen supplies the lower bound, so

0<=E f(Z)-f(c)<=(M_f/2)Var(Z).

For any constant a, Var(Z)<=E(Z-a)^2. Take a=rho(E S_{n,K}); Lipschitzness then gives

Var(Z)<=E|rho(S_{n,K})-rho(E S_{n,K})|^2
<=L_rho^2 Var(S_{n,K})
<=L_rho^2/[4(K+3)].

Finally, the Bernstein partition identity shows that the divergence gap is the average of these Jensen gaps:

Delta-Delta_K=(1/(K+1))sum_{n=0}^K [E f(rho(S_{n,K}))-f(c_{n,K})].

Therefore

0<=Delta-Delta_K<=M_f L_rho^2/[8(K+3)]<=C K^-1.

All constants depend only on f, rho, and the regularity bounds appearing in their respective alternatives, and not on K>=1. The bounds also cover constant rho and zero regularity constants without division by them.
