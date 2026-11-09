# Reference Proof

## Proof Structure

Write Bellman feasibility as a nonnegative linear system whose coefficients depend polynomially (in fact, affinely) on the candidate value vector. Stratify candidates by the rank of its coefficient matrix. Rank and consistency are characterized by minors. A feasible nonnegative solution can be reduced to a basic feasible solution supported on independent columns. Cramer's rule then gives determinant-product sign conditions. The two inclusions establish the finite union exactly.

## Complete Proof

Let n=|S|, q=|O|, and m=q|A|. For x in R^S, define the n-by-m matrix M(x) by
\[
 M(x)_{s,(o,a)}=\beta(o\mid s)\left(r(s,a)+\gamma\sum_{s'\in S}T(s'\mid s,a)x_{s'}\right),
\]
and let R be the q-by-m row-sum matrix, with R_{o,(\tilde o,a)}=1 if \tilde o=o and 0 otherwise. Put
\[
 C(x)=\begin{bmatrix}M(x)\\R\end{bmatrix},\qquad f(x)=\binom{x}{\mathbf 1_q}.
\]
For a policy vector p=(p_{o,a}) with p_{o,a}=\pi(a\mid o), p\ge0 and Rp=\mathbf1_q, the Bellman equations are exactly M(x)p=x. Hence
\[
x\in\mathcal V\quad\Longleftrightarrow\quad\exists p\ge0:\ C(x)p=f(x).\tag{1}
\]
(The Bellman matrix I-\gamma P^\pi is invertible because \gamma\in(0,1) and P^\pi is stochastic, so this equation indeed has the unique policy value.)

For each integer \rho with 1\le\rho\le\min(n+q,m), each row set I\subseteq\{1,\ldots,n+q\} and column set B\subseteq\{1,\ldots,m\} of cardinality \rho, let U_{\rho,I,B} be the set of x satisfying:

1. det C(x)_{I,B}\ne0;
2. every (\rho+1)-minor of C(x) is zero (when such minors exist);
3. every (\rho+1)-minor of the augmented matrix [C(x)\mid f(x)] is zero (when such minors exist);
4. for every t\in B,
\[
\det C(x)_{I,B,t}\;\det C(x)_{I,B}\ge0,
\]
where C(x)_{I,B,t} is obtained from C(x)_{I,B} by replacing the column indexed by t by f(x)_I (with the replacement in t's position).

Conditions 1 and 2 imply rank C(x)=\rho. Together with condition 3 they imply rank [C(x)\mid f(x)]=\rho, hence f(x) lies in the column space of C(x). For each t\in B, Cramer's rule defines p_t=\det C_{I,B,t}/\det C_{I,B}, and condition 4 gives p_t\ge0; set p_t=0 for t\notin B. The selected rows are solved by construction, and the rank-consistency conclusion makes all rows hold. Thus C(x)p=f(x), so U_{\rho,I,B}\subseteq\mathcal V.

Conversely, take x\in\mathcal V and choose p\ge0 satisfying (1). Let \rho=rank C(x). Among all such nonnegative solutions, choose one with minimal support. If the columns indexed by its support are linearly dependent, there is a nonzero vector z supported there with C(x)z=0. Replacing p by p+tz preserves C(x)p=f(x). Choosing an endpoint of the interval of t for which p+tz\ge0 makes at least one positive coordinate zero while none becomes negative, contradicting minimality. Therefore the support columns are independent. Extend them to a set B of \rho independent columns, assigning zero to the added coordinates, and choose \rho rows I for which C(x)_{I,B} is invertible. Then rank C(x)=\rho, so all (\rho+1)-minors of C(x) vanish; because C(x)p=f(x), rank [C(x)\mid f(x)]=\rho, so all augmented (\rho+1)-minors vanish. On the basis B, the unique solution is given by Cramer's rule and equals the nonnegative coordinates of p, yielding every determinant-product inequality. Hence x\in U_{\rho,I,B}.

There are finitely many \rho,I,B, so (1) gives
\[
\mathcal V=\bigcup_{\rho,I,B}U_{\rho,I,B}.
\]
All entries of C(x) and f(x) are affine in x, and determinants are polynomials; nonvanishing, vanishing, and weak sign conditions therefore make each U_{\rho,I,B} a basic semi-algebraic set. The displayed finite union is the claimed finite rank-stratified quantifier-free semi-algebraic characterization.
