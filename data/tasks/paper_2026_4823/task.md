# Problem

## Setup

Let gamma_n denote standard Gaussian probability measure on R^n. For a Borel set K, write K^{(delta)}={x:dist(x,K)<=delta} and define its Gaussian surface area by
GSA(K)=lim_{delta->0+} gamma_n(K^{(delta)}\\K)/delta,
when this limit exists. Let f:R^n->{-1,1} be Borel-measurable, set K={x:f(x)=1}, assume gamma_n(partial K)=0, and suppose the displayed limit exists (possibly with value +infinity). Write GSA(f)=GSA(K).

## Task

Prove that there is a universal constant C such that, for every n, every f satisfying the setup, and every 0<epsilon<=1/2, there exists a real polynomial p on R^n of degree at most
C GSA(f)^2 log(1/epsilon)/epsilon^2
satisfying
E_{X~gamma_n}[|f(X)-p(X)|]<=epsilon.
