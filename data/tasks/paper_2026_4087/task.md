# Problem

## Setup

Let x_1,...,x_n and y_1,...,y_m be evaluated and reference length-L sliding-window segments in R^{L×d}, where n,m>=2. Their observed labels are ell_1,...,ell_n and eta_1,...,eta_m in a common label set. Let Psi be a fixed multi-scale wavelet representation with finite real coefficient vectors, and define

d_wav(u,v)=||Psi(u)-Psi(v)||_1.

For each i and j, let

I_i={p: ell_p=ell_i},   J_j={q: eta_q=eta_j},

P_i=(1/|I_i|)sum_{p in I_i}delta_{x_p},   Q_j=(1/|J_j|)sum_{q in J_j}delta_{y_q},

where delta_u is the unit point mass at u. Thus P_i and Q_j are the empirical distributions of segments conditional on the corresponding observed labels. Define the label-consistency cost by

d_lab(x_i,y_j)=W_{d_wav}(P_i,Q_j),

where W_{d_wav}(P,Q) is the minimum of the integral of d_wav(u,v) over all probability couplings with first marginal P and second marginal Q. Assume these costs are finite. For fixed c>=0, set

D_ij=d_wav(x_i,y_j)+c d_lab(x_i,y_j).

The data, labels, representation, and resulting finite cost matrix D remain fixed as the masses below vary. Fix kappa>0.

For positive probability vectors a in (0,infinity)^n and b in (0,infinity)^m, with sum_i a_i=sum_j b_j=1, define

W(a,b)=min_{T in R_+^{n×m}} [sum_{i,j}D_ij T_ij+kappa sum_i a_i h((T1_m)_i/a_i)+kappa sum_j b_j h((T^T1_n)_j/b_j)],

where 1_s denotes the vector of s ones, h(t)=t log t-t+1 for t>0, and h(0)=1. Write

Delta_n=(1/n,...,1/n),   Delta_m=(1/m,...,1/m),   W_SW=W(Delta_n,Delta_m).

The sign convention for dual potentials is as follows: when independent marginal variables r and s are introduced, f and g are the multipliers with terms f·(r-T1_m) and g·(s-T^T1_n), respectively.

## Task

Prove that the KL-unbalanced transport problem has unique optimal dual potentials for every such a and b. Let (f*,g*) denote these potentials at a=Delta_n and b=Delta_m, and let psi_kappa(u)=kappa(1-exp(-u/kappa)). Prove that, for each evaluated segment, the score

v(x_i)=-[psi_kappa(f_i*)-(1/(n-1))sum_{k!=i}psi_kappa(f_k*)]

is exactly the negative directional derivative of W(a,Delta_m) at a=Delta_n along the mass-preserving perturbation

a_i(delta)=1/n+delta,   a_k(delta)=1/n-delta/(n-1) for k!=i,

for delta in a neighborhood of zero where all masses are positive. Explain why a positive score means that increasing the mass of segment x_i, while compensating uniformly across the others, decreases the discrepancy to first order.
