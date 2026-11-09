# Reference Proof

## Proof Structure

Derive uniform effective-linearity and dissipative bounds for the tamed drift. Establish the polynomial Lyapunov inequality, including the endpoint q=2, and iterate it. Construct invariant measures by the Feller/Cesaro-average argument and prove the moment bound for every invariant measure without assuming its integrability. Finally, prove compact generator convergence, control the off-compact contribution using one fixed admissibility order, and apply stationary identification.

All constants below may depend on the fixed data and on explicitly fixed moment orders or test functions, but not on the state, iteration index, sufficiently small step size, or choice of invariant measure. The family-specific moment constant is denoted by M.

## Step 1: Uniform envelope and dissipative bounds

Write t=||x||, a=eta^alpha, and D_eta(x)=eta b_eta(x). For 0<eta<=1,

1+aA(x) >= a(1+A(x)).

Consequently, the envelope compatibility assumption gives

||D_eta(x)|| <= C_A eta^(1-alpha)(1+t).                                           (1)

Let K_0=1+L_A. The upper envelope bound gives

1+eta^alpha A(x) <= K_0(1+t^r).

For t>=1, t^(r+2)/(1+t^r)>=t^2/2; for 0<=t<=1, that quotient is nonnegative. Thus, for all t>=0,

t^(r+2)/(1+t^r) >= (t^2-1)/2.

Because b_0>=0, dissipativity now yields

<x,b_eta(x)> <= b_0 - (m/K_0)t^(r+2)/(1+t^r)
              <= B-a_0 t^2,                                                     (2)

where a_0=m/(2K_0)>0 and B=b_0+a_0. Both constants are independent of eta.

## Step 2: Polynomial Lyapunov drift and iteration

For every real q>=2 there is a finite K_q such that

V_q(x+u)-V_q(x)
<= q||x||^(q-2)<x,u>
   + K_q(1+||x||^(q-2))||u||^2 + K_q||u||^q.                                    (3)

Here the linear term is zero at x=0, and the factor ||x||^0 for q=2 is interpreted as 1. To establish (3), when x is nonzero and ||u||<=||x||/2, apply Taylor's formula along x+su and use the Hessian bound for ||y||^q by a constant times ||x||^(q-2). When ||u||>||x||/2, use ||x||<=2||u|| to bound the function increment minus its linear term by a constant times ||u||^q. The case x=0 follows directly. This proves (3) for all real q>=2.

Set sigma=sqrt(2 beta^(-1)) and Delta=D_eta(x)+sigma sqrt(eta) xi. For every fixed real s>=2, (1), the elementary inequality ||v+w||^s<=C_s(||v||^s+||w||^s), and the finite Gaussian s-th moment give

E||Delta||^s <= K_s eta^[s(1-alpha)](1+t^s)+K_s eta^(s/2).                        (4)

Also E Delta=eta b_eta(x). From (2), and the inequality t^(q-2)<=epsilon t^q+C_(epsilon,q), which also holds for q=2,

q eta t^(q-2)<x,b_eta(x)> <= -lambda_q eta t^q+B_q eta                           (5)

for some lambda_q>0.

Apply (3), take expectations, and use (4) with s=2 and s=q. Since

(1+t^(q-2))(1+t^2) <= K_q(1+t^q),

the result is bounded by

Q_eta V_q(x)-V_q(x)
<= -lambda_q eta t^q+B_q eta
   +K_q[eta^(2-2alpha)+eta^[q(1-alpha)]](1+t^q)
   +K_q eta(1+t^(q-2))+K_q eta^(q/2).                                           (6)

Use Young's inequality to bound K_q(1+t^(q-2)) by (lambda_q/4)t^q plus a constant. Since 2-2alpha>1 and q(1-alpha)>1, choose a positive eta_q<=1 so that the coefficient of t^q in the square-bracket term of (6) is at most (lambda_q/4)eta whenever eta<=eta_q. Every remaining state-independent term is O(eta), including eta^(q/2); at q=2 this last term is exactly of order eta and is not treated as o(eta). Therefore

Q_eta V_q(x)-V_q(x) <= -(lambda_q/2)eta t^q+C'_q eta.

Writing t^q=V_q(x)-1 gives constants c_q,C_q>0 with

Q_eta V_q <= (1-c_q eta)V_q+C_q eta.                                            (7)

Decrease eta_q further so that 0<=rho_eta:=1-c_q eta<1. Iteration of (7) gives

Q_eta^k V_q(x) <= rho_eta^k V_q(x)+(C_q/c_q)(1-rho_eta^k).                        (8)

For any initial distribution with finite q-th moment, integration of (8) gives the corresponding uniform-in-time trajectory moment bound.

## Step 3: Invariant measures and moments without circular integration

The maps b and A are continuous, so x -> x+eta b_eta(x) is continuous for fixed eta. If h is bounded and continuous, dominated convergence in the Gaussian expectation shows that Q_eta h is bounded and continuous. Thus Q_eta is Feller.

The independent compactness principle used here is that a tight sequence of probability measures on R^d has a weakly convergent subsequence. For completeness, the Feller invariant-measure implication is verified directly. Fix x and eta<=eta_q and form

nu_n=(1/n) sum_(k=0)^(n-1) delta_x Q_eta^k.

Equation (8) gives nu_n(V_q)<=V_q(x)+C_q/c_q. Since V_q tends to infinity at infinity, these probability measures are tight. Take a weakly convergent subsequence with limit nu. For h bounded and continuous,

nu_n(Q_eta h)-nu_n(h)=[Q_eta^n h(x)-h(x)]/n -> 0.

Both h and Q_eta h are bounded continuous functions, so weak convergence gives nu(Q_eta h)=nu(h). Bounded continuous functions determine probability measures on R^d; hence nu Q_eta=nu.

Now let nu be any invariant probability measure, without assuming nu(V_q)<infinity. Put V=V_q and V_N=min(V,N). If V(x)<=N, then

Q_eta V_N(x)-V_N(x) <= Q_eta V(x)-V(x) <= -c_q eta V(x)+C_q eta.

If V(x)>N, then Q_eta V_N(x)-V_N(x)<=0 because V_N<=N. Integrating these bounds against nu is legitimate because V_N and Q_eta V_N are bounded. Invariance therefore gives

0 <= -c_q eta integral_{V<=N} V dnu+C_q eta nu(V<=N).

Let N increase to infinity. Monotone convergence proves

nu(V_q) <= C_q/c_q.                                                            (9)

This establishes the claimed bound for every invariant measure, uniformly for eta<=eta_q, and one may take M_q=C_q/c_q.

## Step 4: Tightness and local generator consistency

Let p=Q_*>=2 be fixed and let (mu_eta) be p-admissible. Write

M=sup_(0<eta<=eta_0) integral V_p dmu_eta < infinity.

For any R>0, mu_eta({||x||>R})<=M R^(-p), so the family is tight. Given a sequence eta_j decreasing to zero, pass to a subsequence, retaining the same notation, for which mu_eta_j converges weakly to a probability measure mu_*.

Fix f in C_c^infinity and a compact K. On K, both b and A are bounded, and

sup_K ||b_eta-b|| <= eta^alpha (sup_K A)(sup_K ||b||) -> 0.

Also sup_K ||b_eta|| is uniformly bounded. The derivatives of f through order three are globally bounded. Taylor expansion, together with

E Delta=eta b_eta(x),
E[Delta Delta^T]=eta^2 b_eta(x)b_eta(x)^T+sigma^2 eta I_d,

therefore gives

Q_eta f(x)-f(x)
=eta <b_eta(x),grad f(x)>+beta^(-1)eta Delta f(x)
 +(eta^2/2)b_eta(x)^T Hess f(x)b_eta(x)+R_eta(x),

where sup_K |R_eta|<=C_(f,K) eta^(3/2), using the Gaussian third moment and the compact bound on b_eta. Consequently, for

G_eta f=(Q_eta f-f)/eta,

sup_K |G_eta f-Lf| -> 0.                                                       (10)

The function Lf is continuous, bounded, and supported in supp f. In particular, the identification assumption involves well-defined finite integrals for every probability measure.

## Step 5: Quantitative off-compact control and stationary identification

If f=0, there is nothing to prove. Otherwise choose R>=1 with supp f contained in the closed ball of radius R, and let K be the closed ball of radius R+1. Set

B_eta={x: ||D_eta(x)||>1/2}.

For x in K^c outside B_eta, a transition landing in supp f requires ||sigma sqrt(eta) xi||>=1/2. The Gaussian exponential moment E exp(||xi||^2/4)=2^(d/2) gives

P(||sigma sqrt(eta) xi||>=1/2)
<=2^(d/2) exp[-1/(16 sigma^2 eta)].                                             (11)

Let C be the constant in (1). For sufficiently small eta such that C eta^(1-alpha)<=1/4, the implication

x in B_eta => ||x||>(4C)^(-1) eta^(-(1-alpha))

follows directly from (1). Markov's inequality and the single fixed p-th moment bound thus give

mu_eta(B_eta) <= M(4C)^p eta^[p(1-alpha)].                                       (12)

Combining (11) and (12),

integral_(K^c) Q_eta |f|(x)/eta dmu_eta(x)
<= C_f eta^(-1) exp(-c_f/eta)+C_f M eta^[p(1-alpha)-1] -> 0,                      (13)

because p>=2 and alpha<1/2 imply p(1-alpha)-1>0. Neither arbitrarily high moments nor an eta-dependent moment order is used.

For each eta, boundedness of f and invariance imply integral G_eta f dmu_eta=0. Since f=Lf=0 on K^c, equations (10) and (13) imply

|integral (G_eta f-Lf) dmu_eta|
<=sup_K |G_eta f-Lf|+integral_(K^c) Q_eta |f|/eta dmu_eta ->0.

This compares the two globally defined integrals and does not require that the boundary of K have zero limiting mass. As Lf is bounded continuous, weak convergence along the selected subsequence yields

integral Lf dmu_*=0.

The argument applies to every f in C_c^infinity. Stationary identification gives mu_*=pi. Every sequence of step sizes tending to zero is tight and has no other possible subsequential weak limit. It follows that the full family mu_eta converges weakly to pi.

The proof establishes the public existential threshold with Q_min=2. This value and the tail estimates belong to the private proof, not to the public assumptions.

## Obligation Closure

The envelope estimates, polynomial increment bound, absorption including q=2, invariant-measure construction, arbitrary-invariant-measure moment bound, compact generator expansion, off-compact estimate, and full-family stationary identification have all been derived. The only independent compactness principle used is the standard tightness/weak-subsequence result on R^d, and its hypotheses have been verified. There is no unresolved specialized dependency or private proof gap.
