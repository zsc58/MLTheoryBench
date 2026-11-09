# Problem

## Setup

Let \(d,K\) be positive integers, let \(1\le k\le K\), and let \(T\) be a finite index set. Fix \(z_t\in\mathbb R^d\setminus\{0\}\) for \(t\in T\), and put \(v_t=z_t/\|z_t\|_2\). Let \(P=[p_1,\ldots,p_K]\in\mathbb R^{d\times K}\), with every \(p_j\ne0\), and put \(q_j=p_j/\|p_j\|_2\).

At this reference matrix, each token retains a set \(K_t\subseteq\{1,\ldots,K\}\) of at most \(k\) indices by keeping the largest strictly positive similarities \(v_t^{\mathsf T}q_j\), up to \(k\) of them. Define the numerical activation vector by
\[
a_{t,j}=\max\{v_t^{\mathsf T}q_j,0\}\,\mathbf 1_{\{j\in K_t\}},
\qquad
\widehat z_t=Pa_t,\qquad r_t=z_t-\widehat z_t,\qquad
G_A=\sum_{t\in T}a_ta_t^{\mathsf T}.
\]
The vectors \(a_t\) are held fixed when differentiating the reconstruction objective.

Let \(\mathcal J\) be the finite collection of selected clustering terms. Each \(s\in\mathcal J\) has fixed indices \(t(s)\in T\) and \(k(s)\in K_{t(s)}\), and a fixed coefficient \(c_s\ge0\) incorporating its loss weight and normalization. Every selected pair satisfies \(v_{t(s)}^{\mathsf T}q_{k(s)}>0\). Work in a local region where supports, selected winner identities, and these positive branches remain unchanged. For a variable prototype matrix \(X=[x_1,\ldots,x_K]\) near \(P\), define
\[
L_{\rm rec}(X)=\frac\eta2\sum_{t\in T}\|z_t-Xa_t\|_2^2,
\qquad
L_{\rm clst}(X)=-\sum_{s\in\mathcal J}c_s\,v_{t(s)}^{\mathsf T}\frac{x_{k(s)}}{\|x_{k(s)}\|_2},
\qquad \eta>0.
\]
Thus reconstruction uses frozen numerical activations, whereas the selected cosine expressions in clustering are differentiated. Define
\[
H_{\rm rec+clst}
=\left.\nabla^2_{\operatorname{vec}(X)}\bigl(L_{\rm rec}(X)+L_{\rm clst}(X)\bigr)\right|_{X=P},
\]
where \(\operatorname{vec}(X)\) stacks the columns of \(X\).

At \(P\), define
\[
A_j=\sum_{s:k(s)=j}c_s\,v_{t(s)}^{\mathsf T}q_j,
\qquad
b_j=\sum_{s:k(s)=j}c_s v_{t(s)},
\qquad
t_j=b_j-A_jq_j.
\]
Empty sums are zero. Let
\[
S=\{j:\text{there exists }s\in\mathcal J\text{ with }k(s)=j\text{ and }c_s>0\}
\]
be the set of supported clustering indices; indices outside \(S\) are unsupported. Write
\[
G_{A,S}=(G_A)_{S,S},\qquad
D=\operatorname{diag}_{j\in S}\left(\frac{A_j}{\|p_j\|_2^2}\right),
\]
using the same increasing index order for both matrices. The conditioning assertion below applies only when \(S\ne\varnothing\). For a real symmetric positive-definite matrix \(C\), define \(\kappa(C)=\|C\|_2\|C^{-1}\|_2\), where the matrix norm is the spectral norm. For a real symmetric matrix, \(\lambda_{\max}\) denotes its largest eigenvalue.

## Task

Prove
\[
H_{\rm rec+clst}=\eta G_A\otimes I_d+\operatorname{diag}(B_1,\ldots,B_K),
\qquad
B_j=\frac{A_j(I_d-q_jq_j^{\mathsf T})+q_jt_j^{\mathsf T}+t_jq_j^{\mathsf T}}{\|p_j\|_2^2},
\]
including \(B_j=0\) for unsupported indices.

Also, when \(S\ne\varnothing\) and \(D\succ0\), define
\[
H_{\rm tan}=D+\eta G_{A,S},\qquad
M=\eta D^{-1/2}G_{A,S}D^{-1/2}.
\]
Prove
\[
H_{\rm tan}=D^{1/2}(I_{|S|}+M)D^{1/2},
\qquad
\kappa(D^{-1/2}H_{\rm tan}D^{-1/2})
=\kappa(I_{|S|}+M)
\le1+\lambda_{\max}(M).
\]
