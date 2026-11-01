# Exercise 9: A System from a Sum Condition

## 1. Problem Statement
Find numbers $x,y$ satisfying
$$x+y=10,\qquad 2x+5y=32.$$
Solve the system and explain geometrically why the solution is unique.

## 2. Theoretical Background and Concepts
A system of two linear equations in two variables $x$ and $y$:
$$\begin{cases}
a_1 x + b_1 y = c_1, \\
a_2 x + b_2 y = c_2,
\end{cases}$$
has a clear **geometric interpretation** in the Cartesian plane $\mathbb{R}^2$:
- Each non-degenerate linear equation $a_i x + b_i y = c_i$ defines a **straight line** $\ell_i$ consisting of all points $(x,y)$ that satisfy that condition.
- A solution $(x,y)$ to the system is a point that lies on **both** lines simultaneously—that is, an **intersection point** of $\ell_1$ and $\ell_2$.
- Two lines in the plane have **slopes** $m_1 = -\frac{a_1}{b_1}$ and $m_2 = -\frac{a_2}{b_2}$ (when $b_1, b_2 \neq 0$). Two lines in $\mathbb{R}^2$ intersect at **one and only one point** if and only if they are not parallel, which occurs if and only if their slopes are different ($m_1 \neq m_2$, equivalently $\det(A) = a_1 b_2 - a_2 b_1 \neq 0$).

## 3. Detailed Step-by-Step Solution

### Step 1: Solve the system by Gaussian elimination
Write the system in augmented matrix form:
$$\left[\begin{array}{cc|c}
1 & 1 & 10 \\
2 & 5 & 32
\end{array}\right]$$
Eliminate $x$ from the second equation using the row operation $R_2 \leftarrow R_2 - 2R_1$:
- New $R_2$: $(2 - 2(1),\; 5 - 2(1) \mid 32 - 2(10)) = (0, 3 \mid 12)$.

The augmented matrix becomes:
$$\left[\begin{array}{cc|c}
1 & 1 & 10 \\
0 & 3 & 12
\end{array}\right]$$
Now perform back-substitution:
1. From the second row:
   $$3y = 12 \implies y = \frac{12}{3} = 4.$$
2. Substitute $y = 4$ into the first row ($x + y = 10$):
   $$x + 4 = 10 \implies x = 10 - 4 = 6.$$

Thus, the unique solution is:
$$(x, y) = (6, 4).$$

### Step 2: Geometric explanation of why the solution is unique
In the Cartesian $xy$-plane, each equation represents a straight line:
- **Line $\ell_1$:** $x + y = 10 \iff y = -x + 10$, which has slope $m_1 = -1$ and $y$-intercept $(0, 10)$.
- **Line $\ell_2$:** $2x + 5y = 32 \iff y = -\frac{2}{5}x + \frac{32}{5}$, which has slope $m_2 = -\frac{2}{5} = -0.4$ and $y$-intercept $\left(0, \frac{32}{5}\right)$.

Because the two lines have **different slopes** ($m_1 = -1 \neq -\frac{2}{5} = m_2$, corresponding to non-parallel normal vectors $(1,1)$ and $(2,5)$ and non-zero determinant $\det\begin{pmatrix}1&1\\2&5\end{pmatrix} = 5 - 2 = 3 \neq 0$), the lines $\ell_1$ and $\ell_2$ are **not parallel**. In Euclidean geometry, two non-parallel lines in a plane intersect at **exactly one point**—namely $(6, 4)$—which explains why the solution is unique.

## 4. Verification and Consistency Checks
We substitute $x = 6$ and $y = 4$ back into both original conditions:
1. **First condition (sum condition):**
   $$x + y = 6 + 4 = 10 \quad (\text{matches } 10).$$
2. **Second condition (weighted sum condition):**
   $$2x + 5y = 2(6) + 5(4) = 12 + 20 = 32 \quad (\text{matches } 32).$$

Both equations are satisfied, confirming that $(6, 4)$ is the unique intersection point of the two lines.
