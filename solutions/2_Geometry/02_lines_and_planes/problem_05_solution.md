# Exercise 5: Relative Position of Two Lines

## 1. Problem Statement

Analyze the position of
$$L_1:(x,y,z)=(1,1,0)+t(1,2,1),$$
$$L_2:(x,y,z)=(2,0,1)+s(0,1,-1).$$
If they intersect, give the intersection point. If not, determine whether they are parallel or skew. Justify the classification.

## 2. Theoretical Background and Concepts

In $\mathbb{R}^3$, two lines $L_1: p_1 + t v_1$ and $L_2: p_2 + s v_2$ can have one of four relative positions:

1. **Collinear (Identical) or Strictly Parallel:**
   This occurs if and only if their direction vectors are proportional ($v_1 = \lambda v_2$ for some $\lambda \neq 0$, or $v_1 \times v_2 = \mathbf{0}$). If $p_2 \in L_1$, the lines are identical; otherwise, they are strictly parallel (coplanar with no intersection).
2. **Intersecting at a Unique Point:**
   The direction vectors $v_1$ and $v_2$ are not proportional, **and** the system of three coordinate equations $p_1 + t v_1 = p_2 + s v_2$ in the two unknowns $(t, s)$ is **consistent** (has a unique solution $(t, s)$). In this case, the lines are coplanar and meet at one point.
3. **Skew (Non-coplanar):**
   The direction vectors $v_1$ and $v_2$ are not proportional, **and** the system $p_1 + t v_1 = p_2 + s v_2$ is **inconsistent** (no pair $(t, s)$ satisfies all three coordinate equations simultaneously). Equivalently, $(p_2 - p_1) \cdot (v_1 \times v_2) \neq 0$.

## 3. Detailed Step-by-Step Solution

Given lines:
$$L_1: (x, y, z) = (1, 1, 0) + t(1, 2, 1) = (1 + t,\, 1 + 2t,\, t)$$
$$L_2: (x, y, z) = (2, 0, 1) + s(0, 1, -1) = (2,\, s,\, 1 - s)$$

### Step 1: Check whether the direction vectors are parallel
The direction vectors are:
$$v_1 = (1, 2, 1), \qquad v_2 = (0, 1, -1)$$
Since the first coordinate of $v_1$ is $1 \neq 0$ while the first coordinate of $v_2$ is $0$, there is no scalar $\lambda$ such that $v_1 = \lambda v_2$. Thus, $L_1$ and $L_2$ are **not parallel** (and not identical). They must either **intersect at one point** or be **skew**.

### Step 2: Test for intersection by equating coordinates
Set $(1 + t,\, 1 + 2t,\, t) = (2,\, s,\, 1 - s)$ to obtain the system of three linear equations in two unknowns $t$ and $s$:
$$\begin{cases} 1 + t = 2 & \text{(1)} \\ 1 + 2t = s & \text{(2)} \\ t = 1 - s & \text{(3)} \end{cases}$$

From equation (1), we immediately find $t$:
$$1 + t = 2 \implies t = 1$$
Substitute $t = 1$ into equation (2) to find $s$:
$$s = 1 + 2(1) = 3$$
Now substitute $(t, s) = (1, 3)$ into the third equation (3) to check whether the system is consistent:
- Left-hand side of (3): $t = 1$
- Right-hand side of (3): $1 - s = 1 - 3 = -2$

Since $1 \neq -2$, the third equation is **contradicted**! Therefore, the system has **no solution**, which means $L_1$ and $L_2$ have no common point.

### Step 3: Classification and justification
Because the direction vectors $v_1 = (1, 2, 1)$ and $v_2 = (0, 1, -1)$ are not parallel, and the lines do not intersect ($L_1 \cap L_2 = \emptyset$), the lines $L_1$ and $L_2$ are **skew lines** (they do not lie in any common plane and never meet).

## 4. Verification and Consistency Checks

**Scalar Triple Product Coplanarity Check:**
Two lines $L_1: p_1 + t v_1$ and $L_2: p_2 + s v_2$ are skew if and only if the vectors $p_2 - p_1$, $v_1$, and $v_2$ are linearly independent (non-coplanar), i.e., $(p_2 - p_1) \cdot (v_1 \times v_2) \neq 0$.
Let us compute:
- $p_2 - p_1 = (2, 0, 1) - (1, 1, 0) = (1, -1, 1)$
- $v_1 \times v_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 1 \\ 0 & 1 & -1 \end{vmatrix} = (-2 - 1,\, 0 - (-1),\, 1 - 0) = (-3, 1, 1)$
- Scalar triple product:
  $$(p_2 - p_1) \cdot (v_1 \times v_2) = (1)(-3) + (-1)(1) + (1)(1) = -3 - 1 + 1 = -3 \neq 0 \quad \checkmark$$

Since the scalar triple product is $-3 \neq 0$ (and the minimum distance between the two skew lines is $\frac{|(p_2 - p_1) \cdot (v_1 \times v_2)|}{\|v_1 \times v_2\|} = \frac{3}{\sqrt{11}} > 0$), this independently confirms that $L_1$ and $L_2$ are skew.
