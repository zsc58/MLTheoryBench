# Problem

## Setup

Let N,K,M be positive integers. There are N agents with nonempty locally compact standard Borel observation spaces Y^i and nonempty finite action spaces U^i, and a nonempty compact metric hidden-state space X. Write Y=product_i Y^i and U=product_i U^i. The bounded continuous one-stage cost is c:X times U to R, and beta is in (0,1).

At time t, conditional on x_t, the joint observation y_t has law

Q(dy|x_t)=product_i Q^i(dy^i|x_t).

Each Q^i has a measurable nonnegative density h_i(x,y^i) relative to a fixed reference probability psi_i on Y^i; its integral is one for every x, and h_i(.,y^i) is continuous for every y^i. After observations and actions, the next state has law T(dx'|x_t,u_t). The kernel T is continuous in total variation in (x,u). Initial state laws and the model are known to the agents.

For t=qK+r, 0<=r<K, common information is the joint observation and realized-action history strictly before qK. Agent i additionally has its observations y^i_[qK,t] and actions u^i_[qK,t-1] from the current period. All policies are measurable and use only this information.

A block prescription a consists of deterministic measurable maps f^i_r from agent i's within-period observations and previous actions to U^i, for r=0,...,K-1. The coordinator chooses the entire block prescription at the sharing boundary using common information. Give these prescription spaces the product Young topology: for each i,r and fixed preceding private action sequence, the measure induced by the map on (Y^i)^(r+1) times U^i, with observation marginal psi_i^(r+1), is given the weak topology. Assume the admissible prescription space is compact in this topology. Probability measures on X have their weak topology; retained observation/realized-action windows have the product topology.

Use full total variation,

||mu-nu||_TV=2 sup_A |mu(A)-nu(A)|=sup_{|f|<=1}|integral f dmu-integral f dnu|.

For a prior p, a joint observation y, and a realized joint action u, define the one-step predictor update by

F(p,u,y)(A)= [integral T(A|x,u) product_i h_i(x,y^i) p(dx)]/[integral product_i h_i(x,y^i) p(dx)].

Choose a measurable version on zero-denominator events. The K-step map G is K successive applications of F along a complete block of joint observations and realized actions. Intermediate joint records used to define G are not revealed to the agents before the next sharing boundary.

Let pi_q be the conditional law of x_qK given the full common information. Let I_q^M be the ordered joint observation/realized-action record from times (q-M)K through qK-1. Define the true augmented state

hat Z_q=(pi_(q-M),I_q^M).

The current predictor is obtained from the old prior and these M blocks by the stated recursion. Assume directly that the controlled transition kernel of this true augmented state is weak-Feller: integration of every bounded continuous next-state function against the kernel is continuous in the current augmented state and prescription.

For a prior p and prescription a, let

c_K(p,a)=E_p^a[sum_{r=0}^{K-1} beta^r c(x_r,u_r)],

where the expectation uses the observation channels, prescription maps, and plant transitions just specified. Define C=||c_K||_infinity=sup_{p,a}|c_K(p,a)| and b=beta^K.

Fix a substitute old prior nu in P(X). At every boundary, the substitute state is hat Z_q*=(nu,I_q^M). Its current predictor pi_q* is obtained by applying the M retained blocks to nu. Its block cost is c_K(pi_q*,a_q), its next joint block is generated from pi_q* using the same observation channels and prescription, its window is shifted and appended, and its old-prior coordinate is reset to nu. Throughout, consider only initializations for which pi_(q-M)<<nu almost surely at every q>=0 under every admissible stationary Markov policy of the true augmented-state model. This is a standing requirement covering all policies in each stability supremum, not an eligibility restriction removing individual policies. In all comparisons, both predictor recursions are evaluated on the same true retained record and realized actions, not on independently generated records.

Let J(z) be the optimal true expected discounted future cost starting from z, and J_M*(z*) the corresponding substitute optimum, using discount b and block cost c_K. For any optimal stationary substitute policy gamma_M*, its application in the true model chooses gamma_M*(nu,I_q^M), without access to the true old or current predictor. Denote its true cost by J^{gamma_M*}(z).

## Initialization and Stability Sequences

For a deterministic paired initialization z=(p,I_0^M), z*=(nu,I_0^M) satisfying the standing domination requirement, hold that initialization fixed and define

L_q^M(z)=sup_gamma E_z^gamma ||pi_q-pi_q*||_TV,

where gamma ranges over all admissible stationary Markov policies of the true augmented-state model.

For a generated initialization, the true model is run from time -MK under an admissible prehistory policy and known initial law. At time zero the agents have the generated retained window and their respective old priors. Write Lambda for the resulting paired initialization law and define

bar L_q^M=sup_{Lambda,gamma} E_{Lambda,true}^gamma ||pi_q-pi_q*||_TV.

The supremum is over admissible generated initialization laws satisfying the standing domination requirement and all admissible stationary Markov true augmented-state policies. This expectation includes the sampling of the retained initial window. Conditional and generated-initialization stability sequences must not be interchanged.

## Task

Prove, for each deterministic paired initialization under consideration,

|J(z)-J_M*(z*)| <= C/(1-beta) sum_{q>=0} b^q L_q^M(z),

and, for any optimal stationary substitute policy applied as specified,

J^{gamma_M*}(z)-J(z) <= 2C/(1-beta) sum_{q>=0} b^q L_q^M(z).

Also prove the corresponding generated-initialization bounds

|E_Lambda J(hat Z_0)-E_Lambda J_M*(hat Z_0*)| <= C/(1-beta) sum_{q>=0} b^q bar L_q^M,

E_Lambda[J^{gamma_M*}(hat Z_0)-J(hat Z_0)] <= 2C/(1-beta) sum_{q>=0} b^q bar L_q^M.

When the applicable sequence tends to zero as M tends to infinity for each fixed q, conclude the corresponding value and policy near-optimality.

For the additional stability assertion, retain the following extra assumptions: Y is finite; Q(y|x)>=epsilon for every x,y and some epsilon>0; and there exist a nonzero finite measure lambda on X and constants epsilon_u>0, one for each joint action u, such that for every Borel A and x,

epsilon_u lambda(A)<=T(A|x,u)<=epsilon_u^{-1}lambda(A).

For a kernel H define its overlap coefficient by

delta(H)=1-(1/2) sup_{x,x'} ||H(.|x)-H(.|x')||_TV.

Let delta(Q) refer to the state-only joint observation channel, let T^u(.|x)=T(.|x,u), and let underlinedelta_T=inf_{u in U} delta(T^u).

Prove that rho=(2-delta(Q))(1-underlinedelta_T)<1 implies geometric expected total-variation stability of the two predictor recursions under the true observation law, uniformly over admissible policies, first for one-step sharing and then for K-periodic sharing. Deduce decay of bar L_q^M for generated M-block windows, and hence the generated-initialization near-optimality conclusions. No uniform conditional stability assertion for every fixed retained-window realization is requested.
