# Problem

## Setup

For a positive integer d, let W_d={w in R^d: ||w||_2<=1}. A stochastic convex optimization instance consists of a finite instance space Z, a distribution D on Z, and a loss f:W_d x Z -> R such that f(.,z) is convex and 1-Lipschitz with respect to the Euclidean norm for every z in Z.

Define F(w)=E_{z~D} f(w,z). For a sample S=(z_1,...,z_m) drawn i.i.d. from D, define F_S(w)=m^{-1}sum_{r=1}^m f(w,z_r). For epsilon>=0, an epsilon-ERM is any w_S in W_d satisfying F_S(w_S)<=min_{w in W_d}F_S(w)+epsilon. Strong convexity is with respect to the Euclidean norm, with the convention that its quadratic term is (lambda/2)||u-v||_2^2.

## Task

Prove that there are universal constants c,C>0 such that both statements below hold for every integer m>=6, with dimension d=6m.

1. **Constant lower bound.** There exists an instance as defined above whose loss f(.,z) is m^{-3/2}-strongly convex for every z in Z. There is an event E in Z^m with P_{S~D^m}(E)>=1/2 such that, for every S in E, every 0<=epsilon<=c m^{-3/2}, and every epsilon-ERM w_S,

   F(w_S)-min_{w in W_d}F(w)>=C.

2. **Curvature-dependent lower bound.** For every lambda satisfying m^{-3/2}<=lambda<=m^{-1/2}, there exists an instance as defined above whose loss f(.,z) is lambda-strongly convex for every z in Z. There is an event E in Z^m with P_{S~D^m}(E)>=1/2 such that, for every S in E, every 0<=epsilon<=c/(lambda m^3), and every epsilon-ERM w_S,

   F(w_S)-min_{w in W_d}F(w)>=C/(lambda m^{3/2}).

In each statement the instance is fixed before S is drawn. The instance in the second statement may depend on m and lambda; its event and probability assertion are for that instance. The constants c and C are common to both statements and independent of m and lambda. In each case the conclusion is simultaneous for all indicated approximate ERMs on the same sample event, and the exact ERM is unique for every sample.
