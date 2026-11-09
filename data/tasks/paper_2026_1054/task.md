# Problem

## Setup

Let (X,d_X) be a metric space, and let Y be Polish, both equipped with their Borel sigma-algebras. Let (X_i,Y_i)_{i=1}^n be iid with law P, with supp(P_Y)=Y and nondegenerate P_Y. Let k_Y:Y×Y→R be a bounded, continuous, characteristic kernel, and assume that no section k_Y(·,y) is constant. Using a regular conditional law of the response given the covariate, write
\[
V_Y(y)=\operatorname{Var}(k_Y(Y,y)),\qquad
m_{1,y}(x)=\mathbb E[k_Y(Y,y)\mid X=x],\qquad
m_{2,y}(x)=\mathbb E[k_Y(Y,y)^2\mid X=x].
\]
Assume that these conditional moments have versions satisfying the conditions below. All displayed assumption constants are finite, positive, and fixed independently of n and K.

Assume
\[
\int V_Y(y)^{-3}\,dP_Y(y)<C_3.
\]
For some x_*∈X and C_1,C_2,α>0, assume
\[
P_X\{d_X(X,x_*)≥t\}≤C_1e^{-C_2t^α}\qquad(t>0).
\]
For some d,c_0>0, every T>0, every x with d_X(x_*,x)≤T, and every r>0 satisfying c_0r^d≤1, assume
\[
P_X\{d_X(X,x)≤r\}≥c_0r^d.
\]
For some L,β>0, the conditional moments are uniformly Holder:
\[
|m_{\ell,y}(x)-m_{\ell,y}(x')|≤L\,d_X(x,x')^β,\qquad \ell∈\{1,2\},
\]
for all x,x'∈X and y∈Y.

Let n≥3 and let K=K_n be any deterministic integer sequence satisfying 1≤K≤⌊n/2⌋. Let N_j be the indices of the K nearest neighbours of X_j among {1,…,n}\{j}. For i≠j, let N_j^{\backslash i} be the indices of the K nearest neighbours of X_j among {1,…,n}\{i,j}. Ties are broken uniformly at random, with independent auxiliary randomizations independent of the observations; neighbour selections depend only on the covariates and this auxiliary randomness. Assume that, almost surely,
\[
\delta_\ell:=|\{j:\ell∈N_j\}|≤C_XK\qquad\text{for all }\ell∈\{1,…,n\},
\]
where C_X is independent of n and the admissible K.

Define the scalar population quantity
\[
D(Y,X)=1-\int\frac{\mathbb E_X[\operatorname{Var}(k_Y(Y,y)\mid X)]}{V_Y(y)}\,dP_Y(y).
\]
Define
\[
E_{n,i}^{K\text{-}NN}=\frac1{2K(n-1)}\sum_{j\ne i}\sum_{k∈N_j^{\backslash i}}\bigl(k_Y(Y_j,Y_i)-k_Y(Y_k,Y_i)\bigr)^2,
\]
\[
V_{n,i}^{K\text{-}NN}=\frac1{n-1}\sum_{j\ne i}k_Y(Y_j,Y_i)^2-\left(\frac1{n-1}\sum_{j\ne i}k_Y(Y_j,Y_i)\right)^2,
\]
and
\[
\widehat D^{K\text{-}NN}(Y,X)=1-\frac1n\sum_{i=1}^n\frac{E_{n,i}^{K\text{-}NN}}{V_{n,i}^{K\text{-}NN}}.
\]
In this last definition, assign the summand the value zero whenever V_{n,i}^{K\text{-}NN}=0.

## Task

Prove that, for every such deterministic sequence K_n, as n→∞,
\[
\left|\widehat D^{K\text{-}NN}(Y,X)-D(Y,X)\right|
=O_P\!\left(n^{-1/2}+\left(\frac Kn\right)^{β/d}+n^{-2}(\log n)^{β/α}\right).
\]
The stochastic-order constants may depend on the fixed law, kernel, and assumption constants, but not on n or the admissible K.
