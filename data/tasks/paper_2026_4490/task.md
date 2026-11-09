# Problem

## Setup

A question has an intrinsic difficulty parameter \(p\in[0,1]\), drawn independently from a fixed distribution \(P\) for each newly encountered question. Conditional on \(p\), attempts are independent and each succeeds with probability \(p\). Assume \(P(p>0)>0\). Define
\[
F(k)=1-\mathbb E_{p\sim P}[(1-p)^k],\qquad k=0,1,2,\ldots.
\]

Fix an integer reset interval \(\tau\ge1\). A question is attempted until it succeeds or until \(\tau\) consecutive failures have occurred. On \(\tau\) failures it is discarded and a fresh question, with an independent draw from \(P\), is attempted. Let \(T_\tau\) be the total number of attempts until a question is solved.

## Task

Prove that for every admissible difficulty distribution \(P\),
\[
\mathbb E[T_1]\le \mathbb E[T_2]\le\mathbb E[T_3]\le\cdots.
\]
In particular, resetting after every attempt (\(\tau=1\)) minimizes the expected number of attempts per solved question among all deterministic reset intervals.
