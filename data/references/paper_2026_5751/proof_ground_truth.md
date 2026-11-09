# Reference Proof

## Proof obligations and probability convention

The proof closes the following obligations: the degenerate-class cases; comparison of parity dimension with DS dimension; the density bound for tuples that may contain repeated inputs; preservation of parity certificates under rollout; application of the two independent learning black boxes in the public probability model; and a matching worst-case lower bound with exact dimension and confidence dependence. The only external results used without proof are the two standard independent learning theorems stated precisely in Section 4 below. The lower bound is proved directly.

The sampling probability is over the i.i.d. input tuple and the learner's internal randomness, with target labels substituted as deterministic values. Measurability of the displayed disagreement sets and success events is the public standing well-definedness convention. There is no additional requirement that the complete labeled tuple be a measurable random variable into a separately prescribed measurable label space. In particular, neither pointwise termination nor the combinatorial arguments below are claimed to prove that target-label maps, stopping predicates, or global choices of transductive rules are measurable for arbitrary externally imposed measurable structures.

Write \(R=\mathsf R_\sigma(\mathcal H)\) and \(d=\operatorname{DSdim}(\mathcal H)\).

## 1. Degenerate cases and parity certificates

If \(d=\infty\), the upper bound is an extended-real, vacuous bound. If \(\mathcal H=\varnothing\), the realizable requirement has no targets; the constant empty-string predictor shows \(n_{\rm PAC}^{\epsilon,\delta}(R)=0\). This is well-defined even when \(\mathcal A\) is empty, since \(\varnothing\in\mathcal A^*\).

If \(\mathcal H\ne\varnothing\) and \(d=0\), any two members of \(\mathcal H\) agree everywhere. Otherwise their two different labels at a point would form a nonempty one-dimensional pseudo-cube. Thus the class has one function, and its rollout can be returned without data. Its disagreement set against the unique target is empty and its success event is certain. This also covers an empty state domain. Hence the upper bound holds with zero samples in these cases. For the remaining upper-bound argument assume \(1\leq d<\infty\).

For a finite nonempty class \(G\subseteq Y^D\), an even certificate is a nonzero vector \(w\in\mathbb F_2^G\) such that, for every \(i\in D\) and every \(u\in G|_{D\setminus\{i\}}\),
\[
 \sum_{g:g|_{D\setminus\{i\}}=u}w_g=0.
\]
All certificate sums are in \(\mathbb F_2\). Define \(\operatorname{ParDim}(F)\) as the supremum of the sizes of finite domain sets \(D\) on which some finite nonempty subset of \(F|_D\) admits such a certificate. Set it to zero when no positive-dimensional witness exists, and to infinity when the sizes are unbounded. A finite set of restriction patterns can always be represented by a finite subclass of \(F\), by choosing one representative for each pattern.

The support of an even certificate is a nonempty DS pseudo-cube. Indeed, the deletion fiber containing a support point has even total coefficient and contains that point with coefficient one, so it contains another support point. Those two patterns agree off the deleted coordinate and differ at that coordinate. Therefore
\[
 \operatorname{ParDim}(F)\leq\operatorname{DSdim}(F). \tag{1}
\]

## 2. Parity dimension bounds one-inclusion density

For a finite nonempty \(G\subseteq Y^I\), with \(I\) a finite coordinate set, define
\[
 \operatorname{dens}_I(G)=\frac{1}{|G|}\sum_{i\in I}\left(|G|-\left|G|_{I\setminus\{i\}}\right|\right).
\]
For \(F\subseteq Y^Z\), a tuple \(\mathbf z=(z_1,\ldots,z_n)\), and a finite subclass \(F_0\subseteq F\), write
\[
 F_0|_{\mathbf z}=\{(f(z_1),\ldots,f(z_n)):f\in F_0\}\subseteq Y^{[n]}.
\]
The tuple may contain repetitions. Define
\[
 \mu_F(n)=\sup_{\mathbf z\in Z^n}\ \sup_{\substack{\varnothing\ne F_0\subseteq F\\F_0\text{ finite}}}\operatorname{dens}_{[n]}(F_0|_{\mathbf z}),
\]
with value zero when there are no admissible pairs. We prove
\[
 \mu_F(n)\leq\operatorname{ParDim}(F)\qquad(n\geq1). \tag{2}
\]
The infinite-parity-dimension case is immediate. Otherwise put \(p=\operatorname{ParDim}(F)<\infty\), and fix an admissible tuple and subclass. Set \(I=[n]\) and \(G=F_0|_{\mathbf z}\).

For \(S\subseteq I\), let \(V_S\subseteq\mathbb F_2^G\) be the space of functions on \(G\) depending only on the coordinates in \(S\), and let
\[
 L_p=\sum_{\substack{S\subseteq I\\|S|\leq p}}V_S.
\]
For \(w\in\mathbb F_2^G\), define its marginal \(m_Sw\in\mathbb F_2^{G|_S}\) by summing coefficients over fibers of \(G\to G|_S\). Under the standard coordinatewise bilinear pairing, orthogonality to \(V_S\) is equivalent to \(m_Sw=0\): test against the indicator of each restriction fiber. Successive marginalization equals direct marginalization, since both operations sum over the same finite fibers.

Suppose \(L_p\ne\mathbb F_2^G\). Nondegeneracy of the pairing gives a nonzero \(w\in L_p^\perp\). Hence \(m_Sw=0\) whenever \(|S|\leq p\). Since \(m_Iw=w\ne0\), choose an inclusion-minimal \(T\subseteq I\) with \(\theta=m_Tw\ne0\). Then \(|T|>p\), and each one-coordinate deletion marginal of \(\theta\) vanishes, by minimality and compositionality of marginalization.

The original inputs \(z_i\), \(i\in T\), must be distinct. If \(z_i=z_j\) for different \(i,j\in T\), every pattern in \(G|_T\) has equal entries at \(i,j\). Deleting coordinate \(i\) is therefore injective: its missing entry is determined by coordinate \(j\). All its fibers are singletons, so its zero marginal forces every coefficient of \(\theta\) to be zero, a contradiction. Relabeling the coordinates of \(T\) by their distinct original inputs now turns \(\theta\) into an even certificate for a finite restriction of \(F\) on \(|T|>p\) points. This contradicts the definition of \(p\). Consequently \(L_p=\mathbb F_2^G\).

Choose a basis \(b_1,\ldots,b_{|G|}\) from the union of the spaces \(V_S\) with \(|S|\leq p\). For each \(b_j\), choose such a set \(S_j\) on which it depends. The space \(V_{I\setminus\{i\}}\) has dimension \(\left|G|_{I\setminus\{i\}}\right|\), and contains the independent basis vectors with \(i\notin S_j\). Thus
\[
 |G|-\left|G|_{I\setminus\{i\}}\right|\leq|\{j:i\in S_j\}|.
\]
Summing over \(i\) yields
\[
 |G|\operatorname{dens}_I(G)\leq\sum_j|S_j|\leq p|G|.
\]
Division by \(|G|>0\), followed by the two suprema, proves (2), including tuples with repeated inputs.

## 3. Parity dimension does not increase under rollout

We prove
\[
 \operatorname{ParDim}(R)\leq\operatorname{ParDim}(\mathcal H). \tag{3}
\]
It suffices to transfer every positive-dimensional finite witness. Let \(x_1,\ldots,x_k\) be distinct start states, and let a finite trace table \(V\) on those starts carry a nonzero even certificate \(\alpha\). Choose a finite set \(\mathcal H_0\subseteq\mathcal H\) of representatives whose rollout table is exactly \(V\). Let \(T_i\) be its set of traces at start \(x_i\).

Each \(T_i\) is finite and prefix-free. If one terminal trace were a proper prefix of another, the same deterministic predicate \(\sigma(x_i,u)\) would have to be both one and zero at the shorter trace \(u\). Pointwise termination guarantees that all strings in these finite sets are finite. Their prefix nodes consequently form finite rooted trees. At prefix \(u\), the block consists of traces extending \(u\); the child blocks partition it according to the next action. Leaves are singleton terminal traces. Unary chains are allowed.

Extend \(\alpha\) by zero to \(T_1\times\cdots\times T_k\). The resulting tensor is nonzero and line-even: for each coordinate and each fixing of the other coordinates, its sum in that coordinate is zero. Such a line either is a deletion fiber of \(V\) or has no supported entries.

We establish the required product-tree fact. Suppose a nonzero tensor on a product of finite leaf sets is line-even in every coordinate. Process the coordinates successively, retaining child-block systems in processed coordinates and singleton leaf systems elsewhere. Maintain that the current tensor is nonzero and line-even in all coordinates. In the next coordinate, treat all other current indices as one finite parameter set. To each tree node assign the vector obtained by summing the current tensor over leaves beneath that node. The root vector is zero, and some leaf vector is nonzero. Along a path from the root to such a leaf, take the first node with nonzero vector. Its parent has zero vector and a child family not all of whose vectors are zero. Replacing this coordinate by the children of that parent therefore gives a nonzero tensor whose sum in that coordinate is zero. For every other coordinate, each new line sum is a finite sum of old zero line sums. This proves the induction invariant. At the end, one internal node has been selected in each tree, and the quotient over their child blocks is nonzero and line-even.

Apply this fact to the extended trace tensor, obtaining internal prefixes \(u_i\). Relabel a child \(u_i a_i\) by its next action \(a_i\). Children of a prefix have distinct next actions, so the resulting action tensor \(\beta\) remains nonzero and line-even. If an action tuple has coefficient one, the defining block sum contains at least one trace tuple with coefficient one. One representative \(h\in\mathcal H_0\) realizes that whole trace tuple, and its rollouts satisfy
\[
 h(x_i\mathbin{\cdot}u_i)=a_i\qquad\text{for every }i.
\]
Thus every support tuple of \(\beta\) is realized in the finite local-value table
\[
 W=\{(h(x_1\mathbin{\cdot}u_1),\ldots,h(x_k\mathbin{\cdot}u_k)):h\in\mathcal H_0\}.
\]
Extend \(\beta\) by zero to all of \(W\). This produces a nonzero even certificate: a deletion fiber with a fixed action outside a selected child set has only zero coefficients; every other deletion sum is a zero line sum of \(\beta\).

The states \(z_i=x_i\mathbin{\cdot}u_i\) are distinct. If \(z_i=z_j\), every pattern in \(W\) has equal entries at \(i,j\), so deleting \(i\) is injective and its zero marginal forces the whole certificate to vanish. This is impossible. The resulting certificate therefore witnesses parity dimension at least \(k\) on \(k\) distinct local states. Taking the supremum proves (3).

Combining (1)-(3) gives, for every \(n\geq1\),
\[
 \mu_R(n)\leq\operatorname{ParDim}(R)\leq\operatorname{ParDim}(\mathcal H)\leq d. \tag{4}
\]
The construction used only finitely many traces at a time, not a uniform bound on rollout lengths.

## 4. Conversion to the PAC upper bound

Here are the relevant statements of the two standard independent background results, corresponding to theory_014 and theory_015 and supplied source L000115-L000128. Their probability expressions use the same well-definedness convention as the public PAC definition. They are not assertions about measurable realizations of arbitrary set-theoretic maps for additional prescribed measurable structures.

A transductive rule at size \(n\) receives the entire input tuple \(\mathbf z=(z_1,\ldots,z_n)\), a hidden index \(i\), and all labels except the label at \(i\). The tuple need not have distinct entries. Its leave-one-out error on \(F\) is
\[
 \operatorname{LOO}_n(A;F)=\sup_{\substack{f\in F\\\mathbf z\in Z^n}}\frac1n\sum_{i=1}^n\Pr[A(\mathbf z,i,(f(z_j))_{j\ne i})\ne f(z_i)],
\]
where the probability is over the rule's randomness. Permutation invariance means that simultaneously permuting inputs, the hidden index, and the revealed labels preserves the distribution of its output.

The one-inclusion theorem states that for every multiclass class and every \(n\geq1\), there is a possibly randomized permutation-invariant rule with leave-one-out error at most \(\lceil\mu_F(n)\rceil/n\). It applies to arbitrary label sets and uses the density defined using finite subclasses, even when the whole restriction is infinite.

The aggregation theorem states that if a multiclass class admits, for every \(n\geq1\), a permutation-invariant rule with leave-one-out error at most \(K/n\), with one fixed \(K\geq0\), then a universal constant \(C\) satisfies
\[
 n_{\rm PAC}^{\epsilon,\delta}(F)\leq C\frac{K+\log(1/\delta)}{\epsilon}
\]
for every \(\epsilon,\delta\in(0,1)\), in the possibly randomized, improper realizable learning model.

We verify the structural hypotheses for this application while retaining the standing probability convention. Pointwise termination makes \(R\subseteq(\mathcal A^*)^{\mathcal X}\) a class of total functions with a nonempty label set; it is used for totality, not to infer measurability of label generation. Exact-trace examples and losses are exactly the deterministic target labels and zero-one losses of this multiclass class. Equation (4) holds for every tuple size, including repetitions and arbitrary finite subclasses. Since \(d\) is an integer, one-inclusion gives a permutation-invariant rule with error at most \(d/n\) for every \(n\). Aggregation with \(K=d\), in the same probability convention, proves
\[
 n_{\rm PAC}^{\epsilon,\delta}(R)\leq C\frac{d+\log(1/\delta)}{\epsilon}.
\]
The degenerate and infinite-dimensional cases were already handled. There is no restriction requiring the learner to output a local hypothesis or a proper rollout. No trace-length parameter enters the bound.

In particular, this argument must not be read as supplying measurable complete-label observations for arbitrary stopping rules and arbitrary separately chosen sigma-algebras. That stronger assertion is neither needed by the public probability model nor established by the source. For the reported two-target example with a shared bit and a possibly nonmeasurable choice between trace lengths one and two, one observation reveals the bit and the learner returns the corresponding known rollout function. Its risk is identically zero and its success event is certain. Nonmeasurability of the whole label map therefore does not obstruct that source-model learning experiment.

## 5. Matching worst-case lower bound

We give an explicit ordinary binary family and then apply one-step stopping. This proves the required existential lower bound without assuming a confidence lower bound for every class of positive DS dimension.

Fix \(d\geq1\). On \(Z=\{0,1,\ldots,d\}\), let
\[
 F_d=\{f_b:b\in\{0,1\}^d\},\qquad f_b(0)=0,\quad f_b(j)=b_j\ (1\leq j\leq d).
\]
All binary patterns occur on \(\{1,\ldots,d\}\), while any larger domain set contains the constant coordinate zero. Thus \(\operatorname{DSdim}(F_d)=d\).

Take \(0<\epsilon,\delta\leq1/16\). For the dimension lower bound, put \(\rho=8\epsilon\), give each point \(j\geq1\) mass \(\rho/d\), and give zero the remaining mass. Choose \(b\) uniformly at random, independently of the sample and learner randomness. Conditional on a point \(j\) being absent from the sample, its bit is still fair and independent of the learner's information, so its conditional prediction error is at least one half. Let \(W\) be the learner's risk restricted to the rare points. Then \(0\leq W\leq\rho\) and
\[
 \mathbb E W\geq\frac\rho2(1-\rho/d)^m.
\]
If \(m\leq d/(4\rho)=d/(32\epsilon)\), the elementary inequality \((1-t)^m\geq1-mt\) gives \(\mathbb E W\geq3\rho/8=3\epsilon\). Also
\[
 \mathbb E W\leq\epsilon+(\rho-\epsilon)\Pr(W>\epsilon).
\]
Consequently \(\Pr(W>\epsilon)\geq2/7\). Total risk is at least \(W\), even if the learner also errs at the dummy point. Averaging over the finite set of targets shows that some fixed target has failure probability at least \(2/7>\delta\). Hence
\[
 n_{\rm PAC}^{\epsilon,\delta}(F_d)>\frac{d}{32\epsilon}.
\]

For the confidence lower bound, give point one mass \(2\epsilon\), give zero the remaining mass, and give all other points zero mass. Consider the two targets whose only possible difference is their bit at point one. With probability \((1-2\epsilon)^m\), point one is not observed. On that event the observed sample is identical under the two targets. For any randomized learner, averaging over those targets gives probability at least one half of a wrong prediction at point one, which incurs risk \(2\epsilon>\epsilon\). Therefore any learner succeeding for both targets must satisfy
\[
 \tfrac12(1-2\epsilon)^m\leq\delta.
\]
Since \(-\log(1-2\epsilon)\leq4\epsilon\) and \(\log(1/(2\delta))\geq\tfrac12\log(1/\delta)\) in the chosen parameter range,
\[
 n_{\rm PAC}^{\epsilon,\delta}(F_d)\geq\frac{\log(1/\delta)}{8\epsilon}.
\]
Both experiments use the same class \(F_d\). Combining the two necessary sample sizes gives
\[
 n_{\rm PAC}^{\epsilon,\delta}(F_d)\geq\frac{d+\log(1/\delta)}{64\epsilon}. \tag{5}
\]

Embed this class into the required aligned domain. Set \(\mathcal E=Z\), \(\mathcal A=\{0,1\}\), and \(\mathcal X=\mathcal E\times\mathcal A^*\). Define \(h_b(j,\varnothing)=b_j\) for \(1\leq j\leq d\), and set \(h_b=0\) at every other state. Let \(\mathcal H=\{h_b:b\in\{0,1\}^d\}\). Its only nonconstant coordinates are the \(d\) indicated roots, where all binary patterns occur, so \(\operatorname{DSdim}(\mathcal H)=d\).

Define the total stopping rule by
\[
 \sigma(x,y)=1\quad\Longleftrightarrow\quad |y|\geq1.
\]
Every rollout from every state halts after exactly one action. On root states its labels are precisely the singleton strings corresponding to \(F_d\)'s labels. Any trace learner can therefore be used on an ordinary \(F_d\) sample by encoding inputs as roots and labels as singleton strings. Decode its predicted trace as one if it is the singleton string \((1)\), and as zero otherwise. Whenever the trace prediction is correct, its decoded bit is correct; hence decoded risk is no larger than trace risk. This reduction applies to arbitrary improper and randomized trace learners and gives
\[
 n_{\rm PAC}^{\epsilon,\delta}(\mathsf R_\sigma(\mathcal H))\geq n_{\rm PAC}^{\epsilon,\delta}(F_d).
\]
Equation (5) proves the required lower bound with, for example, \(c=1/64\) and \(c_0=1/16\). This completes all proof obligations in the stated probability model.
