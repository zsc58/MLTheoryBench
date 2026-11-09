# Problem

## Setup

Fix integers n>=2 and k in {1,...,n-1}. Let (a_i,b_i)_{i=1}^n be fixed real pairs with sum_i a_i^2>0. For every size-k set S, assume

 sum_{i not in S} a_i^2 > 0.

Define

 theta=(sum_i a_i b_i)/(sum_i a_i^2),
 theta_{-S}=(sum_{i not in S}a_i b_i)/(sum_{i not in S}a_i^2),
 Delta(S)=theta-theta_{-S}.

Let M be the number of distinct values attained by Delta(S) over all size-k subsets S.

## Task

Prove the following integrated theorem: the exact maximization of Delta(S) over size-k subsets can be reduced to finitely many exact top-k linear subproblems, with a scalar-parameter procedure that terminates after at most M+1 updates from any initial scalar value and returns a globally maximizing subset. The top-k subproblems must be finite additive maximizations over selected indices, and all quantities used by the procedure must be constructed from the given pairs (a_i,b_i).
