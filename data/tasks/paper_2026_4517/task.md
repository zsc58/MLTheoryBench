# Problem

## Setup

Let d≥1 and K≥2 be integers. Let X_0 have probability law p_data on R^d, with M_2²=E||X_0||²<∞. Fix positive parameters alpha_k and eta_k for k=0,...,K-1, and form the Markov chain

X_{k+1}=alpha_k X_k+alpha_k sqrt(eta_k) Z_k,

where the Z_k are independent N(0,I_d) vectors, independent of X_0. Write p_k for the law of X_k, bar-alpha_k=product_{j<k}alpha_j, and define sigma_0²=0 and

sigma_{k+1}²=alpha_k²(sigma_k²+eta_k).

Thus p_k is the law of bar-alpha_k X_0+sigma_k Z for an independent standard Gaussian Z. Set nu=sigma_1²=alpha_0² eta_0>0. For k≥1, also use p_k for its density. The variance-preserving setting means bar-alpha_k²+sigma_k²=1 for all k; in particular, 0<nu<1 and alpha_0=sqrt(1-nu).

For k=1,...,K, let s_k:R^d→R^d be fixed, finite-valued measurable score estimates, and define

s_k^*=grad log p_k,

epsilon_{k,score}²=E_{X~p_k}||s_k(X)-s_k^*(X)||²<∞,

D_k(x)=bar-alpha_k^{-1}(x+sigma_k² s_k(x)).

Let N(S;r) be the minimum number of closed Euclidean balls of radius r covering S, with value infinity if no finite cover exists, and log infinity=infinity. Define

d_* = min{d, max{1, inf_{r≥0}[log N(supp(p_data);r)+r² alpha_0²/nu]}}.

The exact reverse conditional density for k=1,...,K-1 is

rho_k(x|x') proportional to p_k(x) exp(-||x-alpha_k^{-1}x'||²/(2eta_k)).

In addition to the transition parameters, let eta_K>0 be a terminal score-error weight. It does not specify an additional transition.

## Sampling procedure

Use clipping level one, with Clip(u)=max{-1,min{1,u}}. Given a reverse input x' at transition k, set

v_k=(eta_k^{-1}+sigma_k^{-2})^{-1},

g_k(x')=alpha_k^{-1}x'+alpha_k eta_k s_{k+1}(x'),

q_k(.|x')=N(g_k(x'),v_k I_d).

One attempt to generate the next reverse state proceeds as follows.

1. Draw x~q_k(.|x') and J~Poisson(2), independently.
2. For each j=1,...,J, independently draw r_j uniform on [0,1], z_j~N(0,v_k I_d/2), and u_j~N(g_k(x'),v_k I_d/2), conditionally independently of x and J.
3. For r in [0,1], define

   a(r)=(1+2cos(2pi(1-r)/3))/3,

   b(r)=2sin(2pi(1-r)/3)/sqrt(3),

   gamma_{r,z,u}(x)=a(r)x+(1-a(r))u+b(r)z,

   dot-gamma_{r,z,u}(x)=a'(r)(x-u)+b'(r)z.

   Compute

   W_j=Clip((bar-alpha_k/sigma_k²)<dot-gamma_{r_j,z_j,u_j}(x), D_k(gamma_{r_j,z_j,u_j}(x))-D_{k+1}(x')>).

4. Accept x with probability product_{j=1}^J(1+W_j)/2, using an independent uniform random variable. The empty product is one. If rejected, repeat the attempt with fresh randomness.

Cache s_{k+1}(x') for this transition. Count each evaluation of any s_j as one score query. Apart from dependence through the current reverse input, use fresh independent randomness throughout the procedure.

Initialize with phat_K=N(0,sigma_K² I_d), apply this procedure for k=K-1,...,1, and denote the output law by phat_1.

For probability measures P,Q, let KL(P||Q)=E_P log(dP/dQ), with value infinity if P is not absolutely continuous with respect to Q, and let W_2²(P,Q) be the infimum of E||U-V||² over couplings. Define

D_BL(P,Q)=sup{|E_P f-E_Q f|: |f|≤1 and |f(x)-f(y)|≤||x-y|| for all x,y}.

All constants in O, asymp, and displayed constant-factor inequalities are universal; these notations do not hide logarithmic factors.

## Task

Prove the following integrated theorem.

There are universal constants C_0,C_1>0 such that, for every delta in (0,1/2], if for each k=1,...,K-1,

alpha_k² eta_k≤eta_{k+1},

sigma_k²/eta_k≥C_0[d_* log(1/delta)+log²(1/delta)],

then the sampling procedure terminates almost surely and

KL(p_1||phat_1)≤C_1[KL(p_K||phat_K)+(K-1)delta+sum_{k=1}^K eta_k epsilon_{k,score}²].

Moreover, in the variance-preserving setting, for every fixed early-noise variance nu in (0,1) and every delta in (0,1/2], there is a schedule, including the terminal weight eta_K, satisfying these conditions, with

K=O((d_*+log(kappa/delta))log²(d_*kappa/delta)),

kappa=1+M_2²/nu,

for which

KL(p_K||phat_K)≤delta²,

KL(p_1||phat_1)≤C_1[delta²+sum_{k=1}^K eta_k epsilon_{k,score}²],

and the total number of score queries is O(K) with probability at least 1-delta. The schedule may depend on the data law through nu, M_2, and d_*, but its guarantee holds for every collection of score estimates satisfying the setup.

Finally, prove

W_2²(p_data,p_1)≤(1-alpha_0)²M_2²+nu d.

In the variance-preserving setting, choosing nu asymp delta²/(d+M_2²) with a sufficiently small universal proportionality constant yields

D_BL(p_data,phat_1)²≤C_1[delta²+sum_{k=1}^K eta_k epsilon_{k,score}²],

with total score-query complexity O(d_* log³((d+M_2²)/delta²)) with probability at least 1-delta.
