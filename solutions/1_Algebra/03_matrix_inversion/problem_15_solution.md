# Exercise 15: Two Methods for Solving the Same System

## 1. Problem Statement
For
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}7\\8\end{pmatrix}$$
solve $Ax=b$ in two ways:

1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

## 2. Theoretical Background and Concepts
A linear system $Ax = b$ with an invertible $n \times n$ matrix $A$ can be solved by:
1. **The Matrix Inverse Method ($x = A^{-1}b$):** First compute the full inverse matrix $A^{-1}$, then multiply $A^{-1}$ by the column vector $b$.
2. **Gaussian Elimination:** Form the augmented matrix $[A \mid b]$, reduce it to upper triangular (row echelon) form using elementary row operations, and find the unknowns by back-substitution.

While both methods must produce the exact same unique solution $x$, Gaussian elimination only performs operations needed for the specific vector $b$, whereas finding $A^{-1}$ is equivalent to solving $n$ systems simultaneously (with right-hand sides equal to the columns of $I_n$).

## 3. Detailed Step-by-Step Solution

### Method 1: Using the Inverse Matrix ($x = A^{-1}b$)
1. **Compute $\det(A)$:**
   $$\det(A) = (2)(3) - (1)(1) = 6 - 1 = 5.$$
2. **Construct $A^{-1}$ using the $2 \times 2$ formula:**
   $$A^{-1} = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix} = \begin{pmatrix}\frac{3}{5}&-\frac{1}{5}\\[4pt]-\frac{1}{5}&\frac{2}{5}\end{pmatrix}.$$
3. **Multiply $A^{-1}$ by $b$:**
   $$x = A^{-1}b = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix} = \frac{1}{5}\begin{pmatrix}3(7) + (-1)(8)\\(-1)(7) + 2(8)\end{pmatrix} = \frac{1}{5}\begin{pmatrix}21 - 8\\-7 + 16\end{pmatrix} = \frac{1}{5}\begin{pmatrix}13\\9\end{pmatrix} = \begin{pmatrix}\frac{13}{5}\\[4pt]\frac{9}{5}\end{pmatrix}.$$

### Method 2: Using Gaussian Elimination
1. **Write the augmented matrix $[A \mid b]$ and swap rows to put $1$ in the $(1,1)$ pivot position:**
   $$\left[\begin{array}{cc|c}2&1&7\\1&3&8\end{array}\right] \xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{cc|c}1&3&8\\2&1&7\end{array}\right]$$
2. **Eliminate the entry below the first pivot ($R_2 \leftarrow R_2 - 2R_1$):**
   $$\left[\begin{array}{cc|c}1&3&8\\0&1-2(3)&7-2(8)\end{array}\right] = \left[\begin{array}{cc|c}1&3&8\\0&-5&-9\end{array}\right]$$
3. **Back-substitution:**
   - From the second row: $-5x_2 = -9 \implies x_2 = \frac{9}{5}$.
   - From the first row: $x_1 + 3x_2 = 8 \implies x_1 = 8 - 3\left(\frac{9}{5}\right) = \frac{40 - 27}{5} = \frac{13}{5}$.

Thus,
$$x = \begin{pmatrix}x_1\\x_2\end{pmatrix} = \begin{pmatrix}\frac{13}{5}\\[4pt]\frac{9}{5}\end{pmatrix}.$$

### Comparison of the Two Methods
- **Agreement of Results:** Both methods yield the exact same solution $x = \begin{pmatrix}\frac{13}{5}\\[4pt]\frac{9}{5}\end{pmatrix} = \begin{pmatrix}2.6\\1.8\end{pmatrix}$.
- **Number of Essential Steps:**
  - *Method 1 ($A^{-1}b$):* Requires 3 essential stages (computing the determinant: 2 multiplications and 1 subtraction; forming the adjugate/inverse; and computing the matrix-vector product: 4 multiplications, 2 additions, and 2 divisions). For a $2 \times 2$ matrix, the explicit shortcut formula makes this very compact.
  - *Method 2 (Gaussian elimination):* Requires 1 row swap, 1 row elimination step ($R_2 \leftarrow R_2 - 2R_1$: 2 multiplications and 2 subtractions), and back-substitution (1 division, 1 multiplication, 1 subtraction).
- **Which method was simpler here?**
  - For a **single $2 \times 2$ system**, both methods require almost the same minimal effort: Gaussian elimination avoids fractions until the final back-substitution step (making mental arithmetic slightly cleaner), while the $2 \times 2$ inverse formula is very direct. However, for larger systems ($3 \times 3$ and above) with only **one** right-hand side vector $b$, **Gaussian elimination is much simpler and more efficient** because computing $A^{-1}$ requires roughly three times as many arithmetic operations as solving a single system by elimination. Conversely, if we already know $A^{-1}$ (as we computed for this exact matrix $A$ in Exercise 6!) or have many right-hand sides $b_1, b_2, \dots, b_k$, then multiplying $A^{-1}b$ is simpler.

## 4. Verification and Consistency Checks
Substitute $x_1 = \frac{13}{5}$ and $x_2 = \frac{9}{5}$ into the original system $Ax = b$:
- First equation: $2\left(\frac{13}{5}\right) + 1\left(\frac{9}{5}\right) = \frac{26 + 9}{5} = \frac{35}{5} = 7$ (matches $b_1 = 7$).
- Second equation: $1\left(\frac{13}{5}\right) + 3\left(\frac{9}{5}\right) = \frac{13 + 27}{5} = \frac{40}{5} = 8$ (matches $b_2 = 8$).

Both equations are satisfied identically.
