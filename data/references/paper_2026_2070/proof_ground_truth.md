# Reference Proof

## Obligations and conventions

We prove the claimed bound with a finite constant depending only on \(\theta\). The proof closes the following obligations explicitly: an independent centered-sum estimate; a shifted-log change-of-measure estimate; conditional application under each product law; the first-scale and subsequent-scale geometric bounds; integrability and convergence for an arbitrary data-dependent learner; and the distinction between scale-by-scale finiteness and summability.

Throughout, \(q=1/\theta\geq1/2\). Constants introduced below depend only on \(\theta\). They need not equal a particular numerical choice suggested in the source appendix: the target quantifies the existence of \(M_\theta\).

## 1. An elementary centered-sum estimate

Suppose \(X_1,\ldots,X_n\) are independent, centered, and satisfy \(\mathbb E\exp(|X_i|^\theta)\leq2\). We show that a finite \(K_\theta\) satisfies
\[
\mathbb E\exp\left(\left|\frac{\sum_{i=1}^nX_i}{K_\theta\sqrt n}\right|^\theta\right)\leq2.
\]

The exponential assumption gives \(\mathbb P(|X_i|>t)\leq2\exp(-t^\theta)\), hence
\[
\mathbb E|X_i|^r\leq2\Gamma(1+qr),\qquad r>0.
\]
For \(u>0\),
\[
\Gamma(1+u)=\int_0^\infty t^u\exp(-t)\,dt
\leq2(2u/\exp(1))^u,
\]
because \(t^u\exp(-t/2)\leq(2u/\exp(1))^u\). Therefore, with \(C_\theta=2(2q/\exp(1))^q\),
\[
\mathbb E|X_i|^r\leq(C_\theta r^q)^r\quad(r\geq2).
\]
Using \(r!\geq(r/\exp(1))^r\), put \(c_\theta=\exp(1)C_\theta\) to obtain
\[
\frac{\mathbb E|X_i|^r}{r!}\leq c_\theta^r r^{(q-1)r}\quad(r\in\mathbb N,\ r\geq2).
\]

Let \(p\geq2\) be even and \(Y=n^{-1/2}\sum_iX_i\). Expand the \(p\)-th moment. Independence and centering remove every term with an index appearing exactly once. Taking absolute values of the remaining expectations gives
\[
\mathbb E|Y|^p\leq p!c_\theta^p
\sum_{k=1}^{\min(n,p/2)}\binom nk n^{-p/2}
\sum_{\substack{j_1+\cdots+j_k=p\\j_a\geq2}}
\prod_{a=1}^k j_a^{(q-1)j_a}.
\]
There are at most \(2^{p-1}\) ordered compositions of \(p\), and this upper bound also applies for each fixed \(k\).

If \(q\geq1\), the product is at most \(p^{(q-1)p}\), while
\[
\sum_{k\leq\min(n,p/2)}\binom nk n^{-p/2}
\leq\sum_{k\leq p/2}\frac{n^{k-p/2}}{k!}\leq\exp(1).
\]
Together with \(p!\leq p^p\), this gives \(\|Y\|_p\leq4c_\theta p^q\).

If \(1/2\leq q\leq1\), write \(b=1-q\). Convexity of \(x\log x\) yields
\[
\prod_a j_a^{-b j_a}\leq(k/p)^{bp}.
\]
Since \(n\geq k\) and \(k-p/2\leq0\),
\[
\binom nk n^{-p/2}\leq\frac{k^{k-p/2}}{k!}
\leq\exp(k)k^{-p/2}.
\]
Thus the coefficient times the product is at most
\[
\exp(p/2)p^{-bp}k^{(b-1/2)p}\leq\exp(p/2)p^{-bp}.
\]
Summing over all compositions again gives \(\|Y\|_p\leq4c_\theta p^q\).

Set \(K_0=4c_\theta\). For any real \(r\geq2\), comparison with the next even integer gives \(\|Y\|_r\leq2^qK_0r^q\); for \(0<r<2\), use \(\|Y\|_r\leq\|Y\|_2\). It follows that, for every integer \(j\geq1\),
\[
\|Y\|_{j\theta}\leq H_\theta j^q,
\qquad H_\theta=2^{2q}K_0.
\]
Choose \(K_\theta=H_\theta(2\exp(1))^q\). Expanding the exponential and using nonnegative-term convergence,
\[
\mathbb E\exp(|Y/K_\theta|^\theta)
\leq1+\sum_{j\geq1}\frac{H_\theta^{j\theta}j^j}{K_\theta^{j\theta}j!}
\leq1+\sum_{j\geq1}2^{-j}=2.
\]
This proves the needed sum estimate without invoking a specialized external moment theorem.

## 2. A directly verified shifted-log estimate

Define
\[
B_\theta=\sup_{y\geq0}y\exp(-y^\theta/2)
=\left(\frac{2}{\exp(1)\theta}\right)^{1/\theta}.
\]
For \(x,y\geq0\) and \(A\geq1\),
\[
xy\leq2^q x[\log(x+A)]^q+B_\theta\exp(y^\theta).
\]
Indeed, if \(y\leq2^q[\log(x+A)]^q\), the first term suffices. Otherwise \(x<\exp(y^\theta/2)\), and
\(xy\leq y\exp(y^\theta/2)\leq B_\theta\exp(y^\theta)\).

Consequently, if \(P\ll Q\), \(r\geq0\), and \(\mathbb E_Q\exp(r^\theta)\leq2\), integration with \(x=dP/dQ\) gives
\[
\mathbb E_Pr\leq2^qD_{f_\theta}(P\|Q)+2B_\theta.
\]
This argument is valid for extended nonnegative integrals, so it does not assume the desired dependent expectation is finite in advance.

Fix once and for all
\[
M_\theta=K_\theta\max\{1,B_\theta/2\}.
\]
Combining the two estimates, whenever conditionally fixed representatives \(u,v\) have \(d(u,v)\leq\delta\), the empirical increment satisfies
\[
\mathbb E_P|G(u,S)-G(v,S)|
\leq\frac{M_\theta\delta}{\sqrt n}
\bigl(2^qD_{f_\theta}(P\|Q)+4\bigr)
\]
under the joint-versus-product application justified below. This \(M_\theta\) is independent of the shift \(A\), the metric space, the sample size, and the learner.

## 3. Entropy, integrability, and the separable limit

We establish the regularity needed for the data-dependent evaluation, rather than inferring it from metric convergence alone.

Consider \(X_w=\bar\ell(w,Z)\). Each fixed coordinate is integrable and centered. The increment assumption and the moment estimate preceding the sum calculation imply the following finite-family bound: if \(V_1,\ldots,V_m\) have sub-Weibull scale at most \(b\), then
\[
\mathbb E\max_{a\leq m}|V_a|\leq C'_{\theta}b[\log(2m)]^q.
\]
To verify it, choose \(r=\max\{2,\log m\}\), use
\(\|\max_a|V_a|\|_r\leq m^{1/r}\max_a\|V_a\|_r\), and use the already derived single-variable moment bound. The constants relating \(r\) and \(\log(2m)\) are universal.

Finite entropy implies that \(N(\mathcal W,d,\varepsilon)<\infty\) for every \(\varepsilon>0\), since otherwise the entropy integrand is infinite on an interval. In particular, \(\mathcal W\) is totally bounded and has finite covering radius. Fix \(R>0\) large enough and let \(\rho_j=R2^{-j}\). Choose finite \(\rho_j\)-nets \(T_j\) with \(|T_j|=N_j=N(\mathcal W,d,\rho_j)\). Monotonicity of the covering numbers gives
\[
\sum_{j\geq1}\rho_j[\log(2N_j)]^q<\infty.
\]
For the part involving \(\log N_j\), use
\(\rho_j[\log N_j]^q\leq2\int_{\rho_{j+1}}^{\rho_j}[\log N(\mathcal W,d,u)]^q\,du\); the additional constant logarithm contributes a geometric series.

Let \(T_*\) be the countable union of a separability set, the nets, and all prescribed representatives. For each \(t\in T_*\), choose \(\pi_j(t)\in T_j\) within distance \(\rho_j\). Let \(A_j\) be the maximum increment between pairs in \(T_j\times T_{j-1}\) at distance at most \(\rho_j+\rho_{j-1}\), taking the maximum to be zero if there are no such pairs. Let \(B_j\) be the maximum increment between pairs in \(T_j\times T_j\) at distance at most \(3\rho_j\). The finite-family bound gives
\[
\sum_{j\geq2}\mathbb EA_j+\sum_{j\geq1}\mathbb EB_j<\infty.
\]
Therefore both corresponding sums are finite almost surely.

The functions \(t\mapsto X_{\pi_j(t)}\), restricted to \(T_*\), converge uniformly almost surely, because consecutive differences are at most \(A_j\). For each fixed \(t\in T_*\), increment control also gives \(X_{\pi_j(t)}\to X_t\) in \(L^1\), hence in probability. Uniqueness of a probability limit identifies the uniform limit with \(X_t\), simultaneously on the countable set \(T_*\).

If \(s,t\in T_*\) and \(d(s,t)\leq\rho_j\), then \(d(\pi_j(s),\pi_j(t))\leq3\rho_j\), so
\[
|X_s-X_t|\leq2\sum_{l>j}A_l+B_j.
\]
The right side tends to zero almost surely. Thus the paths on \(T_*\) are uniformly continuous. Their suprema are integrable, since
\[
\sup_{t\in T_*}|X_t|\leq\max_{u\in T_1}|X_u|+\sum_{j\geq2}A_j,
\]
and the finite maximum has finite expectation.

The public simultaneous separability condition now identifies every coordinate outside \(T_*\) with the continuous extension from the separability set, on one common event. Hence the original process, not merely a coordinatewise modification, has uniformly continuous paths and an integrable absolute supremum. Applying this fact to each of the finitely many observations gives
\[
\sup_w|G(w,S)|\leq\frac1n\sum_{i=1}^n\sup_w|\bar\ell(w,Z_i)|\in L^1.
\]
For the prescribed representatives \(W_m=t_{[W]_m}\), the covering condition gives \(d(W_m,W)\leq e2^{-m}\). Uniform continuity on the common sample event therefore gives \(G(W_m,S)\to G(W,S)\) almost surely and in \(L^1\). This argument permits arbitrary dependence of \(W\) on the sample.

## 4. Finite-depth chaining under the original cell laws

If \(e=0\), then \(\mathcal W\) is a singleton: its diameter is at most twice every positive one-ball covering radius. The learner is deterministic, \(\mathbb EG(W,S)=0\), and every cell variable is constant. The series in the target is finite and its prefactor is zero, so the conclusion holds.

Assume \(e>0\). Fix \(\eta>0\). By the definition of the infimum \(e\), choose a deterministic \(w_\eta\in\mathcal W\) such that
\[
\sup_{w\in\mathcal W}d(w,w_\eta)\leq e+\eta.
\]
No attainment of the optimal radius is assumed. Set \(U_k=[W]_k\), \(W_k=t_{U_k}\) for \(k\geq1\), and use \(w_\eta\) as the initial anchor. Define
\[
\Delta_1=G(W_1,S)-G(w_\eta,S),\qquad
\Delta_k=G(W_k,S)-G(W_{k-1},S)\quad(k\geq2),
\]
and
\[
\delta_1=e+\eta,\qquad \delta_k=e2^{-(k-1)}\quad(k\geq2).
\]
For \(k\geq2\), the representative \(W_k\) belongs to its parent cell, which is covered by the ball centered at \(W_{k-1}\) of radius \(\delta_k\). Thus \(d(W_k,W_{k-1})\leq\delta_k\). The first-scale bound follows from the choice of \(w_\eta\). This avoids adding a singleton-\(\mathcal P_0\) assumption.

For every finite \(m\), without assuming eventual exact reproduction of \(W\),
\[
G(W_m,S)=G(w_\eta,S)+\sum_{k=1}^m\Delta_k.
\]
The deterministic baseline has expectation zero.

At scale \(k\), let \(P_k=P_{U_k,S}\) and \(Q_k=P_{U_k}\otimes P_S\). A finite-valued variable has joint law absolutely continuous with respect to this product law. More explicitly, for every positive-probability cell \(u\), the likelihood ratio is \(p(u\mid s)/p(u)\), and is bounded by \(1/p(u)\). Consequently \(I_{f_\theta}(U_k;S)<\infty\) at each fixed scale. Null-probability cells contribute nothing.

Under \(Q_k\), condition on \(U_k\). Both representatives defining \(\Delta_k\) are now fixed, because the parent is a deterministic function of the child cell; at the first scale the other representative is the deterministic anchor. The variables
\[
X_i=\frac{\bar\ell(u,Z_i)-\bar\ell(v,Z_i)}{\delta_k}
\]
are conditionally independent, centered, and satisfy \(\mathbb E\exp(|X_i|^\theta)\leq2\). Coincident representatives give zero increments and cause no difficulty. Section 1 therefore proves
\[
\mathbb E_{Q_k}\exp\left(\left[\frac{\sqrt n|\Delta_k|}{K_\theta\delta_k}\right]^\theta\right)\leq2.
\]
Apply Section 2 with \(r=\sqrt n|\Delta_k|/(K_\theta\delta_k)\) to obtain
\[
\mathbb E|\Delta_k|
\leq\frac{M_\theta\delta_k}{\sqrt n}
\left(2^q I_{f_\theta}(U_k;S)+4\right).
\]
Thus
\[
\mathbb EG(W_m,S)
\leq\frac{eM_\theta}{\sqrt n}\sum_{k=1}^m2^{-(k-1)}
\left(2^qI_{f_\theta}(U_k;S)+4\right)
+\frac{\eta M_\theta}{\sqrt n}\left(2^qI_{f_\theta}(U_1;S)+4\right).
\]

## 5. Limits and the finiteness conclusion

Section 3 permits \(m\to\infty\) on the left in \(L^1\). The nonnegative partial sums on the right converge monotonically, possibly to infinity. The first-scale information is finite, so then letting \(\eta\downarrow0\) proves
\[
\mathbb EG(W,S)\leq\frac{eM_\theta}{\sqrt n}
\sum_{k=1}^\infty2^{-(k-1)}
\left(2^{1/\theta}I_{f_\theta}([W]_k;S)+4\right).
\]
The geometric weights sum to \(2\), not \(1\). Therefore the constant portion of the series is \(8\), and the right side is finite whenever the weighted information series converges. No condition on the ordinary mutual information of the unquantized learner was used.

Scale-by-scale finiteness is not enough. For example, with a uniform observation on \([0,1]\), the deterministic learner \(W=Z_1\), zero loss, the Euclidean metric, and \(\theta=2\), choose successively refining equal-interval partitions with \(2^{4^k}\) cells. They satisfy the required radius upper bounds and may use midpoint representatives. Each information is finite and equals \([\log(2^{4^k}+A)]^{1/2}\), but the geometrically weighted series diverges. This explains why the public corollary requires summability rather than merely finite information at every level.

All theorem-critical obligations are closed by the arguments above. No unresolved private reference-proof dependency remains.
