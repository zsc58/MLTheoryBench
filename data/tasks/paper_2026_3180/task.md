# Problem

## Setup

Fix T>0 and an integer N>=1, and set tau=T/N and t_j=j tau for j=0,...,N. Let d, k, and m be positive integer state, control, and noise dimensions. Let A be a nonempty compact convex subset of R^k. The coefficients b:[0,T]xR^d x A -> R^d and sigma:[0,T]xR^d x A -> R^{d x m} are measurable, 1/2-Holder in time, globally Lipschitz in state and control, and of uniform linear growth. The running cost f:[0,T]xR^d x A -> R has the same time and state/control regularity and uniform linear growth, and the terminal cost g:R^d -> R is globally Lipschitz. The Euclidean norm is used for vectors and the Frobenius norm for matrices. Degenerate or deterministic sigma is allowed.

Let G be the Borel measurable maps R^d -> A. On an innovation probability space let Z_1,...,Z_N be independent standard Gaussian vectors in R^m, with expectation E. For a deterministic x in R^d and a feedback policy alpha=(alpha_0,...,alpha_{N-1}) in G^N, define

X_{t_0}^{x,alpha}=x,
X_{t_{j+1}}^{x,alpha}=X_{t_j}^{x,alpha}+tau b(t_j,X_{t_j}^{x,alpha},alpha_j(X_{t_j}^{x,alpha}))+sqrt(tau) sigma(t_j,X_{t_j}^{x,alpha},alpha_j(X_{t_j}^{x,alpha})) Z_{j+1},

tilde J(0,x,alpha)=E[tau sum_{j=0}^{N-1} f(t_j,X_{t_j}^{x,alpha},alpha_j(X_{t_j}^{x,alpha}))+g(X_{t_N}^{x,alpha})],

and V_0(x)=inf_{alpha in G^N} tilde J(0,x,alpha).

On an independent auxiliary probability space let xi be R^d-valued, with expectation E_0, xi in L2, and |xi|<=R almost surely for some R>=0. For a fixed policy alpha, tilde J(0,xi,alpha) denotes the auxiliary-space random variable omega_0 -> tilde J(0,xi(omega_0),alpha): E in its definition averages over the Gaussian innovations while holding the initial state fixed. Write G_L for the L-Lipschitz maps R^d -> A, where L>=0, and let hat G_L be a nonempty subclass of G_L. For M>R, write B_M={x in R^d:|x|<=M}, diam(A)=sup_{a,a' in A}|a-a'|, and

d_{infty,B_M}(u,hat G_L)=inf_{h in hat G_L} sup_{x in B_M}|u(x)-h(x)|.

Let epsilon>0 and assume bar alpha^epsilon in G^N satisfies E_0[tilde J(0,xi,bar alpha^epsilon)] <= E_0[V_0(xi)]+epsilon. For eta>0 assume hat alpha in hat G_L^N satisfies

E_0[tilde J(0,xi,hat alpha)] <= inf_{alpha in hat G_L^N} E_0[tilde J(0,xi,alpha)]+eta,

and set hat V_0(x)=tilde J(0,x,hat alpha).

## Task

Prove that there is a constant C_{T,L}, depending only on T, L, the coefficient and cost bounds, and the dimensions (but not on N, M, R, xi, epsilon, or eta), such that, for every M>R,

E_0|hat V_0(xi)-V_0(xi)| <= C_{T,L}[(tau sum_{j=0}^{N-1} d_{infty,B_M}^2(bar alpha^epsilon_j,hat G_L))^(1/2) + diam(A)(1+E_0|xi|^2)^(1/2)/(M-R)] + epsilon + eta.

The estimate requires no nondegeneracy assumption on the controlled dynamics.
