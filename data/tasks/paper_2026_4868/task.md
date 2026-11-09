# Problem

## Setup

Write `N={1,2,...}` and `N_0={0,1,2,...}`. Let `X` be a countable domain. Identify a binary hypothesis `h` with its support `supp(h)={x in X:h(x)=1}`. A class is **UUS** if every support is infinite.

Generators are deterministic. The target `h` is fixed before the interaction and is hidden from the generator. At round `t`, the generator receives the ordered input prefix `x_1,...,x_t` and outputs `o_t in X`. It may retain its previous inputs, outputs, and permitted oracle answers.

For a fixed target `h` and generator `G`, a **replay sequence** satisfies, at every round,

`x_t in supp(h) union {o_s:1<=s<t}`,

where the outputs are those produced by this same generator on the preceding prefixes. It is an **enumeration with replay** if every element of `supp(h)` occurs as an input at some finite round. A class is **limit-generatable with replay** if there is one generator `G` such that, for every target `h` in the class and every enumeration with replay for `h` and `G`, there is a finite `T` such that

`o_t in supp(h) minus {x_1,...,x_t}` for every `t>=T`.

The success time may depend on the target and the enumeration. An **ordinary enumeration** has every input in the target support and eventually presents every element of that support. Ordinary limit generation uses the same quantifiers and output requirement, restricted to ordinary enumerations.

### Information access

For the first clause, a nonempty countable class is supplied as an indexed list `H={h_1,h_2,...}`, with repetitions allowed, together with an enumeration `X={y_1,y_2,...}` of distinct domain elements. Class evaluation is available only through the oracle

`M(i,x)=h_i(x)`.

A query specifies both the class-member index `i` and the domain element `x`. The index of the hidden target is not supplied, and there is no oracle identifying membership in that hidden target. The algorithm must terminate each round after finitely many operations and finitely many such queries.

For the second clause, generators have no oracle input. For the fixed class, they may be arbitrary, possibly computationally unbounded, deterministic maps from finite input histories to domain elements.

## Task

Prove the following integrated theorem.

1. Every countable UUS binary hypothesis class on a countable domain is limit-generatable with replay. For nonempty classes, one algorithm achieves this for all indexed classes and enumerated domains using only the class-membership access specified above.

2. The following explicit class is uncountable and UUS, is ordinarily limit-generatable without queries, but is not limit-generatable with replay in that same no-query setting.

Let `X'=Z union {mu^n:n in N}`, where the markers `mu^n` are pairwise distinct symbols disjoint from `Z`. For each `b in N_0`, define families of integer supports

`H_1^b = {{b} union A union {x in Z:x>j}: A subseteq Z, j in Z, j>b}`,

`H_2^b = {{x in Z:x<b} union A: A subseteq Z minus {b}}`.

Set `M_b={mu^k:1<=k<=b}`. The class in question, identified with its supports, is

`H = {{mu^n:n in N}} union {L union M_b: b in N_0, L in H_1^b union H_2^b}`.

Show both the ordinary generation claim and the replay non-generation claim for this class.
