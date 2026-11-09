# Reference Proof

Let \(Q_e\) denote the law of the source random vector \(x_e\), and let \(P_V=VV^\top\). For any zero-mean distribution \(Q\) with covariance \(\Sigma_Q\), put
\[
v_Q(V)=\operatorname{tr}(V^\top\Sigma_QV),\qquad
r_Q(V)=\operatorname{tr}((I-P_V)\Sigma_Q),
\]
and let \(r_Q^*=\min_{W\in\mathcal O_{p\times k}}r_Q(W)\) and \(g_Q(V)=r_Q(V)-r_Q^*\). Since \(P_V\) is an orthogonal projector,
\[
r_Q(V)=\operatorname{tr}(\Sigma_Q)-v_Q(V).
\]

Take \(Q\in\mathcal P\). By definition, there are numbers \(\mu_e\ge 0\) with \(\sum_e\mu_e=1\) such that
\[
\Sigma_Q=\sum_e\mu_e\Sigma_e.
\]
Therefore, for every \(V\),
\[
v_Q(V)=\sum_e\mu_ev_e(V),\qquad r_Q(V)=\sum_e\mu_er_e(V).
\]
Consequently,
\[
v_Q(V)\ge \min_e v_e(V),\qquad r_Q(V)\le \max_e r_e(V).
\]
Taking the infimum or supremum over \(Q\) gives the corresponding inequalities. Each source law \(Q_e\) belongs to \(\mathcal P\), because it is zero-mean and has covariance \(\Sigma_e\). Since the index set is finite, a source index attains each displayed minimum or maximum. Hence
\[
\inf_{Q\in\mathcal P}v_Q(V)=\min_e v_e(V),\qquad
\sup_{Q\in\mathcal P}r_Q(V)=\max_e r_e(V).
\]

For regret, using the same covariance decomposition gives
\[
r_Q^*=\min_W\sum_e\mu_er_e(W)\ge \sum_e\mu_e\min_Wr_e(W)=\sum_e\mu_er_e^*.
\]
Thus
\[
g_Q(V)=r_Q(V)-r_Q^*
\leq \sum_e\mu_e(r_e(V)-r_e^*)
=\sum_e\mu_eg_e(V)\leq \max_eg_e(V).
\]
Taking the supremum over \(Q\in\mathcal P\) gives one inequality. The reverse inequality follows because every source law \(Q_e\) is in \(\mathcal P\), so a source index attaining \(\max_eg_e(V)\) supplies a member of the uncertainty class with that regret. Therefore
\[
\sup_{Q\in\mathcal P}g_Q(V)=\max_eg_e(V).
\]

The three identities hold for every \(V\). Hence any maximizer of \(\min_ev_e(V)\), any minimizer of \(\max_er_e(V)\), and any minimizer of \(\max_eg_e(V)\) respectively maximizes \(\inf_{Q\in\mathcal P}v_Q(V)\), minimizes \(\sup_{Q\in\mathcal P}r_Q(V)\), and minimizes \(\sup_{Q\in\mathcal P}g_Q(V)\).

For the normalized assertions, write \(\bar\Sigma_e=\Sigma_e/\operatorname{tr}(\Sigma_e)\). If \(Q\in\mathcal P_{\rm norm}\), then by definition there are \(\mu_e\ge0\), \(\sum_e\mu_e=1\), such that
\[
\bar\Sigma_Q=\sum_e\mu_e\bar\Sigma_e.
\]
The normalized quantities are the same trace expressions with \(\Sigma_Q\) replaced by \(\bar\Sigma_Q\). In particular, if
\[
\bar r_Q^*=\min_W\bar r_Q(W),\qquad \bar g_Q(V)=\bar r_Q(V)-\bar r_Q^*,
\]
then the preceding linearity argument gives
\[
\bar v_Q(V)=\sum_e\mu_e\bar v_e(V),\qquad
\bar r_Q(V)=\sum_e\mu_e\bar r_e(V),
\]
and
\[
\bar r_Q^*\geq\sum_e\mu_e\bar r_e^*.
\]
Therefore
\[
\bar v_Q(V)\geq\min_e\bar v_e(V),\qquad
\bar r_Q(V)\leq\max_e\bar r_e(V),\qquad
\bar g_Q(V)\leq\max_e\bar g_e(V).
\]
Every source law \(Q_e\) belongs to \(\mathcal P_{\rm norm}\), because \(\operatorname{tr}(\Sigma_e)>0\) and its normalized covariance is \(\bar\Sigma_e\). Source inclusion gives the reverse inequalities, so
\[
\inf_{Q\in\mathcal P_{\rm norm}}\bar v_Q(V)=\min_e\bar v_e(V),\qquad
\sup_{Q\in\mathcal P_{\rm norm}}\bar r_Q(V)=\max_e\bar r_e(V),\qquad
\sup_{Q\in\mathcal P_{\rm norm}}\bar g_Q(V)=\max_e\bar g_e(V).
\]
Since these identities also hold for every \(V\), the corresponding normalized source optimizers are minimax-optimal over \(\mathcal P_{\rm norm}\).
