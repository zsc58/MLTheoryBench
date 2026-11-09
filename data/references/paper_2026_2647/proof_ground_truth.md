# Reference Proof

## Proof Structure

1. Prove continuity of the conditional-density map in both the density and query variables.
2. Encode each query by a constant function and lift the map to a function-space map on a compact set.
3. Extend this map continuously to the ambient Banach space and invoke the compact-set approximation property stated in the public setup.
4. Realize the constant-function encoding with a vector-to-function layer and compose it with the approximating neural operator.

## Complete Conditional Derivation

Fix `delta > 0`, a compact set `K subset X_delta`, and `epsilon > 0`. Write `m_rho(y) = integral_D rho(x,y) dx` and `rho_y = rho(.,y)`.

For `p,q in X_delta` and fixed `y in E`,

`p_y/m_p(y) - q_y/m_q(y) = (p_y-q_y)/m_p(y) + q_y(1/m_p(y)-1/m_q(y))`.

Since both marginals are at least `delta`, and

`|m_p(y)-m_q(y)| <= |D| ||p-q||_infinity`,

we obtain

`||p_y/m_p(y)-q_y/m_q(y)||_infinity <= delta^(-1) (1 + |D| ||q||_infinity/delta) ||p-q||_infinity`.

Interchanging `p` and `q` and taking the smaller numerator norm gives the symmetric bound

`||G*(p)-G*(q)||_infinity <= delta^(-1) (1 + |D| min(||p||_infinity,||q||_infinity)/delta) ||p-q||_infinity`,

where `G*(rho)(x,y)=rho(x,y)/m_rho(y)`. Thus changes in the density variable are uniform in `y`.

If `(rho_n,y_n)` tends to `(rho,y)` in the product norm, split `Psi*(rho_n,y_n)-Psi*(rho,y)` into the change from `rho_n` to `rho` at fixed query `y_n`, followed by the change from `y_n` to `y` at fixed density `rho`. The first term tends to zero by the preceding bound. Uniform continuity of `rho` on compact `D x E` gives uniform convergence of `rho(.,y_n)` to `rho(.,y)` and convergence of their integrals. The lower bound `delta` controls the denominators. Hence `Psi*` is continuous on `X_delta x E`.

For `y in E`, let `c_y` be the constant function on `D x E` with value `y`. The map `iota(y)=c_y` is continuous because `||c_y-c_{y'}||_infinity=|y-y'|`. Define

`S={rho direct-sum c_y : (rho,y) in K x E}`

and `F(rho direct-sum c_y)=Psi*(rho,y)`. The concatenation map is an embedding: its first channel recovers `rho`, and any value of its remaining constant channels recovers `y`. Both recovery maps are continuous. Thus `S` is compact and `F:S -> C(D)` is well-defined and continuous. Since `S` is closed in the Banach space `C(D x E;R^{r+1})`, the continuous-extension result invoked by the source gives a continuous extension `F_tilde:C(D x E;R^{r+1})->C(D)`. Its relevant form is that a continuous Banach-valued map on a closed subset of a Banach space admits a continuous extension; the compactness, closedness, and Banach-space hypotheses have been checked here. If `S` is empty, the zero map is an extension.

Apply the compact-set approximation property expressly stated in the public setup to `F_tilde` and `S`. It yields a neural operator `N:C(D x E;R^{r+1})->C(D)` with

`sup_{u in S} ||N(u)-F_tilde(u)||_infinity <= epsilon`

when `S` is nonempty; for empty `S`, any operator of the stipulated class suffices. The availability of this architecture-specific approximation property under the source's external theorem has **not** been independently established from the supplied source; see the unresolved obligation below.

Take `h` identically one and the permitted identity network to obtain the vector-to-function layer `V(y)=c_y`. Define `J(rho,y)=rho direct-sum V(y)` and `tilde_Psi(rho,y)=N(J(rho,y))`. This is an augmented neural operator. For `(rho,y) in K x E`, `J(rho,y) in S` and `F_tilde(J(rho,y))=Psi*(rho,y)`, so the stated uniform error bound follows.

## Unresolved External Obligation

The source invokes a nonstandard neural-operator universal-approximation result and a distinct-input/output-domain modification, but supplies neither the independent technical hypotheses nor their verification for this exact architecture and activation. The derivation above proves the public statement under its explicit approximation-property assumption; it does not independently prove that the externally cited result supplies that property. This gap is not evidence that the source theorem is false.
