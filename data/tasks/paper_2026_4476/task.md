# Problem

## Setup

Fix an embedding dimension \(d\ge1\). Let \(K\ge1\) and let \(z_1,\ldots,z_K\in\mathbb R^d\) be support embeddings (possibly produced using an arbitrary parameter \(\theta\)). Define
\[
\bar z=\frac1K\sum_{i=1}^K z_i,\qquad S_z=\sum_{i=1}^K(z_i-\bar z)(z_i-\bar z)^\top.
\]
Assume a Normal-Inverse-Wishart prior with parameters \(\mu_0\in\mathbb R^d\), \(\kappa_0>0\), \(\Lambda_0\in\mathbb R^{d\times d}\) satisfying \(\Lambda_0\succ0\), and \(\nu_0>d-1\). The normal-embedding model is \(z\mid(\mu,\Sigma)\sim\mathcal N(\mu,\Sigma)\). For the support set, define
\[
\kappa_n=\kappa_0+K,\qquad \nu_n=\nu_0+K,\qquad \mu_n=\frac{\kappa_0\mu_0+K\bar z}{\kappa_n},
\]
\[
\Lambda_n=\Lambda_0+S_z+\frac{\kappa_0K}{\kappa_n}(\bar z-\mu_0)(\bar z-\mu_0)^\top,
\]
and let the posterior predictive parameters be
\[
\Sigma_n=a_n\Lambda_n,\qquad a_n=\frac{\kappa_n+1}{\kappa_n(\nu_n-d+1)},\qquad v_n=\nu_n-d+1.
\]

## Task

Prove that, for every \(K\ge1\), every support set in \(\mathbb R^d\) and every parameter \(\theta\), the posterior predictive distribution with location \(\mu_n\), scale \(\Sigma_n\), and degrees of freedom \(v_n\) is a proper multivariate Student-t distribution, that \(\Sigma_n\) is strictly positive definite, and that its log-density is finite for every query embedding \(x\in\mathbb R^d\). Your proof must include the case \(K<d\).
