# Problem

## Setup

Let C>=2, d>=1, and n>=1 be integers. Fix examples (x_i,y_i), with x_i in R^d and y_i in {1,...,C}, for i=1,...,n. Assume every class is represented by at least one example. Write e_c for the c-th standard basis vector of R^C. A parameter is a matrix W in R^{C x d}, and its empirical cross-entropy loss is

L(W)=(1/n) sum_{i=1}^n log(sum_{c=1}^C exp(e_c^T W x_i-e_{y_i}^T W x_i)).

Assume the data are separable: some W satisfies (e_{y_i}-e_c)^T W x_i>0 for every i and every c!=y_i. Fix R>0 such that max_i ||x_i||_1<=R.

Let ||.|| be either an entrywise p-norm or a Schatten p-norm, with 1<=p<=infinity, using the usual maximum-entry and largest-singular-value conventions at p=infinity. The matrix inner product is <A,B>=tr(A^T B), and ||G||_*=max_{||V||<=1}<G,V> is the dual norm. Define

gamma=max_{||W||<=1} min_{i,c!=y_i}(e_{y_i}-e_c)^T W x_i.

Let b and m be positive integers with n=mb. At the beginning of each epoch, draw a fresh uniform random permutation of the n example indices, independently of the previous epochs, and divide it into m consecutive batches of size b. Process those batches in order. At iteration t, let B_t be the current batch and let

G_t=(1/b) sum_{i in B_t} grad_W log(sum_{c=1}^C exp(e_c^T W_t x_i-e_{y_i}^T W_t x_i)).

For a matrix G, let phi_{||.||}(G) be any maximizer of <G,V> over ||V||<=1. Starting from W_0 in R^{C x d}, the no-momentum update is

W_{t+1}=W_t-eta_t phi_{||.||}(G_t),  t=0,1,2,... .

For part (a), W_0 is arbitrary and the fixed stepsize sequence consists of positive real numbers, is nonincreasing, satisfies eta_t ->0, and satisfies sum_{t=0}^infinity eta_t=infinity. Part (b) instead permits any sequence of positive real stepsizes. In part (b), batch-one SignSGD means the update with phi(G)=sign(G) applied entrywise, with sign(0)=0.

## Task

Prove the following integrated theorem.

(a) If rho:=gamma-4(m-1)R>0, then there is an integer t_2>=1 such that W_t!=0 for every t>t_2 and

rho - [min_{i,c!=y_i}(e_{y_i}-e_c)^T W_t x_i]/||W_t||

= O((sum_{s=0}^{t_2-1}eta_s + sum_{s=t_2}^{t-1}eta_s^2 + sum_{s=t_2}^{t-1}eta_s exp[-(rho/4) sum_{tau=t_2}^{s-1}eta_tau]) / sum_{s=0}^{t-1}eta_s).

The estimate holds for every reshuffling realization and every permitted choice of maximizing directions. The threshold and the implicit constant may depend on the fixed data, norm, R, initialization, and stepsize schedule, but not on t. Empty sums are zero. Moreover, gamma<=2R, so the condition rho>0 forces m=1; thus this worst-case guarantee is necessarily a full-batch guarantee.

(b) For every 0<epsilon<1, consider C=2, d=2, n=2, b=1, x_1=(1,-epsilon), y_1=1, and x_2=(epsilon,-1), y_2=2. This dataset is separable, but batch-one SignSGD started at W_0=0 never strictly correctly classifies both examples for any positive stepsizes and any reshuffling realization. Here strict correct classification means that the correct-class logit is strictly larger than every incorrect-class logit. Consequently L(W_t)>=log(2)/2 for all t, so the loss does not converge to zero.
