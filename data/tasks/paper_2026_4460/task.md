# Problem

## Setup

Let X be a measurable instance space. Let G be a family of groups represented by indicators g:X->{0,1}, identifying g with the set {x:g(x)=1}, and let H be a class of hypotheses h:X->{-1,1}. All functions below are assumed measurable, as are events obtained by existential or universal quantification over the indicated function classes in finite-sample statements.

Define
\[
C_{G,H}=\{c:X\to\{-1,1\}:\text{for every }g\in G\text{ there is }h_g\in H\text{ with }c(x)=h_g(x)\text{ for all }x\in g\}.
\]
Fix a probability distribution P on X and a target c* in C_{G,H}. Labels are y=c*(x) for x sampled from P. Write P(g)=P({x:g(x)=1}). For P(g)>0 define
\[
\operatorname{err}_g(f)=\Pr_{x\sim P}[f(x)\ne c^*(x)\mid x\in g].
\]

For a binary class F on a domain Z and a nonnegative integer m, define its growth function by
\[
S_Z(F,m)=\sup_{\substack{A\subseteq Z\\ |A|\le m}}\bigl|\{f|_A:f\in F\}\bigr|.
\]
A finite set A is shattered by F if every binary labeling of A is realized by a member of F. Let VC(F) be the supremum of the cardinalities of finite sets shattered by F, allowing the value infinity and setting VC(F)=0 for an empty class. Write
\[
H|_g=\{h|_g:h\in H\},\qquad
d_{g,H}=\operatorname{VC}(H|_g),\qquad
d_G=\operatorname{VC}(G),\qquad
d_H^{\mathrm{sup}}=\sup_{g\in G}d_{g,H},
\]
with d_H^sup=0 when G is empty. Use natural logarithms and, for d in {0,1,2,...} union {infinity}, the convention
\[
\binom{m}{\le d}=\sum_{j=0}^{\min(d,m)}\binom mj,
\]
so this equals 2^m when d>=m, including d=infinity.

Fix a positive integer n and a confidence parameter delta in (0,1). Draw S=(x_i,c*(x_i))_{i=1}^n with x_1,...,x_n iid from P. Call c in C_{G,H} consistent if c(x_i)=c*(x_i) for every i.

## Task

Prove the following integrated theorem.

(a) For every fixed g in G, with probability at least 1-delta over S, every c in C_{G,H} consistent with S obeys
\[
\Pr_{x\sim P}[c(x)\ne c^*(x),\ x\in g]\le {4\over n}\left(\log\binom{2n}{\le d_{g,H}}+\log{4\over\delta}\right).
\]

(b) With probability at least 1-delta over S, simultaneously for all g in G, every consistent c in C_{G,H} obeys
\[
\Pr_{x\sim P}[c(x)\ne c^*(x),\ x\in g]\le {4\over n}\left(\log\binom{2n}{\le d_G}+\log\binom{2n}{\le d_H^{\mathrm{sup}}}+\log{4\over\delta}\right).
\]
For each g with P(g)>0, dividing the corresponding joint bound by P(g) yields the conditional error bound for err_g(c).
