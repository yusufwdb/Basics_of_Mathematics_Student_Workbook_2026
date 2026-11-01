# Exercise 15: Classifying Three Systems

## 1. Problem Statement
For each of the following systems, perform only as much elimination as necessary to recognize its type:

1. $\begin{cases}x+y=2,\\x-y=0,\end{cases}$
2. $\begin{cases}x+y=2,\\2x+2y=4,\end{cases}$
3. $\begin{cases}x+y=2,\\2x+2y=5.\end{cases}$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

## 2. Theoretical Background and Concepts
For a $2 \times 2$ linear system reduced by a single Gaussian elimination step to upper triangular (row echelon) form:
$$\left[\begin{array}{cc|c}
1 & a_{12} & b_1 \\
0 & d & c
\end{array}\right]$$
we can immediately classify the system from its **second row** $0x + dy = c$ without even needing to back-substitute:
1. **One Solution (Unique Solution):** Occurs when the second pivot is non-zero ($d \neq 0$). Then both columns have pivots ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 2$), so $y = \frac{c}{d}$ and $x$ are uniquely determined.
2. **Infinitely Many Solutions:** Occurs when $d = 0$ and $c = 0$ (the second row is $[0 \;\; 0 \mid 0]$, i.e., $0 = 0$). Then there is no contradiction, $\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 1 < 2$, and $1$ variable is free.
3. **No Solution (Inconsistent):** Occurs when $d = 0$ and $c \neq 0$ (the second row is $[0 \;\; 0 \mid c]$ with $c \neq 0$, i.e., $0 = c$). This is a contradiction ($\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b])$).

## 3. Detailed Step-by-Step Solution

### System 1: $\begin{cases}x+y=2,\\x-y=0\end{cases}$
1. **Single Elimination Step ($R_2 \leftarrow R_2 - R_1$):**
   $$\left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   1 & -1 & 0
   \end{array}\right]
   \xrightarrow{R_2 \leftarrow R_2 - R_1}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & -2 & -2
   \end{array}\right].$$
2. **Classification and Justification:**
   - **Type:** **Exactly one solution**.
   - **Justification:** After eliminating $x$ from the second row, the second row has a **non-zero pivot** $d = -2 \neq 0$ in the $y$-column ($-2y = -2$). Thus, both unknowns $x$ and $y$ are pivot (basic) variables with no free variables and no contradictory rows ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 2$).

---

### System 2: $\begin{cases}x+y=2,\\2x+2y=4\end{cases}$
1. **Single Elimination Step ($R_2 \leftarrow R_2 - 2R_1$):**
   $$\left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   2 & 2 & 4
   \end{array}\right]
   \xrightarrow{R_2 \leftarrow R_2 - 2R_1}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & 0 & 0
   \end{array}\right].$$
2. **Classification and Justification:**
   - **Type:** **Infinitely many solutions**.
   - **Justification:** After one elimination step, the entire second row becomes $[0 \;\; 0 \mid 0]$ ($0x + 0y = 0$), because the second equation is an exact multiple ($2\times$) of the first equation. Since there is no contradiction ($0 = 0$) and only $1$ pivot for $2$ unknowns ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = 1 < 2$), the variable $y$ is a free parameter ($y = t \in \mathbb{R}$, $x = 2 - t$), yielding infinitely many solutions.

---

### System 3: $\begin{cases}x+y=2,\\2x+2y=5\end{cases}$
1. **Single Elimination Step ($R_2 \leftarrow R_2 - 2R_1$):**
   $$\left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   2 & 2 & 5
   \end{array}\right]
   \xrightarrow{R_2 \leftarrow R_2 - 2R_1}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & 0 & 1
   \end{array}\right].$$
2. **Classification and Justification:**
   - **Type:** **No solution (inconsistent)**.
   - **Justification:** After one elimination step, the second row becomes $[0 \;\; 0 \mid 1]$, which represents the impossible equation $0x + 0y = 1$ ($0 = 1$). Because the coefficient entries in Row 2 are all zero while the right-hand side entry is non-zero ($\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b])$), no pair $(x,y)$ can satisfy both equations.

## 4. Verification and Consistency Checks
We verify all three classifications by checking the solutions and geometric interpretations:
1. **System 1 Check:** From $-2y = -2 \implies y = 1$, and $x = 2 - 1 = 1$. Substituting $(1, 1)$ gives $1 + 1 = 2$ and $1 - 1 = 0$. Geometrically, the lines $y = 2 - x$ (slope $-1$) and $y = x$ (slope $+1$) are perpendicular and intersect at the single point $(1, 1)$.
2. **System 2 Check:** Dividing $2x + 2y = 4$ by $2$ gives $x + y = 2$, which is the exact same line as the first equation (coincident lines $\implies$ infinitely many points $(2-t, t)$).
3. **System 3 Check:** Dividing $2x + 2y = 5$ by $2$ gives $x + y = 2.5$, whereas the first equation states $x + y = 2$. Since $2 \neq 2.5$, these are two parallel, distinct lines with slope $-1$ that never intersect.
