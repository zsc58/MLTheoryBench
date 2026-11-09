# Reference Proof

## Proof Structure

1. Obtain a closed recurrent non-goal class from an improper policy. Derive the reachability direction by finite-horizon optimization, and choose a direction-greedy policy that preserves this class.
2. Show that the selected action maximizes both the parameter vector and the direction. Deduce preservation of the greedy region, invariance of every Bellman residual, and invariance of the likelihood.
3. Construct a full-dimensional cube in the greedy region and infinitely many disjoint translates with the same positive likelihood minimum.
4. For any proper policy, prove invertibility of its state-action residual matrix by absorption, and integrate the resulting complete-data Gaussian by an affine change of variables.

## Complete Proof

Write I={(s,a):s!=s^g, a in A_s}, so d=|I|. The assumed improper policy implies d>0.

### 1. Reachability and the improper policy

We use the finite-state Markov-chain fact that an improper stationary policy in a chain with an absorbing goal has a closed communicating recurrent class excluding the goal. In a finite communicating recurrent class, every state is reached almost surely from every other state in the class. These facts apply because the state space is finite and the policy is deterministic and stationary.

Choose an improper deterministic stationary policy nu, a closed communicating recurrent class C not containing s^g, and s^r in C.

First allow hitting s^r at time zero. Let h_n(s) be the largest probability of hitting s^r by time n, starting at s, over deterministic time-dependent Markov policies. Set h_0(s)=1 if s=s^r and h_0(s)=0 otherwise. Backward induction gives h_n(s^r)=1, h_n(s^g)=0, and, for s different from these two states,

h_{n+1}(s)=max_{a in A_s} sum_{s'} p(s'|s,a) h_n(s').

For each finite horizon, a single sequence of decision rules attains these values simultaneously from all starting states: at each backward step select a maximizing action separately at each state. Thus this recurrence does not interchange a supremum with a sum without justification.

The sequence h_n increases and is bounded by one. Let h(s)=lim_n h_n(s). For any policy, the probability of ever hitting s^r is the limit of its finite-horizon hitting probabilities and is at most h(s). Conversely, finite-horizon optimizers have eventual hitting probabilities at least h_n(s). Hence h(s) is the supremum eventual hitting probability. Finiteness of each action set allows passage to the limit in the recurrence, giving

h(s)=max_{a in A_s} sum_{s'}p(s'|s,a)h(s')

when s is neither s^r nor s^g. Following nu inside C reaches s^r almost surely, so h=1 throughout C. In particular nu(s^r) has all its successors in C, and therefore the same displayed identity holds at s^r. It also holds at the absorbing goal, where h=0.

For every (s,a) in I, define

u_dir(s,a)=sum_{s'}p(s'|s,a)h(s'),

and write u_{s,a}=u_dir(s,a). Then 0<=u_{s,a}<=1 and

max_{a in A_s}u_{s,a}=h(s),

with zero goal contribution. Moreover, u_{s,a} is the supremum probability of visiting s^r at some strictly positive time after fixing the initial pair (s,a). Indeed, conditioning on the first state gives the upper bound sum p h. For the reverse bound, use a simultaneous n-step optimizer after the first transition; this achieves sum p h_n, which increases to sum p h. A first transition directly to s^r already counts as a hit.

For completeness, the supremum is a maximum, as in the source definition. Let T be the first hitting time of s^r, allowing T=0. For 0<beta<1, maximize E[beta^T 1_{T<infinity}]. On states other than s^r and s^g, its finite-horizon recurrence has operator f -> beta max_a sum p f, with boundary values 1 at s^r and 0 at s^g. The sup-norm distance between two successive iterates contracts by at most beta, so the iterates converge uniformly to a unique fixed point v_beta. Choosing a maximizing action at each state produces a deterministic stationary policy psi_beta. Iterating its fixed-point equation shows that its discounted hitting expectation equals v_beta: the unaccounted remainder after n steps is bounded by beta^n. For every n,

beta^n h_n(s)<=v_beta(s)<=h(s).

Consequently v_beta(s) tends to h(s) as beta increases to one. There are finitely many deterministic stationary policies, so along a sequence beta increasing to one a single psi occurs infinitely often. Its undiscounted hitting probability is at least v_beta along that subsequence and at most h, and therefore equals h simultaneously at every state. Following this psi after the prescribed initial action attains u_{s,a}. This attainment argument is not needed for the later algebra, but closes the maximum in the source's reachability definition.

Choose phi(s) in argmax_{a in A_s}u_{s,a}, requiring phi(s)=nu(s) for s in C. This is possible because nu stays in C, h=1 on C, and hence u_{s,nu(s)}=1 there. At the goal use its unique action. The policy phi preserves C and agrees with nu there. Thus s^r is recurrent under phi, phi is improper, and u_{s^r,phi(s^r)}=1. In particular u is nonzero.

Finally, combining the definition of u with max_a u_{s,a}=h(s) gives, for every non-goal admissible pair,

u_dir(s,a)=sum_{s'!=s^g}p(s'|s,a) max_{b in A_{s'}}u_{s',b}.

All choices so far depend only on the MDP and the selected recurrent class, not on theta, epsilon, or the dataset.

### 2. Translation invariance

Let theta in O^phi and c>=0. For every non-goal s and a in A_s,

(theta_{s,phi(s)}+c u_{s,phi(s)})-(theta_{s,a}+c u_{s,a})
=(theta_{s,phi(s)}-theta_{s,a})+c(u_{s,phi(s)}-u_{s,a})>=0.

Thus theta+cu belongs to O^phi, including at ties, and

max_{a in A_s}(theta_{s,a}+c u_{s,a})
=max_{a in A_s}theta_{s,a}+c max_{a in A_s}u_{s,a}.

Substituting this identity and the identity for u into the definition of g gives

g_{s,a}(theta+cu)-g_{s,a}(theta)
=c[u_{s,a}-sum_{s'!=s^g}p(s'|s,a)max_{b in A_{s'}}u_{s',b}]=0.

Every observation factor is therefore unchanged. Multiplying proves the likelihood identity for every finite observation list and every epsilon>0. Repeated observations cause no difficulty, and the empty product is identically one.

### 3. Infinite mass

Fix epsilon>0 and a finite dataset D. Define theta_bar by assigning value 1 to each selected coordinate (s,phi(s)) and value 0 to every competing coordinate. Choose 0<delta<1/2 and let

K=theta_bar+[-delta,delta]^d.

For every competing action the selected-minus-competing gap on K is at least 1-2delta>0. A state with only one admissible action imposes no comparison. Hence K is contained in O^phi, has volume (2delta)^d>0, and this construction also works when every state has only one admissible action.

The likelihood is a positive continuous function on R^d: finite maxima are continuous and every Gaussian factor has positive finite scale and a real argument. Its minimum m on the compact cube K is therefore strictly positive. For empty D, m=1.

For k=0,1,2,... set K_k=K+3k delta u. Section 2 shows that K_k is contained in O^phi and that its likelihood minimum is m. The coordinate indexed by (s^r,phi(s^r)) has u-coordinate 1. Its interval on K_k has length 2delta and its centers for consecutive k differ by 3delta. Thus the cubes K_k are pairwise disjoint.

For every integer J>=0, translation invariance of Lebesgue measure gives

integral_{O^phi} L_hat_epsilon(theta|D) dtheta
>=sum_{k=0}^J integral_{K_k} L_hat_epsilon(theta|D) dtheta
>=(J+1)m(2delta)^d.

Letting J increase proves divergence. The positive lower bound may depend on epsilon and D; no uniform lower bound in either is claimed or needed.

### 4. Finite mass for a proper policy

Let mu be any proper deterministic stationary policy. If no such policy exists, this universally quantified conclusion has no instance to prove.

Define the d by d substochastic matrix P_mu by

(P_mu)_{(s,a),(t,b)}=p(t|s,a) 1_{b=mu(t)},

for non-goal admissible pairs (s,a) and (t,b), and let B_mu=I-P_mu. On O^mu, the vector of g-values is B_mu theta, so the complete-data likelihood is

(2pi epsilon^2)^(-d/2) exp(-||B_mu theta-rbar||_2^2/(2epsilon^2)),

where rbar is the vector of the finite expected rewards indexed by I.

Suppose B_mu v=0. Then v=P_mu^n v for every n. By induction, (P_mu^n v)_{s,a} is the expectation of v_{S_n,mu(S_n)} on the event S_n!=s^g when the first action is fixed to a and subsequent actions follow mu. Therefore

|(P_mu^n v)_{s,a}|<=||v||_infinity P(S_n!=s^g|S_0=s,A_0=a, thereafter mu).

The probability on the right tends to zero: condition on the first successor state and use properness from each of the finitely many successors. It follows that v=0. Thus B_mu is invertible and B_mu^T B_mu is positive definite.

Use y=B_mu theta-rbar in the full-space Gaussian integral. The integral over O^mu is bounded above by

(2pi epsilon^2)^(-d/2)|det B_mu|^(-1)
 times integral_{R^d} exp(-||y||_2^2/(2epsilon^2)) dy
=|det B_mu|^(-1)<infinity.

This proves the proper-policy conclusion for every epsilon>0. No existence of a proper policy and no condition on improper-policy reward returns was used in the other parts of the proof.

## Obligation Closure

The recurrent-class input is the standard finite-state recurrence fact indexed by theory_020 and used in theory_014. Reachability, its boundary condition and attainment, the policy selection, every residual identity, the positive-volume disjointness argument, absorption after an arbitrary initial action, and Gaussian integrability have all been explicitly derived. The grouped theory_009 is used only for its Lemma 5 argument, reproduced in Section 4; its other results are not dependencies of this proof. There are no unresolved theorem-critical obligations.
