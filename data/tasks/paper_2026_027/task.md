# Problem

## Setup

Fix integers `p,d` and `1 <= r <= d`. Let `M` be a fixed `p x d` real matrix with `rank(M)=r`. Let `u_1,u_2,...` be i.i.d. random vectors in `R^p` with finite second moment and positive-definite covariance `Sigma`.

For a fixed `beta_0 in R^d`, observe

`t_i=u_i^T M beta_0+eta_i`,

where the noises are i.i.d. `N(0,nu^2)`, `nu^2>0`, and independent of the inputs. Given the data, use the prior `beta ~ N(0,kappa^2I_d)`, where `kappa^2>0`. Let `ell_n(beta)` be the resulting Gaussian log-likelihood and define the evidence

`Z_n=integral exp(ell_n(beta)) pi(beta) d beta`.

Let `hat beta_n` be any maximum-likelihood estimator and define the Laplace/BIC score

`Q_n=ell_n(hat beta_n)-(d/2)log n`.

The RLCT `lambda` is the coefficient of `log n` in the standard singular evidence expansion; that expansion may also contain a multiplicity term proportional to `log log n`. All asymptotics below are as `n -> infinity` under the stated data-generating law.

## Task

Prove the following integrated claim:

`log Z_n=ell_n(beta_0)-(r/2)log n+O_p(1)`,

so the RLCT is `lambda(r)=r/2` and there is no `log log n` term, and

`Q_n-log Z_n=-((d-r)/2)log n+O_p(1)`.

In particular, when `r<d`, the ordinary `d/2` Laplace/BIC penalty over-penalizes the evidence by `((d-r)/2)log n` up to a tight stochastic remainder.
