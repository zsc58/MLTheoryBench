# Reference Proof

## Audited obligations

The proof must establish: (i) the marginal sampler's endpoint estimate in its observed path filtration, not merely a one-time posterior; (ii) identification of this estimate with a conditional expectation under the true forward law; (iii) the reverse drifts and a justified full-horizon entropy identity; (iv) the nested-projection comparison and its strictness implication. The terminal boundary and initialization integrability must also be checked. All these obligations are closed below.

## Preliminary full-horizon and regularity check

This check is essential for interpreting the actual assumptions. Let \(\mathcal X=\{e_v:v\in\mathcal V\}^L\), and let \(S\subseteq\mathcal X\) be the support of \(X_0\). For every \(s>0\) and every finite state \(z\), the Gaussian likelihood of \(z\) is strictly positive for every \(a\in S\). Consequently each \(a\in S\) has strictly positive posterior probability given \(X_s=z\).

Suppose \(S\) contains at least two different sequences. Some block \(l\) then takes at least two different one-hot values on \(S\). For every \(s>0\) and every \(z\), the block \(m_{s,l}(z)\) has at least two positive coordinates, and hence is not one-hot.

The final grid interval has starting noise level \(v=u_{K-1}>0\). By its pinned endpoint definition, the mean-endpoint sampler satisfies
\[
 \widehat Y^{\rm mean}_T
 =m_v(\widehat Y^{\rm mean}_{t_{K-1}}).
\]
It therefore assigns probability zero to the event \(\{\omega:\omega(T)\in\mathcal X\}\), whereas the true path law assigns this event probability one. This contradicts \(P\ll Q^{\rm mean}\). Thus, under the public assumptions,
\[
 X_0=a\quad\text{almost surely}
\]
for one fixed \(a\in\mathcal X\).

In this case every posterior is concentrated on \(a\), for every positive noise level and every state. Both samplers therefore use exactly the same bridge-to-\(a\) dynamics. Concatenating these bridge segments gives the same conditional full-path law as the true reversed OU process, conditional on its initial state. Denote this common conditional path kernel by \(H_y\). Then
\[
 P=\int H_y\,\lambda_T(dy),\qquad
 Q^{\rm mar}=Q^{\rm mean}=\int H_y\,\pi_T(dy).
\]
If \(f=d\lambda_T/d\pi_T\), these disintegrations show directly that
\[
 \frac{dP}{dQ^{\rm mar}}(\omega)
 =\frac{dP}{dQ^{\rm mean}}(\omega)
 =f(\omega(0))
\]
up to the respective null sets. Hence both path entropies equal the finite quantity
\[
 C=\mathrm{KL}(\lambda_T\|\pi_T).
\]
All three conditional dynamics have the same drift on \([0,T)\). Their drift differences are zero, their Girsanov stochastic exponentials are identically one, and every Novikov and drift-difference integrability requirement used below is satisfied. This verifies, rather than merely invokes, the full-horizon regularity needed in the original comparison argument. It also explains why no additional unnamed Novikov assumption is needed in the repaired public formulation.

The source introduces a numerical difference of the path entropies. Finite initialization entropy makes that subtraction well-defined. This must not be replaced by an unqualified subtraction of two possibly infinite quantities.

The argument above already proves the weak inequality. It also shows that the strictness antecedent cannot occur under the full-horizon assumptions. For completeness, the source's posterior-identification and projection argument is retained and justified next.

## 1. Endpoint filtering in the observed path filtration

Fix a grid interval and put \(v=u_k\). Condition on its starting state \(y\). Use \(A\) for the endpoint drawn under the marginal sampler, and keep its conditional expectations distinct from conditional expectations under the true forward law.

For \(0<u<v\), conditioning on the current bridge state suffices for filtering \(A\), even when the whole observed bridge history is available. To verify this, write a forward-time partition
\[
 u=r_0<r_1<\cdots<r_n=v,
 \qquad z_0=z,\quad z_n=y,
\]
and let \(g_h(\cdot\mid\cdot)\) be the OU transition density over duration \(h\). Conditional on endpoint \(a\) and final state \(y\), the density of the bridge observations contains the factor
\[
 \frac{g_u(z\mid a)\prod_{i=1}^n
 g_{r_i-r_{i-1}}(z_i\mid z_{i-1})}{g_v(y\mid a)}.
\]
Dividing this by the bridge likelihood of the current state,
\[
 \frac{g_u(z\mid a)g_{v-u}(y\mid z)}{g_v(y\mid a)},
\]
leaves an expression independent of \(a\). Thus the portion of the path already observed in reverse time supplies no further endpoint information once \(y\) and \(z\) are known. Finite-dimensional conditioning extends to the continuous observed segment because continuous paths are determined by observations at a countable dense set of times. Fresh randomness at the grid point ensures that earlier grid-interval history supplies no additional information conditional on \(y\).

Conditional on \(y\), the marginal sampler has product endpoint prior and independent coordinate-block bridge likelihoods. Its conditional distribution of \(A_l\), given the full current state and the observed history, therefore depends only on \(y\) and the current block \(z_l\). The prior for this block is exactly
\[
 \mathcal L(X_{0,l}\mid X_v=y).
\]
Under the true forward law, conditional on \(X_v=y\) and \(X_{0,l}\), the bridge likelihood for \(X_{u,l}=z_l\) depends only on \(X_{0,l}\) and \(y_l\), with the same Gaussian formula. Bayes' rule consequently identifies the two posterior means:
\[
 \bar m_{k,u,l}(y,z_l)
 :=\mathbb E[X_{0,l}\mid X_v=y,X_{u,l}=z_l].
\]
This is an equality of posterior-mean functions; it does not assert equality of the full joint laws of the two processes.

For a latent-endpoint bridge, projecting its drift onto the observed filtration replaces the endpoint by its conditional mean in that filtration. Indeed, subtracting this projected drift gives an observed continuous local martingale with quadratic variation \(2tI_D\), and hence Brownian innovation with diffusion coefficient \(\sqrt2I_D\). On every interval bounded away from \(T\), the bounded endpoints ensure the local integrability needed for this argument. The history calculation above therefore justifies using \(\bar m_{k,u}\) in the actual observed path drift, rather than only in a one-time marginal description.

## 2. Reverse drifts and the entropy identities

Write \(u=T-t\). The reverse-time OU formula and the score identity in the supplied source give
\[
 b_t^\star(z)
 =\frac{m_u(z)-z\cosh u}{\sinh u}.
\]
The mean-endpoint bridge drift on the interval is
\[
 b_t^{\rm mean}(z;y)
 =\frac{m_{u_k}(y)-z\cosh u}{\sinh u},
\]
and the preceding filtering argument gives
\[
 b_t^{\rm mar}(z;y)
 =\frac{\bar m_{k,u}(y,z)-z\cosh u}{\sinh u}.
\]
All these are drifts in the respective observed path filtrations; the sampled endpoint is not added to the path-space information used in the KL comparison.

The standard equal-diffusion Girsanov entropy identity has coefficient \(1/4\) when the diffusion coefficient is \(\sqrt2I_D\). More explicitly, when the initial density is \(f\), the admissible likelihood representation under the true law is
\[
 \log\frac{dP}{dQ}
 =\log f(Y_0)
 +\frac1{\sqrt2}\int_0^T(b_t^\star-b_t^Q)\cdot dB_t^P
 +\frac14\int_0^T\|b_t^\star-b_t^Q\|^2dt.
\]
If the stochastic integral has mean zero and the displayed terms are integrable, taking expectation gives the entropy identity. Here those qualifications are explicitly verified by the preliminary argument: the drift differences and stochastic integrals vanish, the change-of-drift exponential is one, and the likelihood is exactly \(f(Y_0)\) with finite entropy. Thus there is no unresolved global Girsanov application or limiting argument at \(T\).

Since
\[
 \frac1{4\sinh^2u}=\frac{c_u^2}{\sigma_u^4},
\]
we obtain, with expectations under the true forward law,
\[
 \mathrm{KL}(P\|Q^{\rm mean})
 =C+\sum_k\int_{t_k}^{t_{k+1}}
 \frac{c_u^2}{\sigma_u^4}
 \mathbb E\|m_u(X_u)-m_{u_k}(X_{u_k})\|^2dt,
\]
and
\[
 \mathrm{KL}(P\|Q^{\rm mar})
 =C+\sum_k\int_{t_k}^{t_{k+1}}
 \frac{c_u^2}{\sigma_u^4}
 \sum_l\mathbb E\|m_{u,l}(X_u)-\bar m_{k,u,l}\|^2dt.
\]
Integrands are defined at interior times; changing their value at the finitely many grid endpoints has no effect. Their integrability on the full horizon has been checked, not inferred from ignoring the endpoint \(u=0\).

## 3. Projection comparison and strictness

Fix an interior time and a block \(l\), and set
\[
 M_l=\mathbb E[X_{0,l}\mid X_u],\qquad
 \mathcal G=\sigma(X_{u_k}),\qquad
 \mathcal H_l=\sigma(X_{u_k},X_{u,l}).
\]
The Markov relation \(X_0\to X_u\to X_{u_k}\) gives
\[
 \mathbb E[X_{0,l}\mid X_u,X_{u_k}]=M_l.
\]
Both \(\mathcal G\) and \(\mathcal H_l\) are sub-sigma-algebras of \(\sigma(X_u,X_{u_k})\). Applying the tower property therefore yields
\[
 \mathbb E[M_l\mid\mathcal G]
 =\mathbb E[X_{0,l}\mid X_{u_k}],\qquad
 \mathbb E[M_l\mid\mathcal H_l]
 =\bar m_{k,u,l}.
\]
The one-hot variables and all their conditional means are bounded, so the required square integrability holds.

Because \(\mathcal G\subseteq\mathcal H_l\), write
\[
 M_l-\mathbb E[M_l\mid\mathcal G]
 =\bigl(M_l-\mathbb E[M_l\mid\mathcal H_l]\bigr)
 +\bigl(\mathbb E[M_l\mid\mathcal H_l]-\mathbb E[M_l\mid\mathcal G]\bigr).
\]
The cross term has zero expectation by conditioning on \(\mathcal H_l\). Hence
\[
 \mathbb E\|M_l-\mathbb E[M_l\mid\mathcal G]\|^2
 -\mathbb E\|M_l-\mathbb E[M_l\mid\mathcal H_l]\|^2
 =\mathbb E\|\bar m_{k,u,l}-m_{u_k,l}(X_{u_k})\|^2\ge0.
\]
Summing over blocks, multiplying by the positive interior weight, and integrating compares the two entropy identities. Their finite common initialization term can be subtracted, proving the required weak inequality.

If the stated strictness antecedent holds, then on a set of times of positive Lebesgue measure at least one of the last squared norms has strictly positive expectation. Its positively weighted integral is therefore strictly positive, giving the asserted strict inequality. Measurability follows from the finite Gaussian posterior formulas at interior times.

Finally, the preliminary full-horizon check shows that, for the actual admissible one-hot models in this task, \(X_0=a\) almost surely. All conditional endpoint means then equal \(a_l\), so the strictness antecedent is never satisfied. The strict implication remains correct but is vacuous in this full-horizon setting. This is not a license to change the task to an early-stopped horizon or to drop its path-space absolute-continuity assumption.
