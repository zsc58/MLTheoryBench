# Reference Proof

## Proof Structure

Reduce restoration to cosine similarity between a bipolar invariant and its sign-cleaned noisy sum. Analyze normalized bipolar noise by counting coordinate agreements, then analyze Gaussian noise through coordinate-wise sign-agreement probabilities. Apply Hoeffding concentration, with the square-root transfer in the bipolar case.

## Complete Proof

Let H=K\odot V. Coordinatewise multiplication by the bipolar key K preserves norms and inner products, and V=H\odot K, so
\[
\operatorname{CosSim}(\widetilde V,V)=\operatorname{CosSim}(\operatorname{sign}(H+N),H),
\qquad \widetilde V=\operatorname{sign}(H+N)\odot K.
\]

For normalized bipolar noise, each N_i is an independent uniform sign, independent of H_i. Agreement N_i=H_i has probability 1/2 and gives cleaned coordinate H_i; disagreement gives sum zero and cleaned coordinate zero. If K_D is the number of agreements, then K_D\sim\operatorname{Binomial}(D,1/2),
\[
\langle\operatorname{sign}(H+N),H\rangle=K_D,\quad
\|\operatorname{sign}(H+N)\|^2=K_D,\quad \|H\|^2=D.
\]
With cosine defined as zero when the first vector is zero,
\[
\operatorname{CosSim}(\widetilde V,V)=\sqrt{K_D/D}.
\]
Since K_D/D\to1/2 in probability and the square-root is bounded on [0,1],
\[
\mathbb E[\operatorname{CosSim}(\widetilde V,V)]\to1/\sqrt2.
\]
Hoeffding gives
\[
\Pr(|K_D/D-1/2|\ge t)\le2e^{-2Dt^2}.
\]
For 0<\varepsilon<1/\sqrt2, if |\sqrt{x}-1/\sqrt2|\ge\varepsilon, then |x-1/2|\ge\varepsilon(\sqrt2-\varepsilon). Applying this with x=K_D/D yields
\[
\Pr\left(|\operatorname{CosSim}-1/\sqrt2|\ge\varepsilon\right)
\le2\exp\{-2D\varepsilon^2(\sqrt2-\varepsilon)^2\}.
\]

For Gaussian noise, let N_i be iid \mathcal N(0,\sigma^2), independent of H. Ties have probability zero. Set
\[
Y_i=H_i\operatorname{sign}(H_i+N_i)\in\{-1,1\}.
\]
Conditionally on H_i=1, agreement has probability \Pr(N_i>-1)=\Phi(1/\sigma); symmetry gives the same conditional agreement probability for H_i=-1. Thus
\[
\mathbb EY_i=2\Phi(1/\sigma)-1=:\mu_\sigma.
\]
Both vectors have norm \sqrt D almost surely, so the cosine is D^{-1}\sum_iY_i, and its expectation is \mu_\sigma. Applying Hoeffding to independent variables in [-1,1] gives
\[
\Pr\left(|\operatorname{CosSim}-\mu_\sigma|\ge\varepsilon\right)\le2e^{-D\varepsilon^2/2},
\]
which proves the Gaussian clause.
