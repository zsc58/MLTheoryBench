# Problem

## Setup

Fix an integer K at least 2 and let G be a class of predictors with benchmark-risk map rho:G to [0,1]^K. Assume that rho(G) is compact. Write f preceq_rho g when rho_k(f) is at most rho_k(g) for every k. Call f Pareto-optimal if there is no g in G such that g preceq_rho f and rho(g) is different from rho(f). Let

 Gamma={rho(f): f is Pareto-optimal} subset [0,1]^K.

For x,y in Gamma define the asymmetric Pareto distance

 delta(x,y)=max_{1<=k<=K}(x_k-y_k).

For t>0 and A subset Gamma, a finite set S subset A is a t-cover if every y in A has some x in S with delta(x,y) at most t. Let M(t,A) be the minimum cardinality of such a cover, with M(t,empty set)=0.

Assume Gamma is a compact smooth embedded (K-1)-dimensional submanifold with boundary. Let nu:Gamma to R^K be a continuous unit normal field, defined also on the boundary, such that nu_k(r) is at least eta for every r in Gamma and every k, for some eta>0. Let H_{K-1} denote (K-1)-dimensional Hausdorff measure on Gamma.

A set A subset Gamma is called Jordan measurable relative to Gamma if its boundary in the relative topology of Gamma has H_{K-1}-measure zero. All such sets are bounded here because Gamma is compact.

## Task

Prove that there exists a constant C_K>0 depending only on K, valid for every setup above, such that, with

 beta(v)=C_K product_{k=1}^K v_k/(sum_{k=1}^K v_k)^(K-1)

for positive unit vectors v in R^K, and

 mu(A)=integral_A beta(nu(r)) dH_{K-1}(r),

one has, for every Jordan-measurable A subset Gamma,

 lim_{t downarrow 0} M(t,A)t^(K-1)=mu(A).
