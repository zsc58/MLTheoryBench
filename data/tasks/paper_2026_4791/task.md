# Problem

## Setup

Let \(n\geq1\) be an integer, let \(\mathcal X\) be a covariate space, and let \(\mathcal H\) be a nonempty class of functions \(h:\mathcal X\to\mathbb R\). Fix an arbitrary labeled sequence \(S=((x_i,y_i))_{i=1}^n\), where \(x_i\in\mathcal X\) and \(y_i\in\mathbb R\). Fix a finite real number \(\Delta>0\) and a loss \(\ell:\mathbb R\times\mathbb R\to[0,\Delta]\). Assume the empirical minima displayed below are attained.

For each held-out index \(i\), the learner observes all covariates and the labels \(y_j\) with \(j\ne i\), but not \(y_i\). The hypothesis class, loss, tolerance grid, and aggregation rule are prescribed without using the response vector; they may depend on the full covariate sequence. Any measure used to implement the aggregation rule obeys the same information restriction.

Let \(S_{-i}\) denote the labeled sequence with its \(i\)-th entry removed. Define
\[
L_S(h)=\sum_{i=1}^n\ell(h(x_i),y_i),\qquad
L_{S_{-i}}(h)=\sum_{j\ne i}\ell(h(x_j),y_j),
\]
and
\[
\operatorname{LOO}_S(A)=\frac1n\sum_{i=1}^n\ell(A(S_{-i},x_i),y_i),
\]
where the notation for \(A\) suppresses its access to the full covariate sequence.

Equip \(\mathcal H\) with a sigma-algebra \(\mathscr F\) and a measure \(\mu\). Assume \(h\mapsto\ell(h(x),y)\) is measurable for every \((x,y)\in\mathcal X\times\mathbb R\). Let \(\operatorname{Agg}\) map every \(G\in\mathscr F\) with \(0<\mu(G)<\infty\) and every covariate \(x\) to a real prediction.

For \(t\geq0\), set
\[
H_t=\{h\in\mathcal H:L_S(h)\leq\min_{g\in\mathcal H}L_S(g)+t\},
\qquad
H_{t,i}=\{h\in\mathcal H:L_{S_{-i}}(h)\leq\min_{g\in\mathcal H}L_{S_{-i}}(g)+t\},
\]
and set \(H_s=\varnothing\) for \(s<0\).

Let \(T\subset[0,\infty)\) be a finite nonempty tolerance grid and let \(t_{\max}=\max T\). Assume \(0<\mu(H_{t,i})<\infty\) for every \(t\in T\) and every \(i\). Define
\[
\widehat y_{t,i}=\operatorname{Agg}(H_{t,i},x_i),\qquad
\widehat y_i=\operatorname{med}_{t\in T}\widehat y_{t,i},
\]
where \(\operatorname{med}\) is the smallest median: for \(m=|T|\), it is the order statistic of rank \(\lceil m/2\rceil\), with repetitions counted. Let \(\mathrm{MLSA}\) denote this transductive leave-one-out procedure.

Assume:

1. **Aggregation stability.** There is a finite constant \(c>0\) such that for every \(G\in\mathscr F\) with \(0<\mu(G)<\infty\) and every \((x,y)\in\mathcal X\times\mathbb R\),
\[
\ell(\operatorname{Agg}(G,x),y)\leq\frac{c}{\mu(G)}\int_G\ell(h(x),y)\,\mu(dh).
\]
2. **Local level-set growth.** Fix a finite constant \(C_g\geq1\). A tolerance \(t\in T\) is good when \(0<\mu(H_{t-\Delta})<\infty\), \(\mu(H_{t+\Delta})<\infty\), and
\[
H_{t-\Delta}\subseteq H_{t,i}\subseteq H_{t+\Delta}\quad\text{for every }i,
\qquad
\frac{\mu(H_{t+\Delta})}{\mu(H_{t-\Delta})}\leq C_g.
\]
3. **Strict-majority grid condition.** For some \(\rho>1/2\), at least \(\rho|T|\) tolerances in \(T\) are good.
4. **Monotone loss.** Either, for all \(a,b,y\in\mathbb R\),
\[
|b-y|\geq|a-y|\quad\Longrightarrow\quad\ell(b,y)\geq\ell(a,y),
\]
or, for each fixed \(y\in\mathbb R\), the function \(a\mapsto\ell(a,y)\) is monotone in a known direction, nondecreasing or nonincreasing. In the latter alternative, the direction may depend on \(y\).

## Task

Prove the deterministic theorem
\[
\operatorname{LOO}_S(\mathrm{MLSA})
\leq
\frac{2cC_g}{(2\rho-1)n}
\left(\min_{h\in\mathcal H}L_S(h)+t_{\max}+\Delta\right).
\]
