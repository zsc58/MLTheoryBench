# Problem

## Setup

Let \(u\) be an input random variable with distribution \(p\), and let \(\epsilon\) be an independent noise random variable. Let \(\mathcal H_u=L^2(p)\) and \(\mathcal H_\epsilon=L^2(p_\epsilon)\), with the usual inner products and norms; write \(\mathcal H=\mathcal H_u\otimes\mathcal H_\epsilon\). Let \(\{y_l\}_{l\ge1}\) be a complete orthonormal basis of \(\mathcal H_u\), and let \(\{z_m\}_{m\ge1}\) be a complete orthonormal basis of \(\mathcal H_\epsilon\) with \(z_1\equiv1\). Thus \(\{y_lz_m\}_{l,m}\) is a complete orthonormal basis of \(\mathcal H\).

A stationary system has \(K\) square-integrable readouts \(X_i(u,\epsilon)\in\mathcal H\), and \(\mathcal S=\operatorname{span}\{X_1,\ldots,X_K\}\). For every nonzero target \(f\in\mathcal H_u\), identify \(f\) with \(f(u)z_1(\epsilon)\in\mathcal H\), and define its information-processing capacity by
\[
 C(f,\mathcal S)=\frac{\|P_{\mathcal S}f\|^2}{\|f\|^2},
\]
where \(P_{\mathcal S}\) is the orthogonal projector onto \(\mathcal S\). Call the system genuinely noisy when \(\mathcal S\) is not contained in the input-only subspace \(\mathcal H_u\otimes\operatorname{span}\{z_1\}\).

## Task

Prove that for every complete orthonormal input basis \(\{y_l\}\), a genuinely noisy system satisfies
\[
\sum_{l\ge1} C(y_l,\mathcal S)<K.
\]
