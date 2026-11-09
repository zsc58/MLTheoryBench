# Problem

## Setup

Let X be a nonempty topological space equipped with a sigma-algebra containing its Borel sets, and let V be a measurable output space. Let P_X and Q_X be probability measures on X that are mutually absolutely continuous and have full support: every nonempty open subset of X has positive measure under each law. Fix alpha in [0,1] and set

R_X = alpha P_X + (1-alpha) Q_X.

Let k be a real-valued continuous bounded positive definite kernel on X with RKHS H_k, and let ell be a real-valued measurable characteristic positive definite kernel on V with RKHS H_ell.

Let kappa_P and kappa_Q be fixed regular Markov-kernel versions of the conditional laws P_{Y|X} and Q_{Z|X}, respectively. Define the joint laws used below to be

R_X(dx) kappa_P(x,dy), and R_X(dx) kappa_Q(x,dz).

All expectations involving X below use R_X. Expectations involving (X,Y) or (X,Z) use these respective joint laws.

Write k_x=k(.,x). Assume the map x -> k_x tensor k_x is strongly measurable, and define the positive trace-class covariance operator

C_XX = E_{X~R_X}[k_X tensor k_X].

For a positive operator C_XX and any real a>=0, C_XX^a denotes its spectral-calculus power, with C_XX^0=I.

For each x, assume y -> ell(.,y) and z -> ell(.,z) are strongly measurable under the respective conditional laws and have finite integrals of their H_ell norms. Define the Bochner conditional mean embeddings

mu_{Y|x} = integral ell(.,y) kappa_P(x,dy),
mu_{Z|x} = integral ell(.,z) kappa_Q(x,dz).

Assume x -> mu_{Y|x} and x -> mu_{Z|x} are strongly measurable. There exist fixed exponents gamma_P,gamma_Q>=1/2 such that, for every g in H_ell, the functions

x -> integral g(y) kappa_P(x,dy),
x -> integral g(z) kappa_Q(x,dz)

belong to range(C_XX^{gamma_P}) and range(C_XX^{gamma_Q}), respectively.

Let C_{Y|X}, C_{Z|X}:H_k -> H_ell be the corresponding bounded Hilbert-Schmidt conditional mean operators, satisfying, for every g in H_ell and x in X,

(C_{Y|X}^*g)(x) = integral g(y) kappa_P(x,dy),
(C_{Z|X}^*g)(x) = integral g(z) kappa_Q(x,dz).

Equivalently, their conditional mean embeddings are C_{Y|X}k_x and C_{Z|X}k_x. Define Delta=C_{Y|X}-C_{Z|X}.

Assume the joint tensor-feature maps below are strongly measurable and that, under the respective joint laws,

E[||k_X||_{H_k} ||ell(.,Y)||_{H_ell}] < infinity,
E[||k_X||_{H_k} ||ell(.,Z)||_{H_ell}] < infinity.

Define the Bochner joint mean embeddings

mu_XY = E[k_X tensor ell(.,Y)],
mu_XZ = E[k_X tensor ell(.,Z)]

in H_k tensor H_ell. Use the canonical tensor/Hilbert-Schmidt identification, the Hilbert-Schmidt norm, and the operator trace.

For every real s>=0, define

CMMD_s^2 = ||Delta C_XX^{s/2}||_{HS}^2.

Set sigma_max=||C_XX||_{op}. For the scalar factor in the claim below, use sigma_max^0=1, including when sigma_max=0.

## Task

Prove that

1. The level-1 and level-2 quantities agree with the conditional and joint embedding discrepancies and have the following trace representations:

CMMD_1^2 = E_{X~R_X}||mu_{Y|X}-mu_{Z|X}||_{H_ell}^2 = Tr(Delta^*Delta C_XX),

CMMD_2^2 = ||mu_XY-mu_XZ||_{H_k tensor H_ell}^2 = Tr(Delta^*Delta C_XX^2).

2. For every real s>=s'>=0,

CMMD_s^2 <= sigma_max^(s-s') CMMD_{s'}^2.
