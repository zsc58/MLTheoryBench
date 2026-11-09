# Problem

## Setup

Let \(P\) and \(Q\ne P\) be fixed probability distributions on \(\mathbb R\), and let \(n\ge1\) be an integer. Draw the reference sample \(D_0=(X_1^0,\ldots,X_n^0)\) iid from \(P\), independently of a test stream \(X_1,X_2,\ldots\) drawn iid from \(Q\). Let \(F\) be the CDF of \(P\), and define
\[
\widehat F_0(x)=\frac1n\sum_{i=1}^n\mathbf 1\{X_i^0\le x\},\qquad x\in\mathbb R.
\]
Let \(\epsilon:\mathbb R\to[0,1]\) be a measurable confidence-width function selected using only the reference data and held fixed during testing. Assume that its maximum on \([0,1]\) exists. Condition throughout on a fixed realization of the reference data and its selected width function for which
\[
|\widehat F_0(x)-F(x)|\le\epsilon(x)\qquad\text{for every }x\in\mathbb R.
\]
Put \(p_t=\widehat F_0(X_t)\), let \(\mathcal F_t=\sigma(p_1,\ldots,p_t)\) in this conditional experiment, and let \(\mathcal F_0\) be the trivial sigma-field.

For each smoothing parameter \(k>0\), define
\[
C_k=\left(\tfrac12+\sqrt{1+k^2}\max_{p\in[0,1]}\epsilon(p)\right)^{-1},
\qquad
b_{t,k}(u)=1+C_k\left[u(p_t-\tfrac12)-\sqrt{u^2+k^2}\,\epsilon(p_t)\right],
\quad u\in I:=[-\tfrac12,\tfrac12].
\]
Use the following one-dimensional online Newton step recursion for the losses \(\ell_{t,k}(u)=-\log b_{t,k}(u)\). Initialize \(\eta_1=0\) and \(a_0=1\). After observing \(p_t\), set
\[
z_t=-\ell_{t,k}'(\eta_t)=\frac{b_{t,k}'(\eta_t)}{b_{t,k}(\eta_t)},\qquad
a_t=a_{t-1}+z_t^2,\qquad
\eta_{t+1}=\Pi_I\left(\eta_t+\frac{4z_t}{a_t}\right),
\]
where the derivatives are with respect to \(u\), and \(\Pi_I(v)=\max(-\tfrac12,\min(v,\tfrac12))\). The parameter \(\eta_t\) is thus chosen before observing \(p_t\). For each \(k\), define
\[
S_{0,k}=1,\qquad S_{t,k}=S_{t-1,k}b_{t,k}(\eta_t),\qquad
\tau_k=\inf\{t\ge1:S_{t,k}\ge1/\alpha\},\quad \alpha\in(0,1),
\]
with \(\inf\varnothing=\infty\). The recursion is run separately for each \(k\).

Define the conditional effective signal margins
\[
\Delta_k=\left|\mathbb E_Q[p_t-\tfrac12\mid D_0]\right|-\sqrt{1+k^2}\,\mathbb E_Q[\epsilon(p_t)\mid D_0],
\qquad
\Delta_0=\left|\mathbb E_Q[p_t-\tfrac12\mid D_0]\right|-\mathbb E_Q[\epsilon(p_t)\mid D_0].
\]
Assume \(\Delta_k>0\) for all sufficiently small positive \(k\).

## Task

Prove that there is a universal numerical constant \(K<\infty\) such that, for each conditional setup satisfying these assumptions and each \(\alpha\in(0,1)\), there exists \(k_0>0\) for which every \(0<k<k_0\) satisfies
\[
Q(\tau_k<\infty\mid D_0)=1
\]
and
\[
\mathbb E_Q[\tau_k\mid D_0]
\le K\left(\Delta_0^{-2}\log\frac1{\alpha\Delta_0}+\Delta_0^{-2}\right).
\]
Thus the expected detection-time bound has the stated universal big-O order in the regime \(k\downarrow0\).
