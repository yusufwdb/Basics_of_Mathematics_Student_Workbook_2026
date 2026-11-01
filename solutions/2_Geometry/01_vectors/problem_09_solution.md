# Exercise 9: Cross Product as a Perpendicular Direction

## 1. Problem Statement

For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

## 2. Theoretical Background and Concepts

1. **Cross Product (Vector Product) in $\mathbb{R}^3$:**
   For two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, their cross product is the vector defined by the symbolic determinant:
   $$u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = (u_2 v_3 - u_3 v_2,\, u_3 v_1 - u_1 v_3,\, u_1 v_2 - u_2 v_1)$$

2. **Key Geometric and Algebraic Properties:**
   - **Mutual Orthogonality:** $u \times v$ is perpendicular to both $u$ and $v$, hence perpendicular to the plane spanned by $u$ and $v$:
     $$(u \times v) \cdot u = 0 \quad \text{and} \quad (u \times v) \cdot v = 0$$
   - **Anticommutativity (Skew-Symmetry):** Swapping the order of the factors reverses the orientation of the cross product (by the right-hand rule) while keeping its magnitude and line of action unchanged:
     $$v \times u = -(u \times v)$$

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (1, 2, 0), \qquad v = (0, 1, 3)$$

### Step 1: Compute $u \times v$
Using the determinant expansion for $u = (1, 2, 0)$ and $v = (0, 1, 3)$:
$$u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 3 \end{vmatrix} = \left(\begin{vmatrix} 2 & 0 \\ 1 & 3 \end{vmatrix},\, -\begin{vmatrix} 1 & 0 \\ 0 & 3 \end{vmatrix},\, \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix}\right)$$
Compute each $2 \times 2$ minor:
- First component: $(2)(3) - (0)(1) = 6 - 0 = 6$
- Second component: $-\big((1)(3) - (0)(0)\big) = -3$
- Third component: $(1)(1) - (2)(0) = 1 - 0 = 1$

Thus:
$$u \times v = (6, -3, 1)$$

### Step 2: Check perpendicularity to both $u$ and $v$ using dot products
Compute $(u \times v) \cdot u$:
$$(u \times v) \cdot u = (6, -3, 1) \cdot (1, 2, 0) = (6)(1) + (-3)(2) + (1)(0) = 6 - 6 + 0 = 0$$
Compute $(u \times v) \cdot v$:
$$(u \times v) \cdot v = (6, -3, 1) \cdot (0, 1, 3) = (6)(0) + (-3)(1) + (1)(3) = 0 - 3 + 3 = 0$$
Since both dot products are $0$, $u \times v = (6, -3, 1)$ is orthogonal to both $u$ and $v$.

### Step 3: Compute $v \times u$ and compare the results
Computing $v \times u$ directly from the determinant with the rows of $v$ and $u$ swapped:
$$v \times u = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 1 & 3 \\ 1 & 2 & 0 \end{vmatrix} = \big((1)(0) - (3)(2),\, (3)(1) - (0)(0),\, (0)(2) - (1)(1)\big) = (-6, 3, -1)$$
**Comparison:**
We see that:
$$v \times u = (-6, 3, -1) = -(6, -3, 1) = -(u \times v)$$
Both $u \times v$ and $v \times u$ have the exact same length ($\sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{46}$) and lie along the exact same line perpendicular to the plane of $u$ and $v$, but they point in **opposite orientations** (in accordance with the right-hand rule and the anticommutativity of the cross product).

## 4. Verification and Consistency Checks

**Lagrange's Identity Check:**
For any two vectors $u, v \in \mathbb{R}^3$, Lagrange's identity states that $\|u \times v\|^2 = \|u\|^2\|v\|^2 - (u \cdot v)^2$. Let us check both sides:
- Left-hand side:
  $$\|u \times v\|^2 = 6^2 + (-3)^2 + 1^2 = 36 + 9 + 1 = 46$$
- Right-hand side:
  $$\|u\|^2 = 1^2 + 2^2 + 0^2 = 5, \qquad \|v\|^2 = 0^2 + 1^2 + 3^2 = 10, \qquad u \cdot v = 1(0) + 2(1) + 0(3) = 2$$
  $$\|u\|^2\|v\|^2 - (u \cdot v)^2 = (5)(10) - 2^2 = 50 - 4 = 46$$
Both sides equal $46$, confirming that the magnitude and components of $u \times v$ and $v \times u$ are completely accurate.
