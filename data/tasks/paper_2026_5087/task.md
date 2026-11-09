# Problem

## Geometry and parameters

Fix integers d>=1, N>=1 and m,l>=0, a step size Delta t>0, a friction parameter gamma>=0, and epsilon>0. Let h:R^d->R^m and g:R^d->R^l be smooth, and set

Sigma={x in R^d:h(x)=0, g(x)<=0}.

Assume Sigma is a stratified manifold. For x in R^d, let I_x={j in {1,...,l}:g_j(x)>=0}. Assume there is an open neighborhood U of Sigma such that, for every x in U and every subset B of I_x, the matrix with rows

{nabla h_i(y)^T:1<=i<=m} and {nabla g_j(y)^T:j in B}

has constant rank for y in a sufficiently small neighborhood of x, with B held fixed. Assume U contains the forward and generated reverse positions defined below, almost surely for every parameter value.

Let J(x) be the vector obtained by stacking h(x) and g_j(x)+epsilon for j in I_x. Let A(x) be the matrix obtained by stacking the corresponding gradient rows at x; this defines the selected-gradient matrix even when I_x changes. Define

G(x)=A(x)A(x)^T,
Pi(x)=I_d-A(x)^T G(x)^dagger A(x),

where dagger denotes the Moore-Penrose inverse. Thus Pi(x) is the orthogonal projector onto ker A(x). Empty constraint matrices give Pi(x)=I_d. These formulas are used for ambient points as well as points of Sigma.

Fix positive schedule values sigma_0,...,sigma_N satisfying

0<sigma_min<=sigma_j<=sigma_max<infinity,

and set sigma_{N+1}=sigma_N and a_j=exp(-gamma sigma_j^2 Delta t) for 0<=j<=N.

## Coefficients and forward experiment

Let Theta be a nonempty parameter set. All objects and probability laws in the setup are independent of theta in Theta except the displayed family b_j^theta and the reverse laws constructed from it.

For 1<=j<=N, let b_j^theta:R^d x R^d->R^d satisfy, for finite L,B independent of j and theta,

||b_j^theta(x,p)-b_j^theta(x',p')||<=L(||x-x'||+||p-p'||),
||b_j^theta(x,p)||<=B(1+||x||+||p||).

Let phi:R^d x R^d->R^d be Borel and normal in the sense Pi(x)phi(x,p)=0. For 0<=j<N, let u_j,psi_j:R^d x R^d->R^d be fixed Borel maps, with Pi(x)psi_j(x,p)=0 and

||u_j(x,p)||<=B_f(1+||x||+||p||)

for a finite B_f. For every real r>=1 assume there is a finite c_r such that, for all x,p and all 0<=j<N,

||phi(x,p)||^{2r}+||psi_j(x,p)||^{2r}
<=c_r(1+||x||^{2r}+||p||^{2r}+||p||^{4r}).

Let X_0 have a fixed law Q_0 with E||X_0||^{2r}<infinity for every r>=1. Let Z_in,Z_0,...,Z_{N-1} be independent standard Gaussian vectors in R^d, independent of X_0. Set v_0=Pi(X_0)Z_in and, for 1<=j<N, set

v_j=Pi(X_j)(X_j-X_{j-1})/(sigma_{j-1}^2 Delta t).

Define the forward positions recursively for 0<=j<N by

X_{j+1}=X_j+sigma_j^2 Delta t Pi(X_j)[a_j v_j+sigma_j^2 Delta t u_j(X_j,v_j)]
+sigma_j^2 Delta t sqrt(1-a_j^2)Pi(X_j)Z_j
+sigma_j^2 Delta t psi_j(X_j,v_j).

Independently of the entire forward experiment, draw Z_*~N(0,I_d) and define the terminal auxiliary point by

X_{N+1}=X_N+sigma_{N+1}^2 Delta t Pi(X_N)Z_*.

For 0<=k<=N, let bar Q_k be the law of (X_k,X_{k+1}). For 0<=k<N, write Q_{k|k+1,k+2} for a regular conditional law of X_k given (X_{k+1},X_{k+2}).

## Reverse experiment

For 1<=j<=N and x,x' in R^d, define

p_j(x,x')=Pi(x)(x'-x)/(sigma_{j+1}^2 Delta t)

and

m_j^theta(x,x')=x-sigma_j^2 Delta t Pi(x)[a_j p_j(x,x')+sigma_j^2 Delta t b_j^theta(x,p_j(x,x'))]
+sigma_j^2 Delta t phi(x,p_j(x,x')).

Let R_j^theta(.|x,x') be the Gaussian probability law with mean m_j^theta(x,x') and covariance

sigma_j^4 Delta t^2(1-a_j^2)Pi(x).

Singular covariance is allowed. Its pair kernel bar R_j^theta samples y from R_j^theta(.|x,x') and returns (y,x).

Fix a terminal position prior pi_N on R^d satisfying

integral ||x||^{2r} pi_N(dx)<infinity for every r>=1.

To define the base pair prior bar pi_N, independently draw Y_N~pi_N and Z_pr~N(0,I_d), set

Y_{N+1}=Y_N+sigma_{N+1}^2 Delta t Pi(Y_N)Z_pr,

and take bar pi_N=Law(Y_N,Y_{N+1}). Starting from this pair, apply bar R_N^theta,...,bar R_1^theta in descending order, using fresh independent Gaussian randomness at each step. Define

bar P_0^theta=bar pi_N bar R_N^theta...bar R_1^theta,
P_0^theta=(pr_1)_#bar P_0^theta,

where pr_1(x,y)=x and # denotes pushforward of a probability law.

## Objective and task

All norms are Euclidean. For probability laws mu,nu on the same Euclidean space, use

W_2(mu,nu)=[inf_{lambda in Cpl(mu,nu)} integral ||x-y||^2 lambda(dx,dy)]^{1/2},

where Cpl(mu,nu) is the set of their joint probability laws with marginals mu and nu.

Define

L^u(theta)=E sum_{k=0}^{N-1} ||Pi(X_{k+1})(X_k-m_{k+1}^theta(X_{k+1},X_{k+2}))||^2,

where expectation includes the forward experiment and its independent terminal Gaussian Z_*.

Prove that there are finite nonnegative constants C_1,C_2,C_3, independent of theta, such that for every theta in Theta,

W_2(Q_0,P_0^theta)<=C_1 L^u(theta)+C_2+C_3 Delta t.

The constants may depend on the fixed finite grid, schedule, geometry, coefficient bounds, initial law, and terminal position prior. No uniformity as the grid is refined is requested.
