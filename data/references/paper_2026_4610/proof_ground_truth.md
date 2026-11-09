# Reference Proof

## Proof Obligations

1. Distinguish the independent scalar gate arguments from their ensemble-generated values and verify well-definedness.
2. Derive the mean sensitivity, its sign, and its exact zero-mean boundary value.
3. Derive the spread sensitivity and distinguish positive-mean strictness from the zero-mean case.
4. Derive the scale sensitivity and distinguish positive-mean strictness from the zero-mean case.
5. Prove gate saturation and vanishing of all three sensitivities for each fixed positive spread-scale pair.

## Complete Proof

### 1. Domain and scalar interpretation

The probability-simplex assumption gives `0<=mu_c<=1`. Since `M>1`, the sample-variance denominator is positive, and the additive stabilization gives `sigma_c>=epsilon>0`. Together with `kappa_c>0`, these facts make every empirical gate evaluation well-defined.

The partial derivatives and final limit concern the explicitly defined function `F(u,v,w)` with independent arguments `u>=0`, `v>0`, and `w>0`. They are not total derivatives through the member vectors. In particular, empirical means cannot tend to infinity with spread and scale fixed; the final limit is the stated scalar-function asymptotic.

Write

`r=u/(w v)` and `F=1-exp(-r)`.

Then `r>=0`, `0<=F<1`, and `1-F=exp(-r)>0`.

### 2. Mean sensitivity

Holding `v` and `w` fixed, the chain rule gives

`partial F/partial u = exp(-r)/(w v) = (1-F)/(w v) > 0`.

Thus `F` is strictly increasing in its first argument. This also follows directly because increasing `u` strictly increases `r`, strictly decreases `exp(-r)`, and strictly increases `F`.

At `u=0`, the right-hand derivative is

`lim_{h down to 0} [F(h,v,w)-F(0,v,w)]/h = 1/(w v)`.

This agrees with the continuous boundary value of the displayed derivative. Also, `F(0,v,w)=0`.

### 3. Spread sensitivity

Holding `u` and `w` fixed gives `partial r/partial v=-u/(w v^2)`. Therefore

`partial F/partial v = -u exp(-r)/(w v^2) = -(1-F)u/(w v^2) <= 0`.

For `u>0`, the derivative is strictly negative, so the gate is strictly decreasing in spread. At `u=0`, the derivative is exactly zero, and `F(0,v,w)=0` for every positive `v`. Thus the gate is nonincreasing in its second argument on the entire stated domain.

### 4. Scale sensitivity

Holding `u` and `v` fixed gives `partial r/partial w=-u/(w^2 v)`. Hence

`partial F/partial w = -u exp(-r)/(w^2 v) = -(1-F)u/(w^2 v) <= 0`.

This derivative is strictly negative exactly when `u>0`. At `u=0`, it is zero, and the gate is constant in `w`. Consequently, the gate is nonincreasing in its third argument, with strict decrease for positive first argument.

Evaluating the three formulas at `(u,v,w)=(mu_c,sigma_c,kappa_c)` gives

`partial G_c/partial mu_c = exp(-mu_c/(kappa_c sigma_c))/(kappa_c sigma_c)`,

`partial G_c/partial sigma_c = -mu_c exp(-mu_c/(kappa_c sigma_c))/(kappa_c sigma_c^2)`,

`partial G_c/partial kappa_c = -mu_c exp(-mu_c/(kappa_c sigma_c))/(kappa_c^2 sigma_c)`.

Here each expression denotes the corresponding independent-argument sensitivity specified in the task. At `mu_c=0`, the gate is zero and the sensitivities are respectively `1/(kappa_c sigma_c)`, `0`, and `0`. In the ensemble setup, a zero mean of nonnegative coordinates forces every `x_c^(m)=0`, so `sigma_c=epsilon` and the first boundary value is also `1/(kappa_c epsilon)`.

The case `C=1` causes no exception: its empirical evaluation has `mu_1=1` and `sigma_1=epsilon`, and the same scalar sensitivities apply. No differentiation of the empirical standard deviation at a consensus configuration is required.

### 5. Fixed-parameter saturation

Fix any `v>0` and `w>0`. As `r=u/(w v)` tends to infinity, `exp(-r)` tends to zero, and therefore `F` tends to one. The derivative formulas can be written as

`partial F/partial u = exp(-r)/(w v)`,

`partial F/partial v = -(r/v) exp(-r)`,

`partial F/partial w = -(r/w) exp(-r)`.

To justify the remaining limits explicitly, for `r>0` the exponential series gives `exp(r)>=r^2/2`. Thus

`0<=r exp(-r)<=2/r`,

which tends to zero. Since `v` and `w` are fixed positive constants, all three displayed sensitivities tend to zero. They share the attenuation factor `1-F=exp(-r)`, while the fixed prefactors and the factor `r` are controlled in this stated limit.

This establishes every requested derivative, monotonicity, boundary value, and saturation limit. It does not assert uniform vanishing over arbitrary jointly varying triples `(u,v,w)`.

## Private Source-Repair Note — Not an Additional Solver Obligation

The source's explanation at L000097 incorrectly claims that both factors in the mean sensitivity decrease as spread increases. For fixed `u` and `w`, let `H(v)=exp(-u/(w v))/(w v)`. Direct differentiation gives

`H'(v)=exp(-r)(r-1)/(w v^2)`.

The inverse prefactor decreases with `v`, but the exponential factor increases. Accordingly, mean sensitivity increases where `r>1`, decreases where `r<1`, and has zero derivative where `r=1`. This corrects the explanatory inference without changing any of the gate-monotonicity results proved above.

The source proofs for spread and scale also repeat strict-negative signs at zero mean. Their exact formulas establish nonpositivity, with strict negativity only for positive mean, as used in this proof. No global monotonicity of sensitivity magnitudes in spread or scale is needed for the public task.
