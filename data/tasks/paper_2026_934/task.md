# Problem

## Setup

Let \(d,q,p\) be positive integers. Let \(\varepsilon_U,\varepsilon_Y,\varepsilon_X\) be mutually independent structural noises with a fixed joint law, and let \(f_0,g_0\) be fixed measurable functions such that
\[
U=\varepsilon_U\in\mathbb R^q,\qquad
Y=g_0(U,\varepsilon_Y)\in\mathbb R,\qquad
Z=f_0(Y,U,\varepsilon_X)\in\mathbb R^d.
\]
Assume
\[
\mathbb E[Y]=0,\qquad \mathbb E[Z]=0,\qquad
\mathbb E[Y^2]<\infty,\qquad \mathbb E[\|Z\|_2^2]<\infty.
\]
An environment \(e\) specifies a perturbation \(\varepsilon_e\in\mathbb R^d\), independent of the structural noises, and the covariate vector is
\[
X=Z+\varepsilon_e.
\]
Only the perturbation law varies across environments. Let \(\mathcal E\) contain an environment for every probability distribution on \(\mathbb R^d\) with finite second moment, with every environment in \(\mathcal E\) having such a perturbation law. Write \(\mathbb E^e\) for expectation in environment \(e\), and define
\[
M_e=\mathbb E^e[\varepsilon_e\varepsilon_e^\top].
\]

Let \(\mathcal E^{\mathrm{tr}}=\{e_1,\ldots,e_p\}\subseteq\mathcal E\) be the training environments, and let \(\varnothing\ne\mathcal L\subseteq\mathcal E^{\mathrm{tr}}\) be the labeled subset. Covariate observations are available from every training environment, whereas joint covariate-outcome observations are available from the labeled subset. All objectives below are population objectives.

Define
\[
\bar M=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}M_e,
\qquad
\mu_i=\mathbb E^{e_i}[\varepsilon_{e_i}],
\qquad
\bar\mu=\frac1p\sum_{i=1}^p\mu_i,
\]
\[
V=\frac1p\sum_{i=1}^p(\mu_i-\bar\mu)(\mu_i-\bar\mu)^\top.
\]
Also define the matrix of training covariate means and its covariance by
\[
K=[\mathbb E^{e_1}X,\ldots,\mathbb E^{e_p}X],\qquad
H=\frac1pKK^\top-
\left(\frac1pK\mathbf 1_p\right)
\left(\frac1pK\mathbf 1_p\right)^\top,
\]
where \(\mathbf 1_p\in\mathbb R^p\) is the vector of ones.

For a finite real parameter \(\gamma\ge0\), set
\[
\Delta_\gamma=\{A\in\mathbb R^{d\times d}:A=A^\top,\ 0\preceq A\preceq\gamma V\},
\]
where \(\preceq\) is the positive-semidefinite order, and set
\[
\mathcal E_\gamma=\{e\in\mathcal E:M_e=\bar M+A\text{ for some }A\in\Delta_\gamma\}.
\]
Let \(\beta_\gamma\) be any minimizer over \(\beta\in\mathbb R^d\) of
\[
\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[(Y-\beta^\top X)^2]
+\gamma\beta^\top H\beta.
\]

## Task

Prove that, for every \(\beta\in\mathbb R^d\),
\[
\sup_{e\in\mathcal E_\gamma}\mathbb E^e[(Y-\beta^\top X)^2]
=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[(Y-\beta^\top X)^2]
+\gamma\beta^\top H\beta,
\]
and consequently every such \(\beta_\gamma\) minimizes the worst-case squared-error risk over \(\mathcal E_\gamma\).
