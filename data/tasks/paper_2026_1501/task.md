# Problem

## Setup

Let `Z` be a real-valued random variable with distribution function `F_Z`. For `u\in(0,1)`, define its (left-continuous generalized-inverse) quantile by
`Q_Z(u)=inf{x\in\mathbb R:F_Z(x)\ge u}`.
For `p\in(0,1)`, define the lower-tail subquantile
`L_p(Z)=(1/p)\int_0^p Q_Z(u)\,du`.
Write `(x)_+=max{x,0}` and interpret expectations in the extended-real sense whenever applicable.

## Task

Prove that, for every real-valued random variable `Z` and every `p\in(0,1)`,
`L_p(Z)=max_{eta\in\mathbb R}\left\{eta-\frac1p\,\mathbb E[(eta-Z)_+]\right\}`.
