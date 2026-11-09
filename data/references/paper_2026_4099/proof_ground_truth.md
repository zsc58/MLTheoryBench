# Reference Proof

## Proof Structure

1. Evaluate the interventional coalition values for the balanced three-bit XOR oracle.
2. Apply the defining Möbius sums to obtain the singleton, pair, and triple coefficients.
3. Evaluate the two explicitly defined scalar pair-reporting rules.
4. Evaluate the interventional squared-loss LOCO gains and the resulting U/R/S decomposition.

## Complete Proof

Fix any \(x\in\{0,1\}^3\), and let \(y=x_1\oplus x_2\oplus x_3\). The predictor is the fixed XOR function, and all background coordinates are independent fair bits. All expectations are finite sums, and the target label \(y\) remains fixed during background replacement.

### 1. Coalition values

For a proper coalition \(S\subsetneq N\), choose a coordinate \(r\notin S\). Conditional on all other background coordinates, the masked oracle output is either \(Z_r\) or \(1-Z_r\). In either case it is a fair bit. Averaging over the other coordinates therefore gives
\[
v(S;x)=\mathbb E_Z[f(\mathbf 1_S\odot x+(\mathbf 1-\mathbf 1_S)\odot Z)]=\tfrac12.
\]
For \(S=N\), no coordinate is replaced, and \(v(N;x)=f(x)=y\).

### 2. Möbius coefficients

For a singleton, the defining alternating sum gives
\[
m_i=v(\{i\};x)-v(\varnothing;x)=\tfrac12-\tfrac12=0.
\]
For a pair,
\[
m_{ij}=v(\{i,j\};x)-v(\{i\};x)-v(\{j\};x)+v(\varnothing;x)
=\tfrac12-\tfrac12-\tfrac12+\tfrac12=0.
\]
For the triple,
\[
\begin{aligned}
m_{123}
&=v(N;x)-\sum_{|S|=2}v(S;x)+\sum_{|S|=1}v(S;x)-v(\varnothing;x)\\
&=y-3\cdot\tfrac12+3\cdot\tfrac12-\tfrac12
=y-\tfrac12.
\end{aligned}
\]
Since \(y\in\{0,1\}\), this coefficient is always nonzero and belongs to \(\{-1/2,1/2\}\).

### 3. Pair reports

A faithful pair report is \(m_{ij}\) by the task's definition, so it is zero.

For a fixed pair \(i,j\), let \(k\) be the remaining coordinate. All four coalitions in the empty-context difference are proper, so
\[
\Delta_{ij}v(\varnothing)=0.
\]
For the other admissible context,
\[
\begin{aligned}
\Delta_{ij}v(\{k\})
&=v(N;x)-v(\{i,k\};x)-v(\{j,k\};x)+v(\{k\};x)\\
&=y-\tfrac12-\tfrac12+\tfrac12
=y-\tfrac12=m_{123}.
\end{aligned}
\]
Consequently,
\[
P_{ij}=\tfrac12\Delta_{ij}v(\varnothing)+\tfrac12\Delta_{ij}v(\{k\})
=\tfrac12m_{123}\in\{-1/4,1/4\}.
\]
The sign is negative when \(y=0\) and positive when \(y=1\). Thus the faithful rule has zero pair outputs despite the nonzero third-order coefficient, while the projective rule has nonzero signed pair outputs despite every pair Möbius coefficient being zero. This establishes the stated interpretation for these two rules.

### 4. Squared-loss LOCO decomposition

For a proper coalition, the masked prediction is zero or one with equal probability. Because \(y\) is fixed,
\[
L(S;x,y)=\tfrac12(0-y)^2+\tfrac12(1-y)^2=\tfrac12
\qquad(S\subsetneq N).
\]
This calculation holds for both possible labels. It is the expectation of squared loss, not the squared loss of the expected prediction. At the grand coalition, the prediction equals \(y\), so \(L(N;x,y)=0\).

Fix \(i\in N\). Every admissible context \(C\subseteq N\setminus\{i\}\) is proper. If \(C\ne N\setminus\{i\}\), then \(C\cup\{i\}\) is also proper and
\[
G_i(C)=\tfrac12-\tfrac12=0.
\]
If \(C=N\setminus\{i\}\), then
\[
G_i(C)=\tfrac12-0=\tfrac12.
\]
The empty context belongs to the first case. Hence
\[
U_i=0,\qquad M_i=\tfrac12,\qquad \pi_i=0,
\]
and therefore
\[
R_i=\pi_i-U_i=0,\qquad S_i=M_i-\pi_i=\tfrac12.
\]
Thus \((U_i,R_i,S_i)=(0,0,1/2)\) for every feature and every binary input.

## Source-Audit Notes

The source's displayed calculation at L001327, \(0.5(1-0)^2+0.5(0-1)^2=1/2\), contains an arithmetic error: its left side is 1. The fixed-label calculation in Section 4 is the local repair. It preserves the claimed coalition loss and every subsequent LOCO conclusion; this repair is recorded under theory_001 in provenance.

The proof uses only the report definitions supplied in the public task. It does not assume that all named interaction-index variants in the source equal these rules. No general impossibility theorem for arbitrary scalar encodings is required or established. Every proof obligation for the frozen public task is closed by the finite calculations above.
