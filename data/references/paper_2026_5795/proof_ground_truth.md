# Reference Proof

## Proof obligations

We establish: (1) well-defined positive updates in the stated diffuse observation-space interpretation; (2) low-mass parameter and covariance bounds; (3) the one-round score bound; (4) aggregation through the admissible quantity; (5) the Lambert-W threshold, including its branch-point case; and (6) a positive invariant sequence converging to zero. No specialized external theorem is needed. The elementary matrix identities and scalar inequalities are derived below. The standard digamma fact used is psi'(z)=sum_{m=0}^infinity (z+m)^{-2}>0 for z>0; all its arguments below are positive.

## 1. Domains and low-mass parameter bounds

Fix a round with 0<beta<s. This implies M>0. The incoming observation-space moments m^- and S^- are finite, with S^- positive definite. Each summand defining G is positive semidefinite, and G is finite. Therefore Phi=((Phi')^{-1}+G)^{-1} is finite and positive definite. Set Q=phi Phi, also positive definite. The updated shape parameters satisfy eta=eta'+beta>0 and phi=phi'+beta>D-1.

Strict monotonicity of psi gives

psi(eta)<psi(eta'+s).

Every argument in psi_D(phi/2)=sum_{i=1}^D psi((phi+1-i)/2) is positive. Applying the same monotonicity term by term gives

psi_D(phi/2)<psi_D((phi'+s)/2).

Writing K=(Phi')^{1/2}G(Phi')^{1/2}, we have K positive semidefinite and

Phi=(Phi')^{1/2}(I+K)^{-1}(Phi')^{1/2}.

Consequently |Phi|=|Phi'|/|I+K|<=|Phi'|, so log|Phi|<=log|Phi'|.

## 2. Diffuse state update and positivity

For finite tau, write R=(beta Q)^{-1}. The matrix identity

(A^{-1}+H^T R^{-1}H)^{-1}=A-AH^T(R+HAH^T)^{-1}HA

holds for positive-definite A and R, as can be checked by multiplication. Apply it with A=Sigma' and H Sigma' H^T=tau I. It gives

H Sigma H^T=tau I-tau^2(R+tau I)^{-1}=(beta Q+tau^{-1}I)^{-1}.

The round's incoming moments and its updated Q are fixed when taking this state-update limit. Thus, in the specified observation-space limit,

H Sigma H^T=(beta Q)^{-1},

Tr(Q H Sigma H^T)=D/beta.

For completeness, if v=sum_j r_j y_j and m'=Hmu', the same Gaussian update gives

Hmu=(tau^{-1}I+beta Q)^{-1}(tau^{-1}m'+Qv).

Its limit is v/beta, which is finite. Hence the outgoing observation-space mean and covariance are finite, and the covariance is positive definite. They are valid incoming moments for the next round.

Every factor in u_j is now finite and strictly positive. Since lambda_c>0 and c_j is finite and nonnegative, 0<r_j^+<1. In particular beta^+>0. This verifies that subsequent ratios and positive-mass state updates remain meaningful; it does not assert a state update at beta=0.

## 3. One-round association bound

Let d_j=exp((y_j-Hmu)^T Q(y_j-Hmu)/2). Then 1<=d_j<infinity. Inserting the strict digamma bounds, determinant bound, and trace identity into the score yields

u_j/lambda_c < (C_s/d_j) exp(-D/(2beta)).

The function z/(1+z) is strictly increasing on z>0. Nonnegative competing scores therefore give

r_j^+ <= u_j/(lambda_c+u_j)
       < 1-1/[1+(C_s/d_j)exp(-D/(2beta))].                         (1)

## 4. Aggregation

For 0<a<=alpha and 0<x<=1,

1-1/(1+ax) <= [1-1/(1+a)](alpha+1)/(alpha+1/x).                 (2)

Indeed, after cancellation of positive factors, (2) is equivalent to

(1+a)(alpha x+1)<=(alpha+1)(1+ax).

The right side minus the left side is (alpha-a)(1-x)>=0.

Apply (2) with a=C_s exp(-D/(2beta)), alpha=T_s, and x=1/d_j. Since beta<s, a<alpha. Summing (1) and (2) over the nonempty finite observation set gives

beta^+<h(beta) Delta,

h(x)=1-1/[1+C_s exp(-D/(2x))],  x>0.                           (3)

In particular Delta>0. Define F(x)=B h(x). Admissibility applies to the complete current configuration, including the incoming moments, and gives Delta<=B.

## 5. Scalar threshold and Lambert-W branches

For arbitrary p,q,r,x>0, consider

x>p[1-1/(1+q exp(-r/x))].                                     (4)

Set t=r/p-r/x. Then t<r/p and x=r/(r/p-t). Multiplying (4) by positive denominators and using exp(-r/x)=exp(t-r/p) shows that (4) is equivalent to

t exp(t)>-(r/(pq))exp(r/p).                                   (5)

This equivalence holds for every x>0, not just x<p.

The derivative of t exp(t) is exp(t)(1+t). Its global minimum is -1/e at t=-1; it decreases on (-infinity,-1) and increases on (-1,infinity). Put A_*=(pq/r)exp(-r/p), so the right side of (5) is -1/A_*.

If A_*<e, then -1/A_*<-1/e, and (5) holds for every x>0.

If A_*>=e, its right side is in [-1/e,0). Let w_-=W_{-1}(-1/A_*) and w_+=W_0(-1/A_*). The strict inequality holds exactly when t<w_- or t>w_+. At A_*=e the roots coincide at -1, and equality at that point remains excluded. Since t=r/p-r/x is strictly increasing in x, the lower interval is

0<x<[1/p-W_{-1}(-(r/(pq))exp(r/p))/r]^{-1}.

The upper interval is x>[1/p-W_0(-(r/(pq))exp(r/p))/r]^{-1}. Both denominators are positive because both roots are negative. The upper interval is not needed for the invariant threshold.

Take p=B, q=C_s, r=D/2. Then A_*=A. For A<e, F(x)<x for all x>0. For A>=e, F(x)<x whenever 0<x<V. V is evaluated only in this latter case, where it is positive and real, including A=e. Thus the public definition of L gives

0<x<L implies x<s and F(x)<x.                                (6)

## 6. Invariance and convergence

Let beta_0 satisfy 0<beta_0<L. Suppose 0<beta_n<L. The preceding finiteness argument ensures that the next round is defined and beta_{n+1}>0. Equations (3), (6), positivity of Delta_n, and admissibility yield

0<beta_{n+1}<F(beta_n) Delta_n/B
             <beta_n Delta_n/B<=beta_n<L.

Division by beta_n proves the asserted per-round ratio bound. Induction proves that all subsequent masses are positive, remain below the same fixed L, and decrease strictly.

The sequence has a limit ell>=0. If ell>0, then ell<=beta_0<L. Equation (3) and Delta_n<=B give beta_{n+1}<F(beta_n). Continuity of F on (0,infinity) gives ell<=F(ell), while (6) gives F(ell)<ell, a contradiction. Therefore ell=0.

When M=0 the positive-mass premise is impossible. No separate zero-mass state update or absorption assertion is needed. This proves the stated guarantee.
