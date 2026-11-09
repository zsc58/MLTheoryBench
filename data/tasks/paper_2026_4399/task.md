# Problem

## Setup

All logarithms are base two. For each nonnegative integer m, let U_m denote the uniform distribution on {0,1}^m. Let G be a deterministic polynomial-time generator mapping k-bit strings to n=ell(k) bits, where k>=1, ell(k)>k, and ell is polynomially bounded.

A function epsilon:N_{>=1}->[0,infinity) is negligible if, for every a>0, epsilon(k)<=k^{-a} for all sufficiently large k. Assume G is a non-uniform pseudorandom generator with the following security convention: there is a negligible function epsilon such that, for every probabilistic polynomial-time algorithm with advice strings of length polynomial in k, the resulting distinguisher family D_k satisfies

|Pr[D_k(G(U_k))=1]-Pr[D_k(U_n)=1]|<=epsilon(k)

for all sufficiently large k. The starting index may depend on the distinguisher family. Running time is polynomial in k, and the probabilities include the distinguisher's internal randomness.

Fix a universal prefix-free coding machine. The sample-space dimension m is supplied as auxiliary input to both evaluation and sampling and is not charged to program length. Let T:N->N be a fixed non-decreasing, time-constructible, polynomially bounded time function. Require T(m)>=c2 m+c3 for all m, where c2,c3 are fixed machine- and implementation-dependent constants large enough to evaluate and sample the uniform distribution within that time.

At dimension m, a T-time probabilistic model is a prefix-free program P with both of the following operations on the fixed machine:

- On input m and x in {0,1}^m, its evaluator halts within T(m) steps and returns an exact number P(x) in [0,1] with a finite binary expansion.
- On input m and an infinite random tape, its sampler halts within T(m) steps on every tape and returns an m-bit string.

The probabilities must satisfy

sum_{x in {0,1}^m}P(x)=1,

and the sampler, when its tape consists of independent fair bits, must output each x with probability P(x). Let P_T(m) be this dimension-specific feasible model class, and let |P| be the program length in bits. The notation P(x) refers to the probability mass function implemented by the program.

For a distribution Y on m-bit strings define

MDL_T(Y)=min_{P in P_T(m)}(|P|+E[-log P(Y)]).

Use -log 0=+infinity, and take the expectation over Y. Choose a minimizing program P*_Y using any fixed tie-breaking rule, and define

S_T(Y)=|P*_Y|,

H_T(Y)=E[-log P*_Y(Y)],

MDL_T(Y)=S_T(Y)+H_T(Y).

## Task

Prove that there is a fixed constant c, depending only on the coding machine and uniform-model implementation, such that for all sufficiently large k, with X=G(U_k) and n=ell(k),

H_T(X)>=n-2-n epsilon(k),

S_T(X)<=c+n epsilon(k),

and

H_T(G(U_k))>=H_T(U_k)+n-k-n epsilon(k)-c.

The same time-bound function T is used at the seed and output dimensions. The starting index for these conclusions may depend on the fixed generator, time bound, and security envelope.

Thus a deterministic polynomial-time stretch can increase time-bounded entropy by essentially the output-input length gap while the generated distribution has only constant-plus-negligible epiplexity.
