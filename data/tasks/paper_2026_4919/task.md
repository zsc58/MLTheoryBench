# Problem

## Setup

Consider a symmetric \(K\)-armed bandit with \(K\ge 3\) and a unique correct arm \(y^*\). The reward is deterministic:
\[
R(a)=\mathbf 1\{a=y^*\}.
\]
A policy assigns probability \(p\in(0,1)\) to the correct arm and equal probability
\[
\pi(y^*)=p,\qquad \pi(a)=q:=\frac{1-p}{K-1}\quad(a\ne y^*).
\]
Fix a baseline \(b\in(0,1)\), and define the advantage \(U(a)=R(a)-b\), surprisal \(\ell(a)=-\log\pi(a)\), multiplicative delight \(\chi(a)=U(a)\ell(a)\), and, for \(\alpha\in[0,1]\), the additive priority
\[
f_\alpha(a)=\alpha U(a)+(1-\alpha)\ell(a).
\]

## Task

Prove the following integrated claim. For every allowed \(p,K,b\), multiplicative delight is sign-consistent:
\[
\chi(y^*)>0>\chi(a)\quad\text{for every }a\ne y^*.
\]
Moreover, with
\[
L=\log\frac{p(K-1)}{1-p},
\]
the additive priority ranks the correct arm strictly above every incorrect arm, \(f_\alpha(y^*)>f_\alpha(a)\), precisely as follows:

- if \(L>0\) (equivalently \(p>1/K\)), exactly when \(\alpha>L/(1+L)\);
- if \(L=0\) (equivalently \(p=1/K\)), exactly when \(\alpha>0\);
- if \(L<0\) (equivalently \(p<1/K\)), for every \(\alpha\in[0,1]\).

Thus additive priorities require a policy- and action-space-dependent tuning threshold in the \(p>1/K\) regime, whereas delight does not.
