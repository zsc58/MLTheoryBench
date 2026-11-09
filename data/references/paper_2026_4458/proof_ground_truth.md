# Reference Proof

## Proof Structure

Construct finitely many localized ReLU cutoffs for each nonzero residual. Their positive and negative sums are separately dominated by the corresponding parts of the residual, and their signed sum contracts the sup norm. Every individual cutoff strictly reduces every finite L^p norm while preserving pointwise residual domination. Pipeline the two-layer cutoff realizations so that a width-5d+1 state emits one correction at every grade after initialization, including at block boundaries. Iteration yields geometric sup-norm decay at block endpoints and uniform convergence along the entire sequence.

## Complete Proof

Write D=[0,1]^d and m=5d+1. Fix eta in (0,(1+2^d)^-1) and a dilation factor s in (1,2). We use the following standard facts: continuous functions on D attain their extrema and are uniformly continuous; every nonempty relatively open subset of D has positive d-dimensional Lebesgue measure. The latter holds because any relative neighborhood of a point of D contains a portion of a sufficiently small box with positive side lengths. Every function and residual constructed below is continuous on D, so its displayed norms and integrals are finite.

### 1. Explicit cutoffs

Define

psi(t)=[rho(t+s)-rho(t+1)+rho(-t+s)-rho(-t+1)]/(s-1)-1.

Direct evaluation gives psi(t)=1 for |t|<=1, psi(t)=(s-|t|)/(s-1) for 1<=|t|<=s, and psi(t)=0 for |t|>=s. Hence 0<=psi<=1. Set

Psi(t_1,...,t_d)=rho(1-d+sum_{i=1}^d psi(t_i)).

Then 0<=Psi<=1, Psi=1 on [-1,1]^d, and Psi=0 whenever some |t_i|>=s. For an axis-aligned cube Q of side length delta and center c, define

Gamma_Q(x)=Psi(2(x-c)/delta).

Thus Gamma_Q=1 on Q and vanishes outside sQ.

For explicit affine maps, let U_Q:R^d->R^{4d} have, for each i, the four coordinates t_i+s, t_i+1, -t_i+s, -t_i+1, where t_i=2(x_i-c_i)/delta. Define V:R^{4d}->R by

V(v)=1-2d+(1/(s-1)) sum_{i=1}^d (v_{4i-3}-v_{4i-2}+v_{4i-1}-v_{4i}).

Then Gamma_Q=rho composed with V composed with rho composed with U_Q. In particular, the cutoff is exactly realized by two affine/ReLU layers, with 4d coordinates in the first layer and one in the second.

### 2. Positive contraction

Fix g in C(D), and put M=||g^+||_infinity. If M=0, define T_eta g=0 and use an empty cutoff list. Suppose M>0, and set

E={x in D:g(x)>(1-eta)M}.

This set is nonempty and relatively open. Define the modulus of continuity

omega_{g^+}(t)=sup{|g^+(x)-g^+(y)|:x,y in D, ||x-y||_2<=t}.

Choose delta>0 sufficiently small that

omega_{g^+}(2 sqrt(d) delta)<=[1-(1+2^d)eta]M.

This is possible by uniform continuity and the strict upper bound on eta. Refine delta further, if needed, so that E meets at least two distinct grid cubes. Such a choice is possible because E contains a relative neighborhood with positive extent. Let Q range over all closed cubes of the grid delta Z^d that meet E. There are finitely many such cubes, and they cover E.

For any fixed point x, membership in a dilated grid cube sQ restricts each grid index to an interval of length s<2. Each such interval contains at most two integers, so at most 2^d dilated cubes contain x.

For any selected Q and x in sQ intersect D, choose y in Q intersect E. Both points belong to sQ, so ||x-y||_2<=s sqrt(d) delta<2 sqrt(d) delta. Consequently,

g^+(x)>=g^+(y)-omega_{g^+}(2 sqrt(d) delta)>2^d eta M>0.

In particular, g(x)>0 on every selected dilated cube intersected with D. Define

T_eta g=eta M sum_Q Gamma_Q.

The overlap bound and the preceding support estimate give 0<=T_eta g<=g^+ everywhere. If x is in E, some selected Q contains x and its cutoff equals one, so T_eta g(x)>=eta M. Therefore, on E,

0<=g^+(x)-T_eta g(x)<=M-eta M,

and outside E,

0<=g^+(x)-T_eta g(x)<=g^+(x)<=(1-eta)M.

Thus, including the M=0 case,

0<=g^+-T_eta g<=(1-eta)||g^+||_infinity.

### 3. Signed contraction and every individual update

Set S_eta g=T_eta g-T_eta(-g). The functions

a=g^+-T_eta g and b=g^--T_eta(-g)

are nonnegative and bounded above by (1-eta)||g||_infinity. Since g-S_eta g=a-b,

||g-S_eta g||_infinity<=(1-eta)||g||_infinity.

Now assume g is nonzero. List first all positive-side cutoffs and then all negative-side cutoffs, omitting any empty side. Write the resulting corrections as

h_t=alpha_t Gamma_{Q_t}, 1<=t<=n,

where alpha_t=eta||g^+||_infinity on the positive side and alpha_t=-eta||g^-||_infinity on the negative side. Each coefficient in the list is nonzero, n>=2, and sum_t h_t=S_eta g. Define H_0=g and H_t=g-sum_{i=1}^t h_i.

On {g>=0}, all negative-side cutoffs vanish, and every partial sum of positive corrections lies between zero and T_eta g<=g. On {g<0}, all positive-side cutoffs vanish, and every partial sum of the magnitudes of negative corrections lies between zero and T_eta(-g)<=-g. It follows that each residual H_t retains the sign of g wherever it is nonzero and

|H_t(x)|<=|H_{t-1}(x)| for every x in D.

More precisely, at an update with h_t(x) nonzero, the remaining sign-compatible correction is bounded by the preceding residual magnitude, so

|H_{t-1}(x)|-|H_t(x)|=|h_t(x)|>0.

Each update is nonzero on a positive-measure subset of D. Indeed, Q_t was selected because it contains some y in the relevant superlevel set in D. Since Gamma_{Q_t}(y)=1 and the cutoff is continuous, the set {x in D:Gamma_{Q_t}(x)>0} is a nonempty relatively open subset of D and has positive measure. This argument remains valid when Q_t meets D only along a boundary face; it does not assert that E intersect Q_t has positive measure.

For any 1<=p<infinity, the function |H_{t-1}|^p-|H_t|^p is nonnegative everywhere and strictly positive on that positive-measure set. Integration yields

||H_t||_p<||H_{t-1}||_p, 1<=t<=n.

At the end of the list,

||H_n||_infinity=||g-S_eta g||_infinity<=(1-eta)||g||_infinity.

Thus one finite block has the required contraction and strict monotonicity at every individual correction, not merely at its endpoint.

### 4. Iteration at the function level

If f=0, take every output map to be zero and any compatible affine state maps. All conclusions follow. Otherwise start with G_0=f. Apply the preceding finite construction to G_0 and let G_1 be its endpoint residual. Whenever G_j is nonzero, apply the same construction, with the same eta, to obtain the next finite list and G_{j+1}. Then

||G_j||_infinity<=(1-eta)^j||f||_infinity

for all constructed endpoints. Every intervening correction has the pointwise and strict finite-L^p properties proved above. If an endpoint vanishes, stop producing nonzero corrections and continue with zero corrections. A residual cannot vanish before the last correction of one of these lists, because each remaining correction would contradict the strict decrease just established.

Concatenate the finite lists into a single list h_t=alpha_t Gamma_{Q_t}. If termination occurs after finitely many corrections, extend the list by zero corrections. The selection of the next list depends only on the already defined endpoint function, so this recursive construction is well-defined. There is no restriction in the task on dependence of the affine maps on f.

### 5. Exact width and a correction at every grade

For every nonzero correction in the concatenated list, write Gamma_{Q_t}=rho composed with V_t composed with rho composed with U_t, using the explicit affine maps above. For any zero corrections appended after termination, take alpha_t=0 and U_t,V_t to be zero affine maps of the same dimensions.

Use state coordinates (u,v,w) in R^d x R^{4d} x R. Define

B_1(x)=(x,U_1(x),0), and C_1=0.

For every j>=2 define the affine maps

B_j(u,v,w)=(u,U_j(u),V_{j-1}(v)),

C_j(u,v,w)=alpha_{j-1} w.

All state maps have exactly the dimensions required by the public task. Since x belongs to D, its coordinates are nonnegative and are preserved by ReLU. Induction gives

z_1(x)=(x,rho(U_1(x)),0)

and, for j>=2,

z_j(x)=(x,rho(U_j(x)),rho(V_{j-1}(rho(U_{j-1}(x))))).

Consequently, C_j(z_j(x))=h_{j-1}(x), and

F_k=sum_{t=1}^{k-1} h_t, r_k=f-sum_{t=1}^{k-1} h_t.

The last state coordinate stores the completed preceding cutoff, not an accumulated sum; the accumulated sum is supplied by the residual-sum outputs. Every layer after the first simultaneously completes one cutoff and initializes the next cutoff's features. This also holds when the two cutoffs belong to different contraction blocks. Thus there are no additional initialization or inactive grades between blocks. If the functional construction terminates, all subsequent outputs vanish, as required.

### 6. Uniform convergence and all stated inequalities

Let N_j be the number of corrections through block j, with N_0=0. At grade k_j=N_j+1 the residual is G_j, and therefore

||r_{k_j}||_infinity<=(1-eta)^j||f||_infinity.

If the construction does not terminate, each block is finite and nonempty, so k_j tends to infinity. For k_j<=k<k_{j+1}, pointwise monotonicity gives

||r_k||_infinity<=||r_{k_j}||_infinity.

Hence the whole residual sequence converges uniformly to zero. If the construction terminates, uniform convergence is immediate from the zero continuation.

The first grade has r_1=r_0=f. At every grade k>=2 before zero continuation, the output is exactly one of the corrections whose strict finite-L^p decrease and pointwise domination were proved in Section 3. During zero continuation, both consecutive residuals vanish. Thus all the requested pointwise inequalities and all finite-L^p inequalities, including their strictness condition, hold simultaneously for this single sequence of affine maps. This proves the public task.
