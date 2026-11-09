# Reference Proof

## Proof Structure

1. Expand the CPD response and establish the fixed-core linear representation needed for the diagonal block.
2. Differentiate the regularized least-squares loss to obtain the diagonal Hessian blocks.
3. Differentiate the cross-core gradient componentwise, separating the derivative of the residual from the derivative of the fixed-core design factor.
4. Assemble the corrected cross-core blocks and the full Hessian formula.

## Complete Proof

Write S^(d)=Phi^(d)V^(d). For each core k, define Z^(k) in R^{N x R} by
Z^(k)_{nr}=product_{d != k}S^(d)_{nr},
where an empty product is 1 for every n and r. Then
f_n=sum_{r=1}^R S^(k)_{nr}Z^(k)_{nr}
=sum_{i=1}^{I_k}sum_{r=1}^R Phi^(k)_{ni}V^(k)_{ir}Z^(k)_{nr}.
Therefore, with columns indexed by (i,r), f=A^(k)v^(k), because A^(k)_{n,(i,r)}=Phi^(k)_{ni}Z^(k)_{nr}.

Fix k. When the other cores are held fixed, A^(k) is constant as a function of v^(k), and
J=beta/2||y-A^(k)v^(k)||_2^2+gamma/2||v^(k)||_2^2+constant.
Thus
grad_{v^(k)}J=beta A^(k)^T(f-y)+gamma v^(k)
and
H_{kk}=beta A^(k)^T A^(k)+gamma I_{I_kR}.

Now fix distinct cores k and m. Define Z^(k,m) in R^{N x R} by
Z^(k,m)_{nr}=product_{d != k,m}S^(d)_{nr},
where an empty product is 1 for every n and r. For the rth column of core k, the gradient component is
g^(k)_r=beta Phi^(k)^T diag(Z^(k)_:r)(f-y)+gamma v^(k)_r.
Since Z^(k)_:r=S^(m)_:r elementwise-multiplied by Z^(k,m)_:r, differentiating the residual with respect to V^(m)_{jp} gives
partial f_n/partial V^(m)_{jp}=Phi^(m)_{nj}Z^(m)_{np}.
Consequently, the derivative of the residual part of g^(k)_r with respect to V^(m)_{jp} has entries
beta sum_n Phi^(k)_{ni}Z^(k)_{nr}Z^(m)_{np}Phi^(m)_{nj}
+beta delta_{rp}sum_n Phi^(k)_{ni}(f_n-y_n)Z^(k,m)_{nr}Phi^(m)_{nj}.
The first term is
beta[Phi^(k)^T diag([Z^(k) odot_R Z^(m)]_:(r,p))Phi^(m)]_{ij},
and the second is
beta delta_{rp}[Phi^(k)^T diag(f-y)diag([Z^(k,m)]_:r)Phi^(m)]_{ij}.
The regularizer has no cross-core derivative. Hence, defining
D^(k,m,r,p)=diag([Z^(k) odot_R Z^(m)]_:(r,p)),
E^(k,m,r)=diag(f-y)diag([Z^(k,m)]_:r),
T^(k,m,r,p)=D^(k,m,r,p)+delta_{rp}E^(k,m,r),
we obtain
H_(k,r),(m,p)=beta Phi^(k)^T T^(k,m,r,p)Phi^(m).
Together with the diagonal formula, these blocks comprise the full Hessian.
