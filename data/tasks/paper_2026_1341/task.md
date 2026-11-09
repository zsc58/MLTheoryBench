# Problem

## Setup

Fix integers \(E,p,k\) with \(E\ge 1\) and \(1\le k<p\). There are \(E\) source domains indexed by \(e\in\{1,\ldots,E\}\). Domain \(e\) supplies a zero-mean random row vector \(x_e\in\mathbb R^{1\times p}\) with covariance \(\Sigma_e=\mathbb E[x_e^\top x_e]\succeq0\) and \(\operatorname{tr}(\Sigma_e)>0\). Domain weights are positive and sum to one. Let
\[
\mathcal O_{p\times k}=\{V\in\mathbb R^{p\times k}:V^\top V=I_k\},\qquad P_V=VV^\top .
\]
For a zero-mean distribution \(Q\) with covariance \(\Sigma_Q\), define explained variance and reconstruction loss
\[
v_Q(V)=\operatorname{tr}(V^\top\Sigma_QV),\qquad r_Q(V)=\operatorname{tr}((I-P_V)\Sigma_Q).
\]
Let \(r_Q^*=\min_{W\in\mathcal O_{p\times k}}r_Q(W)\) and regret \(g_Q(V)=r_Q(V)-r_Q^*\). Subscript \(e\) denotes these quantities for source domain \(e\).

Define the unnormalized uncertainty set
\[
\mathcal C=\operatorname{conv}\{\Sigma_1,\ldots,\Sigma_E\},\qquad
\mathcal P=\{Q:Q\text{ is zero-mean and }\Sigma_Q\in\mathcal C\}.
\]
Set \(\bar\Sigma_e=\Sigma_e/\operatorname{tr}(\Sigma_e)\), \(\mathcal C_{\rm norm}=\operatorname{conv}\{\bar\Sigma_1,\ldots,\bar\Sigma_E\}\), and for any \(Q\) with positive covariance trace set \(\bar\Sigma_Q=\Sigma_Q/\operatorname{tr}(\Sigma_Q)\). Define \(\bar v_Q,\bar r_Q,\bar g_Q\) exactly as \(v_Q,r_Q,g_Q\) with \(\Sigma_Q\) replaced by \(\bar\Sigma_Q\), and let
\[
\mathcal P_{\rm norm}=\{Q:Q\text{ is zero-mean, }\operatorname{tr}(\Sigma_Q)>0,\ \bar\Sigma_Q\in\mathcal C_{\rm norm}\}.
\]

## Task

Prove the following integrated theorem. For every \(V\in\mathcal O_{p\times k}\),
\[
\inf_{Q\in\mathcal P}v_Q(V)=\min_e v_e(V),\qquad
\sup_{Q\in\mathcal P}r_Q(V)=\max_e r_e(V),\qquad
\sup_{Q\in\mathcal P}g_Q(V)=\max_e g_e(V).
\]
Moreover, any matrix maximizing \(\min_e v_e(V)\), any matrix minimizing \(\max_e r_e(V)\), and any matrix minimizing \(\max_e g_e(V)\) is respectively optimal for the corresponding minimax problem over \(\mathcal P\): maximize \(\inf_{Q\in\mathcal P}v_Q(V)\), minimize \(\sup_{Q\in\mathcal P}r_Q(V)\), and minimize \(\sup_{Q\in\mathcal P}g_Q(V)\).

The same equalities and optimizer conclusions hold for the normalized quantities over \(\mathcal P_{\rm norm}\):
\[
\inf_{Q\in\mathcal P_{\rm norm}}\bar v_Q(V)=\min_e\bar v_e(V),\qquad
\sup_{Q\in\mathcal P_{\rm norm}}\bar r_Q(V)=\max_e\bar r_e(V),\qquad
\sup_{Q\in\mathcal P_{\rm norm}}\bar g_Q(V)=\max_e\bar g_e(V),
\]
with source optimizers corresponding to the three normalized objectives being optimal for these normalized minimax problems.
