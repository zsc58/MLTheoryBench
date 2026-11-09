# Problem

## Setup

Let X be an instance space and H subseteq {0,1}^X a nonempty binary hypothesis class of finite VC dimension d. The unknown marginal distribution is P on X, and the unknown realizable target is h* in H. Let n>=2 be an integer, and let alpha in [0,1] be a known parameter. All classifiers and learning procedures under consideration are measurable so that the probabilities and expectations below are defined.

At round 0 the learner receives n independent examples (X,h*(X)), with X distributed according to P, and outputs a binary classifier h_0. At each round t>=1, it receives n fresh independent covariates from P. For each covariate X, independently draw a Bernoulli(alpha) source indicator, independent of the covariates, the past, and the learner's randomization. The displayed label is h_{t-1}(X) if that indicator is one, and h*(X) otherwise. After receiving the complete batch, the learner outputs h_t. All samples are retained with their multiplicities, order, and round boundaries.

The learner observes only these covariates and displayed labels, together with its own previous classifiers and randomization; it does not observe the source indicators and is not given P or h*. It may depend on H, n, and alpha. General learners may output binary classifiers outside H. Define

L(h)=Pr_{X distributed according to P}[h(X)!=h*(X)].

Expectations include both sample-process and learner randomness. An empirical-risk minimizer minimizes the fraction of incorrectly classified displayed labels in the entire retained sample, counting multiplicity, over H.

For the lower-bound clause only, let X=R^(d-1), with its Euclidean structure, and let H consist of the affine halfspaces

h_{w,b}(x)=1{<w,x>+b>=0},

including the two constant classifiers. Use the following ERM selector. On a finite sample containing both labels that admits zero empirical error, select a separating halfspace maximizing

min_i (2y_i-1)(<w,x_i>+b)/||w||

over nonzero w and real b. On a one-label sample select the matching constant classifier. On a nonseparable sample select any empirical-risk minimizer. Any remaining ties may be resolved arbitrarily.

For alpha>1/2, let W_0=0 and let W have independent increments +1 with probability alpha and -1 with probability 1-alpha. Define

c_alpha=Pr(W_s>=1 for every integer s>=1).

Assume the following PU primitive. For any nonempty binary class C of VC dimension at most d and 0<epsilon,delta<1, there is a learner depending on C, epsilon, and delta, but not on an unknown marginal P or target c in C, with this guarantee whenever P(c(X)=1)>0: given independent i.i.d. positive covariates from P conditioned on c(X)=1 and independent i.i.d. unlabeled covariates from P, it returns a binary classifier a satisfying Pr_{X distributed according to P}[a(X)!=c(X)]<=epsilon with probability at least 1-delta. Sufficient positive and unlabeled sample counts m_P(epsilon,delta) and m_U(epsilon,delta) are each at most

ceil(C_PU [d log(1/epsilon)+log(1/delta)]/epsilon)

for a universal constant C_PU. The returned classifier need not belong to C. The primitive is asserted only when the positive conditional distribution is defined.

## Task

Prove the following integrated theorem.

1. For every n>=2, d>=2, and alpha in (1/2,1), there are a distribution P and a target h* in the affine-halfspace class H specified above, which has VC dimension d, such that the recursive max-margin ERM iterates satisfy

liminf_{t->infinity} E[L(h_t)] >= c_alpha/(8n) > 0.

2. For every nonempty binary class H of finite VC dimension d, every integer n>=2, and every 0<=alpha<1, there exists one recursive learner, depending on H, n, and alpha but not on P or h*, such that simultaneously for every marginal P and every target h* in H, and for every integer t>=1,

E[L(h_t)] <= tilde-O(sqrt(d/((1-alpha)nt))).

The hidden constants are universal. Here tilde-O permits factors polynomial in log(e+n), log(e+t), log(e+d), and log(e/(1-alpha)), but no additional polynomial dependence on these parameters. The learner uses only the batches and observations described in the setup.
