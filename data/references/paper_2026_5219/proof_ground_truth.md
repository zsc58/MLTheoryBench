# Reference Proof

## Proof Structure

The theorem-critical obligations are: establish the finite-game Shapley representation; compute the restricted metagame's coefficients and its directed Shapley attribution; derive the symmetric pair coefficients from their defining finite differences; compare the Shapley singleton and pair expressions; prove the path-based singleton identity by the one-dimensional fundamental theorem; and identify and symmetrize the path-based off-diagonal expressions. The nonstandard pair representation is derived rather than assumed. The path-based singleton is an endpoint difference, not an integrated-gradient value by definition.

## Complete Proof

Write \(v(A)=f(A;x)\), and let
\[
m_U=\sum_{R\subseteq U}(-1)^{|U|-|R|}v(R)
\]
be the Mobius transform of \(v\). Thus \(v(A)=\sum_{U\subseteq A}m_U\). Indeed, substituting the definition into this last sum leaves coefficient \((1-1)^{|A\setminus R|}\) on \(v(R)\), so only \(R=A\) survives.

We first recall and verify the Shapley Mobius formula for an arbitrary real-valued game \(w\) on a finite player set \(B\):
\[
\operatorname{SV}_i(w)=\sum_{\substack{U\subseteq B\\i\in U}}\frac{m_U(w)}{|U|}.
\]
The factorial weights in the Shapley definition are the probabilities of the possible predecessor sets of \(i\) in a uniformly ordered list of the players. Mobius inversion writes \(w\) as the sum of its coefficients times the games \(A\mapsto\mathbf 1\{U\subseteq A\}\). For a nonempty \(U\) containing \(i\), the marginal contribution in this game is one precisely when \(i\) is last among the members of \(U\), which has probability \(1/|U|\). If \(i\notin U\), or if \(U=\varnothing\), the marginal contribution is zero. Linearity proves the displayed formula. In particular, it does not require \(w(\varnothing)=0\). All games used here have finitely many players and finite real values, so these hypotheses hold.

Fix \(i\). For \(A\subseteq N\setminus\{i\}\), define the restricted metagame
\[
n_i(A)=\operatorname{SV}_i(A\cup\{i\}).
\]
The Mobius coefficients of a restriction of \(v\) agree with those of \(v\) on subsets of its player set. Applying the Shapley Mobius formula to the restriction to \(A\cup\{i\}\) gives
\[
n_i(A)=\sum_{T\subseteq A}\frac{m_{T\cup\{i\}}}{|T|+1}.
\]
Consequently, by uniqueness of Mobius inversion, the Mobius coefficient of \(n_i\) at \(T\subseteq N\setminus\{i\}\) is
\[
m_T(n_i)=\frac{m_{T\cup\{i\}}}{|T|+1}.
\]
For \(j\ne i\), the definition of \(\mathcal M^{\operatorname{SV}}_{j\to i}\) is exactly the Shapley value of player \(j\) in \(n_i\), since
\[
\frac{1}{(d-1)\binom{d-2}{|S|}}
=\frac{|S|!(d-2-|S|)!}{(d-1)!}.
\]
Applying the Shapley Mobius formula once more yields
\[
\mathcal M^{\operatorname{SV}}_{j\to i}
=\sum_{\substack{T\subseteq N\setminus\{i\}\\j\in T}}\frac{m_T(n_i)}{|T|}
=\sum_{U\supseteq\{i,j\}}\frac{m_U}{|U|(|U|-1)}. \tag{1}
\]
Also, the diagonal definition and the singleton restricted game give
\[
\mathcal M^{\operatorname{SV}}_{i\to i}
=\operatorname{SV}_i(\{i\})
=v(\{i\})-v(\varnothing)
=m_{\{i\}}
=\Theta_{\{i\}}. \tag{2}
\]

It remains to identify the symmetric pair expression. For fixed \(i\ne j\) and \(S\subseteq N\setminus\{i,j\}\), Mobius inversion and cancellation give
\[
\sum_{T\subseteq\{i,j\}}(-1)^{|T|}v(S\cup T)
=\sum_{U:\ \{i,j\}\subseteq U\subseteq S\cup\{i,j\}}m_U.
\]
In fact, the coefficient of \(m_U\) vanishes unless \(U\) contains both \(i\) and \(j\); if it contains both, only the term with \(T=\{i,j\}\) contributes.

Fix \(U\supseteq\{i,j\}\) and put \(r=|U|-2\). The coefficient of \(m_U\) in \(\Theta_{\{i,j\}}\) is
\[
\sum_{s=r}^{d-2}\frac{2}{d\binom{d-1}{s}}\binom{d-2-r}{s-r}. \tag{3}
\]
For integers \(0\le s\le d-1\), elementary integration by parts gives
\[
\frac{1}{\binom{d-1}{s}}
=d\int_0^1 t^s(1-t)^{d-1-s}\,dt.
\]
Thus, writing \(q=s-r\), expression (3) equals
\[
2\int_0^1 t^r(1-t)
\sum_{q=0}^{d-2-r}\binom{d-2-r}{q}
 t^q(1-t)^{d-2-r-q}\,dt
=2\int_0^1t^r(1-t)\,dt
=\frac{2}{(r+1)(r+2)}
=\frac{1}{\binom{|U|}{2}}.
\]
All sums are finite, so their interchange with these polynomial integrals needs no limiting argument. Consequently,
\[
\Theta_{\{i,j\}}
=\sum_{U\supseteq\{i,j\}}\frac{m_U}{\binom{|U|}{2}}
=\sum_{U\supseteq\{i,j\}}\frac{2m_U}{|U|(|U|-1)}.
\]
By (1), this is
\[
\mathcal M^{\operatorname{SV}}_{j\to i}
+\mathcal M^{\operatorname{SV}}_{i\to j},
\]
because interchanging \(i\) and \(j\) leaves the summands in (1) unchanged. Together with (2), this proves both Shapley-based identities.

For the path-based singleton, put
\[
h_i(t)=f(z^{\{i\}}(t)),\qquad 0\le t\le1.
\]
Existence of the ordinary partial derivative along this coordinate segment implies that \(h_i\) is continuous on \([0,1]\) and differentiable at every interior point, with
\[
h_i'(t)=(x_i-b_i)\partial_i f(z^{\{i\}}(t)).
\]
When \(x_i=b_i\), the same statements hold because \(h_i\) is constant. The stated integrability assumption implies \(h_i'\in L^1([0,1])\).

We use the following standard independent one-dimensional Newton-Leibniz theorem: if \(h\) is continuous on a compact interval, differentiable at every interior point, and its derivative is Lebesgue integrable, then the integral of its derivative is the difference of its endpoint values. Everywhere interior differentiability, rather than merely almost-everywhere differentiability, is part of this statement. All its hypotheses have just been verified for \(h_i\). It follows that
\[
\operatorname{IG}_i(\{i\})
=\int_0^1h_i'(t)\,dt
=h_i(1)-h_i(0)
=f(\{i\};x)-f(\varnothing;x)
=\mathcal P_i.
\]
Since \(\mathcal M^{\operatorname{IG}}_{i\to i}=\operatorname{IG}_i(\{i\})\), the path-based singleton identity follows. No endpoint identity was assumed as a premise.

Finally, for \(i\ne j\), the displayed definitions give
\[
\mathcal P_{j\to i}=\mathcal M^{\operatorname{IG}}_{j\to i}
\]
term by term. The definition of \(\mathcal P_{\{i,j\}}\) as the sum of both directions therefore gives
\[
\mathcal P_{\{i,j\}}
=\mathcal M^{\operatorname{IG}}_{j\to i}
+\mathcal M^{\operatorname{IG}}_{i\to j}.
\]

The arguments include \(d=2\): the relevant subset sum then contains only the empty set, and the coefficient computation has \(r=0\). No step divides by a coordinate displacement or assumes a zero baseline value. Thus zero displacements, constant predictors, and arbitrary finite \(f(b)\) are covered. All four identities are proved.
