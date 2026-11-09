# Reference Proof

Fix the current parameter values and regard J as a function of the free coordinates of U together with all coordinates of V and T. Because the network is a finite composition of affine maps, finite maxima and minima, and smooth softmax cross-entropy operations, J is locally Lipschitz and piecewise continuously differentiable. Use the standard piecewise-smooth characterization of the Clarke subdifferential: select a differentiable stratum incident to the current parameter and take the limit of its ordinary gradient. This gives a valid element of the Clarke subdifferential.

Choose such a stratum and let n* be the sample whose loss is active on it. By continuity, J = ell_n* at the current parameter. For every output class d, let h_d be the active maximizer of g_h(x_n*) + T_{h,d} on the selected stratum. For every hidden unit h, choose the single active minimizer i_h of lambda_i(x_n*) + V_{i,h} on that same stratum. This common choice is important because each g_h is shared by all output classes. For each class write i_d = i_{h_d}. All these selected indices remain active at the current parameter.

Write p_d for p_d(x_n*) and set a_d = p_d - 1{d = y_n*}. The ordinary derivative on the selected stratum with respect to the output logit z_d is a_d. Therefore define

G2_{h,d} = a_d if h = h_d, and G2_{h,d} = 0 otherwise.

Only the coordinates (h_d,d), one per class, can be nonzero, so |supp(G2)| <= C.

Propagating through the selected output maxima and the common selected hidden minima gives

G1_{i,h} = 1{i = i_h} sum_{d:h_d=h} a_d.

Thus the support of G1 is contained in the set {(i_{h_d},h_d): d = 1,...,C}, which has at most C elements. Contributions from classes selecting the same pair are aggregated at that one coordinate.

For the first layer, only coordinates in the free mask F are trainable. Since lambda_i(x_n*) = sum_p U_{i,p}x_{n*,p}, the selected-branch derivative is

G0_{i,p} = 1{(i,p) in F} x_{n*,p} sum_{d:i_{h_d}=i} a_d.

Every selected row i_{h_d} contains at most one free coordinate in F. There are at most C selected rows, so |supp(G0)| <= C. Coincident rows or cancellations can only reduce the support.

The vector obtained as the limit of the ordinary gradient on the selected differentiable stratum is a valid Clarke subgradient of J. Hence G=(G0,G1,G2) is a valid nonsmooth subgradient, and every trainable layer has at most C nonzero entries.
