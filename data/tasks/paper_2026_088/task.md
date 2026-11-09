# Problem

## Setup

Let $(X_1,Y_1),\ldots,(X_n,Y_n),(X_{n+1},Y_{n+1})$ be exchangeable random labeled examples in measurable input and label spaces $\mathcal X$ and $\mathcal Y$. Let $\alpha\in(0,1)$, let $n\ge1$ be an integer, and let $k$ be a fixed integer satisfying $1\le k<n$. Write $Z_i=(X_i,Y_i)$.

Fix a one-shot prediction mechanism $\pi$ and its real-valued score rule. Every labeled reference pair $z'=(x',y')$ induces a predictor $\pi_{z'}(\cdot\mid x)=\pi(\cdot\mid x;z')$ and a nonconformity score $s_{z'}(x,y)$, with smaller values more conforming. The map $(z',x,y)\mapsto s_{z'}(x,y)\in\mathbb R$ is fixed and jointly measurable. For $z=(x,y)$, also write $s_{z'}(z)=s_{z'}(x,y)$.

A finite reference dataset is an indexed collection of labeled pairs, with repeated observations retained. For such a collection $D$ and target $z$, let
\[
A_D(z)=\{s_{z'}(z):z'\in D\}
\]
be the multiset containing one score for each occurrence in $D$. For a finite multiset $A$ of size $m\ge k$, with ordered values $a_{(1)}\le\cdots\le a_{(m)}$, define
\[
\Sigma_k(A)=\sum_{r=1}^k a_{(r)}.
\]
For $|D|\ge k$, put $S_D(z)=\Sigma_k(A_D(z))$.

Let $D_n=(Z_1,\ldots,Z_n)$, and let $D_n^{-i}$ be this collection with only the occurrence at index $i$ deleted. Define
\[
S_i=S_{D_n^{-i}}(Z_i),\qquad i=1,\ldots,n,
\]
and put $\beta=(1-\alpha)(1+1/n)$. For a finite list of real numbers $u_1,\ldots,u_n$, define
\[
\operatorname{Quantile}_\beta(u_1,\ldots,u_n)
=\inf\{t\in\mathbb R:n^{-1}\#\{i:u_i\le t\}\ge\beta\},
\]
with the infimum of the empty set equal to $+\infty$. Set $q=\operatorname{Quantile}_\beta(S_1,\ldots,S_n)$ and
\[
C(X_{n+1})=\{y\in\mathcal Y:S_{D_n}(X_{n+1},y)\le q\}.
\]

## Task

Prove that
\[
\Pr\{Y_{n+1}\in C(X_{n+1})\}\ge1-\alpha.
\]
