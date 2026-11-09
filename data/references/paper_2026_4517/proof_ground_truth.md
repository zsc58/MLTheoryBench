# Reference Proof

All constants below are numerical and may change between displays. The clipping level is one. Write chi²(P||Q)=E_Q[(dP/dQ-1)²]. This proof uses the actual diffusion-specific sampler in the public task, not the Gaussian-tilt proposal in the previous artifact.

## 1. Output law, termination, and query accounting

For a fixed proposal x and a conditionally iid estimator sequence W_j in [-1,1], independence and the Poisson generating function give

P(accept|x)=E[((1+E[W_1|x])/2)^J]=exp(E[W_1|x]-1).

Summing over independent repeated attempts proves that the output density is proportional to q(x)exp(E[W_1|x]). In particular, every conditional output is a bounded tilt of its proposal, with density ratio between exp(-2) and exp(2).

An attempt with J=0 always succeeds. Thus the number of attempts is dominated by a geometric variable with success probability exp(-2), uniformly in the reverse input and the score functions. For n calls, including adaptively determined reverse inputs, conditional exponential-moment bounds give O(n+log(1/delta)) attempts with probability at least 1-delta/2. On a deterministic cap of that order, the sum of the Poisson(2) counts is O(n+log(1/delta)) with probability at least 1-delta/2. This argument does not assume that an attempt's acceptance event is independent of its Poisson count. There is one cached next-score evaluation per reverse transition and one current-score evaluation per sampled estimator. Consequently the total number of score queries is O(n+log(1/delta)).

## 2. Posterior exponential moments from covering numbers

Let U have finite second moment, Y_t=U+B_t with independent standard Brownian motion, and m_t(y)=E[U|Y_t=y]. Let D_t be the intrinsic dimension at variance t, with the same covering-number definition as in the task. We prove

E exp(||U-m_t(Y_t)||²/(Ct))≤exp(D_t).                                      (A)

First suppose a finite r-cover with N centers exists. Let h(y) be a nearest center, breaking ties measurably, and choose a center z_i within r of U. Conditional on U, comparing the chosen center z_j with z_i gives

||z_j-z_i||²≤2<sqrt(t)Z+(U-z_i),z_j-z_i>.

For all j simultaneously, Gaussian tails and a union bound imply, except with probability exp(-u),

2<sqrt(t)Z,z_j-z_i>≤(1/4)||z_j-z_i||²+8t(log N+u).

Also 2<U-z_i,z_j-z_i>≤(1/4)||z_j-z_i||²+4r². It follows that

||U-h(Y_t)||²≤C[r²+t(log N+u)]

with the same probability. Integration yields E exp(||U-h(Y_t)||²/(C_0t))≤exp(C_1[1+log N+r²/t]). This remains valid for r=0 when the support is finite.

Conditional Jensen and Cauchy–Schwarz transfer the bound to the posterior mean: for any a>0,

E exp(||U-m_t(Y_t)||²/(4a))≤E exp(||U-h(Y_t)||²/a).

Indeed, use ||U-m_t||²≤2||U-h||²+2||m_t-h||² and m_t-h=E[U-h|Y_t]. The alternative estimator h(y)=y gives an ambient-dimension bound by the Gaussian moment E exp(c||Z||²). Taking the better bound, optimizing over finite covers, and increasing the universal denominator gives (A), since D_t≥1. If every finite-radius covering number is infinite, only the ambient bound is needed. No attainment of the covering infimum is assumed.

For 0<s≤t, the Markov property gives

m_s(Y_s)-m_t(Y_t)=E[U-m_t(Y_t)|Y_s,Y_t].

Therefore another conditional Jensen application proves

E exp(||m_s(Y_s)-m_t(Y_t)||²/(Ct))≤exp(D_t).                    (B)

This is the posterior increment estimate needed below. It is important that its right-hand side comes from (A), not from a Gaussian observation-noise moment with ambient dimension.

## 3. Symmetric clipping control

Let p proportional to q exp(h), r proportional to q exp(h_c), where h=E W and h_c=E Clip_1(W). Put a=h-h_c and t=E(|W|-1)_+, so |a|≤t. The identity p=r exp(a)/E_r exp(a), Cauchy–Schwarz, and Jensen imply

max{chi²(p||r),chi²(r||p)}≤E_r[exp(4|a|)-1].

For example, 1+chi²(p||r)=E_r exp(2a)/(E_r exp(a))². Its denominator is at least exp(2E_r a); the resulting upper bound is at most (E_r exp(2|a|))²≤E_r exp(4|a|). The reverse direction follows from (E_r exp(a))(E_r exp(-a))≤E_r exp(2|a|). Since r/q≤exp(2), convexity gives

max{chi²(p||r),chi²(r||p)}≤exp(2) E_{q,W}[exp(4(|W|-1)_+)-1].       (C)

The symmetric direction is essential in the later change of measure.

## 4. Exact-score single-step error

Fix k and rescale only the next observation: y=x'/alpha_k. Put U=bar-alpha_k X_0, S=sigma_k², h=eta_k, T=S+h, and v=hS/T. In these coordinates the forward pair is U plus Brownian noise at times S and T. Its next-time score is alpha_k s_{k+1}^*(alpha_k y). Write m_S and m_T for the posterior means of U.

The exact-score proposal is q_y=N(g_y,vI), with g_y=y+h grad log p_T(y). Completing the Gaussian square gives the true conditional law

rho_y=E[N((S/T)y+(h/T)U,vI)|Y_T=y].                              (D)

The exact path estimator is W*=S^{-1}<dot-gamma,m_S(gamma)-m_T(y)>. Direct differentiation of the public coefficients gives

a²+(1-a)²/2+b²/2=1,

and its derivative is zero. Hence, under independent x~N(g_y,vI), xhat~N(g_y,vI/2), z~N(0,vI/2), the pair (gamma,dot-gamma) is independent Gaussian with laws N(g_y,vI) and N(0,cvI), where c=8pi²/27<3.

Moreover, differentiation in x gives

grad log(rho_y/q_y)(x)=S^{-1}(m_S(x)-m_T(y)).

The path starts at xhat+z independently of x and ends at x, so integration along it proves rho_y proportional to q_y exp(E W*). Let r_y be the corresponding exact-score clipped output.

Set H_y(x)=m_S(x)-m_T(y). For any L≥4, (C), the inequality exp(4(u-1)_+)-1≤exp(-L)exp(Lu), and Gaussian integration give

max{chi²(rho_y||r_y),chi²(r_y||rho_y)}≤A_y,

A_y=C exp(-L) E_{q_y} exp(C L²v||H_y(x)||²/S²).                  (E)

Here and below C can be increased consistently. Because r_y/q_y is bounded above and below, Cauchy–Schwarz in the correct direction gives

A_y≤C exp(-L) sqrt((1+A_y) F_y),

F_y=E_{rho_y} exp(C L²v||H_y(x)||²/S²).

These quantities are finite almost everywhere in the range used below. To justify this before solving the inequality, (D) and Jensen imply

rho_y(x)/q_y(x)≥exp(-h² Var(U|Y_T=y)/(2vT²)).

Thus q_y/rho_y is bounded by a finite y-dependent constant. The moment (B) gives integrability of F_y, and hence of the proposal expectation, for sufficiently small C L²vT/S². This avoids an invalid manipulation of infinite quantities.

Solving the quadratic inequality yields

A_y≤C[exp(-L)sqrt(F_y)+exp(-2L)F_y].

By (B), monotonicity of the intrinsic dimension with increasing effective noise, and vT/S²=h/S,

E F_y≤exp(C L²(h/S)d_*)

provided C L²h/S≤c_0 for a numerical c_0>0. Choose

L=c min{sqrt(S/h), S/(h d_*)}

with sufficiently small numerical c. Under S/h≥C[d_* log(1/epsilon)+log²(1/epsilon)], this L is at least a sufficiently large multiple of log(1/epsilon), and C L²(h/S)d_*≤L/2 after adjusting constants. Averaging (E) therefore proves

E_{p_{k+1}} chi²(rho_k||rho_k^*)≤C epsilon,

and hence E KL(rho_k||rho_k^*)≤C epsilon.

All rescalings preserve the relevant intrinsic bound: dim_T(Law(bar-alpha_k X_0))=dim_{T/bar-alpha_k²}(p_data)≤d_*, since effective noise has increased from nu/alpha_0².

## 5. Robustness to the two score errors

Continue in the same coordinates. Let e(x)=s_k(x)-s_k^*(x), and e_+(y)=alpha_k[s_{k+1}(alpha_k y)-s_{k+1}^*(alpha_k y)]. Estimated posterior means differ from exact ones by S e(x) and T e_+(y), and the proposal mean displacement is h e_+(y).

We use the following bounded-Gaussian-tilt comparison. If nu_i proportional to N(g_i,vI)exp(f_i), |f_i|≤1, then

KL(mu||nu_1)≤C[KL(mu||nu_0)+E_{nu_0}(f_1-f_0)²+||g_1-g_0||²/v].     (F)

For completeness, insert the intermediate law proportional to N(g_0,vI)exp(f_1). Changing only a bounded tilt costs at most C[KL(mu||nu_0)+E_{nu_0}(f_1-f_0)²]: expand the log normalizer using exp(u)≤1+u+C u² for bounded u, and bound the difference of expectations by Cauchy–Schwarz on square-root densities and H²≤KL/2. Changing the Gaussian mean then uses KL(mu||Q)≤2KL(mu||P)+log(1+chi²(P||Q)); the common bounded tilt multiplies chi-squared by at most a numerical constant. The equal-covariance Gaussian identity log(1+chi²)=||g_1-g_0||²/v proves (F).

Apply (F) to the exact-score and estimated-score clipped outputs. In comparing their clipped tilt functions, first change the auxiliary xhat distribution while keeping the integrand fixed. Boundedness and the Gaussian TV/KL bound give squared cost at most C h²||e_+||²/v. Then hold xhat at its exact-score law and change the integrand. Clipping is 1-Lipschitz, and the untruncated difference is

<dot-gamma,e(gamma)-(T/S)e_+(y)>.

Gaussian independence from the preceding section, together with the bounded density ratios between q_y and rho_y^*, bounds its clipped squared contribution by

C E_{rho_y^*} min{v||e(x)-(T/S)e_+(y)||²,1}.

For any 0≤f≤1, the square-root-density Cauchy–Schwarz argument gives E_P f≤3E_Q f+4H²(P,Q). Apply this with P=rho_y^*, Q=rho_y, then H²≤KL(rho_y||rho_y^*)/2. Remove the truncation only after this transfer to the true kernel. Averaging over the true next marginal, whose exact reverse marginal is p_k, gives

E KL(rho_k||rhohat_k)
≤C[E KL(rho_k||rho_k^*)+v epsilon_{k,score}²+(h²/v+vT²/S²)E||e_+||²].

Since v≤h and h²/v=vT²/S²=hT/S, this becomes

E KL(rho_k||rhohat_k)
≤C[epsilon+eta_k epsilon_{k,score}²+alpha_k² eta_k(1+eta_k/sigma_k²)epsilon_{k+1,score}²].       (G)

This explains both the terminal score contribution and the alpha factor missing from the previous proof.

## 6. Accumulation

Factoring the exact and approximate reverse joint laws gives

KL(p_1||phat_1)≤KL(p_K||phat_K)+sum_{k=1}^{K-1}E_{p_{k+1}}KL(rho_k||rhohat_k).

The small-step requirement makes eta_k/sigma_k² bounded by a numerical constant. The adjacent-weight condition alpha_k² eta_k≤eta_{k+1}, including k=K-1, absorbs the next-score terms in (G). Therefore

KL(p_1||phat_1)≤C[KL(p_K||phat_K)+(K-1)epsilon+sum_{k=1}^K eta_k epsilon_{k,score}²].

No transition with index K is simulated. Its positive eta_K is the weight needed for the queried terminal score.

## 7. Variance-preserving schedule and initialization

Fix nu in (0,1), alpha_0=sqrt(1-nu), and kappa=1+M_2²/nu. Put

L=log(e d_* kappa/delta),  G=C(d_*+L)L.

Define t_1=nu/(1-nu), and for reverse-transition indices choose eta_k=sigma_k²/G. The variance-preserving recurrence gives

t_{k+1}=(1+1/G)t_k,  t_k=sigma_k²/(1-sigma_k²).

Define eta_K=sigma_K²/G as the terminal weight. Then

alpha_k² eta_k/eta_{k+1}=G/(G+1)<1.

Choose n=K-1 to be at least one, at least log(1/delta), and at least log(max{1,M_2²/(2delta²t_1)})/log(1+1/G). The maximum handles M_2=0 without taking its logarithm. Since M_2²/t_1≤M_2²/nu≤kappa,

K=O((d_*+log(kappa/delta))log²(d_*kappa/delta)).

Also log(K/delta²)≤C L. Thus increasing the numerical constant in G makes every step satisfy the preceding theorem with epsilon=delta²/(C K), and in particular the weaker conditions requested at tolerance delta.

Convexity of KL under mixing and the equal-covariance Gaussian formula give, without requiring sigma_K² to be bounded away from zero,

KL(p_K||N(0,sigma_K²I))≤bar-alpha_K² M_2²/(2sigma_K²)=M_2²/(2t_K)≤delta².

The accumulated bound now gives KL(p_1||phat_1)≤C[delta²+sum_{k=1}^K eta_k epsilon_{k,score}²]. The query bound from Section 1 is O(K), because K≥log(1/delta).

## 8. Early stopping and bounded-Lipschitz error

Couple X_1=alpha_0 X_0+sqrt(nu)Z with X_0. Independence and centering give

W_2²(p_data,p_1)≤E||X_0-X_1||²=(1-alpha_0)²M_2²+nu d.

In the variance-preserving setting, 1-sqrt(1-nu)≤nu. Taking nu=c delta²/(d+M_2²), for any fixed sufficiently small positive numerical c, gives W_2²≤Cdelta². This choice is in (0,1) because d≥1.

The definition of D_BL gives D_BL(P,Q)≤W_2(P,Q) when the latter is finite, and D_BL(P,Q)≤2TV(P,Q). The triangle inequality, Pinsker, and the preceding KL bound therefore imply

D_BL(p_data,phat_1)²≤C[delta²+sum_{k=1}^K eta_k epsilon_{k,score}²].

For this nu, d_*≤d and log(e d_* kappa/delta)≤C log((d+M_2²)/delta²). Since d_*≥1, the step bound is O(d_*log³((d+M_2²)/delta²)), as is the high-probability query count.

All theorem-critical obligations are derived above. The separate Hölder, refined Frobenius, proximal-sampling, and Gaussian-optimality branches are not used.
