# Reference Proof

## Proof Structure

The theorem-critical obligations are: well-defined predictions and normalized integrals; the full/leave-one-out level-set sandwich; the loss bound at each good tolerance; the median-majority comparison under each permitted monotonicity condition; and the final summation and normalization. All are established below without external results. The sandwich is also available directly from the definition of a good tolerance, so deriving it again is optional for a solution.

## Complete Proof

The sample size and grid cardinality are positive. The assumed finite positive measures of the leave-one-out level sets make every aggregation call valid. Measurability and boundedness of the loss make its integrals over finite-measure sets finite. The prescribed objects and the definition of each leave-one-out level set ensure that prediction at index i does not use the held-out response.

Write \(L_*:=\min_{h\in\mathcal H}L_S(h)\). Fix a full-sample minimizer \(h_*\) and, for each \(i\), a leave-one-out minimizer \(h_{*,i}\). Since \(0\leq\ell\leq\Delta\),
\[
L_*-\Delta\leq L_{S_{-i}}(h_{*,i})\leq L_*.
\]
Indeed, the upper bound follows by comparing with \(h_*\), and the lower bound follows from \(L_*\leq L_S(h_{*,i})\leq L_{S_{-i}}(h_{*,i})+\Delta\).

If \(h\in H_{t,i}\), then
\[
L_{S_{-i}}(h)\leq L_{S_{-i}}(h_{*,i})+t\leq L_*+t,
\]
so \(L_S(h)\leq L_*+t+\Delta\), hence \(h\in H_{t+\Delta}\). If \(t\geq\Delta\) and \(h\in H_{t-\Delta}\), then
\[
L_{S_{-i}}(h)\leq L_S(h)\leq L_*+t-\Delta\leq L_{S_{-i}}(h_{*,i})+t,
\]
so \(h\in H_{t,i}\). For \(0\leq t<\Delta\), the lower inclusion holds because \(H_{t-\Delta}=\varnothing\). Thus the sandwich holds for every nonnegative tolerance.

Fix a good tolerance \(t\). Its defining measure conditions allow division by \(\mu(H_{t-\Delta})\). Aggregation stability, nonnegativity, the sandwich, and finite-sum linearity of integration give
\[
\begin{aligned}
\sum_{i=1}^n\ell(\widehat y_{t,i},y_i)
&\leq c\sum_i\frac{1}{\mu(H_{t,i})}\int_{H_{t,i}}\ell(h(x_i),y_i)\,d\mu(h)\\
&\leq \frac{c}{\mu(H_{t-\Delta})}\int_{H_{t+\Delta}}L_S(h)\,d\mu(h)\\
&\leq c\,\frac{\mu(H_{t+\Delta})}{\mu(H_{t-\Delta})}(L_*+t+\Delta)\\
&\leq cC_g(L_*+t+\Delta).
\end{aligned}
\]
The second line uses both set inclusions and \(\mu(H_{t,i})\geq\mu(H_{t-\Delta})>0\). The third uses the definition of \(H_{t+\Delta}\), and the last uses local growth.

Let \(G\subseteq T\) be the good tolerances, let \(m=|T|\), and put \(\varepsilon_i=\ell(\widehat y_i,y_i)\). The smallest median, like any median, has at least \(m/2\) entries weakly on each side, counting repetitions.

For distance-monotone loss, if \(\widehat y_i\geq y_i\), every prediction \(\widehat y_{t,i}\geq\widehat y_i\) has distance from \(y_i\) at least \(|\widehat y_i-y_i|\), and hence loss at least \(\varepsilon_i\). If \(\widehat y_i<y_i\), use instead the predictions \(\widehat y_{t,i}\leq\widehat y_i\). Each chosen side contains at least \(m/2\) entries. This includes equality \(\widehat y_i=y_i\) and all ties.

For one-sided monotone loss, fix \(y_i\). If the first-argument function is nondecreasing, use the predictions at least \(\widehat y_i\); if it is nonincreasing, use those at most \(\widehat y_i\). Again at least \(m/2\) entries have loss at least \(\varepsilon_i\). This argument permits the monotonicity direction to depend on the fixed response.

At most \(m-|G|\) entries on the chosen side are bad. Thus at least
\[
m/2-(m-|G|)=|G|-m/2\geq(\rho-1/2)m
\]
good entries have loss at least \(\varepsilon_i\). Nonnegativity of the remaining losses gives
\[
(\rho-1/2)m\sum_i\varepsilon_i
\leq\sum_{t\in G}\sum_i\ell(\widehat y_{t,i},y_i).
\]
Using the single-tolerance bound and \(t\leq t_{\max}\),
\[
\sum_{t\in G}\sum_i\ell(\widehat y_{t,i},y_i)
\leq |G|cC_g(L_*+t_{\max}+\Delta)
\leq mcC_g(L_*+t_{\max}+\Delta).
\]
Cancel \(m>0\), divide by \(\rho-1/2>0\), and then divide by \(n>0\). This proves
\[
\operatorname{LOO}_S(\mathrm{MLSA})
\leq\frac{2cC_g}{(2\rho-1)n}\bigl(L_*+t_{\max}+\Delta\bigr).
\]

All theorem-critical obligations are closed. The argument covers \(n=1\), a singleton grid, even grids, tied predictions, and zero comparator loss. A tolerance with \(t<\Delta\) cannot be good because its lower full-sample level set is empty; it may nevertheless occur as a bad tolerance with a well-defined prediction.
