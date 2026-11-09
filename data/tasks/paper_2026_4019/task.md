# Problem

## Setup

Let \(D\subseteq\mathbb R^m\) be an open parameter domain, and let \(E:\mathbb R^N\times D\to\mathbb R\) be smooth and convex in its first argument. Fix matrices \(A\in\mathbb R^{N\times p}\) and \(B\in\mathbb R^{N\times q}\), and vectors \(a\in\mathbb R^p\) and \(b\in\mathbb R^q\). Assume the input and output involve disjoint state coordinates: for every row index, at least one of the corresponding rows of \(A\) and \(B\) is zero.

For every \(\theta\in D\), assume that \(E(\cdot;\theta)\) is strictly convex on the nonempty affine set \(\{z:A^Tz=a\}\) and attains its minimum there. Let \(z_0=z_0(\theta)\) denote its unique minimizer, and put \(\delta=B^Tz_0-b\).

Consider either of the following zero-nudge constructions, with \(\theta\), \(z_0(\theta)\), and \(\delta\) held fixed when the nudge is varied:

- **Scheme I:** \(z_\varepsilon\) minimizes
  \[
  E(z;\theta)-\varepsilon\langle B\delta,z\rangle
  \quad\text{subject to}\quad A^Tz=a.
  \]
- **Scheme II:** \(z_\varepsilon\) minimizes \(E(z;\theta)\) subject to
  \[
  A^Tz=a,
  \qquad B^Tz=(1+\varepsilon)B^Tz_0-\varepsilon b.
  \]

For the chosen scheme, assume that for every \(\theta\in D\) the displayed constrained minimizers exist uniquely and depend differentiably on \(\varepsilon\) in a neighborhood of zero, and that the following continuous-time update exists:
\[
 \dot\theta_i=
 \lim_{\varepsilon\to0}
 \frac{\partial_{\theta_i}E(z_\varepsilon;\theta)-
       \partial_{\theta_i}E(z_0;\theta)}{\varepsilon},
 \qquad i=1,\ldots,m.
\]
Here \(\partial_{\theta_i}E\) means the partial derivative with respect to the parameter argument, holding the state argument fixed.

For each \(i\), let \(D_i=\{\theta_i:\theta\in D\}\). Suppose further that the energy is separable in the parameters:
\[
 E(z;\theta)=\sum_{i=1}^m h_i(\theta_i)U_i(z),
\]
where \(U_i:\mathbb R^N\to\mathbb R\), each \(h_i:D_i\to\mathbb R\) is differentiable with \(h_i'(u)\ne0\) for every \(u\in D_i\), and there is a differentiable \(F_i:D_i\to\mathbb R\) satisfying
\[
 F_i'(u)=\frac{h_i(u)}{h_i'(u)}
 \qquad (u\in D_i).
\]
Define
\[
 M(\theta)=\frac12\sum_{i=1}^mF_i(\theta_i).
\]

For the circuit specializations, let \(d_j\) be oriented edge-incidence vectors of a connected graph, and assume the input constraint makes the quadratic-energy minimizer unique. For positive edge parameters, define
\[
 L(c)=\sum_jc_jd_jd_j^T,
 \qquad
 L(s)=\sum_js_j^{-1}d_jd_j^T,
\]
and use \(E(z;c)=\frac12z^TL(c)z\) or \(E(z;s)=\frac12z^TL(s)z\), respectively, with the same equilibrium, nudge, and update assumptions.

## Task

Prove that, under either Scheme I or Scheme II, \(M(\theta(t))\) is constant along every differentiable trajectory \(\theta(t)\in D\) satisfying the displayed continuous-time update on an interval. Deduce that for the conductance circuit \(\frac12\sum_jc_j(t)^2\) is conserved, and for the resistance circuit \(\frac12\sum_js_j(t)^2\) is conserved, on such intervals with positive edge parameters.
