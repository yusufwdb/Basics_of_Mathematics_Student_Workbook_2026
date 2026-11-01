# Exercise 11: A Parameter in a System of Three Equations

## 1. Problem Statement
Analyze the number of solutions depending on $t$:
$$\begin{cases}x+y+z=1,\\x+ty+z=2,\\x+y+tz=3.\end{cases}$$
Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

## 2. Theoretical Background and Concepts
When applying **Gaussian elimination** to a system containing a real parameter $t$:
- Any row addition $R_i \leftarrow R_i + c(t)R_j$ is valid for **all** $t \in \mathbb{R}$.
- However, dividing a row by an expression containing $t$ (such as dividing by a diagonal entry $t - 1$ to solve for an unknown or normalize a pivot) is **only valid when that divisor is non-zero** ($t - 1 \neq 0$).
- Whenever a pivot expression vanishes ($t - 1 = 0 \iff t = 1$), the standard division step ceases to be valid (as it would divide by zero), and we must substitute that specific parameter value into the reduced matrix and analyze it separately.

## 3. Detailed Step-by-Step Solution

### Step 1: Set up the augmented matrix and perform parameter-safe elimination
Write the augmented matrix of the system:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
1 & t & 1 & 2 \\
1 & 1 & t & 3
\end{array}\right]$$
Use the $(1,1)$-entry ($1 \neq 0$, which does not depend on $t$) to eliminate $x$ from Row 2 and Row 3 via $R_2 \leftarrow R_2 - R_1$ and $R_3 \leftarrow R_3 - R_1$:
- New $R_2$: $(1-1,\; t-1,\; 1-1 \mid 2-1) = (0, t-1, 0 \mid 1)$
- New $R_3$: $(1-1,\; 1-1,\; t-1 \mid 3-1) = (0, 0, t-1 \mid 2)$

This immediately yields an upper triangular (row echelon) matrix without any division by $t$:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & t-1 & 0 & 1 \\
0 & 0 & t-1 & 2
\end{array}\right]$$

### Step 2: Identify the parameter value where the standard step ceases to be valid
In the reduced system:
$$\begin{cases}
x + y + z = 1, \\
(t - 1)y = 1, \\
(t - 1)z = 2,
\end{cases}$$
the standard back-substitution step solves the second and third equations by dividing by $t - 1$. This division is valid **if and only if $t - 1 \neq 0$, i.e., $t \neq 1$**. At **$t = 1$**, dividing by $t - 1$ is division by zero and ceases to be valid.

### Step 3: Analyze the two cases

#### Case 1: $t \neq 1$ (Unique Solution)
When $t \neq 1$, both diagonal entries $t - 1$ are non-zero pivots ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 3$). Dividing by $t - 1 \neq 0$ in back-substitution gives:
1. From Row 3:
   $$(t - 1)z = 2 \implies z = \frac{2}{t - 1}.$$
2. From Row 2:
   $$(t - 1)y = 1 \implies y = \frac{1}{t - 1}.$$
3. From Row 1:
   $$x = 1 - y - z = 1 - \frac{1}{t - 1} - \frac{2}{t - 1} = 1 - \frac{3}{t - 1} = \frac{t - 4}{t - 1}.$$
Thus, for every **$t \neq 1$**, the system has **exactly one solution**:
$$(x, y, z) = \left(\frac{t - 4}{t - 1},\; \frac{1}{t - 1},\; \frac{2}{t - 1}\right).$$

#### Case 2: $t = 1$ (No Solution)
Substituting $t = 1$ into the reduced augmented matrix gives:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 2
\end{array}\right]$$
Both the second row ($0 = 1$) and the third row ($0 = 2$) are contradictory equations ($\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b])$). Indeed, in the original system, setting $t = 1$ makes all three left-hand sides equal to $x + y + z$, requiring $x + y + z$ to simultaneously equal $1$, $2$, and $3$, which is impossible.
Thus, for **$t = 1$**, the system is **inconsistent (no solution)**.

*(Summary: The system has **1 solution** for $t \in \mathbb{R} \setminus \{1\}$, **0 solutions** for $t = 1$, and **never has infinitely many solutions**.)*

## 4. Verification and Consistency Checks
Let us substitute the general solution $(x, y, z) = \left(\frac{t-4}{t-1}, \frac{1}{t-1}, \frac{2}{t-1}\right)$ for $t \neq 1$ back into the original three equations:
1. **Equation 1:**
   $$x + y + z = \frac{(t - 4) + 1 + 2}{t - 1} = \frac{t - 1}{t - 1} = 1 \quad \checkmark.$$
2. **Equation 2:**
   $$x + ty + z = \frac{(t - 4) + t(1) + 2}{t - 1} = \frac{2t - 2}{t - 1} = \frac{2(t - 1)}{t - 1} = 2 \quad \checkmark.$$
3. **Equation 3:**
   $$x + y + tz = \frac{(t - 4) + 1 + t(2)}{t - 1} = \frac{3t - 3}{t - 1} = \frac{3(t - 1)}{t - 1} = 3 \quad \checkmark.$$

All three equations hold identically for every $t \neq 1$.
