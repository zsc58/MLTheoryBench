# Problem

## Setup

Let $T,d,r$ be positive integers, let $\mathcal V$ be a vocabulary, and fix tokens $x_1,\ldots,x_T\in\mathcal V$. Each token $w\in\mathcal V$ has a fixed embedding $e_w\in\mathbb R^d$.

Choose a positive integer $C$, indices $1\le t^*<n\le T-1$ with $C\mid(n-1)$, and tokens $k^*,v^*\in\mathcal V$ such that
\[
x_{t^*}=k^*,\qquad x_{t^*+1}=v^*,\qquad x_n=k^*,\qquad x_{n+1}=v^*,\qquad k^*\ne v^*.
\]

Fix matrices $W_{\rm gate},W_{\rm up}\in\mathbb R^{r\times d}$ and an initial matrix $W^{(0)}\in\mathbb R^{d\times r}$. Let $\phi:\mathbb R\to\mathbb R$ be a measurable activation function. On a probability space $(\Omega,\mathcal F,\mathbb P)$, let $H$ be a measurable random matrix in $\mathbb R^{n\times d}$, and define the intermediate activation matrix
\[
Z=\phi(HW_{\rm gate}^T)\odot(HW_{\rm up}^T)\in\mathbb R^{n\times r},
\]
where $\phi$ acts elementwise and $\odot$ denotes elementwise multiplication. Write its rows as $z_t^T$, $1\le t\le n$. The gated MLP output with matrix $W\in\mathbb R^{d\times r}$ is $ZW^T$. Only $W$ is adapted; the two input-projection matrices remain fixed.

Compare two separate runs from $W^{(0)}$. For $1\le t<n$, the target vectors are
\[
v_t=e_{x_{t+1}}\quad\text{in the LM-aligned run},
\qquad
v_t=e_{x_t}\quad\text{in the reconstruction run}.
\]

Put $m=(n-1)/C$, and partition the prior positions into the consecutive chunks
\[
I_i=\{iC+1,\ldots,(i+1)C\},\qquad i=0,\ldots,m-1.
\]
For each chunk, let $Z_{[i]}$ and $V_{[i]}$ have rows $z_t^T$ and $v_t^T$, respectively, for $t\in I_i$ in increasing order. In each run, process the chunks in order. First evaluate a chunk using the current matrix $W$, giving $Z_{[i]}W^T$, and then take one gradient descent step with learning rate $\lambda>0$ on
\[
L(Z_{[i]}W^T,V_{[i]})=-\langle Z_{[i]}W^T,V_{[i]}\rangle_F.
\]
The gradient is with respect to $W$, with the realized activations and target vectors held fixed as inputs. Evaluate the query position only after all these chunks and their updates have been completed.

In each run, let $\Delta W$ denote the accumulated change from $W^{(0)}$ before evaluating the query, and define
\[
\Delta\ell_n[w]=e_w^T\Delta W z_n.
\]
The symbols $v_t$, $\Delta W$, and $\Delta\ell_n$ refer to the target choice of the run under discussion. All expectations below are with respect to $\mathbb P$ over the representations; the token sequence and embeddings are fixed.

Assume
\[
\mathbb E\bigl[|z_t^Tz_n|\bigr]<\infty\qquad(1\le t<n).
\]
Let $\epsilon>0$, $c_{\rm norm}>0$, and $c_{\rm align}>0$ be constants such that
\[
|e_{w_1}^Te_{w_2}|\le\epsilon\quad(w_1,w_2\in\mathcal V,\ w_1\ne w_2),
\qquad
\|e_w\|^2\ge c_{\rm norm}^2\quad(w\in\mathcal V).
\]
Assume also
\[
\mathbb E[z_{t^*}^Tz_n]=c_{\rm align}.
\]
For each of the two target choices, assume that every other prior position satisfies
\[
\mathbb E[(v_tz_t^T)z_n]=0\in\mathbb R^d
\qquad(1\le t<n,\ t\ne t^*).
\]

## Task

Prove that in the LM-aligned run,
\[
\mathbb E[\Delta\ell_n[v^*]]\ge\lambda c_{\rm norm}^2c_{\rm align},
\qquad
|\mathbb E[\Delta\ell_n[w]]|\le\lambda\epsilon c_{\rm align}
\quad\text{for every }w\in\mathcal V\setminus\{v^*\},
\]
whereas in the reconstruction run,
\[
|\mathbb E[\Delta\ell_n[v^*]]|\le\lambda\epsilon c_{\rm align}.
\]
