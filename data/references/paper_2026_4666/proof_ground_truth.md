# Reference Proof

All probabilities and expectations below are conditional on the fixed reference realization. The width function is consequently fixed. The test observations remain iid from Q. We prove the fixed-benchmark growth, the ONS regret inequality, the wealth comparison, a variance-sensitive concentration bound uniform over sufficiently small positive k, and the stopping-time estimate.

## 1. A feasible benchmark with quantitative growth and variance bounds

Write
\[
Y_t=p_t-\tfrac12,\quad e_t=\epsilon(p_t),\quad e_*=\max_{p\in[0,1]}\epsilon(p),\quad
\mu=\mathbb E Y_t,\quad m=\mathbb E e_t,\quad d=\Delta_0=|\mu|-m.
\]
The pairs \((Y_t,e_t)\) are iid, with \(|Y_t|\le1/2\) and \(0\le e_t\le1\). Since \(\Delta_k\le d\), the assumption implies \(0<d\le1/2\); in particular \(\mu\ne0\). Set \(\sigma=\operatorname{sign}(\mu)\) and
\[
H_t=\sigma Y_t-e_t,\qquad V=\operatorname{Var}(H_t).
\]
Then \(\mathbb E H_t=d\), and \(H_t\in[-3/2,1/2]\), so \(V\le1\). For example, \(V\le\mathbb E(H_t+1/2)^2\le1\).

For benchmark analysis only, extend the factor continuously to k=0. Let
\[
C_0=(1/2+e_*)^{-1},\qquad
\theta=\frac{d}{2(1+d^2)},\qquad
\nu=\sigma\frac{\theta}{C_0},\qquad
q=\frac{d^2}{4(1+d^2)}.
\]
Thus \(b_{t,0}(u)=1+C_0[uY_t-|u|e_t]\). Since \(C_0\ge2/3\) and \(\theta\le1/4\), we have \(|\nu|\le3/8<1/2\). Thus this is a feasible benchmark, not an unconstrained quadratic optimizer. With \(g_{t,k}(u)=b_{t,k}(u)-1\), also at k=0,
\[
g_{t,0}(\nu)=\theta H_t.
\]
For every \(u\in I\), \(|g_{t,0}(u)|\le C_0|u|(1/2+e_*)\le1/2\). Therefore \(\log(1+x)\ge x-x^2\) on \([-1/2,1/2]\) gives, for \(L_{t,0}=\log b_{t,0}(\nu)\),
\[
\mathbb E L_{t,0}
\ge\theta d-\theta^2(V+d^2)
\ge\theta d-\theta^2(1+d^2)=q.
\]
Furthermore,
\[
\operatorname{Var}(g_{t,0}(\nu))=\theta^2V\le q,
\qquad
\operatorname{Var}(L_{t,0})\le4q.
\]
The second inequality follows because \(x\mapsto\log(1+x)\) is 2-Lipschitz on this interval: apply the independent-copy identity for variance to the Lipschitz bound. Notice that a lower bound for the mean is sufficient; the mean is not asserted to equal its quadratic lower bound. Also,
\[
\frac{d^2}{5}\le q\le\frac1{20}.
\]

## 2. The exact ONS recursion has logarithmic regret

We verify this directly, rather than relying on the source's incorrect assertion that every smoothed factor is at least 1/2. Fix k>0 throughout this section. For \(u\in I\) and integer \(T\ge1\), define the cumulative regret
\[
R_T(u)=\sum_{t=1}^T\bigl[\ell_{t,k}(\eta_t)-\ell_{t,k}(u)\bigr],
\]
suppressing its dependence on the fixed k in the notation.

Fix one observation and write \(y=p-1/2\), \(e=\epsilon(p)\), \(s=\sqrt{1+k^2}\), \(A=1/2+s e_*\). For \(u\in I\), put \(v=|u|\), \(r=\sqrt{u^2+k^2}\). The factor is
\[
b_k(u)=\frac{A+uy-re}{A}.
\]
Its numerator satisfies
\[
A+uy-re\ge\tfrac12(1-v)+(s-r)e\ge\tfrac14>0.
\]
Thus the logarithmic losses are well-defined for every positive k. Also \(b_k''(u)=-C_k e k^2/(u^2+k^2)^{3/2}\le0\), so the factor is concave and the loss is 1-exp-concave.

For the logarithmic derivative,
\[
\left|\frac{b_k'(u)}{b_k(u)}\right|
\le\frac{1/2+(v/r)e}{(1-v)/2+(s-r)e}\le2.
\]
To verify the last inequality, note that \(r\ge vs\), whence
\[
r(s-r)=\frac{(1-v^2)r}{s+r}\ge v(1-v)\ge v/2.
\]
Consequently \(2(s-r)-v/r\ge0\), and twice the denominator minus the numerator in the preceding fraction is
\(1/2-v+[2(s-r)-v/r]e\ge0\).

For completeness, the relevant ONS argument is elementary. Fix any comparator \(u\in I\). Concavity of \(b_{t,k}\) gives
\[
\frac{b_{t,k}(u)}{b_{t,k}(\eta_t)}\le1+z_t(u-\eta_t).
\]
The right side is positive and \(z_t(u-\eta_t)\le2\). The inequality
\(\log(1+x)\le x-x^2/8\) for \(-1<x\le2\) therefore yields
\[
\ell_{t,k}(\eta_t)-\ell_{t,k}(u)
\le z_t(u-\eta_t)-\tfrac18z_t^2(u-\eta_t)^2.
\]
This logarithm inequality follows by differentiating \(x-x^2/8-\log(1+x)\), whose derivative is \(x(3-x)/(4(1+x))\).

Projection onto the interval cannot increase distance to u. Using the specified update with coefficient 4 gives
\[
z_t(u-\eta_t)
\le\frac{a_t}{8}\big((\eta_t-u)^2-(\eta_{t+1}-u)^2\big)+\frac{2z_t^2}{a_t}.
\]
Combining the last two displays and using \(a_t-a_{t-1}=z_t^2\) telescopes to
\[
R_T(u)\le\frac{a_0}{8}(\eta_1-u)^2+2\sum_{t=1}^T\frac{z_t^2}{a_t}
\le\frac1{32}+2\log a_T
\le\frac12+2\log(1+4T).
\]
Here \((a_t-a_{t-1})/a_t\le\log(a_t/a_{t-1})\), \(a_0=1\), and \(|z_t|\le2\). This closes the regret obligation for the actual algorithm, with no unproved specialized dependency.

## 3. Adaptive-versus-fixed wealth

Expanding the products gives the exact identity
\[
\log S_{T,k}=\sum_{t=1}^T\log b_{t,k}(u)-R_T(u).
\]
In particular, for the fixed comparator \(\nu\) from Section 1,
\[
\log S_{T,k}\ge\sum_{t=1}^T L_{t,k}-r(T),\qquad
L_{t,k}=\log b_{t,k}(\nu),\quad r(T)=2\log(1+4T)+1/2.
\]
The comparator depends on the fixed conditional distribution, not on the test observations. It is used only in the proof; the algorithm receives no knowledge of Q.

## 4. Uniform small-k transfer and Bernstein concentration

For \(0<k\le1\),
\[
0\le C_0-C_k\le2k^2,\qquad
0\le\sqrt{u^2+k^2}-|u|\le k.
\]
Since \(|uY_t-|u|e_t|\le3/4\) on I and \(C_k\le2\), these imply the deterministic uniform estimate
\[
|g_{t,k}(u)-g_{t,0}(u)|\le\tfrac32k^2+2k\le4k.
\]
For \(k\le1/16\), both factors in this comparison are at least 1/4, and hence
\[
|\log b_{t,k}(u)-\log b_{t,0}(u)|\le16k.
\]
Take \(0<k\le q/64\), which also ensures \(k\le1/16\). Then
\[
|L_{t,k}-L_{t,0}|\le q/4,
\qquad w_k:=\mathbb E L_{t,k}\ge3q/4\ge q/2.
\]
Thus a positive fixed-benchmark log gain holds for every sufficiently small positive k. Moreover,
\[
\operatorname{Var}(L_{t,k})
\le2\operatorname{Var}(L_{t,0})+2\operatorname{Var}(L_{t,k}-L_{t,0})
\le8q+q^2/8\le9q.
\]
The range of \(L_{t,k}\) has length at most \(\log3+q/2<2\), so \(|L_{t,k}-w_k|\le2\).

The standard independent Bernstein inequality used here states that independent centered variables with absolute bound B and total variance at most Tv satisfy
\[
\Pr\!\left(\sum_{t=1}^T Z_t\le-Tx\right)
\le\exp\!\left(-\frac{Tx^2}{2v+(2/3)Bx}\right),\qquad x>0.
\]
All its hypotheses hold conditionally: the benchmark is fixed, the observations are iid, \(B=2\), and \(v=9q\). Taking \(x=q/4\) and using \(w_k\ge q/2\) gives
\[
\Pr\!\left(\sum_{t=1}^T L_{t,k}<Tq/4\right)
\le\exp\!\left(-\frac{T(q/4)^2}{18q+q/3}\right)
\le e^{-Tq/400}.
\]
The exponent is of order Tq, not merely Tq squared. This distinction is essential for the expected stopping-time rate.

## 5. Threshold domination, stopping, and expectation

Let
\[
A_\alpha=\log(1/\alpha),\qquad H=A_\alpha+\log(1/q)+1,\qquad
T_0=\left\lceil\frac{128H}{q}\right\rceil.
\]
Then, for all \(T\ge T_0\),
\[
Tq/4\ge A_\alpha+2\log(1+4T)+1/2.
\]
Indeed, at \(T_0\) use \(1+4T_0\le517H/q\), \(\log H\le H\), and \(H\ge1\); the right side is less than \(32H\le T_0q/4\). Thereafter the difference is nondecreasing because its derivative is \(q/4-8/(1+4T)\ge0\) when \(T\ge8/q\).

By the wealth comparison, for \(T\ge T_0\),
\[
\Pr(\tau_k>T)\le\Pr(S_{T,k}<1/\alpha)\le e^{-Tq/400}.
\]
Only the inclusion \(\{\tau_k>T\}\subseteq\{S_{T,k}<1/\alpha\}\) is used: a wealth process may fall below the threshold after an earlier crossing.

The correct integer-valued tail-sum identity starts at zero. Therefore
\[
\mathbb E\tau_k=\sum_{T=0}^{\infty}\Pr(\tau_k>T)
\le T_0+\sum_{T=T_0}^{\infty}e^{-Tq/400}
\le T_0+1+400/q<\infty.
\]
The last inequality uses \((1-e^{-x})^{-1}\le1+1/x\) for \(x>0\). In particular \(\Pr(\tau_k<\infty)=1\). Finally, \(q\ge d^2/5\) and \(\log(1/q)\le\log5+2\log(1/d)\) imply
\[
\mathbb E\tau_k
=O\!\left(d^{-2}\log\frac1{\alpha d}+d^{-2}\right)
\]
with a universal constant, simultaneously for every sufficiently small positive k in this fixed conditional experiment. No exchange of a k-limit with a stopping-time expectation is needed.

The proof covers either sign of the signal, zero benchmark variance, zero confidence width, and the entire stated range of α. The excluded case d=0 is incompatible with the assumed positive effective margin. The confidence-band event is retained from the task's source setup, but the power argument itself does not require a probability-integral-transform or continuity assumption.
