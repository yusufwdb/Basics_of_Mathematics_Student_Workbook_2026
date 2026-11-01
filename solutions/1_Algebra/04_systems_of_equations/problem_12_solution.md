# Exercise 12: Homogeneous System

## 1. Problem Statement
Solve
$$\begin{cases}x+2y-z=0,\\2x+4y-2z=0,\\x-y+2z=0.\end{cases}$$
Give all solutions in parametric form and explain why $(0,0,0)$ always satisfies a homogeneous system.

## 2. Theoretical Background and Concepts
A system of linear equations is called **homogeneous** if all constant terms on the right-hand side are zero:
$$A\mathbf{x} = \mathbf{0}.$$
Key properties of homogeneous systems:
1. **Always Consistent (Trivial Solution):** Every homogeneous system $A\mathbf{x} = \mathbf{0}$ is guaranteed to be consistent because the zero vector $\mathbf{x} = \mathbf{0} = (0, 0, \dots, 0)^T$ always satisfies $A\mathbf{0} = \mathbf{0}$. This solution is called the **trivial solution**.
2. **Non-trivial Solutions:** A homogeneous system in $n$ unknowns has non-trivial (non-zero) solutions if and only if there is at least one free variable, i.e., $\operatorname{rank}(A) < n$ (which for a square $n \times n$ matrix is equivalent to $\det(A) = 0$). In that case, it has **infinitely many solutions** forming a linear subspace (the null space or kernel of $A$).

## 3. Detailed Step-by-Step Solution

### Step 1: Explain why $(0,0,0)$ always satisfies a homogeneous system
In any homogeneous system in three variables,
$$\begin{cases}
a_{11}x + a_{12}y + a_{13}z = 0, \\
a_{21}x + a_{22}y + a_{23}z = 0, \\
a_{31}x + a_{32}y + a_{33}z = 0,
\end{cases}$$
every term on the left-hand side of every equation is a product of a coefficient $a_{ij}$ and one of the unknowns $x, y, z$, while every right-hand side is $0$. Substituting $(x, y, z) = (0, 0, 0)$ makes every product $a_{ij} \cdot 0 = 0$, so the left-hand side of each equation evaluates to $0 + 0 + 0 = 0$, which automatically equals the right-hand side $0$ (in matrix form, $A\mathbf{0} = \mathbf{0}$ for any matrix $A$). Geometrically, every plane $a_{i1}x + a_{i2}y + a_{i3}z = 0$ passes through the origin $(0,0,0)$.

### Step 2: Set up the augmented matrix and perform Gaussian elimination
Write the augmented matrix $[A \mid \mathbf{0}]$:
$$\left[\begin{array}{ccc|c}
1 & 2 & -1 & 0 \\
2 & 4 & -2 & 0 \\
1 & -1 & 2 & 0
\end{array}\right]$$
Eliminate $x$ from Row 2 and Row 3 using $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$:
- New $R_2$: $(2-2(1),\; 4-2(2),\; -2-2(-1) \mid 0) = (0, 0, 0 \mid 0)$
- New $R_3$: $(1-1,\; -1-2,\; 2-(-1) \mid 0) = (0, -3, 3 \mid 0)$

$$\left[\begin{array}{ccc|c}
1 & 2 & -1 & 0 \\
0 & 0 & 0 & 0 \\
0 & -3 & 3 & 0
\end{array}\right]$$
Swap Row 2 and Row 3 ($R_2 \leftrightarrow R_3$) and divide the new Row 2 by $-3$ ($R_2 \leftarrow -\frac{1}{3}R_2$):
$$\left[\begin{array}{ccc|c}
1 & 2 & -1 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]$$

### Step 3: Express all solutions in parametric form
- The pivots are in Column 1 ($x$) and Column 2 ($y$), so $\operatorname{rank}(A) = 2 < 3$.
- Column 3 ($z$) has no pivot, so **$z$ is a free variable**.

Let $z = t$, where $t \in \mathbb{R}$ is an arbitrary real parameter:
1. **From Row 2:**
   $$y - z = 0 \implies y = z = t.$$
2. **From Row 1:**
   $$x + 2y - z = 0 \implies x = -2y + z = -2t + t = -t.$$

Therefore, all solutions in parametric form are given by:
$$\begin{cases}
x = -t, \\
y = t, \\
z = t,
\end{cases} \quad t \in \mathbb{R},$$
or in vector form:
$$\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}-t\\t\\t\end{pmatrix} = t\begin{pmatrix}-1\\1\\1\end{pmatrix}, \quad t \in \mathbb{R}.$$
*(Notice that setting $t = 0$ recovers the trivial solution $(0, 0, 0)$.)*

## 4. Verification and Consistency Checks
We substitute $(x, y, z) = (-t, t, t)$ into all three original equations for any $t \in \mathbb{R}$:
1. **Equation 1:**
   $$x + 2y - z = (-t) + 2(t) - t = -t + 2t - t = 0 \quad \checkmark.$$
2. **Equation 2:**
   $$2x + 4y - 2z = 2(-t) + 4(t) - 2(t) = -2t + 4t - 2t = 0 \quad \checkmark.$$
3. **Equation 3:**
   $$x - y + 2z = (-t) - t + 2(t) = -2t + 2t = 0 \quad \checkmark.$$

Every equation is satisfied identically for all $t \in \mathbb{R}$.
