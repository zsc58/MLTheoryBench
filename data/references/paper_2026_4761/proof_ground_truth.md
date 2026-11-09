# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) existence, uniqueness, and equivalence to Euclidean projection; (2) the common-shift clipping characterization, or another complete optimality argument; (3) preservation of order; (4) equality with the unique minimizer on the ordered feasible subset; and (5) an actual PAV-based computation enforcing both bounds and mass, with the claimed running time. Each obligation is closed below. No result from the cited projection thesis or an unstated fixed-sum PAV theorem is assumed.

## Complete Proof

### 1. Projection formulation and uniqueness

Put `z=x/tau`. The hypersimplex is nonempty because `(k/n,...,k/n)` belongs to it. It is compact and convex. Moreover,

`tau ||u||_2^2-2<x,u> = tau ||u-z||_2^2-||x||_2^2/tau`.

Since `tau>0`, the two objectives have the same minimizers. Continuity on the compact feasible set gives existence, and strict convexity gives uniqueness. When `k=n`, the feasible set consists only of the all-one vector; this also covers `n=1`. Henceforth suppose `1<=k<n`.

### 2. Common-shift characterization and optimality

Define `clip(a,0,1)=min(1,max(0,a))` and

`F(lambda)=sum_i clip(z_i-lambda,0,1)`.

This function is continuous and nonincreasing. It equals `n` for `lambda<=min_i(z_i-1)` and equals `0` for `lambda>=max_i z_i`. Therefore there is a real `lambda` with `F(lambda)=k`.

For any fixed `lambda`, minimizing

`Q_lambda(u)=1/2 ||u-z||_2^2 + lambda(sum_i u_i-k)`

over `[0,1]^n` separates coordinatewise. Completing each coordinate's square shows that its unique minimizer is

`v_i=clip(z_i-lambda,0,1)`.

Choose a root of `F(lambda)=k`. Then `v` is feasible for the hypersimplex. For every other feasible `u`, the multiplier term in `Q_lambda` vanishes at both `u` and `v`, so `Q_lambda(v)<=Q_lambda(u)` proves that `v` minimizes the original squared distance. By uniqueness, `v=y`.

This is also the KKT clipping formula, with the multiplier scaled for the objective `1/2 ||u-z||_2^2`. No uniqueness of the multiplier is asserted. Flat root intervals can occur even for interior values of `k`.

### 3. Order preservation

The function `a -> clip(a-lambda,0,1)` is nondecreasing. Consequently `z_1>=...>=z_n` implies `y_1>=...>=y_n`. The all-one solution for `k=n` has the same property.

### 4. Ordered minimization

Let

`C_k={u in [0,1]^n: u_1>=...>=u_n, sum_i u_i=k}`.

Order preservation gives `y in C_k`, and `C_k` is contained in the hypersimplex. Since `y` uniquely minimizes squared distance on the larger set, it uniquely minimizes it on `C_k` as well.

### 5. PAV with the bounds and prescribed sum enforced

It is important not to substitute ordinary PAV for the entire constrained computation. Ordinary nonincreasing PAV starts with singleton blocks and pools adjacent blocks whenever the left block mean is smaller than the right block mean. On nonincreasing input there are no such violations, so it returns that input after a linear scan.

For a fixed common shift `lambda`, the data `w_i=z_i-lambda` remain nonincreasing. Thus PAV on `w` has no violations. Clipping its output to `[0,1]` gives `v_i=clip(w_i,0,1)`, still nonincreasing. Each coordinate separately minimizes `(u_i-w_i)^2` on `[0,1]`; because these coordinate minimizers are ordered, they jointly give the unique bounded isotonic minimizer for the shifted data. This proves the only PAV behavior needed here directly, without importing a general isotonic-regression theorem.

The remaining task is to find the shift enforcing `sum_i v_i=k` exactly within the stated time bound. Use the function `F` from Step 2. Its only possible breakpoints are the `2n` numbers

`z_i-1` and `z_i`.

Sort these events and group equal event values. For sufficiently small `lambda`, all coordinates are one, so `F(lambda)=n` and its slope is zero. At an event `z_i-1`, coordinate `i` starts decreasing with slope `-1`; at an event `z_i`, it stops decreasing and is zero. Consequently, between consecutive distinct event values `t<t'`,

`F(lambda)=F(t)-m(lambda-t)`,

where `m` is the number of coordinates currently in their decreasing segment. Grouped events update `m` by adding the number of starts and subtracting the number of stops.

Initialize at the smallest event, where `F=n`. At each event `t`, first test whether `F(t)=k`; if so, choose `lambda=t`. Otherwise update the slope count for all events at `t` and consider the next interval. When `m>0` and `F(t)>=k>=F(t)-m(t'-t)`, the exact root is

`lambda=t+(F(t)-k)/m`.

If no root lies in that interval, advance using `F(t')=F(t)-m(t'-t)`. When `m=0`, the interval is flat; either its left endpoint was already a root, or it contains no root, so no division by zero occurs. Continuity, the initial value `n`, and the final value `0` ensure that the sweep finds a root. Processing equal events together handles all ties.

Having found this shift, perform the bounded PAV computation just described. Its output has mass `k`. The shifted objective differs from the original objective by a constant on `C_k`, since

`||u-(z-lambda*1)||_2^2 = ||u-z||_2^2 + 2lambda(sum_i u_i-sum_i z_i) + n lambda^2`.

Hence this feasible bounded isotonic minimizer also solves the original problem on `C_k`, consistently with Steps 2-4.

Sorting costs `O(n log n)` arithmetic operations and comparisons; grouping and sweeping the events, running PAV on the shifted sorted data, and clipping cost `O(n)` additional operations. The storage requirement is `O(n)`. The endpoint `k=n` is returned directly in `O(n)` time. Thus the full constrained PAV-based computation has the claimed `O(n log n)` asymptotic running time, with no accuracy-dependent iteration count.

All five theorem-critical obligations are closed.
