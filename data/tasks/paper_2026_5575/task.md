# Problem

## Setup

Fix integers N >= 2 and 1 <= B <= floor(N/2). There are N sellers, one customer type, and a horizon of T positive-integer periods. Each period is a separate epoch: a customer arrives, an assortment is offered, and any resulting seller decision is completed before the next period. No proposal carries over between periods.

The preference vectors v=(v_i) and u=(u_i) are fixed but unknown to the policy, with

  0 < v_i <= 1,    0 < u_i <= 1    for i=1,...,N.

Both outside-option parameters are normalized to one.

In period t, a policy chooses an assortment A_t contained in {1,...,N}, with |A_t| <= B. Conditional on the preceding history and A_t, the customer's proposal Y_t takes values in A_t union {0}, with

  P(Y_t=i | history, A_t) = v_i / (1 + sum_{j in A_t} v_j),    i in A_t,
  P(Y_t=0 | history, A_t) = 1 / (1 + sum_{j in A_t} v_j).

The value Y_t=0 means that no proposal is made. If Y_t=i, that seller accepts the proposal with conditional probability u_i/(1+u_i); otherwise it rejects it. Write X_t=1 for an accepted proposal and X_t=0 otherwise. In particular, X_t=0 when Y_t=0. These are the conditional outcome laws given the preceding history and the current decisions.

The policy observes Y_t and X_t at the end of period t. It may use N, B, T, all preceding assortments and observed outcomes, and its own independent randomization. Its decision kernels must be the same for every unknown pair (u,v); it receives no initial observations or signals depending on that pair. These requirements define an admissible policy. No additional performance or exploration requirement is imposed.

A successful match earns one unit of reward. For a fixed feasible assortment A, let R_{u,v}(A) be the expected value of X in a single period in which A is offered, according to the outcome laws above. Define

  Reg_{pi,(u,v)}(T)
    = T max_{A subset of {1,...,N}, |A| <= B} R_{u,v}(A)
      - E_{u,v}^{pi}[sum_{t=1}^T X_t].

The expectation includes customer choices, seller decisions, and policy randomization.

## Task

Prove that, for every fixed N and B in the stated range, there is a constant c_{N,B}>0, depending only on N and B, such that for every positive integer T and every admissible policy pi,

  sup_{(u,v) in (0,1]^{2N}} Reg_{pi,(u,v)}(T)
      >= c_{N,B} [log(NT)]^2.

Here log is the natural logarithm. Establish the lower bound without assuming any paper-specific intermediate result.
