# Problem

## Geometry and statistical model

Let \((M,G)\) be a finite-dimensional smooth Riemannian manifold. Write \(\langle\cdot,\cdot\rangle_\theta\), \(\|\cdot\|_\theta\), and \(d\) for its inner products, tangent norms, and Riemannian distance. Operator norms and adjoints use these inner products. For tangent vectors, define \((u\otimes v)w=u\langle v,w\rangle\).

Let \(q_\theta\) be a jointly measurable family of probability densities on \(\mathbb R^m\) with respect to Lebesgue measure. On a common set of full Lebesgue measure, suppose \(q_\theta(y)>0\) and \(\theta\mapsto\log q_\theta(y)\) is smooth. Define
\[
\phi(y;\theta)=\operatorname{grad}_\theta\log q_\theta(y),\qquad
I_F(\theta)=\mathbb E_{Y\sim q_\theta}[\phi(Y;\theta)\otimes\phi(Y;\theta)].
\]
The expectations defining \(I_F\) are finite on the compact set introduced below. No global positive-definiteness assumption on \(I_F\) is made.

Let \(R\) be a smooth second-order retraction, meaning \(R_x(0)=x\), \(DR_x(0)=\mathrm{Id}\), and locally
\(d(R_x(v),\exp_x(v))=O(\|v\|_x^3)\).
Let \(K\subset M\) be a compact totally retractive set. Here the inverse branches \(R_x^{-1}\), for \(x\in K\), are defined smoothly on neighborhoods of \(K\), are inverses of restrictions of \(R_x\) to open neighborhoods of zero, and depend smoothly on \((x,y)\) for \(x,y\in K\). Define the invertible differentiated-retraction transport
\[
T_{x,y}=DR_x(R_x^{-1}(y)):T_xM\longrightarrow T_yM.
\]
All iterates below lie in \(K\), and every update vector lies in the chosen inverse branch, so that \(R_{\theta^s}^{-1}(\theta^{s+1})\) equals that update vector.

Let \(L:M\to\mathbb R\) be differentiable. Assume there is a finite constant \(L_0\geq0\) such that, for all \(x,y\in K\),
\[
L(y)\leq L(x)+\langle\operatorname{grad}L(x),R_x^{-1}(y)\rangle_x
 +\frac{L_0}{2}\|R_x^{-1}(y)\|_x^2.
\]
Fix a stationary point \(\theta^\star\in M\), and write \(w(\theta)=L(\theta)-L(\theta^\star)\) and \(W_s=w(\theta^s)\).

## Oracle, sampling, and iteration

Let \(p_\theta\) be a measurable probability kernel on a measurable observation space \(\mathcal Y\). Let \(g(y;\theta)\in T_\theta M\) be a measurable oracle whose integrable expectation satisfies
\[
\mathbb E_{Y\sim p_\theta}[g(Y;\theta)]=\operatorname{grad}L(\theta),\qquad \theta\in K.
\]
Fix an integer minibatch size \(B\geq1\), a starting point \(\theta^{-1}=\theta^0\in K\), and \(\varepsilon>0\). Initialize \(H_0=\varepsilon\mathrm{Id}_{T_{\theta^0}M}\).

Let \(\mathcal G_s\) be the history containing the initial state and all score and gradient samples through step \(s\). At step \(s\geq0\), the state \(\theta^s,H_s\) is \(\mathcal G_s\)-measurable and \(H_s\) acts on \(T_{\theta^{s-1}}M\). Perform the following operations:

1. Put \(T_{s,s-1}=T_{\theta^s,\theta^{s-1}}\), with \(T_{0,-1}=\mathrm{Id}\), and define
\[
Q_s=T_{s,s-1}^*H_s^{-1}T_{s,s-1}.
\]
2. Draw \(\bar Y_{s+1}\) with conditional law \(q_{\theta^s}\) given \(\mathcal G_s\), and put \(\phi_{s+1}=\phi(\bar Y_{s+1};\theta^s)\). Set
\[
H_{s+1}=Q_s^{-1}+\phi_{s+1}\otimes\phi_{s+1},\qquad
\bar H_{s+1}=\frac{H_{s+1}}{s+1},\qquad
\bar H_{s+1}^{-1}=(s+1)H_{s+1}^{-1}.
\]
3. Let \(\mathcal F_s=\mathcal G_s\vee\sigma(\bar Y_{s+1})\). Given \(\mathcal F_s\), draw \(Y_{s+1,1},\ldots,Y_{s+1,B}\) independently with common law \(p_{\theta^s}\), and define
\[
\widehat g_s=\frac1B\sum_{i=1}^B g(Y_{s+1,i};\theta^s).
\]
4. Update
\[
\theta^{s+1}=R_{\theta^s}\!\left(-\tau_{s+1}\bar H_{s+1}^{-1}\widehat g_s\right),
\]
and let \(\mathcal G_{s+1}\) include the new score and gradient samples.

For every parameter visited by the iteration, assume
\[
\mathbb E_{Y\sim p_\theta}[\|g(Y;\theta)\|_\theta^2]
\leq C_0+C_1w(\theta),
\]
\[
\mathbb E_{Y\sim q_\theta}[\|\phi(Y;\theta)\|_\theta^4]
\leq C'_0+C'_1w(\theta)^2,
\]
where \(C_0,C_1\geq0\) and \(C'_0,C'_1>0\) are finite deterministic constants.

Let
\[
\tau_s=\frac{c_\alpha}{(c'_\alpha+s)^\alpha},\qquad
c_\alpha,c'_\alpha>0,\quad \alpha\in(1/2,1),
\]
and assume, for some \(\beta\in[0,\alpha-1/2)\),
\[
\|\bar H_s^{-1}\|_{\mathrm{op}}=O(s^\beta)\quad\text{almost surely}.
\]

## Additional local hypotheses

For the local rate only, additionally assume \(\theta^s\to\theta^\star\) almost surely, \(L\) is twice differentiable in a neighborhood of \(\theta^\star\), and both \(\operatorname{Hess}L(\theta^\star)\) and \(I_F(\theta^\star)\) are positive definite. Assume there exist finite deterministic constants \(C_{\eta,0},C_{\eta,1}>0\) and \(\eta>1/\alpha-1\) such that, for every \(\theta\in K\),
\[
\mathbb E_{Y\sim p_\theta}[\|g(Y;\theta)\|_\theta^{2+2\eta}]
\leq C_{\eta,0}+C_{\eta,1}w(\theta)^{1+\eta}.
\]
This assumption includes that the displayed real power is defined and finite on \(K\). For clarity, nonnegative bases use the usual real power, with \(0^r=0\) for \(r>0\); for a negative base, \(t^r\) is used only when \(r=a/b\) in lowest terms with odd \(b\), and then means \((-1)^a|t|^r\). No nonnegativity of \(W_s\) is otherwise assumed.

## Task

Prove, almost surely, that
\[
L(\theta^s)-L(\theta^\star)\text{ converges to a finite random limit},
\qquad
\min_{0\leq k\leq s}\|\operatorname{grad}L(\theta^k)\|_{\theta^k}^2
=o\!\left(s^{-(1-\alpha)}\right).
\]

If \(L\) is geodesically strictly convex with bounded sublevel sets, prove that \(\theta^s\) converges almost surely to its unique minimizer. Here geodesic strict convexity is understood on a geodesically convex domain containing the parameters and the stationary point: every two points in that domain admit a connecting minimizing geodesic in the domain, and \(L\) is strictly convex along every nonconstant such geodesic. The minimizer conclusion is on that domain.

Under the additional local hypotheses, prove that for every \(\delta>0\),
\[
d(\theta^s,\theta^\star)^2
=O\!\left(\max\left\{\frac{\log s}{s^\alpha},
\frac{(\log s)^{4+\delta}}{s^{4\alpha-2}}\right\}\right)
\quad\text{almost surely}.
\]
In particular, prove \(d(\theta^s,\theta^\star)^2=O(\log s/s^\alpha)\) almost surely when \(\alpha>2/3\). Constants in these almost-sure asymptotic bounds may depend on the sample path and on \(\delta\).
