# Problem

## Setup

Let $\gamma_d$ be the standard Gaussian probability measure on $\mathbb R^d$. For a Borel set $H\subseteq\mathbb R^d$, let
\[
\Gamma(H)=\liminf_{\delta\downarrow0}\frac{\gamma_d(H_\delta)-\gamma_d(H)}{\delta},
\]
where $H_\delta=\{x:\operatorname{dist}(x,H)\le\delta\}$. Let $\mathcal H$ be a class of Borel subsets of $\mathbb R^d$ with
\[
\Gamma_{\mathcal H}:=\sup_{H\in\mathcal H}\Gamma(H)<\infty.
\]
A non-negative $L^1$-approximating polynomial for $H$ with error $\varepsilon$ is a polynomial $q:\mathbb R^d\to\mathbb R$ such that $q(x)\ge0$ for all $x$ and
\[
\mathbb E_{x\sim\gamma_d}\left[|q(x)-\mathbf1_H(x)|\right]\le\varepsilon.
\]

## Task

Prove that for every $\varepsilon\in(0,1/2)$ and every $H\in\mathcal H$, there exists a polynomial $q:\mathbb R^d\to\mathbb R_{\ge0}$ satisfying
\[
\mathbb E_{x\sim\gamma_d}\left[|q(x)-\mathbf1_H(x)|\right]\le\varepsilon
\]
and
\[
\deg(q)\le C\,\Gamma_{\mathcal H}^{\,2}\varepsilon^{-2}\log(1/\varepsilon)
\]
for a universal constant $C$, with the degree-zero case understood when $\Gamma_{\mathcal H}=0$.
