# Problem

## Setup

Let n and d be positive integers with d>n. Let x_1,...,x_n be iid random vectors in R^d with mean zero and covariance Sigma=V Lambda V^T, where V is orthogonal and Lambda is diagonal with nonnegative entries. Suppose x_i=V Lambda^{1/2}z_i, where each z_i has independent mean-zero 1-subgaussian coordinates; here 1-subgaussian means E exp(u z_{i,j})<=exp(u^2/2) for every real u. Let X=[x_1^T;...;x_n^T] have rank n. Write lambda for the eigenvalues of Sigma, L=||lambda||_1, d_2=L^2/||lambda||_2^2, and d_infty=L/||lambda||_infty. Labels are arbitrary and satisfy 0<y_min<=|y_i|<=y_max and

 d_2>=C_0^2 n^2 y_max^2/y_min^2,  d_infty>=C_0 n^{3/2} y_max/y_min.

Fix a universal numerical factor K sufficiently large. The universal constants C_g,C_y,C_alpha,C_eta,C_lb are positive, C_eta>=1, and

C_alpha>=K max{C_g^2,C_y C_g,C_eta C_g},
C_0>=K C_alpha^2,
and C_lb>=K max{C_alpha^2,C_eta^2 C_g}.

Consider h_w(x)=max{w^T x,0}, with h_w(X)=(h_w(x_1),...,h_w(x_n))^T, R(w)=1/2||h_w(X)-y||_2^2, and the iteration

w^{t+1}=w^t-eta X^T D_t(h_w(X)-y),  D_t=diag(1{x_i^T w^t>0}),

for integers t>=0. Choose

1/(C_eta C_g L)<=eta<=1/(C_g L),
w^0=X^T(XX^T)^(-1)epsilon,

where 0<epsilon_i<=y_min/C_alpha. Let S_+={i:y_i>0}, S_-={i:y_i<=0}, let X_+,X_- be the corresponding row submatrices, let y_+ be the subvector of y indexed by S_+, and let n_-=|S_-|. Define w^1 by the first update. Let w^star be the unique minimizer of

min_w 1/2||w||_2^2 subject to x_i^T w=y_i for i in S_+ and x_j^T w<=0 for j in S_-.

Empty row submatrices have zero rows, and their associated constraints are vacuous.

## Task

Prove that there are universal c>0 and universal constants satisfying the above conditions, independent of n,d,the feature distribution, labels, eta, and epsilon, such that for every setup and choices as specified, with probability at least 1-2e^{-cn} over the sampled features, activation is fixed from t=1 onward with positive-label points active and nonpositive-label points inactive, the iterates converge in Euclidean norm to

w^infty=argmin_{X_+w=y_+}||w-w^1||_2 with X_-w^infty<=0,

and

sqrt(n_- y_min^2/(C_lb C_g L)) <= ||w^infty-w^star||_2 <= sqrt(16 n_- y_max^2/(C_g L)).
