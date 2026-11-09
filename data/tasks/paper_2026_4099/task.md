# Problem

## Setup

Let \(X_1,X_2,X_3\) be independent Bernoulli\((1/2)\) variables and let
\[
Y=X_1\oplus X_2\oplus X_3,
\]
where \(\oplus\) denotes addition modulo two. Fix an input \(x=(x_1,x_2,x_3)\in\{0,1\}^3\) and write \(y=x_1\oplus x_2\oplus x_3\). The deployed predictor is the fixed function
\[
f:\{0,1\}^3\to\{0,1\},\qquad f(u)=u_1\oplus u_2\oplus u_3.
\]
The background vector \(Z=(Z_1,Z_2,Z_3)\) has independent Bernoulli\((1/2)\) coordinates and is independent of \((X_1,X_2,X_3)\). The loss is squared loss \(\ell(a,y)=(a-y)^2\).

Let \(N=\{1,2,3\}\). For a coalition \(S\subseteq N\), let \(\mathbf 1_S\in\{0,1\}^3\) be its indicator vector, and let \(\mathbf 1=(1,1,1)\). With \(\odot\) denoting componentwise multiplication, define the interventional coalition loss
\[
L(S;x,y)=\mathbb E_Z\left[\ell\left(f(\mathbf 1_S\odot x+(\mathbf 1-\mathbf 1_S)\odot Z),y\right)\right].
\]
Define the coalition value
\[
v(S;x)=\mathbb E_Z[f(\mathbf 1_S\odot x+(\mathbf 1-\mathbf 1_S)\odot Z)].
\]
For \(T\subseteq N\), its Möbius coefficient is
\[
m_T=\sum_{S\subseteq T}(-1)^{|T|-|S|}v(S;x).
\]
Use the abbreviations \(m_i=m_{\{i\}}\), \(m_{ij}=m_{\{i,j\}}\), and \(m_{123}=m_N\).

For distinct \(i,j\in N\), let \(k\) be the remaining feature. For \(S\subseteq N\setminus\{i,j\}\), define
\[
\Delta_{ij}v(S)=v(S\cup\{i,j\};x)-v(S\cup\{i\};x)-v(S\cup\{j\};x)+v(S;x).
\]
In this problem, a faithful pair report is the second-order Möbius mass \(m_{ij}\), and a projective pair report is
\[
P_{ij}=\tfrac12\Delta_{ij}v(\varnothing)+\tfrac12\Delta_{ij}v(\{k\}).
\]
Finally, define \(G_i(C)=L(C;x,y)-L(C\cup\{i\};x,y)\) for \(C\subseteq N\setminus\{i\}\), and
\[
U_i=\min_{C\subseteq N\setminus\{i\}}G_i(C),\qquad
M_i=\max_{C\subseteq N\setminus\{i\}}G_i(C),\qquad
\pi_i=G_i(\varnothing),\qquad
R_i=\pi_i-U_i,\qquad
S_i=M_i-\pi_i.
\]

## Task

Prove that for every input \(x\in\{0,1\}^3\):

1. Every proper coalition has \(v(S;x)=1/2\), while \(v(N;x)=y\); consequently \(m_i=m_{ij}=0\) for all singletons and pairs and \(m_{123}=y-1/2\in\{-1/2,1/2\}\).
2. Every faithful pair report is zero, whereas each projective pair report is \(P_{ij}=m_{123}/2\in\{-1/4,1/4\}\). Thus, for the two reporting rules defined here, the faithful rule gives zero pair outputs despite nonzero third-order mass, while the projective rule assigns a signed multiple of that mass to each pair despite vanishing second-order masses.
3. For each feature \(i\), the LOCO decomposition satisfies
\[
(U_i,R_i,S_i)=(0,0,1/2).
\]
