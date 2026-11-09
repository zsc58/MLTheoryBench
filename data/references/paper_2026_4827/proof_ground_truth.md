# Reference Proof

## Proof Structure

1. Reduce the vector transition to coordinatewise maps after translating each coordinate modulo one.
2. Use translation invariance of uniform measure on the one-dimensional torus.
3. Prove directly from the two affine branches that the triangle-wave map sends a uniform scalar to a uniform scalar.
4. Use independence of the input coordinates and coordinatewise application to obtain the uniform product law on the hypercube.

## Complete Proof

Fix an action `a` and write `c=aM+d`. The activation is continuous and takes values in `[0,1]`, so `F_a` is a measurable map into the hypercube. For each coordinate, let
\[
Q_i=(S_i+c_i)\bmod 1,
\]
where modulo one takes values in `[0,1)`. Since `S` is uniform on the hypercube, its coordinates are independent uniform variables on `[0,1]`. Translation modulo one preserves one-dimensional Lebesgue (Haar) probability measure: for a uniform scalar `U` and a fixed real number `h`, `(U+h)\bmod1` has the uniform law on `[0,1)`. Applying this standard translation-invariance result with `U=S_i` and `h=c_i` shows that each `Q_i` is uniform. This is also the uniform probability law on `[0,1]`, since the endpoint has zero measure. Each `Q_i` is a measurable function of `S_i` alone, so the vector `Q` remains a product of independent uniform coordinates.

For `y\in[0,1]`, the activation satisfies
\[
\phi(y)=\frac1\pi\arccos(\cos(2\pi y))
      =\begin{cases}2y,&0\le y\le 1/2,\\2(1-y),&1/2<y\le1.\end{cases}
\]
Let `0\le u\le v\le1`. The preimage within `[0,1]` is
\[
\{y\in[0,1]:\phi(y)\in[u,v]\}
=[u/2,v/2]\ \cup\ [1-v/2,1-u/2].
\]
The two intervals are disjoint except possibly for the endpoint `1/2`, which has zero Lebesgue measure. Their total length is
\[
(v-u)/2+(v-u)/2=v-u.
\]
This calculation also holds when `u=v`. Therefore, if `U` is uniform on `[0,1]`, then `P(\phi(U)\in[u,v])=v-u`. In particular, taking `u=0` gives the uniform distribution function on `[0,1]`; together with the range of `\phi`, this determines the uniform Borel probability law.

Because `\phi` is one-periodic, for every real `t`, `\phi(t)=\phi(t\bmod1)`. Hence the `i`th output coordinate is
\[
Y_i=\phi(S_i+c_i)=\phi(Q_i),
\]
and is uniform on `[0,1]`. Each `Y_i` is a measurable function of `Q_i` alone, so the coordinates remain independent. Consequently `Y=F_a(S)` has the product law of `d_s` independent `U[0,1]` variables, which is exactly Lebesgue-uniform measure on `[0,1]^{d_s}`. Thus for every Borel set `B` in the hypercube,
\[
\Pr\{F_a(S)\in B\}=\operatorname{Leb}(B).
\]
