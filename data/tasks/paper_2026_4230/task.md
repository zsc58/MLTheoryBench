# Problem

## Setup

Let \(x_1,\ldots,x_N\in\mathbb R^P\) be mean-centered training inputs (\(\sum_n x_n=0\)) and let observations satisfy
\[
y_n=\theta^\top x_n+\varepsilon_n,\qquad \varepsilon_n\stackrel{\mathrm{iid}}\sim N(0,\sigma^2),
\]
with known \(\sigma^2>0\). Assume the prior \(\theta\sim N(0,\alpha^{-1}I_P)\) with \(\alpha>0\). Write \(X\in\mathbb R^{N\times P}\) for the design matrix with rows \(x_n^\top\), and \(Y=(y_1,\ldots,y_N)^\top\).

The exact posterior is \(N(\mu,\Sigma)\), where
\[
\Sigma=(X^\top X/\sigma^2+\alpha I_P)^{-1},\qquad
\mu=\Sigma X^\top Y/\sigma^2.
\]
Fix an orthonormal basis \(e_1,\ldots,e_P\) of parameter space. Mean-field variational inference is the reverse-KL projection of this posterior onto Gaussian distributions \(N(m,S)\) whose covariance has the form
\[
S=\sum_{p=1}^P d_p e_pe_p^\top,\qquad d_p>0.
\]
Let \(S^*\) denote the covariance of an optimizer. Define the empirical input covariance \(\widehat\Gamma=N^{-1}X^\top X\), and let \(\widehat p=N^{-1}\sum_{n=1}^N\delta_{x_n}\).

For a parameter covariance \(C\), define the empirical average total predictive variance by
\[
V(C)=\mathbb E_{x\sim\widehat p}[\sigma^2+x^\top Cx]
=\sigma^2+\operatorname{Tr}(\widehat\Gamma C).
\]

## Task

Prove that
\[
V(S^*)\ge V(\Sigma),
\]
equivalently,
\[
\mathbb E_{x\sim\widehat p}\!\left[x^\top\Sigma x-x^\top S^*x\right]\le 0.
\]
