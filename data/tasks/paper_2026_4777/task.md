# Problem

## Setup

Fix an integer N>=1, a vector x=(x_1,...,x_N) in R^N, and epsilon>0. Let D be the one-dimensional first-difference operator, (D sigma)_n=sigma_{n+1}-sigma_n for n=1,...,N-1, and let ||D sigma||_1 be the sum of absolute differences (zero when N=1).

For tau in R define the extended-valued function

f_e(x,tau)=((|x|/epsilon+1)^2)/(2 tau)+(1/2)log tau-1/2 for tau>=1,

and f_e(x,tau)=+infinity for tau<1. For alpha>=0 define

Psi_{alpha,epsilon}(x)=min_{sigma in R^N: ||D sigma||_1<=alpha} sum_{n=1}^N f_e(x_n,sigma_n).

## Task

Prove that

1. lim_{alpha->infinity} Psi_{alpha,epsilon}(x)=sum_{n=1}^N log(|x_n|/epsilon+1), and
2. lim_{alpha->0+} Psi_{alpha,epsilon}(x)=Psi_{0,epsilon}(x)=N log sqrt((1/N) sum_{n=1}^N (|x_n|/epsilon+1)^2).

Thus the variational penalty has the elementwise log-sum form at an unbounded TV budget and converges to the logarithmic global l2 form as the TV budget decreases to zero.
