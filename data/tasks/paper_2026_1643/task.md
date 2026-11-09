# Problem

## Setup

Let m and n_1,...,n_m be fixed positive integers. There are m candidate configurations, indexed by k=1,...,m. Configuration k has n_k iid real-valued observations X_{k,1},...,X_{k,n_k} with unknown fixed CDF F_k; observations from different configurations may be arbitrarily dependent. Write D=((X_{k,i})_{i=1}^{n_k})_{k=1}^m for the collection of all observations. For x in R, define

Fhat_k(x) = (1/n_k) sum_{i=1}^{n_k} 1{X_{k,i}<=x}.

A measurable data-dependent rule S applied to all observations returns a random subset A=S(D) of {1,...,m}. For each selected k, a reported band consists of functions L_k,U_k on R and its miscoverage event is O_k={there exists x in R: L_k(x)>F_k(x) or F_k(x)>U_k(x)}. Define

FCP = [1/max{|A|,1}] sum_{k in A} 1{O_k},   FCR=E[FCP],

where the expectation is under the joint distribution of all observations and delta is fixed in (0,1).

An e-calibrator is a nonincreasing upper-semicontinuous function f:[0,1]->[0,infinity] satisfying integral_0^1 f(u)du<=1. Its generalized inverse is f^{-1}(t)=sup{u in [0,1]: f(u)>=t}, with supremum 0 when the set is empty.

## Task

For any measurable selection rule S and any fixed e-calibrator f, prove the following integrated claim. On the event a=|A|>0, set q=m/(delta a), r=f^{-1}(q), and

 epsilon_k = sqrt((1/(2 n_k)) log(2/r)),
 L_k(x)=max{0,Fhat_k(x)-epsilon_k},
 U_k(x)=min{1,Fhat_k(x)+epsilon_k}

for every selected k and every x in R (if r=0, take epsilon_k=+infinity and hence L_k=0,U_k=1). Then the resulting full-data uniform bands satisfy FCR<=delta, with the empty-selection event contributing FCP=0.
