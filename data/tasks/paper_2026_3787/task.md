# Problem

## Setup

Let n>=1 be an integer and write N=n+1. Consider an exchangeable split-conformal regression construction whose calibration and test scores have a continuous, tie-free joint distribution. Under the null, its conformal p-value P_n is uniform on the grid

G_N={1/N,2/N,...,N/N}.

A grid p-variable is a G_N-valued random variable P satisfying Pr(P<=k/N)<=k/N for every k=1,...,N. An e-variable is a nonnegative random variable E with null expectation at most one; it is exact when the expectation equals one. For this fixed grid, a grid p-to-e calibrator is a nonincreasing map F:[0,1]->[0,infinity) such that F(P) is an e-variable for every grid p-variable P. It is set-preserving at level alpha when, for every such conformal construction, {P_n>alpha}={F(P_n)<1/alpha}.

Fix alpha in (0,1) such that alpha N>1 and alpha N is not an integer. Let F_AoN(p)=alpha^{-1} for p<=alpha and F_AoN(p)=0 for p>alpha.

## Task

Prove that there exists a positive strictly decreasing function f:[0,1]->(0,infinity) satisfying

(1/N) sum_{k=1}^N f(k/N)=alpha f(alpha),

such that F_f(p)=f(p)/(alpha f(alpha)) is a grid p-to-e calibrator, is exact for P_n, and is set-preserving at level alpha.

Moreover, prove that for every fixed real s satisfying

alpha<s<ceil(alpha N)/N,

there is C_{n,alpha,s}>0 for which

F_{n,alpha,s}(p)=alpha^{-1} [1+exp(C_{n,alpha,s}(alpha-s))]/[1+exp(C_{n,alpha,s}(p-s))]

is a positive, smooth, strictly decreasing grid p-to-e calibrator, is invertible onto its image, is exact for P_n and set-preserving at level alpha, and satisfies F_{n,alpha,s}(p)>=F_AoN(p) for every p in [0,1].
