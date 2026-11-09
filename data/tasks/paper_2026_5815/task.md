# Problem

## Setup

Let \((\Theta,\mathcal B_\Theta)\) be a standard Borel parameter space and let \(\mathcal U\) be a standard Borel quotient space. A measurable group \(G\) acts on \(\Theta\), with measurable quotient map \(\pi:\Theta\to\mathcal U=\Theta/G\). Let \(Z\) have distribution \(\mathcal D\), let \(S=(Z_1,\ldots,Z_n)\sim\mathcal D^n\) with \(n\ge1\), and let the loss \(\ell(f_\theta,z)\in[0,1]\) be measurable. Define
\[
R(\theta)=\mathbb E_{Z\sim\mathcal D}\ell(f_\theta,Z),\qquad
\widehat R_S(\theta)=\frac1n\sum_{i=1}^n\ell(f_\theta,Z_i).
\]
Assume the symmetry is predictor-preserving: \(f_{g\cdot\theta}=f_\theta\) for every \(g\in G\), and there is a measurable quotient predictor \(\bar f_u\) satisfying \(f_\theta=\bar f_{\pi(\theta)}\). Let \(P\) be a prior on \(\Theta\), independent of \(S\), and let \(Q\) be a (possibly sample-dependent) posterior with \(Q\ll P\). Write \(\bar P=\pi_\#P\), \(\bar Q=\pi_\#Q\), and define quotient risks \(\bar R(u)=\mathbb E_Z\ell(\bar f_u,Z)\) and \(\widehat{\bar R}_S(u)=n^{-1}\sum_i\ell(\bar f_u,Z_i)\). For regular conditional probabilities over the fibers, define
\[
\Delta_\pi:=\int_{\mathcal U}\mathrm{KL}\!\left(Q(\cdot\mid u)\middle\|P(\cdot\mid u)\right)\,\bar Q(du).
\]
Let
\[
C_{n,\delta}(k)=\sqrt{\frac{k+\log(1/\delta)+\log n+2}{2n-1}},\qquad C_{n,\delta}(\infty)=\infty,
\]
for \(\delta\in(0,1)\).

## Task

Prove that, with probability at least \(1-\delta\) over \(S\),
\[
\mathbb E_{\bar Q}\bar R\le \mathbb E_{\bar Q}\widehat{\bar R}_S+C_{n,\delta}\!\left(\mathrm{KL}(\bar Q\|\bar P)\right),
\]
\[
\mathbb E_{\bar Q}\bar R=\mathbb E_QR,\qquad
\mathbb E_{\bar Q}\widehat{\bar R}_S=\mathbb E_Q\widehat R_S,
\]
and
\[
\mathrm{KL}(Q\|P)=\mathrm{KL}(\bar Q\|\bar P)+\Delta_\pi,\qquad \Delta_\pi\ge0.
\]
Consequently the quotient certificate is no larger than
\[
\mathbb E_Q\widehat R_S+C_{n,\delta}(\mathrm{KL}(Q\|P)).
\]
When \(\mathrm{KL}(Q\|P)<\infty\), the KL reduction can equivalently be written \(\mathrm{KL}(\bar Q\|\bar P)=\mathrm{KL}(Q\|P)-\Delta_\pi\).
