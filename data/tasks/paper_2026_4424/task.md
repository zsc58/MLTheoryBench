# Problem

## Setup

Let X be an n x d real feature matrix, where n and d are positive integers. For a feature half A, write x_i^A for row i restricted to A, and define the cosine-distance RDM entry
\[
D^A_{ij}=1-\frac{x_i^A\cdot x_j^A}{\|x_i^A\|\,\|x_j^A\|},\qquad i<j,
\]
when the denominator is nonzero. The RDM vector lists these entries in a common row-pair order for both halves. Let \rho_s denote Spearman correlation of two RDM vectors, computed as Pearson correlation of their midranks; this requires both rank vectors to be nonconstant.

For a split into complementary halves A and B, if either restricted matrix X_A or X_B is identically zero, define its split-half score to be 0 without evaluating the RDM correlation. Otherwise, the split-half score is \rho_s(D^A,D^B), and is defined only when every restricted row in both halves is nonzero and both RDM rank vectors are nonconstant.

For d=4 there are three unordered equipartitions into two-element halves. Define the estimator only for matrices for which all three split-half scores are defined by the preceding rules. For K=30 independent uniformly sampled equipartitions, let S_30(X) be the average of the 30 split-half scores, and let \bar S(X)=E[S_30(X)] be the average over all three equipartitions. The matrix is fixed, and the expectation is over the partition draws only.

For centered linear CKA of real matrices U and V with n rows, put H=I_n-(1/n)\mathbf1\mathbf1^T, where \mathbf1 is the all-ones vector, and K_U=HUU^TH. Define
\[
\operatorname{CKA}(U,V)=\frac{\langle K_U,K_V\rangle_F}{\|K_U\|_F\,\|K_V\|_F}
\]
when both Frobenius norms in the denominator are nonzero.

## Task

Prove that SheshaFS is not invariant under orthogonal feature-basis rotations even though linear CKA can remain exactly one. In particular, exhibit a real 3 x 4 matrix X and an orthogonal 4 x 4 matrix Q such that, with Y=XQ, all the following quantities are defined and
\[
\operatorname{CKA}(X,Y)=1,\qquad \bar S(X)=\frac12,\qquad \bar S(Y)=-\frac13.
\]
Conclude that the K=30 estimator S_30 is not invariant in general.
