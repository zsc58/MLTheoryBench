# Problem

## Setup

Let \(n\geq1\) be an integer, let \((\mathcal Z,\Sigma,\mu)\) be a probability space, and let \((\mathcal W,d)\) be a nonempty separable metric space equipped with its Borel sigma-algebra. Let \(S=(Z_1,\ldots,Z_n)\sim\mu^{\otimes n}\). A possibly randomized learner is specified by a Markov kernel \(P_{W\mid S}\), with joint law
\[
P_{S,W}(ds,dw)=\mu^{\otimes n}(ds)P_{W\mid S}(dw\mid s).
\]

Let \(\ell:\mathcal W\times\mathcal Z\to[0,\infty)\) be jointly measurable, with \(\int\ell(w,z)\,\mu(dz)<\infty\) for every \(w\). Define
\[
\bar\ell(w,z)=\int\ell(w,z')\,\mu(dz')-\ell(w,z),
\qquad
G(w,S)=\frac1n\sum_{i=1}^n\bar\ell(w,Z_i).
\]

Fix \(0<\theta\leq2\). Assume the centered-loss process is separable in the following simultaneous sense: there is a countable dense set \(\mathcal W_*\subseteq\mathcal W\) such that, for \(\mu\)-almost every \(z\), every \(w\in\mathcal W\) admits a sequence \(v_j\in\mathcal W_*\) with
\[
d(v_j,w)\longrightarrow0,
\qquad \bar\ell(v_j,z)\longrightarrow\bar\ell(w,z).
\]
Assume also that, for all distinct \(s,t\in\mathcal W\),
\[
\mathbb E_{Z\sim\mu}\exp\left(
\frac{|\bar\ell(t,Z)-\bar\ell(s,Z)|^\theta}{d(t,s)^\theta}
\right)\leq2.
\]

For \(\varepsilon>0\), let \(N(\mathcal W,d,\varepsilon)\) be the minimum number of closed \(d\)-balls of radius \(\varepsilon\), with centers in \(\mathcal W\), needed to cover \(\mathcal W\), and set it to \(+\infty\) if no finite cover exists. Assume
\[
J:=\int_0^\infty[\log N(\mathcal W,d,\varepsilon)]^{1/\theta}\,d\varepsilon<\infty.
\]
Define the minimum covering radius
\[
e:=\inf\{\varepsilon>0:N(\mathcal W,d,\varepsilon)=1\}.
\]

For a convex function \(f:[0,\infty)\to\mathbb R\), use the unnormalized convention
\[
D_f(P\|Q)=\int f\!\left(\frac{dP}{dQ}\right)dQ
\quad\text{if }P\ll Q,
\qquad D_f(P\|Q)=+\infty\quad\text{otherwise}.
\]
Fix a finite real number
\[
A\geq A_\theta:=\max\left\{1,
2^{\lceil2/\theta\rceil-2}(\lceil2/\theta\rceil)!,
2\exp(\lfloor2/\theta\rfloor)\right\}.
\]
Set
\[
f_\theta(x)=x[\log(x+A)]^{1/\theta}\quad(x\geq0),
\qquad
I_{f_\theta}(U;S)=D_{f_\theta}(P_{U,S}\|P_U\otimes P_S).
\]
In particular, \(f_\theta(0)=0\); no subtraction of \(f_\theta(1)\) is made.

Let \((\mathcal P_k)_{k\geq0}\) be fixed finite Borel partitions of \(\mathcal W\), with nonempty cells, increasing in the sense that each cell of \(\mathcal P_k\) is contained in a cell of \(\mathcal P_{k-1}\) for \(k\geq1\). For every cell \(C\in\mathcal P_k\), let \(t_C\in\mathcal W\) be a fixed representative satisfying
\[
C\subseteq\{w:d(w,t_C)\leq e2^{-k}\}.
\]
Whenever \(C\in\mathcal P_k\) is contained in \(B\in\mathcal P_{k-1}\), assume \(t_C\in B\). The partitions and representatives do not depend on the realized sample or the learner's randomization. Write \([W]_k\) for the cell of \(\mathcal P_k\) containing \(W\).

## Task

Prove that there exists a finite constant \(M_\theta>0\), depending only on \(\theta\), such that for every setup above,
\[
\mathbb E G(W,S)\leq
\frac{eM_\theta}{\sqrt n}
\sum_{k=1}^\infty2^{-(k-1)}
\left(2^{1/\theta}I_{f_\theta}([W]_k;S)+4\right).
\]
The series is allowed to equal \(+\infty\). Include the case \(e=0\).

In particular, the right-hand side is finite whenever
\[
\sum_{k=1}^\infty2^{-(k-1)}I_{f_\theta}([W]_k;S)<\infty.
\]
This conclusion also applies to deterministic learners, without requiring finite ordinary mutual information \(I(W;S):=D_{x\mapsto x\log x}(P_{W,S}\|P_W\otimes P_S)\), where \(0\log0=0\).
