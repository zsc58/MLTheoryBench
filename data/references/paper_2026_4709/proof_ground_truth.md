# Reference Proof

## Theorem-Critical Obligations

1. Establish normalization of the backward path law from each terminal and of the forward terminal marginal from the local policy definitions and finite acyclic graph.
2. Use the actual pointwise zero-loss condition to derive the under-allocated balance equations, establish $Z_\nabla>0$, and exclude forward mass on over-allocated trajectories.
3. Sum the balance equations over paths to each under-allocated terminal.
4. Normalize over terminal states to determine $Z_\nabla$ and the complete distribution.

All four obligations are closed below. The elementary marginalization fact indexed by theory_011 is proved directly; no external theorem or specialized method is invoked without proof.

## Complete Proof

### 1. Path-law normalization

All path sets are finite because the graph is finite and acyclic. Every vertex is reachable from the unique source: otherwise, following incoming edges backward from an unreachable vertex would eventually reach another source. Likewise, every vertex has a directed path to the unique sink. Terminal states have only their deterministic transition to the sink, so paths to the sink partition according to their final terminal state.

For a vertex $v\ne s_{\mathrm{sink}}$, let $B(v)$ be the sum of backward product probabilities over paths from $v$ back to $s_0$. The empty path gives $B(s_0)=1$. In topological order, for $v\ne s_0,s_{\mathrm{sink}}$,
\[
 B(v)=\sum_{u:\,(u,v)\in E}p_B^\nabla(v,u)B(u).
\]
Every parent precedes $v$. Induction and local normalization of the backward policy therefore give $B(v)=1$. In particular,
\[
 \sum_{\tau\in\mathcal T_x}p_B^\nabla(\tau\mid x)=1
 \qquad(x\in X).
\]
The deterministic sink transition is not included in this backward product.

Similarly, let $F(v)$ be the total forward product probability of completing a path from $v$ to the sink, including the deterministic terminal transition. Set $F(s_{\mathrm{sink}})=1$. Reverse topological induction gives $F(v)=1$: at a terminal this follows from its deterministic final transition, and at a nonterminal it follows by summing $p_F^\nabla(v,w)F(w)$ over its children. Consequently,
\[
 \sum_{x\in X}p_{\mathrm{top}}^\nabla(x)=F(s_0)=1.
\]

### 2. Extracting the consequences of zero loss

For every trajectory, the loss is a well-defined square of a real logarithm. Its being zero means that its logarithm argument equals $1$.

For $x\in U$ and $\tau\in\mathcal T_x$, the indicator vanishes, so
\[
 \frac{Z_\nabla p_F^\nabla(\tau)}{R(x)^\beta p_B^\nabla(\tau\mid x)}=1,
\]
and hence
\[
 Z_\nabla p_F^\nabla(\tau)
 =R(x)^\beta p_B^\nabla(\tau\mid x).
\]
Because $U$ is nonempty, choose $x\in U$ and a path to it. The right-hand side is strictly positive by the loss-domain assumptions. Since $p_F^\nabla(\tau)\ge0$ and $Z_\nabla\ge0$, this proves $Z_\nabla>0$.

For $x\in O$ and $\tau\in\mathcal T_x$, the indicator equals $1$, so
\[
 \frac{Z_\nabla p_F^\nabla(\tau)}{R(x)^\beta p_B^\nabla(\tau\mid x)}+1=1.
\]
The denominator and $Z_\nabla$ are positive. Therefore $p_F^\nabla(\tau)=0$, and summing over paths gives
\[
 p_{\mathrm{top}}^\nabla(x)=0\qquad(x\in O).
\]

### 3. Marginal balance on the under-allocated set

For each $x\in U$, sum the balance equation over $\mathcal T_x$. Using the definitions and the backward normalization proved above,
\[
 \begin{aligned}
 Z_\nabla p_{\mathrm{top}}^\nabla(x)
 &=R(x)^\beta\sum_{\tau\in\mathcal T_x}p_B^\nabla(\tau\mid x)\\
 &=R(x)^\beta.
 \end{aligned}
\]

### 4. Determining the normalizer and distribution

The forward terminal marginal is normalized and has zero mass on $O$. Therefore
\[
 Z_\nabla
 =Z_\nabla\sum_{x\in X}p_{\mathrm{top}}^\nabla(x)
 =\sum_{x\in U}R(x)^\beta.
\]
This sum is finite and strictly positive because $X$ is finite, $U$ is nonempty, and $R(x)>0$. Substituting into the marginal balance equation and combining it with zero mass on $O$ yields
\[
 p_{\mathrm{top}}^\nabla(x)=
 \frac{R(x)^\beta\mathbf 1\{x\in U\}}
 {\sum_{y\in U}R(y)^\beta}
 \qquad(x\in X).
\]
This proves both conclusions.

## Boundary and Dependency Checks

The argument also covers $O=\varnothing$ and singleton terminal or under-allocated sets. It does not condition on a potentially empty allocation region. Although a nonnegative exploration normalizer is admitted in the setup, $Z_\nabla=0$ is incompatible with the pointwise zero-loss assumption on nonempty $U$, as shown explicitly. Equality at the allocation threshold belongs to $O$ under the stated definition. Zero forward probabilities on $O$ cause no logarithm problem: the logarithm argument there equals $1$.

The hypothesis concerns every trajectory and the exact allocation sets of the fixed canonical model. No assumption about an exploratory sampling frequency, estimated allocation indicator, convergence of training, existence of a zero-loss parameterization, or uniqueness of an optimizer is used.

## Source Correspondence

The source loss at L000093 has the indicator inside the logarithm. The former theory_005 record put it outside and was a transcription error. The source's products at L000033-L000038 end at the terminal state; conditioning the backward law on $x$ does not introduce a backward transition from the auxiliary sink.

The source-local corrections already recorded for theory_006 are retained: use the tempered reward in the balance calculation, use the over-allocated set for its support-exclusion term, and sum the final normalizer only over the under-allocated set. The selected theorem at L000100-L000102 is a one-way implication from pointwise zero loss. Its proof does not require the stronger converse wording at L000264 or the conditional-expectation decomposition and exploratory-probability estimate at L000266-L000267. Neither is used as a proof obligation here. The frozen task retains its finite-state scope; the source's general state-graph definition does not expressly state global finiteness.
