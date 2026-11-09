# Reference Proof

## Proof Structure

Express both quantities as expectations of functions of the score gap. The sigmoid kernel differs from the indicator kernel by an exponentially decaying error. Split the gap distribution into a neighborhood of zero, where its density is bounded, and its complement, where the exponential error is uniformly tiny. This yields the stated approximation, including its uniform version, and then the ranking consequence.

## Complete Proof

Fix a score function and write
\[
G=s_1-s_2
\]
for the gap under the conditional law of a comparable ordered pair. Because \(G\) has a density, \(\Pr(G=0)=0\), so the tie-splitting definition gives
\[
C=\Pr(G>0),\qquad 1-C=\Pr(G<0)=\mathbb E[\mathbf 1\{G<0\}].
\]
Let
\[
g_\tau(z)=\sigma(-z/\tau)-\mathbf 1\{z<0\}.
\]
Then
\[
L_\tau-(1-C)=\mathbb E[g_\tau(G)].
\]
For \(z\ge 0\), \(0\le \sigma(-z/\tau)\le e^{-z/\tau}\). For \(z<0\), \(|\sigma(-z/\tau)-1|=\sigma(z/\tau)\le e^{z/\tau}=e^{-|z|/\tau}\). Hence, for every \(z\),
\[
|g_\tau(z)|\le e^{-|z|/\tau}.
\]
Choose \(\varepsilon>0\) from the density assumption. If \(p\) is the density of \(G\), then
\[
\begin{aligned}
|L_\tau-(1-C)|
&\le \int_{|z|\le\varepsilon}e^{-|z|/\tau}p(z)\,dz
   +\int_{|z|>\varepsilon}e^{-|z|/\tau}p(z)\,dz\\
&\le B\int_{-\varepsilon}^{\varepsilon}e^{-|z|/\tau}\,dz
   +e^{-\varepsilon/\tau}\Pr(|G|>\varepsilon)\\
&\le 2B\tau+e^{-\varepsilon/\tau}.
\end{aligned}
\]
Since \(e^{-\varepsilon/\tau}=o(\tau)\) as \(\tau\downarrow0\), this is \(2B\tau+o(\tau)\). If the same \(B,\varepsilon\) work for every score in a class, the bound is uniform over that class.

Writing \(r_\tau=2B\tau+e^{-\varepsilon/\tau}\), we have \(L_\tau(s)=1-C(s)+e_s\) with \(|e_s|\le r_\tau\). Therefore, for any two scores \(s_a,s_b\),
\[
C(s_a)-C(s_b)>2r_\tau\quad\Longrightarrow\quad L_\tau(s_a)<L_\tau(s_b),
\]
so, up to the approximation error, lower sigmoid loss ranks scores by higher concordance.
