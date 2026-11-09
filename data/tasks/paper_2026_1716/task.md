# Problem

## Setup

Let \(a>0\), \(\sigma^2>0\), and \(\mu\in\mathbb C\). Interpret every occurrence of \(\sigma^{2a}\) below as \((\sigma^2)^a\), and interpret densities on \(\mathbb C\) with respect to planar Lebesgue area measure. For \(u\in\mathbb C\) and integer \(k\ge0\), write \((u)_0=1\) and \((u)_k=u(u+1)\cdots(u+k-1)\), and define
\[
\mathcal L_\rho(t):=\sum_{k=0}^\infty\frac{(-\rho)_k t^k}{(k!)^2},
\qquad
I_0(t):=\sum_{k=0}^\infty\frac{(t^2/4)^k}{(k!)^2}.
\]
Define the nonnegative function, with the immaterial convention \(p(0)=0\),
\[
p(z)=\frac{|z|^{2a-2}\exp(-|z-\mu|^2/\sigma^2)}{\pi\,\sigma^{2a}\Gamma(a)\,\mathcal L_{a-1}(-|\mu|^2/\sigma^2)},\qquad z\in\mathbb C\setminus\{0\}.
\]
Prove below that \(p\) integrates to one. After this is established, let \(Z\) have density \(p\). Write \(\nu=|\mu|\), let \(R=|Z|\) denote the amplitude, and set \(X=R^2\), \(\beta=1/\sigma^2\), and \(\lambda=\beta\nu^2\).

## Task

Prove that the density above is normalized and that:

1. The amplitude density for \(r>0\) is
\[
f_R(r)=\frac{2r^{2a-1}e^{-(r^2+\nu^2)/\sigma^2}I_0(2\nu r/\sigma^2)}{\sigma^{2a}\Gamma(a)\,\mathcal L_{a-1}(-\nu^2/\sigma^2)}.
\]
Moreover, \(a=1\) gives the Rice law, while \(\nu=0\) with \(a=m>0\) and \(\sigma^2=\Omega/m\) for \(\Omega>0\) gives the Nakagami-\(m\) law, including the Rayleigh case \(m=1\) and the one-sided normal case \(m=\tfrac12\).

2. The power density for \(x>0\) is
\[
f_X(x)=\frac{\beta^a x^{a-1}e^{-\beta x}I_0(2\sqrt{\beta\lambda x})}{\Gamma(a)\,\mathcal L_{-a}(\lambda)},
\]
with \(\lambda=0\) yielding the \(\mathrm{Gamma}(a,\text{rate }\beta)\) density. For \(\lambda\ge0\), show the equivalent gamma-mixture representation
\[
f_X(x)=\sum_{n=0}^\infty w_n g_{a+n,\beta}(x),\qquad
w_n=\frac{(a)_n\lambda^n}{(n!)^2\mathcal L_{-a}(\lambda)},
\]
where \(g_{k,\beta}(x)=\beta^k x^{k-1}e^{-\beta x}/\Gamma(k)\) for \(k>0\), and prove \(\sum_n w_n=1\).
