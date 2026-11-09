# Problem

## Setup

Let \(L\in\mathbb R^{d\times d}\) be the Hodge Laplacian on a fixed finite simplicial complex; thus \(L\) is real symmetric and positive semidefinite. Let \(H_t\) be a real polynomial, depending continuously on \(t\in[0,1]\), and set \(A_t=H_t(L)\). Let \(\alpha:[0,1]\to\mathbb R^d\) be continuous and let \(\sigma>0\). Let \(W\) be standard \(d\)-dimensional Brownian motion. Consider
\[
 dX_t=(A_tX_t+\alpha_t)\,dt+\sigma\,dW_t.
\]

For \(0\le s\le t\le1\), let \(\Phi_{s,t}\) be the fundamental matrix satisfying
\[
 \frac{d}{dt}\Phi_{s,t}=A_t\Phi_{s,t},\qquad \Phi_{s,s}=I.
\]
For \(r,s,t\in[0,1]\) with \(r\le s\wedge t\), define
\[
 \widetilde\Sigma_{s,t\mid r}
 =\int_r^{s\wedge t}\Phi_{q,s}\Phi_{q,t}^{\mathsf T}\,dq,
 \qquad
 m_{t\mid r}(x)=\Phi_{r,t}x+\int_r^t\Phi_{q,t}\alpha_q\,dq.
\]
Write \(m_t(x)=m_{t\mid0}(x)\) and \(\widetilde\Sigma_{s,t}=\widetilde\Sigma_{s,t\mid0}\). Fix endpoints \(x_0,x_1\in\mathbb R^d\). Start the reference process at \(X_0=x_0\), and consider its law conditioned on \(X_1=x_1\). Here endpoint conditioning means the version of the conditional path law that is weakly continuous in the terminal value, on \(C([0,1];\mathbb R^d)\) equipped with the uniform norm.

## Task

Prove the following integrated claim.

For \(0\le t<1\), the endpoint-conditioned process has Gaussian one-time marginal with mean
\[
 b_t=m_t(x_0)+\widetilde\Sigma_{t,1}\widetilde\Sigma_{1,1}^{-1}
 \bigl(x_1-m_1(x_0)\bigr)
\]
and covariance
\[
 \sigma^2\left(\widetilde\Sigma_{t,t}
 -\widetilde\Sigma_{t,1}\widetilde\Sigma_{1,1}^{-1}
 \widetilde\Sigma_{1,t}\right).
\]
Its drift, for \(0\le t<1\), is the reference drift plus the endpoint bridge control
\[
 u_t(x)=\Phi_{t,1}\widetilde\Sigma_{1,1\mid t}^{-1}
 \bigl(x_1-m_{1\mid t}(x)\bigr).
\]
Set \(b_1=x_1\). As \(\sigma\downarrow0\), the conditioned path law converges weakly on \(C([0,1];\mathbb R^d)\), with its uniform topology, to the Dirac mass at \(b=(b_t)_{t\in[0,1]}\). The control along this limiting path, for \(0\le t<1\), is
\[
 u_t(b_t)=\Phi_{t,1}\widetilde\Sigma_{1,1}^{-1}
 \bigl(x_1-m_1(x_0)\bigr).
\]

Moreover, specialize to \(A_t=-\kappa L\) with \(\kappa\ge0\). Define
\[
 h_t=\int_0^t e^{-\kappa L(t-q)}\alpha_q\,dq.
\]
For an orthonormal eigenbasis \(Lv_i=\lambda_i v_i\), put
\(y_{0,i}=\langle x_0,v_i\rangle\) and
\(y_{1,i}=\langle x_1-h_1,v_i\rangle\). The path identities below are asserted for \(0\le t\le1\), and the control identities for \(0\le t<1\). Show that, when \(\kappa\lambda_i=0\),
\[
 \langle b_t-h_t,v_i\rangle=(1-t)y_{0,i}+ty_{1,i},
 \qquad
 \langle u_t(b_t),v_i\rangle=y_{1,i}-y_{0,i}.
\]
When \(\kappa\lambda_i>0\), show that
\[
 \langle b_t-h_t,v_i\rangle
 =\frac{\sinh(\kappa\lambda_i(1-t))}{\sinh(\kappa\lambda_i)}y_{0,i}
 +\frac{\sinh(\kappa\lambda_i t)}{\sinh(\kappa\lambda_i)}y_{1,i},
\]
\[
 \langle u_t(b_t),v_i\rangle
 =\frac{2\kappa\lambda_i e^{-\kappa\lambda_i(1-t)}}{1-e^{-2\kappa\lambda_i}}
 \left(y_{1,i}-e^{-\kappa\lambda_i}y_{0,i}\right).
\]
