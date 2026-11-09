# Reference Proof

## Source Contract and Scope

The relevant source assumptions are finite state and action spaces, a terminal binary reward with mean $f^*$, uniform terminal-action sampling, conditional independence of feedback from the action and trajectory prefix given context, terminal state, and reward, exact reward decoding almost surely, and the stated heterogeneous/homogeneous alternatives. The source does not require the context space or feedback space to be finite. Its finite function classes introduce no additional restriction needed by this fixed-witness decoder theorem; no estimation, exploration, or regret theorem is invoked.

All conditional-probability equalities below are almost sure under the uniform-terminal-action experiment. No full-support assumption is used, and no claim is made about arbitrary versions of conditional probabilities on null conditioning events. In particular, the argument does not strengthen decoder realizability to impose conditions at null context-state pairs.

## Theorem-Critical Obligations

1. Derive the action posterior without assuming atomic feedback or a feedback density, using only uniform sampling, conditional independence, and decoder realizability.
2. Verify positivity of the decoder parameters and of the posterior denominators in heterogeneous states.
3. Prove heterogeneous posterior separation for each of the two realized reward values.
4. Establish the threshold consequences and optimal-action equality, including ties.
5. Prove the homogeneous posterior statement for interior and endpoint values of $c$.
6. Establish the decoder's lower-bound, exactness, and homogeneous-mean conclusions without confusing expected reward with realized reward.
7. Prove a global Lipschitz bound, including pairs of points in different regimes and at their boundaries.

All seven obligations are closed below by explicit elementary arguments.

## 1. Posterior Identity

Let $\mathcal C=\sigma(x,s_H)$ and $U=a_H$. For brevity, write $f_a=f^*(x,s_H,a)$, $Q=\sum_b f_b$, and $D=\phi^*(x,y,s_H)$. These are measurable random quantities, and $D=r$ almost surely. Uniform terminal-action sampling gives
\[
\Pr(U=a\mid\mathcal C)=\frac1K.
\]
Because the reward is binary with conditional mean $f_U$, conditional expectation yields
\[
\Pr(U=a,r=1\mid\mathcal C)=\frac{f_a}{K},\qquad
\Pr(U=a,r=0\mid\mathcal C)=\frac{1-f_a}{K}.
\]
Summing over actions gives
\[
\Pr(r=1\mid\mathcal C)=\frac QK,\qquad
\Pr(r=0\mid\mathcal C)=\frac{K-Q}{K}.
\]
Consequently, on $0<Q<K$, finite-outcome conditional Bayes' rule gives
\[
\Pr(U=a\mid\mathcal C,r=1)=\frac{f_a}{Q},\qquad
\Pr(U=a\mid\mathcal C,r=0)=\frac{1-f_a}{K-Q}.
\]
These formulas can equivalently be verified by multiplying each candidate conditional probability by the corresponding conditional probability of $r$; the products reproduce the joint conditional probabilities just computed.

The feedback independence assumption implies
\[
\mathbb E[\mathbf1_{\{U=a\}}\mid\mathcal C,r,y]
=\mathbb E[\mathbf1_{\{U=a\}}\mid\mathcal C,r].
\]
On $0<Q<K$, its right side is
\[
\frac{f_a r}{Q}+\frac{(1-f_a)(1-r)}{K-Q}.
\]
Now condition again on $(\mathcal C,y)$. The tower property applies because $\sigma(\mathcal C,y)\subseteq\sigma(\mathcal C,r,y)$; all conditional probabilities are bounded, and $r=D$ is measurable with respect to $(\mathcal C,y)$ up to a null set. Thus
\[
h^*_a(x,y,s_H)
=\frac{f_aD}{Q}+\frac{(1-f_a)(1-D)}{K-Q}.
\]
This proves the desired identity. No probability of an individual feedback value was divided by another such probability.

## 2. Parameters and Posterior Geometry

From $\sigma>1$,
\[
\theta(K-M)>M,\qquad
\frac\theta M>\frac1{K-M}>\frac1K.
\]
Hence $\xi>0$ and $K\theta-M>0$, so $\kappa>0$. All denominators in the definitions of $G$ and $J$ are therefore positive.

On a heterogeneous pair, choose any maximizing action $a^*$ and put $F=f_{a^*}$. Then
\[
0<\theta\leq F\leq Q\leq M<K/2<K.
\]
The posterior formula therefore applies. The following algebra is pointwise on the almost-sure domain where that formula and $D=r$ hold.

If $D=1$, then $h^*_a=f_a/Q$, and
\[
\Delta(h^*)\geq h^*_{a^*}-\frac1K
=\frac FQ-\frac1K
\geq\frac\theta M-\frac1K
=\frac{K\theta-M}{KM}
\geq\frac{K\theta-M}{K(K-M)}=\kappa.
\]
The last inequality uses $M<K-M$ and the positive numerator.

If $D=0$, then $h^*_a=(1-f_a)/(K-Q)$, and
\[
\Delta(h^*)\geq\frac1K-h^*_{a^*}
=\frac{KF-Q}{K(K-Q)}
\geq\frac{K\theta-Q}{K(K-Q)}.
\]
For the final comparison, direct subtraction gives
\[
\frac{K\theta-Q}{K(K-Q)}-
\frac{K\theta-M}{K(K-M)}
=\frac{(1-\theta)(M-Q)}{(K-Q)(K-M)}\geq0.
\]
Thus $\Delta(h^*)\geq\kappa$ also in this case.

At a homogeneous pair with $0<c<1$, we have $f_a=c$ and $Q=Kc$, so the posterior formula gives
\[
h^*_a=\frac{cD}{Kc}+\frac{(1-c)(1-D)}{K(1-c)}=\frac1K.
\]
For $c=0$ or $c=1$, the reward is the constant $c$ on the homogeneous event. Conditional independence then implies that conditioning on feedback does not change the conditional action distribution there: given $\mathcal C$, the additional conditioning on $r$ is redundant on that event, and
\[
\Pr(U=a\mid\mathcal C,y)=\Pr(U=a\mid\mathcal C)=\frac1K.
\]
This proves the endpoint cases without evaluating a zero denominator. The same observation explains the ordinary posterior interpretation whenever $Q=0$ or $Q=K$.

## 3. Decoder Conclusions

The threshold satisfies
\[
t=\frac12\left(\frac\theta M+\frac1{K-M}\right),\qquad
\frac1{K-M}<t<\frac\theta M=t+\xi.
\]
At a heterogeneous pair, the separation result puts $h^*$ in the last branch of $J$, including the boundary $\Delta(h^*)=\kappa$.

If $D=1$, then $r=1$ and $0\leq G(h^*_a,t,\xi)\leq1$ for every action. Moreover, for every maximizing action $a^*$,
\[
h^*_{a^*}=\frac{f_{a^*}}Q\geq\frac\theta M=t+\xi,
\]
so $G(h^*_{a^*},t,\xi)=1$. Therefore $J(h^*,a)\leq r$ for every action, with equality for every maximizing action.

If $D=0$, then $r=0$, and for every action
\[
h^*_a=\frac{1-f_a}{K-Q}\leq\frac1{K-M}<t.
\]
Thus $G(h^*_a,t,\xi)=0$ and $J(h^*,a)=0=r$ for every action. This also establishes the threshold consequences in the zero-reward case. The argument for maximizing actions uses only their shared maximal reward mean, so ties cause no exception. Since the action set is finite, the probabilistic identities and conclusions may be taken to hold simultaneously for every action on a single probability-one event.

At a homogeneous pair, including both endpoints, $h^*=\mathbf1/K$ and therefore $\Delta(h^*)=0$. The first branch gives
\[
J(h^*,a)=c=f^*(x,s_H,a).
\]
This is an equality with the conditional expected reward, not a claim that $c=r$ when $0<c<1$.

## 4. Global Lipschitz Bound

For $v\in\Delta_A$, define privately for the proof
\[
\alpha(v)=\min\{1,\max\{0,2\Delta(v)/\kappa-1\}\},\qquad
q_a(v)=G(v_a,t,\xi).
\]
Checking the three branches, including their endpoints, gives the single identity
\[
J(v,a)=c+\alpha(v)(q_a(v)-c).
\]
The reverse triangle inequality gives
\[
|\Delta(v)-\Delta(w)|\leq\|v-w\|_\infty.
\]
Clipping a real number to $[0,1]$ cannot increase the distance between two numbers. Hence
\[
|\alpha(v)-\alpha(w)|\leq\frac2\kappa\|v-w\|_\infty.
\]
Similarly, since $G(z,t,\xi)$ is the clipping to $[0,1]$ of $(z-t)/\xi$,
\[
|q_a(v)-q_a(w)|\leq\frac1\xi|v_a-w_a|
\leq\frac1\xi\|v-w\|_\infty.
\]
Using $0\leq\alpha\leq1$, $0\leq q_a\leq1$, and $0\leq c\leq1$,
\[
\begin{aligned}
|J(v,a)-J(w,a)|
&\leq \alpha(v)|q_a(v)-q_a(w)|
 +|\alpha(v)-\alpha(w)|\,|q_a(w)-c|\\
&\leq\left(\frac1\xi+\frac2\kappa\right)\|v-w\|_\infty\\
&\leq\left(\frac1\xi+\frac4\kappa\right)\|v-w\|_\infty.
\end{aligned}
\]
This argument is global and automatically handles both interpolation boundaries and pairs from different regions.

No extra restriction such as $\theta\leq M$ is imposed globally. If the parameter choices permit no heterogeneous pair, the heterogeneous conclusions are vacuous, while the homogeneous and global Lipschitz conclusions remain valid. The argument also covers the one-action simplex and horizon one. All theorem-critical obligations are closed; there is no unresolved external or paper-specific proof dependency.
