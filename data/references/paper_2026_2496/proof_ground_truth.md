# Reference Proof

Let the signs be independent Rademacher variables and let each X_t be a function of earlier signs. All constructions below are such finite trees, so their covariates are bounded over the fixed horizon.

## Scalar upper bound

In dimension one, S_t=0 whenever V_t=0. Fix 0<c<=1/4 and put C=exp(c/(1-2c)). If V_t+X_{t+1}^2=0, then R_t=R_{t+1}=0 and the claimed one-step inequality is immediate. Otherwise set u=V_t/(V_t+X_{t+1}^2). When V_t=0, interpret uR_t as zero; no division by V_t is needed. Conditional on the past, Hoeffding's lemma for Y_{t+1} gives

E[exp(cR_{t+1})|F_t] <= exp(cuR_t+c(1-u)+2c^2R_tu(1-u))
                         <= exp(cuR_t+c(1-u)+2c^2R_t(1-u)).

If R_t<=1/(1-2c), the last exponent is at most c/(1-2c): its coefficient of u is c((1-2c)R_t-1)<=0. If R_t>1/(1-2c), that exponent is at most cR_t, because the difference is c(1-u)(1-(1-2c)R_t)<=0. Thus E[exp(cR_{t+1})|F_t]<=exp(cR_t)+C. Separately, R_1 is zero if X_1=0 and one otherwise, so E[exp(cR_1)]<=exp(c)<=C. Iterating from t=1, including T=1, proves E[exp(cR_T)]<=TC. Jensen gives E[R_T]<=(log T)/c+1/(1-2c). At c=1/4 this is O(log T) for T>=10.

## Scalar lower bound

For T>=10 let n=floor((log_2 T)/2), K=floor(T/n), and M=2T/n. Use complete blocks j=0,...,K-1, each of length n. Set X_t=M^j throughout block j if every earlier complete block contains a negative sign; otherwise set X_t=0. This defines X_1=1. On the remaining fewer than n rounds, use X_t=M^K if every complete block contains a negative sign, and zero otherwise. Each choice depends only on previous signs.

Let i be the first all-positive complete block, if there is one. On {0<=i<K}, every later covariate is zero, the contribution of block i to S_T is nM^i, and the earlier contributions have absolute sum at most TM^{i-1} (zero when i=0). Also V_T<=nM^{2i}/(1-M^{-1})<=2nM^{2i}. Since T/M=n/2, R_T>=n/8 on this event. The K disjoint complete blocks are independently all-positive with probability 2^{-n}, so P(i exists)=1-(1-2^{-n})^K>=1-exp(-K2^{-n}), bounded below by an absolute positive constant for T>=10. Finally n is bounded below by an absolute positive multiple of log T. This proves E[R_T]>=a log T for an absolute a>0.

## Higher dimensions and regret

For d>=2, start at S_0=V_0=0 and set A_t=V_t+I_d. Given the past, select a unit vector e_t orthogonal to A_t^{-1/2}S_t and put X_{t+1}=rA_t^{1/2}e_t. A fixed deterministic selection rule makes e_t measurable; on a finite sign tree there are no selection or boundedness difficulties. With q_t=S_t^T A_t^{-1}S_t, Sherman-Morrison and e_t^T A_t^{-1/2}S_t=0 give, pathwise,

q_{t+1}-q_t=r^2/(1+r^2).

Indeed X_{t+1}^T A_t^{-1}X_{t+1}=r^2, X_{t+1}^T A_t^{-1}S_t=0, and the latter orthogonality also removes the sign-dependent cross term. Consequently q_T=Tr^2/(1+r^2). Since S_T lies in range(V_T), the spectral decomposition of V_T gives S_T^T V_T^dagger S_T>=S_T^T(V_T+I_d)^{-1}S_T=q_T. Choose r^2=(1-epsilon^2)/epsilon^2. Conversely, writing B=[X_1 ... X_T] and Y=(Y_1,...,Y_T)^T gives R_T=Y^T B^T(BB^T)^dagger BY. The middle matrix is an orthogonal projector, so 0<=R_T<=||Y||^2=T.

For the regret consequence, use this same covariate tree as an environment, reveal x_t=X_t before the learner predicts, and reveal y_t=Y_t afterward. The sign is independent of the covariate and of the learner's information when predicting. Conditional expected learner loss on round t is hat y_t^2+1>=1, including for randomized learners. Completing the square in the comparator gives, on every realization,

sum_t y_t^2-inf_{theta in R^d} sum_t(<theta,x_t>-y_t)^2=S_T^T V_T^dagger S_T.

Hence every learner's expected regret is at least E[R_T]>=(1-epsilon^2)T. There are finitely many nodes in the constructed tree; multiplying every covariate by one common positive constant makes ||x_t||<=1 without changing R_T or the comparator infimum. The same bounded environment therefore works for every learner. This proves the stated impossibility of a sublinear uniform regret bound.
