# Problem

## Setup

Let K>=2 be an integer. For each arm i, fix an online reward distribution P_i^on and an offline reward distribution P_i^off, both supported on [0,1], with means mu_i^on and mu_i^off. Online rewards are independent draws from the corresponding arm's online distribution. Before online play, arm i has a fixed number N_i>=0 of offline observations X_{i,1},...,X_{i,N_i}, drawn independently from P_i^off. The N_i are integers, and all offline observations and online reward draws are mutually independent.

The learner receives the offline observations before the first round. At each online round it selects an arm before observing that round's reward and observes only the reward of the selected arm. The reward distributions and their means are unknown to the learner. Known finite numbers V_i>=0 satisfy |mu_i^off-mu_i^on|<=V_i. For analysis, label the unique online-optimal arm as arm 1, and define Delta_i=mu_1^on-mu_i^on>0 for i!=1.

Let T_i(t) be the number of pulls of arm i before round t and let n_i(t)=T_i(t)+N_i. Define hat-mu_i^on(t) to be the average of the observed online rewards from arm i when T_i(t)>0, and set hat-mu_i^on(t)=0 when T_i(t)=0. Define hat-mu_i^hyb(t) to be the average of all N_i offline observations and all T_i(t) observed online rewards from arm i when n_i(t)>0, and set hat-mu_i^hyb(t)=0 when n_i(t)=0. Put

b_i(t)=N_i V_i/n_i(t) if n_i(t)>0, and b_i(t)=0 if n_i(t)=0.

Consider the following policy, starting with T_i(1)=0. At round t, conditional on the available history, it draws 2K fresh, mutually independent Gaussian random variables with laws

 theta_i^on(t) ~ Normal(hat-mu_i^on(t), 1/(T_i(t)+1)),

 theta_i^hyb(t) ~ Normal(hat-mu_i^hyb(t)+b_i(t), 1/(n_i(t)+1)).

Here the second argument of Normal is its variance. The sampling randomness is independent of the reward-generation randomness. Set

 hat-theta_i(t)=median{hat-mu_i^on(t),theta_i^on(t),theta_i^hyb(t)}.

Select an arm A(t) maximizing hat-theta_i(t), resolving ties by any fixed ordering of the arms, and update the counts and empirical means using the observed reward.

For an integer horizon T>=1, define

 Reg(T)=sum_{i!=1} Delta_i E[sum_{t=1}^T 1{A(t)=i}],

where expectation includes the offline observations, online rewards, and policy randomness.

## Task

Prove that there are universal constants C,C_1,C_2,C_3>0, independent of the reward distributions, K, T, the sample sizes, and the shift bounds, such that for every admissible instance and every integer horizon T>=1,

Reg(T) <= C sum_{i!=1} Delta_i( [C_1 log(T Delta_i^2+e^6)/Delta_i^2 - N_i(1-3 omega_i/Delta_i)_+]_+
 + [C_2 log(T Delta_i^2+e^6)/Delta_i^2 - N_1]_+ + C_3/Delta_i^2 ),

where omega_i=V_i+mu_i^off-mu_i^on, (z)_+=max{z,0}, and log denotes the natural logarithm.

In particular, deduce the online-only order O(sum_{i!=1} log(T Delta_i^2+e^6)/Delta_i), while retaining the displayed reductions attributable to offline samples of arm i and arm 1.
