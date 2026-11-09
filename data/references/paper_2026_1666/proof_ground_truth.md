# Reference Proof

## Proof Structure

1. Verify the graphical and observational-domain hypotheses of standard backdoor adjustment.
2. Expand the adjusted conditional using the conditional latent model.
3. Compare the full likelihood integral with the importance-weight expectation restricted to variational support, apply Jensen's inequality, and obtain the three KL terms.

## Complete Proof

Fix theta. Write P_H and P_Z for its observational marginals and P_{Z|h} for the chosen observational conditional law of Z given H=h.

The standard backdoor-adjustment result used here states that, when Z contains no descendant of H and blocks every backdoor path from H to Y, the intervention law is identified by averaging the observational outcome conditional over P_Z, on the observational conditional-distribution domain with overlap. With fixed conditional versions, the assertion holds for P_H-almost every h satisfying P_Z << P_{Z|h}. In the discrete case it therefore applies at every positive-probability h satisfying overlap. The graphical assumptions are given in the setup, and overlap is explicitly part of admissibility. Unsupported values are not covered by the almost-everywhere assertion.

The no-descendant condition gives the unchanged intervention distribution of Z. Total probability under intervention and the adjustment result therefore give, for almost every eligible h and each label y,

p_theta(y | do(H=h)) = integral p_theta(y | h,z) P_Z(dz).

The exceptional set can be chosen independently of phi, and simultaneously for every y because the label set is finite.

The stipulated conditional latent law and label kernel give, for observationally almost every (h,z),

p_theta(y | h,z) = integral integral p_theta(y | h,u,z) P_{U|h}(du) P_{V|h}(dv).

This is ordinary conditional marginalization: the conditional distribution of (U,V) is the specified product and the label kernel does not depend on V. Disintegration makes this identity valid for P_{Z|h}-almost every z, for P_H-almost every h. Admissible overlap transfers it to P_Z-almost every z. As before, a common exceptional set suffices for all labels.

Now fix such an h, a label y, and any phi making the quadruple admissible. Let

P = P_Z tensor P_{U|h} tensor P_{V|h},
Q = Q_{Z|h} tensor Q_{U|h} tensor Q_{V|h},
L(z,u,v) = p_theta(y | h,u,z),
A = p_theta(y | do(H=h)).

The preceding identities yield A = integral L dP. Admissibility gives A > 0. Since Y is categorical, 0 <= L <= 1 and A <= 1.

Choose the product dominating measure from the setup and write p and q for the densities of P and Q. Factorwise absolute continuity gives Q << P. Let S = {q > 0}. On S, outside a Q-null set, p > 0 and L > 0. Define R = Lp/q there; its value elsewhere is immaterial. Then

E_Q[R] = integral over S of Lp <= integral Lp = A.

This is an inequality, not generally an equality: Q may omit positive model likelihood mass. Moreover R > 0 Q-almost everywhere, so 0 < E_Q[R] <= A <= 1.

We also verify log-integrability before invoking Jensen. For any one of the three factor pairs Q_i << P_i, with t_i = dQ_i/dP_i, the negative part of log t_i has Q_i-integral at most 1/e, because -t log t <= 1/e on 0 < t < 1. Finite KL(Q_i || P_i) therefore implies integrability of |log t_i|. By product normalization these log-ratios are also integrable under Q. The reconstruction log-likelihood is integrable by admissibility. Consequently

log R = log L - log t_Z - log t_U - log t_V

is Q-integrable.

The audited standard Jensen inequality for the concave logarithm states E[log R] <= log E[R] for a positive random variable with integrable logarithm and finite positive expectation. All these hypotheses have just been verified. Monotonicity of the logarithm and Jensen give

ell_theta(h,y) = log A >= log E_Q[R] >= E_Q[log R].

Integrating the combined log-ratios, rather than separating potentially divergent log densities, now gives

E_Q[log R] = E_{q_phi(z | h)q_phi(u | h)}[log p_theta(y | h,u,z)]
- KL(q_phi(z | h) || p_theta(z))
- KL(q_phi(u | h) || p_theta(u | h))
- KL(q_phi(v | h) || p_theta(v | h)).

The first expectation loses V because L is independent of V and Q_{V|h} is normalized. Its KL penalty remains in the density ratio. Thus both requested conclusions hold for each theta, for P_H-almost every h, simultaneously for every admissible phi and label y. The discrete formulas are the corresponding sums.

## Obligation Closure

The adjustment obligation is closed by the stated standard result with graphical and overlap hypotheses verified. Conditional marginalization, transfer from P_{Z|h} to P_Z, product absolute continuity, support-restricted integration, log-integrability, Jensen, and the KL decomposition are explicitly derived above. No paper-specific unresolved dependency is used.
