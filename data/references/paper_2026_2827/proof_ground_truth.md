# Reference Proof

## Proof Structure

For INT8, show that the first quantization error is at most half a scale, that the residual therefore lies inside the second-pass representable range, and that the second rounding error gives the stated bound. For MXFP4, derive the nearest-rounding error from the stated grid, use the power-of-two scale choice to bound normalized entries, handle normal and clipped values in the first pass, then handle normal and clipped values in the second pass.

## Complete Proof

Nearest-integer rounding has error at most one half: between two consecutive integers, at least one endpoint is within one half of any point in that interval. Either choice at a midpoint has the same error.

For INT8, let $M=\|x\|_\infty>0$, $\alpha=M/127$, and $\beta=\alpha/254$. These scales are positive. Since $|x_i/\alpha|\le127$, every nearest integer lies in $[-127,127]$, so the first clipping is inactive. Nearest integer rounding therefore gives
\[
|x_i-\alpha x_i^{(1)}|\le\alpha/2,
\]
so $\|r\|_\infty\le\alpha/2$, where $r=x-\alpha x^{(1)}$. Consequently
\[
|r_i/\beta|\le(\alpha/2)/(\alpha/254)=127,
\]
so the second clipping is also inactive, including at the endpoints. Its rounding error is at most $\beta/2=\alpha/508$. Hence
\[
\|x-(\alpha x^{(1)}+\beta x^{(2)})\|_\infty
=\|r-\beta x^{(2)}\|_\infty
\le\frac{\beta}{2}
=\frac{M}{127\cdot508}
=\frac{M}{64516}.
\]

For the stated FP4 quantizer, consecutive elements of $S$ throughout $[-1.75,1.75]$ are separated by $0.25$. Every point in each interval between consecutive grid elements is within $0.125$ of at least one endpoint. Thus nearest-element rounding gives
\[
|t-Q_4(t)|\le0.125\qquad\text{when }|t|\le1.75.
\]
This holds for either nearest choice at a midpoint. When $|t|>1.75$, clipping gives the endpoint with the sign of $t$, so
\[
|t-Q_4(t)|=|t|-1.75.
\]
These statements cover positive and negative inputs.

For an MXFP4 block, write $M_b=\|x_b\|_\infty>0$ and
\[
\alpha=2^{\lceil\log_2(M_b/1.859375)\rceil},\qquad \beta=\alpha/16.
\]
The logarithm is defined and both scales are positive powers of two. Since $\lceil u\rceil\ge u$ and $2^u$ is increasing,
\[
\alpha\ge M_b/1.859375,
\]
hence $|x_{b,i}/\alpha|\le1.859375$.

In the first pass, if $|x_{b,i}/\alpha|\le1.75$, the nearest-grid bound just derived gives error at most $0.125\alpha$. If $1.75<|x_{b,i}/\alpha|\le1.859375$, the signed clipping formula gives error at most
\[
(1.859375-1.75)\alpha=0.109375\alpha<0.125\alpha.
\]
Thus, with $r=x_b-\alpha q_1$, $\|r\|_\infty\le\alpha/8$.

Therefore
\[
|r_i/\beta|\le(\alpha/8)/(\alpha/16)=2.
\]
In the second pass, normalized magnitudes at most $1.75$ incur rounding error at most $0.125\beta$, while magnitudes in $(1.75,2]$ incur clipping error at most
\[
(2-1.75)\beta=0.25\beta.
\]
The latter is the worst case, so
\[
\|r-\beta q_2\|_\infty\le\beta/4=\alpha/64,
\]
and consequently
\[
\|x_b-(\alpha q_1+\beta q_2)\|_\infty\le\alpha/64.
\]
Both conclusions hold coordinatewise (and the MXFP4 conclusion blockwise), as required. No assumption on clipping proportions or input distributions is used.
