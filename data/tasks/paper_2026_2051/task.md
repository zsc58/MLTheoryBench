# Problem

## Setup

Let \(K\geq1\) be an integer and let
\[
\Delta^{K-1}=\{z\in\mathbb R^K:z_i\geq0,\ \sum_i z_i=1\}.
\]
Let \(Z_0\) be an integrable \(\mathbb R^K\)-valued random variable and let \(Z_1\in\Delta^{K-1}\) almost surely, with an arbitrary joint law. Set
\[
Z_t=(1-t)Z_0+tZ_1,\qquad 0\leq t\leq1,
\]
and denote its law by \(p_t\).

Let \(D\subseteq\mathbb R^K\) be a Borel state domain with \(p_t(D)=1\) for every \(t\), containing the trajectories considered below. For \(0\leq t<1\), fix measurable versions
\[
q_t(x)=\mathbb E[Z_1\mid Z_t=x],\qquad x\in D,
\]
with \(q_t(D)\subseteq\Delta^{K-1}\), and use the compatible pointwise drift
\[
v_t(x)=\frac{q_t(x)-x}{1-t}.
\]
Assume the ODE \(\dot x_t=v_t(x_t)\) has a unique forward solution from every \((s,x)\in[0,1)\times D\) up to every time below \(1\). Denote its solution maps by \(\Phi_{s,t}:D\to D\), with \(\Phi_{s,s}(x)=x\). Assume they have continuous terminal extensions \(\Phi_{s,1}:D\to D\) for \(s<1\).

Use the following regularity class. The maps \(\Phi_{s,t}(x)\) are jointly \(C^1\) for \(0\leq s\leq t<1\), including the preterminal diagonal, and jointly \(C^1\) off the diagonal for \(0\leq s<t\leq1\). At temporal boundaries derivatives are one-sided; spatial derivatives are understood through local \(C^1\) extensions to neighborhoods in \(\mathbb R^K\). No joint continuity of \(\Phi\) at \((s,t)=(1,1)\) is required.

For \(0\leq s<t\leq1\), define \(m_{s,t}\) by
\[
\Phi_{s,t}(x)=\frac{1-t}{1-s}x+\frac{t-s}{1-s}m_{s,t}(x).
\]
Assume this family has a jointly continuous extension in \((s,t,x)\) to \(0\leq s\leq t\leq1\), and define its diagonal values \(m_{t,t}\) by that extension. Write \(D_x\) for the spatial Jacobian.

## Task

Prove that, on \(D\),
\[
m_{t,t}(x)=q_t(x)=\mathbb E[Z_1\mid Z_t=x]
\qquad(0\leq t<1),
\]
and that \(m_{1,1}\) is a simplex-valued version on \(D\) of \(\mathbb E[Z_1\mid Z_1=\cdot]\). Denote this terminal version by \(q_1\), so that the diagonal identity also holds at \(t=1\) with this choice of version.

Prove that every off-diagonal \(m_{s,t}\), including \(m_{s,1}\), is simplex-valued. Prove, for \(x\in D\) and \(0\leq s<u<t\leq1\),
\[
m_{s,t}(x)=\frac{(1-t)(u-s)}{(1-u)(t-s)}m_{s,u}(x)
+\frac{(t-u)(1-s)}{(1-u)(t-s)}m_{u,t}(\Phi_{s,u}(x)),
\]
and, for \(x\in D\) and \(0\leq s<t\leq1\),
\[
m_{s,t}(x)=m_{t,t}(\Phi_{s,t}(x))-
\frac{(1-t)(t-s)}{1-s}\partial_t m_{s,t}(x),
\]
\[
\partial_s m_{s,t}(x)+D_xm_{s,t}(x)v_s(x)
=\frac{1-t}{(1-s)(t-s)}\bigl(m_{s,t}(x)-m_{s,s}(x)\bigr).
\]

Conversely, let \(n_{s,t}\) be another family with the same continuity and off-diagonal differentiability properties. Suppose its affine maps
\[
F_{s,t}(x)=\frac{1-t}{1-s}x+\frac{t-s}{1-s}n_{s,t}(x)
\quad(s<t),\qquad F_{s,s}(x)=x,
\]
map \(D\) into \(D\) and have the same flow-map regularity specified above. Suppose \(n_{t,t}=q_t\) for \(t<1\), and that the three displayed identities hold with \((m,\Phi)\) replaced by \((n,F)\). Prove that these affine maps obey the semigroup law and the equations
\[
\partial_tF_{s,t}(x)=v_t(F_{s,t}(x))
\quad(0\leq s<t<1),
\]
\[
\partial_sF_{s,t}(x)+D_xF_{s,t}(x)v_s(x)=0
\quad(0\leq s<t\leq1),
\]
and coincide with \(\Phi_{s,t}\), including their terminal extensions. No value of \(v_1\) is stipulated.
