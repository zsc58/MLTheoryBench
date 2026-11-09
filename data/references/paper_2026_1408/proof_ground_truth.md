# Reference Proof

## Proof Structure

1. Establish the auxiliary-marginal identity and solve the unrestricted pointwise regularized problem.
2. Verify measurable assembly of its minimizers and derive the average-budget duality by a scalar convex-value argument.
3. Identify the dual value with Sibson alpha-mutual information and derive the joint law and posterior.
4. Prove feasibility and optimality of the regularized law at an interior dual maximizer.

## Complete Proof

Fix a policy pi. Write P_xi(theta,x)=p(theta)p(x|theta,xi), F(q)=E_pi U(xi,q), and G(q)=E_pi KL(q_xi||P_xi). The domain consists of all measurable conditional joint densities, without additional restrictions.

### Auxiliary marginal

The KL chain rule gives, as an equality of nonnegative extended-real quantities,

KL(q_xi||p(theta)nu(x|xi)) = U(xi,q) + KL(q(x|xi)||nu(x|xi)).

For finite quantities this follows by splitting the logarithm; the extended form follows by the relative-entropy chain rule. Therefore U(xi,q)=inf_nu KL(q_xi||p(theta)nu), attained at nu=q(x|xi). This uses the fixed nominal prior, not the theta marginal of q.

### Pointwise minimization

Fix beta>0 and set alpha=beta/(1+beta). Let A_nu=p(theta)nu(x|xi),

Z_nu=integral A_nu^(1-alpha) P_xi^alpha dtheta dx.

If Z_nu=0, the two laws have disjoint supports up to null sets, and no probability density has finite KL to both. The corresponding regularized infimum and Renyi divergence are both infinite. If Z_nu>0, define r_nu=A_nu^(1-alpha)P_xi^alpha/Z_nu. Direct logarithmic expansion gives

KL(q||A_nu)+beta KL(q||P_xi)
= (1+beta)KL(q||r_nu)-(1+beta)log Z_nu.

The minimizer over all normalized joint densities is r_nu, and its value is D_alpha(P_xi||A_nu), since 1/(alpha-1)=-(1+beta). The relevant KL integrals at r_nu are finite: on the common support, an interior power t^alpha times |log t| is bounded by a constant times t^(alpha-h)+t^(alpha+h), where 0<alpha-h<alpha+h<1; both overlap integrals are at most one by Holder's inequality. Thus the calculation does not rely on cancelling infinities.

Put m_alpha(x|xi)=integral p(theta)p(x|theta,xi)^alpha dtheta and S_alpha(xi)=integral m_alpha(x|xi)^(1/alpha)dx. Then

Z_nu=integral nu(x|xi)^(1-alpha)m_alpha(x|xi)dx
<= S_alpha(xi)^alpha

by Holder's inequality. Equality holds at nu=p_alpha=m_alpha^(1/alpha)/S_alpha. Since the coefficient 1/(alpha-1) is negative, maximizing Z_nu minimizes the divergence. Consequently

J_beta(xi):=inf_q {U(xi,q)+beta KL(q||P_xi)}
= inf_nu D_alpha(P_xi||p(theta)nu)
= I_alpha^S(theta;x|xi)
= -beta log S_alpha(xi).

The minimizing joint law is r_{p_alpha}. Its outcome marginal is p_alpha, because

integral r_{p_alpha}(theta,x)dtheta
= p_alpha(x)^(1-alpha)m_alpha(x)/S_alpha^alpha
= p_alpha(x).

Hence it also minimizes the original regularized utility, not merely the auxiliary two-variable objective. This establishes existence of q_alpha^* and its geometric-mixture formula. The integral measurability and normalization hypotheses make these formulas measurable in xi, so they assemble into a permissible kernel for every beta>0.

The source's L000614 coefficient for the joint overlap integral is locally corrected: the value is -(1+beta)log Z_{p_alpha}=-beta log S_alpha, not -beta log Z_{p_alpha}.

### Separation and duality

The pointwise inequality gives F(q)+beta G(q)>=E_pi J_beta. The measurable kernel q_alpha^* attains equality. Moreover, the strictly feasible finite-objective kernel q0 in the task gives

E_pi J_beta <= F(q0)+beta G(q0)<infinity.

Thus F(q_alpha^*) and G(q_alpha^*) are finite, and

inf_q {F(q)+beta G(q)}=E_pi J_beta.

Convexity of G follows from convexity of relative entropy. Convexity of F follows from joint convexity of relative entropy, since both q and p(theta)q(x|xi) depend affinely on the joint density q. Integration preserves these properties.

Define v(r)=inf_{G(q)<=r}F(q). Mixtures of kernels show that v is convex and nonincreasing. Since F>=0 and q0 has finite F with G(q0)<rho, v is finite on an open interval containing rho. A finite convex function on an open interval has a supporting line; this follows from the ordering of its left and right secant slopes. Choose a supporting slope -b at rho, with b>=0. For every q with finite F and G,

F(q)>=v(rho)-b(G(q)-rho).

The inequality also holds at a boundary budget by taking budgets decreasing to G(q); infinite F causes no difficulty.

If b>0, this inequality gives inf_q(F+bG)-b rho>=v(rho). Weak duality gives the reverse inequality. If b=0, every q with finite F and G has F(q)>=v(rho), so for every beta>0,

inf_q(F+beta G)-beta rho >= v(rho)-beta rho.

Weak duality again bounds this expression above by v(rho); taking beta down to zero proves the same supremum identity. Therefore

v(rho)=sup_{beta>0}{E_pi J_beta-beta rho}.

Substitution of J_beta=I_alpha^S and beta=alpha/(1-alpha) proves the requested value identity. The argument includes the case where the supremum occurs only as alpha decreases to zero. Taking the supremum over policies preserves the equality and requires no exchange of optimization order.

### Posterior

In the geometric mixture, all factors other than p(theta)p(x|theta,xi)^alpha depend only on x. For p_alpha-almost every x, m_alpha(x|xi)>0, and conditioning gives

q_alpha^*(theta|x,xi)=p(theta)p(x|theta,xi)^alpha/m_alpha(x|xi).

On outcomes of zero q_alpha^* marginal probability, a posterior version may be assigned arbitrarily.

### Constrained optimality at a dual maximizer

Strong duality alone does not make every Lagrangian minimizer feasible. We verify that claim for this law.

Suppose beta_*>0 is dual optimal, and write q_*=q_{alpha_*}^*, J_*=E_pi J_{beta_*}, and v=v(rho). Then J_*-beta_*rho=v. Choose feasible kernels q_n with F(q_n) tending to v; they have finite F and G after discarding finitely many terms.

For any finite-objective kernel q, the log-partition identity and the auxiliary-marginal identity imply

F(q)+beta_*G(q)-J_*
= (1+beta_*)E_pi KL(q_xi||q_{*,xi})
  - E_pi KL(q(x|xi)||p_{alpha_*}(x|xi))
>= beta_* E_pi KL(q_xi||q_{*,xi}).

The last inequality is the KL chain rule, which bounds marginal KL by joint KL. These terms are finite in this calculation because the left auxiliary weighted-KL objective is finite at every q with finite F and G; equivalently the pointwise log-partition identity first bounds the joint KL and then the marginal KL.

For q_n, the left side is nonnegative and at most F(q_n)-v, so E_pi KL(q_{n,xi}||q_{*,xi}) tends to zero. Regarding pi(dxi)q_xi as joint probability laws, this is their joint relative entropy. Pinsker's inequality, in the form ||R-S||_TV^2<=KL(R||S)/2, gives total-variation convergence of these joint laws to the law of q_*.

Relative entropy is lower semicontinuous under total-variation convergence of both arguments. One relevant standard-independent formulation is

KL(R||S)=sup_{bounded measurable f}{E_R f-log E_S exp(f)};

each expression on the right is continuous under such convergence, proving the claimed lower semicontinuity. Apply this first with S=pi(dxi)P_xi to obtain G(q_*)<=rho. Apply it also to F(q)=KL(pi q||pi p(theta)q(x|xi)); the second argument converges in total variation because taking a marginal and multiplying it by the fixed prior are total-variation contractions. Thus F(q_*)<=liminf F(q_n)=v.

Feasibility gives F(q_*)>=v, so equality holds. The regularized identity then yields beta_*(G(q_*)-rho)=0. Hence q_* is a constrained worst-case law, as asserted.

All theorem-critical obligations are closed: unrestricted admissibility, the auxiliary identity, normalized joint minimization, marginal optimization, measurable assembly, average-budget duality including the zero-multiplier boundary, posterior support conventions, and constrained feasibility at an interior dual maximizer.
