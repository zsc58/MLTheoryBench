# Problem

## Setup

Let A be finite, let X and Y be standard Borel spaces, and let Z_i=(X_i,Y_i), i>=1, be i.i.d. from a joint law P. Let pi_0:X->A be a measurable deterministic baseline policy, let ell:A x Y->R be measurable, let c be a real cutoff, and let epsilon satisfy 0<epsilon<1.

Fix a measurable fitted conditional violation-probability function bar g:A x X->[0,1] independently of the calibration and test observations. Using a fixed tie-breaking order on A, define a_s(x) to minimize bar g(a,x), choosing pi_0(x) whenever it is a minimizer. Define the fitted score

s(x)=bar g(pi_0(x),x)-bar g(a_s(x),x).

Let top be a formal threshold ordered after every element of [0,1]. For t in [0,1] union {top}, define the switching policy

pi_t(x)=pi_0(x) if s(x)<t, and pi_t(x)=a_s(x) otherwise,

where s(x)<top for every x. Its violation loss is L((x,y);t)=1{ell(pi_t(x),y)>=c}. For a finite calibration data set D, let

G(D)={0,top} union {s(x):(x,y) in D},

R_D^+(t)=(1+sum_{z in D} L(z;t))/(|D|+1),

and let t(D) be the largest t in G(D) for which R_D^+(t)<=epsilon. If no such t exists, set t(D)=0.

Assume that s(X) is atomless. Put

p_s=P(ell(a_s(X),Y)>=c), p_0=P(ell(pi_0(X),Y)>=c),

and assume p_s<epsilon<p_0. Define

W=1{ell(pi_0(X),Y)>=c}-1{ell(a_s(X),Y)>=c}.

Assume that there are constants c_W>0 and beta>=0, and a measurable function m, such that

E[W | s(X)]=m(s(X)) and m(u)>=c_W u^beta for P_{s(X)}-almost every u in (0,1].

For each positive integer n, put N=n+1, form the augmented sample D^+=(Z_1,...,Z_N), write t^+=t(D^+), and write t^{-i}=t(D^+ without Z_i). Measure both threshold ranks in the common augmented score ordering by

j(t)=#{r in {1,...,N}:s(X_r)<t},

and set K=max_{1<=i<=N}|j(t^{-i})-j(t^+)|.

## Task

Prove the following integrated theorem. There are constants C_1,C_2, independent of n, such that

E[K] <= C_1 log(n+1)+C_2.

Consequently, there is a constant C_3, independent of n, such that for all sufficiently large n,

E[L(Z_{n+1};t(Z_1,...,Z_n))] <= epsilon + C_3 log(n+1)/(n+1).
