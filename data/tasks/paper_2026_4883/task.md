# Problem

## Setup

Consider \(N\ge 2\) contexts. Let \(v_1,\ldots,v_N\) be pairwise orthogonal nonzero vectors, and write \(a_n=\|v_n\|^2>0\). Each context has a correct-action probability \(p_n\in(0,1)\), with the \(p_n\) not all equal. Fix a temperature \(\eta>1/2\), let \(\sigma(x)=1/(1+e^{-x})\), and define the gate
\[
s_n=\sigma\!\left(\frac{-\log p_n}{\eta}\right).
\]
The equal-weight oracle, standard policy-gradient, and expected gated directions are respectively
\[
d_{\rm CE}=\sum_{n=1}^N v_n,\qquad
d_{\rm PG}=\sum_{n=1}^N p_nv_n,\qquad
d_{\rm DG}=\sum_{n=1}^N p_ns_nv_n.
\]
For nonzero vectors, \(\cos(x,y)=\langle x,y\rangle/(\|x\|\,\|y\|)\).

## Task

Prove that the expected gated direction is strictly better aligned with the equal-weight oracle than the standard policy-gradient direction:
\[
\cos(d_{\rm DG},d_{\rm CE})>\cos(d_{\rm PG},d_{\rm CE}).
\]
