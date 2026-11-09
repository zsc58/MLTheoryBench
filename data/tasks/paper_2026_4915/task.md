# Problem

## Setup

A probabilistic circuit is a rooted computational tree whose leaves are univariate distributions, product nodes multiply child distributions, and sum nodes form weighted mixtures. It is decomposable when the child scopes of every product node are pairwise disjoint, and smooth when all children of a sum node have the same scope. A context-free grammar generates only such valid circuits and represents each circuit by a depth-first sequence of labeled tokens.

Fix one generated sequence of length T tokens. Let I be the positions at which the grammar makes a genuinely stochastic structural choice, and let D=|I|, with 1 <= D <= T. All positions outside I are grammar-determined. For each position t, let Z_t be its scalar reward-score contribution. Assume the Z_t are independent, each has variance sigma^2>0, has mean mu != 0 for t in I, and has mean 0 for t not in I.

Define
\[
G_{tok}=\frac1T\sum_{t=1}^T Z_t,\qquad G_{opt}=\frac1D\sum_{t\in I}Z_t,
\]
and SNR(G)=|E[G]|/sqrt(Var(G)).

## Task

Prove that
\[
\frac{SNR(G_{opt})}{SNR(G_{tok})}=\sqrt{\frac{T}{D}}.
\]
