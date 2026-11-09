# Problem

## Setup

Let (M,g) be a complete, connected, smooth d-dimensional Riemannian manifold, with Riemannian volume measure rho. Let q_1:M to [0,infinity) be measurable and rho-integrable with positive integral, and let the target probability have density p_1=q_1/(integral_M q_1 d rho) with respect to rho. Let pi_{0,1} be a coupling of probabilities pi_0 and pi_1 that is absolutely continuous with respect to rho tensor rho, with joint density p_{0,1}. Its marginal densities satisfy

p_0(x)=integral_M p_{0,1}(x,y)d rho(y),

p_1(y)=integral_M p_{0,1}(x,y)d rho(x),

where marginal-density identities are understood rho-almost everywhere.

Fix a jointly measurable conditional probability-density kernel p_{0|1}(x|y), normalized by integral_M p_{0|1}(x|y)d rho(x)=1 for every y, such that

p_{0,1}(x,y)=p_1(y)p_{0|1}(x|y)

for rho tensor rho-almost every (x,y). On endpoints where p_1(y)=0, choose p_{0|1}(x|y)=p_0(x). All density versions may be taken Borel measurable.

For y in M, let C(y) be its cut locus, ID(y) its injectivity domain, including the zero tangent vector, Exp_y the exponential map, and Log_y its inverse on M\C(y). For a unit tangent vector u, let c_y(u) denote the cut time, namely the supremum of s>0 for which the geodesic r maps to Exp_y(ru), 0<=r<=s, is minimizing. The cut time may be infinite.

For x outside C(y), define

F_t(x;y)=Exp_y((1-t)Log_y x),  0<=t<=1.

For (X_0,X_1) with law pi_{0,1}, let pi_t be the law of F_t(X_0;X_1), using any fixed measurable extension on pairs with X_0 in C(X_1). Write p_t for its density with respect to rho when it exists. For 0<=t<1, define

U_t(y)=Exp_y((1-t)ID(y)).

The Jacobi determinant in the statement has the following normalization. For a unit vector u in T_yM, let gamma(s)=Exp_y(su), and let P_s be parallel transport from T_yM along gamma to T_{gamma(s)}M. For w in u-perp, let J_w be the normal Jacobi field along gamma satisfying J_w(0)=0 and covariant derivative nabla_s J_w(0)=w. Define the endomorphism B_{y,u}(s) of u-perp by

B_{y,u}(s)w=P_s^{-1}J_w(s),  s>=0.

The determinant is taken on u-perp; on a zero-dimensional normal space its value is 1.

## Task

Prove the following integrated theorem.

For rho tensor rho-almost every (x,y), the curve t maps to F_t(x;y) is well defined by the exponential-logarithm formula and smooth on [0,1].

For every y and 0<=t<1, F_t(.;y) is a smooth diffeomorphism from M\C(y) onto the open set U_t(y), with inverse

F_t^{-1}(z;y)=Exp_y(Log_y z/(1-t)),  z in U_t(y).

Moreover, for z different from y and outside C(y), writing r=dist(y,z) and u=Log_y z/r, membership z in U_t(y) is equivalent to

r<(1-t)c_y(u).

Finally, for each 0<=t<1, a regular conditional distribution of X_t given X_1 can be chosen to have a jointly measurable density p_{t|1}(z|y) with respect to rho for every y. For this choice and every y, the density is given for rho-almost every z different from y by

p_{t|1}(z|y) =

- p_{0|1}(F_t^{-1}(z;y)|y) * det B_{y,u}(r/(1-t)) / ((1-t) det B_{y,u}(r)), if z is in U_t(y) and z is different from y, where r=dist(y,z) and u=Log_y z/r;
- 0, if z is outside U_t(y).

Thus the inverse and determinant ratio are evaluated only on their indicated domain, rather than evaluated outside that domain and multiplied by zero. If p_{0|1}(.;y) is smooth for a fixed y, then p_{t|1}(.;y) has a representative that is smooth on all of U_t(y), including y.
