# Problem

## Setup

Let \(P\) be a distribution of \((X,Y,Y',W)\), where \(Y\ne Y'\) almost surely and \(W\in\{-1,1\}\). Let \(\mathcal H\) be a class of measurable real-valued scoring functions \(h(x,y)\), and define
\[
 d_h(x,y,y')=h(x,y)-h(x,y').
\]
Use the binary sign convention
\[
 \operatorname{sgn}_+(t)=
 \begin{cases}
  1,&t\ge0,\\
  -1,&t<0.
 \end{cases}
\]
For \(h\in\mathcal H\), define the ranking loss by
\[
 \ell_0(h;x,y,y',w)
 =\mathbf 1\{w\ne\operatorname{sgn}_+(d_h(x,y,y'))\}.
\]
Thus a zero score difference is assigned the prediction \(+1\).

Let \(S=(X,Y,Y')\). Fix one version of the conditional distribution of \(W\) given \(S\), and use this same conditional distribution for every hypothesis and loss when defining conditional risks.

For any nonnegative measurable loss \(\ell\), write
\[
 R_\ell(h)=\mathbb E_P[\ell(h;X,Y,Y',W)],\qquad
 R_\ell^*(\mathcal H)=\inf_{g\in\mathcal H}R_\ell(g).
\]
Define conditional risks and their best-in-class values by
\[
 c_\ell(h;S)=\mathbb E_P[\ell(h;X,Y,Y',W)\mid S],
 \qquad
 c_\ell^*(\mathcal H;S)=\inf_{g\in\mathcal H}c_\ell(g;S).
\]
The conditional infimum is a pointwise infimum of the conditional risks defined using the fixed conditional distribution. Use \(\inf\varnothing=+\infty\).

Whenever the following subtraction is defined in extended-real arithmetic, define the minimizability gap by
\[
 M_\ell(\mathcal H)=R_\ell^*(\mathcal H)-\mathbb E_P[c_\ell^*(\mathcal H;S)].
\]
No expression of the form \(\infty-\infty\) is assigned a value.

Let \(\Phi:\mathbb R\to[0,\infty)\) be non-increasing. Fix \(\gamma>0\) such that \(\Phi(-\gamma)>0\), and define the shifted surrogate loss
\[
 \ell_{\Phi_\gamma}(h;x,y,y',w)
 =\Phi\bigl(wd_h(x,y,y')-\gamma\bigr).
\]
Assume that the functions \(s\mapsto c_{\ell_0}^*(\mathcal H;s)\) and \(s\mapsto c_{\ell_{\Phi_\gamma}}^*(\mathcal H;s)\) are measurable.

Finally, whenever its terms are defined, set
\[
 A_\gamma(\mathcal H)
 =\frac{\mathbb E_P[c_{\ell_{\Phi_\gamma}}^*(\mathcal H;S)]}{\Phi(-\gamma)}
 -\mathbb E_P[c_{\ell_0}^*(\mathcal H;S)].
\]

## Task

Prove that, for every \(h\in\mathcal H\) for which all terms in the following display are defined (in particular, no difference is of the form \(\infty-\infty\)),
\[
 R_{\ell_0}(h)-R_{\ell_0}^*(\mathcal H)+M_{\ell_0}(\mathcal H)
 \le
 \frac{R_{\ell_{\Phi_\gamma}}(h)-R_{\ell_{\Phi_\gamma}}^*(\mathcal H)+M_{\ell_{\Phi_\gamma}}(\mathcal H)}{\Phi(-\gamma)}
 +A_\gamma(\mathcal H).
\]
