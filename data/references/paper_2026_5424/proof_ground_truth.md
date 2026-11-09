# Reference Proof

## Proof Structure

First embed every fixed-pair class into the constant-mixture class, and embed the latter into the input-adaptive class using constant bias-only gates. Strictness is proved in two dimensions by constructing two width-one functions and studying the jump of their derivative normal to the line \(x_2=0\). Fixed-pair networks have restricted one-dimensional jump profiles, while constant-mixture networks have jump profiles represented almost everywhere by a finite activation-dictionary ridge class. The second witness is excluded from every such finite class by a local analytic-versus-piecewise-polynomial argument. Finally, extend the witnesses to \(d>2\) by ignoring the extra coordinates.

## Complete Proof

Write \(R(t)=\max\{0,t\}\), let \(\mathcal N=\{R,L_\eta\}\), and initially take \(d=2\).

### 1. The two inclusions

Fix \(p,q\). If \(p\le q\), every member of \(\mathcal F_{p,q}^{(m)}\) belongs to \(\mathcal L^{(m)}\) by setting \(\alpha_{p,q}=1\) and all other mixture coefficients to zero. If \(p>q\), commute the two scalar factors and interchange \(w_k,u_k\), reducing to the preceding case. Hence
\[
\bigcup_{p,q=1}^7\mathcal F_{p,q}^{(m)}\subseteq\mathcal L^{(m)}.
\]

Now take \(f\in\mathcal L^{(m)}\). Choose \(\rho>0\) so small that \(|\rho\alpha_{p,q}|<1\) for every pair. Such a choice also exists when every coefficient is zero. For each pair choose the bias-only vector
\[
v_{p,q}=(0,\ldots,0,\operatorname{arctanh}(\rho\alpha_{p,q})),
\]
so that \(\tanh(v_{p,q}^{\mathsf T}\bar x)=\rho\alpha_{p,q}\) for every \(x\). Replacing each output coefficient \(a_k\) by \(a_k/\rho\) gives exactly \(f\) in \(\mathcal M^{(m)}\). Thus \(\mathcal L^{(m)}\subseteq\mathcal M^{(m)}\).

### 2. Jump profiles for fixed-pair networks

For a piecewise \(C^1\) function define, wherever the one-sided traces exist,
\[
Jf(t)=\partial_{x_2}f(t,0+)-\partial_{x_2}f(t,0-).
\]
The profile restrictions below concern agreement outside a finite exceptional set with a continuous profile function. They do not assert that the actual jump has the same value at an intersection with another singular line.

For an activation \(\sigma\), let
\[
\mathcal R_\sigma^{(M)}=
\left\{\sum_{\ell=1}^M b_\ell\sigma(r_\ell t+s_\ell):
 b_\ell,r_\ell,s_\ell\in\mathbb R\right\}.
\]
Every function in this class is continuous. We claim that if \(f\in\mathcal F_{p,q}^{(m)}\), there exist a finite set \(E\subset\mathbb R\) and a continuous function
\[
H\in
\mathbf 1_{\{\sigma_p\in\mathcal N\}}\mathcal R_{\sigma_q}^{(m)}+
\mathbf 1_{\{\sigma_q\in\mathcal N\}}\mathcal R_{\sigma_p}^{(m)}
\quad\text{such that}\quad
Jf(t)=H(t)\quad(t\notin E). \tag{1}
\]
An absent term denotes \(\{0\}\).

To verify this, examine each affine argument \(\ell(x_1,x_2)=a x_1+b x_2+c\). If it is constant, its activated factor has zero normal derivative. In particular, an identically zero argument gives a zero factor, since every dictionary activation vanishes at zero. Otherwise its zero set is an affine line. A line different from \(x_2=0\) meets that line in at most one point or is disjoint from it. Exclude those finitely many intersection coordinates, taking their union over the representation. At every remaining point, a nonsmooth ridge can contribute a normal-derivative jump only if its singular line equals \(x_2=0\).

Among the dictionary activations, only \(R\) and \(L_\eta\) have jumps in their first derivatives. When a nonconstant affine argument has zero set \(x_2=0\), it is \(b x_2\) with \(b\ne0\). The jumps of the normal derivatives of \(R(bx_2)\) and \(L_\eta(bx_2)\) are respectively \(|b|\) and \((1-\eta)|b|\), both constants. The other five activations are \(C^1\) and contribute no such jump.

For continuous factors \(g,h\) with these traces, the product rule on each side gives
\[
J(gh)(t)=Jg(t)\,h(t,0)+g(t,0)\,Jh(t)
\]
outside the exceptional set. Thus, when the first factor produces a jump, its contribution is a constant multiple of the second factor restricted to the line, namely \(\sigma_q(rt+s)\). The analogous statement holds with the factors interchanged. If both singular lines equal \(x_2=0\), both factors vanish on that line, so these contributions are zero. Summing over the neurons gives at most \(m\) ridges of each indicated type. Padding with zero coefficients proves (1).

Consider
\[
A(t)=R(t)+\tanh t.
\]
This function does not belong to the profile class in (1), for any finite \(m\) and any pair \(p,q\). If neither activation is in \(\mathcal N\), that class is \(\{0\}\), whereas \(A\) is not identically zero. If exactly one is in \(\mathcal N\), every possible profile is \(C^1\), whereas
\[
A'(0-)=1,\qquad A'(0+)=2.
\]
If both are in \(\mathcal N\), every possible profile is continuous piecewise affine with finitely many breakpoints. Such a function is affine on some nonempty subinterval of \((0,1)\), while
\[
A''(t)=\tanh''t=-2(1-\tanh^2t)\tanh t\ne0
\quad(t>0).
\]
This proves the exclusion in all three cases.

Now define
\[
T_L(x_1,x_2)=R(x_2)\bigl(R(x_1)+\tanh x_1\bigr).
\]
It belongs to \(\mathcal L^{(1)}\): use \(a_1=1\), \(w_1=(0,1,0)\), \(u_1=(1,0,0)\), set \(\alpha_{2,2}=\alpha_{2,7}=1\), and set every other mixture coefficient to zero. The dictionary order makes both selected branches admissible. Hence it also belongs to \(\mathcal L^{(m)}\) by adding zero-output neurons.

On the other hand, \(JT_L=A\). If \(T_L\) belonged to any \(\mathcal F_{p,q}^{(m)}\), equality of the functions would give equality of their one-sided normal-derivative traces wherever used in (1). Consequently \(A=H\) outside a finite set for a continuous profile \(H\) in the class specified there. Since \(A\) and \(H\) are continuous and the complement of a finite set is dense, they agree everywhere. This contradicts the exclusion above. Thus
\[
T_L\in\mathcal L^{(m)}\setminus
\bigcup_{p,q=1}^7\mathcal F_{p,q}^{(m)},
\]
which proves strictness of the first inclusion.

### 3. Jump profiles for constant-mixture networks

Define the finite dictionary-ridge class
\[
\mathcal A^{(M)}=
\left\{
\sum_{\ell=1}^M\sum_{c=1}^7
 b_{\ell,c}\sigma_c(r_\ell t+s_\ell):
 b_{\ell,c},r_\ell,s_\ell\in\mathbb R
\right\}.
\]
The affine parameters \(r_\ell,s_\ell\) are shared by all seven activations in the \(\ell\)-th dictionary ridge. Every function in this class is continuous.

We claim that
\[
f\in\mathcal L^{(m)}\quad\Longrightarrow\quad
\text{there exist finite }E\subset\mathbb R\text{ and }H\in\mathcal A^{(2m)}
\text{ with }Jf(t)=H(t)\text{ for }t\notin E. \tag{2}
\]
Use the same exceptional-set construction and constant-factor treatment as in the preceding section. For neuron \(k\), write the restrictions of its two affine arguments to \(x_2=0\) as \(\xi_k(t)\) and \(\zeta_k(t)\). For each activation \(\sigma_p\), let \(c_{k,p}\) be its constant normal-derivative jump when applied to the first affine argument, outside the exceptional set. This constant is zero unless the activation is in \(\mathcal N\) and its nonconstant affine argument has zero set \(x_2=0\). Define \(d_{k,q}\) analogously for the second argument.

The product-rule calculation gives the following profile for neuron \(k\):
\[
a_k\sum_{p\le q}\alpha_{p,q}
\left[c_{k,p}\sigma_q(\zeta_k(t))+
 d_{k,q}\sigma_p(\xi_k(t))\right].
\]
Grouping the first terms by \(q\) and the second terms by \(p\), this becomes
\[
\sum_{q=1}^7 C_{k,q}\sigma_q(\zeta_k(t))+
\sum_{p=1}^7 D_{k,p}\sigma_p(\xi_k(t)),
\]
where
\[
C_{k,q}=a_k\sum_{p=1}^{q}\alpha_{p,q}c_{k,p},
\qquad
D_{k,p}=a_k\sum_{q=p}^{7}\alpha_{p,q}d_{k,q}.
\]
These are two dictionary ridges with shared affine arguments. There are therefore at most two such ridges per neuron, proving (2), with zero coefficients used to pad unused ridges.

### 4. A profile outside every finite dictionary-ridge class

Let
\[
B(t)=R(t)\tanh t.
\]
We prove that \(B\notin\mathcal A^{(M)}\) for every finite \(M\ge1\). Suppose otherwise. For each nonconstant affine argument \(r_\ell t+s_\ell\), the only possible breakpoint of a ReLU, leaky-ReLU, or squared-ReLU term is \(-s_\ell/r_\ell\). Constant arguments have no breakpoints. Choose \(\varepsilon>0\) so that none of the finitely many nonzero breakpoints lies in \((-\varepsilon,\varepsilon)\).

The activations \(\mathrm{id}\), GELU, SiLU, and \(\tanh\) are real analytic at every real argument, not merely at zero. For SiLU and \(\tanh\), this follows from their exponential formulas with denominators nonzero on the real line. For GELU, \(\Phi'(t)=(2\pi)^{-1/2}e^{-t^2/2}\) is real analytic, and locally integrating its power series shows that \(\Phi\), and hence \(t\Phi(t)\), is real analytic. Thus arbitrary real affine shifts cause no difficulty.

On \((-\varepsilon,\varepsilon)\), collect all terms using these analytic activations into a single real-analytic function \(S\). Every remaining term is polynomial of degree at most two separately on each side of zero, including constant affine arguments. Consequently there are polynomials \(P_-\) and \(P_+\), each of degree at most two, such that
\[
B(t)=S(t)+P_-(t)\quad(-\varepsilon<t<0),
\qquad
B(t)=S(t)+P_+(t)\quad(0<t<\varepsilon).
\]

Use the standard real-analytic identity principle: two real-analytic functions on a connected open interval that agree on a nonempty open subinterval agree throughout that interval. Here \(S\) and \(-P_-\) are both real analytic on the connected interval \((-\varepsilon,\varepsilon)\). Because \(B=0\) on \((-\varepsilon,0)\), they agree on that nonempty open subinterval. Hence \(S=-P_-\) throughout \((-\varepsilon,\varepsilon)\). It follows on the positive interval that
\[
B(t)=P_+(t)-P_-(t),
\]
a polynomial of degree at most two.

This is impossible. The exponential expansions give
\[
\sinh t=t+\frac{t^3}{6}+O(t^5),\qquad
\cosh t=1+\frac{t^2}{2}+O(t^4),
\]
and therefore
\[
\tanh t=t-\frac{t^3}{3}+O(t^5).
\]
For positive \(t\),
\[
B(t)=t\tanh t=t^2-\frac{t^4}{3}+O(t^6).
\]
If a polynomial of degree at most two agreed with this function on \((0,\varepsilon)\), the expansion at zero would force its constant and linear coefficients to be zero and its quadratic coefficient to be one. It would then equal \(t^2\), contradicting the nonzero fourth-order coefficient. Thus \(B\notin\mathcal A^{(M)}\) for every finite \(M\ge1\).

Finally set
\[
T_M(x_1,x_2)=R(x_2)R(x_1)\tanh x_1.
\]
This lies in \(\mathcal M^{(1)}\): choose \(a_1=1\), \(w_1=(0,1,0)\), \(u_1=(1,0,0)\), \(v_{2,2}=(1,0,0)\), and every other gate vector equal to zero. All other branches vanish because \(\tanh(0)=0\). Hence \(T_M\in\mathcal M^{(m)}\) by zero-output padding.

Its jump profile is \(JT_M=B\). If it belonged to \(\mathcal L^{(m)}\), (2) would give a continuous \(H\in\mathcal A^{(2m)}\) agreeing with \(B\) outside a finite set. Continuity would imply \(H=B\) everywhere, contradicting the preceding non-membership result. Therefore
\[
T_M\in\mathcal M^{(m)}\setminus\mathcal L^{(m)},
\]
so the second inclusion is strict.

### 5. Higher dimensions

For \(d>2\), both witnesses are realized by giving every weight and gate vector zero in coordinates \(3,\ldots,d\), retaining the same bias coordinates. Conversely, restricting any alleged \(d\)-dimensional representation of either witness to the subspace \(x_3=\cdots=x_d=0\) produces a representation in the corresponding two-dimensional class with the same width and the same sharing of coefficients and affine arguments. This would contradict the two-dimensional separations. The strict hierarchy therefore holds for every \(d\ge2\) and \(m\ge1\).
