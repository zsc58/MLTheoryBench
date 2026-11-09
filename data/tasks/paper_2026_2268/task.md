# Problem

## Setup

Let \(d\ge1\) be an integer, and use the Euclidean norm \(\|\cdot\|\) on \(\mathbb R^d\). Let \(S_{\rm ref},S_{\rm cl}\subset\mathbb R^d\) be nonempty compact convex sets. For each such set \(S\), define
\[
\xi_S(u)=\max_{w\in S}u^\top w,\qquad z_S^*(c)=\min_{w\in S}c^\top w,
\]
fix an arbitrary selector \(w_S^*(c)\in\arg\min_{w\in S}c^\top w\), and set
\[
\ell_S^{\mathrm{SPO+}}(h,c)=\xi_S(c-2h)+2h^\top w_S^*(c)-z_S^*(c).
\]
Fix finite constants \(0<C_{\min}\le C_{\max}\) and \(\tau\ge0\). A triple \(h,c_{\rm ref},c_{\rm cl}\in\mathbb R^d\) is admissible when
\[
\|h\|\le\tau,\qquad C_{\min}\le\|c_i\|\le C_{\max}\quad(i\in\{\mathrm{ref},\mathrm{cl}\}).
\]
For nonempty compact sets \(A,B\), let
\[
d_H(A,B)=\max\left\{\sup_{a\in A}\inf_{b\in B}\|a-b\|,\ \sup_{b\in B}\inf_{a\in A}\|a-b\|\right\},
\qquad D(S)=\sup_{u,v\in S}\|u-v\|.
\]
Define
\[
\delta_N=\inf_{v\in\mathbb R^d}d_H(S_{\rm ref},S_{\rm cl}+v),\quad
D_{\min}=\min\{D(S_{\rm ref}),D(S_{\rm cl})\},\quad
c_d=\|c_{\rm ref}-c_{\rm cl}\|,
\]
where \(S+v=\{w+v:w\in S\}\), and define
\[
T(h)=\min\left\{
D(S_{\rm ref})c_d+\delta_N(\|c_{\rm cl}-2h\|+\|c_{\rm cl}\|),\ 
D(S_{\rm cl})c_d+\delta_N(\|c_{\rm ref}-2h\|+\|c_{\rm ref}\|)
\right\}.
\]

## Task

Prove, for every admissible triple and every choice of the fixed selectors,
\[
|\ell_{S_{\rm ref}}^{\mathrm{SPO+}}(h,c_{\rm ref})-\ell_{S_{\rm cl}}^{\mathrm{SPO+}}(h,c_{\rm cl})|
\le H(h):=T(h)+2\|h\|(\delta_N+D_{\min}).
\]

For a finite \(\rho>0\), call a set \(\rho\)-strongly convex if it is an intersection of closed Euclidean balls of radius \(\rho\). If the two sets are respectively \(\rho_{\rm ref}\)- and \(\rho_{\rm cl}\)-strongly convex, let \(\rho_{\min}=\min\{\rho_{\rm ref},\rho_{\rm cl}\}\) and
\[
\Gamma=\rho_{\min}\left\|\frac{c_{\rm ref}}{\|c_{\rm ref}\|}-\frac{c_{\rm cl}}{\|c_{\rm cl}\|}\right\|+\delta_N+2\sqrt{\rho_{\min}\delta_N}.
\]
Prove that the same discrepancy is at most
\[
H_{\rm SC}(h):=T(h)+2\|h\|\Gamma.
\]

Finally, prove that the diameter-scale term in the unrestricted bound is generally necessary in the following existential sense. There exist fixed admissible choices of dimension and constants with \(\tau>0\), a fixed nonempty compact convex set \(S\) with \(D(S)>0\), a fixed prediction \(h\) with \(0<\|h\|\le\tau\), a fixed optimizer selector for \(S\), and sequences of costs \(c_{\rm ref}^{(n)},c_{\rm cl}^{(n)}\) obeying the same cost bounds, such that
\[
\|c_{\rm ref}^{(n)}-c_{\rm cl}^{(n)}\|\longrightarrow0,
\qquad
\liminf_{n\to\infty}
\frac{|\ell_S^{\mathrm{SPO+}}(h,c_{\rm ref}^{(n)})-\ell_S^{\mathrm{SPO+}}(h,c_{\rm cl}^{(n)})|}{\|h\|D(S)}>0.
\]
