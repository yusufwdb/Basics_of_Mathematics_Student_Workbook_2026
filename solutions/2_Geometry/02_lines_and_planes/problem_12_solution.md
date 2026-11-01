# Exercise 12: Intersection Line of Two Planes

## 1. Problem Statement

Find a parametric equation of the line that is the intersection of
$$x+y+z=3,\qquad x-y+z=1.$$
Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results.

## 2. Theoretical Background and Concepts

1. **Intersection of Two Non-Parallel Planes:**
   Two non-parallel planes $\Pi_1: n_1 \cdot x = d_1$ and $\Pi_2: n_2 \cdot x = d_2$ in $\mathbb{R}^3$ intersect in a line $L = \Pi_1 \cap \Pi_2$.

2. **Two Equivalent Ways to Find the Direction Vector $v$ of $L$:**
   - **Method A (Algebraic / System of Equations):** Solve the $2 \times 3$ linear system with one free parameter $t \in \mathbb{R}$. Expressing $(x, y, z) = p_0 + t v$ directly reveals both a point $p_0 \in L$ and a direction vector $v$.
   - **Method B (Geometric / Cross Product of Normals):** Because the line $L$ lies in $\Pi_1$, its direction vector $v$ is perpendicular to $n_1$ ($v \perp n_1$). Because $L$ also lies in $\Pi_2$, its direction vector $v$ is perpendicular to $n_2$ ($v \perp n_2$). Therefore, $v$ is parallel to the cross product of the two normal vectors:
     $$v_{\text{cross}} = n_1 \times n_2$$

## 3. Detailed Step-by-Step Solution

Given planes:
$$\Pi_1: x + y + z = 3, \qquad \Pi_2: x - y + z = 1$$

### Method 1: From the system of equations (Algebraic Approach)
Consider the system:
$$\begin{cases} x + y + z = 3 & \text{(1)} \\ x - y + z = 1 & \text{(2)} \end{cases}$$
Subtract equation (2) from equation (1) to eliminate $x$ and $z$:
$$(x + y + z) - (x - y + z) = 3 - 1 \implies 2y = 2 \implies y = 1$$
Substitute $y = 1$ back into equation (1):
$$x + 1 + z = 3 \implies x + z = 2$$
Let $z = t \in \mathbb{R}$ be the free parameter. Then $x = 2 - t$ and $y = 1$.
Writing $(x, y, z)$ in parametric vector form gives:
$$(x, y, z) = (2 - t,\, 1,\, t) = (2, 1, 0) + t(-1, 0, 1), \qquad t \in \mathbb{R}$$
From this parametric equation, we read off:
- A point on the line: $P_0 = (2, 1, 0)$
- Direction vector from the system:
  $$v_1 = (-1, 0, 1)$$

### Method 2: From the cross product of the normal vectors (Geometric Approach)
The normal vectors of $\Pi_1$ and $\Pi_2$ are:
$$n_1 = (1, 1, 1), \qquad n_2 = (1, -1, 1)$$
Compute their cross product $v_2 = n_1 \times n_2$:
$$v_2 = n_1 \times n_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix} = \big((1)(1) - (1)(-1),\, (1)(1) - (1)(1),\, (1)(-1) - (1)(1)\big) = (2, 0, -2)$$

### Comparison of the Results
Comparing $v_1 = (-1, 0, 1)$ from the system of equations and $v_2 = (2, 0, -2)$ from the cross product of the normals, we observe that:
$$v_2 = (2, 0, -2) = -2(-1, 0, 1) = -2v_1$$
Thus, $v_1$ and $v_2$ are **non-zero scalar multiples of each other** (collinear vectors). Both define the **exact same line direction** in $\mathbb{R}^3$; the factor of $-2$ simply corresponds to a rescaling and reversal of the parameter $t$ (specifically, replacing $t$ by $-2s$ in $(2, 1, 0) + t(-1, 0, 1)$ gives $(2, 1, 0) + s(2, 0, -2)$).

## 4. Verification and Consistency Checks

1. **Check that $(x, y, z) = (2 - t,\, 1,\, t)$ satisfies both plane equations for all $t \in \mathbb{R}$:**
   - Substitute into $\Pi_1: x + y + z = 3$:
     $$(2 - t) + 1 + t = 3 + 0t = 3 \quad \checkmark$$
   - Substitute into $\Pi_2: x - y + z = 1$:
     $$(2 - t) - 1 + t = 1 + 0t = 1 \quad \checkmark$$

2. **Check that $v_1 = (-1, 0, 1)$ and $v_2 = (2, 0, -2)$ are orthogonal to both $n_1$ and $n_2$:**
   - $v_1 \cdot n_1 = (-1)(1) + (0)(1) + (1)(1) = -1 + 0 + 1 = 0 \quad \checkmark$
   - $v_1 \cdot n_2 = (-1)(1) + (0)(-1) + (1)(1) = -1 + 0 + 1 = 0 \quad \checkmark$
   This confirms that the algebraic and geometric methods are completely consistent.
