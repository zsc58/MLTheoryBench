# Reference Proof

## Proof Structure

Prove smooth self-boundedness and a strict-separation family; derive the dual smoothness inequality; use it in the projected-gradient potential recursion, complete the square, telescope, and tune the step size; finally prove the deterministic linear-loss lower bound by Rademacher averaging.

## Complete Proof

Let $a_t=\nabla f_t(w_t)$ and $b_t=\nabla f_t(u)$.

For an $L$-smooth function, the descent lemma at $x-\nabla f(x)/L$ gives
$f(x-\nabla f(x)/L)\le f(x)-\|\nabla f(x)\|^2/(2L)$. Hence
$\|\nabla f(x)\|^2\le2L(f(x)-\inf f)$ (with the extended-real inequality automatic when $\inf f=-\infty$). Summing at $w^\star$ proves $Q_T^\star\le2LS_T^\star$.

For strictness, let $r=D/2$, $K=[-r,r]$, $T=2N$, $c_k=Lk^{-1/3}$, and
$f_{2k-1}(x)=c_k(x-r)^2/2$, $f_{2k}(x)=c_k(x+r)^2/2$. Each pair sums to $c_k(x^2+r^2)$, so $w^\star=0$. Thus
$S_{2N}^\star=r^2\sum_kc_k=\Theta(LD^2N^{2/3})$ and
$Q_{2N}^\star=2r^2\sum_kc_k^2=\Theta(L^2D^2N^{1/3})$, so $Q_{2N}^\star/(LS_{2N}^\star)\to0$.

For convex $L$-smooth $f$, let $h(z)=f(z)-\langle\nabla f(y),z\rangle$. Since $\nabla h(y)=0$, the descent lemma gives
$f(x)-f(y)-\langle\nabla f(y),x-y\rangle\ge\|\nabla f(x)-\nabla f(y)\|^2/(2L)$. Applying this with $x=u,y=w_t$, projection nonexpansiveness yields
\[
\|w_{t+1}-u\|^2\le\|w_t-u\|^2-2\eta(f_t(w_t)-f_t(u))-\frac\eta L\|a_t-b_t\|^2+\eta^2\|a_t\|^2.
\]
For $0<\eta<1/L$, completing the square gives
$\eta^2\|a\|^2-(\eta/L)\|a-b\|^2\le\eta^2\|b\|^2/(1-\eta L)$. Summation therefore gives
\[
R_T(u)\le\frac{D^2}{2\eta}+\frac{\eta Q_T(u)}{2(1-\eta L)}.
\]
At $u=w^\star$, choose $\eta=\min\{D/\sqrt{2Q_T^\star},1/(2L)\}$. In the second regime $Q_T^\star\le2L^2D^2$ and the bound is at most $2LD^2$; in the first regime $1/(1-\eta L)\le2$ and the bound is at most $D\sqrt{2Q_T^\star}$. Hence
$R_T(w^\star)\le\max\{2LD^2,D\sqrt{2Q_T^\star}\}$.

For the lower bound, fix a deterministic online algorithm, take $K=[-D/2,D/2]$, independent Rademacher signs $\varepsilon_t$, and losses $f_t(x)=M\varepsilon_tx$. If $S=\sum_t\varepsilon_t$, the best comparator has loss $-(DM/2)|S|$, while the learner's expected loss over signs is zero. Since $\mathbb ES^2=T$ and $\mathbb ES^4=3T^2-2T\le3T^2$, Holder interpolation gives $\mathbb E|S|\ge(\mathbb ES^2)^{3/2}/(\mathbb ES^4)^{1/2}\ge\sqrt T/2$. Therefore some fixed sign sequence has regret at least $DM\sqrt T/4$. All gradients have norm $M$, so $Q_T^\star=M^2T$ and the regret is at least $(D/4)\sqrt{Q_T^\star}$.
