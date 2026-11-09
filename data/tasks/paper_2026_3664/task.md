# Problem

## Setup

Let `p=(p_i)_{i>=1}` be any probability distribution on the countable alphabet `N`. Let `X_1,...,X_n` be iid samples from `p`, let `c_i=sum_{r=1}^n 1{X_r=i}`, and define the empirical pmf `hat p_i=c_i/n`. Set

`Delta_n(p)=E_p[ ||hat p-p||_infty ]`.

## Task

Prove that there are universal constants `c,C>0` and `n_0` such that, for every `n>=n_0`, with `p*=(1/2,1/2,0,...)`,

`Delta_n(p*) >= c Delta_n(p)` for every countable-alphabet distribution `p`,

and, as a global consequence,

`c n^{-1/2} <= sup_p Delta_n(p) <= C n^{-1/2}`.
