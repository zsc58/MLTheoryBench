# Problem

## Setup

Let \(\mathcal X=\mathcal X_1\times\cdots\times\mathcal X_m\) be a finite product state space. For each component \(i\), let \(c_i(a\mid x_{-i})\) be a probability distribution on \(\mathcal X_i\) for every assignment of the other components \(x_{-i}\). Let \(\alpha_i>0\) with \(\sum_{i=1}^m\alpha_i=1\). Define the random-scan transition kernel
\[
K(x\mid x')=\sum_{i=1}^m\alpha_i\,c_i(x_i\mid x'_{-i})\,\mathbf 1\{x_{-i}=x'_{-i}\}.
\]
Assume that some positive power of \(K\) has strictly positive entries. Hence the finite-state chain has a unique limiting (stationary) distribution \(\pi\), with \(\pi(x)>0\) for all \(x\). The conditional family \(\{c_i\}_{i=1}^m\) is called jointly consistent if there exists a full-support probability distribution \(\rho\) on \(\mathcal X\) whose conditionals satisfy \(\rho(x_i\mid x_{-i})=c_i(x_i\mid x_{-i})\) for every \(i\) and every complement.

The kernel satisfies detailed balance with respect to \(\pi\) when
\[
\pi(x')K(x\mid x')=\pi(x)K(x'\mid x)\quad\text{for all }x,x'\in\mathcal X.
\]

## Task

Prove that detailed balance of \(K\) with respect to its limiting distribution \(\pi\) is equivalent to joint consistency of the modeled conditionals. Moreover, whenever these equivalent conditions hold, prove that
\[
 c_i(x_i\mid x_{-i})=\pi(x_i\mid x_{-i})
\]
for every component \(i\) and every state \(x\).
