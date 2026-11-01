# Exercise 13: Does Every Equation Add New Information?

## 1. Problem Statement
Consider the system
$$x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.$$
Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

## 2. Theoretical Background and Concepts
In a system of linear equations, an equation is **redundant** (or **linearly dependent** on the others) if it can be obtained as a linear combination of the remaining equations.
- Removing a redundant equation does **not** change the solution set of the system.
- During **Gaussian elimination**, a redundant equation manifests as an entire row of zeros $[0 \;\; 0 \;\; \dots \;\; 0 \mid 0]$ ($0 = 0$), because subtracting the appropriate linear combination of earlier rows completely cancels both its left-hand and right-hand sides.
- Consequently, the number of truly independent equations is $\operatorname{rank}(A) = \operatorname{rank}([A \mid b])$, which here is strictly less than the number of written equations.

## 3. Detailed Step-by-Step Solution

### Step 1: Show directly by calculation how one equation follows from the others
Label the three given equations as:
$$\begin{aligned}
(E_1): \quad & x_1 + x_2 = 10, \\
(E_2): \quad & x_2 + x_3 = 8, \\
(E_3): \quad & x_1 - x_3 = 2.
\end{aligned}$$
Subtract Equation $(E_2)$ from Equation $(E_1)$:
$$(E_1) - (E_2): \quad (x_1 + x_2) - (x_2 + x_3) = 10 - 8.$$
Simplifying both sides (since $x_2 - x_2 = 0$):
$$x_1 - x_3 = 2,$$
which is **literally Equation $(E_3)$**!

Therefore, **not all three equations are independently necessary**: Equation $(E_3)$ is a direct algebraic consequence of $(E_1)$ and $(E_2)$ (specifically, $E_3 = E_1 - E_2$) and adds **no new information** to the system. Any pair of the three equations completely describes the exact same solution set.

### Step 2: Solve the system using Gaussian elimination
Write the augmented matrix of the system:
$$\left[\begin{array}{ccc|c}
1 & 1 & 0 & 10 \\
0 & 1 & 1 & 8 \\
1 & 0 & -1 & 2
\end{array}\right]$$
1. Eliminate $x_1$ from Row 3 using $R_3 \leftarrow R_3 - R_1$:
   $$\left[\begin{array}{ccc|c}
   1 & 1 & 0 & 10 \\
   0 & 1 & 1 & 8 \\
   0 & -1 & -1 & -8
   \end{array}\right]$$
2. Eliminate $x_2$ from Row 3 using $R_3 \leftarrow R_3 + R_2$:
   $$\left[\begin{array}{ccc|c}
   1 & 1 & 0 & 10 \\
   0 & 1 & 1 & 8 \\
   0 & 0 & 0 & 0
   \end{array}\right]$$
   *(Notice that Row 3 becomes $[0 \;\; 0 \;\; 0 \mid 0]$ via $R_3 - R_1 + R_2 = 0$, confirming that $E_3 = E_1 - E_2$.)*

### Step 3: Write the parametric solution set
From the row echelon form, the pivots are in Column 1 ($x_1$) and Column 2 ($x_2$), while Column 3 ($x_3$) has no pivot. Thus, $x_3 = t \in \mathbb{R}$ is a **free variable**:
1. From Row 2:
   $$x_2 + x_3 = 8 \implies x_2 = 8 - t.$$
2. From Row 1:
   $$x_1 + x_2 = 10 \implies x_1 = 10 - x_2 = 10 - (8 - t) = 2 + t.$$

Thus, the complete solution set is:
$$\begin{cases}
x_1 = 2 + t, \\
x_2 = 8 - t, \\
x_3 = t,
\end{cases} \quad t \in \mathbb{R}, \qquad \text{or} \qquad \begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} = \begin{pmatrix}2\\8\\0\end{pmatrix} + t\begin{pmatrix}1\\-1\\1\end{pmatrix}, \quad t \in \mathbb{R}.$$

## 4. Verification and Consistency Checks
Substitute $(x_1, x_2, x_3) = (2 + t, 8 - t, t)$ into all three original equations:
1. **Equation 1:** $x_1 + x_2 = (2 + t) + (8 - t) = 10 \quad \checkmark$.
2. **Equation 2:** $x_2 + x_3 = (8 - t) + t = 8 \quad \checkmark$.
3. **Equation 3:** $x_1 - x_3 = (2 + t) - t = 2 \quad \checkmark$.

Furthermore, solving the system consisting of **only the first two equations** $\begin{cases}x_1+x_2=10\\x_2+x_3=8\end{cases}$ immediately gives $x_2 = 8 - x_3$ and $x_1 = 10 - (8 - x_3) = 2 + x_3$, which yields the exact same solution set without using the third equation at all.
