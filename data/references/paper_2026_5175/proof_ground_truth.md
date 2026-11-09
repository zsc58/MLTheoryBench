# Reference Proof

## Proof Structure

Define a loss-based good set of trajectories. The two independent samples certify that its complements have small mass under both trajectory distributions. On the good set, the log-ratio bound controls the unknown normalizer ratio and hence the likelihood ratio between the forward and target-backward trajectory laws. A good/bad-set decomposition bounds trajectory total variation, and marginalization transfers that bound to terminal states.

## Complete Proof

Write \(P=p\), \(Q=q\), and \(K=A/A_*\). Since each \(b(\cdot\mid x)\) is normalized on its terminal fiber,
\[
\sum_{\tau\in\mathcal T}Q(\tau)
=\sum_{x\in\mathcal X}\rho(x)\sum_{\tau:x(\tau)=x}b(\tau\mid x)
=1.
\]
Both \(P\) and \(Q\) are positive on \(\mathcal T\). Define
\[
G=\{\tau\in\mathcal T:\ell(\tau)\le c^2\},\qquad
\varepsilon=Q(G^c),\qquad \eta=P(G^c).
\]
The set \(G\) and the two masses are fixed because the model and threshold are fixed before sampling.

Set \(a_m=\log(1/\alpha)/m\) and \(a_n=\log(1/\alpha)/n\). Let \(H_Q\) be the event that every \(Q\)-sample lies in \(G\), and let \(H_P\) be the corresponding event for the \(P\)-samples. If \(\varepsilon>a_m\), independence within the \(Q\)-sample gives
\[
\Pr(H_Q)=(1-\varepsilon)^m\le e^{-m\varepsilon}<e^{-ma_m}=\alpha.
\]
If \(\varepsilon\le a_m\), the event \(H_Q\cap\{\varepsilon>a_m\}\) is empty. Consequently,
\[
\Pr\bigl(H_Q\cap\{\varepsilon>a_m\}\bigr)\le\alpha.
\]
Likewise,
\[
\Pr\bigl(H_P\cap\{\eta>a_n\}\bigr)\le\alpha.
\]
Define
\[
E=\bigl(H_Q\cap\{\varepsilon>a_m\}\bigr)
\cup\bigl(H_P\cap\{\eta>a_n\}\bigr).
\]
A union bound gives \(\Pr(E)\le2\alpha\). Outside \(E\), the all-good observation \(H_Q\cap H_P\) therefore implies
\[
\varepsilon\le a_m,\qquad \eta\le a_n. \tag{1}
\]
This is an unconditional bound on a failure event, not a probability statement conditioned on observing \(H_Q\cap H_P\).

We next prove the deterministic inequality
\[
\operatorname{TV}(P,Q)\le e^{2c}-1+\varepsilon+\eta. \tag{2}
\]
If \(\varepsilon=1\), then
\[
\operatorname{TV}(P,Q)
\le\tfrac12\sum_{\tau}(P(\tau)+Q(\tau))=1
\le e^{2c}-1+\varepsilon+\eta,
\]
using \(c\ge0\) and \(\eta\ge0\). Thus this case is already settled. In particular, no division by \(1-\varepsilon\) is needed when \(G\) is empty.

Suppose now that \(\varepsilon<1\). For every \(\tau\in G\), the definition of the loss and \(c\ge0\) give
\[
e^{-c}\le K\frac{P(\tau)}{Q(\tau)}\le e^c. \tag{3}
\]
Summing the left inequality after multiplying by \(Q(\tau)\) yields
\[
K P(G)\ge e^{-c}Q(G)=e^{-c}(1-\varepsilon).
\]
Since \(P(G)\le1\) and \(K>0\), it follows that
\[
K\ge e^{-c}(1-\varepsilon).
\]
The right inequality in (3) now implies, on \(G\),
\[
\frac{P(\tau)}{Q(\tau)}\le\frac{e^{2c}}{1-\varepsilon}=:D. \tag{4}
\]
Here \(D\ge1\).

For a real number \(z\), write \(z_+=\max\{z,0\}\). Because \(\sum_{\tau}(P(\tau)-Q(\tau))=0\), the sums of the positive and negative parts are equal. Hence
\[
\operatorname{TV}(P,Q)=\sum_{\tau}(P(\tau)-Q(\tau))_+.
\]
For \(\tau\in G\), (4) and \(D\ge1\) give
\((P(\tau)-Q(\tau))_+\le(D-1)Q(\tau)\). On \(G^c\), the positive part is at most \(P(\tau)\). Therefore
\[
\begin{aligned}
\operatorname{TV}(P,Q)
&\le (D-1)Q(G)+P(G^c)\\
&=\left(\frac{e^{2c}}{1-\varepsilon}-1\right)(1-\varepsilon)+\eta\\
&=e^{2c}-1+\varepsilon+\eta.
\end{aligned}
\]
This proves (2) in every case, including \(c=0\).

For each terminal state \(x\), normalization of \(b(\cdot\mid x)\) gives
\[
\sum_{\tau:x(\tau)=x}Q(\tau)=\rho(x),
\]
while the corresponding marginal of \(P\) is \(p_X(x)\). The triangle inequality consequently gives
\[
\begin{aligned}
\operatorname{TV}(p_X,\rho)
&=\frac12\sum_x\left|\sum_{\tau:x(\tau)=x}(P(\tau)-Q(\tau))\right|\\
&\le\frac12\sum_x\sum_{\tau:x(\tau)=x}|P(\tau)-Q(\tau)|\\
&=\operatorname{TV}(P,Q).
\end{aligned}
\]
Outside \(E\), whenever all sampled losses are at most \(c^2\), substituting (1) into (2) and applying this marginal bound proves
\[
\operatorname{TV}(p_X,\rho)
\le e^{2c}-1+\frac{\log(1/\alpha)}{m}+\frac{\log(1/\alpha)}{n}.
\]
No assumption that either sampled mass bound is below one is required. If \(2\alpha\ge1\), the asserted probability bound is simply noninformative, but remains valid.
