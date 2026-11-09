# Reference Proof

## Proof Structure

For each allocation, isolate the smallest pairwise rate in the weighted log-sum-exp expression. Bound the remaining normalized sum using the smallest and largest challenger weights. Subexponentiality then gives uniform convergence. Continuity and compactness guarantee existence of surrogate maximizers, and uniqueness of the hard-minimum maximizer identifies every possible limiting allocation.

## Complete Proof

The constrained rate definitions use
\[
D_i(v;\theta_i)=A_i(\theta_i)-A_i(v)-A_i'(v)(\theta_i-v),
\]
which is the source divergence \(d_i(v,\theta_i)\). The minima are assumed finite and attained. Their continuity is also an assumption; neither computation of the projections nor an envelope argument is needed for the conclusions below. The term large-deviation-optimal allocation designates the stipulated unique maximizer of the hard-minimum objective; no separate probability-asymptotic characterization is used in this proof.

Because there are finitely many challengers and every \(C_{b,j}\) is real-valued and continuous on the simplex,
\[
m(p)=\min_{j\ne b}C_{b,j}(p)
\]
is real-valued and continuous. For each fixed \(t>0\), the sum defining \(F_t\) is a finite, strictly positive, continuous function of \(p\). Thus \(F_t\) is continuous. The closed simplex is nonempty and compact, so \(F_t\) attains its maximum for every \(t>0\).

Define
\[
S_t(p)=\sum_{j\ne b}\rho_{j,t}\exp\{-t(C_{b,j}(p)-m(p))\}.
\]
Every rate gap is nonnegative, and at least one challenger attains the minimum defining \(m(p)\). Hence at least one exponential factor equals one, while all exponential factors are at most one. Consequently,
\[
\min_{j\ne b}\rho_{j,t}\le S_t(p)\le (K-1)\max_{j\ne b}\rho_{j,t}.
\]
With
\[
L_t=\max_{j\ne b}|\log\rho_{j,t}|,
\]
this implies
\[
-L_t\le\log S_t(p)\le L_t+\log(K-1),
\qquad
|\log S_t(p)|\le L_t+\log(K-1).
\]
Factoring out the minimum rate gives
\[
F_t(p)=m(p)-\frac1t\log S_t(p).
\]
Therefore
\[
\varepsilon_t:=\sup_{p\in\Delta^{K-1}}|F_t(p)-m(p)|
\le\frac{L_t+\log(K-1)}{t}\longrightarrow0.
\]
This proves uniform convergence. The same argument applies when \(K=2\), in which case \(\log(K-1)=0\), and when allocations or pairwise rates vanish: no allocation coordinate or rate is divided by in this argument.

Now choose any \(p_t\in\arg\max_{p\in\Delta^{K-1}}F_t(p)\). By maximality and uniform approximation,
\[
m(p_t)\ge F_t(p_t)-\varepsilon_t
\ge F_t(p^\star)-\varepsilon_t
\ge m(p^\star)-2\varepsilon_t.
\]
To establish the limit for real \(t\to\infty\), suppose it fails. There would then be a number \(\delta>0\) and a sequence \(t_n\to\infty\) such that
\[
\|p_{t_n}-p^\star\|_2\ge\delta
\]
for every \(n\). Compactness supplies a convergent subsequence \(p_{t_{n_k}}\to\bar p\) in the simplex. Continuity of \(m\), the displayed near-optimality inequality, and \(\varepsilon_{t_{n_k}}\to0\) give
\[
m(\bar p)\ge m(p^\star).
\]
Since \(p^\star\) maximizes \(m\), equality holds. Its uniqueness forces \(\bar p=p^\star\), contradicting the distance bound. Thus \(p_t\to p^\star\) for every choice of surrogate maximizers.

## Proof-Obligation Closure

- Rate well-definedness and continuity are explicit assumptions, not conclusions imported from projection regularity.
- Surrogate well-definedness and existence of maximizers follow from positivity, continuity, and compactness, as verified above.
- The normalized-sum bounds and uniform convergence are derived explicitly.
- Maximizer convergence is proved for arbitrary choices and arbitrary diverging real annealing levels.
- No specialized external result or unresolved paper-specific dependency is used.
