# Problem

## Setup

Fix \(A>0\). Let \(\mathcal P([0,A])\) denote the Borel probability measures on \([0,A]\), and let \(\mathbb N_0=\{0,1,2,\ldots\}\). For \(G\in\mathcal P([0,A])\), let
\[
p_G(x)=\int_0^A e^{-\theta}\frac{\theta^x}{x!}\,dG(\theta),\qquad x\in\mathbb N_0.
\]
The data are generated from an arbitrary test prior \(G_0\in\mathcal P([0,A])\): independently draw \(\theta_i\sim G_0\) and then \(X_i\mid\theta_i\sim\operatorname{Poisson}(\theta_i)\), independently over \(i=1,\ldots,n\). Let
\[
\theta_{G_0}(x)=\mathbb E_{G_0}[\theta\mid X=x]
\]
be the oracle posterior mean when \(p_{G_0}(x)>0\), and set \(\theta_{G_0}(x)=0\) otherwise. Define the regret of an estimator \(\widehat\theta:\mathbb N_0^n\to[0,A]^n\) by
\[
\mathcal R_n(\widehat\theta;G_0)=\frac1n\sum_{i=1}^n\mathbb E_{G_0}\big[(\widehat\theta_i(X_1,\ldots,X_n)-\theta_{G_0}(X_i))^2\big].
\]

For a constant \(c_0>0\) and each integer \(n\ge3\), set
\[
k=\left\lceil c_0\frac{\log n}{\log\log n}\right\rceil,
\]
where logarithms are natural. Draw locations \(\mu_1,\ldots,\mu_k\) independently and uniformly on \([0,A]\), draw \(W=(W_1,\ldots,W_k)\sim\operatorname{Dirichlet}(1,\ldots,1)\) independently of the locations, and put \(G=\sum_{j=1}^kW_j\delta_{\mu_j}\). Denote the resulting law of \(G\) by \(\Pi_n\).

Define the hierarchical Bayes estimator by the following model: first draw \(G\sim\Pi_n\), then draw \(\theta_1,\ldots,\theta_n\mid G\stackrel{\mathrm{iid}}\sim G\), and then draw the observations conditionally independently with \(X_i\mid\theta_1,\ldots,\theta_n,G\sim\operatorname{Poisson}(\theta_i)\). Set
\[
\widehat\theta_i(X_1,\ldots,X_n)=\mathbb E[\theta_i\mid X_1,\ldots,X_n]
\]
under this hierarchical model. The regret is evaluated under the test experiment with prior \(G_0\), not under this hierarchical model.

## Task

Prove that there is an absolute constant \(c_*>0\) such that, for every \(A>0\) and every \(c_0\ge c_*\), there are constants \(C(A,c_0)>0\) and an integer \(n_0(A,c_0)\ge3\) for which, for every integer \(n\ge n_0(A,c_0)\),
\[
\sup_{G_0\in\mathcal P([0,A])}\mathcal R_n(\widehat\theta;G_0)
\le C(A,c_0)\frac{\log^3 n}{n(\log\log n)^2}.
\]
