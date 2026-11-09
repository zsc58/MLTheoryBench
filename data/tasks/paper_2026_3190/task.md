# Problem

## Setup

Work in the complex Fourier representation of planar rotations. Orders are integers and angles are real. An order-m feature transforms under a global rotation by angle alpha as x_m -> exp(i m alpha)x_m. A fixed complex-linear map between feature spaces of the same order commutes with this action; multiplying orders m_1 and m_2 produces order m_1+m_2, multiplying by a conjugate produces order m_1-m_2, and order-zero features may act as invariant gates.

Fix an integer M >= 2 and a nonnegative integer m_max < M. For each global orientation phi, the environment has M neighbors at angles theta_k(phi)=phi+2 pi k/M for k=0,...,M-1. For integer order m define x_m^k(phi)=exp(i m theta_k(phi)) and A_m(phi)=sum_{k=0}^{M-1} x_m^k(phi). Retain input orders 0 <= m <= m_max.

A post-aggregation product expression is any finite complex-linear combination, with fixed complex coefficients, of products of the retained A_m, their conjugates, and order-zero gates. Each gate is a fixed complex-valued function of the retained aggregate vector, defined wherever it is applied and invariant under simultaneous rotation of that vector.

For the edge-preaggregation construction, consider any pair of retained orders m_1,m_2 satisfying m_1+m_2=M.

## Task

Prove that every post-aggregation product expression is independent of phi. Prove also that, for every retained pair m_1,m_2 satisfying m_1+m_2=M, multiplying the order-m_1 and order-m_2 features on each edge before aggregation yields M exp(i M phi), a nonzero orientation-sensitive component transforming by exp(i M alpha) under a further rotation alpha.
