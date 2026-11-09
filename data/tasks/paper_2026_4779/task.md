# Problem

## Setup

Let X be a measurable instance space and let H be a class of measurable functions from X to {0,1}. Write P(X) for the family of all probability distributions on X, and let Z=X x {0,1}, equipped with the product sigma-algebra. Let N={1,2,...}, and write X* and Z* for finite sequences, including the empty sequence, over these spaces.

For D in P(X) and h in H, let D_h be the law of (x,h(x)) when x~D. For a measurable predictor f:X->{0,1}, define

 L(f,D_h)=Pr_{(x,y)~D_h}[f(x)!=y].

A learner A takes a finite labeled training sequence and produces a possibly randomized binary predictor. Its predictions may depend on that sequence and the test instance, but not on an unknown marginal or unknown labeling hypothesis supplied separately. For each training length k, require the prediction probability

 (S,x) -> Pr[A(S)(x)=1]

to be measurable on Z^k x X. Expectations involving a randomized learner include its internal randomness, independent of the sample. Its worst-case realizable error is

 epsilon_A(D,m)=sup_{h in H} E_{S~D_h^m,A}[L(A(S),D_h)].

A certifier is a function C:X*->[0,1] measurable on each X^k. In particular, its input contains no labels. It is sound for A if, for every Q in P(X) and every k in N,

 E_{T~Q^k}[C(T)] >= epsilon_A(Q,k).

A rate epsilon:P(X) x N->[0,1] is certifiable if, for every D in P(X), there exist a learner A_D and a certifier C_D such that C_D is sound for A_D at every Q in P(X), and

 E_{T~D^k}[C_D(T)] <= epsilon(D,k)

for every k in N. The pair (A_D,C_D) may be chosen using knowledge of D, but it is fixed for all sample sizes and labeling hypotheses; when evaluated at another marginal Q, that same pair is used.

### The learner to be studied

For a finite unlabeled multiset U=(x_1,...,x_N), a transductive rule sees all instance values and the labels on all occurrences except one designated occurrence i, and predicts the label at x_i. Its worst-case leave-one-out error is

 max_{h in H} (1/N) sum_{i=1}^N Pr[the prediction from U with label i withheld differs from h(x_i)],

where probabilities include the rule's internal randomness. Repetitions in U are retained as separate occurrences.

The one-inclusion graph for U has vertex set

 V_U={(h(x_1),...,h(x_N)):h in H},

with an edge between two vertices exactly when they differ in one coordinate. The One-Inclusion Graph learner, denoted OIG, chooses a distribution over orientations of these edges that minimizes its worst-case leave-one-out error. Such a randomized orientation can equivalently specify, for each edge, the probability of pointing toward either endpoint. Its choice uses only the unlabeled multiset, not the revealed labels or the designated withheld occurrence.

Given the revealed labels, if only one vertex is consistent with them, OIG predicts its withheld coordinate. If two vertices are consistent, they are joined by an edge, and OIG predicts the withheld coordinate of the endpoint toward which that edge points. On an inconsistent input it may predict 0. Choices of minimizing orientations are permutation-equivariant: reordering the occurrences and then undoing that reordering leaves prediction probabilities unchanged. Use any such choice whose induced learner has the measurability property specified above.

To predict at a test point from a labeled training sequence, OIG applies this transductive rule to the multiset consisting of the training instances together with the test point, with only the test label withheld.

If H is empty, set its worst-case population and transductive errors to zero and let OIG predict arbitrarily.

For a constant alpha>0 and a function sigma:N x (0,1)->N, a learner A is relatively (alpha,sigma)-smart if

 epsilon_A(D,sigma(m,eta)) <= alpha epsilon(D,m)+eta

for every certifiable rate epsilon, every D in P(X), every m in N, and every eta in (0,1).

## Task

Prove that, for every instance space and hypothesis class satisfying the setup, every certifiable rate epsilon, every D in P(X), every integer m>=1, and every 0<eta<1, the integer budget

 n=ceil(e m^2/eta)-1

satisfies

 epsilon_OIG(D,n) <= e epsilon(D,m)+eta,

where e is the base of the natural logarithm. Equivalently, OIG is relatively (e,sigma)-smart for sigma(m,eta)=ceil(e m^2/eta)-1.
