# Problem

## Setup

Let n be a positive integer and [n]={1,...,n}. An acyclic binary structural causal model (SCM) on variables X_1,...,X_n consists of a DAG, mutually independent exogenous noises with computable rational finite-support distributions, and computable Boolean structural equations evaluated in a topological order. Whenever a structural equation takes a tuple of parent values, that tuple is listed in increasing order of the parent labels.

Fix a computable canonical encoding of rational joint-distribution tables and of their indexed tuples. Its observational answer Obs(M) is the encoding of the induced joint distribution. A hard intervention do(X_i=x) replaces the equation for X_i by the constant x and leaves all other equations and noise distributions unchanged. Int_1(M) is the encoding of Obs(M) together with the joint distributions under do(X_i=0) and do(X_i=1), indexed by i=1,...,n.

Fix a universal prefix-free machine. Let K(z|w) be conditional Kolmogorov complexity, and define DL_1(M)=K(Obs(M)|n), DL_2(M)=K(Int_1(M)|n), and Delta_{2|1}(M)=K(Int_1(M)|Obs(M),n).

For each rooted labeled tree T on [n], define M_T by taking a Bernoulli(1/2) root and making every other node copy its parent. For n=2m+1, where m is a nonnegative integer, use the fixed labels r=1, a_i=i+1, and b_j=m+1+j. For every bipartite graph G between A={a_1,...,a_m} and B={b_1,...,b_m}, define M_G with a Bernoulli(1/2) root r, equations X_{a_i}=X_r, and
X_{b_j}=X_r AND (AND over i with (a_i,b_j) in E(G) of X_{a_i}); the empty AND is 1.

A Boolean gate schema gamma is a family (gamma_k)_{k>=0}, where gamma_k takes k binary parent inputs and a local noise value in a specified domain U_gamma and returns a bit. The family is uniformly computable: one fixed algorithm, independent of n and k, computes gamma_k when given k and its inputs. Let Gamma be a fixed finite set of such schemas and Pi a fixed finite set of finite-support rational noise distributions, both fixed independently of n. Only schema/noise choices with noise support contained in the schema's noise domain are permitted. Let M_{n,d}(Gamma,Pi) be the class of binary acyclic SCMs in which every node has at most d endogenous parents, and its equation applies the k-ary component of a chosen schema to its k parent values and a local noise with a distribution chosen from Pi. There are no additional per-node gate parameters or parent-input ordering choices.

All logarithms in the bounds are base 2. Implicit constants are independent of n,d,c and the particular tree, graph, or model. They may depend on the fixed machine and encodings and, in part 2, on Gamma and Pi.

## Task

Prove the following integrated theorem.

1. Every tree model M_T and every bipartite model M_G has the same observational distribution P* assigning probability 1/2 to the all-zero assignment and 1/2 to the all-one assignment, so DL_1=O(1). For a uniformly random rooted labeled tree and every c>=0,
Pr[Delta_{2|1}(M_T)>=(n-1)log_2 n-c-O(log n)]>=1-2^{-c},
while DL_2(M_T)<=(n-1)log_2 n+O(log n). For a uniformly random bipartite graph, meaning a uniformly chosen subset of A x B, and every c>=0,
Pr[Delta_{2|1}(M_G)>=m^2-c-O(log n)]>=1-2^{-c},
while DL_2(M_G)<=m^2+O(1).

2. For every fixed Gamma and Pi, there is a constant C_{Gamma,Pi}, uniform in n and d, such that for every 1<=d<=n-1 and every M in M_{n,d}(Gamma,Pi),
DL_2(M)<=C_{Gamma,Pi}n+n log_2(sum_{k=0}^d binom(n-1,k))+O(n log n),
and consequently Delta_{2|1}(M)=O(nd log_2(en/d)+n log n). The displayed families belong to suitable fixed finite gate and noise libraries and attain the n log n order at bounded indegree and the n^2 order in the dense regime. Thus these upper-bound orders are sharp across such classes; attainment is not asserted for every arbitrary choice of libraries.
