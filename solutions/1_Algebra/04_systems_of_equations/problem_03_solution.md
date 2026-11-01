# Exercise 3: Inconsistent System

## 1. Problem Statement
Solve or show that the system is inconsistent:
$$\begin{cases}x+2y=3,\\2x+4y=7.\end{cases}$$
Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

## 2. Theoretical Background and Concepts
A system of linear equations is called **inconsistent** if its solution set is empty (it has **no solution**).
- **In Gaussian Elimination:** A system is inconsistent if and only if row reduction of the augmented matrix $[A \mid b]$ produces a **contradictory row** of the form
  $$\left[\begin{array}{cccc|c}0 & 0 & \dots & 0 & c\end{array}\right] \quad \text{with } c \neq 0,$$
  which translates to the impossible equation $0x_1 + 0x_2 + \dots + 0x_n = c$ ($0 = c$).
- **In terms of Ranks (Rouché–Capelli Theorem):** $\operatorname{rank}(A) < \operatorname{rank}([A \mid b])$.
- **Geometric Interpretation in $\mathbb{R}^2$:** The two equations represent two parallel, distinct lines with the same slope and normal vector $(1,2)$ (up to scaling), which never intersect.

## 3. Detailed Step-by-Step Solution

### Step 1: Write the augmented matrix $[A \mid b]$
$$\left[\begin{array}{cc|c}
1 & 2 & 3 \\
2 & 4 & 7
\end{array}\right]$$

### Step 2: Perform Gaussian elimination
To eliminate the entry $2$ below the first pivot in position $(2,1)$, apply the row operation $R_2 \leftarrow R_2 - 2R_1$:
- New $R_2$: $(2 - 2(1),\; 4 - 2(2) \mid 7 - 2(3)) = (0, 0 \mid 1)$.

The augmented matrix after elimination is:
$$\left[\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 0 & 1
\end{array}\right]$$

### Step 3: Interpret the contradiction in the matrix and in terms of equations
- **In the augmented matrix:** The second row is $[0 \;\; 0 \mid 1]$, which has all zeros in the coefficient block to the left of the vertical bar, but a non-zero number ($1$) on the right-hand side.
- **In terms of equations:** Rewriting the second row as a linear equation gives:
  $$0\cdot x + 0\cdot y = 1 \iff 0 = 1.$$
  No real (or complex) values of $x$ and $y$ can ever make $0$ equal to $1$.
- **Direct interpretation from the original system:** Notice that the left-hand side of the second equation, $2x + 4y = 2(x + 2y)$, is exactly twice the left-hand side of the first equation. If $x + 2y = 3$, then multiplying by $2$ forces $2x + 4y = 2(3) = 6$. However, the second equation demands that $2x + 4y = 7$. Since $6 \neq 7$, the two conditions contradict each other.

Therefore, the system is **inconsistent** and has **no solution** (solution set $\emptyset$).

## 4. Verification and Consistency Checks
1. **Rank Check:** From the row echelon form $\left[\begin{array}{cc|c}1&2&3\\0&0&1\end{array}\right]$, the coefficient matrix $A$ has 1 non-zero row ($\operatorname{rank}(A) = 1$), whereas the augmented matrix $[A \mid b]$ has 2 non-zero rows ($\operatorname{rank}([A \mid b]) = 2$). Since $\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b])$, the Rouché–Capelli theorem confirms there are no solutions.
2. **Geometric Check:** Writing both lines in slope-intercept form $y = mx + k$:
   - Line 1: $y = -\frac{1}{2}x + \frac{3}{2}$ (slope $m_1 = -\frac{1}{2}$, $y$-intercept $\frac{3}{2}$)
   - Line 2: $y = -\frac{1}{2}x + \frac{7}{4}$ (slope $m_2 = -\frac{1}{2}$, $y$-intercept $\frac{7}{4}$)
   Since $m_1 = m_2 = -\frac{1}{2}$ and $\frac{3}{2} \neq \frac{7}{4}$, the lines are strictly parallel and disjoint.
