# Exercise 7: Linear Dependence Without Heavy Computation

## 1. Problem Statement

Given
$$u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).$$
Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

## 2. Theoretical Background and Concepts

1. **Linear Dependence and Independence:**
   A set of vectors $\{v_1, v_2, \dots, v_k\}$ in a vector space is **linearly dependent** if there exist scalars $c_1, c_2, \dots, c_k \in \mathbb{R}$, **not all zero**, such that:
   $$c_1 v_1 + c_2 v_2 + \dots + c_k v_k = \mathbf{0}$$
   Otherwise, if the only solution is $c_1 = c_2 = \dots = c_k = 0$, the vectors are **linearly independent**.

2. **Proportionality and Subset Property:**
   - Two vectors are linearly dependent if and only if one is a scalar multiple of the other (they are collinear/parallel).
   - **Key Theorem:** Any set of vectors that contains a linearly dependent subset is itself linearly dependent. Specifically, if $v = \alpha u$ for some scalar $\alpha$, then $c_1 u + c_2 v + c_3 w = \mathbf{0}$ is immediately satisfied by choosing $c_1 = \alpha$, $c_2 = -1$, and $c_3 = 0$ (which is a non-trivial combination since $c_2 = -1 \neq 0$).

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (1, 2, 3), \qquad v = (2, 4, 6), \qquad w = (0, 1, 1)$$

### Step 1: Identify the specific relation between $u$ and $v$
Comparing the coordinates of $u = (1, 2, 3)$ and $v = (2, 4, 6)$ component by component, we observe that every coordinate of $v$ is exactly twice the corresponding coordinate of $u$:
$$v = (2 \cdot 1,\, 2 \cdot 2,\, 2 \cdot 3) = 2(1, 2, 3) = 2u$$
Equivalently, $2u - v = \mathbf{0}$. Thus, $u$ and $v$ are collinear (proportional).

### Step 2: Decide whether the three vectors can be linearly independent
The three vectors $u, v, w$ **cannot be linearly independent**—they are **linearly dependent**.
Indeed, using the relation $2u - v = \mathbf{0}$, we can write a non-trivial linear combination of $u, v, w$ that equals the zero vector:
$$2u + (-1)v + 0w = \mathbf{0}$$
Since the coefficients $(c_1, c_2, c_3) = (2, -1, 0)$ are not all zero, the definition of linear dependence is satisfied immediately.

### Step 3: Explain why no long calculation is needed
Normally, to test three vectors in $\mathbb{R}^3$ for linear independence, one might set up a $3 \times 3$ homogeneous system of linear equations, perform Gaussian elimination, or compute a $3 \times 3$ determinant. However, no such calculation is needed here because:
1. By inspection, $\{u, v\}$ is already a linearly dependent pair ($v = 2u$), meaning $u$ and $v$ span only a $1$-dimensional line rather than a $2$-dimensional plane.
2. Adding a third vector $w$ to a set that already contains a redundant vector cannot remove that redundancy; any superset of a linearly dependent set is automatically linearly dependent (and 3 vectors spanning at most $\dim\operatorname{span}\{u,v,w\} \le 1 + 1 = 2 < 3$ dimensions cannot be linearly independent).

## 4. Verification and Consistency Checks

1. **Direct Verification of the Linear Combination:**
   Evaluate $2u - 1v + 0w$ explicitly:
   $$2(1, 2, 3) - 1(2, 4, 6) + 0(0, 1, 1) = (2, 4, 6) - (2, 4, 6) + (0, 0, 0) = (0, 0, 0) = \mathbf{0} \quad \checkmark$$

2. **Determinant / Cross-Product Check:**
   In $\mathbb{R}^3$, three vectors $u, v, w$ are linearly dependent if and only if their scalar triple product $(u \times v) \cdot w = 0$. Since $v = 2u$, the cross product of parallel vectors is:
   $$u \times v = u \times (2u) = 2(u \times u) = \mathbf{0}$$
   Therefore, $(u \times v) \cdot w = \mathbf{0} \cdot w = 0$, confirming that the parallelepiped spanned by $u, v, w$ has zero volume (the three vectors are coplanar, and in fact $u, v$ are collinear).
