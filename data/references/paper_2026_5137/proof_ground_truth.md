# Reference Proof

## Scope and Obligations

The proof must establish: equality of the encoded laws; a measurable matching map on conull subsets; a globally injective measurable extension using the common measure class; both Blackwell comparisons; membership in the two almost-everywhere transition sets; and the group-identifiability conclusion.

Continuity and full support do not, by themselves, identify the encoder images. In particular, the proof below does not identify an encoder image with the support of its pushforward. It uses the already-stated mutual absolute continuity of the two priors to handle exceptional sets.

## Standard Independent Background

We use the Borel injective image theorem in the following precise form: an injective Borel map between standard Borel spaces has Borel image and a Borel inverse on its image. Its restriction to any Borel subset has the same properties. This is an independent standard result, not a paper-specific dependency. Here the original spaces are Polish with their Borel sigma-fields, hence standard Borel; the encoders are continuous and therefore Borel; and every subsequent restriction is to a Borel subset. Thus all applications satisfy its hypotheses.

## Complete Proof

If the model class is empty, the claims are vacuous. Otherwise fix \(M=(Q,K)\) and \(M'=(Q',K')\) in the class with equal feature laws. In particular,
\[
Q\sim\mu\sim Q'.
\]
Choose the continuous injective encoders \(\phi,\phi':C\to I\) such that
\[
K=BE_\phi,\qquad K'=BE_{\phi'}.
\]
Functoriality and feature equality give
\[
B(E_\phi Q)=KQ=K'Q'=B(E_{\phi'}Q').
\]
Both encoded measures belong to \(\mathcal R\). Separation therefore yields
\[
R:=E_\phi Q=E_{\phi'}Q'. \tag{1}
\]

### Matching on Conull Borel Subsets

The images \(\phi(C)\) and \(\phi'(C)\) are Borel. Define
\[
J:=\phi(C)\cap\phi'(C),\qquad A:=\phi^{-1}(J),\qquad A':=(\phi')^{-1}(J).
\]
Both images have \(R\)-measure one, so \(R(J)=1\). Consequently \(Q(A)=Q'(A')=1\). Equivalence to \(\mu\) implies that both \(C\setminus A\) and \(C\setminus A'\) are \(\mu\)-null.

Define
\[
\theta:A\to A',\qquad \theta=(\phi'|_{A'})^{-1}\circ\phi|_A.
\]
The Borel injective image theorem shows that \(\theta\) is a Borel bijection with Borel inverse. It satisfies \(\phi'\circ\theta=\phi\) on \(A\).

For each Borel \(H\subseteq A'\), the set \(\phi'(H)\) is Borel and
\[
Q(\theta^{-1}(H))=R(\phi'(H))=Q'(H).
\]
Thus \(\theta\) sends \(Q|_A\) to \(Q'|_{A'}\). In particular, if \(F\subseteq A\) is Borel and \(\mu(F)=0\), then
\[
Q'(\theta(F))=Q(F)=0,
\]
so \(\mu(\theta(F))=0\). Similarly, \(\theta^{-1}\) sends Borel \(\mu\)-null subsets of \(A'\) to \(\mu\)-null sets. These conclusions use both directions of absolute continuity; full topological support alone would not justify them.

### A Global Borel Bijection

Let
\[
N_0:=(C\setminus A)\cup(C\setminus A'),
\]
and recursively define
\[
N_{n+1}:=N_n\cup\theta(N_n\cap A)\cup\theta^{-1}(N_n\cap A')\qquad(n\geq0).
\]
Every \(N_n\) is Borel and \(\mu\)-null, by the preceding null-set preservation and Borel-image facts. Therefore
\[
N:=\bigcup_{n\geq0}N_n,\qquad D:=C\setminus N
\]
are Borel, \(\mu(N)=0\), and \(D\subseteq A\cap A'\).

We claim \(\theta(D)=D\). If \(x\in D\) and \(\theta(x)\in N_n\), then
\(x\in\theta^{-1}(N_n\cap A')\subseteq N_{n+1}\), a contradiction. Thus \(\theta(D)\subseteq D\). Conversely, if \(y\in D\) and \(\theta^{-1}(y)\in N_n\), then \(y\in\theta(N_n\cap A)\subseteq N_{n+1}\), again a contradiction. Hence \(\theta^{-1}(D)\subseteq D\), which proves the claim.

Define
\[
\tau(c):=\begin{cases}\theta(c),&c\in D,\\c,&c\in N.\end{cases}
\]
Because \(\theta\) bijects \(D\) onto itself and the other branch is the identity on the disjoint Borel set \(N\), \(\tau\) is a bijective measurable self-map of \(C\). Its inverse is \(\theta^{-1}\) on \(D\) and the identity on \(N\), and is also measurable.

Since \(Q(N)=Q'(N)=0\), this change on null sets preserves the distributional identity:
\[
E_\tau Q=Q'. \tag{2}
\]
On \(D\), the matching-encoder identity gives
\[
K(\cdot\mid c)=B(\cdot\mid\phi(c))=B(\cdot\mid\phi'(\tau(c)))=K'(\cdot\mid\tau(c)).
\]
Therefore
\[
K=K'E_\tau\quad\mu\text{-almost everywhere}, \tag{3}
\]
and also \(Q\)-almost everywhere. Equations (2) and (3) prove \(M\preceq_\tau M'\).

The inverse comparison is equally explicit. Equation (2) gives
\[
E_{\tau^{-1}}Q'=Q.
\]
Since \(\tau^{-1}\) bijects \(D\) onto itself, equation (3) gives
\[
K'=KE_{\tau^{-1}}\quad Q'\text{-almost everywhere}.
\]
Thus \(M'\preceq_{\tau^{-1}}M\), and the models are Blackwell-equivalent.

### Transition Sets and Identifiability

Equation (2), together with \(Q,Q'\in\mathcal Q\), implies \(\tau\in\mathsf T_{\mathcal Q}\). Equation (3), together with \(K,K'\in\mathcal K\), implies \(\tau\in\mathsf T_{\mathcal K}\). This second membership uses the stated almost-everywhere definition; it does not require the two kernels to agree at every point of \(N\).

If \(\mathsf T_{\mathcal Q}\cap\mathsf T_{\mathcal K}\subseteq G\), then \(\tau\in G\). Equations (2) and (3) consequently give \(M\sim_G M'\).

For completeness, the relation \(\sim_G\) is an equivalence relation on the model space. Reflexivity follows from the identity in \(G\). For symmetry, if \(M\preceq_f M'\) with \(f\in G\), then \(E_{f^{-1}}Q'=Q\). If \(K(c)=K'(f(c))\) off a \(Q\)-null Borel set \(H\), its image \(f(H)\) is Borel and \(Q'\)-null. Hence \(K'(c')=K(f^{-1}(c'))\) outside that image, proving the reverse comparison under \(f^{-1}\in G\).

For transitivity, suppose \(M\preceq_f M'\) and \(M'\preceq_g M''\). Then
\[
Q''=E_gE_fQ=E_{g\circ f}Q.
\]
A \(Q'\)-null exceptional set for the second kernel identity has \(Q\)-null preimage under \(f\), because \(Q'=E_fQ\). Combining the two identities therefore gives
\[
K=K''E_{g\circ f}\quad Q\text{-almost everywhere}.
\]
The composition \(g\circ f\) belongs to \(G\), proving transitivity.

Finally, the pair \(M,M'\) was arbitrary. Under the class-level containment assumption, every feature-equivalent pair is \(\sim_G\)-related, proving class identifiability.

## Audit Boundary

All obligations of this public task are closed. The construction uses the common measure class already present in the task. It does not prove the broader standalone assertion that continuity and full support, without mutual absolute continuity of the priors, always give a global injective transition. That broader source assertion is not used as a black box.
