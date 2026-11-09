# Reference Proof

For each stratum l in the support of L, write p_l=P(L=l)>0 and q(Z)=I{f(Z)>0}. The rule-dependent part of V(D) is E[delta_R(Z)q(Z)]; the remaining part is constant by SUTVA and conditional ignorability.

For either action, conditional demographic parity is equivalent to equality of the two conditional action probabilities for S=0 and S=1 within each stratum. By the definition of psi_l,

E[q(Z)I{L=l}psi_l(S)] = p_l{P(q=1|S=1,L=l)-P(q=1|S=0,L=l)}.

Thus the epsilon-CDP constraint is exactly |E[q(Z)I{L=l}psi_l(S)]|<=p_l epsilon for every l. The objective and constraints separate across strata.

Fix l and define G_l(omega)=E[I{delta_R(Z)-omega psi_l(S)>0}I{L=l}psi_l(S)]. Pointwise maximization of q(delta_R-omega psi_l)I{L=l} gives q_omega=I{delta_R-omega psi_l>0} on the stratum; outside it the choice does not affect this stratum’s Lagrangian. The function G_l is non-increasing: increasing omega can only remove selected observations in S=1, where psi_l>0, and add selected observations in S=0, where psi_l<0.

Let B be a uniform bound on |delta_R|, which exists because both treatment-specific conditional means are uniformly bounded. Since |psi_l(s)|<=1/c0, any K>Bc0^{-1} has the following property: at omega=K, the rule selects no S=1 observations and all S=0 observations in stratum l; at omega=-K, it selects all S=1 observations and no S=0 observations there. Consequently G_l(K)=-p_l and G_l(-K)=p_l. Because G_l is continuous, if G_l(0)>p_l epsilon the intermediate value theorem gives omega_l* in (0,K) with G_l(omega_l*)=p_l epsilon. If G_l(0)<-p_l epsilon, it gives omega_l* in (-K,0) with G_l(omega_l*)=-p_l epsilon. Otherwise choose omega_l*=0. A common finite K may be used for all strata.

The selected rule is feasible: its moment is the relevant boundary value in either active case, and is within tolerance at zero. For any measurable feasible q, pointwise maximization gives

E[(q-q_{omega_l*})(delta_R-omega_l*psi_l)I{L=l}]<=0.

If omega_l*>0, the selected moment is p_l epsilon and feasibility makes the feasible moment difference nonpositive; the displayed inequality therefore implies E[(q-q_{omega_l*})delta_R I{L=l}]<=0. If omega_l*<0, the selected moment is -p_l epsilon and feasibility makes the moment difference nonnegative, yielding the same objective inequality. If omega_l*=0, pointwise maximization of delta_R directly gives that inequality. Summing over the finite strata proves global optimality and gives

D*(Z)=2I{delta_R(Z)-sum_l I{L=l}omega_l*psi_l(S)>0}-1.

The value inequality for D follows because its value differs from the treatment-effect objective only by a constant.
