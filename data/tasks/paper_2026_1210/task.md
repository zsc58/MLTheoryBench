# Problem

## Setup

Let Z=(X,S,L), where X is in [0,1]^d, S is a binary sensitive attribute, and L takes finitely many values. Interpret the strata as the support of L, so p_l=P(L=l)>0 for every stratum l under consideration. Treatment A is binary with potential outcomes R(0),R(1). Assume SUTVA and conditional ignorability A independent of (R(0),R(1)) given Z. An individualized decision rule is D(Z) in {-1,1}, written D(Z)=2I{f(Z)>0}-1; put q(Z)=I{f(Z)>0} and define its value by V(D)=E[R(0)+q(Z)(R(1)-R(0))]. Let delta_R(z)=E[R(1)-R(0)|Z=z].

For each stratum l, let pi(s|l)=P(S=s|L=l) and assume pi(s|l)>=c0>0 for s in {0,1}. Define

psi_l(s)=I{s=1}/pi(1|l)-I{s=0}/pi(0|l).

Assume the treatment-specific conditional means are uniformly bounded and beta-Holder in x, and that, for every l,

G_l(omega)=E[I{delta_R(Z)-omega psi_l(S)>0} I{L=l} psi_l(S)]

is continuous on R. Fix epsilon>=0. Conditional epsilon-demographic parity means that, in every stratum l, the absolute difference between the conditional probabilities of assigning action 1 to S=1 and S=0 is at most epsilon. Equivalently, its moment constraint is

|E[q(Z)I{L=l}psi_l(S)]|<=P(L=l)epsilon for every l.

## Task

Prove that the value-maximizing rule subject to these conditional epsilon-demographic-parity constraints has the form

D*(Z)=2I{delta_R(Z)-sum_l I{L=l}omega_l*psi_l(S)>0}-1,

where, for each l, omega_l*=0 when |G_l(0)|<=P(L=l)epsilon; when G_l(0)>P(L=l)epsilon, omega_l* is a root in (0,K) of G_l(omega)=P(L=l)epsilon; and when G_l(0)<-P(L=l)epsilon, omega_l* is a root in (-K,0) of G_l(omega)=-P(L=l)epsilon, for a finite K supplied by the regularity assumptions. Prove also that D* is feasible and V(D)<=V(D*) for every feasible rule D.
