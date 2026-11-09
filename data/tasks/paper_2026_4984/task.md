# Problem

## Setup

Let chi=(chi_k,chi_u) be a centered jointly Gaussian vector with chi_k in R^p and chi_u in R^q. The observed concepts are chi_k; chi_u is unobserved. Let alpha range over a given index set I, and let B_kk be a fixed positive-definite p by p matrix, B_temp a fixed positive-definite q by q matrix, and B_ku(alpha) a p by q matrix. Define

B_uu(alpha)=B_temp+B_ku(alpha)^T B_kk^{-1}B_ku(alpha)

and assume Cov(chi)=B(alpha) with blocks [[B_kk,B_ku(alpha)],[B_ku(alpha)^T,B_uu(alpha)]]. Let psi_k in R^p, psi_u in R^q, and let eta be independent Gaussian noise N(0,sigma_y^2), with sigma_y^2>0. Define

tau=psi_k^T chi_k+psi_u^T chi_u+eta,    y=1{tau>0}.

A classifier restricted to the observed concepts is any measurable function of chi_k, and its loss is 0-1 loss. Define

phi(alpha)=psi_k+B_kk^{-1}B_ku(alpha)psi_u.

## Task

Prove that, for every alpha in I, a Bayes-optimal classifier using only chi_k is

h_alpha(chi_k)=1{phi(alpha)^T chi_k>0},

and that its accuracy is

P(h_alpha(chi_k)=y)
=1/2+(1/pi) arctan sqrt( [phi(alpha)^T B_kk phi(alpha)] / [psi_u^T B_temp psi_u+sigma_y^2] ).

Show additionally that the numerator decomposes as

phi(alpha)^T B_kk phi(alpha)
=psi_k^T B_kk psi_k+2 psi_k^T B_ku(alpha)psi_u
 +psi_u^T B_ku(alpha)^T B_kk^{-1}B_ku(alpha)psi_u,

so only the cross-aligned and recoverable-unknown terms vary with alpha, whereas the irreducible residual denominator is alpha-independent.
