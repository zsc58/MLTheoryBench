# Problem

## Setup

Let Z be a compact Polish metric space with metric d. Let X be a nonempty compact subset of Z, and let V be a nonempty Borel subset of X. For a Borel subset S of Z, write P(S) for the Borel probability laws on S, viewed as laws on Z by extension by zero. Fix finite real parameters p>=1 and epsilon>0.

For probability laws mu,nu on Z, define

W_p(nu,mu)=(inf_{pi in Pi(mu,nu)} integral_{Z x Z} d(x,y)^p pi(dx,dy))^(1/p),

where Pi(mu,nu) is the set of Borel probability laws on Z x Z with first marginal mu and second marginal nu.

An epsilon-LDP mechanism is a map M:P(X)->P(V) such that M[mu](A)<=exp(epsilon)M[mu'](A) for all inputs mu,mu' and Borel A subseteq V.

For a nonnegative finite Borel measure m on V, define Q_{m,epsilon}={nu in P(V): exp(-epsilon/2)m(A)<=nu(A)<=exp(epsilon/2)m(A) for every Borel A subseteq V}, assuming it is nonempty. A Wasserstein projection mechanism M_{m,epsilon} maps each mu to any minimizer of W_p(nu,mu) over nu in Q_{m,epsilon}. Define U[M]=sup_{mu in P(X)}W_p(M[mu],mu), with both laws viewed on Z.

In the finite specialization, let k,k_v be positive integers with 1<=k_v<=k, let X={1,...,k} and V={1,...,k_v}, and set alpha=exp(-epsilon/2), beta=exp(epsilon/2), and c_{ij}=d(i,j)^p. Here R_+ denotes the nonnegative real numbers, (a)_+=max{a,0}, and delta_i denotes the probability law concentrated at i.

Let D={m in R_+^{k_v}: 1/beta<=sum_j m_j<=1/alpha}. For each i, fix an ordering sigma_i(1),...,sigma_i(k_v) of the outputs such that c_{i,sigma_i(1)}<=...<=c_{i,sigma_i(k_v)}, breaking ties arbitrarily. For m in D, set s(m)=1-alpha sum_j m_j and b_j(m)=(beta-alpha)m_j, and define

phi_i(m)=alpha sum_j m_j c_{ij}+sum_{t=1}^{k_v} c_{i,sigma_i(t)} min{b_{sigma_i(t)}(m),(s(m)-sum_{r<t}b_{sigma_i(r)}(m))_+}.

An empty sum is zero.

## Task

Prove that:

1. Every epsilon-LDP mechanism M admits a nonnegative finite base measure m with M[P(X)] subseteq Q_{m,epsilon}; consequently W_p(M_{m,epsilon}[mu],mu)<=W_p(M[mu],mu) for every mu and U[M_{m,epsilon}]<=U[M].
2. In the finite specialization, each phi_i is the pth-power cost of projecting delta_i onto Q_{m,epsilon}; f(m)=max_i phi_i(m) is convex on D and attains its minimum at some m*; and the WPM based on m* is minimax optimal, with U[M_{m*,epsilon}]=inf_{M' epsilon-LDP}U[M']=min_{m in D}f(m)^(1/p).
