# Problem

## Setup

Let S and A be nonempty measurable state and action spaces, and let Z be a measurable feature space with a sigma-finite reference measure mu. Let p(ds'|s,a) be a measurable probability kernel from S x A to S, and fix a stationary policy given by a measurable probability kernel pi(da|s) from S to A. Fix gamma in [0,1) and a finite real exponent n with 1<=n<infinity. Use the convention gamma^0=1, including when gamma=0.

A conditional probability density means a jointly measurable nonnegative function f(z|s,a) with integral f(z|s,a) mu(dz)=1 for every (s,a). Let h be such a density and assume

H := sup_(s,a) (integral |h(z|s,a)|^n mu(dz))^(1/n) < infinity.

Identify conditional densities f and g when f(z|s,a)=g(z|s,a) for mu-almost every z for every (s,a). The exceptional null set may depend on (s,a). Let Q be the quotient space of conditional probability densities with finite supremum conditional L_n norm, equipped with

bar L_n([f],[g]) = sup_(s,a) (integral |f(z|s,a)-g(z|s,a)|^n mu(dz))^(1/n).

Density-valued formulas are interpreted mu-almost everywhere in z for each conditioning pair.

For each integer Delta>=1, let p_Delta^pi(d sbar|s,a) denote the law of the state reached Delta transitions after starting from the fixed pair (s,a), with subsequent actions sampled from pi. Define

d^pi,gamma(d sbar,d abar|s,a)
= (1-gamma) sum_(Delta>=1) gamma^(Delta-1) p_Delta^pi(d sbar|s,a) pi(d abar|sbar).

Define

q^pi(z|s,a) = integral h(z|sbar,abar) d^pi,gamma(d sbar,d abar|s,a).

For a reference probability density q*(z) with respect to mu, define

r_int(s,a) = -KL(q^pi(.|s,a)||q*),

where KL is the extended relative entropy of the probability measures with the indicated densities; its value may be +infinity, giving r_int(s,a)=-infinity.

Finally, for a representative conditional density f, define

(P^pi f)(z|s,a) = E_{S'~p(.|s,a), A'~pi(.|S')}[(1-gamma)h(z|S',A') + gamma f(z|S',A')].

## Task

Prove the following integrated theorem: the formula for P^pi is independent of the representative, defines a map from Q into itself, and is a gamma-contraction on (Q,bar L_n); [q^pi] belongs to Q and is its unique fixed point, P^pi[q^pi]=[q^pi]; and for every [f_0] in Q, the iterates [f_(k+1)]=P^pi[f_k] satisfy

bar L_n([f_k],[q^pi]) <= gamma^k bar L_n([f_0],[q^pi])

for every integer k>=0 and converge to [q^pi] in bar L_n. Thus the intrinsic reward is independent of the representative of this uniquely identified density class.
