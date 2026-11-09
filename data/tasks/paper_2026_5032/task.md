# Problem

## Setup

There are integers \(K\ge2\) arms and \(d\ge1\) objectives. For each arm \(a\), let \(Y_{a,1},Y_{a,2},\ldots\) be i.i.d. reward vectors in \([0,1]^d\), with mean \(\mu_a\in[0,1]^d\). These sequences are independent across arms. At round \(t\), a policy chooses \(A_t\) and observes the entire next unused reward vector from that arm, and no reward from any other arm. Policies may know \(K,d,T\), but their choices must be measurable functions of the previously observed arm/reward history and, if randomized, internal randomness independent of all reward sequences. The decision rules are the same across instances and do not have access to the unknown reward distributions or their means.

Let \(N_a(t)=\sum_{s=1}^t\mathbf1\{A_s=a\}\). Whenever \(N_a(t)>0\), let \(\widehat\mu_{a,j}(t)\) be the average of the observed objective-\(j\) rewards from arm \(a\) through round \(t\).

For vectors in \(\mathbb R^d\), \(x\succeq y\) means coordinatewise domination and \(x\succ y\) means domination with at least one strict coordinate. Arm \(a\) is Pareto-optimal if no arm has mean strictly dominating \(\mu_a\); let \(A^\star\) be the Pareto set. With \(\mathbf1\in\mathbb R^d\) denoting the all-ones vector, define
\[
\Delta_a^P=\inf\{\varepsilon\ge0:\ \nexists b\in\{1,\ldots,K\}\text{ with }\mu_b\succ\mu_a+\varepsilon\mathbf1\},\qquad
R_T^P=\sum_{t=1}^T\Delta_{A_t}^P,
\]
and \(\Delta_{\max}^P=\max_a\Delta_a^P\).

For each objective \(j\), let \(m_j=\max_a\mu_{a,j}\), \(M_j=\arg\max_a\mu_{a,j}\), and \(\Delta_a^{(j)}=m_j-\mu_{a,j}\). If \(M_j\) is a singleton with winner \(a_j\), set \(g_j=m_j-\max_{b\ne a_j}\mu_{b,j}\); otherwise set \(g_j=0\). Let \(j^\dagger\in\arg\max_j g_j\) and \(g^\dagger=g_{j^\dagger}\).

For the upper bound, assume \(g^\dagger>0\) and marginal-Pareto consistency: whenever \(\Delta_a^{(j)}=0\), arm \(a\) is Pareto-optimal.

Consider the following horizon-aware policy for an integer horizon \(T\ge K\). Here and throughout, \(\log\) is the natural logarithm. The policy pulls each arm once initially. At every later round \(t\), until an arm has been committed to, put
\[
\beta_a(t)=\sqrt{2\log T/N_a(t-1)},\quad U_{a,j}(t)=\widehat\mu_{a,j}(t-1)+\beta_a(t),\quad L_{a,j}(t)=\widehat\mu_{a,j}(t-1)-\beta_a(t).
\]
For each objective choose distinct arms \(b_j(t),c_j(t)\) with the largest and second-largest \(U_{a,j}(t)\), respectively. If for any objective \(j\), \(L_{b_j(t),j}(t)>U_{c_j(t),j}(t)\), commit to that arm \(b_j(t)\) and pull it on the current round and every remaining round, breaking ties between certifying objectives arbitrarily. If no objective certifies, select an objective maximizing \(\beta_{b_j(t)}(t)+\beta_{c_j(t)}(t)\), and pull whichever of its two endpoints has larger \(\beta\). All other ties may also be broken arbitrarily subject to the policy information restriction above.

For the converse, fix \(K,d\). The full stochastic bandit model consists of all independent-across-arm, i.i.d. bounded-vector reward sequences described above, without requiring marginal-Pareto consistency or \(g^\dagger>0\). Call a policy uniformly good over this full model if, for every instance \(\nu\), every arm \(a\notin A^\star(\nu)\), and every \(\alpha>0\),
\[
\mathbb E_\nu[N_a(T)]=o(T^\alpha)\qquad(T\to\infty),
\]
where \(A^\star(\nu)\) is that instance's Pareto set. This condition is imposed on the full model, not merely on the subclass below.

## Task

Prove the following integrated theorem.

1. For the specified policy, on every instance satisfying the upper-bound assumptions,
\[
\mathbb E[R_T^P]\le K\Delta_{\max}^P+\frac{64K\log T}{g^\dagger}+2Kd\,\Delta_{\max}^P T^{-2}.
\]
In particular, \(\mathbb E[R_T^P]=O(K\log T/g^\dagger)\) as \(T\to\infty\) with \(K,d\) and the reward distributions fixed.

2. Conversely, for every \(K\ge2\), every \(d\ge1\), and every \(\Delta_{\rm sc}\in(0,1/4]\), consider the duplicated-coordinate Bernoulli instance \(Y_{a,n}=Z_{a,n}\mathbf1\), where all scalar samples are independent across arms and pulls, arm 1 has mean \(1/2+\Delta_{\rm sc}\), and all other arms have mean \(1/2\). Every policy uniformly good over the full model satisfies
\[
\liminf_{T\to\infty}\frac{\mathbb E[R_T^P]}{\log T}\ge \frac{3}{8}\frac{K-1}{\Delta_{\rm sc}}.
\]
Thus no uniformly good policy can improve the \(\Omega(K\log T/g^\dagger)\) order uniformly over the full model class.
