# Problem

## Setup

Fix a sufficiently large horizon \(T\). Let \(m=2^{\lfloor(\log _2 T)/3\rfloor}\), and let \(X=\{x_i:0\le i<m\}\) with \(x_i=1/4+i/(2(m-1))\). At round \(t\), the context is presented deterministically in round-robin order, \(x^t=x_{(t-1)\bmod m}\). The outcome is \(y^t=x^t+\xi_t/4\), where \(\xi_t\) are independent uniform signs. An online forecaster, possibly randomized, chooses \(p_t\in[0,1]\) from the history before \(\xi_t\) is revealed.

A group function is a map \(g:X\times[0,1]\to[0,1]\); it is prediction-independent when it depends only on \(x\), and binary when it takes values in \(\{0,1\}\). For a finite group family \(G\), define
\[
B_T(v,g)=\sum_{t:p_t=v}g(x^t,p_t)(p_t-y^t),\qquad
\operatorname{Err}_T(g)=\sum_{v\in\{p_1,\ldots,p_T\}}|B_T(v,g)|,
\]
and \(\operatorname{MCerr}_T(G)=\max_{g\in G}\operatorname{Err}_T(g)\). Expectations include the forecaster's and environment's randomness.

Identify indices with \(q=\log _2m\) bits and let \(w_\ell(i)=(-1)^{\langle\ell,i\rangle}\) be the Walsh characters. For \(\ell\ne0\), define prediction-independent binary groups \(g_\ell^\pm(x_i,v)=(1\pm w_\ell(i))/2\), and include the constant group \(g_{\rm all}\equiv1\).

## Task

Prove that there are universal constants \(c,C>0\) and \(T_0\) such that, for every \(T\ge T_0\), one can choose a set \(S\subseteq\{1,\ldots,m-1\}\) with \(|S|\le C\log ^3(m+1)\) for which the family
\[
G_S=\{g_{\rm all}\}\cup\{g_\ell^+,g_\ell^-:\ell\in S\}
\]
is prediction-independent and binary, and every possibly randomized online forecaster satisfies
\[
\mathbb E[\operatorname{MCerr}_T(G_S)]\ge {c\,T^{2/3}\over \log ^C(T+1)}.
\]
