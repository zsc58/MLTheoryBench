# Reference Proof

## Proof Structure

First compare the true and predicted primal feasible regions componentwise. Then use tight primal constraints to identify exactly when an overprediction violates feasibility. Finally, under predicted feasibility, use complementary slackness and equality of the true and predicted primal-dual objectives to characterize zero gap by equality of the predicted and true right-hand sides on the positive dual support.

## Complete Proof

Let \(\widehat b=p(\xi)\). Since \((x^\ast,y^\ast)\) is optimal for the true LP, \(x^\ast\) satisfies \(Ax^\ast\ge b\), \(x^\ast\ge0\), and \(y^\ast\) satisfies \(A^\top y^\ast\le c\), \(y^\ast\ge0\). The latter dual constraints do not depend on the right-hand side.

If \(b\ge\widehat b\) componentwise, then \(Ax^\ast\ge b\ge\widehat b\), so \(x^\ast\) is feasible for the predicted primal. Together with the unchanged dual feasibility of \(y^\ast\), this gives \((x^\ast,y^\ast)\in\widehat S(\xi;p)\).

Conversely, if \(j'\in J^=(x^\ast)\) and \(b_{j'}<\widehat b_{j'}\), then \(a_{j'}^\top x^\ast=b_{j'}<\widehat b_{j'}\). Thus \(x^\ast\) violates the \(j'\)-th predicted primal constraint, and \((x^\ast,y^\ast)\notin\widehat S(\xi;p)\).

Now assume \((x^\ast,y^\ast)\in\widehat S(\xi;p)\). Suppose first that it also belongs to \(\widehat S^\ast(\xi;p)\), so \(c^\top x^\ast=\widehat b^\top y^\ast\). True strong duality gives \(c^\top x^\ast=b^\top y^\ast\). For every \(j\in J^+(y^\ast)\), complementary slackness gives \(j\in J^=(x^\ast)\), hence predicted feasibility implies \(\widehat b_j\le a_j^\top x^\ast=b_j\). Since \(y_j^\ast=0\) outside \(J^+(y^\ast)\),
\[
0=\widehat b^\top y^\ast-b^\top y^\ast
 =\sum_{j\in J^+(y^\ast)}(\widehat b_j-b_j)y_j^\ast.
\]
Every summand is nonpositive and every displayed multiplier is positive, so each summand is zero. Therefore \(\widehat b_j=b_j\) for all \(j\in J^+(y^\ast)\).

Conversely, assume \(\widehat b_j=b_j\) for every \(j\in J^+(y^\ast)\), while \((x^\ast,y^\ast)\in\widehat S(\xi;p)\). Because \(y_j^\ast=0\) off this support, \(\widehat b^\top y^\ast=b^\top y^\ast=c^\top x^\ast\). Thus the predicted primal and dual feasible pair has zero primal-dual gap, which is precisely membership in \(\widehat S^\ast(\xi;p)\).
