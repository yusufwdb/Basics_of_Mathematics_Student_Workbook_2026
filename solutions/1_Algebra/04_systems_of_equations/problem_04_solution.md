# Exercise 4: Infinitely Many Solutions

## 1. Problem Statement
Solve
$$\begin{cases}x+y+z=2,\\2x+2y+2z=4,\\x-y+z=0.\end{cases}$$
Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

## 2. Theoretical Background and Concepts
When Gaussian elimination on an augmented matrix $[A \mid b]$ yields no contradictory rows ($[0 \dots 0 \mid c]$ with $c \neq 0$), the system is **consistent**.
- Variables corresponding to columns **with pivots** (leading non-zero entries) are called **basic (or leading) variables**.
- Variables corresponding to columns **without pivots** are called **free variables**.

If a consistent system has $r = \operatorname{rank}(A)$ pivots and $n$ unknowns with $r < n$, there are $n - r$ free variables. Assigning arbitrary real parameters (such as $t \in \mathbb{R}$) to the free variables and solving for the basic variables in terms of those parameters yields the **parametric form** of the infinitely many solutions.

## 3. Detailed Step-by-Step Solution

### Step 1: Set up the augmented matrix and apply Gaussian elimination
The augmented matrix of the system is:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
2 & 2 & 2 & 4 \\
1 & -1 & 1 & 0
\end{array}\right]$$
Eliminate $x$ from Row 2 and Row 3 using $R_2 \leftarrow R_2 - 2R_1$ and $R_3 \leftarrow R_3 - R_1$:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
0 & 0 & 0 & 0 \\
0 & -2 & 0 & -2
\end{array}\right]$$
Swap Row 2 and Row 3 ($R_2 \leftrightarrow R_3$) and divide the new Row 2 by $-2$ ($R_2 \leftarrow -\frac{1}{2}R_2$):
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 2 \\
0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]$$
*(Notice that the second equation $2x+2y+2z=4$ was simply twice the first equation $x+y+z=2$, producing the zero row $0=0$.)*

### Step 2: Identify basic and free variables
In the row echelon matrix:
- **Column 1 ($x$)** has a pivot at $(1,1)$.
- **Column 2 ($y$)** has a pivot at $(2,2)$.
- **Column 3 ($z$)** has **no pivot**.

Therefore, $x$ and $y$ are **basic variables**, and **$z$ is a free variable** (alternatively, since $x+z$ appears together, $x$ could also be chosen as free, but $z$ is the standard choice from the non-pivot column).

### Step 3: Write the solution in parametric form
Let the free variable be $z = t$, where $t \in \mathbb{R}$ is an arbitrary real parameter:
1. From Row 2:
   $$y = 1.$$
2. From Row 1:
   $$x + y + z = 2 \implies x + 1 + t = 2 \implies x = 1 - t.$$

Thus, the general solution in parametric form is:
$$\begin{cases}
x = 1 - t, \\
y = 1, \\
z = t,
\end{cases} \quad t \in \mathbb{R},$$
or in vector form:
$$\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}1 - t\\1\\t\end{pmatrix} = \begin{pmatrix}1\\1\\0\end{pmatrix} + t\begin{pmatrix}-1\\0\\1\end{pmatrix}, \quad t \in \mathbb{R}.$$

## 4. Verification and Consistency Checks

### Check 1: Specific parameter value ($t = 3$)
Choose $t = 3$. Substituting $t = 3$ into the parametric formula gives the point:
$$(x, y, z) = (1 - 3, 1, 3) = (-2, 1, 3).$$
Substitute $(-2, 1, 3)$ into all three original equations:
- **Equation 1:** $x + y + z = (-2) + 1 + 3 = 2$ (matches $2$).
- **Equation 2:** $2x + 2y + 2z = 2(-2) + 2(1) + 2(3) = -4 + 2 + 6 = 4$ (matches $4$).
- **Equation 3:** $x - y + z = (-2) - 1 + 3 = 0$ (matches $0$).

The point $(-2, 1, 3)$ satisfies every equation of the system.

### Check 2: General parameter value ($t \in \mathbb{R}$)
For any $t \in \mathbb{R}$:
- $x + y + z = (1 - t) + 1 + t = 2$,
- $2x + 2y + 2z = 2(1 - t) + 2(1) + 2t = 4$,
- $x - y + z = (1 - t) - 1 + t = 0$.

Every point on the line $(1-t, 1, t)$ satisfies the system identically.
