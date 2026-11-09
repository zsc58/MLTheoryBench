# Reference Proof

## Proof Structure

First establish the quantile-negation identity almost everywhere and use it to rewrite the lower-tail quantile integral as the negative of the upper-tail quantile integral of the negated variable. Then prove the required Rockafellar-Uryasev variational representation in the extended-real setting, so that no integrability assumption is silently imposed. Apply that representation to the negated variable at level `1-p`, negate the minimum, and substitute the auxiliary variable.

## Complete Proof

Let `F_Z` be the distribution function and `Q_Z(u)=inf{x:F_Z(x)\ge u}`. A monotone quantile has at most countably many discontinuities. At every continuity point `u\in(0,1)`, quantile symmetry under negation gives
`Q_{-Z}(1-u)=-Q_Z(u)`.
Indeed, `F_{-Z}(t)=P(-Z\le t)=1-F_Z((-t)^-)`. If `x=Q_Z(u)`, then `F_Z(x^-)\le u`, so `F_{-Z}(-x)\ge 1-u` and hence `Q_{-Z}(1-u)\le -x`. Conversely, continuity of `Q_Z` at `u` implies that for every `y>x`, `F_Z(y^-)>u`; hence `F_{-Z}(-y)<1-u`. Therefore no point below `-x` can belong to the defining level set for `Q_{-Z}(1-u)`, giving `Q_{-Z}(1-u)\ge -x`. Thus equality holds at every continuity point and hence almost everywhere.

We will use the following extended-real variational fact. For every real-valued random variable `Y` and every `q\in(0,1)`, define
`U_q(Y)=(1/(1-q))\int_q^1 Q_Y(v)\,dv`.
Then
`U_q(Y)=min_{a\in\mathbb R}{a+(1/(1-q))E[(Y-a)_+]}`,
where the expectation and integral are interpreted as extended-real quantities.

To prove this without an integrability assumption, use the quantile expectation identity for the nonnegative function `y\mapsto(y-a)_+`:
`E[(Y-a)_+]=\int_0^1(Q_Y(v)-a)_+\,dv`.
Let `b=Q_Y(q)`, which is finite because `Y` is real-valued. If `a\ge b`, monotonicity of `Q_Y` gives, for almost every `v\in[q,1]`,
`Q_Y(v)\le a+(Q_Y(v)-a)_+`.
After integration,
`a+(1/(1-q))E[(Y-a)_+]\ge U_q(Y)`.
If `a<b`, then `Q_Y(v)>a` for every `v\in[q,1]`, so
`a+(1/(1-q))E[(Y-a)_+]`
`=U_q(Y)+(1/(1-q))\int_0^q(Q_Y(v)-a)_+\,dv\ge U_q(Y)`.
At `a=b`, the positive-part term on `[q,1]` satisfies `Q_Y(v)=b+(Q_Y(v)-b)_+` almost everywhere, so equality holds, including when `U_q(Y)=+\infty`. This proves the extended-real variational formula and shows that the minimum is attained at `Q_Y(q)`.

Now set `Y=-Z` and `q=1-p`. The almost-everywhere quantile identity and the change of variables `v=1-u` give
`L_p(Z)=(1/p)\int_0^pQ_Z(u)\,du`
`=-(1/p)\int_0^pQ_{-Z}(1-u)\,du`
`=-(1/p)\int_{1-p}^1Q_{-Z}(v)\,dv`
`=-U_{1-p}(-Z)`.

Applying the extended-real variational formula to `-Z` at level `1-p` yields
`U_{1-p}(-Z)=min_{a\in\mathbb R}{a+(1/p)E[(-Z-a)_+]}`.
Negating both sides converts the minimum to a maximum, so
`L_p(Z)=max_{a\in\mathbb R}{-a-(1/p)E[(-Z-a)_+]}`.
Finally set `eta=-a`. Since `a` ranges over all reals,
`(-Z-a)_+=(eta-Z)_+`, and therefore
`L_p(Z)=max_{eta\in\mathbb R}{eta-(1/p)E[(eta-Z)_+]}`.
The argument includes the case in which the tail integral or the hinge expectation is infinite, so it applies to every real-valued random variable `Z` covered by the task.
