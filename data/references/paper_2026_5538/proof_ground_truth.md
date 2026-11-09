# Reference Proof

## Proof Structure

Let W = Gamma Vbar. First establish the standard sup-norm contraction and the residual-to-fixed-point estimate for the concrete Bellman operator. Next use Bellman compatibility of d_V to control the variation of TW between any two states by the directed Hausdorff action-matching distances. The encoder-decoder round trip turns Gamma Tbar_dagger Vbar into an average of TW over the state kernel kappa_S, giving the abstraction bridge bounded by Delta_H. Finally combine this bridge with grounding nonexpansiveness and the residual estimate.

## Complete Proof

Because S and A are finite and nonempty and 0 <= gamma < 1, the Bellman optimality operator T maps real-valued functions on S to real-valued functions on S. All such functions are bounded. For any V1,V2 and state s, the elementary inequality |max_a x_a - max_a y_a| <= max_a |x_a-y_a|, followed by probability normalization, gives

|(T V1)(s)-(T V2)(s)|
 <= gamma max_a sum_{s'} P(s'|s,a)|V1(s')-V2(s')|
 <= gamma ||V1-V2||_infty.

Taking the maximum over s yields

||T V1 - T V2||_infty <= gamma ||V1-V2||_infty.

The standard fixed-point result used here is: a self-map of a nonempty complete metric space with Lipschitz constant strictly less than one has a unique fixed point. Its hypotheses hold because the space R^S with the sup norm is nonempty and complete, T maps that space to itself, and its Lipschitz constant is at most gamma < 1. Thus T has the unique fixed point V*, with V*=TV*.

Grounding is nonexpansive: for any abstract functions U1,U2 and state s,

|(Gamma U1)(s)-(Gamma U2)(s)|
 <= sum_sbar nu_S(sbar|s)|U1(sbar)-U2(sbar)|
 <= ||U1-U2||_infty.

Taking the maximum over s gives ||Gamma U1-Gamma U2||_infty <= ||U1-U2||_infty. Likewise,

|(L V1)(sbar)-(L V2)(sbar)|
 <= sum_s eta_S(s|sbar)|V1(s)-V2(s)|
 <= ||V1-V2||_infty,

so L is also nonexpansive, although this last fact is not needed separately below.

Set W = Gamma Vbar. It belongs to V by hypothesis. Using V*=TV* and the contraction,

||W-V*||_infty <= ||W-TW||_infty + ||TW-TV*||_infty
               <= ||W-TW||_infty + gamma ||W-V*||_infty.

All norms are finite, and 1-gamma > 0. Rearranging gives

||W-V*||_infty <= (1-gamma)^(-1) ||W-TW||_infty.  (1)

For each state-action pair define q_W(s,a) = r(s,a) + gamma sum_{s'} P(s'|s,a)W(s'), so that (TW)(s) = max_a q_W(s,a). The assumed Bellman compatibility of d_V and W in V imply

|q_W(s,a)-q_W(u,b)| <= d_V((s,a),(u,b))

for every s,u,a,b.

Fix s,u and choose an action a_* maximizing q_W(s,a), which exists because A is finite and nonempty. For every b in A,

(TW)(s)-(TW)(u)
 = q_W(s,a_*)-max_c q_W(u,c)
 <= q_W(s,a_*)-q_W(u,b)
 <= |q_W(s,a_*)-q_W(u,b)|
 <= d_V((s,a_*),(u,b)).

Taking the infimum over b, then bounding by the supremum over a, gives

(TW)(s)-(TW)(u) <= sup_a inf_b d_V((s,a),(u,b)).

Interchanging s and u and using symmetry of the pseudometric gives

(TW)(u)-(TW)(s) <= sup_b inf_a d_V((s,a),(u,b)).

Both signed differences are therefore at most D_H(s,u), and hence

|(TW)(s)-(TW)(u)| <= D_H(s,u).  (2)

The state round-trip weights are nonnegative and normalized, since

sum_u kappa_S(u|s)
 = sum_sbar nu_S(sbar|s) sum_u eta_S(u|sbar)
 = sum_sbar nu_S(sbar|s)
 = 1.

By the definitions of grounding, the deformed operator, and kappa_S,

(Gamma Tbar_dagger Vbar)(s)
 = sum_sbar nu_S(sbar|s) sum_u eta_S(u|sbar)(TW)(u)
 = sum_u kappa_S(u|s)(TW)(u).

Thus normalization, the triangle inequality, and (2) imply

|(TW)(s)-(Gamma Tbar_dagger Vbar)(s)|
 = |sum_u kappa_S(u|s)((TW)(s)-(TW)(u))|
 <= sum_u kappa_S(u|s)|(TW)(s)-(TW)(u)|
 <= sum_u kappa_S(u|s)D_H(s,u).

Taking the supremum over s, outside the state-dependent average exactly as in the definition of Delta_H, yields

||TW-Gamma Tbar_dagger Vbar||_infty <= Delta_H(kappa_S;d_V).  (3)

Finally, by the triangle inequality, grounding nonexpansiveness, and (3),

||W-TW||_infty
 <= ||Gamma Vbar-Gamma Tbar_dagger Vbar||_infty
    + ||Gamma Tbar_dagger Vbar-TW||_infty
 <= ||Vbar-Tbar_dagger Vbar||_infty + Delta_H(kappa_S;d_V).

Substitute this bound into (1) and recall W=Gamma Vbar to obtain

||Gamma Vbar-V*||_infty
 <= (1-gamma)^(-1) [ ||Tbar_dagger Vbar-Vbar||_infty + Delta_H(kappa_S;d_V) ].

The argument applies separately to every bounded Vbar with Gamma Vbar in V. It does not require V* in V, closure of V under any operator, positive encoder entries, or nonempty Abar(sbar) at unused abstract states. The case gamma=0 is included without modification; if no admissible Vbar exists, the universal claim is vacuous.

## Obligation Closure

- Concrete fixed-point existence and uniqueness: the contraction is derived explicitly, and the stated standard fixed-point theorem is applied on the verified complete space R^S.
- Residual-to-value estimate: derived in (1) from contraction and V*=TV*.
- Bellman-compatible Hausdorff control: derived in (2), with both possible signs covered.
- Round-trip bridge: normalization and the finite-sum identity are established explicitly, followed by (3).
- Final certificate: obtained by grounding nonexpansiveness, the triangle inequality, and (1).

No specialized external metric construction or unresolved paper-specific result is used.
