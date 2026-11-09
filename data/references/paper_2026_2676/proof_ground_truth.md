# Reference Proof

## Proof Structure

Work coordinatewise. For one coordinate, write the bridge law as a binomial mass on the finite monotone path between the endpoints. For 0<t<1, differentiate this mass and use adjacent-mass ratios. Treat t=0 directly from the binomial polynomial, and check the support boundaries and states outside the support. If the endpoint is larger, the resulting forward equation has only births; if it is smaller, it has only deaths. The coordinate equations combine by independence, and uniqueness on the finite invariant reachable box identifies the complete time-inhomogeneous Markov law.

## Complete Proof

Fix a coordinate and suppress its index. Let a,b in N_0, m=|b-a|, and s=sgn(b-a). Write

q_t(k) = binom(m,k) t^k (1-t)^(m-k),  0 <= k <= m,

with q_t(k)=0 otherwise. The bridge mass is supported on z=a+s k and equals q_t(k).

First suppose 0<t<1. For 0<=k<=m, differentiation gives

q'_t(k) = (k/t - (m-k)/(1-t)) q_t(k),

where the expression is understood only for support points with q_t(k)>0. The adjacent-mass identity needed below is

q_t(k-1)/q_t(k) = [k/(m-k+1)] [(1-t)/t],

whenever k>=1 and q_t(k)>0.

Suppose b>=a, so s=1 and z=a+k. On the reachable support set

lambda_t(z) = (b-z)/(1-t) = (m-k)/(1-t),
mu_t(z) = 0.

For k>=1, the adjacent-mass identity gives

lambda_t(z-1) q_t(k-1) = [k/t] q_t(k).

Therefore

lambda_t(z-1) q_t(k-1) - lambda_t(z) q_t(k)
= [k/t - (m-k)/(1-t)] q_t(k)
= q'_t(k).

At the lower boundary k=0, the incoming term is absent and the equation is

q'_t(0) = -[m/(1-t)]q_t(0) = -lambda_t(a)q_t(0).

At the upper boundary k=m, lambda_t(b)=0, so the displayed equation also holds. If z is outside [a,b], both the mass and all potentially incoming fluxes are zero; at the adjacent endpoint the corresponding outward rate is zero. Thus the birth-only forward equation holds on all of N_0.

Now suppose b<a, so s=-1 and z=a-k. On the reachable support set

lambda_t(z) = 0,
mu_t(z) = (z-b)/(1-t) = (m-k)/(1-t).

For k>=1, the state z+1 corresponds to k-1, and the adjacent-mass identity gives

mu_t(z+1) q_t(k-1) = [k/t] q_t(k).

Hence

mu_t(z+1) q_t(k-1) - mu_t(z) q_t(k)
= [k/t - (m-k)/(1-t)] q_t(k)
= q'_t(k).

The lower and upper support boundaries are handled in the same way: absent incoming terms are omitted, and the rate at the endpoint that would leave the support is zero. States outside the support have zero mass and zero net incoming flux. Thus the death-only forward equation holds on all of N_0.

It remains to handle t=0, where the quotient formulas above are not used. The binomial polynomial gives q_0(0)=1 and q_0(k)=0 for k>=1. Direct differentiation gives q'_0(0)=-m, q'_0(1)=m when m>=1, and q'_0(k)=0 for k>=2. The birth-only or death-only flux equations with the rates above give exactly these values: mass leaves the initial endpoint at rate m and enters the adjacent state at rate m, with no other first-order flux. When m=0, q_t is the constant point mass and both rates vanish on the reachable state. Therefore the one-coordinate forward equation holds for every 0<=t<1.

Applying this calculation independently in every coordinate, define

S = product over i of {min(a_i,b_i), ..., max(a_i,b_i)}.

Starting from a, the displayed rates keep the chain in S: a birth rate vanishes at an upper target endpoint, a death rate vanishes at a lower target endpoint, and the opposite-direction rate is zero throughout the relevant interval. Hence S is a finite invariant state space. The product bridge mass

p_t(z | a,b) = product over i of p_t^(i)(z_i | a_i,b_i)

has initial law delta_a. Its derivative is obtained by the product rule, and the one-coordinate forward equations show that it satisfies the multidimensional forward equation with

lambda_{t,i}(z | a,b) = (b_i-z_i)_+/(1-t),
mu_{t,i}(z | a,b) = (z_i-b_i)_+/(1-t).

The same equation is zero on states outside S because S is invariant and the boundary rates prevent incoming flux across its boundary. On every interval [0,T] with T<1, the rates restricted to the finite set S are bounded and continuous in time. The finite-state time-inhomogeneous forward equation with initial law delta_a therefore has a unique solution. Consequently, the law of the chain is p_t(. | a,b) for every t<1.

Finally, for each coordinate, B_t^(i) has distribution Binomial(|b_i-a_i|,t), so B_t^(i) converges in probability to |b_i-a_i| as t approaches 1 from below. Thus Y_t^(i) converges in probability to b_i for every i, and the bridge law converges to the point mass at b.
