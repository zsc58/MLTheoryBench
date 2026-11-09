# Problem

## Setup

Let \(C,I,Z\) be Polish spaces with their Borel \(\sigma\)-fields, and let \(\mathcal P(C)\) denote the probability measures on \(C\). A latent model is a pair \(M=(Q,K)\), where \(Q\in\mathcal P(C)\) and \(K:C\rightsquigarrow Z\) is a Markov kernel. Its feature law is
\[
p_M:=KQ.
\]
For a measurable map \(f\), write \(E_f\) for its deterministic Markov kernel and \(E_fQ\) for the pushforward of \(Q\). Kernel composition is written from right to left.

For models \(M=(Q,K)\) and \(M'=(Q',K')\) and a Markov kernel \(T:C\rightsquigarrow C\), write \(M\preceq_T M'\) when
\[
Q'=TQ\quad\text{and}\quad K=K'T\quad Q\text{-almost everywhere}.
\]
For a measurable map \(f:C\to C\), abbreviate \(M\preceq_{E_f}M'\) as \(M\preceq_fM'\). Write \(M\preceq M'\) if such a kernel \(T\) exists. The models are *Blackwell-equivalent* if \(M\preceq M'\) and \(M'\preceq M\).

Fix a Borel measure \(\mu\) on \(C\) with \(\operatorname{supp}(\mu)=C\). Let \(\mathcal Q\subseteq\mathcal P(C)\) be any class such that every \(Q\in\mathcal Q\) is mutually absolutely continuous with \(\mu\).

Define
\[
\mathcal R:=\{E_fP:\ P\in\mathcal P(C),\ f:C\to I\text{ is measurable and injective}\}.
\]
Let \(B:I\rightsquigarrow Z\) be a Markov kernel that is measure-separating on \(\mathcal R\): for \(\nu,\nu'\in\mathcal R\), equality \(B\nu=B\nu'\) implies \(\nu=\nu'\). Let \(\mathcal K\) be a class of kernels \(C\rightsquigarrow Z\) that is continuously reducible through \(B\): for every \(K\in\mathcal K\), there is a continuous injective map \(\phi_K:C\to I\) such that
\[
K=B E_{\phi_K}.
\]

Define the valid transition sets
\[
\mathsf T_{\mathcal Q}:=\{f:C\to C:\ f\text{ is measurable and injective, and }E_fQ_0\in\mathcal Q\text{ for some }Q_0\in\mathcal Q\},
\]
\[
\mathsf T_{\mathcal K}:=\{f:C\to C:\ f\text{ is measurable and injective, and there exist }K_0,K_1\in\mathcal K\text{ with }K_0=K_1E_f\ \mu\text{-almost everywhere}\}.
\]
Let \(G\) be a nonempty group of bijective measurable self-maps of \(C\), closed under composition and inverse. Define \(M\sim_G M'\) when \(M\preceq_fM'\) for some \(f\in G\). A model class is identifiable up to \(\sim_G\) if any two models in the class with equal feature laws are \(\sim_G\)-related.

## Task

Prove the following integrated claim. For any \(M=(Q,K)\) and \(M'=(Q',K')\) in \(\mathcal Q\times\mathcal K\), equality of feature laws \(p_M=p_{M'}\) implies that \(M\) and \(M'\) are Blackwell-equivalent. Moreover, if
\[
\mathsf T_{\mathcal Q}\cap\mathsf T_{\mathcal K}\subseteq G,
\]
then \(M\sim_G M'\). Consequently, under this containment assumption, \(\mathcal Q\times\mathcal K\) is identifiable up to \(\sim_G\).
