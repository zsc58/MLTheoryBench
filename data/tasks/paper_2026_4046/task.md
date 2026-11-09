# Problem

## Setup

For an open set \(U\subset\mathbb R^d\), let \(W^{s,\infty}(U)\) be the space of functions with weak derivatives through order \(s\) in \(L^\infty(U)\), equipped with
\[
 \|f\|_{W^{s,\infty}(U)}=\max_{|\alpha|\le s}\|D^\alpha f\|_{L^\infty(U)}.
\]

A scalar \(\sigma\)-network is a finite sequence of affine maps with componentwise activation \(\sigma\) after every hidden affine map and a final affine scalar output. Its width is the largest layer size, including the input and output layers, and its depth is the number of activation layers.

Fix \(n\in\mathbb N\cup\{\infty\}\). For finite \(n\), define
\[
 q_n(u)=\begin{cases}
 0,&u\le0,\\
 \displaystyle\frac{\int_0^u t^n(1-t)^n\,dt}{\int_0^1t^n(1-t)^n\,dt},&0<u<1,\\
 1,&u\ge1,
 \end{cases}
\]
and define
\[
 q_\infty(u)=\begin{cases}
 0,&u\le0,\\
 \displaystyle\frac{e^{-1/u}}{e^{-1/u}+e^{1/(u-1)}},&0<u<1,\\
 1,&u\ge1.
 \end{cases}
\]
On \([0,2]\), let
\[
 g_n(t)=\begin{cases}
 q_n(2t),&0\le t\le\tfrac12,\\
 1-q_n(2t-1),&\tfrac12<t\le1,\\
 0,&1<t\le2,
 \end{cases}
\]
and extend \(g_n\) with period \(2\). On \([0,1]\), let
\[
 \rho_n(t)=\begin{cases}t,&0\le t\le\tfrac12,\\t-q_n(2t-1),&\tfrac12<t\le1,\end{cases}
\]
and extend \(\rho_n\) with period \(1\). Put
\[
 \eta_n=\min\left\{\frac2{11},\frac1{8\|q_n'\|_\infty}\right\}\quad(n<\infty),
 \qquad \eta_\infty=\frac1{16},
\]
and define
\[
 h_n(t)=\begin{cases}
 -\frac95-(1-q_n(2t+10))(1+\rho_n(-t-5)),&t\le-\frac92,\\
 -\frac95+q_n(2t+9)\left(-\frac15-t^{-1}\right),&-\frac92\le t\le-\frac{13}{11},\\
 -2-t^{-1}+q_n\!\left(\eta_n^{-1}(t+1+\eta_n)\right)(t+2+t^{-1}),&-\frac{13}{11}<t<-1,\\
 (1-q_n(11t/4+1))t,&t\ge-1.
 \end{cases}
\]
Define the activation
\[
 \sigma_n(t)=\begin{cases}h_n(t),&t\le0,\\g_n(t),&t>0.\end{cases}
\]

For \(d,s\in\mathbb N\), set
\[
 N_{s,d}=4^d\left[\frac d{d+1}(s+5d+4){s+d-1\choose d}+d+4\right],
 \qquad
 L_{s,d}=\max\{2s+2d-2,\,2d+1,\,7\}.
\]

## Task

Prove that, whenever \(1\le s\le n+1\), for every \(a<b\), every \(f\in W^{s,\infty}((a,b)^d)\), and every \(\varepsilon>0\), there exists a \(\sigma_n\)-network \(\Phi\) of width at most \(N_{s,d}\) and depth at most \(L_{s,d}\) such that
\[
 \|\Phi-f\|_{W^{s-1,\infty}((a,b)^d)}<\varepsilon.
\]
