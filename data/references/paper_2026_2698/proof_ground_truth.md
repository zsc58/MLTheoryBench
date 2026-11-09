# Reference Proof

## Proof Structure

First prove the strict-local bias bound by comparing two global states that agree on a block but may induce different true updates there. Then prove the overlapping-read averaging identity coordinatewise using unique core ownership and halo sufficiency, and derive fixed-point equivalence by elementary algebra.

## Complete Proof

For the strict operator, fix a block index i and u in R^{|D_i|}. Let
E_i(u) = sup_{x:x_{D_i}=u} ||(T^hard(x)-bar F(x))_{D_i}||_c.
If E_i(u)=+infinity, the desired inequality is immediate. Otherwise, take any x,x' with x_{D_i}=x'_{D_i}=u. By strictness, both block outputs equal the same value G_i(u). Hence, by the triangle inequality,

|| (bar F(x))_{D_i} - (bar F(x'))_{D_i} ||_c
<= ||(bar F(x))_{D_i}-G_i(u)||_c + ||G_i(u)-(bar F(x'))_{D_i}||_c.

Each term on the right is bounded by E_i(u), so the left side is at most 2E_i(u). Taking the supremum over all such x,x' gives Delta_i(u) <= 2E_i(u), and therefore E_i(u) >= Delta_i(u)/2.

Now consider a compatible overlapping-read decomposition. For each i, the halo-sufficiency condition implies that the local map T_i is well-defined and satisfies
T_i(x_{S_i}) = (bar F(x))_{D_i}
for every x. Define the lift by
(tilde T_i(x))_{D_i}=T_i(x_{S_i}) and (tilde T_i(x))_{[d]\\D_i}=x_{[d]\\D_i}.
Fix a coordinate j. Since the cores form a disjoint partition, there is a unique index i(j) with j in D_{i(j)}. Compatibility gives
(tilde T_{i(j)}(x))_j=(bar F(x))_j,
while for every i != i(j), j is outside D_i and therefore (tilde T_i(x))_j=x_j. Consequently,
[(1/m) sum_i tilde T_i(x)]_j = (1/m)(bar F(x))_j + ((m-1)/m)x_j.
This holds for every coordinate, so
(1/m) sum_i tilde T_i(x) = (1-1/m)x + (1/m)bar F(x).
Finally, x is a fixed point of the averaged operator iff
x=(1-1/m)x+(1/m)bar F(x).
Multiplying by m and cancelling (m-1)x yields x=bar F(x), and the reverse implication is immediate. Thus the fixed-point sets coincide exactly.
