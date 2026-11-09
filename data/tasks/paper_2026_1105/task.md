# Problem

## Setup

Fix a subregion $\sigma$ and integers $N\ge1$ and $K\ge2$. For model $n\in\{1,\ldots,N\}$, let $Y_n(\sigma)\in\{1,\ldots,K\}$ be its random class assignment and write
\[
p_n^k(\sigma)=\Pr(Y_n(\sigma)=k).
\]
Assume the random assignments $Y_1(\sigma),\ldots,Y_N(\sigma)$ are independent. For a case $t=(z_1,\ldots,z_N)\in\{1,\ldots,K\}^N$, define $N_k^t=\{n:z_n=k\}$ and
\[
C_k^t(\sigma)=\sum_{n\in N_k^t}p_n^k(\sigma).
\]
Let thresholds satisfy $0<v\le N$ and $0<r\le N$. A case is consistently classified as class $k$ when $C_k^t(\sigma)\ge v$ and $C_k^t(\sigma)-C_j^t(\sigma)\ge r$ for every $j\ne k$; otherwise it is inconsistent.

Each model has a true class $k_n^T(\sigma)$. Set $B_k(\sigma)=\{n:k_n^T(\sigma)=k\}$. For the ideal classifier define $\widetilde p_n^k(\sigma)=\mathbf 1\{k=k_n^T(\sigma)\}$ and let $t^T$ be the case with assignment $z_n=k_n^T(\sigma)$. Its ideal scores are $\widetilde C_k(\sigma)=\sum_{n\in B_k(\sigma)}\widetilde p_n^k(\sigma)=|B_k(\sigma)|$. Assume the ideal case satisfies the consistency inequalities for a unique class, denoted $k^*(\sigma)$.

Finally, for some $0\le\alpha<1$, assume every model obeys
\[
\Pr\bigl(Y_n(\sigma)=k_n^T(\sigma)\bigr)\ge (1-\alpha)^4.
\]

## Task

Prove that the probability that $\sigma$ is consistently classified correctly as $k^*(\sigma)$ satisfies
\[
\Pr\bigl(\sigma\text{ is consistently classified correctly as }k^*(\sigma)\bigr)
\ge
\sum_{t\in\mathcal A(k^*(\sigma),\sigma)}
\prod_{k=1}^K\left[
(1-\alpha)^{4|N_k^t\cap B_k(\sigma)|}
\prod_{n\in N_k^t\setminus B_k(\sigma)}p_n^k(\sigma)
\right],
\]
where $\mathcal A(k,\sigma)$ is the set of cases satisfying the actual consistency inequalities for class $k$, and empty products equal $1$.
