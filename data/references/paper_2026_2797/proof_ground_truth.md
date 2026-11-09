# Reference Proof

## Proof Structure

Work on the tail where the accumulation scale is finite; arbitrary positive extensions at earlier indices do not affect any conclusion. Establish the gap representation, existence of a contact gap, and the exact contact identity. The contact-count lower bound combined with a uniform elementary estimate proves subcritical top-two collapse, even when the contact accumulation exponent tends to zero. The exponential envelope bounds both the partition function and its mean-gap term in the supercritical regime, proving entropy collapse. Finally, compare logarithmic growth classes and rearrange the contact identity.

## Complete Proof

Throughout the proof, take \(n\ge n_0\). All limits are unchanged by the finitely many earlier indices. Suppress the index \(n\) when convenient.

### Finite-scale domain and contact coordinates

The gaps \(d_{n,j}=z_n^*-z_{n,j}\) are nonnegative finite real numbers. If two or more gaps were zero, then \(N_n(t)\ge2\) for every \(t>0\), and \(\log N_n(t)/t\ge\log2/t\) would diverge as \(t\downarrow0\). Thus finiteness of \(\Lambda_n\) implies that exactly one gap is zero and \(N_n(0)=1\).

Since \(n\ge2\), there is at least one positive gap. Let \(\eta_n\) and \(M_n\) be the smallest and largest positive gaps. Both are finite and positive. For \(0<t<\eta_n\), \(N_n(t)=1\); for \(t\ge M_n\), \(N_n(t)=n\). On an interval beginning at a positive gap and ending at the next distinct gap, \(N_n(t)\) is constant and \(\log N_n(t)/t\) is nonincreasing. The same holds after the largest gap. Consequently the supremum is a maximum over the finite, nonempty set of positive gaps. In particular,
\[
0<\frac{\log n}{M_n}\le\Lambda_n<\infty.
\]
The largest maximizing gap \(\Delta_n\) therefore exists, and \(\eta_n\le\Delta_n\). Since \(2\le N_n(\Delta_n)\le n\),
\[
\frac{\log2}{\log n}\le\alpha_n\le1.
\]
The definitions give the exact identities
\[
N_n(\Delta_n)=n^{\alpha_n},\qquad
\Lambda_n\Delta_n=\alpha_n\log n.
\]

### Gap representation and integral formula

Define
\[
Z_n(\beta)=\sum_{j=1}^n e^{-\beta d_{n,j}}.
\]
Factoring \(e^{\beta z_n^*}\) out of the original softmax denominator gives
\[
p_{n,j}(\beta)=\frac{e^{-\beta d_{n,j}}}{Z_n(\beta)}.
\]
The unique zero gap contributes one, so \(Z_n(\beta)\ge1\). For every \(d\ge0\) and \(\beta>0\),
\[
e^{-\beta d}=\beta\int_d^\infty e^{-\beta t}\,dt.
\]
Summing this identity over the finite set of gaps yields
\[
Z_n(\beta)=\beta\int_0^\infty e^{-\beta t}N_n(t)\,dt.
\]
All these integrals are finite because \(N_n(t)\le n\).

### Subcritical top-two collapse

Let \((\beta_n)\) be any positive deterministic sequence with
\[
s_n:=\beta_n/\Lambda_n\longrightarrow0.
\]
Each of the \(N_n(\Delta_n)\) gaps at most \(\Delta_n\) contributes at least \(e^{-\beta_n\Delta_n}\), hence
\[
Z_n(\beta_n)\ge N_n(\Delta_n)e^{-\beta_n\Delta_n}
=n^{\alpha_n(1-s_n)}.
\]
For all sufficiently large \(n\), \(s_n\le1/2\), so \(Z_n(\beta_n)\ge n^{\alpha_n/2}\).

The largest and second-largest unnormalized weights are \(1\) and \(e^{-\beta_n\eta_n}\). Using \(1-e^{-x}\le x\) for \(x\ge0\), \(\eta_n\le\Delta_n\), and the contact identity,
\[
\begin{aligned}
D_n(\beta_n)
&=\frac{1-e^{-\beta_n\eta_n}}{Z_n(\beta_n)}\\
&\le\frac{\beta_n\Delta_n}{n^{\alpha_n/2}}
=s_n(\alpha_n\log n)e^{-\alpha_n\log n/2}.
\end{aligned}
\]
The function \(u\mapsto ue^{-u/2}\) on \([0,\infty)\) has maximum \(2/e\), attained at \(u=2\). Therefore
\[
0\le D_n(\beta_n)\le(2/e)s_n\longrightarrow0.
\]
This estimate does not require \(\alpha_n\) to stay bounded away from zero or the contact count to diverge.

### Supercritical entropy collapse

Now let \((\beta_n)\) be any positive deterministic sequence with \(s_n=\beta_n/\Lambda_n\to\infty\). Eventually \(\beta_n>\Lambda_n\). By the definition of \(\Lambda_n\),
\[
N_n(t)\le e^{\Lambda_n t}\qquad(t>0).
\]
Using the integral formula,
\[
1\le Z_n(\beta_n)
\le\beta_n\int_0^\infty e^{-(\beta_n-\Lambda_n)t}\,dt
=\frac{\beta_n}{\beta_n-\Lambda_n}
\longrightarrow1.
\]
Thus \(Z_n(\beta_n)\to1\).

For fixed \(n\), differentiation of the finite sum gives
\[
-Z_n'(\beta)=\sum_j d_{n,j}e^{-\beta d_{n,j}}\ge0.
\]
Differentiating the integral representation also gives
\[
-\beta Z_n'(\beta)
=\beta^2\int_0^\infty t e^{-\beta t}N_n(t)\,dt-Z_n(\beta).
\]
This differentiation is justified locally around any \(\beta>0\): \(N_n(t)\le n\), and an integrable constant multiple of \((1+t)e^{-\beta t/2}\) dominates the differentiated integrand for nearby positive inverse temperatures.

For \(\beta>\Lambda_n\), apply the envelope to the positive integral and use \(Z_n(\beta)\ge1\). The elementary identity \(\int_0^\infty t e^{-at}\,dt=a^{-2}\), for \(a>0\), follows by integration by parts. Hence
\[
0\le-\beta Z_n'(\beta)
\le\frac{\beta^2}{(\beta-\Lambda_n)^2}-1.
\]
At \(\beta=\beta_n\), put \(r_n=\Lambda_n/\beta_n=1/s_n\to0\). Then
\[
0\le-\beta_n Z_n'(\beta_n)
\le\frac{1}{(1-r_n)^2}-1
=\frac{2r_n-r_n^2}{(1-r_n)^2}
\longrightarrow0.
\]

Finally, \(\log p_{n,j}(\beta)=-\beta d_{n,j}-\log Z_n(\beta)\), and summation against the probabilities gives
\[
H_n(\beta)
=\log Z_n(\beta)+\frac{\beta\sum_j d_{n,j}e^{-\beta d_{n,j}}}{Z_n(\beta)}
=\log Z_n(\beta)-\frac{\beta Z_n'(\beta)}{Z_n(\beta)}.
\]
Because \(Z_n(\beta_n)\to1\), \(Z_n(\beta_n)\ge1\), and \(-\beta_nZ_n'(\beta_n)\to0\), both nonnegative terms tend to zero. Thus \(H_n(\beta_n)\to0\). The two implications, for every positive deterministic schedule, prove that the positively extended sequence \((\Lambda_n)\) is a TE scale.

### Exponent selection

Suppose
\[
\beta_n\asymp(\log n)^{\xi_\beta},\qquad
\Lambda_n\asymp(\log n)^{\xi_\Lambda},\qquad \xi_\beta\ge0.
\]
The comparison constants are fixed positive constants, independent of \(n\). Dividing the two comparisons gives
\[
\beta_n/\Lambda_n\asymp(\log n)^{\xi_\beta-\xi_\Lambda}.
\]
If \(\xi_\beta<\xi_\Lambda\), this ratio tends to zero, forcing top-two collapse. If \(\xi_\beta>\xi_\Lambda\), it tends to infinity, forcing entropy collapse. Therefore a schedule avoiding both collapses must satisfy \(\xi_\beta=\xi_\Lambda\). This is a necessary condition, not a claim that every matched-exponent schedule avoids both collapses.

### Contact-coordinate exponents

A logarithmic growth exponent is unique: if a positive sequence is comparable to both \((\log n)^a\) and \((\log n)^b\), then \((\log n)^{a-b}\) is bounded above and below by positive constants eventually. Since \(\log n\to\infty\), this requires \(a=b\).

On the finite-scale tail,
\[
\Lambda_n=\frac{\alpha_n\log n}{\Delta_n}.
\]
Products and quotients of bounded-ratio comparisons remain bounded-ratio comparisons, since all comparison constants and sequences are positive. If \(\alpha_n\) and \(\Delta_n\) have exponents, then
\[
\Lambda_n\asymp(\log n)^{\xi_\alpha-\xi_\Delta+1}.
\]
If \(\Lambda_n\) and \(\Delta_n\) have exponents, rearrange the identity to obtain
\[
\alpha_n=\frac{\Lambda_n\Delta_n}{\log n}
\asymp(\log n)^{\xi_\Lambda+\xi_\Delta-1}.
\]
If \(\Lambda_n\) and \(\alpha_n\) have exponents, use
\[
\Delta_n=\frac{\alpha_n\log n}{\Lambda_n}
\asymp(\log n)^{\xi_\alpha+1-\xi_\Lambda}.
\]
In each case the third exponent exists, and uniqueness gives
\[
\xi_\Lambda=\xi_\alpha-\xi_\Delta+1.
\]
All theorem-critical obligations have been derived above; no external proof dependency remains.
