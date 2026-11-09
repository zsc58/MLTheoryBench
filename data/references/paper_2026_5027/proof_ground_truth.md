# Reference Proof

## Proof Structure

1. Establish exact marginal factorization, including positive, zero, and empty prefixes.
2. Identify the lookahead weight as the conditional expectation of the full importance weight, using proposal support rather than any normalization of the transition factors.
3. Derive the conditional squared-error decomposition and minimum-MSE property.
4. Specialize the decomposition to the prefix weight without assuming that this weight is square-integrable.
5. Use conditional independence of the auxiliary estimate and the evaluated future to prove the approximate-weight identity.
6. Apply the conditional error bound, distinguishing the displayed inequality from a finite asymptotic rate, and check the endpoint conventions.

## Complete Proof

Fix `t`. All factors `a_s=m_s psi_s` are finite and nonnegative. The proposal kernels `r_s` are normalized; normalization of `m_s` is neither assumed nor used.

### 1. Exact marginal and zero-prefix cases

For any prefix `x_{1:t}`, the definition of `gamma_t^look` is the nonnegative sum of the full path weights extending that prefix. Consequently, `0<=gamma_t^look(x_{1:t})<=Z`.

If `gamma_t^prf(x_{1:t})>0`, its finite positive value can be factored out of the suffix sum:
`gamma_t^look(x_{1:t})=gamma_t^prf(x_{1:t}) sum_{x_{t+1:T}} product_{s=t+1}^T a_s = gamma_t^prf(x_{1:t}) L_t(x_{1:t})`.
In particular, `L_t(x_{1:t})<=Z/gamma_t^prf(x_{1:t})<infinity` on such a prefix. It may equal zero.

If `gamma_t^prf(x_{1:t})=0`, every complete path extending the prefix has zero full weight, since its remaining factors are finite. Hence `gamma_t^look(x_{1:t})=0`. This argument does not require the unweighted suffix sum `L_t` to be finite on a zero prefix. It justifies the stated zero-product convention.

The empty-prefix and empty-suffix conventions give `gamma_0^prf=1`, `gamma_0^look=L_0=Z`, and `L_T=1`.

### 2. Conditional expectation under the proposal

Write `B=W_t^prf`. On every sampled path, all sampled proposal probabilities are positive, so `B` is finite. The event `A_t` is exactly the event `B>0`, up to proposal-null sets.

Consider a prefix of positive proposal probability that belongs to `A_t`. Conditional on that prefix, sum only over suffixes having positive conditional proposal probability. Cancellation of those proposal probabilities gives
`E_R[W_T|F_t]=B sum_{supported suffixes} product_{s=t+1}^T a_s`.
Every suffix whose product of future factors is positive has positive conditional proposal probability: together with the positive prefix factor it gives a positive full target weight, and full-path support then forces positive full proposal probability. Thus omitted suffixes contribute zero to the target sum, and the sum above equals `L_t`. Therefore
`E_R[W_T|F_t]=B L_t=W_t^look` on `A_t`.

On `A_t^c`, `B=0`, and every full path extending that prefix has zero target weight. Thus `W_T=0` conditionally almost surely, and both the conditional expectation and the conventionally defined `W_t^look` are zero.

Set `M=W_t^look=E_R[W_T|F_t]`. Since `W_T` is square-integrable, conditional Cauchy-Schwarz gives `M^2<=E_R[W_T^2|F_t]`, so `M` is square-integrable. Define
`V=E_R[(W_T-M)^2|F_t]=Var_R(W_T|F_t)`.
Then `E_R[V]<infinity`.

### 3. Conditional squared-error decomposition

Because the prefix space is countable and `E_R[W_T^2]<infinity`, the conditional second moment of `W_T` is finite at every prefix having positive proposal probability. At one such prefix, write `m` and `v` for the values of `M` and `V`. For any finite real number `y`, expansion under that conditional probability law gives
`E_R[(W_T-y)^2|prefix]=E_R[(W_T-m)^2|prefix]+(m-y)^2+2(m-y)E_R[W_T-m|prefix]`
`=v+(m-y)^2`.
All terms in this conditional calculation are integrable, and the last conditional mean is zero.

For a finite real `F_t`-measurable random variable `Y`, apply this identity at each prefix with its corresponding value `y=Y`. Integrating the nonnegative quantities yields
`E_R[(W_T-Y)^2]=E_R[V]+E_R[(M-Y)^2]`,
with the equality valid also when a nonnegative expectation is infinite. In particular, for the square-integrable `Y` required in the public projection statement, every term is finite.

Taking `Y=M` gives error `E_R[V]`. The added nonnegative term proves minimum MSE; equality occurs precisely when `Y=M` almost surely. The same conditional calculation shows that allowing finite-valued measurable approximations with infinite second moment cannot improve this minimum.

### 4. Prefix-only excess error

The prefix weight `B` is finite and `F_t`-measurable, but it need not be square-integrable. Apply the prefixwise identity just proved rather than substituting it into a result restricted to square-integrable approximations. On `A_t`, `M-B=B(L_t-1)`, and on `A_t^c` both `M` and `B` are zero. Thus
`E_R[(W_T-B)^2]=E_R[V]+E_R[B^2(L_t-1)^2]`,
with the prescribed zero-prefix interpretation. This is an equality of nonnegative extended expectations and involves no subtraction of infinities.

### 5. Auxiliary-estimator excess error

Fix a positive-probability prefix in `A_t`. At this prefix, `B` and `L_t` are finite, and the assumed error bound implies
`E[hat L_t^2|prefix] <= 2 L_t^2 + 2 C_t/J < infinity`.
The estimate is a function of the fixed prefix and `U_t`. Conditional independence of `U_t` and the future trajectory therefore makes `hat L_t` conditionally independent of `W_T` given the prefix.

Expand
`W_T-B hat L_t=(W_T-M)+B(L_t-hat L_t)`.
At the fixed prefix, both terms have finite second moment, and their cross term has conditional mean zero because
`E[(W_T-M)(L_t-hat L_t)|F_t]`
`=E_R[W_T-M|F_t] E[L_t-hat L_t|F_t]=0`.
Conditional independence is what justifies the factorization; two zero conditional means alone would not suffice. The assumed unbiasedness also gives the prefixwise conditional mean `E[B hat L_t|F_t]=B L_t=M` and identifies the conditional squared estimation error with its conditional variance.

It follows on `A_t` that
`E[(W_T-B hat L_t)^2|F_t]=V+B^2 E[(hat L_t-L_t)^2|F_t]`.
On `A_t^c`, `W_T=B=M=0` conditionally almost surely, so the same identity holds with every weighted error term set to zero. No conditional second-moment assumption on the unweighted estimate is needed on this event.

Integrating this identity over the prefix distribution, using nonnegative expectations, gives
`E[(W_T-B hat L_t)^2]=E_R[V]+E[B^2(hat L_t-L_t)^2]`.
This calculation remains valid even when the approximate weight has infinite unconditional second moment.

### 6. Monte Carlo bound and endpoint checks

Since `B^2` is nonnegative and `F_t`-measurable, integration of the assumed conditional bound gives
`E[B^2(hat L_t-L_t)^2]`
`=E_R[B^2 E[(hat L_t-L_t)^2|F_t]]`
`<=J^{-1} E_R[B^2 C_t]`.
Together with the preceding identity, this proves the required inequality.

The coefficient `K_t:=E_R[B^2 C_t]` is a nonnegative expectation and may be infinite. If a family of estimators uses the same fixed model and constants `C_t` as `J` varies, and `K_t<infinity`, the bound gives an excess error at most `K_t/J`, hence a finite O(1/J) rate and convergence to zero. Neither this additional finiteness nor an unconditional vanishing-error claim is needed for the displayed theorem. In particular, when `C_t=0`, the integrand `B^2 C_t` is identically zero; it is not interpreted as an indeterminate product of a scalar zero and an infinite moment.

At `t=0`, `B=1`, `F_0` is trivial, and direct proposal cancellation gives `E_R[W_T]=Z=M`. At `t=T`, `B=M=W_T`, `L_T=1`, and `V=0`; the auxiliary identity still applies to any estimate satisfying the stipulated terminal conditional moments. Zero future value on a positive prefix, zero prefix weights, and `J=1` are all covered by the same calculations.

## Source Correspondence and Proof Closure

The full-path factors need not be normalized, as shown by the powered-base choice at L000060-L000065. The future-sum and exact-marginal definitions are those at L000076-L000089. The ordinary fresh conditional rollout interpretation is supplied by L000095-L000104 and is used explicitly in the auxiliary cross-term calculation. The target comparisons are the identities at L000385-L000412.

The weights here are the unnormalized path-importance weights in that comparison theorem. In particular, `W_0^look=Z`; no particle-weight initialization or resampling normalization is substituted for this definition.

Every theorem-critical obligation is derived above. No specialized external theorem or unproved paper-specific dependency is needed, and no unresolved GT obligation remains.
