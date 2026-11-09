# Reference Proof

## Proof Structure

1. Express each leaf event as the conjunction of branch outcomes along its root-to-leaf path, and factor its mixed-intervention probability into the selected P- or Q-state conditional probabilities and complements.
2. Verify that the mixed leaf probabilities form a probability distribution and sum their products with fixed leaf predictions to obtain every interventional mean.
3. Verify that the all-P and all-Q interventions recover the original means under P and Q.
4. Establish finite Shapley efficiency by counting permutations and telescoping, including the tree with no split nodes.

## Private Source-Audit Note

The source's intended construction uses the ancestors and branch outcomes of each leaf. Its literal Algorithm 2 instead tests whether a leaf region is a subset of a conditioning region and of a designated-branch region. Those tests are not reliable for an empty leaf region: the empty set is a subset of every event. The source-local repair recorded under theory_004 replaces those tests by structural ancestry and the actual branch taken on the leaf's path. It does not impose a nonempty-leaf assumption or alter the public task, which already specifies the correct node-based intervention.

For a concrete check, let X={0,1}, P({1})=1/4, and Q({1})=3/4. Let the root u test x=1, with its designated child v again testing x=1. The designated leaf of v is {1}, its opposite leaf is empty, and the root's opposite leaf is {0}. Give these leaves predictions 2, 1, and 0 respectively. Both split conditionals are defined: p_u=1/4, q_u=3/4, and p_v=q_v=1. The actual model is f(x)=2x and its prediction shift is 1. The literal containment algorithm assigns the empty leaf the selected root probability r rather than zero, so its weighted prediction sum is 3r instead of 2r and its attribution total is 3/2. Structural path traversal assigns that leaf r(1-1)=0 and restores the correct result.

The source's exclusion of undefined split conditionals is explicit at L000249 and L000349. In the public task, the assumption that every event-conditioned probability is defined supplies this domain condition. No conditional probability on a zero-mass split-reach event is assigned an arbitrary value.

## Complete Proof

Let C be the finite set of internal split nodes and L the finite set of terminal nodes. For each leaf l, let A_l be its input region and let Path(l) be its structural ancestor split nodes. For c in Path(l), write b_{l,c}=1 if the path takes the designated branch at c and b_{l,c}=0 otherwise. These are structural path choices, including when A_l is empty; they are not inferred from vacuous containment of A_l in other events.

For each S subset C, define r_c(S)=q_c when c belongs to S and r_c(S)=p_c otherwise. At a split c, route the mass arriving there to its designated child with proportion r_c(S) and to its opposite child with proportion 1-r_c(S). Start with mass 1 at the root. This is the intervention in the public task.

By induction along a path, the mass assigned to leaf l is

Pr_S(l) = product over c in Path(l) of t_{l,c}(S),

where t_{l,c}(S)=r_c(S) if b_{l,c}=1 and t_{l,c}(S)=1-r_c(S) if b_{l,c}=0. The product over an empty path is 1. This argument uses conditional routing at nodes; it does not assert that the original input tests are independent.

All these masses are nonnegative. Whenever a node with mass m is expanded, its two children receive masses m*r_c(S) and m*(1-r_c(S)), whose sum is m. Starting with the root and expanding all internal nodes therefore preserves total mass. Since the tree is finite, the final masses are precisely the leaf masses, and

sum over l in L of Pr_S(l) = 1.

This establishes the mixed law for every S, including branch probabilities equal to 0 or 1. In particular, a node may receive zero mixed mass without requiring any new conditional probability to be estimated there: the routing probabilities are the already specified numbers r_c(S).

An empty input leaf also causes no inconsistency. Its parent, if present, is a split node whose reach event has positive probability under P and Q. The branch leading to that empty leaf has conditional probability zero under both distributions. Its selected branch factor is consequently zero for every S, so the empty leaf receives mass zero. This observation is not needed for mass conservation on the abstract leaf set, but confirms that the structural construction does not give positive mass to an impossible leaf event.

For every S, the tree has the fixed prediction a_l at leaf l. Thus the mean under its mixed leaf law is

mu_hat_S = sum over l in L of Pr_S(l)*a_l.

This is exactly the public definition using widehat P_S. All means are finite because there are finitely many real leaf predictions and the leaf masses form a probability distribution. No additional normalization is introduced.

We next verify the endpoints. Fix R=P or R=Q and select all node probabilities from R. Let A_c be the event of reaching split c. Its two child events are A_c intersect g_{1,c} and A_c minus g_{1,c}. By the definition of event conditioning, their R-probabilities are respectively

R(A_c)*R(g_{1,c} | A_c) and R(A_c)*(1-R(g_{1,c} | A_c)).

The root event has probability 1. Induction down the tree therefore shows that routing with all probabilities from R assigns every leaf l its actual probability R(A_l). This includes zero-probability leaves and uses conditioning only at split nodes, where the task assumes it is defined. Since the leaf events are disjoint, exhaust X, and f equals a_l on A_l,

mu_hat_empty = sum over l of P(A_l)*a_l = mu_P,

mu_hat_C = sum over l of Q(A_l)*a_l = mu_Q.

If C is empty, the root is the only leaf, f is constant, and mu_Q-mu_P=0. The attribution sum is an empty sum and is also zero. No factorial with a negative argument is evaluated, since no attribution phi_c is defined in this case.

Now suppose n=|C| is positive. Define the finite real-valued cooperative game v(S)=mu_hat_S-mu_hat_empty. For a permutation pi of C and a node c, let Pred_pi(c) be the set of nodes preceding c in pi. Given S subset C minus {c}, exactly |S|!*(n-|S|-1)! permutations have Pred_pi(c)=S: order the nodes of S before c, place c next, and order the remaining nodes afterward. Consequently the public weighted formula is exactly

phi_c = (1/n!) times the sum over permutations pi of [mu_hat_{Pred_pi(c) union {c}}-mu_hat_{Pred_pi(c)}].

For a fixed permutation pi=(c_1,...,c_n), put S_0=empty and S_k={c_1,...,c_k}. Summing the marginal differences over the nodes in this permutation gives

sum from k=1 to n of [mu_hat_{S_k}-mu_hat_{S_{k-1}}] = mu_hat_C-mu_hat_empty.

All sums are finite, so summing over c and averaging over permutations may be interchanged. Therefore

sum over c in C of phi_c = mu_hat_C-mu_hat_empty = mu_Q-mu_P.

This explicitly proves the relevant efficiency identity for the defined game. It covers every admissible intervention, unchanged factors, zero prediction shifts, and the allowed endpoint branch probabilities. Together with the empty-C case, it proves the full public claim.

## Obligation Closure

- Mixed-intervention factorization: closed by structural path induction.
- Nonnegativity and normalization for every S: closed by nodewise mass conservation.
- Interventional means and their finiteness: closed by the finite weighted-sum definition.
- Recovery of P and Q means: closed by conditional-probability induction and the leaf-event decomposition of f.
- Shapley efficiency: closed by permutation counting and finite telescoping; theory_009 is standard independent background, not an unresolved dependency.
- Boundary and empty cases: covered by the same routing argument and the explicit empty-C case.

There are no unresolved theorem-critical proof obligations.
