# Problem

## Setup

Let \(T\) be a decoder-only Transformer trained on the binary copying task, with compact position embeddings. Its vocabulary is \(V=\{0,1,\mathtt{|}\}\), where \(\mathtt{|}\) is a separator. For a finite prompt \(x\in V^*\), write \(p_T(r\mid x)\) for the probability assigned to \(r\in V\). These are probabilities on \(V\), not probabilities renormalized over the two bits.

For a nonempty input bitstring \(b=(b_1,\ldots,b_n)\), start generation from the prompt \(b\mathtt{|}\) and generate exactly \(n\) bits by greedy selection over \(\{0,1\}\), resolving ties by a fixed rule. Denote those bits by \(o_{b,1},\ldots,o_{b,n}\), and define
\[
q_{b,k}(r)=p_T(r\mid b\mathtt{|}o_{b,1}\cdots o_{b,k-1}),\qquad r\in\{0,1\}.
\]
Define
\[
\operatorname{ppl}_T(b):=-\frac1n\sum_{k=1}^n\log q_{b,k}(b_k).
\]
Assume that there is \(\lambda>0\) such that \(p_T(r\mid x)\ge\lambda\) for every finite prompt \(x\in V^*\) and every \(r\in V\).

Assume the following compact-position-embedding continuity property. For every \(\eta>0\), there is \(\delta>0\) such that, for every \(n\ge1\), every pair \(b,b'\in\{0,1\}^n\) with \(b_n=b'_n\) and
\[
\frac1n\bigl|\{i:b_i\ne b'_i\}\bigr|<\delta,
\]
and every common finite binary history \(h\in\{0,1\}^*\),
\[
\max_{r\in\{0,1\}}
\left|p_T(r\mid b\mathtt{|}h)-p_T(r\mid b'\mathtt{|}h)\right|\le\eta.
\]

Let \(a=a_1a_2\cdots\) be an infinite bitstring. Fix \(0\le g<1/2\) and assume that for every \(N\ge1\) and every \(1\le k\le N\),
\[
q_{a_N,k}(a_k)\ge1-g,
\]
where \(a_N=(a_1,\ldots,a_N)\).

## Task

Prove that for every \(\varepsilon>0\) there exists \(N_0\) such that, for every \(N\ge N_0\), there is a length-\(N\) bitstring \(c_N\) that is not correctly copied by \(T\) (its greedy output is not \(c_N\)) and satisfies
\[
\operatorname{ppl}_T(c_N)<-\log(1-g)+\varepsilon.
\]
