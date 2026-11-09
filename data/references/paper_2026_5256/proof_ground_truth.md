# Reference Proof

## Proof Structure and Obligations

The upper bound requires: well-defined local optimizers for finite real reward estimates; the conjugate/Bregman representation and pessimism-based weighted squared-error inequality; a simultaneous two-sided confidence and count event under the stated observation model; and the coverage calculation. The lower bound requires: an admissible paired-arm family in the same experiment; its optimal policies and additive loss identity; coordinate-loss separation; bounded neighboring data-law KL; and aggregation by the standard Assouad inequality stated below. Each obligation is established here.

## 1. Optimization, including zero-mass contexts

Write q_s(a)=pi_0(a|s). Fix a context and suppress its index. On the probability simplex define

h(p)=eta^{-1} sum_a q(a) log(q(a)/p(a)),

with h=+infinity at any boundary point having a zero coordinate. Its Hessian on positive vectors is eta^{-1}diag(q(a)/p(a)^2), which is positive definite. Thus h is strictly convex on the relative interior. For any finite real vector u, the function <u,p>-h(p) attains its maximum at a unique interior point p_u. Indeed, it tends to minus infinity at the boundary, and strict concavity gives uniqueness. The one-action case has a singleton simplex and the same conclusion.

Stationarity under sum_a p(a)=1 gives

p_u(a)=q(a)/[eta(lambda_u-u(a))].

The normalization function sum_a q(a)/[eta(lambda-u(a))] is continuous and strictly decreasing from infinity to zero on lambda>max_a u(a). Hence there is exactly one lambda_u in this interval. This also proves that p_u depends continuously on u: near any fixed u, two nearby values bracketing lambda_u continue to bracket the unique normalization root, and then the displayed formula gives continuity of p_u.

The canonical pi* in the task equals p_r at every context. Every maximizer of the contextual objective at an input u must equal p_u at every context with rho(s)>0, since otherwise replacing that context's policy by its unique optimizer would strictly improve the objective. No identification is needed at contexts of zero rho-mass. In particular, the arbitrary output maximizer in the task agrees with p_rhat on the support of rho. All expected-objective calculations below are over that support. No full-support assumption on rho is used.

## 2. Conjugacy and the performance inequality

Define h*(u)=max_p{<u,p>-h(p)}. It is finite, and the maximizing policies give the sandwich

<d,p_u> <= h*(u+d)-h*(u) <= <d,p_{u+d}>.

Continuity of p_u shows that h* is differentiable with gradient p_u. Define B_f(x,y)=f(x)-f(y)-<grad f(y),x-y>. Expanding the conjugate at its optimizers yields

B_{h*}(u,v)=h(p_v)-h(p_u)-<u,p_v-p_u>.

Stationarity says u-grad h(p_u)=lambda_u 1. Since both policies sum to one, the last inner product can be replaced by <grad h(p_u),p_v-p_u>. Consequently

B_{h*}(u,v)=B_h(p_v,p_u).

Let e=r-rhat>=0, p*=p_r, and phat=p_rhat. Expanding the difference between the two true-reward objective values gives

D := J_s(p*;r)-J_s(phat;r)
   = h*(r)-h*(rhat)-<r-rhat,phat>
   = B_{h*}(r,rhat)
   = B_h(phat,p*)
   = eta^{-1} sum_a q(a) phi(y_a),

where y_a=1-phat(a)/p*(a)<1 and phi(y)=-y-log(1-y). Here J_s denotes the single-context summand in J.

Optimality of phat at rhat also gives

D <= <r-rhat,p*-phat> = sum_a p*(a)e(a)y_a.

For z>-1, maximizing zy-phi(y) over y<1 gives y=z/(1+z), and therefore phi*(z)=z-log(1+z). The definition of this supremum gives zy<=phi(y)+phi*(z). Set

z_a=2 eta p*(a)e(a)/q(a)>=0.

Then

2D <= eta^{-1} sum_a q(a)z_a y_a
   <= D + eta^{-1} sum_a q(a)[z_a-log(1+z_a)].

For z>=0,

z-log(1+z)=integral_0^z t/(1+t) dt <= z^2/2.

It follows that

D <= 2 eta sum_a [p*(a)^2/q(a)] e(a)^2.                                      (1)

The proof only requires finite real-valued rhat and pessimism, not rhat>=0. Thus it applies to the task's untruncated estimator. Averaging (1) over the positive-mass contexts gives its contextual version.

## 3. The simultaneous confidence and count event

Let M=SA and L=log(2M/delta). Conditional on all sampled context-action pairs, the N=N(s,a)>0 residuals in a fixed cell are independent and have moment-generating functions bounded by exp(t^2/2). Multiplication of these bounds and the exponential Markov inequality give, for x>0,

P(|rbar(s,a)-r(s,a)|>x | sampled pairs) <= 2 exp(-N x^2/2).

For x=b(s,a)=sqrt(4L/N), this is at most 2exp(-2L). At an unobserved cell, |rbar-r|<=1=b deterministically. A union bound therefore gives confidence-event failure at most

2M exp(-2L)=delta^2/(2M)<=delta/2.

For the counts, put w=rho(s)q_s(a), mu=nw, and N~Bin(n,w). We prove the division-free event

mu/(N vee 1)<=8L.                                                          (2)

If mu<=8L, this holds deterministically, including w=0. If mu>8L, the binomial moment-generating function and exponential Markov inequality give

P(N<mu/2) <= exp(mu/4) E exp(-N/2)
          <= exp(mu[1/4+exp(-1/2)-1])
          <= exp(-mu/8)
          < exp(-L)=delta/(2M).

On N>=mu/2, the left side of (2) is at most 2, which is at most 8L because L>=log 2. A union bound over cells gives count-event failure at most delta/2. The confidence and count events thus hold jointly with probability at least 1-delta, with exactly the penalty in the task.

On this joint event, rhat<=r and 0<=r-rhat<=2b. Also b^2<=4L/(N vee 1), including unobserved cells. Multiplying (2) by 4L/n and summing over cells gives

E_{rho times pi_0} b^2
 = sum_{s,a} rho(s)q_s(a)b(s,a)^2
 <= 32 L^2 SA/n.                                                         (3)

Zero-mass cells contribute zero throughout; no expression of the form 0/0 or 0 times infinity is used.

## 4. The upper rate

By the definition of C_*,

pi*(a|s)^2/pi_0(a|s) <= C_*^2 pi_0(a|s).

Combining (1), pessimism, and (3) gives, on the joint event,

SubOpt(phat)
 <= 2 eta C_*^2 E_{rho times pi_0}(r-rhat)^2
 <= 8 eta C_*^2 E_{rho times pi_0}b^2
 <= 256 eta C_*^2 SA L^2/n.                                               (4)

Thus C=256 suffices for the upper sample-size implication. The result holds for every positive epsilon, so in particular c_epsilon=1 is allowed. When A=1 the policy is unique on each context and suboptimality is zero, consistently with this calculation.

## 5. The lower-bound family and exact losses

Now let A=2K, assume n>max{16SA,4eta^2SA}, and put gamma=sqrt(SA/n). Use uniform rho and pi_0. For v in {-1,1}^{S times K}, define conditionally independent Bernoulli rewards with means

r_v(s,2k-1)=1/2+v_{s,k}gamma,
r_v(s,2k)=1/2-v_{s,k}gamma.

The triples are i.i.d. Because gamma<1/4, all means lie in [0,1]. Each centered reward lies in [-1,1] and has conditional mean zero. Convexity of the exponential bounds its conditional moment-generating function by cosh(t)<=exp(t^2/2), so these are admissible 1-subgaussian observation kernels. The construction does not assume that a residual is independent of its sampled cell. The known logging policy is identical at every vertex.

Set t=eta gamma<1/2 and alpha=(1+sqrt(1+4t^2))/2. At every context there are K higher-mean and K lower-mean actions. Substituting the local optimizer formula into normalization gives alpha^2-t^2=alpha and the respective optimal probabilities

q_+=1/[A(alpha-t)],    q_-=1/[A(alpha+t)].                                 (5)

For an arbitrary full-support policy p, stationarity at pi_v* gives

r_v(s,a)=lambda_s-eta^{-1}pi_0(a|s)/pi_v*(a|s).

Insert this into the objective difference. The lambda_s term cancels because both policies sum to one, and the remaining terms give

SubOpt_s(p)=1/(eta A) sum_a psi(p(a|s)/pi_v*(a|s)),
psi(x)=x-1-log x>=0.                                                       (6)

Consequently the total loss is the sum of m=SK=SA/2 nonnegative coordinate losses

L_{s,k}(p,v)=1/(S eta A) [psi(p(2k-1|s)/pi_v*(2k-1|s))
                         +psi(p(2k|s)/pi_v*(2k|s))].                      (7)

## 6. Separation, neighboring data laws, and aggregation

Let v and v' differ only in coordinate (s,k). Each action in that pair is compared once with q_+ and once with q_- in L_{s,k}(p,v)+L_{s,k}(p,v'). For a single assigned probability x>0, differentiating

psi(x/q_+)+psi(x/q_-)

gives its minimum at x=2/(q_+^{-1}+q_-^{-1})=1/(A alpha). At that minimizer the two ratios are 1-t/alpha and 1+t/alpha. Minimizing the two action probabilities separately only relaxes the policy normalization constraint, so

L_{s,k}(p,v)+L_{s,k}(p,v')
 >= 2/(S eta A) [-log(1-(t/alpha)^2)]
 >= 2t^2/(S eta A alpha^2)
 >= t^2/(S eta A)
 = eta/n.                                                               (8)

Here alpha<=(1+sqrt 2)/2<sqrt 2, since t<1/2.

Let P_v be the full n-triple data law, including the contexts. Neighboring vertices have the same context-action law and differ only in two cells, each sampled with probability 1/(SA). For 0<gamma<=1/4,

kl(Ber(1/2+gamma),Ber(1/2-gamma))
 =2gamma log((1+2gamma)/(1-2gamma))
 <=16gamma^2.

Indeed, log((1+x)/(1-x))<=2x/(1-x)<=4x for 0<=x<=1/2; take x=2gamma. The reversed Bernoulli KL is the same. Factoring the i.i.d. likelihood and averaging its log gives

KL(P_v||P_v')
 <= n [2/(SA)]16gamma^2
 =32.                                                                    (9)

We use the following standard Assouad inequality, recorded as the standard-independent dependency theory_012: for a family indexed by {-1,1}^m, with total loss equal to a sum of nonnegative coordinate losses, if every neighboring pair at coordinate j satisfies L_j(p,v)+L_j(p,v')>=d for every possible output p, and its data-law KL is at most B, then every estimator has worst-case expected total loss at least (md/4)exp(-B). This is precisely the form stated in the supplied source. The loss decomposition (7), uniform separation (8), and full-data KL calculation (9) verify all its hypotheses with m=SA/2, d=eta/n, and B=32. An independent estimator random seed can be appended to each data law without changing KL, so randomized estimators are included.

Therefore every full-support estimator has worst-case expected suboptimality at least

[e^{-32}/8] eta SA/n.

The supremum over all admissible instances is at least that over this family. Thus the lower target holds with the universal constant c=e^{-32}/8. All theorem-critical obligations are closed.
