# Problem

## Setup

Fix an integer dimension \(D\ge1\). Vectors lie in \(\mathbb R^D\). For bipolar vectors, coordinates are in \(\{-1,1\}\). Define coordinatewise binding by \((x\odot y)_i=x_i y_i\); for bipolar keys this operation is self-inverse. Define cleanup by
\[
\operatorname{sign}(x)=\begin{cases}1,&x>0,\\0,&x=0,\\-1,&x<0,\end{cases}
\]
coordinatewise.

Let \(K\in\{-1,1\}^D\) be a key and \(V\in\{-1,1\}^D\) a stored value, and set \(H=K\odot V\). Given noise \(N\), restoration produces
\[
\widetilde V=\operatorname{sign}(H+N)\odot K.
\]
Assume \(H\) is uniform bipolar and independent of \(N\). Define
\(\operatorname{CosSim}(x,y)=\langle x,y\rangle/(\|x\|\|y\|)\) when \(x\ne0\) and \(y\ne0\), and define it to be zero otherwise. In every target expression below, the second argument is bipolar and hence nonzero.

Consider two noise models:

1. **Normalized bipolar noise:** the coordinates of \(N\) are independent uniform signs (so \(\|N\|=\sqrt D\)).
2. **Gaussian noise:** the coordinates of \(N\) are independent \(\mathcal N(0,\sigma^2)\) variables for a fixed \(\sigma>0\).

## Task

Prove the following single-signal recovery contract. In the normalized bipolar-noise model, if \(K_D\) denotes the number of coordinates on which \(N\) and \(H\) agree, then \(K_D\sim\operatorname{Binomial}(D,1/2)\),
\[
\operatorname{CosSim}(\widetilde V,V)=\sqrt{K_D/D},
\qquad
\mathbb E[\operatorname{CosSim}(\widetilde V,V)]\longrightarrow\frac1{\sqrt2}\quad(D\to\infty),
\]
and, for every \(0<\varepsilon<1/\sqrt2\),
\[
\Pr\left(\left|\operatorname{CosSim}(\widetilde V,V)-\frac1{\sqrt2}\right|\ge\varepsilon\right)
\le2\exp\{-2D\varepsilon^2(\sqrt2-\varepsilon)^2\}.
\]
In the Gaussian-noise model,
\[
\mathbb E[\operatorname{CosSim}(\widetilde V,V)]=2\Phi(1/\sigma)-1,
\]
where \(\Phi\) is the standard normal CDF, and for every \(\varepsilon>0\),
\[
\Pr\left(\left|\operatorname{CosSim}(\widetilde V,V)-[2\Phi(1/\sigma)-1]\right|\ge\varepsilon\right)
\le2e^{-D\varepsilon^2/2}.
\]
