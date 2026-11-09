# Problem

## Setup

Let V be a finite alphabet with at least two symbols, let m be a mask symbol not in V, let d be a positive integer, and let ε be a finite nonnegative real number. Write [d]={1,...,d}. The data distribution q_0 is any probability law on V^d. Conditional on the initial data, each coordinate evolves independently under the absorbing masking continuous-time Markov chain with rate 1 from every v∈V to m and no transitions out of m. Write α_t=e^{-t} and let q_t be the resulting law on (V∪{m})^d at forward time t≥0.

For a masked set M⊆[d], write M^c=[d]\M and let x^{M^c} denote the visible coordinates together with their indices. For i∈M, let q_i(·|x^{M^c}) be the conditional law of the original token X_i under q_0, with an arbitrary choice on null contexts. A predictor supplies probability distributions μ_i(·|x^{M^c},t) on V for every such context, every i∈M, and every t>0. Each probability μ_i(a|x^{M^c},t) is a Borel-measurable function of t.

For a state y∈(V∪{m})^d, let M(y)={i:y_i=m}, and write y^{i←a} for y with coordinate i replaced by a. For t>0, q_t(y)>0, i∈M(y), and a∈V, define
\[
r_t(y,i,a)=\frac{q_t(y^{i\leftarrow a})}{q_t(y)},
\qquad
z_t(y,i,a)=\frac{e^{-t}}{1-e^{-t}}\,
\mu_i(a\mid y^{M(y)^c},t).
\]
For nonnegative r,z, define
\[
\Phi(r,z)=z-r+r\log\frac rz
\]
when r,z>0, with Φ(0,z)=z for z≥0 and Φ(r,0)=+∞ for r>0. All logarithms are natural.

Define the integrated score-entropy error by
\[
\mathcal E(\mu)=\int_0^\infty
\sum_{y:q_t(y)>0}q_t(y)
\sum_{i\in M(y)}\sum_{a\in V}
\Phi\bigl(r_t(y,i,a),z_t(y,i,a)\bigr)\,dt.
\]
Empty sums are zero. Assume that \(\mathcal E(\mu)\le\varepsilon\).

The First-Hitting Sampler (FHS) starts at the all-mask state with reverse clock t=∞. When k≥1 coordinates remain masked, it samples a new time τ according to the following conditional law given the complete sampling history:
\[
\Pr(\tau<s\mid\text{history})
=\left(\frac{1-e^{-s}}{1-e^{-t}}\right)^k,
\qquad 0<s<t,
\]
where t is the current clock value and the denominator is interpreted as 1 when t=∞. Conditional on the history and τ, it chooses one of the k masked coordinates uniformly. If the chosen coordinate is i and the current visible context is x^{M^c}, it samples its value from μ_i(·|x^{M^c},τ), replaces that mask by the sampled value, and sets the clock to τ. It repeats until no masks remain. Denote its output law by P_FHS.

For probability laws p,r on a finite set, use
\[
\mathrm{KL}(p\|r)=\sum_{a:p(a)>0}p(a)\log\frac{p(a)}{r(a)},
\]
with value +∞ if r(a)=0 for some a with p(a)>0.

## Task

Prove that FHS performs exactly d unmasking events almost surely and that its output satisfies
\[
\mathrm{KL}(q_0\|P_{\mathrm{FHS}})
\le \mathcal E(\mu)\le\varepsilon.
\]
Moreover, prove sharpness: for every fixed alphabet V and dimension d allowed above and every finite ε≥0, there exist a data law q_0 and predictor μ on that alphabet and dimension such that
\[
\mathcal E(\mu)=\varepsilon
\quad\text{and}\quad
\mathrm{KL}(q_0\|P_{\mathrm{FHS}})=\varepsilon.
\]
