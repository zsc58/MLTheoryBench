# Problem

## Setup

Let n>=2 be an integer, and let x_1,...,x_n be points in a finite-dimensional Euclidean space, with repetitions allowed. Let C_1^*,C_2^* be a partition of {1,...,n} into two nonempty cells, with anchors a_1,a_2 in the same space. Write n_j=|C_j^*| and b=min(n_1,n_2)/n, so 0<b<=1/2. Let R>=0 be finite. Every point indexed by C_j^* lies in the closed Euclidean ball of radius R around a_j. Let S=||a_1-a_2|| and assume S>2R; set m=S-2R>0. In the absolute-loss statement, all data points, anchors, and feasible centers lie on one common real line.

For a partition C=(C_1,C_2) of {1,...,n} into two nonempty cells and centers z_1,z_2, define

L_g(C,z)=sum_{j=1}^2 sum_{i in C_j} g(||x_i-z_j||),

and V_g(C)=inf_{z_1,z_2} L_g(C,z), with centers in the ambient Euclidean space, or on the line in the absolute-loss case. Consider squared loss g(r)=r^2 and absolute loss g(r)=r. Partitions differing only by a swap of cell labels are identified. The label-invariant misclassification rate is

p(C,C^*)=1-max_{pi in Pi_2} (1/n) sum_{j=1}^2 |C_j intersect C^*_{pi(j)}|,

where Pi_2 is the set of permutations of {1,2}.

## Task

Prove the following integrated theorem.

1. If bm^2>4R^2, then C^* is the unique minimizer of V_{r^2} up to swapping labels. When R>0, this condition is equivalent to S/R>2+2/sqrt(b).
2. In the one-dimensional setup, if bm>R, then C^* is the unique minimizer of V_r up to swapping labels. When R>0, this condition is equivalent to S/R>2+1/b. This assertion does not additionally assume the squared-loss condition.

Show also that these dependences on b are order-wise necessary, in the following precise sense. There exist universal constants c>0 and b_0 in (0,1/2) such that, for every rational b in (0,b_0] and every R>0:

- for every m with 0<m<=cR/sqrt(b), there is a finite two-ball configuration with balance b, radius bound R, and anchor separation 2R+m for which C^* is not a minimizer of V_{r^2};
- for every m with 0<m<=cR/b, there is such a configuration on a real line for which C^* is not a minimizer of V_r.

The sample size may depend on the chosen parameters. Construct configurations and verify the claimed failures.
