# Reference Proof

## Contract and proof obligations

This is a conditional theorem within the local slow-time and phase-observation model in the public task. It does not require establishing that arbitrary discrete gradient-descent iterates admit that model. The specialized self-stabilization framework indexed by theory_002 motivates A2 in the source; it is not used here as an independently proved theorem.

The obligations are: establish the regular boundary and compute its Euclidean projected velocity; verify the exit time scaling; compute and control the slow loss difference; derive the phase-averaging error from C² Taylor expansion; and combine these estimates without differentiating the phase error. All are closed below.

## 1. Regular boundary and projected velocity

Put g(x)=∇F(x) and w(x)=∇s(x). The map A=∇²F is C¹ and symmetric. To justify the regularity of s, consider P(x,z)=det(zI−A(x)). At the simple top eigenvalue, the derivative of P with respect to z is the nonzero product of the differences from the other eigenvalues. The C¹ implicit-function theorem, whose applicable statement is that a C¹ scalar equation with nonzero derivative in its scalar unknown has a local C¹ solution, therefore gives a C¹ eigenvalue branch. The spectral gap identifies it locally with the largest eigenvalue. Thus s is C¹ and w is continuous.

Since b=∥w(x*)∥²>0, shrink the neighborhood of the fork so w does not vanish. The regular-level-set form of the implicit-function theorem gives the tangent space

T_xM={z:⟨w(x),z⟩=0}.

The Euclidean projection of −g(x) onto this space is found by subtracting its normal component. Define

α(x)=−⟨g(x),w(x)⟩,   β(x)=∥w(x)∥²,   λ(x)=α(x)/β(x).

The tangent vector nearest to −g(x) is

−g(x)+[⟨g(x),w(x)⟩/β(x)]w(x)=−g(x)−λ(x)w(x).

Indeed, its inner product with w(x) vanishes, and its difference from −g(x) is normal to every tangent vector, which characterizes the orthogonal projection. A2 therefore gives

x_E′(u)=−g(x_E(u))−λ(x_E(u))w(x_E(u)).

For the exit branch, differentiate x_X(u)=y(ρu) using y′=−g(y):

x_X′(u)=−ρg(x_X(u)).

At the fork, λ(x*)=a/b=d²/2. A3 is the source's top-direction condition; no full-spectrum stability inference is needed.

## 2. Slow subset-loss difference

Fix k and define

D_k(u)=f_k(x_X(u))−f_k(x_E(u)),

r_{k,j}(u)=⟨∇f_k(x_j(u)),g(x_j(u))⟩,

q_{k,E}(u)=⟨∇f_k(x_E(u)),w(x_E(u))⟩.

The chain rule gives the exact effective-model identity

D_k′(u)=r_{k,E}(u)−ρr_{k,X}(u)+λ(x_E(u))q_{k,E}(u).

In particular,

D_k′(0)=(1−ρ)r_k+(a/b)q_k.

We next bound the variation without assuming a derivative of w. The C¹ slow curves have bounded velocities on a sufficiently short compact window, so ∥x_j(u)−x*∥≤V_j u. The maps ∇F and ∇f_k are locally Lipschitz, because their derivatives are continuous and bounded on the fixed compact ball. Expanding the difference of their inner products consequently yields

r_{k,j}(u)=r_k+O_k(u).

These bounds also agree with the public Taylor condition A4. No second derivative of s is required.

The function λ is continuous near x*, and λ(x*)=λ₀=a/b>0. Shrink to a window [0,U₀], if necessary, on which

0<λ(x_E(u))≤2λ₀.

This is a continuity consequence for the fixed fork; no amplitude-uniform window is claimed. Continuity and compactness give a finite Q_k bounding both |q_{k,E}(u)| and |q_k|. Hence

|λ(x_E(u))q_{k,E}(u)−λ₀q_k|
≤2λ₀Q_k+λ₀Q_k
=(3/2)Q_k d².

Thus, with constants independent of u,

D_k′(u)=(1−ρ)r_k+(a/b)q_k+O_k(u)+O_k(d²).

This argument deliberately does not assert λ(x_E(u))=λ₀+O(u). Such an assertion would need additional justification if only continuity of the sharpness gradient were available. The weaker estimate above already suffices for the stated final residual and retains the exact derivative coefficient at the fork.

## 3. Integrate the slow difference

The slow curves share x*, so D_k(0)=0 exactly. Integrating the preceding identity gives

D_k(u)=[(1−ρ)r_k+(a/b)q_k]u+O_k(u²)+O_k(d²u).

For example, a derivative error bounded by L_k u+B_k d² contributes at most (L_k/2)u²+B_k d²u. On [0,U₀], the latter term is at most B_k U₀ d².

The initial equality used here concerns D_k, the difference along the slow curves. It is not an assertion that an average involving two phase locations must have exactly the same initial value on the two branches.

## 4. Derive the phase-averaging error at the value level

For j∈{E,X}, let z=x_j(u) and e=e_j⁺(u) or e_j⁻(u). The segment from z to z+e lies in the convex ball B. Let G_k and H_k be finite upper bounds on ∥∇f_k∥ and ∥∇²f_k∥ on B. The C² Taylor formula with integral remainder gives

f_k(z+e)=f_k(z)+⟨∇f_k(z),e⟩+R_k(z,e),

where |R_k(z,e)|≤(H_k/2)∥e∥².

Average this identity over the two phases. A5 bounds the average linear term by G_k M_j d² and the average Taylor remainder by (H_k/2)M_j²d². Therefore

|bar f_{k,j}(u)−f_k(x_j(u))|
≤[G_k M_j+(H_k/2)M_j²]d².

This derives the required second-order loss error from the primitive phase assumptions. It does not assume it as an additional hypothesis. It also does not differentiate this error: a uniformly small value error need not have a uniformly small derivative.

Subtracting the two branch estimates yields

bar Δf_k(u)=D_k(u)+O_k(d²).

Combining this with Section 3 proves

bar Δf_k(u)=[(1−ρ)r_k+(a/b)q_k]u+O_k(u²)+O_k(d²).

All constants are independent of u on the chosen window and may have the dependencies specified in the public task. The proof permits either score to vanish or have either sign. Positivity of a and b is used only in the stated active regime and the local coefficient control. There is no unresolved theorem-critical dependency.
