# Exercise 2: Determinant of a 3×3 Matrix

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2&-1\\0&3&4\\2&1&5\end{pmatrix}$$
compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

## 2. Theoretical Background and Concepts

- **Sarrus' Rule for $3 \times 3$ Determinants:** For a $3 \times 3$ matrix $A = (a_{ij})$, copy the first two columns to the right of the matrix and sum the products along the three downward-right (main) diagonals, then subtract the products along the three upward-right (anti-) diagonals:
  $$\det A = (a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}) - (a_{31}a_{22}a_{13} + a_{32}a_{23}a_{11} + a_{33}a_{21}a_{12}).$$
- **Row-Replacement Invariance Property:** Adding a scalar multiple of one row to another row ($R_i \leftarrow R_i + c R_j$ for $i \neq j$) leaves the determinant unchanged, and the determinant of an upper triangular matrix equals the product of its diagonal entries. Alternatively, cofactor expansion along a column with a zero entry provides a quick check.

## 3. Detailed Step-by-Step Solution

### 1. Computing $\det A$ Using Sarrus' Rule
Write out the matrix $A$ with its first two columns repeated on the right:
$$\left|\begin{array}{ccc|cc}
1 & 2 & -1 & 1 & 2 \\
0 & 3 & 4 & 0 & 3 \\
2 & 1 & 5 & 2 & 1
\end{array}\right|$$

- **Products along the three main (downward-right) diagonals:**
  1. $d_1 = 1 \cdot 3 \cdot 5 = 15$
  2. $d_2 = 2 \cdot 4 \cdot 2 = 16$
  3. $d_3 = (-1) \cdot 0 \cdot 1 = 0$
  $$\text{Sum of positive terms} = 15 + 16 + 0 = 31.$$

- **Products along the three anti- (upward-right) diagonals:**
  1. $u_1 = 2 \cdot 3 \cdot (-1) = -6$
  2. $u_2 = 1 \cdot 4 \cdot 1 = 4$
  3. $u_3 = 5 \cdot 0 \cdot 2 = 0$
  $$\text{Sum of negative terms} = (-6) + 4 + 0 = -2.$$

- **Combining the two sums:**
  $$\det A = 31 - (-2) = 31 + 2 = 33.$$

### 2. Simple Check Using a Determinant Property
We use the **invariance of the determinant under row replacement** ($R_i \leftarrow R_i + cR_j$) to create a second zero in the first column (since $a_{21} = 0$ is already zero!).
Perform $R_3 \leftarrow R_3 - 2R_1$, which does not change the determinant:
$$\det A = \det\begin{pmatrix}1&2&-1\\0&3&4\\2-2(1)&1-2(2)&5-2(-1)\end{pmatrix} = \det\begin{pmatrix}1&2&-1\\0&3&4\\0&-3&7\end{pmatrix}.$$
Now add row 2 to row 3 ($R_3 \leftarrow R_3 + R_2$), which also does not change the determinant and produces an upper triangular matrix:
$$\det A = \det\begin{pmatrix}1&2&-1\\0&3&4\\0&0&11\end{pmatrix} = 1 \cdot 3 \cdot 11 = 33.$$
This immediately confirms $\det A = 33$.

## 4. Verification and Consistency Checks

- **Cofactor Expansion along Column 1 Check:** Since $a_{21} = 0$, expanding along the first column requires only two $2 \times 2$ determinants:
  $$\det A = 1 \cdot \det\begin{pmatrix}3&4\\1&5\end{pmatrix} - 0 + 2 \cdot \det\begin{pmatrix}2&-1\\3&4\end{pmatrix} = 1(15 - 4) + 2(8 - (-3)) = 11 + 2(11) = 33. \quad \checkmark$$
All three methods (Sarrus' rule, triangular reduction via row operations, and cofactor expansion) yield $\det A = 33$.
