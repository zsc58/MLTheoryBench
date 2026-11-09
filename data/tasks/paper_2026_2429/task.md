# Problem

## Setup

Let `D`, `N`, `R`, and each `I_d` be positive integers. Let `N` training samples have responses `y in R^N`. For each mode `d`, let `Phi^(d) in R^{N x I_d}` and `V^(d) in R^{I_d x R}`; write `v^(d)=vec(V^(d))` and `S^(d)=Phi^(d)V^(d)`. The CPD weight tensor is parameterized by the rank-`R` factors `V^(1),...,V^(D)`, and the model response is

`f_n = sum_{r=1}^R product_{d=1}^D S^(d)_{nr}`,   `n=1,...,N`.

For matrices with `N` rows, `odot_R` denotes the row-wise Khatri-Rao product: if `U,W in R^{N x R}`, then `U odot_R W in R^{N x R^2}` has column `(r,p)` equal to `U_:r odot W_:p`. For each `k`, define

`Z^(k) = row-wise product_{d != k} S^(d) in R^{N x R}`;

if the product is empty, `Z^(k)` is the `N x R` all-ones matrix. Define `A^(k) in R^{N x (I_k R)}` by `A^(k)_{n,(i,r)} = Phi^(k)_{ni} Z^(k)_{nr}`. For distinct `k,m`, define `Z^(k,m)` as the row-wise product of all `S^(d)` with `d != k,m`; when this product is empty, set `Z^(k,m)` to the `N x R` all-ones matrix. For component indices `r,p`, set

`D^(k,m,r,p)=diag([Z^(k) odot_R Z^(m)]_{:,(r,p)})`,

`E^(k,m,r)=diag(f-y) diag([Z^(k,m)]_:r)`,

and `T^(k,m,r,p)=D^(k,m,r,p)+delta_{rp}E^(k,m,r)`.

Assume `beta>0` and `gamma>0`, and consider the regularized loss

`J(v)= beta/2 ||y-f||_2^2 + gamma/2 sum_{d=1}^D ||v^(d)||_2^2`.

## Task

Prove that the Hessian of `J` with respect to the vectorized core parameters has the following explicit blocks. For every core `k`,

`H_{kk}= beta A^(k)^T A^(k) + gamma I_{I_k R}`.

For every distinct pair of cores `k != m` and component indices `r,p in {1,...,R}`, the block coupling the `r`th component of core `k` to the `p`th component of core `m` is

`H_{(k,r),(m,p)} = beta Phi^(k)^T T^(k,m,r,p) Phi^(m)`.

Here `I_{I_k R}` is the identity of the indicated dimension, and the displayed diagonal and cross-core blocks together comprise the full Hessian.
