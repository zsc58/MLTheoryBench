# Problem

## Setup

Let d,n >= 1 be integers, let A in R^{d x d} be symmetric positive definite, let b in R^d, and let I denote the d x d identity matrix. Write ||b||_2 for the Euclidean norm and lambda_min(A) for the smallest eigenvalue of A. Define

P_n = span{1,s,...,s^(n-1)}.

For Sigma_ref={sigma_1,...,sigma_n} subset [0,infinity), call Sigma_ref P_n-unisolvent when evaluation at its n ordered nodes is an invertible map from P_n to R^n (equivalently, its evaluation determinant is nonzero). Assume that the reference design Sigma_ref is P_n-unisolvent. Set sigma_max=max_i sigma_i. For h in (0,1], let Sigma_h={h sigma_i:1 <= i <= n}.

Let f(s)=(A+sI)^(-1)b for s >= 0. For any P_n-unisolvent design Sigma={t_1,...,t_n}, let ell_i(.;Sigma) be its Lagrange basis polynomials. Let Pi_h[f] be the value at zero of the unique coordinatewise polynomial in P_n^d interpolating f on Sigma_h. For arbitrary prescribed values hat f(h sigma_i) in R^d, define Pi_h[hat f] by the same coordinatewise Lagrange interpolation functional. Write ||u||_infinity=max_j |u_j| and ||f-hat f||_{infinity,Sigma_h}=max_{i,j}|f_j(h sigma_i)-hat f_j(h sigma_i)|. Define lambda_ref=sum_i |ell_i(0;Sigma_ref)|.

## Task

Prove that, simultaneously,

||f(0)-Pi_h[f]||_infinity <= (1+lambda_ref) sigma_max^n lambda_min(A)^(-(n+1)) ||b||_2 h^n,

||Pi_h[f]-Pi_h[hat f]||_infinity <= lambda_ref ||f-hat f||_{infinity,Sigma_h},

and consequently

||f(0)-Pi_h[hat f]||_infinity <= (1+lambda_ref) sigma_max^n lambda_min(A)^(-(n+1)) ||b||_2 h^n + lambda_ref ||f-hat f||_{infinity,Sigma_h}.
