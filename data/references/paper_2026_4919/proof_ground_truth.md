# Reference Proof

## Proof Structure

1. Establish that surprisal is strictly positive and combine it with the deterministic-reward advantages to obtain the sign of multiplicative delight.
2. Compute the correct and incorrect additive scores under the symmetric policy.
3. Reduce their difference to a scalar inequality and solve it with the required sign cases for the logarithmic likelihood ratio.

## Complete Proof

Let q=(1-p)/(K-1). Since p and q lie in (0,1), the surprisal values are positive:
\[
\ell(y^*)=-\log p>0,\qquad \ell(a)=-\log q=\log\frac{K-1}{1-p}>0
\]
for every incorrect arm a. The deterministic reward and baseline give
\[
U(y^*)=1-b>0,\qquad U(a)=-b<0.
\]
Therefore
\[
\chi(y^*)=U(y^*)\ell(y^*)>0,\qquad \chi(a)=U(a)\ell(a)<0,
\]
for every incorrect arm, independently of p and K.

For the additive priority, define
\[
f_\alpha(x)=\alpha U(x)+(1-\alpha)\ell(x),\qquad \alpha\in[0,1].
\]
Set
\[
L=\log\frac{p(K-1)}{1-p}.
\]
Using the two policy probabilities,
\[
\ell(y^*)-\ell(a)=-\log p+\log q
=-\log\frac{p(K-1)}{1-p}=-L.
\]
Also U(y^*)-U(a)=(1-b)-(-b)=1. Hence the correct-versus-incorrect score difference is
\[
f_\alpha(y^*)-f_\alpha(a)
=\alpha+(1-\alpha)(-L)
=\alpha-(1-\alpha)L.
\]
If L>0, then 1+L>0 and this difference is positive exactly when
\[
\alpha>\frac{L}{1+L}.
\]
If L=0, it equals \alpha and is positive exactly when \alpha>0. If L<0, then
\[
\alpha-(1-\alpha)L=\alpha+(1-\alpha)|L|>0
\]
for every \alpha\in[0,1]. Finally, L>0 is equivalent to p>1/K, L=0 to p=1/K, and L<0 to p<1/K. Thus multiplicative delight always separates the correct arm by sign, while additive advantage-surprisal priorities require the stated policy- and action-space-dependent threshold only in the p>1/K regime, with the two boundary cases as specified.
