# Problem

## Setup

Let m,n,T be positive integers. For a real matrix A, let ||A||_op denote its largest singular value and ||A||_* the sum of its singular values. Write <A,B>=Tr(A^T B). Let S_+^m and S_{++}^m denote the symmetric positive semidefinite and positive definite m by m matrices, respectively. For symmetric matrices, A<=B means that B-A is positive semidefinite. All square roots of positive semidefinite matrices are their principal positive semidefinite square roots.

Fix G,D>0. Let G_1,...,G_T in R^{m x n} satisfy ||G_t||_op<=G. Decisions lie in K={X in R^{m x n}: ||X||_op<=D}. Define

S_t=sum_{s=1}^t G_s,   M_t=sum_{s=1}^t G_sG_s^T,   L_t=(G^2 I_m+M_t)^{1/2},

and Phi(S)=||S||_*.

For a finite convex function f on R^{m x n}, its subdifferential at S is

partial f(S)={Q: f(U)>=f(S)+<Q,U-S> for every U in R^{m x n}}.

For a differentiable function f, define

B_f(U||V)=f(U)-f(V)-<nabla f(V),U-V>.

For alpha,beta>0, an (alpha,beta)-admissible smoothing is a family of finite convex functions

\widetilde\Psi(.;L): R^{m x n} -> R,   L in S_+^m,

continuously differentiable in the matrix argument whenever L is positive definite, with the following properties:

1. For every S in R^{m x n} and L in S_+^m, there exists Q in partial_S \widetilde\Psi(S;L) with ||Q||_op<=1. In particular, for positive definite L this says ||nabla_S \widetilde\Psi(S;L)||_op<=1.
2. For every S and L in S_+^m, \widetilde\Psi(S;L)>=||S||_*, and \widetilde\Psi(S;0)=||S||_*.
3. For every S and every L_1,L_2 in S_+^m with L_1<=L_2,

   \widetilde\Psi(S;L_2)-\widetilde\Psi(S;L_1)<=alpha Tr(L_2-L_1).

4. For every L in S_{++}^m and U,V in R^{m x n},

   B_{\widetilde\Psi(.;L)}(U||V)<=(beta/2)Tr((U-V)^T L^{-1}(U-V)).

Set eta=sqrt(alpha/beta) and \widetilde\Phi_t(S)=\widetilde\Psi(S;L_t/eta). Run

X_1=0,   X_{t+1}=-D nabla \widetilde\Phi_t(S_t),

and define

Reg_T=sum_{t=1}^T <G_t,X_t>+D||S_T||_*.

## Task

Prove that every (alpha,beta)-admissible smoothing satisfies

Reg_T <= 2sqrt(alpha beta)D Tr(G^2 I_m+M_T)^{1/2} +(1-sqrt(alpha beta))D||G_1||_*.

Moreover, for the specific smoothing

\[
\widetilde\Psi^{\circ}(S;L)=\operatorname{Tr}(SS^T+LL^T)^{1/2},
\]

prove that it is (1,1)-admissible, that the corresponding update is

\[
X_{t+1}=-D(G^2 I_m+M_t+S_tS_t^T)^{-1/2}S_t,
\]

and that

Reg_T <= 2D(Tr M_T^{1/2}+mG).
