# Reference Proof

## Proof Structure

Show that deployment samples reveal no information about the latent variable, whereas one observation from the other input reveals it exactly. Compute the entropy decomposition, then apply the two reducibility criteria to obtain the trichotomy and the incompatibility claim.

## Complete Proof

Fix any \(n\geq 0\). Every input in \(S_n\) equals \(0\) almost surely. Conditional on either value of \(\Theta\), each associated label is \(\operatorname{Bernoulli}(1/2)\), independently of \(\Theta\). Hence the conditional law of \(S_n\) is the same for \(\Theta=0\) and \(\Theta=1\), so \(S_n\) is independent of \(\Theta\). Since \(Y^\dagger=\Theta\) almost surely, \(S_n\) is also independent of \((\Theta,Y^\dagger)\).

It follows that
\[
\mathsf E_n=I(\Theta;Y^\dagger\mid S_n)=I(\Theta;Y^\dagger)=H(\Theta)=\log 2.
\]
Moreover, \(Y^\dagger\) is determined by \(\Theta\), and therefore
\[
\mathsf A_n=H(Y^\dagger\mid\Theta,S_n)=0,
\qquad
H(Y^\dagger\mid S_n)=\log 2.
\]

Now consider any finite number \(k\) of acquisitions from \(\mathcal C_\rho\). Their inputs are again \(0\) almost surely and their labels are independent \(\operatorname{Bernoulli}(1/2)\) variables under either value of \(\Theta\). Thus \((S_n,Z_{1:k})\) is independent of \((\Theta,Y^\dagger)\), and
\[
I(\Theta;Y^\dagger\mid S_n,Z_{1:k})=\log 2.
\]
This holds for every admissible finite \(k\), including \(k=0\), so taking the infimum gives
\[
\mathsf E^{\mathcal C_\rho}_\infty=\log 2.
\]

On the other hand, let \(Z=(1,Y)\) be the acquisition available in \(\mathcal C_1\). By the observation model at input \(1\), \(Y=\Theta\) almost surely. Consequently \(\Theta\), and hence \(Y^\dagger\), is measurable with respect to \(Z\). Therefore
\[
I(\Theta;Y^\dagger\mid S_n,Z)=0,
\]
and the plan using this single acquisition proves \(\mathsf E^{\mathcal C_1}_\infty=0\).

Thus the uncertainty is not aleatoric according to the conditional-entropy term, is not reducible by any amount of deployment-distribution data, and is reducible by a different acquisition mechanism. It is therefore a mechanism-reducible epistemic type that is omitted by the proposed aleatoric-versus-deployment-sample-reducible dichotomy.

Finally, the mutual-information convention labels an amount \(\mathsf E_n=\log 2\) as epistemic, with aleatoric amount \(\mathsf A_n=0\). The deployment-reducibility convention instead regards this same persistent amount as non-epistemic, because \(\mathsf E^{\mathcal C_\rho}_\infty=\log 2\); in a binary partition it must consequently be assigned to the aleatoric side. That assignment contradicts \(\mathsf A_n=0\). Hence no two-way classification can satisfy both stated conventions simultaneously.
