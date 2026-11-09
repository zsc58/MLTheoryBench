# Problem

## Setup

Let `D subset R^m` and `E subset R^r` be compact sets with Lipschitz boundaries. Let `C(D x E)` denote real-valued continuous functions with the sup norm, and let `C_ac(D x E)` be the set of continuous nonnegative functions integrating to one over `D x E`. For `rho in C_ac(D x E)`, define

`m_rho(y) = integral_D rho(x,y) dx`.

For `delta > 0`, set

`X_delta = { rho in C_ac(D x E) : inf_{y in E} m_rho(y) >= delta }`.

Define

`Psi*: X_delta x E -> C(D)`, `Psi*(rho,y)(x) = rho(x,y)/m_rho(y)`.

Fix the neural-operator architecture and a fixed activation `sigma`. On a common Lipschitz domain `Omega`, a neural operator is a finite composition of a lifting layer `R(f)(u)=R(u,f(u))`, hidden layers

`L_l(f)(u)=sigma(W_l f(u)+b_l+sum_j <T_{l,j}f,psi_{l,j}> phi_{l,j}(u))`,

and a projection layer `Q(f)(u)=Q(u,f(u))`, with the displayed pairings taken in `L^2`. We use the distinct-input/output-domain variant of this architecture, allowing input functions on `D x E` and output functions on `D`. The fixed activation and this variant are assumed to have the following compact-set approximation property: for every continuous map `H:C(D x E;R^{r+1})->C(D)`, every compact `A subset C(D x E;R^{r+1})`, and every `eta>0`, there is a neural operator `N:C(D x E;R^{r+1})->C(D)` of this architecture such that `sup_{a in A} ||H(a)-N(a)||_infinity <= eta` whenever `A` is nonempty.

A vector-to-function layer on input domain `Omega` has the form `V(z)(u)=h(u) psi(z)`, where `h` is a function on `Omega` and `psi` is a neural network; the identity network is permitted. An augmented neural operator maps `(f,z)` to `N(f direct-sum V(z))`, where `direct-sum` is pointwise channel concatenation.

## Task

Prove the following theorem.

For every `delta > 0`, every compact subset `K` of `X_delta`, and every `epsilon > 0`, there exists a single augmented neural operator

`tilde_Psi : C(D x E) x E -> C(D)`

such that

`sup_{(rho,y) in K x E} ||Psi*(rho,y)-tilde_Psi(rho,y)||_infinity <= epsilon`.
