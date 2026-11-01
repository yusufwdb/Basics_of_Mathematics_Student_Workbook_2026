# Exercise 8: Two Systems with the Same Coefficient Matrix

## 1. Problem Statement
Solve by elimination the two systems
$$\begin{cases}2x+y=5,\\x-y=1,\end{cases}$$
$$\begin{cases}2x+y=1,\\x-y=4.\end{cases}$$
Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

## 2. Theoretical Background and Concepts
In a linear system $Ax = b$, the **sequence of elementary row operations** needed to reduce the augmented matrix $[A \mid b]$ to row echelon form (which rows to swap, which pivot to use, and which multipliers $m_{ij}$ to subtract) is determined **solely by the entries of the coefficient matrix $A$**, and is completely independent of the right-hand side vector $b$.

Because both systems share the exact same coefficient matrix
$$A = \begin{pmatrix}2&1\\1&-1\end{pmatrix},$$
the left-hand side of the augmented matrix undergoes the exact same transformations in both cases; only the arithmetic on the last column (the right-hand side $b$) differs. (In fact, this is why multiple systems with the same $A$ can be solved simultaneously in a single multi-augmented matrix $[A \mid b_1 \; b_2]$.)

## 3. Detailed Step-by-Step Solution

### Part 1: Solve the First System $\begin{cases}2x+y=5,\\x-y=1\end{cases}$
1. **Set up the augmented matrix $[A \mid b_1]$:**
   $$\left[\begin{array}{cc|c}2&1&5\\1&-1&1\end{array}\right]$$
2. **Step A (Swap rows $R_1 \leftrightarrow R_2$ to place $1$ in the $(1,1)$ pivot):**
   $$\left[\begin{array}{cc|c}1&-1&1\\2&1&5\end{array}\right]$$
3. **Step B (Eliminate $x$ from Row 2 using $R_2 \leftarrow R_2 - 2R_1$):**
   $$\left[\begin{array}{cc|c}1&-1&1\\2-2(1)&1-2(-1)&5-2(1)\end{array}\right] = \left[\begin{array}{cc|c}1&-1&1\\0&3&3\end{array}\right]$$
4. **Back-substitution for System 1:**
   - From Row 2: $3y = 3 \implies y = 1$.
   - From Row 1: $x - y = 1 \implies x - 1 = 1 \implies x = 2$.
   - **Solution to System 1:** $(x, y) = (2, 1)$.

---

### Part 2: Solve the Second System $\begin{cases}2x+y=1,\\x-y=4\end{cases}$
1. **Set up the augmented matrix $[A \mid b_2]$:**
   $$\left[\begin{array}{cc|c}2&1&1\\1&-1&4\end{array}\right]$$
2. **Step A (Swap rows $R_1 \leftrightarrow R_2$ to place $1$ in the $(1,1)$ pivot):**
   $$\left[\begin{array}{cc|c}1&-1&4\\2&1&1\end{array}\right]$$
3. **Step B (Eliminate $x$ from Row 2 using $R_2 \leftarrow R_2 - 2R_1$):**
   $$\left[\begin{array}{cc|c}1&-1&4\\2-2(1)&1-2(-1)&1-2(4)\end{array}\right] = \left[\begin{array}{cc|c}1&-1&4\\0&3&-7\end{array}\right]$$
4. **Back-substitution for System 2:**
   - From Row 2: $3y = -7 \implies y = -\frac{7}{3}$.
   - From Row 1: $x - y = 4 \implies x = 4 + y = 4 - \frac{7}{3} = \frac{5}{3}$.
   - **Solution to System 2:** $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

---

### Part 3: Comparison of the Elimination Steps
- **Which part is the same?**
  1. The **choice of elementary row operations** ($R_1 \leftrightarrow R_2$ followed by $R_2 \leftarrow R_2 - 2R_1$) is identical in both calculations.
  2. The **transformation of the $2 \times 2$ coefficient block on the left**—from $\begin{pmatrix}2&1\\1&-1\end{pmatrix}$ to $\begin{pmatrix}1&-1\\2&1\end{pmatrix}$ to the upper triangular matrix $\begin{pmatrix}1&-1\\0&3\end{pmatrix}$—is $100\%$ identical in both cases.
  3. Even in back-substitution, the **divisors and coefficients** (dividing by $3$ to find $y$, then adding $y$ to the first right-hand entry to find $x$) are the same.
- **Why is it the same?**
  Because the elimination operations are chosen solely to create zeros below the pivots in the **coefficient matrix $A$**. Since both systems have the exact same coefficient matrix $A = \begin{pmatrix}2&1\\1&-1\end{pmatrix}$, the pivots and multipliers depend only on $A$ and not at all on the right-hand side constants $b_1 = \begin{pmatrix}5\\1\end{pmatrix}$ or $b_2 = \begin{pmatrix}1\\4\end{pmatrix}$.

## 4. Verification and Consistency Checks
1. **Check System 1 with $(x, y) = (2, 1)$:**
   - $2(2) + 1 = 4 + 1 = 5$ (matches $5$).
   - $2 - 1 = 1$ (matches $1$).
2. **Check System 2 with $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$:**
   - $2\left(\frac{5}{3}\right) + \left(-\frac{7}{3}\right) = \frac{10 - 7}{3} = \frac{3}{3} = 1$ (matches $1$).
   - $\frac{5}{3} - \left(-\frac{7}{3}\right) = \frac{5 + 7}{3} = \frac{12}{3} = 4$ (matches $4$).
3. **Simultaneous Augmented Matrix Check $[A \mid b_1 \; b_2]$:**
   $$\left[\begin{array}{cc|cc}2&1&5&1\\1&-1&1&4\end{array}\right] \xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{cc|cc}1&-1&1&4\\2&1&5&1\end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{cc|cc}1&-1&1&4\\0&3&3&-7\end{array}\right],$$
   which vividly demonstrates how the left side is reduced only once for both systems.
