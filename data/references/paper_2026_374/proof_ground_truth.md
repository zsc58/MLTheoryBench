# Reference Proof

Work with the projected dynamics and payoff in the problem. No assertion equating them to a separately sampled-action model is needed.

Fix \(\pi\) as in the task and abbreviate \(J=J^\pi\), \(G=G^\pi\). At a preterminal triple define, for densities with finite displayed integrals,
\[
 \Phi(\rho)=\int_A\bigl(G(a)+\gamma\ell_p(\rho(a))\bigr)\rho(a)\,da.
\]
For every admissible density used below these integrals are finite: the coefficients multiplying derivatives are bounded at the fixed state, \(r\) has polynomial action growth, and admissibility controls action moments and integrated entropy. Equation (1) says \(J_t-\beta J+\Phi(\pi)=0\).

Suppose \(p>1\). Put \(c=\gamma/(p-1)\) and \(f_a(z)=(G(a)+c)z-cz^p\), \(z\geq0\). This function is strictly concave. For the normalized density \(\rho_*\) in (2), \(cp\rho_*(a)^{p-1}=(G(a)+\lambda)_+\). Thus \(f_a'(\rho_*(a))=c-\lambda\) wherever \(\rho_*>0\), while \(f_a'(0)=G(a)+c\leq c-\lambda\) wherever \(\rho_*=0\). The supporting-line inequality for \(f_a\), integrated against any admissible density \(\rho\), gives
\[
 \Phi(\rho)-\Phi(\rho_*)
 \leq\int_A f_a'(\rho_*(a))(\rho(a)-\rho_*(a))\,da\leq0.
\]
Indeed, on \(\{\rho_*>0\}\) the derivative is the constant \(c-\lambda\); on its complement \(\rho\geq0\) and the derivative is no larger; both densities have mass one. This also proves uniqueness up to null sets among densities with finite objective. It directly justifies the positive-part boundary case, without requiring strict positivity of the optimizer at every action. For \(p=1\), put \(\rho_*(a)=e^{G(a)/\gamma}/Z\). The Gibbs identity
\[
 \Phi(\rho)=\gamma\log Z-\gamma\,\mathrm{KL}(\rho\|\rho_*)
\]
shows the same maximality. Therefore, for \(\pi'=\mathcal T_p\pi\),
\[
 \Phi_{t,x,i}(\pi'(\cdot\mid t,x,i))\geq
 \Phi_{t,x,i}(\pi(\cdot\mid t,x,i))\quad(t<T).\tag{4}
\]

Here are the integrability details for the stochastic comparison. Uniform linear growth of \(b,\sigma\) implies \(|B^\rho(t,x,i)|\leq C(1+|x|)\) and \(\|\overline\sigma^\rho(t,x,i)\|^2\leq C'(1+|x|)^2\) for an admissible \(\rho\). Its stipulated strong solution consequently satisfies, by BDG and Gronwall, for every \(n\geq2\),
\[
 \mathbb E_{t,x,i}\bigl[\sup_{t\leq s\leq T}|X_s^\rho|^n\bigr]
 \leq C_n(1+|x|^n).\tag{5}
\]
The action-moment, entropy, and reward bounds imply that the integrated running payoff of each such policy has an absolute polynomial-growth bound. Applying (5) to the payoff representation of \(J^\pi\) yields \(|J^\pi(s,y,j)|\leq C(1+|y|^m)\), uniformly in \((s,j)\), for some \(m\). These bounds also make every payoff in the comparison finite.

Take \(t<T\) and run the state under \(\pi'\). Apply the regime-switching Itô formula to \(e^{-\beta(s-t)}J(s,X_s^{\pi'},R_s)\), adding the accumulated discounted running payoff under \(\pi'\). Its Brownian and compensated-chain terms are local martingales. Its drift is
\[
 e^{-\beta(s-t)}\bigl[J_t-\beta J+\Phi_{s,X_s^{\pi'},R_s}(\pi')\bigr]
 =e^{-\beta(s-t)}\bigl[\Phi_{s,X_s^{\pi'},R_s}(\pi')
 -\Phi_{s,X_s^{\pi'},R_s}(\pi)\bigr]\geq0.\tag{6}
\]
Choose stopping times \(\tau_n\uparrow T\) that keep the state in a ball of radius \(n\) and stop before \(T\). On each stopped interval the derivatives of \(J\) are bounded on the relevant compact set, so the Brownian and finite-state compensated-jump integrals are true stopped martingales. Taking expectations in (6) gives
\[
\begin{aligned}
 J(t,x,i)\leq\mathbb E_{t,x,i}\Bigl[&e^{-\beta(\tau_n-t)}J(\tau_n,X_{\tau_n}^{\pi'},R_{\tau_n})\\
 &+\int_t^{\tau_n}e^{-\beta(s-t)}\int_A
 \bigl(r(s,X_s^{\pi'},R_s,a)+\gamma\ell_p(\pi'(a\mid s,X_s^{\pi'},R_s))\bigr)
 \pi'(a\mid s,X_s^{\pi'},R_s)\,da\,ds\Bigr].\tag{7}
\end{aligned}
\]
The stopped terminal term is \(J(\tau_n,\cdot)\), not \(h\). Its polynomial bound and (5), and the corresponding bound on the running payoff, supply integrable domination (hence uniform integrability). Continuity of \(J\) up to \(T\) and \(J(T,y,j)=h(y)\) then permit passage to the limit in (7). This proves \(J^\pi(t,x,i)\leq J^{\pi'}(t,x,i)\). At \(t=T\), both values equal \(h(x)\).

For the fixed-point assertion write \(J^*=J^{\pi^*}\). The pointwise argument gives \(\Phi^*_{t,x,i}(\rho)\leq\Phi^*_{t,x,i}(\pi^*)\) for every admissible competitor's density, because \(\pi^*=\mathcal T_p\pi^*\) at \(t<T\). The fixed-policy equation therefore yields
\[
 J_t^*(t,x,i)-\beta J^*(t,x,i)+\Phi^*_{t,x,i}(\rho)\leq0.\tag{8}
\]
Apply the same stopped Itô calculation to \(J^*\) along the projected state under an arbitrary admissible \(\rho\). The drift after adding that policy's running payoff is nonpositive by (8). The polynomial bound for \(J^*\) follows from its payoff representation, so (5) and the running-payoff bound justify the same terminal and integral limits. Hence \(J^\rho(t,x,i)\leq J^*(t,x,i)\) for every admissible \(\rho\). Equality holds when \(\rho=\pi^*\), proving the asserted supremum, including the terminal case.
