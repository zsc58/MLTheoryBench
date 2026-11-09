# Problem

## Setup

Let \(d\ge1\) be an integer and let \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), with Lebesgue measure of total mass one. Write \(\widehat f(k)\) for the Fourier coefficient at \(k\in\mathbb Z^d\). For \(a\in\mathbb R\), define
\[
 \|f\|_{H^a}^2=\sum_{k\in\mathbb Z^d}(1+|2\pi k|^2)^a|\widehat f(k)|^2.
\]
For zero-mean \(f\), define
\[
 \|f\|_{\dot H^a}^2=\sum_{k\in\mathbb Z^d\setminus\{0\}}|2\pi k|^{2a}|\widehat f(k)|^2.
\]
Let \(D^a\) be the Fourier multiplier \(|2\pi k|^a\) at nonzero frequencies and zero at frequency zero.

Fix \(s>1\) and \(\gamma>\max\{d/2,s-1\}\). Let \(V\in H^{\gamma+s}(\mathbb T^d)\) be real-valued and set
\[
 \pi(x)=e^{-V(x)}/Z,\qquad Z=\int_{\mathbb T^d}e^{-V(x)}\,dx.
\]
Let \(K_s\) be the periodic distribution with Fourier coefficients \(\widehat K_s(k)=|2\pi k|^{-2s}\) for \(k\ne0\), and \(\widehat K_s(0)=0\). Its convolution with a vector distribution is defined componentwise.

For a nonnegative probability density \(\rho\), write
\[
 \mathcal H(\rho\mid\pi)=\int_{\mathbb T^d}\rho\log(\rho/\pi)\,dx,
\]
with \(0\log(0/\pi)=0\). Consider the equation
\[
 \partial_t\rho_t+\nabla\!\cdot(\rho_tu_t)=0,\qquad
 u_t=-K_s*\bigl(\rho_t\nabla\log(\rho_t/\pi)\bigr),\qquad
 \rho_0=\bar\rho.
\]
For densities that may vanish, the vector distribution inside this convolution is defined to mean \(\nabla\rho_t+\rho_t\nabla V\).

Assume \(\bar\rho\in H^\gamma\) is a nonnegative probability density. Let \(\rho\) be a distributional solution on its maximal interval \([0,T_{\max})\), weakly continuous as a curve of probability measures and satisfying
\[
 \rho\in L^\infty([0,T'];H^\gamma(\mathbb T^d))\qquad\text{for every }T'<T_{\max}.
\]
Here maximality is with respect to extension in this solution class with the prescribed initial density.

## Task

Prove that there are constants \(C>0\) and \(\delta>0\), depending only on \(d,s,\gamma,\|V\|_{H^{\gamma+s}}\), and \(\|\bar\rho\|_{H^\gamma}\), such that if
\[
 \mathcal H(\bar\rho\mid\pi)\le\delta,
\]
then \(T_{\max}=\infty\) and, for every \(t\ge0\),
\[
 \mathcal H(\rho_t\mid\pi)\le
 \left(\mathcal H(\bar\rho\mid\pi)^{-(s-1)/\gamma}+t/C\right)^{-\gamma/(s-1)}.
\]
Moreover, for every \(0\le\beta\le\gamma\), prove that there is \(C_\beta>0\), depending only on the same data and on \(\beta\), such that
\[
 \|\rho_t-\pi\|_{\dot H^\beta}^2\le
 C_\beta\|\bar\rho-\pi\|_{\dot H^\gamma}^{2\beta/\gamma}
 \left(\mathcal H(\bar\rho\mid\pi)^{-(s-1)/\gamma}+t/C\right)^{-(\gamma-\beta)/(s-1)}
 \qquad\text{for all }t\ge0.
\]
At \(\beta=0\), the initial-norm factor is understood as one. When \(\mathcal H(\bar\rho\mid\pi)=0\), prove that the solution is stationary at \(\pi\), and interpret the bounds accordingly.
