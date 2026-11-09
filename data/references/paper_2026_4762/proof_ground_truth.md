# Reference Proof

## Contract and proof obligations

The partition is fixed and may be unknown. Only independent observed-cell descriptions and the stated origin-centered conditional sampler are available. No fine sample or constant-distance warm start is supplied. We must establish a well-defined likelihood, convexity and local growth, implementable unbiased gradients, stochastic-optimization convergence, confidence amplification, a valid coupling to localized observations, and the additive two-stage sample bound.

The proof below closes these obligations directly. In particular, it does not assume the specialized optimization theorem without proof, does not invoke the auxiliary proposition's sharper explicit logarithmic display, and does not require a hit-and-run implementation of the already-assumed sampler.

## 1. Likelihood normalization and geometry

First consider a box-refined observation experiment: inside a fixed box, report the intersection of the original cell with the box; outside, report the exact point. The original finite-bit observation model has countably many representable cells, and its zero-mass cells have total observation probability zero. Thus the refined experiment has countably many positive-mass interior observations and a continuous exterior component. Use counting measure for the former and Lebesgue measure for the latter. Write its density as q_mu and its law as Q_mu. The same likelihood-ratio argument applies to the original experiment.

Define

F(mu) = -E_{Z~Q_mu*} log(q_mu(Z)/q_0(Z)).

This avoids assuming that the cell distribution has finite entropy. The Gaussian laws are mutually absolutely continuous, as are their observation pushforwards. For any means a,b, conditional Jensen applied to the full Gaussian likelihood ratio gives

KL(Q_a || Q_b) <= KL(N(a,I) || N(b,I)) = ||a-b||^2/2.

Indeed, dQ_b/dQ_a is the conditional expectation, given the observation, of dN(b,I)/dN(a,I); apply convexity of minus log and then take expectation. These finite divergences imply integrability of the log ratios and therefore

F(mu)-F(mu*) = KL(Q_mu* || Q_mu).                    (1)

For a positive-mass convex interior cell A, its candidate likelihood is the Gaussian mass of A. The function

1_A(x) exp(-||x-mu||^2/2)

is jointly log-concave in x and mu. The integral part of Prékopa–Leindler implies that its integral over x is log-concave in mu. To verify the premise explicitly, for means mu_0,mu_1 and points x,y, convexity of A and of squared norm give the required multiplicative interpolation inequality at ((1-t)x+ty,(1-t)mu_0+t mu_1). Thus the cell negative log-likelihood is convex.

Differentiating its Gaussian integral gives the score and Hessian

s_mu(A)=mu-E_mu[Y|A],

H_mu(A)=I-Cov_mu(Y|A).

Differentiation is legitimate on compact sets of means by Gaussian domination. Convexity and nonnegativity of covariance imply

0 <= H_mu(A) <= I.                                (2)

For an exterior fine observation x, use the Gaussian density, not the zero probability of {x}; its score is mu-x and its Hessian is I. The reference normalization is independent of mu and does not change these derivatives.

Consequently each observation score is 1-Lipschitz in mu. At the true mean, Jensen and conditional expectation give

E||s_mu*(Z)||^2 <= E||mu*-X||^2 = d.

Together with score Lipschitzness, this provides an integrable envelope on every bounded candidate domain, justifying differentiation of the population objective. In particular F is finite, differentiable, and convex, with minimizer mu* by (1).

## 2. Quantitative local growth

Let

eta = sqrt(2) alpha/200,

rho = 2 alpha^2/600^2.

If F(mu)-F(mu*)<=rho, Pinsker's inequality, KL(P||Q)>=2 TV(P,Q)^2, and information preservation imply

TV(N(mu*,I),N(mu,I)) <= 1/600.

For equal-covariance Gaussians at mean distance a, comparing their densities across their separating hyperplane gives TV=2 Phi(a/2)-1. This identity also verifies the endpoint of the source's quoted small-TV bound: when TV<=1/600, a<1 and

TV = integral from -a/2 to a/2 of phi(t) dt >= a phi(1/2) >= a/200.

Using (1) and Pinsker again, now as a lower bound, yields

F(mu)-F(mu*) >= 2 alpha^2 TV(N(mu*,I),N(mu,I))^2
                 >= eta^2 ||mu-mu*||^2.           (3)

Thus the claimed local growth holds on the closed rho-sublevel set. The divergence orientation throughout is true law to candidate law.

## 3. Unbiased gradients and two moment bounds

For an ideal refined observation Z, sample Y from the candidate Gaussian restricted to its interior cell, or take Y=x when Z is an exterior fine observation. Set g=mu-Y. Then E[g|Z]=s_mu(Z), so a fresh observation and independent conditional draw produce an unbiased stochastic gradient, conditionally on all previous algorithmic randomness.

If the box has radius R, candidates lie in B(0,D), and ||mu*||<=D, the source's inside/outside decomposition gives

E||Y||^2 <= dR^2 + E||X||^2 <= dR^2+d+D^2,

hence

E||g||^2 <= 4D^2+2dR^2+2d.                       (4)

The additive d cannot be omitted for arbitrary R>0. We choose R>=1, recovering O(D^2+dR^2).

We also need the following elementary consequence of the same likelihood geometry. From (2),

||s_mu(Z)-s_mu*(Z)|| <= ||mu-mu*||.

The conditional covariance trace is at most d, including the singleton case where it is zero. Therefore

E||g||^2 = E||s_mu(Z)||^2 + E tr Cov_mu(Y|Z)
           <= 3d+2||mu-mu*||^2.                  (5)

This bound allows the second estimation stage to keep the original origin-centered box. It does not assume access to a sampler for translated truncation boxes.

## 4. Direct restarted projected-SGD guarantee

Here is a complete derivation of the optimization guarantee needed below. Let F be convex and differentiable on a compact convex domain K containing its minimizer w*, with efficient projection onto the ball intersections used below. Suppose F has (eta,q)-local growth, fresh gradients are conditionally unbiased with conditional second moment at most G^2, and a starting point has known gap at most b_0.

If b_0<=q, return the starting point. Otherwise put tau=ceil(log_2(b_0/q)), b_l=2^{-l}b_0, and run tau stages.

First observe that whenever a point w has gap at most b with b>=q,

||w-w*|| <= b/(eta sqrt(q)).                      (6)

If its gap is at most q, this follows directly from local growth. Otherwise, continuity on the segment from w* to w supplies a point z on that segment with gap q. If z=w*+t(w-w*), convexity gives q<=t(F(w)-F(w*)), whereas local growth gives t||w-w*||<=sqrt(q)/eta. Combining these proves (6).

At stage l, assuming the previous stage has gap at most b_{l-1}, project SGD onto

K intersect B(w^{l-1}, r_l),

where r_l=b_{l-1}/(eta sqrt(q)). This set contains w* by (6). Use

gamma_l=b_l/(200 tau G^2),

T=ceil(80000 G^2 tau^2/(eta^2 q))

fresh gradient steps, and return their average as w^l. Intersections of the Euclidean balls appearing in this proof admit polynomial-time projection; equivalently one solves their convex quadratic projection problem. Arbitrarily small numerical projection error can be budgeted in the slack of the displayed estimates.

For completeness, nonexpansiveness of projection and conditional unbiasedness give, for each iterate u_t,

E_t||u_{t+1}-w*||^2 <= ||u_t-w*||^2
 -2 gamma_l(F(u_t)-F(w*)) + gamma_l^2 G^2.

Sum this inequality, divide by 2 gamma_l T, and use convexity at the averaged iterate. Conditionally on a successful previous stage,

E[F(w^l)-F(w*)] <= r_l^2/(2 gamma_l T)+gamma_l G^2/2
                   <= 3 b_l/(400 tau)
                   < b_l/(100 tau).

The gap is nonnegative. Markov's inequality makes the conditional failure probability at most 1/(100 tau). A union bound over stages proves that the final gap is at most b_tau<=q with probability at least 0.99. The total number of oracle calls is

O(G^2/(eta^2 q) [1+log(b_0/q)]^3),                (7)

with the already-accurate case handled separately. Thus the specialized convergence citation is not an unresolved proof obligation.

To obtain Euclidean accuracy s in (0,1), use

q=min{rho/2, eta^2 s^2/9}.

Then q=Theta(alpha^2 s^2), and every successful run is within s/3 of mu* by (3). Repeat independently O(log(2/beta)) times. A Chernoff bound gives a strict majority, indeed at least two thirds, of good outputs with probability at least 1-beta. Select any output within distance 2s/3 of more than half the outputs. Such an output exists, and its neighbor set intersects the good outputs, so it is within distance s of mu*. No objective evaluation is needed.

Combining (7) with clustering gives a sufficient local-estimation bound

O(G^2/(alpha^4 s^2)
  [1+log(2+b_0/(alpha^2 s^2))]^3 log(2/beta)).     (8)

This is the explicit bound used here. We do not assert that it proves the source's different, sharper logarithmic display for its auxiliary local-partition proposition.

## 5. Localization and the observation coupling

If D<=epsilon, output zero. Henceforth D>epsilon. Fix a deterministic sample budget M large enough for both stages below, and set

R=1+D+sqrt(2 log(8dM/delta)).

For X~N(mu*,I), the coordinate Gaussian tail bound and a union bound give

Pr(||X||_infinity>R) <= delta/(4M).

Thus with probability at least 1-delta/4, every latent point among the at most M observations is inside the box.

Refine each original cell by intersecting it with this box and make exterior points singleton observations. Refinement preserves convexity. Forgetting the refinement is a deterministic observation map, so total variation contracts under that map; therefore the refined experiment retains the same alpha-information-preservation inequality against every candidate mean.

Run the ideal algorithm on this refined experiment. The actual algorithm instead supplies the intersection of each observed original cell with the fixed box. Couple both experiments through the same latent Gaussian observations and the same sampler randomness. Whenever all latent observations lie in the box, their processed cells and entire algorithmic transcripts agree. This is a coupling argument, not an assertion that conditioning all data to lie in the box preserves their original independent law.

An invalid zero-normalizer query can occur only on the exceptional coupling event, apart from a null event. The public oracle imposes no distributional requirement there but still terminates in polynomial time. A fixed-budget algorithm may output any fixed fallback when an operation reports failure. No correctness claim is required on that exceptional event.

## 6. Two estimation stages and the final bound

In the ideal experiment first work on K_0=B(0,D), starting at zero. Equation (1) and Gaussian data processing give the initial gap bound D^2/2; one may use b_0=1+D^2. Use (4), accuracy s=1/2, and failure probability delta/4 in (8). Since

R^2=O(D^2+1+log(dM/delta)),

this stage uses

tilde-O(d(D^2+1) alpha^{-4} log(2/delta))

observations and returns a point c in K_0 with ||c-mu*||<=1/2, except with probability delta/4.

Condition on a successful first stage. On fresh observations, use

K_1=K_0 intersect B(c,1),

starting at c. This domain contains mu*, and every candidate in it has distance at most 3/2 from mu*. By (5), G^2<=3d+9/2=O(d). The initial gap is at most ||c-mu*||^2/2<=1/8, so use the known bound b_0=1. Apply (8) with s=epsilon and failure probability delta/4. This stage needs

tilde-O(d alpha^{-4} epsilon^{-2} log(2/delta))

fresh observations. Importantly, it uses the same origin-centered box and the same stated sampler as stage one.

There is no circular sample-budget choice: for example, let

H=log(e+d+D+alpha^{-1}+epsilon^{-1}+delta^{-1})

and choose M to be the ceiling of a sufficiently large absolute constant times

d(D^2+epsilon^{-2}) alpha^{-4} H^6 log(2/delta).

Then log(dM/delta)=O(H), and the explicit stage bounds above fit inside M after increasing that absolute constant. This is precisely the required tilde-O rate. Since epsilon<1, the first-stage additive d term is absorbed by the second-stage d/epsilon^2 term.

The two estimation failures and the coupling failure have total probability at most 3delta/4, which is at most delta. Thus the actual algorithm returns an epsilon-accurate mean with probability at least 1-delta.

All iterations use observed-cell operations, the assumed polynomial-time conditional sampler, Euclidean ball-intersection projections, and polynomial-time clustering. The number of operations is polynomial in M and the cell bit complexity. Optional approximate hit-and-run guarantees are not needed to establish this oracle-based runtime.

## Source corrections and completeness

The pre-existing true-to-candidate KL-orientation correction is retained. The additional local source corrections are the additive d in (4) and the likelihood-ratio normalization needed for infinite entropy and ideal fine observations. Neither adds a public structural assumption or changes the flagship conclusion. Every theorem-critical obligation listed at the start has been derived. There is no unresolved private GT obligation.
