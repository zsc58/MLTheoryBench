# Reference Proof

## Proof Structure

1. Establish the sigmoid tail bound for a negative-advantage action.
2. Compute the perpendicular squared norms of the plain and gated gradient samples.
3. Average under the contaminated law and isolate the contamination terms.
4. Bound the overlap moment in the near-optimal regime and contrast the two contamination behaviors.

## Complete Proof

Write p_a=pi(a). For any p in (0,1] and c>0, sigma(c(-log p)/eta)=1/(1+p^(c/eta)) and sigma(-c(-log p)/eta)=p^(c/eta)/(1+p^(c/eta)). Hence a negative-advantage action of magnitude c has gate at most p^(c/eta). In the present bandit, every incorrect action has U(a)=-1/2, so w(a)<=p_a^(1/(2 eta)).

For an incorrect action, G_plain(a)=-(1/2)phi_pi(a) and G_gate(a)=-(1/2)w(a)phi_pi(a). Since Pi_perp is an orthogonal projector,
||Pi_perp G_plain(a)||^2=(1/4)||Pi_perp phi_pi(a)||^2,
while
||Pi_perp G_gate(a)||^2=(1/4)w(a)^2||Pi_perp phi_pi(a)||^2
<=(1/4)p_a^(1/eta)||Pi_perp phi_pi(a)||^2.

Summing these expressions against mu over incorrect actions gives
V_plain_perp,fail=(1/4) sum_{a != y*} mu(a)||Pi_perp phi_pi(a)||^2
and
V_gate_perp,fail<=(1/4) sum_{a != y*} mu(a)p_a^(1/eta)||Pi_perp phi_pi(a)||^2.

Using mu=(1-rho)pi+rho nu, the plain expression decomposes as
(1-rho)(1/4) sum_{a != y*} pi(a)||Pi_perp phi_pi(a)||^2 + (rho/4) S_nu,
where S_nu=sum_{a != y*}nu(a)||Pi_perp phi_pi(a)||^2. The gated bound decomposes into an on-policy term plus (rho/4) M_{nu,eta}^perp(pi), with M as defined in the setup. Thus the contaminated gated contribution is controlled by the overlap moment, whereas the plain contaminated contribution is exactly (rho/4)S_nu.

For every action, ||phi_pi(a)||=||e_a-pi||<=2, hence ||Pi_perp phi_pi(a)||^2<=4. If q=max_{a != y*}pi(a), then
M_{nu,eta}^perp(pi)<=4 sum_{a != y*}nu(a)pi(a)^(1/eta)<=4 q^(1/eta).
In the near-optimal regime q<=delta and delta tends to zero, so M_{nu,eta}^perp(pi) tends to zero for every fixed eta>0. Consequently the contaminated gated contribution is at most rho q^(1/eta), and vanishes (for fixed rho) as the incorrect-action probabilities vanish. If S_nu>=gamma>0 throughout the regime, the plain contaminated contribution is at least rho gamma/4 (for rho>0), and therefore does not vanish. This proves the claimed suppression-versus-persistence contrast.
