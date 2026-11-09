# Problem

## Setup

Let n and p be positive integers. Let (x_i,w_i)_{i=1}^n be observed pairs, with x_i in a set X, and let psi(x)=(psi_1(x),...,psi_p(x))^T be a fixed finite basis of real-valued functions on X. Let V be the real linear span of these basis functions. For each w, let m(w,.) be a real-valued linear functional on V.

Let G(x,a) be a differentiable convex generator on a nonempty convex domain A(x) contained in R, with conjugate

G*(x,v)=sup_{a in A(x)} {a v-G(x,a)}.

For beta in R^p, define t_beta(x)=psi(x)^T beta and Omega_q(beta)=q^{-1} sum_j |beta_j|^q, where 1<=q<infinity.

For every parameter value used below, assume the inverse-link value a_beta(x) in A(x) exists and satisfies partial_a G(x,a_beta(x))=t_beta(x). Assume also that G*(x,.) is finite and differentiable at t_beta(x), with partial_v G*(x,t_beta(x))=a_beta(x). In particular, these conditions hold at the fitted minimizer defined below.

For lambda>=0, define

L_lambda(beta)=n^{-1} sum_i [G*(x_i,t_beta(x_i))-m(w_i,t_beta)] + lambda Omega_q(beta).

Assume L_lambda has a finite-valued empirical minimizer beta_hat over R^p. Write a_hat(x)=a_beta_hat(x).

When referring to the unregularized case, assume the balancing constraints are feasible: there exists a function a with a(x) in A(x) such that

n^{-1} sum_i [a(x_i)psi_j(x_i)-m(w_i,psi_j)]=0

for every j=1,...,p.

## Task

Prove the following theorem. For every coordinate j=1,...,p, define

Delta_j=n^{-1} sum_i [a_hat(x_i)psi_j(x_i)-m(w_i,psi_j)].

There exists s in partial Omega_q(beta_hat) such that Delta_j+lambda s_j=0 for all j. Here partial denotes the convex subdifferential. Consequently: (i) if q=1, |Delta_j|<=lambda for every j; (ii) if q>1, |Delta_j|=lambda|beta_hat_j|^(q-1) for every j; and (iii) if lambda=0 (with feasible balancing constraints), Delta_j=0 for every j, i.e. the sample moments balance exactly.
