# Reference Proof

## Proof Structure

The proof has four parts. First, solve the affine three-step return maps for the first and second Adam moments and establish geometric convergence to their unique period-three states. Second, show that at the balanced slope a=2 the limiting normalized directions have strictly negative sum, and use continuity to choose a=2+delta with the required signs and strict negative drift. Third, compare three projected updates with the projection of their total displacement; the negative first direction and positive later directions yield a positive period displacement, and the divergent subsampled step-size sum forces the period-start iterates to reach the right endpoint. Finally, identify the best fixed comparator from the cumulative gradients and compute the Cesaro limit of the regret.

## Complete Proof

Fix b,q,epsilon and a positive step-size sequence as in the statement. Write P(z)=min(1,max(-1,z)). For the three-periodic gradients a,-1,-1, the moment recursions are independent of the iterates.

Let M_i denote the limiting first moment in phase i. If M_1 is the phase-one value, two subsequent updates give
M_2=b M_1-(1-b) and M_3=b^2 M_1-(1-b)(1+b).
The next phase-one update is the affine return map
Phi_b(M_1)=b^3 M_1+(1-b)(a-b-b^2).
Its contraction factor is b^3<1. Hence it has one fixed point and iteration converges geometrically to it (with the immediate-transient interpretation when b=0). Solving gives
M_1=(a-b-b^2)/(1+b+b^2),
M_2=(ab-b^2-1)/(1+b+b^2),
M_3=(ab^2-b-1)/(1+b+b^2).
Thus m_{3k+i}=M_i+O(b^{3k}) for i=1,2,3.

Applying the same calculation to the squared gradients gives the return map
Psi_q(V_1)=q^3 V_1+(1-q)(a^2+q+q^2).
Therefore
V_1=(a^2+q+q^2)/(1+q+q^2),
V_2=(a^2q+q^2+1)/(1+q+q^2),
V_3=(a^2q^2+q+1)/(1+q+q^2),
and v_{3k+i}=V_i+O(q^{3k}).

Define H_i(a)=M_i(a)/(sqrt(V_i(a))+epsilon) and S(a)=H_1(a)+H_2(a)+H_3(a). At a=2, direct substitution gives M_1>0, M_2<0, M_3<0 and M_1+M_2+M_3=0. Put A=-M_2>0 and B=-M_3>0, so M_1=A+B. The displayed V formulas imply
V_1-V_2=3(1-q)/(1+q+q^2)>0,
V_1-V_3=3(1-q^2)/(1+q+q^2)>0.
Consequently sqrt(V_1)+epsilon is strictly larger than each of the other two denominators, and
S(2)=A(1/(sqrt(V_1)+epsilon)-1/(sqrt(V_2)+epsilon))
     +B(1/(sqrt(V_1)+epsilon)-1/(sqrt(V_3)+epsilon))<0.
All these rational expressions have positive denominators and are continuous in a. Hence there is delta in (0,1] (depending only on b,q,epsilon) such that, for a=2+delta,
S(a)<0, M_1(a)>0, M_2(a)<0, and M_3(a)<0.

Let h_t=m_t/(sqrt(v_t)+epsilon), z_k=x_{3k+1}, and u_{k,i}=-alpha_{3k+i}h_{3k+i}. The moment convergence just proved implies h_{3k+i}->H_i(a). After discarding finitely many periods, u_{k,1}<=0 and u_{k,2},u_{k,3}>=0. Since alpha_{t+1}/alpha_t->1, the three step sizes in one period are asymptotically equal, and therefore
U_k:=u_{k,1}+u_{k,2}+u_{k,3}
 =alpha_{3k+1}(-S(a)+o(1)).
Because S(a)<0, there is c>0 such that U_k>=c alpha_{3k+1} for all sufficiently large k.

For completeness, if u_1<=0 and u_2,u_3>=0, then for every x in [-1,1],
P(P(P(x+u_1)+u_2)+u_3)>=P(x+u_1+u_2+u_3).
Indeed P(x+u_1)>=x+u_1. For w>=0 and any z, monotonicity of P gives P(P(z)+w)>=P(z+w): if z<=1 this follows from P(z)>=z, while if z>1 both sides equal 1. Applying this twice proves the displayed inequality. Thus, for all large k,
z_{k+1}>=min(1,z_k+c alpha_{3k+1}).

The ratio assumption implies the sums over phase-one indices diverge: the three terms in each period are eventually comparable, so divergence of sum alpha_t implies divergence of sum_k alpha_{3k+1}. Iterating the last inequality therefore makes z_k reach 1 after finitely many periods; once z_k=1, the same inequality forces every later z_k to remain 1.

It remains to pass from period starts to all iterates. Since |g_t|<=3 and v_t>=1-q (the latter follows from v_t=qv_{t-1}+(1-q)g_t^2 and |g_t|>=1), we have |m_t|<=3 and hence |h_t|<=3/sqrt(1-q). Each within-period displacement is at most a constant times alpha_t, which tends to zero. Since z_k->1, it follows that x_t->1.

Let G_T=sum_{t=1}^T g_t. For T=3k,3k+1,3k+2 respectively,
G_T=k delta, k delta+a, k delta+a-1,
so G_T>0 for every positive horizon. Therefore the best fixed decision in [-1,1] is always -1. With R_T as defined in the setup,
R_T=sum_t g_t x_t+G_T
   =2G_T+sum_t g_t(x_t-1).
The gradients are bounded and x_t->1, so the Cesaro mean of the second sum divided by T tends to zero. Also G_T/T->delta/3. Consequently R_T/T->2delta/3>0.
