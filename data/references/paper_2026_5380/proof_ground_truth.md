# Reference Proof

## Proof Structure

Fix the optimal coefficient vector and minimize only the perspective allocation over the free coordinates. The affordable-support case follows from monotonicity. In the over-budget case, construct a capped proportional allocation, certify it by convex KKT sufficiency, and then obtain its explicit form from the sorted magnitudes. Finally use partial minimization to recover joint optimality.

The theorem-critical obligations are:

1. Reduce recovery to a well-defined free-coordinate allocation problem, retaining the fixed coordinates and box-induced lower bounds.
2. Resolve zero remaining budget and the case in which every positive free coordinate can receive indicator one.
3. Establish budget activity and existence of a feasible positive threshold in the remaining case.
4. Verify a complete global-optimality certificate, including lower-bound and coincident-bound cases.
5. Construct a sorted index in the claimed range and prove the threshold formula and consistency inequalities, including ties.
6. Conclude joint optimality from attainment of the partial minimum.

## Complete Proof

Write \(a_j=|\theta_j^\star|\) for \(j\in J_f\), and let \(I=\{j\in J_f:a_j>0\}\), with \(m=|I|\). Finiteness of \(g(\theta^\star)\) implies that the indicator constraints at \(\theta^\star\) are feasible. Consequently, \(\theta_j^\star=0\) on \(J_0\), \(|\theta_j^\star|\le M\) on \(J_1\), and every free magnitude satisfies \(0\le a_j\le M\).

At fixed \(\theta^\star\), the loss and the perspective contributions of fixed coordinates are constant. A free zero coefficient contributes zero for every feasible indicator; setting its indicator to zero preserves the objective and cannot increase budget usage. Conversely, any feasible allocation on the positive free coordinates extends by these zero indicators and the prescribed fixed indicators. Therefore the only nonconstant allocation problem is
\[
 \min_{u_j}\ \frac12\sum_{j\in I}\frac{a_j^2}{u_j}
 \quad\text{subject to}\quad
 \frac{a_j}{M}\le u_j\le1,\qquad \sum_{j\in I}u_j\le\bar k.
\tag{1}
\]
Its feasible set is nonempty and compact. When \(I\ne\varnothing\), every lower bound is strictly positive, so the objective is continuous on that set and a minimum is attained. The empty-coordinate case has objective zero.

If \(\bar k=0\), feasibility forces \(I=\varnothing\), so all free indicators can and must be zero. This is the stated allocation.

Suppose henceforth that \(\bar k>0\). If \(m\le\bar k\), assigning \(u_j=1\) for \(j\in I\) is feasible. Each positive-coordinate summand is decreasing in its indicator, so this assignment minimizes every summand. Together with zero indicators on free zero coefficients, it is the claimed allocation. This includes an empty free set, all-zero free coefficients, \(m=\bar k\), and \(\bar k\ge p_f\).

Now suppose \(m>\bar k\). At an optimum of (1), the budget must bind. Otherwise, since there are more than \(\bar k\) positive coordinates, some positive-coordinate indicator is below one. Increasing it by a sufficiently small positive amount respects both its bounds and the slack budget and strictly decreases the objective, a contradiction.

Feasibility also gives
\[
 \sum_{j\in I}\frac{a_j}{M}\le\bar k.
\tag{2}
\]
Define
\[
 q(t)=\sum_{j\in I}\min\{1,a_j/t\},\qquad t>0.
\]
This function is continuous on \((0,M]\). Since \(a_j\le M\), equation (2) gives
\[
 q(M)=\sum_{j\in I}\frac{a_j}{M}\le\bar k.
\]
Also, \(q(t)\to m>\bar k\) as \(t\downarrow0\). Choose a sufficiently small positive \(\varepsilon<M\) with \(q(\varepsilon)>\bar k\), and apply continuity on \([\varepsilon,M]\). There exists \(\tau\in(0,M]\) such that \(q(\tau)=\bar k\).

Set
\[
 \widehat u_j=\min\{1,a_j/\tau\}\quad(j\in I).
\tag{3}
\]
Both numbers inside the minimum are at least \(a_j/M\): this follows from \(a_j\le M\) and \(\tau\le M\), respectively. Thus (3) satisfies the lower and upper bounds, and its indicator sum is exactly \(\bar k\).

We now certify its optimality. We use the standard convex KKT sufficiency principle: for a differentiable convex objective and affine inequalities, a feasible point with nonnegative constraint multipliers satisfying stationarity and complementary slackness is globally optimal. This sufficiency statement does not require strict feasibility. Here each summand has second derivative \(a_j^2/u_j^3>0\) on the positive orthant, and all constraints in (1) are affine.

Use multipliers \(\nu\) for the budget, \(\eta_j\) for \(a_j/M-u_j\le0\), and \(\omega_j\) for \(u_j-1\le0\). Choose
\[
 \nu=\frac{\tau^2}{2},\qquad \eta_j=0,\qquad
 \omega_j=
 \begin{cases}
 (a_j^2-\tau^2)/2,&a_j\ge\tau,\\
 0,&a_j<\tau.
 \end{cases}
\]
All multipliers are nonnegative. If \(a_j<\tau\), then \(\widehat u_j=a_j/\tau<1\), and
\[
 -\frac{a_j^2}{2\widehat u_j^2}+\nu-\eta_j+\omega_j=0.
\]
If \(a_j\ge\tau\), then \(\widehat u_j=1\), and the same stationarity equation follows from the displayed value of \(\omega_j\). Complementary slackness holds because the budget binds, all lower-bound multipliers vanish, and a positive upper-bound multiplier is assigned only at an upper-active coordinate. These observations remain valid when \(a_j=\tau\), when \(\tau=M\), and when \(a_j=M\) makes the lower and upper bounds coincide. Thus KKT sufficiency proves that \(\widehat u\) minimizes (1).

For clarity concerning the source's lower-bound discussion, activity of a lower bound alone does not force an arbitrary KKT-derived threshold to equal \(M\). At a KKT point, a positive coordinate with \(u_j=a_j/M<1\) has \(\omega_j=0\), so stationarity gives \(\nu=M^2/2+\eta_j\ge M^2/2\). An interior coordinate would instead imply \(\nu=a_j^2/(2u_j^2)<M^2/2\), and hence cannot coexist with this lower-bound-only coordinate. A capped coordinate with \(a_j<M\) would have inactive lower bound and therefore \(\eta_j=0\), giving \(\omega_j=a_j^2/2-\nu<0\), also impossible. Consequently, in this case every capped coordinate has \(a_j=M\), and every positive coordinate is at its lower bound. Budget activity then gives \(\sum_{j\in I}a_j/M=\bar k\). The identical primal allocation is represented by choosing \(\tau=M\), and the explicit multipliers above certify it, even if some other multiplier choice gives \(\sqrt{2\nu}>M\). In contrast, a coordinate with \(a_j=M\) and \(u_j=1\) has both bounds active and can coexist with interior coordinates; it must not be used to infer \(\nu\ge M^2/2\). The constructive certificate already covers this possibility.

Extend (3) by setting free zero-coefficient indicators to zero and imposing \(u_j^\star=0\) on \(J_0\) and \(u_j^\star=1\) on \(J_1\).

For the sorted formula, order all free magnitudes as in the task and define
\[
 s=\bigl|\{j\in J_f:a_j\ge\tau\}\bigr|.
\]
Each of these \(s\) coordinates contributes one to the budget, so \(s\le\bar k\). Since \(m>\bar k\ge s\), there is at least one positive coordinate outside this capped set. It contributes a strictly positive amount to the budget, giving \(\bar k=q(\tau)>s\). Hence
\[
 s\in\{0,\ldots,\bar k-1\}.
\]
The sorted order and the definition of \(s\) give
\[
 a_{\pi(s)}\ge\tau\ge a_{\pi(s+1)},\qquad a_{\pi(0)}=+\infty.
\]
The next position exists because \(p_f\ge m>\bar k>s\). All magnitudes equal to \(\tau\) can be included in the capped prefix, so ties cause no difficulty. Equation (3) now yields
\[
 \bar k=s+\frac{\sum_{r=s+1}^{p_f}a_{\pi(r)}}{\tau},
\]
and therefore
\[
 \tau=\frac{\sum_{r=s+1}^{p_f}a_{\pi(r)}}{\bar k-s}.
\]
This is exactly the claimed piecewise formula and its capped proportional equivalent.

More generally, any index in the stated range satisfying the displayed threshold formula and consistency inequalities produces an optimal allocation. Its tail contains a positive magnitude because \(m>\bar k>s\), so its threshold is positive. The prefix inequalities and threshold formula imply
\[
 \sum_{j\in J_f}a_j\ge s\tau+(\bar k-s)\tau=\bar k\tau.
\]
Combining this with (2) gives \(\tau\le M\). The resulting allocation equals \(\min\{1,a_j/\tau\}\), uses budget \(\bar k\), and is certified by the same multipliers. This also permits a consistent prefix that places some threshold ties in the proportional tail.

Finally, the constructed \(u^\star\) attains the indicator infimum defining \(g(\theta^\star)\), including its fixed-coordinate contributions. For every feasible pair \((\theta,u)\),
\[
 L(A\theta)+\lambda\sum_j\frac{\theta_j^2}{u_j}
 \ge L(A\theta)+2\lambda g(\theta)
 =\Phi(\theta)
 \ge\Phi(\theta^\star)
 =L(A\theta^\star)+\lambda\sum_j\frac{(\theta_j^\star)^2}{u_j^\star}.
\]
The inequalities use \(\lambda>0\), the definition of the infimum, and optimality of \(\theta^\star\); the final equality uses the attained partial minimum. Thus \((\theta^\star,u^\star)\) is jointly optimal.
