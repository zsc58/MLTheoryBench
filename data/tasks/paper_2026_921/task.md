# Problem

## Setup

Let T>0 and N>=1. Player i has scalar state and control. Let the initial states xi^1,...,xi^N be mutually independent, square-integrable random variables with Var(xi^i)>0, independent of the independent standard Brownian motions B^1,...,B^N. The state dynamics are
\[
dX_t^i=u^i(t,X_t^i)\,dt+\sigma_t^i\,dB_t^i,\qquad X_0^i=\xi^i.
\]
Here sigma^i:[0,T]->R is deterministic and continuous. A distributed admissible policy is a deterministic measurable function u^i:[0,T]xR->R for which this equation has a unique strong solution and
\[
\mathbb E\!\left[\sup_{0\le t\le T}|X_t^i|^2\right]
+\mathbb E\!\left[\int_0^T|u^i(t,X_t^i)|^2dt\right]<\infty.
\]
Write V^i for this class and V for its product over players. Each Q^i is a symmetric positive-definite N-by-N matrix, gamma^i>=0, and d^i is real. For u in V, let X=(X^1,...,X^N)^T and
\[
J^i(u)=\mathbb E\left[\int_0^T\left(|u^i(t,X_t^i)|^2+X_t^TQ^iX_t\right)dt+\gamma^i|X_T^i-d^i|^2\right].
\]

Define Q by
\[
Q_{ii}=Q^i_{ii}+\frac12\sum_{k\ne i}(Q^i_{ik}-Q^k_{ki}),\qquad Q_{ij}=Q^i_{ij}\quad(i\ne j),
\]
and set Lambda=diag(gamma^1,...,gamma^N), d=(d^1,...,d^N)^T, and
\[
\Phi(u)=\mathbb E\left[\int_0^T\left(\sum_i|u^i(t,X_t^i)|^2+X_t^TQX_t\right)dt+(X_T-d)^T\Lambda(X_T-d)\right].
\]
Assume Q_sym=(Q+Q^T)/2 is positive semidefinite. Set
\[
C_Q=\max_i\sum_{j\ne i}|Q^i_{ij}-Q^j_{ji}|.
\]

Fix finite positive numbers M_b^v and M_b^m. Define the deviation class
\[
\mathcal V_b^i=\left\{u^i\in\mathcal V^i:
\int_0^T\operatorname{Var}(X_t^i)dt\le M_b^v,
\quad \|\mathbb E X^i\|_{L^2(0,T)}\le M_b^m\right\},
\]
where the state is controlled by u^i, and put
\[
\alpha=(M_b^v+3(M_b^m)^2)C_Q.
\]
The class V_b^i includes all admissible feedbacks satisfying these bounds; it is not restricted to affine feedbacks.

## Learning policies and parameter conditions

The learning iterates use affine distributed policies
\[
u^i_{K,G}(t,x)=K_t^i\bigl(x-\mathbb EX_t^i\bigr)+G_t^i,
\qquad K^i,G^i\in L^2([0,T],\mathbb R),
\]
where the expectation is under that player's policy and initial law. Write m^{K,G,i}=E[X^i] and v^{K,G,i}=Var(X^i). The symbols grad_{K^i}J^i and grad_{G^i}J^i denote the exact L2 gradients of the cost as a function of the affine parameters, with the other parameters fixed. Define
\[
D_{K^i}J^i(t)=\frac{\nabla_{K^i}J^i(t)}{v_t^{K,G,i}}.
\]
All parameter equations are interpreted almost everywhere in time.

Fix initial gains K_0^i in L-infinity, initial intercepts G_0^i in L2, and a projection radius Cbar_G>0 with ||G_0^i||_2<=Cbar_G. To specify the moment-size conditions, let R_0^i be the absolutely continuous solution of
\[
\dot R_0^i(t)+2K_0^i(t)R_0^i(t)+(K_0^i(t))^2+Q^i_{ii}=0,
\qquad R_0^i(T)=\gamma^i,
\]
and define
\[
B=\max_i\bigl(\|K_0^i\|_{L^\infty}+\|R_0^i\|_{L^\infty}\bigr).
\]
Assume the moment bounds satisfy
\[
M_b^m\ge\max_i\sup_{\substack{K^i\in L^2,\ G^i\in L^2\\ \|G^i\|_2\le\overline C_G}}
\|m^{K,G,i}\|_2,
\qquad
M_b^v\ge\max_i\sup_{\substack{K^i\in L^\infty,\ G^i\in L^2\\ \|K^i\|_\infty\le B}}
\|v^{K,G,i}\|_1.
\]
Here Cbar_G and \(\overline C_G\) denote the same projection radius; these suprema concern the scalar policy of player i. Also assume that, for every affine global minimizer u_{K*,G*} of Phi over V, its intercept satisfies max_i||G*^i||_2<=Cbar_G.

For a common gain step eta_K>0 and player-specific intercept steps eta_G^i>0, run
\[
K_{n+1}^i=K_n^i-\eta_K D_{K^i}J^i(K_n,G_n),
\]
\[
G_{n+1}^i=\Pi_{\{g\in L^2:\|g\|_2\le\overline C_G\}}
\bigl(G_n^i-\eta_G^i\nabla_{G^i}J^i(K_n,G_n)\bigr),
\]
where Pi is orthogonal projection in L2. Put eta_G^min=min_i eta_G^i and eta_G^max=max_i eta_G^i.

## Task

Prove that there exists a positive step threshold, depending only on the fixed game data, initial gain bounds, projection radius, moment bounds, and horizon, with the following property. For fixed steps below this threshold satisfying
\[
\eta_G^{\min}>\frac{\eta_G^{\max}}{1+2\eta_G^{\max}},
\]
there are finite nonnegative constants c_1,c_2 and nonnegative residuals delta_1(C_Q),delta_2(C_Q), independent of epsilon, the iteration index, the player, and the unilateral deviation, such that
\[
\delta_1(C_Q)\le c_1NC_Q^2,\qquad
\delta_2(C_Q)\le c_2NC_Q^2.
\]
The constants may depend on the fixed game data, initial gain bounds, projection radius, moment bounds, horizon, and chosen steps.

For every epsilon>0, prove that there is an integer M>=0 such that, for every n>=M, the policy u_n=u_{K_n,G_n} belongs to the product of the classes V_b^i and satisfies simultaneously for every player i and every deviation tilde u^i in V_b^i,
\[
J^i(u_n)\le J^i(\tilde u^i,u_n^{-i})+\epsilon+\delta(C_Q),
\qquad
\delta(C_Q)=\alpha+\delta_1(C_Q)+\delta_2(C_Q).
\]
Show that M=O(1+log_+(1/epsilon)), where log_+(x)=max(0,log x); in particular the iteration count is O(log(1/epsilon)) as epsilon decreases to zero. Thus the residual vanishes when C_Q=0.
