# Reference Proof

## Proof Obligations

The proof must establish: (1) the LP and regularizers are well defined in the stated domain; (2) the independently parameterized LP value is differentiable in the local basis regime; (3) the full gap derivative separates into fixed-bound and bound-mediated terms; (4) the normalized width derivative includes the entire IBP recursion; and (5) the defined implementation surrogate has the stated uniform coefficients. All five obligations are derived below. Dual sensitivity and the implementation proxy are additional verified explanations, not additional public targets.

## Complete Proof

### Well-definedness and local LP sensitivity

All input bounds and parameters are finite, the batch is nonempty, and the number of hidden neurons is positive. Interval arithmetic gives valid preactivation bounds inductively: a positive weight multiplies the lower input bound in the lower preactivation estimate and the upper bound in the upper estimate, while a negative weight reverses those choices. Applying the nondecreasing ReLU preserves the postactivation interval enclosure. Thus each true forward pass at a batch input is feasible for the big-M relaxation: choose the corresponding integral activation indicators. This also gives \(V_i\leq f_\theta(x_i)\).

The LP output is bounded. Each hidden output satisfies \(0\leq\hat x_j^{(l)}\leq U_j^{(l)}a_j^{(l)}\leq\max\{U_j^{(l)},0\}\), and the affine equalities then bound every preactivation and the output. Consequently the nonempty finite-dimensional closed feasible set has an attained finite output minimum.

Write the independently parameterized value as
\[
\bar V_i(\theta;L,U),\qquad
\bar\delta_i(\theta;L,U)=f_\theta(x_i)-\bar V_i(\theta;L,U).
\]
The objective selects the output variable, so its vector \(c\) is constant even though the output-layer weights and bias belong to \(\theta\). Any parameter-independent variable bounds can be included as rows \(Hy\leq r\).

Let \(p=(\theta,L,U)\). In the stated local optimal-basis regime, the basic solution is obtained by solving a nonsingular system \(M(p)y^*(p)=q(p)\), after fixing or eliminating nonbasic and fixed coordinates as appropriate. The independently parameterized LP data are smooth. Matrix inversion is smooth wherever the determinant is nonzero; hence \(y_i^*(p)\) and \(\bar V_i(p)=c^Ty_i^*(p)\) are smooth locally. The basis remains optimal by the assumed local basis condition. This argument supplies the independent-bound partial derivatives required in the public claim.

For completeness, the dual formula is derived with the source's printed convention. Include fixed variable-bound multipliers \(\eta\) in
\[
\mathcal L=c^Ty+\nu^T(A_{eq}y-b_{eq})+\mu^T(Gy-h)+\eta^T(Hy-r),\qquad \mu,\eta\geq0.
\]
Stationarity gives
\[
c+A_{eq}^T\nu+G^T\mu+H^T\eta=0.
\]
For any infinitesimal change in the independent LP data, equality feasibility gives
\[
A_{eq}\,dy^*=db_{eq}-(dA_{eq})y^*.
\]
Differentiating the active inequalities and using zero multipliers on inactive inequalities gives
\[
\mu^TG\,dy^*=\mu^Tdh-\mu^T(dG)y^*.
\]
Fixed active bound rows have \(H\,dy^*=0\); inactive rows have zero multipliers, so \(\eta^TH\,dy^*=0\). Therefore
\[
\begin{aligned}
d\bar V_i
&=c^Tdy_i^*\\
&=-\nu^TA_{eq}\,dy_i^*-\mu^TG\,dy_i^*-\eta^TH\,dy_i^*\\
&=-\nu^Tdb_{eq}+\nu^T(dA_{eq})y_i^*
  +\mu^T(dG)y_i^*-\mu^Tdh.
\end{aligned}
\]
Both channel signs follow from stationarity. In particular, the inequality signs are the reverse of those retained in the previous reference proof.

### Exact gap decomposition

On a branch where both the forward network outputs and IBP bounds are differentiable,
\[
\delta_i(\theta)=\bar\delta_i(\theta;L(\theta),U(\theta)).
\]
The ordinary multivariable chain rule yields
\[
\nabla_\theta\delta_i
=D_{\rm fix}\delta_i+
\sum_{l=1}^L\sum_{j=1}^{n_l}
\left(
\frac{\partial\bar\delta_i}{\partial L_j^{(l)}}\nabla_\theta L_j^{(l)}+
\frac{\partial\bar\delta_i}{\partial U_j^{(l)}}\nabla_\theta U_j^{(l)}
\right).
\]
Here all independent-argument derivatives are evaluated at the current bounds. The forward output has no dependence on the independent bound arguments, so these bound partial derivatives are the negatives of the corresponding value partial derivatives. Averaging over the fixed batch proves the public total-derivative decomposition.

With \(L,U\) held fixed, \(G,h,H,r\) have zero parameter derivatives. Thus the direct value derivative is
\[
D_{\rm fix}\bar V_i
=-\nu^T\nabla_\theta b_{eq}
+\nu^T(\nabla_\theta A_{eq})y_i^*.
\]
For a layer equality \(z_j^{(l)}-W_j^{(l)}\hat x^{(l-1)}=b_j^{(l)}\), including the output layer, this gives
\[
\frac{\partial\bar V_i}{\partial b_j^{(l)}}\bigg|_{L,U}=-\nu_j^{(l)},\qquad
\frac{\partial\bar V_i}{\partial W_{jk}^{(l)}}\bigg|_{L,U}=-\nu_j^{(l)}\hat x_k^{(l-1)*}.
\]
Consequently
\[
D_{\rm fix}R_{LP}
=\frac1{|B|}\sum_{i\in B}
\left(\nabla_\theta f_\theta(x_i)-D_{\rm fix}\bar V_i\right).
\]
The forward-output term and batch normalization cannot be omitted.

The actual bound coefficients can also be checked directly. Give multipliers \(\mu_{c,i}^{(l,j)}\) and \(\mu_{d,i}^{(l,j)}\) to the rows
\[
\hat x-z+L(1-a)\leq0,\qquad \hat x-Ua\leq0.
\]
The correctly signed envelope formula gives
\[
\frac{\partial\bar V_i}{\partial L_j^{(l)}}
=\mu_{c,i}^{(l,j)}(1-a_{i,j}^{(l)*}),\qquad
\frac{\partial\bar V_i}{\partial U_j^{(l)}}
=-\mu_{d,i}^{(l,j)}a_{i,j}^{(l)*}.
\]
Thus the minimum-gap coefficients are
\[
\frac{\partial\bar\delta_i}{\partial L_j^{(l)}}
=-\mu_{c,i}^{(l,j)}(1-a_{i,j}^{(l)*}),\qquad
\frac{\partial\bar\delta_i}{\partial U_j^{(l)}}
=\mu_{d,i}^{(l,j)}a_{i,j}^{(l)*}.
\]
The gap coefficients, rather than bare inequality multipliers, are what enter the exact decomposition.

### Width differentiation and nonsmooth interpretation

The total differentials of the IBP formulas on a smooth branch obey the product rule. Suppressing indices for one row,
\[
dL=dW^+\ell+W^+d\ell+dW^-u+W^-du+db,
\]
\[
dU=dW^+u+W^+du+dW^-\ell+W^-d\ell+db.
\]
The differentials of previous-layer postactivation bounds are obtained from their selected ReLU branches. Starting with fixed input bounds, whose differentials vanish, this recursion differentiates every layer and includes all upstream dependence. It does not treat the previous-layer intervals as constants.

Since \(N_h\) is fixed,
\[
\nabla_\theta R_{BW}
=\frac1{N_h}\sum_{l=1}^L\sum_{j=1}^{n_l}
\left(\nabla_\theta U_j^{(l)}-\nabla_\theta L_j^{(l)}\right).
\]
The IBP maps and fixed-input network outputs are locally Lipschitz and piecewise polynomial in the joint parameter vector. On a common smooth branch their derivatives have the limiting values specified in the public task. The independently parameterized LP value derivatives are continuous in the local basis regime. Taking a simultaneous branch limit in the already proved identities therefore preserves every equality. Taking the same convex-combination weights in every term also preserves the equalities and gives the stated matched generalized-gradient interpretation. This does not assert a chain rule for independently chosen subgradients or an ordinary derivative at a kink.

### Surrogate identity

By definition,
\[
\nabla^{\rm sur}_\theta(R_{LP}+\alpha R_{BW})
=D_{\rm fix}R_{LP}+\alpha\nabla_\theta R_{BW}.
\]
Substituting the normalized width derivative proves
\[
\nabla^{\rm sur}_\theta(R_{LP}+\alpha R_{BW})
=D_{\rm fix}R_{LP}+\frac\alpha{N_h}
\sum_{l=1}^L\sum_{j=1}^{n_l}
(\nabla_\theta U_j^{(l)}-\nabla_\theta L_j^{(l)}).
\]
In the exact gap decomposition, the coefficient of each bound gradient is its batch-averaged gap sensitivity. In the surrogate, those coefficients are replaced by \(-\alpha/N_h\) and \(+\alpha/N_h\). This is an exact identity for the defined implementation surrogate. It is not an identity for the ordinary total derivative of the combined numerical regularizer and supplies no quantitative approximation-error bound.

### Optional implementation and directional checks

With both the LP primal values and duals detached, define
\[
P_i(\theta)=-\sum_{l=1}^{L+1}(\nu_i^{(l)})^T
(W^{(l)}\hat x_i^{(l-1)*}+b^{(l)}).
\]
Its derivatives reproduce the fixed-bound value sensitivities above. The expression \(P_i-\operatorname{sg}(P_i)+\operatorname{sg}(V_i)\) returns \(V_i\) forward and differentiates \(P_i\) backward. Subtracting this proxy from the forward network output implements the minimum-gap fixed-bound derivative.

For the maximum direction, define \(\delta_i^{\max}=V_i^{\max}-f_\theta(x_i)\). Applying the same independent-argument chain rule, with this gap's signs and a fixed-bound maximization-value derivative, gives the analogous decomposition and uniform-width surrogate. These observations are not additional requirements for proving the public minimum-direction theorem.
