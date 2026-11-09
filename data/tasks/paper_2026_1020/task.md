# Problem

## Setup

There are K possible labels and exchangeable observations (X_1,Y_1), ..., (X_{n+1},Y_{n+1}). Randomly split the first n observations into a training set D_tr and a calibration set D_cal of size m >= 1. Using only D_tr, fit an encoder phi and one prototype hypervector h^y for each label y in {1,...,K}. Let delta be a nonnegative similarity function and define, for every evaluated x,y,

s(x,y) = -[delta(phi(x),h^y) / sum_{j=1}^K delta(phi(x),h^j)] delta(phi(x),h^y),

with the displayed score assumed well-defined. Smaller scores indicate greater conformity. For each calibration point set S_i = s(X_i,Y_i). For alpha in (0,1), let k = ceil((1-alpha)(m+1)); define Q as the kth smallest value among S_1,...,S_m when k <= m, and Q = +infinity when k > m. For a new x, output

C_alpha(x) = { y in {1,...,K} : s(x,y) <= Q }.

## Task

Prove that

P{Y_{n+1} in C_alpha(X_{n+1})} >= 1-alpha.

Moreover, if the m+1 scores consisting of the calibration scores and the true test score are almost surely pairwise distinct, prove

P{Y_{n+1} in C_alpha(X_{n+1})} <= 1-alpha + 1/(m+1).

The probability is over the exchangeable data and the random split.
