# Reference Proof

## Proof Structure

Soundness places each adversarial feature coordinate between its lower and upper bounds. The intervals with convex-combined endpoints are therefore nested as alpha increases. An elementary scalar endpoint-maximization identity gives monotonicity and the two-sided bounds; direct substitution gives the endpoint identities, and continuity follows from the finite maximum formula. For an affine head, the correctly typed feature-space logit-difference map is affine. Its signed weight decomposition gives the claimed same-parameter representation by regrouping.

## Complete Proof

Write h_a=h(x_adv) and h_t=h^t(x). Both are vectors in R^m. Since x_adv is in C_epsilon(x), soundness gives underline h_i <= h_{a,i} <= overline h_i for every i.

First establish the scalar identity

max_{r in [l,u]}(r-c)^2 = max{(l-c)^2,(u-c)^2}

for finite real l<=u and c. If l=u, the identity is immediate. Otherwise, every r in [l,u] is of the form r=(1-t)l+tu for some t in [0,1]. The triangle inequality gives

|r-c| <= (1-t)|l-c|+t|u-c| <= max{|l-c|,|u-c|}.

Squaring proves the required upper bound, and one of the two endpoints attains it. Thus the maximum exists and the identity also covers degenerate intervals.

For alpha in [0,1], define I_i^alpha=[ell_i^alpha,nu_i^alpha]. These are nonempty finite closed intervals: their width is alpha(overline h_i-underline h_i)>=0. The scalar identity gives

R_mix(alpha)=sum_{i=1}^m max_{r in I_i^alpha}(r-h_{t,i})^2.

If 0<=alpha<=beta<=1, then

ell_i^beta-ell_i^alpha=(beta-alpha)(underline h_i-h_{a,i})<=0,

nu_i^beta-nu_i^alpha=(beta-alpha)(overline h_i-h_{a,i})>=0.

Consequently I_i^alpha is a subset of I_i^beta. Every value of the squared distance on the smaller interval is at most its maximum on the larger interval, so

max_{r in I_i^alpha}(r-h_{t,i})^2 <= max_{r in I_i^beta}(r-h_{t,i})^2.

Summing proves that R_mix is nondecreasing on [0,1].

At alpha=0, ell_i^0=nu_i^0=h_{a,i}. Hence

R_mix(0)=sum_{i=1}^m(h_{a,i}-h_{t,i})^2=R_adv.

At alpha=1, ell_i^1=underline h_i and nu_i^1=overline h_i, giving R_mix(1)=overline R. Monotonicity therefore gives R_adv<=R_mix(alpha)<=overline R for every alpha in [0,1].

Each endpoint is affine in alpha, so each squared endpoint discrepancy is continuous. The maximum of two real continuous functions is continuous, as follows from max{p,q}=(p+q+|p-q|)/2. A finite sum preserves continuity, proving continuity of R_mix on the full closed interval.

For the affine-head conclusion, write g(a)=Wa+b with W in R^{K by m} and b in R^K. The correct feature-space logit-difference map is

zeta(a,y)=g(a)_y 1^K-g(a).

Its j-th coordinate is (W_{y,:}-W_{j,:})a+(b_y-b_j), so it has the affine representation tilde W a+tilde b specified in the task. Also, since f=g composed with h, zeta(h(u),y)=z_f(u,y) for every input u. In particular z_adv=z_f(x_adv,y).

Let A=[tilde W]_+ and B=[tilde W]_-. Then A is entrywise nonnegative, B is entrywise nonpositive, and tilde W=A+B. For any x' in C_epsilon(x), soundness and these signs imply

A underline h <= A h(x'),

B overline h <= B h(x').

Adding verifies the setup's description of underline z as a sound coordinatewise lower bound:

underline z=A underline h+B overline h+tilde b <= zeta(h(x'),y)=z_f(x',y).

Furthermore,

z_adv=(A+B)h_a+tilde b.

Substitute this and the definition of underline z into the mixture:

z_mix^alpha=(1-alpha)((A+B)h_a+tilde b)+alpha(A underline h+B overline h+tilde b)

= A((1-alpha)h_a+alpha underline h)+B((1-alpha)h_a+alpha overline h)+tilde b

= A ell^alpha+B nu^alpha+tilde b.

This is precisely the required coupled representation, using the same alpha in both feature vectors. All arguments allow equality in the soundness bounds, epsilon=0, alpha=0 or 1, and zero matrix entries. When K=1, the logit-difference map is zero and the same argument applies.
