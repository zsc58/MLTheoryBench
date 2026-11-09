# Reference Proof

## Proof Structure

1. Construct the Cartesian-product hidden Markov chain and derive its factorized initial and transition probabilities from subsystem independence.
2. Derive the usual unnormalized and normalized forward recursions for that chain.
3. Apply the column-major Kronecker/vectorization identities to convert the dense matrix-vector update into successive mode contractions, and prove equality by induction in time.
4. Count initialization and transition-update work separately, then compare the transition-update costs.

## Complete Proof

Index a joint state by m=(m_1,...,m_K), where m_k belongs to {1,...,M^k}. Independence of the subsystem chains gives joint initial mass rho_bar[m]=product_k rho^k[m_k] and joint transition probability Pi_bar[m',m]=product_k Pi^k[m'_k,m_k]. Under column-major indexing, these are the entries of rho_bar=rho^K tensor ... tensor rho^1 and Pi_bar=Pi^K tensor ... tensor Pi^1. The joint hidden process, with emission vector g_n, is therefore the stated ordinary HMM.

For this HMM, let b'_1=g_1 odot rho_bar and b'_n=g_n odot(Pi_bar a_{n-1}) for n>=2. Write d_n=sum_m b'_n[m] and a_n=b'_n/d_n. The conditional observation model and Markov property give b'_n[m]=p(y_n,S_n=m|y_{1:n-1}) for n>=2, with the analogous unconditional identity at n=1. Consequently d_n=p(y_n|y_{1:n-1}) for n>=2, d_1=p(y_1), and a_n[m]=p(S_n=m|y_{1:n}). This justifies the ordinary normalized forward recursion and its normalizing factors.

The outer-product entries satisfy (rho^1 outer ... outer rho^K)[m]=product_k rho^k[m_k]. Thus vec(B_1)=b'_1, c_1=d_1, and vec(A_1)=a_1. For any tensor T of the stated shape, expansion of the Kronecker product and the mode contractions gives

vec(T x_1 Pi^1 x_2 Pi^2 ... x_K Pi^K)[m'] = sum_m (product_k Pi^k[m'_k,m_k]) T[m] = (Pi_bar vec(T))[m'].

Vectorization also preserves entrywise multiplication and total sums. If vec(A_{n-1})=a_{n-1}, these identities give vec(B_n)=g_n odot(Pi_bar a_{n-1})=b'_n, then c_n=d_n and vec(A_n)=a_n. Induction proves the filter and normalizing-factor claims for every n.

With the usual dense arithmetic implementation, a mode-k contraction forms M output entries from M^k terms each, costing Theta(M M^k). One transition update therefore costs Theta(M sum_k M^k), including its O(M) entrywise and normalization work. A dense M-by-M transition update costs Theta(M^2). For N>=2, the ratio of these transition-update counts is Theta(M/(sum_k M^k))=Theta((product_k M^k)/(sum_k M^k)); exact constants depend on the arithmetic implementation. Forming the initial tensor costs O(KM), while dense initialization costs O(M). Thus the overall upper bounds are O(N M sum_k M^k) and O(N M^2). When N=1, there is no transition update and its cost ratio does not describe the complete algorithms.

If M^k=R for every k, with K fixed and N>=2, the respective overall costs are O(N R^{K+1}) and O(N R^{2K}). The transition-update ratio is Theta(R^{K-1}/K), hence of order R^{K-1} for fixed K.
