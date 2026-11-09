# Reference Proof

## Proof Structure

Reduce the signed rank-one L1 approximation problem to binary rank-one L1-NMF with 2x2 permutation blocks. One-hot factors prove the forward direction. For arbitrary nonnegative factors, paired-coordinate differences and blockwise triangle inequalities give the converse. Summing the block bounds yields the threshold shift.

## Complete Proof

### 1. Decision domains and given premises

Let `(M,D)` be a signed instance, where `s,t` are positive integers, `M in {+1,-1}^{s x t}`, and `D` is a positive integer. The public problem expressly assumes that this decision problem is NP-hard and that every yes-instance admits feasible sign vectors `u in {+1,-1}^s` and `v in {+1,-1}^t`. These are given premises, not results being proved by this reduction. Target witnesses remain arbitrary nonnegative real vectors; zero coordinates are permitted.

### 2. Construction and polynomial complexity

Define

`B(+1) = [[1,0],[0,1]]`,

`B(-1) = [[0,1],[1,0]]`.

Construct `X in {0,1}^{2s x 2t}` by placing `B(M_ij)` in rows `2i-1,2i` and columns `2j-1,2j`. Set

`T = st + D`.

The matrix has `4st` binary entries, and `T` is a positive integer. Under the conventional binary encoding of integer inputs, its bit length is `O(log(st+D+1))`, which is polynomially bounded by the input length. Computing `st`, adding `D`, and writing the matrix all take polynomial time. The mapping uses only `(M,D)`; it does not require finding source witnesses.

### 3. Forward implication

Suppose `(M,D)` is a yes-instance. By the given sign-witness premise, choose `u in {+1,-1}^s` and `v in {+1,-1}^t` satisfying `||M-uv^T||_1 <= D`.

Encode each coordinate equal to `+1` by `(1,0)^T` and each coordinate equal to `-1` by `(0,1)^T`. Concatenating these pairs produces nonnegative vectors `w in R_+^{2s}` and `h in R_+^{2t}`.

Let `E_ij` denote the component-wise L1 error in block `(i,j)`. The outer product of the two one-hot pairs has exactly one entry equal to one. If `M_ij=u_i v_j`, that entry coincides with a one of `B(M_ij)`, leaving error `1`. If `M_ij!=u_i v_j`, it occupies a zero of `B(M_ij)`, leaving error `3`. Therefore

`E_ij = 1 + |M_ij-u_i v_j|`.

Summing over the disjoint blocks gives

`||X-wh^T||_1 = st + ||M-uv^T||_1 <= st+D = T`.

Thus `(X,T)` is a yes-instance.

### 4. Block bounds for arbitrary nonnegative factors

For nonnegative real numbers `a,b,c,d`, define `u=a-b` and `v=c-d`. The errors against the two possible blocks are

`I = |1-ac| + ad + bc + |1-bd|`,

`A = ac + |1-ad| + |1-bc| + bd`.

We prove `I >= 1+|1-uv|` and `A >= 1+|1+uv|`. All uses of the triangle inequality below have the form `|r|+z >= |r+z|` with `z>=0`; this follows immediately from `|r+z| <= |r|+|z|`.

For the identity block, grouping the nonnegative terms gives

`I >= |1-ac+ad| + |1-bd+bc| = |1-av| + |1+bv|`.

If `v>=0`, then `bv>=0`, so

`I >= |1-av| + 1+bv >= 1+|1-av+bv| = 1+|1-uv|`.

If `v<0`, then `-av>=0`, so

`I >= 1-av + |1+bv| >= 1+|1+bv-av| = 1+|1-uv|`.

For the anti-identity block, grouping instead gives

`A >= |1-ad+ac| + |1-bc+bd| = |1+av| + |1-bv|`.

If `v>=0`, then `av>=0`, so

`A >= 1+av + |1-bv| >= 1+|1+av-bv| = 1+|1+uv|`.

If `v<0`, then `-bv>=0`, so

`A >= |1+av| + 1-bv >= 1+|1+av-bv| = 1+|1+uv|`.

These arguments impose no sign restriction on `u`. They also cover zero coordinates and `v=0`, the latter through the first branch. No division, boundedness assumption, or binary restriction on `a,b,c,d` is used.

### 5. Converse, equivalence, and hardness

Suppose nonnegative `w in R_+^{2s}` and `h in R_+^{2t}` satisfy `||X-wh^T||_1 <= T`. Define real vectors

`u_i = w_{2i-1}-w_{2i}`,

`v_j = h_{2j-1}-h_{2j}`.

In block `(i,j)`, apply the preceding bounds with `a=w_{2i-1}`, `b=w_{2i}`, `c=h_{2j-1}`, and `d=h_{2j}`. When `M_ij=+1`, the block error is `I` and is at least `1+|M_ij-u_i v_j|`. When `M_ij=-1`, it is `A` and is at least the same expression, because `|-1-u_i v_j|=|1+u_i v_j|`. Hence

`||X-wh^T||_1 = sum_{i,j} E_ij >= st + ||M-uv^T||_1`.

Combining this with `||X-wh^T||_1 <= T=st+D` yields `||M-uv^T||_1 <= D`. These real vectors are admissible source witnesses, so `(M,D)` is a yes-instance.

Both implications hold for every permitted input. Together with the polynomial construction, they establish the requested polynomial-time many-one reduction. Since the source decision problem is NP-hard by the given premise, binary-input rank-one L1-NMF is NP-hard.
