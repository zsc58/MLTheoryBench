# Reference Proof

## Proof Structure

1. Verify the fixed-order rotation action and the order rule for edge multiplication.
2. Compute the finite Fourier sum over the M-fold orbit, including order zero.
3. Deduce that post-aggregation product expressions and their gates cannot recover orientation from the retained aggregates.
4. For any retained pair whose orders sum to M, compute the edge-preaggregation product aggregate and its rotation action.

## Complete Proof

Let M>=2 be an integer and let m_max be a nonnegative integer with m_max<M. All orders are integers and all angles are real. For a global rotation by alpha, an order-m feature transforms as x_m -> exp(i m alpha)x_m. A fixed complex-linear map W between spaces carrying this same order commutes with the action because

 W(exp(i m alpha)x_m)=exp(i m alpha)W x_m.

This calculation does not assert commutation for arbitrary maps mixing distinct orders. Also,

 (exp(i m_1 alpha)x_{m_1})(exp(i m_2 alpha)x_{m_2})
 =exp(i(m_1+m_2)alpha)x_{m_1}x_{m_2},

and conjugating the second factor changes the sum of orders to their difference.

The neighbor angles and unit angular features are

 theta_k(phi)=phi+2 pi k/M,
 x_m^k(phi)=exp(i m theta_k(phi)),
 k=0,...,M-1.

For any integer m, set q=exp(2 pi i m/M). Then q^M=1, and

 A_m(phi)=exp(i m phi) S,
 S=sum_{k=0}^{M-1}q^k.

If q=1, equivalently M divides m, then S=M. If q!=1, multiplying the finite sum by 1-q gives

 (1-q)S=1-q^M=0,

so S=0. Therefore A_m(phi)=M exp(i m phi) when M divides m, and A_m(phi)=0 otherwise. In particular, every retained positive order 1<=m<=m_max<M has A_m(phi)=0, while A_0(phi)=M. Thus the entire retained aggregate vector is the same for every real phi.

Every gate is a fixed, well-defined function of that retained aggregate vector, so its value is also the same for every phi. Consequently, each product of retained aggregates, their conjugates, and these gates is independent of phi. Finite complex-linear combinations with fixed coefficients remain independent of phi as well. This proves the post-aggregation claim, including expressions containing only scalar factors or gates. It does not claim that every scalar expression is zero.

For the edge construction, suppose a pair of retained orders m_1,m_2 with m_1+m_2=M is given. Both orders are positive: if one were zero, the other would be M, contrary to retention below M. They need not be distinct. Form

 y_k(phi)=x_{m_1}^k(phi)x_{m_2}^k(phi)
         =exp(i M theta_k(phi))
         =exp(i M phi)exp(2 pi i k)
         =exp(i M phi).

Hence the unnormalized product aggregate is

 B_M(phi)=sum_{k=0}^{M-1}y_k(phi)=M exp(i M phi).

Its magnitude is M>0. It is nonconstant in phi, for example B_M(0)=M and B_M(pi/M)=-M. Under a further rotation alpha,

 B_M(phi+alpha)=exp(i M alpha)B_M(phi).

Thus it is a nonzero orientation-sensitive order-M component. Orientation sensitivity means nonconstancy, not that every nonzero rotation changes the value: the component is periodic with period 2 pi/M, consistently with the environment's symmetry.

## Boundary And Dependency Checks

The direct-aggregation conclusion also holds when m_max=0. If there is no retained pair summing to M, the edge claim has no instance; neither the statement nor this proof asserts pair existence from m_max<M alone. The output order M is not subjected to the input cutoff in the stated construction. The proof uses the specified unit angular inputs and does not assert nonzero output for every choice of learnable weights. All theorem-critical obligations are derived above; generalized contraction algorithms and specialized external expressivity results are not invoked.
