# Reference Proof

## Contract and obligations

The estimator minimizes the unpenalized empirical likelihood on the Euclidean ball. The positive scalar zeta regularizes the covariance geometry, not the objective. Model parameters and trajectory action sequences are fixed before the observation experiment. The proof must establish: (1) the conditional filter drift and its expectation bound; (2) simultaneous time-average concentration; (3) feature and covariance perturbation bounds; (4) the clean score concentration with its normalization; (5) constrained-likelihood error control, including the curvature and covariance-comparison factors; and (6) confidence and degenerate-case closure.

## 1. Elementary kernel and posterior comparisons

Use TV(p,q)=||p-q||_1/2. For a stochastic kernel K whose row overlaps are at least kappa, TV(Kp,Kq)<=(1-kappa)TV(p,q). Indeed, writing the positive and negative parts of p-q as tau times probability vectors, where tau=TV(p,q), expresses Kp-Kq as tau times the difference of two mixtures of rows. Convexity bounds their distance by the largest pairwise row distance, at most 1-kappa.

For a softmax row with feature vectors f_x of norm at most B and a unit parameter direction v, its directional derivative has coordinates p_x(<f_x,v>-sum_z p_z<f_z,v>). Its l1 norm is E|U-EU|<=sqrt(Var(U))<=B, since |U|<=B. Integrating along the parameter segment gives row l1 perturbation at most B times parameter distance. In particular, for every belief b and action a,

TV(P_theta^a b,P_theta*^a b)<=B delta(theta)/2,

and every observation row differs in l1 by at most B delta(w). The finite softmax kernels are strictly positive; on the compact feasible ball their entries have positive lower bounds. All Bayesian normalizations and absolute-continuity conditions used below therefore hold.

Here are direct derivations of the finite-space posterior inequalities needed from the specialized filtering dependency. For a positive observation kernel K, denote its observation marginal from prior p by Kp and its posterior given y by p_y. Splitting

(Kq)(y)(p_y(s)-q_y(s))=K(y|s)(p(s)-q(s))+p(s)K(y|s)((Kq)(y)/(Kp)(y)-1)

and summing absolute values over s,y gives

E_{y~Kq} TV(p_y,q_y)<=TV(p,q)+TV(Kp,Kq)<=(2-kappa_K)TV(p,q).

For two positive observation kernels K and K' with the same prior p, splitting their normalized posteriors in the same way gives

E_{y~K'p} TV(p_y^K,p_y^{K'})<=sum_s p(s)||K(.|s)-K'(.|s)||_1.

Finally, for f taking values in [0,1], |E_u f-E_v f|<=TV(u,v). These derivations close the required finite-space specialization of the nonstandard dependency; no unproved filtering theorem is assumed.

## 2. Conditional filter drift and expectation

Fix one trajectory. Let F_k be the sigma-field of its observations through k, with its prescribed actions included, and let X_k=TV(b_k^Theta,b_k^Theta*). Both beliefs are F_k-measurable. Conditional on F_k, the next observation has law Q_*P_*^{a_k}b_k^Theta*, where Q_* is the true observation kernel.

Write the Bayesian update as U_w(P_theta^{a_k}b,y). Insert the intermediate posteriors U_*(P_theta^{a_k}b_k^Theta,y) and U_*(P_*^{a_k}b_k^Theta,y). This gives three nonnegative TV terms I, II, III for observation mismatch, transition mismatch, and propagation.

For I, first average under Q_*P_theta^{a_k}b_k^Theta. The same-prior kernel comparison bounds that expectation by B delta(w). Changing to the true observation law costs at most

(1-kappa_Phi)[(1-kappa_P)X_k+B delta(theta)/2].

Consequently,

E[I|F_k]<=B delta(w)+(1-kappa_Phi)B delta(theta)/2+(1-kappa_Phi)(1-kappa_P)X_k.

For II, average first under Q_*P_*^{a_k}b_k^Theta. The posterior comparison bounds this by (2-kappa_Phi)B delta(theta)/2. Changing to the true law costs at most (1-kappa_Phi)(1-kappa_P)X_k. Thus

E[II|F_k]<=(2-kappa_Phi)B delta(theta)/2+(1-kappa_Phi)(1-kappa_P)X_k.

For III, the posterior comparison and transition contraction apply directly under the true law:

E[III|F_k]<=(2-kappa_Phi)(1-kappa_P)X_k.

Adding gives E[X_{k+1}|F_k]<=alpha X_k+c, with the alpha and c in the task. Since X_0=0, iterating expectations gives

E X_t<=c sum_{j=0}^{t-1}alpha^j=c(1-alpha^t)/(1-alpha)

for t>=1. The t=0 conclusion is immediate and equals zero.

## 3. Time-average concentration with a valid deterministic boundary

This step repairs the source's unsupported substitution of a random predictable variance into a square-root Freedman boundary. It uses only boundedness and the same conditional drift, and proves the source's unchanged bound.

Put beta=1-alpha, Z=sum_{t=0}^{T-1}X_t, a_t=E[X_t|F_{t-1}], A=sum_t a_t, with a_0=0. Summing the drift and using X_0=0 and X_t>=0 gives A<=alpha Z+Tc. For h=exp(beta)-1, convexity on [0,1] gives exp(beta x)<=1+hx. Therefore

E[exp(beta X_t)|F_{t-1}]<=1+h a_t<=exp(h a_t).

Iterated conditioning yields E exp(beta Z-h A)<=1. Markov's inequality implies that, except on an event of probability at most eta,

(beta-alpha h)Z<=hTc+log(1/eta).

For 0<beta<=1, the exponential power series and n!>=2^(n-1) imply h<=2beta/(2-beta). Since alpha=1-beta, this gives beta-alpha h>=beta^2/(1+alpha)>0 and hence

Z/T<=2c/beta+(1+alpha)log(1/eta)/(T beta^2).

Because 1+alpha<=(4+2alpha)/3, this implies

Z/T<=2c/beta+(2/beta)sqrt(2c log(1/eta)/T)+log(1/eta)(4/3+2alpha/beta)/(T beta).

Take eta=delta_b/(2N) for each of the 2N trajectories. Their union bound, which does not require independence within a pair, produces an event E_b of probability at least 1-delta_b on which every trajectory's time-average TV error is at most epsilon_b in the task. This argument covers T=1, c=0, and alpha=0 without division by zero.

## 4. Feature and covariance perturbations

For any beliefs b,b',

||bar psi(b,a)-bar psi(b',a)||_2<=sum_s |b(s)-b'(s)| ||psi(s,a)||_2<=2B_r TV(b,b').

Also ||bar psi(b,a)||_2<=B_r, so ||phi_i||_2 and ||tilde phi_i||_2 are at most 2TB_r. On E_b, summing the Lipschitz bound over both trajectories gives

||Delta_i||_2<=q:=4TB_r epsilon_b, where Delta_i=tilde phi_i-phi_i.

Expand the covariance difference:

E:=tilde Sigma-Sigma=N^(-1)sum_i(phi_i Delta_i^T+Delta_i phi_i^T+Delta_i Delta_i^T).

Using ||uv^T||_op<=||u||_2||v||_2 gives

||E||_op<=4TB_r q+q^2=16T^2B_r^2 epsilon_b(1+epsilon_b)=:H.

If H>0, zeta=c_zeta H and therefore

tilde Sigma+zeta I >= (1-1/c_zeta)(Sigma+zeta I)

in positive-semidefinite order. Inverting yields, for every v,

||v||_{(tilde Sigma+zeta I)^(-1)}<=sqrt(c_zeta/(c_zeta-1))||v||_{(Sigma+zeta I)^(-1)}.

If H=0, E=0 on E_b and the comparison holds with factor 1 for any positive zeta, so it also holds with the displayed larger factor.

## 5. Clean-score concentration

The standard independent self-normalized inequality used here has the following form. For predictable vectors x_i, conditionally mean-zero, conditionally 1-sub-Gaussian scalars xi_i, and deterministic V_0 positive definite, put S=sum_i xi_i x_i and V=V_0+sum_i x_i x_i^T. With probability at least 1-eta,

||S||_{V^(-1)}<=sqrt(log(det V/det V_0)+2log(1/eta)).

Condition on all clean features. Independence of the comparison pairs and preference realizability imply that the labels are independent with the specified Bernoulli probabilities under this conditioning. Thus xi_i=sigma(<mu*,phi_i>)-y_i are conditionally mean zero and, being bounded in [-1,1], are conditionally 1-sub-Gaussian. Reveal the labels sequentially with the clean features in the initial sigma-field; the vectors phi_i are predictable. The parameters and tuning are fixed, so V_0=N zeta I is deterministic and positive definite. The theorem therefore applies and its conditional confidence bound integrates to the same unconditional bound.

For the normalized clean likelihood L,

nabla L(mu*)=N^(-1)S, V=N(Sigma+zeta I),

so, on an event E_c of probability at least 1-delta_c,

||nabla L(mu*)||_{(Sigma+zeta I)^(-1)}<=N^(-1/2)sqrt(log det(I+Sigma/zeta)+2log(1/delta_c)).

The eigenvalues of Sigma are nonnegative and tr Sigma=N^(-1)sum_i||phi_i||_2^2<=4T^2B_r^2. The arithmetic-geometric mean inequality applied to the d eigenvalues of I+Sigma/zeta gives

log det(I+Sigma/zeta)<=d log(1+4T^2B_r^2/(zeta d)).

Denote the resulting clean-score upper bound by G.

## 6. Constrained likelihood, mismatch, and final bound

Let tilde L be the normalized unpenalized likelihood. Its Hessian is

nabla^2 tilde L(mu)=N^(-1)sum_i sigma(<mu,tilde phi_i>)(1-sigma(<mu,tilde phi_i>))tilde phi_i tilde phi_i^T.

On the parameter ball, |<mu,tilde phi_i>|<=2TB_r r_mu, so the explicit rho in the task gives nabla^2 tilde L(mu)>=rho tilde Sigma. Taylor expansion along mu*+t(tilde mu-mu*) and constrained optimality imply, for e=tilde mu-mu*,

(rho/2)||e||_{tilde Sigma}^2<=-<nabla tilde L(mu*),e>.

Set u=||e||_{tilde Sigma+zeta I} and a=||nabla tilde L(mu*)||_{(tilde Sigma+zeta I)^(-1)}. Since ||e||_2<=2r_mu,

(rho/2)u^2<=a u+2rho zeta r_mu^2.

Solving this quadratic gives u<=2a/rho+2r_mu sqrt(zeta). No penalty term in the optimization objective has been used.

For the gradient mismatch, write

(sigma(<mu*,tilde phi_i>)-y_i)tilde phi_i-(sigma(<mu*,phi_i>)-y_i)phi_i

=[sigma(<mu*,tilde phi_i>)-sigma(<mu*,phi_i>)]phi_i+[sigma(<mu*,tilde phi_i>)-y_i]Delta_i.

The sigmoid is 1/4-Lipschitz, its residual has absolute value at most 1, and ||mu*||_2<=r_mu. Therefore each difference has norm at most (1+TB_r r_mu/2)||Delta_i||_2. On E_b,

||nabla tilde L(mu*)-nabla L(mu*)||_{(tilde Sigma+zeta I)^(-1)}<=q(1+TB_r r_mu/2)/sqrt(zeta).

Combining this with the covariance comparison and the clean-score bound gives, on E_b intersect E_c,

u<= (2/rho)sqrt(c_zeta/(c_zeta-1))G + 2q(1+TB_r r_mu/2)/(rho sqrt(zeta)) + 2r_mu sqrt(zeta).

Here the symbol on the left is u, the error norm defined above. Substituting G and q gives exactly g_stat+g_mis+2r_mu sqrt(zeta). The union bound gives probability at least 1-delta_b-delta_c.

If B_r=0, all clean and perturbed features and both covariance matrices vanish; every constrained likelihood minimizer has error at most 2r_mu in Euclidean norm, so the conclusion follows directly for every positive zeta. If r_mu=0, the parameter error is identically zero. These cases are also consistent with the formulas and complete the boundary checks.

All theorem-critical obligations are closed.
