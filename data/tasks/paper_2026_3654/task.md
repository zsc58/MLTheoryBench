# Problem

## Setup

Let y be an observed vector in R^n and Z an n by d real matrix, with columns u_j and rows z_i^T. Consider the Gaussian model with independent prior coordinates and conditionally independent observations,

w_j ~ N(0, alpha_j^{-1}),   y_i | w ~ N(z_i^T w, beta_i),

where all current alpha_j and beta_i are finite and strictly positive. Let A=diag(alpha_j), B=diag(beta_i), and define

S=(A+Z^T B^{-1}Z)^{-1},   m=SZ^T B^{-1}y,

C=B+ZA^{-1}Z^T,   P=C^{-1},   r_i=y_i-z_i^T m.

The negative log marginal likelihood is

L(A,B)=1/2(log|C|+y^T Py),

up to an additive constant. The objective contains no additional hyperprior penalty.

For this task, **l2-IRLS-MM** means the concave Fenchel majorization-minimization procedure for L that uses tangent majorization of the posterior-precision log determinant log|A+Z^T B^{-1}Z| jointly in the variables alpha_j and beta_i^{-1}, leaving the remaining terms exact. At each iteration the tangent is taken at the current scales and held fixed. The procedure first minimizes its quadratic weighted-ridge surrogate over w at the current scales, and then, with that w fixed, simultaneously minimizes the separable scale terms over positive alpha and beta. Neither the tangent nor the posterior is recomputed between these substeps.

All updates below are exact, without damping or clipping. Quantities on the right-hand side of an update are evaluated at the same old iterate.

## Task

Prove the following integrated theorem. Exact EM and l2-IRLS-MM have the same closed-form moment re-estimation maps

alpha_j^{new}=1/((m_j^{old})^2+S_{jj}^{old}),

beta_i^{new}=(r_i^{old})^2+z_i^T S^{old}z_i.

In the strictly positive parameter domain, evidence stationarity is equivalent to the equations

alpha_j(m_j^2+S_{jj})=1,   beta_i=r_i^2+z_i^T Sz_i,

where the moments in these equations are evaluated at the parameters appearing on their left-hand sides. For a coordinate with m_j^{old}!=0, the feature equation has the MacKay fixed-point representation

alpha_j^{MK,new}=(1-alpha_j^{old}S_{jj}^{old})/(m_j^{old})^2.

Show explicitly that this quotient is a fixed-point representation on its stated domain, not generally the same numerical update as the EM map away from stationarity.

If the expression defining beta_i^{new} is zero, interpret that update only as a boundary limit beta_i decreasing to zero, not as an attained minimizer over positive variances or as permission to substitute a singular B into the posterior formulas. Otherwise the update remains positive.
