# Reference Proof

## Proof Structure

Fix an instance and condition on the observed data and selection-performance level. The deployed model-selection draw and each Rashomon draw induce Bernoulli decisions at the instance. A binary case split gives the epistemic-error lower bound. The empirical positive and negative decision frequencies converge by the Law of Large Numbers, and the minimum converges by the Continuous Mapping Theorem. Concavity of the pointwise minimum (equivalently, Jensen's inequality) yields finite-sample downward bias.

## Complete Proof

Write
\[
\pi_1=\mathbb P_H(\widehat d_H(x)=1),\qquad
\pi_0=\mathbb P_H(\widehat d_H(x)=0),
\]
so that \(\pi_0+\pi_1=1\), and let \(\theta=\min\{\pi_1,\pi_0\}\). The true decision \(d(x)\) is binary. If \(d(x)=0\), then an epistemic error occurs exactly when the deployed draw predicts one, hence
\[
\mathbb P_H(\widehat d_H(x)\ne d(x))=\pi_1\ge \min\{\pi_1,\pi_0\}=\theta.
\]
If \(d(x)=1\), the error probability is \(\pi_0\), and the same inequality follows. Thus the claimed lower bound holds in both cases.

For an iid Rashomon sample \(H_1,\ldots,H_n\), define
\[
\widehat\pi_{n,1}=\frac1n\sum_{j=1}^n\mathbf 1\{\widehat d_{H_j}(x)=1\},\qquad
\widehat\pi_{n,0}=\frac1n\sum_{j=1}^n\mathbf 1\{\widehat d_{H_j}(x)=0\},
\]
and \(\widehat\theta_n=\min\{\widehat\pi_{n,1},\widehat\pi_{n,0}\}\). Each summand in the first (respectively second) average is iid Bernoulli with mean \(\pi_1\) (respectively \(\pi_0\)). The Law of Large Numbers therefore gives \(\widehat\pi_{n,1}\to\pi_1\) and \(\widehat\pi_{n,0}\to\pi_0\) in probability. Since \((u,v)\mapsto\min\{u,v\}\) is continuous, the Continuous Mapping Theorem gives \(\widehat\theta_n\to\theta\) in probability.

Finally, the minimum function is concave, so Jensen's inequality gives
\[
\mathbb E[\widehat\theta_n]
=\mathbb E[\min\{\widehat\pi_{n,1},\widehat\pi_{n,0}\}]
\le \min\{\mathbb E\widehat\pi_{n,1},\mathbb E\widehat\pi_{n,0}\}
=\min\{\pi_1,\pi_0\}=\theta,
\]
where the last equality uses linearity of expectation and the iid common selection distribution. Hence the estimator is downward biased for every finite sample size and is consistent asymptotically.
