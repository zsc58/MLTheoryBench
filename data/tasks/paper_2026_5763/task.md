# Problem

## Setup

Let A={0,1,...,n}, where 0 is an always-available no-choice alternative. A query pair is a pair (a,S), where a is in A and S is a subset of {1,...,n}. It is a valid transaction when a is in S union {0}.

Assign every i in A a positive rational attraction w_i. Let G_i be independent standard Gumbel random variables and set

U_i = log(w_i)+G_i.

For a query pair (a,S), define

E(a,S)={U_a>U_b for every b in (S union {0}) excluding a}

when a is in S union {0}, and define E(a,S) to be empty otherwise.

For any finite collection C of query pairs, let E_C be the intersection of its query events and let p_C=Pr(E_C). A transaction history H is a finite collection consisting only of valid transactions. Whenever p_H>0, define the conditional choice probability

p_H(a,S)=Pr(E_H intersect E(a,S))/p_H.

For a finite collection C, its preference digraph G_C has vertex set A and an arc a to b for every pair (a,S) in C and every b in (S union {0}) excluding a. Call a transaction history H acyclic when G_H is acyclic. Finally, define the attraction ratio

R=max_i w_i/min_i w_i.

Inputs are encoded explicitly by the rational attractions, the history, and the query pair.

## Task

Prove the following computational theorem.

1. Exact computation of p_H(a,S) is #P-hard under polynomial-time Turing reductions, even when H is acyclic, p_H>0, and all attractions are positive rationals.

2. For every acyclic transaction history H and epsilon,delta in (0,1), there is a randomized algorithm which, for any query pair (a,S), returns an estimate qhat such that

Pr[(1-epsilon)p_H(a,S) <= qhat <= (1+epsilon)p_H(a,S)] >= 1-delta.

Its runtime is polynomial in n, R, 1/epsilon, log(1/delta), and the input encoding length. It returns zero exactly when the queried event is impossible. Consequently, if R is polynomially bounded in n, conditional choice probability admits a fully polynomial randomized approximation scheme.
