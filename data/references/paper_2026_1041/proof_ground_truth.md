# Reference Proof

## Proof Structure

For any finite set of inputs, write the output vector as the bias vector plus a sum of independent hidden-unit contribution vectors. Expand its covariance. Centering and independence of distinct output-weight blocks eliminate cross-activation terms, while independence and centering across hidden units eliminate off-diagonal unit terms. The remaining diagonal terms give the weighted sum of activation-induced covariances. Finite second moments permit the multivariate central limit theorem, yielding the claimed Gaussian finite-dimensional limit. The covariance calculation also verifies positive semidefiniteness.

## Complete Proof

Fix arbitrary inputs x_1,...,x_n in R^d. Let Z_j(x)=a_j+u_j^T x, where the pairs (a_j,u_j) are iid, a_j has law N(0,sigma_a^2), u_j has law N(0,sigma_u^2 I_d), a_j is independent of u_j, and different pairs are independent. For each m, let v_j^(m) have law N(0,sigma_v^2/H); all output weights are mutually independent and independent of the pre-activation variables and of b, where b has law N(0,sigma_b^2). The stated moment assumption gives finite second moments for every activation coordinate in the fixed input set.

Write

Y_H=(f_H(x_1),...,f_H(x_n))=B_H+sum_{j=1}^H X_{H,j},

where B_H=b 1_n and

X_{H,j}=sum_{m=1}^M sqrt(w_m) v_j^(m) (h_m(Z_j(x_1)),...,h_m(Z_j(x_n))).

The X_{H,j} are iid, centered, independent of B_H, and have finite second moments. For coordinates r,s, covariance expansion gives

Cov(X_{H,j,r},X_{H,j,s}) = sum_{m,m'} sqrt(w_m w_{m'}) E[v_j^(m)v_j^(m') h_m(Z_j(x_r))h_{m'}(Z_j(x_s))].

When m != m', independence and zero means of the output weights make the term zero. When m=m', independence of v_j^(m) and Z_j gives

Cov(X_{H,j,r},X_{H,j,s}) = (sigma_v^2/H) sum_m w_m E[h_m(Z(x_r))h_m(Z(x_s))] = (sigma_v^2/H) sum_m w_m K_m(x_r,x_s).

Independence of distinct hidden units then yields

Cov(Y_H)_{rs}=sigma_b^2+sigma_v^2 sum_m w_m K_m(x_r,x_s)=K(x_r,x_s).

Set S_{H,j}=sqrt(H) X_{H,j}. The variables S_{H,j} are iid centered with an H-independent distribution and covariance matrix whose (r,s) entry is sigma_v^2 sum_m w_m K_m(x_r,x_s). Since their coordinates have finite second moments, the multivariate central limit theorem, equivalently the Cramer-Wold argument, gives

sum_{j=1}^H X_{H,j}=H^(-1/2) sum_{j=1}^H S_{H,j} converges in distribution to N_n(0, [sigma_v^2 sum_m w_m K_m(x_r,x_s)]_{r,s}).

Adding the independent Gaussian vector B_H, whose covariance is sigma_b^2 1_n 1_n^T, gives convergence of Y_H to N_n(0,[K(x_r,x_s)]_{r,s}). Since the finite input set was arbitrary, f_H converges in finite-dimensional distributions to the centered Gaussian process with kernel K.

Finally, for any coefficients c_1,...,c_n,

sum_{r,s} c_r c_s K_m(x_r,x_s) = E[(sum_r c_r h_m(Z(x_r)))^2] >= 0.

Thus each K_m is positive semidefinite, and nonnegative weighting plus the bias kernel preserves this property, so K is a valid covariance kernel.
