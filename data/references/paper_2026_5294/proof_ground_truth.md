# Reference Proof

## Proof Structure

For the accumulated action, first use the placement-error condition to compare its endpoint with the logged later position. Transfer the value from that later position by Lipschitz continuity, then apply the assumed margin and the triangle inequality.

## Complete Proof

Let
\[
y=F(x_i,u,W),\qquad S=\sum_{k=i}^{j-1}\|b_k\|.
\]
The placement-error property applied to the segment gives
\[
\|y-x_j\|\le c_F S.
\]
Consequently, by the triangle inequality,
\[
\|y-g\|\le \|y-x_j\|+\|x_j-g\|
\le c_F S+\|x_j-g\|. \tag{1}
\]

Since \(J\) is \(L\)-Lipschitz in its position argument,
\[
J(y,W)\ge J(x_j,W)-L\|y-x_j\|
\ge J(x_j,W)-Lc_F S.
\]
Multiplying by the nonnegative discount factor \(\delta\) and subtracting \(J(x_i,W)\) yields
\[
\delta J(y,W)-J(x_i,W)
\ge \delta J(x_j,W)-J(x_i,W)-\delta Lc_F S.
\]
The assumed margin implies that the right-hand side is at least
\[
\|x_j-g\|+(\delta L+1)c_F S-\delta Lc_F S
=\|x_j-g\|+c_F S.
\]
Combining this with (1) proves
\[
\delta J(F(x_i,u,W),W)-J(x_i,W)\ge \|F(x_i,u,W)-g\|.
\]
Thus \(u\) is a \(\mu\)-shortcut at \((x_i,W)\), as required.
