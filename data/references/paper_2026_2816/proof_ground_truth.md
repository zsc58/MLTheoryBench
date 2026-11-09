# Reference Proof

Let U=(0,1)^d and write psi_k=Phi_{-j,k}. All integrals involving Sobolev seminorms below are over U. Fix an admissible j, so n=|I(j)|>=1. If the endpoints of the support of phi are a<b, each psi_k has L^2(R^d) norm one, support diameter at most D2^{-j}, where D=sqrt(d)(b-a), and squared essential supremum at most 2^{dj}||phi||_infty^{2d}. The convex hull S_k of its support, intersected with U, is a bounded convex set of volume (b-a)^d2^{-dj}; boundary points do not affect any integral. Compact support also gives a constant M, depending only on phi and d, for which sum_{k in I(j)} 1_{S_k}(x)<=M almost everywhere in U.

Let H=span{psi_k:k in I(j)} in L^2(R^d). The boundedness of f ensures that f psi_k belongs to L^2. The projection-DPP variance identity is

Var[Lambda_S(f)] = sum_{k in I(j)} ||P_{H^perp}(f psi_k)||_2^2.

For completeness, expanding the DPP's first two correlation functions gives Var[Lambda_S(f)]=sum_k ||f psi_k||_2^2-sum_{k,l}|<f psi_k,psi_l>|^2, which is the displayed identity. For any scalar a_k, a_k psi_k belongs to H. Contractivity of the projection therefore gives

Var[Lambda_S(f)] <= sum_{k in I(j)} ||(f-a_k)psi_k||_2^2.  (1)

If f is Holder, choose x_k in the support of psi_k and set a_k=f(x_k). The global Holder condition and normalization of psi_k yield

||(f-a_k)psi_k||_2^2 <= |f|_{C^{0,s}}^2 (D2^{-j})^{2s}.

Summing (1) gives Var[Lambda_S(f)]<=C|f|_{C^{0,s}}^2 n2^{-2js}.

Suppose 0<s<1 and f belongs to H^s(U). Set a_k=|S_k|^{-1}int_{S_k}f. Jensen's inequality, followed by ||x-y||<=diam(S_k), proves the required local fractional estimate directly:

int_{S_k}|f-a_k|^2 <= |S_k|^{-1} int_{S_k}int_{S_k}|f(x)-f(y)|^2 dx dy
 <= diam(S_k)^{d+2s}|S_k|^{-1}|f|_{H^s(S_k)}^2
 <= C 2^{-2js}|f|_{H^s(S_k)}^2.  (2)

The constant in (2) is uniform for 0<s<1: D^{d+2s}/(b-a)^d is bounded uniformly on that interval. Using the bound on ||psi_k||_infty in (1), then bounded overlap, gives

Var[Lambda_S(f)] <= C2^{(d-2s)j}sum_k |f|_{H^s(S_k)}^2 <= CM^2 2^{(d-2s)j}|f|_{H^s(U)}^2.

Indeed, at each pair (x,y), at most M^2 of the integrands defining the local fractional seminorms contribute.

Finally, suppose f belongs to H^1(U). The Payne-Weinberger inequality states that for a bounded convex open set Q and g in H^1(Q), int_Q|g-g_Q|^2 <= diam(Q)^2 pi^{-2}int_Q||nabla g||^2. Apply it to the interior of S_k, whose boundary has measure zero, with a_k the mean of f there. Its hypotheses hold because S_k is bounded and convex and the restriction of f belongs to H^1(S_k). As in the fractional case, the scaling bound and bounded overlap yield

Var[Lambda_S(f)] <= C2^{(d-2)j}sum_k int_{S_k}||nabla f||^2 <= CM2^{(d-2)j}||nabla f||_{L^2(U)}^2.

For the fixed scaling function, the number of permitted integer translates in each coordinate is asymptotic to 2^j as j increases. There are only finitely many smaller admissible scales, and each has n>=1. Consequently c2^{dj}<=n<=C2^{dj} on all admissible scales, with positive constants depending only on phi and d. Converting each displayed scale bound using this comparison proves Var[Lambda_S(f)]<=C|f|_s^2 n^{1-2s/d} in all three cases. The constants can be chosen uniformly over 0<s<=1.
