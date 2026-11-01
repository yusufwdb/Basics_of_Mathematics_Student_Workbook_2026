# Exercise 6: A System with a Parameter — Which Cases Actually Occur?

## 1. Problem Statement
Analyze, depending on the parameter $a$, the system
$$\begin{cases}x+y=2,\\ax+ay=4.\end{cases}$$

Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

## 2. Theoretical Background and Concepts
For a general linear system $Ax = b$ in $n = 2$ unknowns, the three theoretical solution types are governed by the ranks of the coefficient matrix $A$ and augmented matrix $[A \mid b]$ (and for a $2 \times 2$ system, by $\det(A)$):
1. **Exactly one solution:** Occurs if and only if $\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 2$, which for a $2 \times 2$ matrix is equivalent to $\det(A) \neq 0$.
2. **Infinitely many solutions:** Occurs if and only if $\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) < 2$.
3. **No solution (inconsistent):** Occurs if and only if $\operatorname{rank}(A) < \operatorname{rank}([A \mid b])$.

In a parameterized system, the parameter $a$ may enter in such a way that the rows of $A$ are *always* linearly dependent regardless of $a$, preventing $\operatorname{rank}(A)$ from ever reaching $2$.

## 3. Detailed Step-by-Step Solution

### Step 1: Set up the augmented matrix and perform Gaussian elimination
Write the augmented matrix $[A(a) \mid b]$:
$$\left[\begin{array}{cc|c}
1 & 1 & 2 \\
a & a & 4
\end{array}\right]$$
Apply the elementary row operation $R_2 \leftarrow R_2 - aR_1$ to eliminate $x$ from the second row:
- New $R_2$: $(a - a(1),\; a - a(1) \mid 4 - 2a) = (0, 0 \mid 4 - 2a)$.

The row echelon form of the augmented matrix is:
$$\left[\begin{array}{cc|c}
1 & 1 & 2 \\
0 & 0 & 4 - 2a
\end{array}\right]$$

### Step 2: Analyze the cases depending on $a$
From the second row $0x + 0y = 4 - 2a$, the consistency of the system depends entirely on whether the right-hand side $4 - 2a$ is zero or non-zero:

1. **Case 1: $4 - 2a = 0 \iff a = 2$ (Infinitely Many Solutions)**
   When $a = 2$, the augmented matrix becomes:
   $$\left[\begin{array}{cc|c}1&1&2\\0&0&0\end{array}\right].$$
   Here $\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 1 < 2$. Both equations reduce to the single line $x + y = 2$, leaving $1$ free variable ($y = t \in \mathbb{R}$, $x = 2 - t$). Thus, for **$a = 2$**, the system has **infinitely many solutions**.

2. **Case 2: $4 - 2a \neq 0 \iff a \neq 2$ (No Solution)**
   When $a \neq 2$, the second row gives the contradictory equation $0 = 4 - 2a \neq 0$ (here $\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b])$). Thus, for **all $a \neq 2$**, the system is inconsistent and has **no solution**.

### Step 3: Explain why "Exactly One Solution" cannot occur for any value of $a$
The case of **exactly one solution never occurs** for any $a \in \mathbb{R}$:
- **Algebraic / Matrix Rank Explanation:** Regardless of the value of $a$, the second row of the coefficient matrix $A = \begin{pmatrix}1&1\\a&a\end{pmatrix}$ is always a scalar multiple of the first row ($R_2 = aR_1$), and the two columns of $A$ are identical. Consequently,
  $$\det(A) = 1(a) - 1(a) = a - a = 0 \quad \text{for all } a \in \mathbb{R},$$
  and $\operatorname{rank}(A) = 1 < 2$ for every $a$. Since a unique solution requires $2$ pivots ($\operatorname{rank}(A) = 2$), the system can never have a unique solution.
- **Direct Equation / Geometric Explanation:** Both equations only involve the sum $x + y$ (since $ax + ay = a(x + y)$). Fixing the sum $x + y = 2$ never determines $x$ and $y$ individually; Geometrically, for $a \neq 0$ both equations describe lines with slope $-1$ (parallel or coincident lines, never intersecting at a single point), and for $a = 0$ the second equation is $0 = 4$ (contradiction).

## 4. Verification and Consistency Checks
Let us check representative values of $a$ directly in the original system:
- For **$a = 2$**: $\begin{cases}x+y=2\\2x+2y=4\end{cases}$. Dividing the second equation by $2$ gives $x+y=2$, which is identical to the first equation (infinitely many solutions $(2-t, t)$).
- For **$a = 0$**: $\begin{cases}x+y=2\\0=4\end{cases}$, an immediate contradiction (no solution).
- For **$a = 1$**: $\begin{cases}x+y=2\\x+y=4\end{cases}$, which requires $x+y$ to equal $2$ and $4$ simultaneously ($2 = 4$, no solution).
This confirms our complete classification.
