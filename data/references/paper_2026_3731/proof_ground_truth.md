# Reference Proof

All probabilities below use the changed law for the current $T$. The detector and its null survival sequence may vary with $T$. Put $C_v=4+4(1+\log2)^2$, so $C_0=32(C_v+1)$. Since $P(E_T)$ has a positive liminf, choose $\varepsilon>0$ with $P(E_T)\ge\varepsilon$ for all sufficiently large $T$. The stopping-time property and equality of the pre-change laws give
\[
r_{T-1}=P_{F_0,T,F_1}(\tau\ge T-1)\ge P(E_T)\ge\varepsilon.
\]
Thus $c_{\alpha,T}=-\log(\alpha r_{T-1})$ is uniformly bounded. A zero $r_t$ cannot occur with positive changed-law probability on $\{\tau\ge t\}$ by detector domination.

**Rank drift.** Write $P\{S(Z)>S(Y)\}-1/2=\sigma\delta$, where $\sigma\in\{-1,1\}$. For $t=T-k$ and $j=T+\ell$, independence and the randomized self-rank give
\[
E(p_{T-k}^{T+\ell}-1/2)=\frac{\sigma k\delta}{k+\ell+1}.
\]
If $m\le k$ and $0\le\ell<m$, take $a=k\delta/(k+m)$ and compare the oracle with the admissible coefficient $2\sigma a$. For $|x|\le1/2$, $\log(1+x)\ge x-x^2$; also $|p-1/2|\le1/2$. Consequently,
\[
E\log f_{T-k,T+\ell}(p_{T-k}^{T+\ell})\ge a^2.
\]
Forward factors indexed before $T$ equal one: their ranks are uniform under $F_0$ and the unique expected-log maximizer is zero. For a backward product ending at $T+k-1$, a pre-change index $j=T-\ell$ has
\[
E(q_{T+k-1}^{T-\ell}-1/2)=-\frac{\sigma k\delta}{k+\ell}.
\]
The identical comparison with coefficient $-2\sigma k\delta/(k+v)$ shows that each of the $v\le k$ retained pre-change backward factors has expected log at least $(k\delta/(k+v))^2$. Its post-change factors equal one. In particular, either retained log-product of length $h\le k$ has mean at least $\delta^2h/4$. This backward calculation verifies, rather than merely invokes, the forward-to-backward analogy.

**Concentration.** For either retained log-product, let $h$ be its number of mixed-window factors and $k$ the number of observations on the opposite side of the change; here $h\le k$. Every log calibrator has absolute value at most $M=\log2$ and Lipschitz constant at most $L=2$. Changing one of the $k$ opposite-side observations changes each rank by at most its reciprocal window length, giving sensitivity at most $Lh/k$. Changing one of the $h$ retained observations has direct sensitivity at most $2M$ and propagated sensitivity at most $Lh/k$. Each retained uniform affects only its own rank, with sensitivity at most $L/k$. These statements hold with the order of observations reversed for the backward product. The sum of squared sensitivities is at most
\[
\frac{L^2h^2}{k}+h(2M+Lh/k)^2+\frac{L^2h}{k^2}\le C_vh+\frac4k.
\]
The observations and uniforms are independent, and the oracle coefficients are fixed. McDiarmid's bounded-differences inequality, in the form $P\{H-EH\le-u\}\le\exp(-2u^2/\sum c_i^2)$, therefore applies to either product. If its mean exceeds the relevant log threshold by $\delta^2h/8$, its failure probability is at most
\[
\exp\!\left\{-\frac{\delta^4h^2}{32(C_vh+4/k)}\right\}.\tag{1}
\]

**Pre-change candidates.** Set $m_k=\min\{k,\max(1,\lceil s\log k\rceil)\}$. This is nondecreasing, satisfies $1\le m_k\le k$, and equals $\lceil s\log k\rceil$ for all sufficiently large $k$. On $E_T$, all the first $m_k$ post-change factors are observable for every $1\le k\le T-2$. If $T-k\in C_{\rm low}^{\alpha}$, their log-product $B_k$ cannot exceed $-\log(\alpha r_{T-k})\le c_{\alpha,T}$. Its mean is at least $\delta^2m_k/4$. Let $K_T$ be the first $k$ for which $m_k>8c_{\alpha,T}/\delta^2$. Uniform boundedness of $c_{\alpha,T}$ makes $K_T$ uniformly bounded. Counting smaller $k$ trivially and applying (1) to the rest yields
\[
E[|C_{\rm low}^{\alpha}\cap\{t<T\}|;E_T]\le K_T-1+\sum_{k=K_T}^{T-2}\exp\!\left\{-\frac{\delta^4m_k^2}{32(C_vm_k+4/k)}\right\}.
\]
For all sufficiently large $k$, $4/k\le m_k$ and $m_k\ge s\log k$. Hence the summands are at most $k^{-s\delta^4/C_0}$. Summing this series and dividing by $P(E_T)\ge\varepsilon$ gives the three claimed pre-change rates, including the equality case.

**Post-change candidates.** Choose the nondecreasing integer sequence $m_n=\max\{n,\lfloor e^{n/s'}\rfloor\}$, and put $L_T=T+m_T$. For large $T$, integer rounding makes $E_T\subseteq\{T\le\tau\le L_T\}$. For $1\le k\le m_T$ let
\[
u_k=\inf\{n\ge1:m_n\ge k\},\qquad v_{k,T}=\min\{u_k,T-1\}.
\]
Then $1\le v_{k,T}\le k$, and the backward block $j=T-v_{k,T},\ldots,T-1$ uses existing observations. In particular, the source's untruncated block cannot be used when $u_k=T$. For all sufficiently large $k$, uniformly over $k\le m_T$, $v_{k,T}\ge s'\log k-1$; truncation can lose at most one term at the upper endpoint.

To control a stopping-dependent threshold without defining $r_\infty$, put $R_T^*=r_{\min(\tau,L_T)}$. For any $x\in[0,1]$, if some index at most $L_T$ first has $r_j\le x$, the event $\{R_T^*\le x\}$ is $\{\tau\ge j\}$ and has probability at most $r_j\le x$ by detector domination. If no such index exists, the event is empty. Thus $P(R_T^*\le x)\le x$, also when $P(\tau=\infty)>0$. On $E_T$, $R_T^*=r_\tau$, and for a retained candidate $t=T+k\le\tau$, $r_t\ge R_T^*$.

Let $D_{k,T}$ be the log-product over the valid backward block. Its mean is at least $\delta^2v_{k,T}/4$. Choose $c$ with $1/s'<c<\delta^2/8$. Super-uniformity gives
\[
P\{T+k\in C_{\rm up}^{\alpha},E_T\}\le P\{D_{k,T}\le cv_{k,T}+\log(1/\alpha)\}+e^{-cv_{k,T}}.
\]
Because $v_{k,T}\ge s'\log k-1$ for sufficiently large $k$, a fixed $K$ makes $v_{k,T}>\log(1/\alpha)/(\delta^2/8-c)$ for all $K\le k\le m_T$ and sufficiently large $T$. For those $k$, the mean exceeds the displayed deterministic threshold by at least $\delta^2v_{k,T}/8$, so (1) applies with $h=v_{k,T}$. Eventually $4/k\le v_{k,T}$; the two resulting summands are bounded by constant multiples of $k^{-s'\delta^4/C_0}$ and $k^{-cs'}$. Both series converge by the assumptions on $s'$ and $c$. Count $t=T$ and the finitely many $k<K$ trivially. It follows that
\[
E[|C_{\rm up}^{\alpha}\cap\{t\ge T\}|;E_T]=O(1),
\]
and division by $P(E_T)\ge\varepsilon$ gives an $O(1)$ conditional contribution.

Finally, $C\subseteq C_{\rm low}^{\alpha}$ before $T$ and $C\subseteq C_{\rm up}^{\alpha}$ at or after $T$. Adding the two bounds proves the stated trichotomy. Each rate is $o(T)$, proving the relative-size assertion.
