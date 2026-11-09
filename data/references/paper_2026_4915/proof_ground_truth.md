# Reference Proof

## Proof Structure

Compute the first two moments of the average over all token positions and of the average over the D structural positions, then substitute them into the SNR definition.

## Complete Proof

Let I be the fixed set of structural positions, |I|=D, with 1 <= D <= T. Assume the token contributions Z_1,...,Z_T are independent, each has variance sigma^2>0, has mean mu != 0 when t is in I, and has mean 0 when t is not in I. Define
\[
G_{tok}=\frac1T\sum_{t=1}^T Z_t,\qquad G_{opt}=\frac1D\sum_{t\in I}Z_t.
\]
By linearity,
\[
E[G_{tok}]=\frac{D\,mu}{T},\qquad E[G_{opt}]=mu.
\]
Independence and the common variance give
\[
Var(G_{tok})=\frac{1}{T^2}\sum_{t=1}^T sigma^2=\frac{sigma^2}{T},
\qquad
Var(G_{opt})=\frac{1}{D^2}\sum_{t\in I} sigma^2=\frac{sigma^2}{D}.
\]
For SNR(G)=|E[G]|/sqrt(Var(G)), this yields
\[
SNR(G_{tok})=\frac{|mu|D}{sigma\sqrt T},\qquad
SNR(G_{opt})=\frac{|mu|\sqrt D}{sigma}.
\]
Therefore
\[
\frac{SNR(G_{opt})}{SNR(G_{tok})}=\sqrt{\frac{T}{D}}.
\]
(The two means differ by T/D, a deterministic scaling.)
