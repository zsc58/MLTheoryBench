# Problem

## Setup

For a symmetric matrix $A\in\mathbb{R}^{n\times n}$, where $n$ is a positive integer, and a parameter $R>0$, define
\[
\operatorname{OPT}(A,R)=\max_{x\in\mathbb{R}^n}\left\{x^\top A x:\ \|x\|_1\le1,\ \|x\|_2=R\right\}
\]
when the feasible set is nonempty, and set $\operatorname{OPT}(A,R)=-\infty$ otherwise.

For a simple undirected loopless graph $G$ on $n$ vertices, let $A(G)$ be its adjacency matrix. Given an integer $k$ with $1<k<n$, consider the restricted instances with $A=A(G)$ and $R=1/\sqrt{k}$. For computational purposes, these restricted instances are encoded by the graph $G$ and the integer $k$ in binary; the radius is specified exactly by the expression $1/\sqrt{k}$.

## Task

Prove that computing $\operatorname{OPT}(A,R)$ exactly is NP-hard. More precisely, for every such graph and $k$,
\[
\operatorname{OPT}(A(G),1/\sqrt{k})=1-1/k
\quad\Longleftrightarrow\quad
G\text{ contains a clique of size }k,
\]
and if $G$ contains no $k$-clique then $\operatorname{OPT}(A(G),1/\sqrt{k})<1-1/k$.
