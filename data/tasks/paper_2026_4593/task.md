# Problem

## Game and regret

Let H and K be positive integers. Consider a finite episodic two-player zero-sum Markov game with disjoint nonempty state layers S_1,...,S_(H+1), where S_(H+1) contains a single terminal state. Write S for their union. At step h the learner and opponent have nonempty finite action sets A_h and B_h; write A and B for their unions. The unknown transition law is P_h:S_h×A_h×B_h→Delta(S_(h+1)), and the reward function is r_h:S_h×A_h×B_h→[0,1]. Here Delta(X) denotes the probability distributions on a finite set X.

In episode k, the initial state s_1^k is chosen adversarially without access to future random draws. The players use Markov policies mu^k and nu^k, fixed before play in that episode and not changed during it. The learner's policy may depend on previous episodes. The opponent's full policy sequence (nu^1,...,nu^K) is fixed in advance. Conditional on the current state, the players independently draw their actions from their committed distributions, receive reward r_h^k=r_h(s_h^k,a_h^k,b_h^k), and draw the next state from P_h. The learner observes states, its own actions, rewards, and successor states, but neither opponent actions nor opponent policies.

For a policy pair, V_h^(mu,nu)(s) is its expected total reward from step h through H starting at s. Set V_(H+1)^(mu,nu)=0. Define

P_h f(s,a,b)=sum_(s')P_h(s'|s,a,b)f(s'),

D_(p,q)[Q](s)=sum_(a,b)p(a)q(b)Q(s,a,b).

Thus Q_h^(mu,nu)=r_h+P_h V_(h+1)^(mu,nu) and V_h^(mu,nu)(s)=D_(mu_h(s),nu_h(s))[Q_h^(mu,nu)](s).

Each nu_h^k(s) is defined for every s in S_h, whether or not that state is visited. These distributions are used only to define the benchmark and are not revealed to the learner. Recursively set V_(H+1)^*=0 and

V_h^*(s)=max_(p in Delta(A_h)) min_(q in {nu_h^k(s):1<=k<=K}) D_(p,q)[r_h+P_h V_(h+1)^*](s).

Define

Enr_K=sum_(k=1)^K(V_1^*(s_1^k)-V_1^(mu^k,nu^k)(s_1^k)).

For each h,s, fix a minimizer

nu_h^*(s) in argmin_(q in Conv{nu_h^1(s),...,nu_h^K(s)}) max_(p in Delta(A_h)) D_(p,q)[r_h+P_h V_(h+1)^*](s).

The choice of minimizer is fixed independently of the sampled trajectories. For distributions p,q on the same finite set, let TV(p,q)=(1/2)sum_x|p(x)-q(x)|. Put

C=sum_(h=1)^H sum_(k=1)^K TV(nu_h^k(s_h^k),nu_h^*(s_h^k)),

L=1+sum_(k=1)^(K-1)1{nu^k!=nu^(k+1)},

where policy inequality means inequality at some step and state.

## Bandit module and confidence parameter

The learner uses a fixed supplied bandit module, instantiated by one-half-Tsallis FTRL with implicit exploration and doubling, through the following interface and assumed guarantee. A fresh module on m actions starts with the uniform distribution. At observation i it has a distribution p_i determined by its past feedback, draws a_i from p_i, observes only Y_i in [0,1], and produces the next distribution.

For every nonanticipating environment with predictable conditional-mean reward vector g_i in [0,1]^m satisfying E[Y_i|past,a_i]=g_i(a_i), and every confidence rho in (0,1), assume

P(for every 1<=n<=K: max_(p in Delta([m])) sum_(i=1)^n [<p,g_i>-<p_i,g_i>] <= c sqrt(m n log(m/rho))) >= 1-rho,

where c is a fixed universal constant. The vectors g_i may depend on earlier observations but not on the current action draw. The guarantee applies conditionally when a fresh module is started after a random past history.

For delta in (0,1), use a common confidence parameter

iota=a_0 H^2|A| log(8HK^8|A||S|/delta),

where a_0 is a sufficiently large universal constant, chosen in relation to c. Each fresh base instance has confidence allocation epsilon=delta/(2K^6); each of its fresh state-epoch bandit modules uses rho=epsilon/(4H|S|(K+1)). Set beta_n=sqrt(iota/n) for positive integers n. Let c_0>=2 be a sufficiently large fixed universal constant. Neither a_0 nor c_0 depends on the game, H, K, delta, C, or L.

## Base learner

A fresh base instance takes an epoch increment eta>0. It maintains separate epochs for each h,s. Initially V_h(s)=H-h+1, V_(H+1)=0, the previous epoch length is N_0(h,s)=1, and the current epoch has count zero. Each state has a fresh bandit module and its current action distribution is uniform.

At the start of each episode, freeze all value tables and action distributions for that episode. Their entries are denoted V_h^k(s) and mu_h^k(s). At the visit to s=s_h^k, draw the learner's action from mu_h^k(s), observe r_h^k and s_(h+1)^k, append the sample

r_h^k+V_(h+1)^k(s_(h+1)^k)

to that state's current epoch, and increment its visit count n. The target length for epoch tau is ceil((1+eta)N_(tau-1)(h,s)).

If n reaches this target, record N_tau(h,s)=n and, for the next episode, replace that state's estimate by

min{H-h+1, (1/n)sum_(j in the completed epoch)(r_h^j+V_(h+1)^j(s_(h+1)^j))+beta_n}.

Start the next epoch with count zero and a fresh uniform bandit module. Otherwise, leave the value estimate unchanged and update the current bandit module with the played action and feedback (r_h^k+V_(h+1)^k(s_(h+1)^k))/H; use its output distribution in the next episode. At states not visited, retain the estimates and distributions. All updates take effect only in the next episode. An unfinished epoch need not produce a value update.

## Restart learner

Starting at block b=1, run at most 4^b+1 consecutive sub-blocks. Each sub-block uses a fresh base instance with the confidence allocation above. Its increment is

eta=1/H for sub-blocks ell<=4^b,

eta=max{4^(-b)/H,|S|/K} for sub-block ell=4^b+1.

At the start of a sub-block set T=emptyset, Phi=0, and D=0. While Phi<=D and fewer than K total episodes have been played, play one episode using this base instance, add its index to T, and update

Phi=sum_(k in T)(V_1^k(s_1^k)-sum_(h=1)^H r_h^k)+sqrt(iota|T|).

For ell<=4^b set

D=3c_0 H sqrt(iota|S||T|log(K)/eta).

For ell=4^b+1 set

D=4c_0 H sqrt(iota|S|K log(K)/eta).

If Phi>D, move to the next sub-block, or to block b+1 after its final sub-block. Stop the entire procedure immediately after K episodes. The logarithm is the natural logarithm, including log(1)=0. The specified schedule is used also for small K; no additional lower bound on the increments of ordinary sub-blocks is imposed.

## Task

Prove that universal choices of a_0 and c_0 as above give, for every delta in (0,1), with probability at least 1-delta,

Enr_K <= tilde O(H^2|S| + min{sqrt(H^3 iota|S|K log K) + (iota H^5|S|KC log K)^(1/3), sqrt((L+log K)H^3 iota|S|K log^2 K)}).

The hidden factors are universal logarithmic factors in H, K, |S|, |A|, and 1/delta, with no hidden polynomial dependence on these parameters, C, or L. Both alternatives must hold on the same probability event, so the conclusion uses their minimum.
