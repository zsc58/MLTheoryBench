# Problem

## Setup

Let $\mathcal X$ be a finite CW complex of dimension $K$. For each rank $k$, let $C^k(\mathcal X)$ be the real cell-coordinate space on its oriented $k$-cells, equipped with the standard Euclidean inner product. Spaces outside ranks $0,\ldots,K$ are zero spaces. For $1\le k\le K$, let
\[
B_k:C^k(\mathcal X)\longrightarrow C^{k-1}(\mathcal X)
\]
be the signed cellular boundary incidence matrix. Let $B_0$ and $B_{K+1}$ be the corresponding zero maps at the two ends. Thus $B_{k-1}B_k=0$ for $1\le k\le K$. Set
\[
C^\bullet(\mathcal X)=\bigoplus_{k=0}^K C^k(\mathcal X).
\]
Choose real weights $\beta_1,\ldots,\beta_K\ge0$ and $\gamma_0,\ldots,\gamma_{K-1}\ge0$. Define the symmetric block-tridiagonal operator $L^*$ on $C^\bullet(\mathcal X)$ by diagonal blocks
\[
D_k=\beta_kB_k^\top B_k+\beta_{k+1}B_{k+1}B_{k+1}^\top,
\qquad 0\le k\le K,
\]
omitting the first term at $k=0$ and the second term at $k=K$. Its off-diagonal blocks between ranks $k$ and $k+1$ are $-\gamma_kB_{k+1}$ and its transpose. Assume that, for each $0\le k<K$, if $B_{k+1}\ne0$ then
\[
\gamma_k\le \beta_{k+1}\,\sigma_{\min}^+(B_{k+1}),
\]
where $\sigma_{\min}^+$ denotes the smallest positive singular value; if $B_{k+1}=0$, impose no condition on $\gamma_k$ beyond nonnegativity.

Let
\[
H=\bigoplus_{k=1}^K C^k(\mathcal X)
\]
and partition $L^*$ according to $C^0(\mathcal X)\oplus H$:
\[
L^*=\begin{bmatrix}A&X\\X^\top&C\end{bmatrix}.
\]
Here $X:H\to C^0(\mathcal X)$ is the coupling matrix, distinct from the complex $\mathcal X$. Let $C^\dagger$ denote the Moore–Penrose pseudoinverse of $C$, and let $I$ denote the identity on $H$. For $\epsilon>0$ define
\[
S_\epsilon=A-X(C+\epsilon I)^{-1}X^\top,
\qquad
S^\dagger=A-XC^\dagger X^\top.
\]
All matrix norms $\|\cdot\|_2$ are Euclidean operator norms. If $C$ has positive eigenvalues, write $\lambda_+=\lambda_{\min}^+(C)$ for its smallest positive eigenvalue.

## Task

Prove that the regularized collapsed operator converges in operator norm to the pseudoinverse collapse. Specifically, whenever $C$ has a positive eigenvalue,
\[
\|S_\epsilon-S^\dagger\|_2\le
\frac{\epsilon\|X\|_2^2}{\lambda_+(\lambda_++\epsilon)}
\quad\text{for every }\epsilon>0,
\]
and $S_\epsilon\to S^\dagger$ as $\epsilon\downarrow0$. If $C$ has no positive eigenvalues, then $S_\epsilon=S^\dagger=A$ for every $\epsilon>0$. In particular, when $C$ is nonsingular, the limit is the ordinary Schur complement $A-XC^{-1}X^\top$.
