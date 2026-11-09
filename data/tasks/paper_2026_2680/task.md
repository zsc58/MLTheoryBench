# Problem

## Setup

Let \(x_1,\ldots,x_n\) be an ordered input sequence with targets \(y_i\in\mathbb R^{d_y}\). Let \(\phi(x)\in\mathbb R^{d_\phi}\), write \(X_n=[x_1,\ldots,x_n]\) and \(Y=[y_1,\ldots,y_n]\in\mathbb R^{d_y\times n}\), and define
\[
k(x,x')=\phi(x)^\top\phi(x'),\quad K=[k(x_i,x_j)]_{i,j=1}^n,\quad k(X_n,x)=[k(x_1,x),\ldots,k(x_n,x)]^\top.
\]
Let \(K^U\) be the strictly upper-triangular part of \(K\): \((K^U)_{ij}=K_{ij}\) for \(i<j\), and zero otherwise. Fix \(\eta>0\) and \(\gamma>0\). Define
\[
f_{\rm off}(x;X_n,Y)=Y(\gamma I_n+K)^{-1}k(X_n,x).
\]
Starting from \(W_1=0\), perform unregularized online updates
\[
W_{t+1}=W_t-\eta\bigl(W_t\phi(x_t)-y_t\bigr)\phi(x_t)^\top,\qquad t=1,\ldots,n,
\]
and set \(f_{\rm on}(x;X_n,Y)=W_{n+1}\phi(x)\).

## Task

Prove the following integrated theorem. With \(A=\eta^{-1}I_n+K^U\) and \(B=\gamma I_n+K\),
\[
f_{\rm on}(x;X_n,Y)=YA^{-1}k(X_n,x).
\]
Consequently, for effective targets \(Y^e=YA^{-1}B\), one has \(f_{\rm on}(x;X_n,Y)=f_{\rm off}(x;X_n,Y^e)\) for every \(x\). Moreover, for corrected targets \(Y^c=YB^{-1}A\), running the same online recursion on \((X_n,Y^c)\) yields \(f_{\rm on}(x;X_n,Y^c)=f_{\rm off}(x;X_n,Y)\) for every test point \(x\).
