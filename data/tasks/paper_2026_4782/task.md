# Problem

## Model and posterior notation

Let d be a positive integer, let r>0, and let X be a nonempty finite subset of [0,r]^d. Let k be a positive semidefinite covariance kernel on X with k(x,x)<=1. Draw f~GP(0,k). Query i at x_i in X has response

`y_i=f(x_i)+epsilon_i`,

where the observation noises are independent N(0,sigma_noise^2), sigma_noise>0, and independent of f and the independent randomization used by the procedure.

Datasets are indexed lists, so repeated query locations are retained. For an indexed dataset D=((a_i,b_i))_{i=1}^m, let K_D=(k(a_i,a_j))_{i,j=1}^m, k_D^vec(x)=(k(a_i,x))_{i=1}^m, and b_D=(b_i)_{i=1}^m. Define

`mu(x;D)=k_D^vec(x)^T(K_D+sigma_noise^2 I)^{-1}b_D`,

`k_D(x,x')=k(x,x')-k_D^vec(x)^T(K_D+sigma_noise^2 I)^{-1}k_D^vec(x')`,

`sigma^2(x;D)=k_D(x,x)`, and `sigma(x;D)=sqrt(sigma^2(x;D))`.

For the empty dataset, mu(x;empty)=0 and k_empty=k. For an index set N, write D_N=((x_i,y_i))_{i in N}, in increasing index order; the corresponding matrix and vector may also be denoted K_N and k_N(x). Write D_{t-1}=D_{ {1,...,t-1} } for the full actual dataset, including responses that may not yet have been revealed to the procedure.

For each positive integer n, define

`gamma_n=max_{a_1,...,a_n in X} I((f(a_i)+e_i)_{i=1}^n ; (f(a_i))_{i=1}^n)`,

where the locations in this maximization are deterministic, the e_i are independent N(0,sigma_noise^2) and independent of f, and I denotes Shannon mutual information using natural logarithms. Set gamma_0=0. Let gamma_bar:[0,infinity)->[0,infinity) be a finite-valued, nondecreasing concave function satisfying gamma_bar(n)>=gamma_n for every nonnegative integer n. Write gamma_bar_s=gamma_bar(s).

## Procedure and information timing

There are Q workers, where Q is a positive integer. Initially no observations are available. At the beginning of round t, N_{t-1} is the subset of {1,...,t-1} whose responses have been revealed. Completed responses are retained, so N_t contains N_{t-1}. Each pending evaluation occupies one worker, and each worker has at most one pending evaluation. A new query is assigned only to an available worker; if necessary, the procedure waits for a worker to become available before the next round. In particular, at most Q-1 previous evaluations are pending when a new query is selected.

Selected locations and completed/pending indicators are known, but a pending response is not available until completion. Selection, assignment, and completion decisions are causal: they may use previously revealed observations, selected locations, past algorithmic randomness, and independent timing randomness, but not unrevealed function values or observation noises. Evaluation timing supplies no additional information about unrevealed responses.

Let A be a measurable base rule mapping an indexed dataset to a point of X. It may use fresh internal randomization, but uses no information other than its supplied dataset. Its internal randomization is independent of the unknown objective conditional on that dataset.

At round t, using fresh randomness, draw

`g_t~GP(mu(.;D_{N_{t-1}}),k_{D_{N_{t-1}}})`.

Conditional on the information available before this draw, g_t is independent of f. Form D^{fant}_{t-1} by retaining the completed responses and replacing each pending response at index i by

`g_t(x_i)+epsilon_i^(t)`,

where the fantasy noises are independent N(0,sigma_noise^2), independent of the current posterior draw and all other randomness. Select

`x_t=A(D^{fant}_{t-1})`

using fresh base-rule randomization, and assign this query to an available worker.

## Base-rule assumption

Assume the following uniform condition. There are deterministic sequences zeta_t>=0 and xi_t in R and measurable families of real-valued auxiliary random variables U_t(D),V_t(D) with the following property for every positive integer t and every fixed indexed dataset D of length t-1.

In the experiment where h~GP(mu(.;D),k_D), h^*=max_{x in X}h(x), and a=A(D) is selected with internal randomness independent of h, the auxiliary variables satisfy

`E[h^*-h(a)] <= E[U_t(D) sigma(a;D)+V_t(D)]`,

`E[U_t(D)^2]<=zeta_t`, `E[|V_t(D)|]<infinity`, and `E[V_t(D)]<=xi_t`.

These expectations are taken in this fixed-dataset experiment. The same zeta_t and xi_t apply to every D. The auxiliary variables may depend on h and on the algorithmic randomness; they are not additional inputs to A and need not be nonnegative.

Assume also

`sum_{t=1}^T zeta_t=tilde O(T)` and `sum_{t=1}^T xi_t=O(1)`.

Here tilde O(T) allows a fixed power of 1+log T: there exist finite constants C_z,C_x and p>=0, independent of T and D, such that for all sufficiently large positive integers T,

`sum_{t=1}^T zeta_t <= C_z T(1+log T)^p` and `|sum_{t=1}^T xi_t|<=C_x`.

## Target

Set

`C1=2/log(1+sigma_noise^{-2})`,

`C2=2+2 log(|X|/2)`,

`B_T=sqrt(C1 gamma_T sum_{t=1}^T zeta_t)+sum_{t=1}^T xi_t`,

and

`BCR_T=E[sum_{t=1}^T(f^*-f(x_t))]`, where `f^*=max_{x in X}f(x)`.

The expectation defining BCR_T is over all randomness in the objective, observations, procedure, and permitted timing.

Prove that for every positive integer T,

`BCR_T<=B_T+sqrt(C1 C2 Q T gamma_bar_{T/Q})`.
