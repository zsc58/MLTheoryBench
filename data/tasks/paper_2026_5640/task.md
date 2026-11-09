# Problem

## Setup

Let \(n\ge2\) be an integer, \(1/n<\nu<1\), and \(\eta>0\). For fixed paired observations \((x_k,x_k^*)\), let \(K\) and \(K^*\) be real-valued positive-semidefinite kernels on their respective observation spaces. Consider minimizing
\[
 F(u,v)=\frac1{\nu n}\sum_{k,m=1}^n u_ku_mK(x_k,x_m)
 +\frac1\eta\sum_{k,m=1}^n(u_k-v_k)(u_m-v_m)K^*(x_k^*,x_m^*)
\]
over real coefficient vectors satisfying
\[
 \sum_k u_k=\sum_kv_k=\nu n,\qquad u_k\ge0,\qquad 0\le v_k\le1.
\]
Define
\[
 G_k=\frac1{\nu n}\sum_m u_mK(x_k,x_m)
 +\frac1\eta\sum_m(u_m-v_m)K^*(x_k^*,x_m^*),
\]
\[
 H_k=\frac1\eta\sum_m(u_m-v_m)K^*(x_k^*,x_m^*),
\]
and, for \(i,j\),
\[
 D_{ij}=\frac{K(x_i,x_i)+K(x_j,x_j)-2K(x_i,x_j)}{\nu n},\qquad
 D^*_{ij}=\frac{K^*(x_i^*,x_i^*)+K^*(x_j^*,x_j^*)-2K^*(x_i^*,x_j^*)}{\eta}.
\]

Fix \(\tau>0\). At a feasible point, an ordinary violating pair is a pair \((i,j)\) attaining
\[
 \max_{u_i>0}G_i-\min_jG_j>\tau.
\]
Its update is
\[
 u_i\leftarrow u_i+t,\quad u_j\leftarrow u_j-t,\qquad
 t=-\min\!\left\{\frac{G_i-G_j}{D_{ij}+D^*_{ij}},u_i\right\}.
\]
An auxiliary violating pair is a pair \((i,j)\) attaining
\[
 \max_{v_i<1}H_i-\min_{v_j>0}H_j>\tau.
\]
Its update is
\[
 v_i\leftarrow v_i+s,\quad v_j\leftarrow v_j-s,\qquad
 s=\min\!\left\{\frac{H_i-H_j}{D^*_{ij}},1-v_i,v_j\right\}.
\]
All scores and step sizes are evaluated before the update. All coordinates not displayed remain unchanged.

To initialize, put \(q=\lfloor\nu n\rfloor\) and \(r=\nu n-q\). Initialize each of \(u\) and \(v\) with \(q\) entries equal to \(1\), one further entry equal to \(r\) if \(r>0\), and all remaining entries equal to \(0\). Any choices of the entry locations are allowed.

At every iteration, evaluate both displayed maximum score gaps over all indices. If neither exceeds \(\tau\), stop. Otherwise perform the update for the kind with the larger gap; if the two gaps are equal and exceed \(\tau\), either kind may be chosen. Any maximizers and minimizers attaining the selected gap may be used.

Call a feasible point \(\tau\)-approximate when neither of the two displayed maximum score gaps exceeds \(\tau\).

## Task

Prove that, for every \(\tau>0\), every allowed initialization and every sequence of allowed tie-breaking choices, this algorithm stops after finitely many iterations. Consequently, its output is a \(\tau\)-approximate solution of the stated minimization problem.
