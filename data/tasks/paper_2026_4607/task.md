# Problem

## Setup

Let `J` be a finite index set. Let `Y` be a balanced binary label, taking values in `{+1,-1}` with probability `1/2` each. For every `i` in `J`, let `X_i` be a jointly distributed binary output in `{+1,-1}`. Define the error indicator
\[
E_i=\mathbf 1\{X_i\ne Y\}.
\]
For `S` a subset of `J`, write `X_S=(X_i)_{i\in S}` and `E_S=(E_i)_{i\in S}`. For `j` not in `S`, define
\[
\Delta(j\mid S)=I(Y;X_j\mid X_S),
\qquad
\Lambda_j(S)=I(E_j;Y\mid E_S)-I(E_j;Y),
\]
where `I` and conditional `I` denote mutual information and conditional mutual information under the joint law of these variables.

## Task

Prove that, for every `S` and `j` not in `S`,
\[
\Delta(j\mid S)=I(Y;X_j)-I(X_j;X_S)+I(E_j;E_S)+\Lambda_j(S).
\]
Moreover, if the entire error vector `(E_i)_{i\in J}` is jointly independent of `Y`, prove the simplified identity
\[
\Delta(j\mid S)=I(Y;X_j)-I(X_j;X_S)+I(E_j;E_S).
\]
