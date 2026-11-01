# Exercise 2: Gaussian Elimination — One Solution

## 1. Problem Statement
Solve using Gaussian elimination:
$$\begin{cases}x+y+z=6,\\2x-y+z=3,\\x+2y-z=2.\end{cases}$$
After solving, substitute the result into all equations and check consistency.

## 2. Theoretical Background and Concepts
**Gaussian elimination** solves a linear system $Ax = b$ by transforming its augmented matrix $[A \mid b]$ into **row echelon form** (an upper triangular structure where each leading non-zero entry, or *pivot*, lies strictly to the right of the pivot in the row above it) using three elementary row operations:
1. Swapping two rows ($R_i \leftrightarrow R_j$),
2. Multiplying a row by a non-zero scalar ($R_i \leftarrow cR_i$, $c \neq 0$),
3. Adding a scalar multiple of one row to another ($R_i \leftarrow R_i + cR_j$).

Elementary row operations preserve the solution set of the system. When an $n \times n$ system reduces to an upper triangular form with $n$ non-zero pivots, the system has a **unique solution**, which is found from the bottom equation upward via **back-substitution**.

## 3. Detailed Step-by-Step Solution

### Step 1: Write the augmented matrix $[A \mid b]$
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
2 & -1 & 1 & 3 \\
1 & 2 & -1 & 2
\end{array}\right]$$

### Step 2: Eliminate $x$ from the second and third rows
Use the $(1,1)$-entry ($1$) as the first pivot and perform:
- $R_2 \leftarrow R_2 - 2R_1$: $(2-2,\; -1-2,\; 1-2 \mid 3-12) = (0, -3, -1 \mid -9)$
- $R_3 \leftarrow R_3 - R_1$: $(1-1,\; 2-1,\; -1-1 \mid 2-6) = (0, 1, -2 \mid -4)$

This gives:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & -3 & -1 & -9 \\
0 & 1 & -2 & -4
\end{array}\right]$$

### Step 3: Swap Row 2 and Row 3 to get a convenient pivot of $1$ in position $(2,2)$
Apply $R_2 \leftrightarrow R_3$:
$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & -3 & -1 & -9
\end{array}\right]$$

### Step 4: Eliminate $y$ from the third row
Apply $R_3 \leftarrow R_3 + 3R_2$:
- New $R_3$: $(0,\; -3+3(1),\; -1+3(-2) \mid -9+3(-4)) = (0, 0, -7 \mid -21)$.

$$\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & -7 & -21
\end{array}\right]$$

### Step 5: Back-substitution
1. From Row 3:
   $$-7z = -21 \implies z = \frac{-21}{-7} = 3.$$
2. Substitute $z = 3$ into Row 2:
   $$y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2.$$
3. Substitute $y = 2$ and $z = 3$ into Row 1:
   $$x + y + z = 6 \implies x + 2 + 3 = 6 \implies x = 1.$$

Thus, the unique solution is:
$$(x, y, z) = (1, 2, 3), \quad \text{or} \quad \begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}1\\2\\3\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We substitute $x = 1$, $y = 2$, and $z = 3$ into all three original equations:
1. **First equation:**
   $$x + y + z = 1 + 2 + 3 = 6 \quad (\text{matches right-hand side } 6).$$
2. **Second equation:**
   $$2x - y + z = 2(1) - 2 + 3 = 2 - 2 + 3 = 3 \quad (\text{matches right-hand side } 3).$$
3. **Third equation:**
   $$x + 2y - z = 1 + 2(2) - 3 = 1 + 4 - 3 = 2 \quad (\text{matches right-hand side } 2).$$

All three equations are satisfied, confirming the consistency and accuracy of the solution $(x,y,z) = (1,2,3)$.
