# Reference Proof

## Proof Structure and Obligations

1. Verify that every inverse and logarithm is well-defined, and identify the supplied variance ratios with the source's Gaussian entropy criteria.
2. Establish a uniform noisy-Gram inverse expansion and derive the gain expansion.
3. Derive the leave-subset-out identity by explicit block algebra, then obtain the uniform loss expansion.
4. Transfer the uniform expansions to eventual unique maximization, treating singleton subset families separately.

All four obligations are closed below. No paper-specific identity is assumed without derivation.

## Complete Proof

### 1. Well-definedness and the variance-ratio criteria

Write \(\tau=\sigma^2\), and keep the dataset, query, features, and subset size fixed throughout. For \(T\subseteq D\), let \(\Phi_T\) have rows \(\phi(x)^{\mathsf T}\), indexed by \(x\in T\), and write \(\phi_*=\phi(x_*)\). Then
\[
K_T=\Phi_T\Phi_T^{\mathsf T},\qquad b_T=\Phi_T\phi_*,\qquad k_{**}=\|\phi_*\|^2>0.
\]
For nonempty \(T\), \(A_T=K_T+\tau I\) is positive definite because \(\tau>0\). Moreover, for any \((u,t)\ne(0,0)\),
\[
\begin{bmatrix}u\\t\end{bmatrix}^{\mathsf T}
\begin{bmatrix}A_T&b_T\\b_T^{\mathsf T}&k_{**}\end{bmatrix}
\begin{bmatrix}u\\t\end{bmatrix}
=\|\Phi_T^{\mathsf T}u+t\phi_*\|^2+\tau\|u\|^2>0.
\]
If \(u\ne0\), the noise term is positive; if \(u=0\), then \(t\ne0\) and \(\phi_*\ne0\). Evaluating this quadratic form at \((u,t)=(-A_T^{-1}b_T,1)\) proves
\[
v(T)=k_{**}-b_T^{\mathsf T}A_T^{-1}b_T>0.
\]
For \(T=\varnothing\), positivity follows from \(v(\varnothing)=k_{**}>0\). Thus all public logarithms are defined, including when a Gram matrix is singular or the query is itself a training input.

The standard Gaussian result used by the source is the following: if a scalar latent variable and an observation vector are jointly Gaussian with covariance blocks \(k_{**}\), \(b_T\), and an invertible observation covariance \(A_T\), then the conditional scalar variance is \(k_{**}-b_T^{\mathsf T}A_T^{-1}b_T\). A scalar Gaussian of variance \(v>0\) has differential entropy \(\tfrac12\log(2\pi e v)\), independently of its mean. The required covariance model is realized by a standard Gaussian feature coefficient vector \(z\), latent values \(f(x)=\phi(x)^{\mathsf T}z\), and observation errors independent of \(z\) and each other, each having variance \(\tau\). Its observation covariance is exactly \(A_T\), and the preceding argument verifies invertibility and positive conditional variance. Consequently the entropy differences are precisely the already supplied definitions
\[
G(S)=-\frac12\log\frac{v(S)}{k_{**}},\qquad
L(S)=\frac12\log\frac{v(D\setminus S)}{v(D)}.
\]
The proof below uses these explicit definitions directly; no targets, posterior means, or additional observation assumptions are required for the algebraic task.

### 2. Uniform inverse expansion and gain

Use the Euclidean operator norm, assigning norm zero to empty matrices and vectors. Set
\[
B=\max\left\{1,\max_{T\subseteq D}\|K_T\|\right\}.
\]
This is finite. For \(\tau\ge2B\), put \(E_T=K_T/\tau\), so \(\|E_T\|\le1/2\). The identity
\[
(I+E_T)^{-1}=I-E_T+E_T^2(I+E_T)^{-1}
\]
and the bound \(\|(I+E_T)^{-1}\|\le2\) give
\[
(K_T+\tau I)^{-1}=\tau^{-1}I-\tau^{-2}K_T+R_T(\tau),
\qquad \|R_T(\tau)\|\le2B^2\tau^{-3}.
\]
This estimate holds uniformly over all nonempty \(T\subseteq D\). Since the vectors \(b_T\) also have a common finite norm bound, it follows that
\[
v(T)=k_{**}-\tau^{-1}\|b_T\|^2+O(\tau^{-2})
\]
uniformly over every \(T\subseteq D\), with the empty case holding exactly. All remainder constants and thresholds here and below depend only on the fixed data, features, query, and, if needed, subset size; they do not depend on \(T\), \(S\), or \(\tau\).

For \(|u|\le1/2\),
\[
\left|\log(1+u)-u\right|
=\left|\int_0^u\frac{-t}{1+t}\,dt\right|\le u^2.
\]
For \(T=S\), write
\[
\frac{v(S)}{k_{**}}=1+u_S,
\qquad u_S=-\frac{a(S)}{k_{**}\tau}+O(\tau^{-2}).
\]
The finite family gives \(u_S=O(\tau^{-1})\) uniformly, so a common threshold ensures \(|u_S|\le1/2\). Hence
\[
G(S)=\frac{a(S)}{2k_{**}\tau}+O(\tau^{-2})
\]
uniformly over \(\mathcal S_M\). The same calculation is valid for any subset of \(D\).

### 3. Leave-subset-out identity and loss

Let \(R=D\setminus S\), let \(A=K_D+\tau I\), and put \(q=A^{-1}b_D\). First suppose both \(R\) and \(S\) are nonempty. Order the retained coordinates first and write
\[
A=\begin{bmatrix}U&B_0\\B_0^{\mathsf T}&V\end{bmatrix},
\quad U=K_R+\tau I,\quad B_0=K_{R,S},\quad V=K_S+\tau I.
\]
Here \(K_{R,S}=(k(x,x'))_{x\in R,x'\in S}\). Define
\[
H=V-B_0^{\mathsf T}U^{-1}B_0,\qquad
r=b_S-B_0^{\mathsf T}U^{-1}b_R.
\]
Both \(U\) and \(H\) are positive definite. For \(H\), apply positive definiteness of \(A\) to \((-U^{-1}B_0w,w)\) for any nonzero \(w\); the resulting quadratic form is \(w^{\mathsf T}Hw>0\).

Direct multiplication verifies the block inverse formula
\[
A^{-1}=\begin{bmatrix}
U^{-1}+U^{-1}B_0H^{-1}B_0^{\mathsf T}U^{-1}&-U^{-1}B_0H^{-1}\\
-H^{-1}B_0^{\mathsf T}U^{-1}&H^{-1}
\end{bmatrix}.
\]
Expanding its quadratic form gives
\[
b_D^{\mathsf T}A^{-1}b_D
=b_R^{\mathsf T}U^{-1}b_R+r^{\mathsf T}H^{-1}r.
\]
Also, its last block row gives
\[
q_S=H^{-1}r,\qquad (A^{-1})_{S,S}=H^{-1}.
\]
Subtracting the variance formulas and substituting these identities yields
\[
v(R)-v(D)=r^{\mathsf T}H^{-1}r
=q_S^{\mathsf T}\big((A^{-1})_{S,S}\big)^{-1}q_S.
\]
This is the required leave-subset-out identity, now derived rather than cited.

If \(S=D\ne\varnothing\), the same identity follows directly from
\[
v(\varnothing)-v(D)=b_D^{\mathsf T}A^{-1}b_D=q^{\mathsf T}Aq.
\]
If \(S=\varnothing\), the variance difference is zero and no inverse of an empty block is needed. These cases also cover \(D=\varnothing\).

For nonempty \(S\), the uniform inverse expansion from the preceding section gives
\[
q_S=\tau^{-1}b_S+O(\tau^{-2}),\qquad
(A^{-1})_{S,S}=\tau^{-1}I_S+O(\tau^{-2}).
\]
Factoring \(\tau^{-1}\) from the second expression leaves \(I_S+O(\tau^{-1})\). Beyond a common threshold its error has norm at most \(1/2\); the same inverse bound therefore gives
\[
\big((A^{-1})_{S,S}\big)^{-1}=\tau I_S+O(1).
\]
Substitution into the derived identity yields
\[
\begin{aligned}
v(R)-v(D)
&=\big(\tau^{-1}b_S+O(\tau^{-2})\big)^{\mathsf T}
\big(\tau I_S+O(1)\big)
\big(\tau^{-1}b_S+O(\tau^{-2})\big)\\
&=\tau^{-1}a(S)+O(\tau^{-2}).
\end{aligned}
\]
The cross terms are \(O(\tau^{-2})\) because the \(b_S\) have a common finite bound; all other error terms have that order or smaller. The expansion also holds for \(S=\varnothing\), where both sides have zero leading term and the variance difference is exactly zero.

Applying the variance expansion to \(D\) gives \(v(D)=k_{**}+O(\tau^{-1})\). In particular, \(v(D)\ge k_{**}/2\) beyond a fixed threshold, and
\[
\frac1{v(D)}-\frac1{k_{**}}
=\frac{k_{**}-v(D)}{k_{**}v(D)}=O(\tau^{-1}).
\]
Consequently,
\[
\frac{v(R)-v(D)}{v(D)}
=\frac{a(S)}{k_{**}\tau}+O(\tau^{-2})
\]
uniformly over \(\mathcal S_M\). Applying the logarithm estimate once more proves
\[
L(S)=\frac12\log\left(1+\frac{v(R)-v(D)}{v(D)}\right)
=\frac{a(S)}{2k_{**}\tau}+O(\tau^{-2}).
\]
Because \(\tau=\sigma^2\), the two remainder bounds are exactly \(O(\sigma^{-4})\). No positivity of \(a(S)\) was used, so vanishing leading coefficients cause no exception.

### 4. Eventual common unique maximization

The family \(\mathcal S_M\) is finite and nonempty because \(0\le M\le|D|\). If it has one element, that element uniquely maximizes every function on it for every \(\tau>0\); one may choose \(\sigma_0^2=1\). This includes \(M=0\), \(M=|D|\), and the empty-dataset case.

Otherwise, assume \(a\) has a unique maximizer \(S^\dagger\), and define the strictly positive gap
\[
\Delta=a(S^\dagger)-\max_{S\in\mathcal S_M,\ S\ne S^\dagger}a(S)>0.
\]
The two uniform expansions provide common constants \(C>0\) and \(\tau_{\rm asym}\ge1\) such that, for either \(J\in\{G,L\}\), every \(S\in\mathcal S_M\), and every \(\tau\ge\tau_{\rm asym}\),
\[
J(S)=\frac{a(S)}{2k_{**}\tau}+r_J(S,\tau),
\qquad |r_J(S,\tau)|\le C\tau^{-2}.
\]
For every competitor \(S\ne S^\dagger\),
\[
J(S^\dagger)-J(S)
\ge\frac{\Delta}{2k_{**}\tau}-2C\tau^{-2}.
\]
Choose
\[
\sigma_0^2=\max\left\{\tau_{\rm asym},\frac{4Ck_{**}}{\Delta}+1\right\}.
\]
This is finite, and the displayed difference is strictly positive for every \(\tau=\sigma^2\ge\sigma_0^2\), every competitor, and both criteria. Thus both criteria are uniquely maximized by \(S^\dagger\) throughout the required eventual range.
