# Problem

## Setup

Consider K independent finite-state Markov chains. Chain k has state set {1,...,M^k}, column-stochastic transition matrix Pi^k, and initial probability vector rho^k. At each time n=1,...,N the observed value y_n has nonnegative emission likelihood E_n[m_1,...,m_K] conditional on the tuple of subsystem states. Let M=product_{k=1}^K M^k and assume all normalizing constants below are positive.

Let the Cartesian-product state be m=(m_1,...,m_K). The joint hidden process therefore defines an ordinary HMM, denoted H_bar, on the M tuple states; write rho_bar and Pi_bar for its induced initial vector and transition matrix, and let g_n=vec(G_n) be the emission vector obtained from the tensor G_n with entries E_n[m]. Use column-major vectorization.

For a tensor T of shape (M^1,...,M^K), let [T] denote the sum of all entries, let odot denote entrywise multiplication, and define the mode-k contraction by

(T x_k P)_{i_1,...,i_K}=sum_{j_k=1}^{M^k} P_{i_k,j_k}T_{i_1,...,j_k,...,i_K}.

Define tensorized forward quantities by

B_1=G_1 odot(rho^1 outer ... outer rho^K), c_1=[B_1], A_1=B_1/c_1,

B_n=G_n odot(A_{n-1} x_1 Pi^1 x_2 Pi^2 ... x_K Pi^K), c_n=[B_n], A_n=B_n/c_n (n>=2).

Let a_n be the standard normalized forward filter of H_bar with initial vector rho_bar, transition matrix Pi_bar, and emissions g_n.

## Task

Prove that for every n=1,...,N,

vec(A_n)=a_n and c_n is the ordinary HMM normalizing factor. Establish the overall arithmetic upper bounds O(N M sum_{k=1}^K M^k) for tensorized filtering and O(N M^2)=O(N M product_{k=1}^K M^k) for dense filtering on H_bar. For N>=2, show that the ratio of their per-transition-update arithmetic costs is of order product_k M^k/(sum_k M^k), up to constant factors. In the equal-size case M^k=R, with K fixed and N>=2, give the tensorized bound O(N R^{K+1}) and the dense bound O(N R^{2K}), and show that the asymptotic transition-update speedup is of order R^{K-1}. When N=1, no transition update occurs and no transition-update speedup is claimed.
