# Reference Proof

## Proof Structure

At the fixed iteration, compose the affine maps into one affine map and identify its linear part. The covariance has the same range and null space as that linear part because the initial covariance is positive definite. The universal fixed-point identity applies to the sampled exact truth and places the error in the covariance range, giving the deterministic null-space condition. Finally, the range-projected error is a Gaussian linear image with covariance equal to the projected covariance, so whitening gives a standard normal law. The zero-rank case is handled by the empty-space convention in the task.

## Complete Proof

Fix an iteration index and write the cumulative affine map as

P(z)=Gz+f,

so that the computed mean is x_i=P(x_0). By affine Gaussian pushforward, the belief at this iteration is

mu_i=N(x_i,Sigma),   Sigma=G Sigma_0 G^T.

For every vector v,

v^T Sigma v=(G^T v)^T Sigma_0(G^T v).

Since Sigma_0 is positive definite, this implies

ker(Sigma)=ker(G^T).

Therefore

range(Sigma)=ker(Sigma)^perp=ker(G^T)^perp=range(G),

and consequently rank(Sigma)=rank(G)=r.

If r=0, then G=0 and Sigma=0. The universal fixed-point assumption applies to the sampled exact truth, so

x_i-x^star=P(x_0)-P(x^star)=G(x_0-x^star)=0.

Thus the null-space condition holds, while the range condition is the vacuous standard-normal statement in dimension zero. Hence strong calibration holds in this case.

Now assume r>=1. Choose a rank factorization

G=Y W^T,

where Y,W are d by r matrices with full column rank. Put K=W^T Sigma_0 W. For every nonzero u in R^r,

u^T K u=(Wu)^T Sigma_0(Wu)>0,

so K is positive definite. Also range(G)=range(Y), and hence range(Sigma)=range(Y).

Choose R and N as in the task. Since the columns of R span range(Sigma), they are linearly independent and R^T Sigma R is positive definite: for every nonzero u, Ru is a nonzero vector in range(Sigma), and a positive-semidefinite matrix is positive definite on the orthogonal complement of its kernel. Thus the symmetric inverse square root in the target is well-defined.

Because the sampled x^star is an exact solution in the calibration experiment and the fixed-point property holds for every exact solution, P(x^star)=x^star almost surely. Hence

x_i-x^star=P(x_0)-P(x^star)=G(x_0-x^star).

This error lies in range(G)=range(Sigma). Since the columns of N span ker(Sigma)=range(Sigma)^perp,

N^T(x_i-x^star)=0

identically, and therefore almost surely.

Now sample x^star from N(x_0,Sigma_0), and write z=x^star-x_0. Then z is centered Gaussian with covariance Sigma_0, and

R^T(x_i-x^star)=-R^T G z

is centered Gaussian with covariance

R^T G Sigma_0 G^T R=R^T Sigma R.

For any centered Gaussian vector with positive-definite covariance C, C^(-1/2) times the vector has law N(0,I). Taking C=R^T Sigma R gives

(R^T Sigma R)^(-1/2)R^T(x_i-x^star) ~ N(0,I_r).

Together with the identically vanishing null-space component, this is exactly strong calibration.
