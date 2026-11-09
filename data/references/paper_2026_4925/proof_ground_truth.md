# Reference Proof

## Contract and proof obligations

The initial state may depend on w_0. The pair (x_0,w_0) is independent of the future disturbance sequence, and the input sequence is independent of both. Consequently a conditional excitation assertion for z_1 is not available in general. We must establish polynomial growth with a separate initialization and use observations z_2 onward for the block argument. Observations omitted from that argument remain in the feasible set and can only reduce it.

The obligations are: a fixed polynomial moment/truncation constant; the displayed numerical one-step small-ball constants at valid times; sphere covering and conditional lower-tail concentration; block PE with the prescribed radii; predictable boundary elimination without conditioning on future PE; and the exact sample-size calculation. All are closed below.

## 1. Polynomial growth and truncation

Write d_z=n+nm, D=1+m u_max^2, and Sigma_t=E[x_t x_t^T]. Set R=||A||_2^2+sigma_u^2 sum_i ||B_i||_2^2. By independence and isotropy of u_0,

E|| (A+sum_i u_0[i]B_i)x_0 ||_2^2 <= R E||x_0||_2^2.

The inequality ||a+b||^2<=2||a||^2+2||b||^2 therefore gives

E||x_1||_2^2 <= 2R E||x_0||_2^2+2n w_max^2.

This step does not assume independence of x_0 and w_0. For t>=1, future-noise independence and input independence give

Sigma_{t+1}=A Sigma_t A^T+sigma_u^2 sum_i B_i Sigma_t B_i^T+Sigma_w,

where Sigma_w=E[w_t w_t^T]. Hence

vec(Sigma_t)=TildeA^{t-1}vec(Sigma_1)+sum_{s=0}^{t-2}TildeA^s vec(Sigma_w),  t>=1,

with the sum empty at t=1. Since rho(TildeA)<=1 and TildeA has dimension n^2, its Jordan blocks imply ||TildeA^s||_2<=C(1+s^{n^2-1}) for s>=1. The case s=0 is included by enlarging C. Summing and using tr(Sigma_t)<=sqrt(n)||Sigma_t||_F gives a fixed c_PMS with

E||x_t||_2^2<=c_PMS(1+t^r),  t>=0,

where r=n^2 is admissible. The initial-state bound at t=0 is included by enlarging c_PMS.

Since ||z_t||_2^2=(1+||u_t||_2^2)||x_t||_2^2<=D||x_t||_2^2, choose a fixed C_z>0 sufficiently large that

sum_{t=1}^T E||z_t||_2^2 <= C_z T^{r+1},  T>=1.

For example, C_z>=2D c_PMS suffices. This choice precedes T, eta, and epsilon and has only the allowed dependencies. For H_M={max_{1<=t<=T}||z_t||_2<=M}, Markov's inequality and a union bound give

P(H_M^c)<=C_z T^{r+1}/M^2.

## 2. Numerical conditional small-ball bound

Define H_t=sigma(x_0,u_0,...,u_t,w_0,...,w_{t-1}). The regressor z_t is H_t-measurable. For t>=1, w_t is independent of H_t, and u_{t+1} is independent of H_t and w_t.

Fix a unit v=(v_0,v_1,...,v_m), let V=[v_1 ... v_m], and put q=v_0+V u_{t+1}. Then ||v_0||^2+||V||_F^2=1 and

v^T z_{t+1}=q^T(Theta_*z_t+w_t).

Conditional on H_t and a nonzero q, Y=q^T w_t has a centered symmetric log-concave density and variance at least sigma_w^2||q||^2. A symmetric unimodal density assigns maximal mass among intervals of a fixed length to the centered interval: this follows by integrating a density nonincreasing with distance from zero. Thus adding the known shift q^T Theta_*z_t cannot decrease the outside probability at a fixed symmetric threshold.

The standard independent one-dimensional moment comparison used here is: for centered symmetric log-concave Y, E[Y^4]<=6(E[Y^2])^2. Its hypotheses hold for every nonzero q by scaling the assumed unit-direction density; bounded noise supplies all moments. Paley-Zygmund applied to Y^2 at theta=1/4 yields

P(|q^T(Theta_*z_t+w_t)|>=sigma_w||q||/2 | H_t,q)>= (3/4)^2/6=3/32.

Let a=min{1,sigma_u^2} and X=||q||^2. Conditional on H_t,

EX=||v_0||^2+sigma_u^2||V||_F^2>=a,

0<=X<=D,

EX^2<=D EX.

Paley-Zygmund at theta=1/2 gives P(X>=EX/2 | H_t)>=a/(4D). This event implies ||q||>=sqrt(a)/2 and in particular q is nonzero. Integrating the preceding conditional noise estimate over this event gives, for every t>=1,

P(|v^T z_{t+1}|>=k_z | H_t)>=p_z,

where k_z=sigma_w sqrt(a)/4 and p_z=3a/(128D), exactly as in the task. No estimate for z_1 is asserted.

## 3. Covering and conditional concentration

We only need the following sphere-net logarithmic bound, in either Euclidean or vectorized Frobenius norm:

log V_{e,d}<=log 544+5d log(d/e),  d>=1, 0<e<=1/4.

For completeness, choose a maximal e-separated subset of the unit sphere. Balls of radius e/2 around its points are disjoint and lie in the ball of radius 1+e/2. Volume comparison gives V_{e,d}<=(1+2/e)^d. Maximality gives an e-net. Since 1+2/e<=3/e and d>=1, e<=1/4, this proves the displayed logarithmic bound. Thus no specialized covering theorem is needed to close this obligation.

We also verify the scalar conditional lower-tail estimate. Suppose an adapted process satisfies P(|Z_s|>=k | F_{s-1})>=p at every one of N consecutive indices. Let I_s=1{|Z_s|>=k}. If sum_s Z_s^2<=k^2 p^2 N/8, then sum_s I_s<=p^2 N/8<=pN/2. On the other hand sum_s E[I_s|F_{s-1}]>=pN. The martingale differences I_s-E[I_s|F_{s-1}] are bounded in absolute value by one. The bounded-difference exponential estimate therefore gives

P(sum_s Z_s^2<=k^2 p^2 N/8 | F_start)<=exp(-Np^2/8).

Indeed the lower deviation is at least pN/2, and the usual exponential-supermartingale bound is exp(-(pN/2)^2/(2N)). This argument also proves the conditional version stated here. Every first observation in an application must satisfy the conditional hypothesis.

## 4. Shifted blocks and PE

Fix eta, epsilon, and a positive integer T satisfying the task's sample condition. Put

M=sqrt(6C_z T^{r+1}/eta),  a_1=k_z p_z/4,

kappa=ceil(8L_z/p_z^2),  N=floor((T-2)/kappa).

Since L_z>=1 and p_z<=1,

8L_z/p_z^2<=kappa<=9L_z/p_z^2<=16L_z/p_z^2,

and kappa>=2. The sample condition ensures T is large enough that the displayed blocks exist; the final calculation below also shows N>0.

For 0<=k<N define the block B_k={k kappa+2,...,(k+1)kappa+1} and

K_k=(1/kappa)sum_{t in B_k}z_t z_t^T.

Every such index is between 2 and T-1. Let E_PE={K_k>=a_1^2 I for every k}. A fixed unit direction satisfies the preceding small-ball hypotheses throughout each block, conditionally on H_{k kappa+1}. Thus

P(v^T K_k v<=2a_1^2 | H_{k kappa+1})<=exp(-kappa p_z^2/8).

Take an epsilon_z-net of the unit sphere in R^{d_z}. Its size V_z obeys the logarithmic covering bound. The task's epsilon_z equals min{a_1^2/(2M^2),1/4}. On H_M, ||K_k||_2<=M^2. If every net quadratic form exceeds 2a_1^2, then for any unit v and a net point lambda within epsilon_z,

v^T K_k v>=lambda^T K_k lambda-2epsilon_z M^2>=a_1^2.

The final inequality also holds when the minimum defining epsilon_z is 1/4. Therefore

P(E_PE^c)<= (T/kappa)V_z exp(-kappa p_z^2/8)+P(H_M^c).

Here P(H_M^c)<=eta/6. Since kappa p_z^2/8>=L_z,

(T/kappa)V_z exp(-kappa p_z^2/8)
<=T exp(log 544+5d_z log(d_z/epsilon_z)-L_z)
=eta/(3e)<=eta/3.

Consequently P(E_PE^c)<=eta/2.

## 5. Parameter directions and predictable elimination

Let Gamma_T={Theta-Theta_*:Theta in S_T}. Then

Gamma_T={gamma:w_t-gamma z_t in W for t=0,...,T-1},

and diam(S_T)=diam(Gamma_T)<=2 sup_{gamma in Gamma_T}||gamma||_F. Thus {diam(S_T)>epsilon} is contained in E_large={exists gamma in Gamma_T:||gamma||_F>=epsilon/2}. These are measurable events: for example, restrict candidate errors to closed bounded annuli, project the closed feasibility relation over these compact sets, and take a countable union.

Take a deterministic epsilon_gamma-net {G_i} of the unit Frobenius sphere in R^{n by d_z}; its logarithmic size is at most log 544+5d_gamma log(d_gamma/epsilon_gamma). The task's radius equals min{a_1/(4M sqrt(n)),1/4}, and hence epsilon_gamma M<=a_1/(4sqrt(n)).

For each i and t choose the first coordinate attaining ||G_i z_t||_infty, and its sign, with a fixed tie rule. Denote them j_{i,t}, b_{i,t}. They are H_t-measurable. In block B_k let tau_{i,k} be the first time with ||G_i z_t||_infty>=a_1/sqrt(n), or a cemetery value if none exists. On E_PE,

(1/kappa)sum_{t in B_k}||G_i z_t||_2^2=tr(G_i K_k G_i^T)>=a_1^2,

so a hit exists in every block.

Suppose E_large, E_PE, and H_M occur. Select a feasible gamma with norm at least epsilon/2 and a net point G_i within epsilon_gamma of gamma/||gamma||_F. At each selected hit, using j=j_{i,t} and b=b_{i,t},

b((gamma/||gamma||_F)z_t)[j]
>=a_1/sqrt(n)-epsilon_gamma M
>=3a_1/(4sqrt(n)).

Therefore b(gamma z_t)[j]>=3a_1 epsilon/(8sqrt(n))>=e_delta, where

e_delta=a_1 epsilon/(4sqrt(n))=k_z p_z epsilon/(16sqrt(n)).

The task's accuracy range ensures 0<e_delta<=epsilon_0. Feasibility implies

b w_t[j]>=-w_max+e_delta.

This requires the noise to avoid the opposite boundary interval; it does not force the noise into that interval. Put q=c_w e_delta. Since the boundary assumption lower-bounds an event probability, 0<q<=1. For any fixed j,b, the opposite-sign boundary assumption and the absence of coordinate atoms give

P(b w_t[j]>=-w_max+e_delta)
=1-P((-b)w_t[j]>w_max-e_delta)
<=1-q.

For a fixed net point, define G_{i,k}^{surv} to be the event that a hit occurs in block k and the preceding non-elimination inequality holds at that hit. Then

E_large intersect E_PE intersect H_M
is contained in union_i intersection_{k=0}^{N-1} G_{i,k}^{surv}.

To justify iteration, fix the event that all earlier blocks survived and that the first hit in the present block is at a specified time t. This event, and the chosen sign and coordinate, are H_t-measurable. Since t>=2, w_t is independent of H_t and has the original disturbance law. Its conditional non-elimination probability is at most 1-q. Sum over all possible hit times. The sum of their probabilities is at most the probability of earlier survival. Induction gives

P(intersection_{k=0}^{N-1} G_{i,k}^{surv})<=(1-q)^N.

In particular, this argument never conditions on the global PE or truncation event. Union bounding over i and adding the truncation tail yields

P(E_large intersect E_PE)<=V_gamma exp(-qN)+eta/6.

## 6. Exact integer-block and sample calculation

The task's sample condition is exactly

T>=(16L_z/p_z^2)(L_gamma/q).

Using the ceiling choice of kappa gives T/kappa>=16L_gamma/(9q). Also

N=floor((T-2)/kappa)>=T/kappa-1-2/kappa>=T/kappa-2.

Since L_gamma>=2 and q<=1,

qN>=16L_gamma/9-2q>=L_gamma-1>0.

This both verifies that full blocks exist and absorbs the shifted starting index without changing the constant 256. Consequently

V_gamma exp(-qN)
<=exp(log 544+5d_gamma log(d_gamma/epsilon_gamma)-L_gamma+1)
=eta/3.

Thus P(E_large intersect E_PE)<=eta/2. Combining this with P(E_PE^c)<=eta/2 proves

P(diam(S_T)>epsilon)<=eta.

For a fixed model and fixed eta, the two logarithmic factors grow at most logarithmically with T. A sufficiently large T of order epsilon^{-1} times powers of log(1/epsilon) satisfies the implicit condition. The exact displayed formula, including r and C_z inside its logarithms, specifies the dimension and model dependence; no stronger dimension-uniform assertion is needed.
