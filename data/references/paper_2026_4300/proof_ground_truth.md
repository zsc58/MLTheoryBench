# Reference Proof

## Proof Structure

Bound all true trajectories from the compact initial set in a common compact state region. Approximate the drift and control matrix separately there by shallow ReLU networks with time-independent parameters. A first-contact argument keeps the approximating trajectories in that region, and a Lipschitz error decomposition followed by Gronwall gives the required uniform trajectory error.

## Standard Results Used

1. **Caratheodory existence and uniqueness.** If a vector field is measurable in time, continuous in the state, globally Lipschitz in the state with an integrable Lipschitz bound, and its value at state zero has an integrable bound, then each initial state has a unique absolutely continuous solution on the finite time interval. The equation holds almost everywhere. The resulting linear growth estimate excludes finite-time blow-up.
2. **Gronwall.** If a nonnegative continuous function satisfies \(v(t)\le a(t)+C\int_0^t v(s)\,ds\), where \(C\ge0\) and \(a\) is nonnegative and nondecreasing, then \(v(t)\le a(t)e^{Ct}\).
3. **Scalar shallow-ReLU universal approximation.** For a compact set \(D\subset\mathbb R^n\), a continuous scalar function \(h\) on \(D\), and \(\delta>0\), a finite sum \(\sum_r c_r\sigma(\langle a_r,x\rangle+b_r)\) approximates \(h\) uniformly on \(D\) within \(\delta\). No width bound is asserted. These are the standard-independent tools indexed by theory_017 and theory_018.

## Complete Proof

If \(K=\varnothing\), choose any positive widths and zero output weights. There are no initial states to check, so the conclusion is vacuous. Assume henceforth that \(K\ne\varnothing\).

Let
\[
F_0=\sup_{t\in[0,T]}\|f(0,t)\|,\qquad
G_0=\sup_{t\in[0,T]}\|G(0,t)\|_{\mathrm{op}},
\]
which are finite by continuity, and put
\[
R_0=\max_{z_0\in K}\|z_0\|,\qquad B=F_0+MG_0,\qquad C=L_f+ML_g.
\]
The controlled target field is measurable in time for each fixed state and continuous in the state. For almost every time it is globally state-Lipschitz with constant \(C\), and its norm at zero is bounded by \(B\). Thus the stated Caratheodory theorem applies uniformly to every admissible control. Changes to a control on a null set do not change the integral equation or its solution.

For each true trajectory,
\[
\|z(t)\|\le R_0+Bt+C\int_0^t\|z(s)\|\,ds.
\]
Gronwall gives \(\|z(t)\|\le(R_0+Bt)e^{Ct}\). Define
\[
R_*=(R_0+(B+1+M)T)e^{CT},\qquad
K_T=\{x\in\mathbb R^d:\|x\|\le R_*\}.
\]
In particular every true trajectory lies in \(K_T\). This ball and its product with \([0,T]\) are compact and independent of the individual initial state and control.

Set
\[
\eta=\min\left\{1,\frac{\varepsilon}{2(1+M)Te^{CT}}\right\}>0.
\]
Apply scalar shallow-ReLU universal approximation on \(D=K_T\times[0,T]\) to each component of \(f\) with tolerance \(\eta/\sqrt d\), and to each entry of \(G\) with tolerance \(\eta/\sqrt{dm}\). The required functions are continuous on the compact domain.

Here is the finite-output assembly explicitly. For each scalar approximation to a component of \(f\), place its scalar output coefficient in that component of a vector output weight and put zeros in the other components. Concatenate all these finite lists of ridge functions. The resulting vector network is of the required architecture: for each ridge, repeat its affine state-time feature across the rows of the hidden block and use the specified vector output weight. Do the same for \(G\), placing each scalar coefficient in its designated matrix entry and zero elsewhere. Concatenating all the matrix-entry lists produces one matrix-output network; repeat each affine feature across its rows to put it in the stated architecture. All parameters are constant in time. The two constructions are independent and yield finite widths \(P,Q\), padded with zero output weights if necessary to make them positive.

The coordinate error bounds imply
\[
\sup_D\|f_\Theta-f\|\le\eta,
\qquad
\sup_D\|G_\Phi-G\|_{\mathrm{op}}
\le\sup_D\|G_\Phi-G\|_F\le\eta.
\]
This assembly uses no quantitative approximation rate and no assertion that separately selected scalar approximants already have the same ridge directions.

Every finite network just constructed is globally Lipschitz in the state variable, uniformly in time: each ReLU ridge has state Lipschitz constant at most the norm of its state coefficient, and a finite weighted sum has a finite Lipschitz constant. For the matrix field one can use the Frobenius norm to bound the operator norm. Denote suitable constants by \(L_\Theta,L_\Phi\). Both neural fields at state zero are bounded on \([0,T]\), since they are continuous there. Hence for each admissible control the neural controlled field is measurable in time, globally state-Lipschitz with constant \(L_\Theta+ML_\Phi\), and has a uniform linear growth bound. The same Caratheodory theorem gives its unique solution on all of \([0,T]\). No width-independent bound on these neural Lipschitz constants is needed.

Fix arbitrary \(z_0\in K\) and \(u\in U_M\), and write \(y\) for this neural solution. As long as \(y(s)\in K_T\), the approximation estimates and \(\eta\le1\) give, for almost every \(s\),
\[
\|f_\Theta(y(s),s)+G_\Phi(y(s),s)u(s)\|
\le B+1+M+C\|y(s)\|.
\]
Thus, on any initial interval during which the path remains in \(K_T\),
\[
\|y(t)\|\le (R_0+(B+1+M)t)e^{Ct}=:r(t).
\]
The function \(r\) is strictly increasing because \(B+1+M>0\) and \(C\ge0\). Also \(r(0)=R_0<R_*=r(T)\), so the initial state is strictly inside \(K_T\). If the continuous path first reached its boundary at some \(\tau<T\), the preceding inequality would apply through \(\tau\) and give
\[
R_*=\|y(\tau)\|\le r(\tau)<r(T)=R_*,
\]
a contradiction. Any departure before or at \(T\) would require a boundary contact before \(T\). Continuity at \(T\) therefore proves \(y(t)\in K_T\) throughout the interval. This supplies the strict margin missing from an argument based only on continuity of non-strict discrepancy bounds.

Set \(e(t)=\|y(t)-z(t)\|\). Both paths now lie in \(K_T\). Subtract their integral equations and add and subtract \(f(y(s),s)\) and \(G(y(s),s)\). The target state differences are bounded by \(L_f e(s)\) and \(L_g e(s)\), while the field-approximation differences along \(y\) are bounded by \(\eta\). Consequently,
\[
e(t)\le\int_0^t\bigl[Ce(s)+(1+M)\eta\bigr]ds.
\]
Gronwall yields
\[
e(t)\le(1+M)\eta t e^{Ct}
\le(1+M)\eta T e^{CT}
\le\varepsilon/2\le\varepsilon.
\]
All choices preceding the fixing of \(z_0,u\) depend only on the fixed problem data and \(\varepsilon\), not on either individual trajectory. Thus one pair of networks gives the required bound for every initial state and every admissible control. The proof also directly covers \(M=0\) and \(C=0\).

## Source-Local Repairs and Obligation Closure

The source enclosure inequality must include the integral of the unit drift discrepancy, namely \(+t\). For the source's original radius \(R(t)\), all terms in its bracket are nonnegative and nondecreasing, and the term \((1+M)t\) makes the radius strictly increasing. The same first-contact argument therefore proves the original enclosure lemma with its original radius; the simpler larger radius used above preserves the reference proof's presentation. The true reachable set is a set of states contained in \(K_T\); only its state-time lift is contained in \(K_T\times[0,T]\).

The source's qualitative matrix-approximation invocation is replaced by the finite concatenation just derived. Since widths are existential and unrestricted, this is a local repair, not a use of the quantitative shared-dictionary claim. It neither assumes nor establishes any prescribed-width rate.

All theorem-critical obligations are closed: well-posedness and control-equivalence semantics; uniform target growth; approximation in the required vector and operator norms by the stated architecture; enclosure of the neural paths; and uniform Gronwall error propagation. No nonstandard external dependency or unresolved proof obligation remains.
