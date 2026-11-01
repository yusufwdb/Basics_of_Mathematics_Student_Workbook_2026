# Exercise 10: Detecting Dependence

## 1. Problem Statement

Without carrying out a full determinant calculation, explain why
$$\det\begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}=0.$$
Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

## 2. Theoretical Background and Concepts

- **Proportional Rows Property:** If one row of a square matrix is a scalar multiple of another row ($R_i = c R_j$ for $i \neq j$), then the determinant of the matrix is zero:
  $$\det A = 0.$$
  *(Proof: Applying the determinant-preserving row operation $R_i \leftarrow R_i - c R_j$ replaces row $i$ with a row of all zeros $(0, 0, \ldots, 0)$, and expanding along a row of zeros yields $0$.)*
- **Linear Dependence of Rows and Noninvertibility:** A set of rows $\{R_1, R_2, \ldots, R_n\}$ is **linearly dependent** if one row can be written as a linear combination of the others. For any $n \times n$ matrix $A$, the following statements are equivalent:
  1. The rows of $A$ are linearly dependent.
  2. $\det A = 0$.
  3. $A$ is **not invertible** (singular), and $\operatorname{rank}(A) < n$.

## 3. Detailed Step-by-Step Solution

### 1. Identifying the Specific Dependence Between the Rows
Let the rows of the matrix $A = \begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}$ be denoted by:
$$R_1 = \begin{pmatrix}1 & 2 & 3\end{pmatrix}, \qquad R_2 = \begin{pmatrix}2 & 4 & 6\end{pmatrix}, \qquad R_3 = \begin{pmatrix}0 & 1 & 5\end{pmatrix}.$$
By inspection, every entry of the second row $R_2$ is exactly $2$ times the corresponding entry of the first row $R_1$:
$$R_2 = 2 R_1 \qquad (\text{or equivalently, } 2R_1 - 1R_2 + 0R_3 = \begin{pmatrix}0 & 0 & 0\end{pmatrix}).$$

### 2. Explaining Why $\det A = 0$ Without Full Expansion
Because $R_2 = 2R_1$, the first and second rows are **proportional** (linearly dependent).
- Using the homogeneity and alternating properties of determinants:
  $$\det\begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix} = \det\begin{pmatrix}1&2&3\\2(1)&2(2)&2(3)\\0&1&5\end{pmatrix} = 2\det\begin{pmatrix}1&2&3\\1&2&3\\0&1&5\end{pmatrix} = 0,$$
  because a matrix with two identical rows always has determinant zero (swapping the two identical rows leaves the matrix unchanged while negating its determinant, so $d = -d \implies d = 0$).
- Equivalently, performing the single row operation $R_2 \leftarrow R_2 - 2R_1$ (which does not change the determinant) turns the second row into $(0, 0, 0)$, and a matrix with a zero row has determinant $0$.

### 3. Connection with Noninvertibility of the Matrix
Because the rows of $A$ are linearly dependent ($R_2 = 2R_1$), the three rows span at most a $2$-dimensional subspace of $\mathbb{R}^3$ ($\operatorname{rank}(A) = 2 < 3$), and $\det A = 0$. Consequently, the matrix $A$ is **not invertible (singular)**. In terms of linear systems $Ax = b$, the first two equations $x_1 + 2x_2 + 3x_3 = b_1$ and $2x_1 + 4x_2 + 6x_3 = b_2$ are redundant when $b_2 = 2b_1$ (giving infinitely many solutions) and contradictory when $b_2 \neq 2b_1$ (giving no solution), so $A$ cannot have an inverse matrix $A^{-1}$.

## 4. Verification and Consistency Checks

1. **Nullspace Vector Check:** Notice that the vector $v = \begin{pmatrix}-7\\5\\-1\end{pmatrix} \neq \begin{pmatrix}0\\0\\0\end{pmatrix}$ satisfies:
   $$Av = \begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}\begin{pmatrix}-7\\5\\-1\end{pmatrix} = \begin{pmatrix}-7+10-3\\-14+20-6\\0+5-5\end{pmatrix} = \begin{pmatrix}0\\0\\0\end{pmatrix},$$
   which directly confirms that $A$ is not one-to-one and therefore not invertible.
2. **Sarrus' Rule Check:**
   - Main diagonals: $(1)(4)(5) + (2)(6)(0) + (3)(2)(1) = 20 + 0 + 6 = 26$.
   - Anti-diagonals: $(0)(4)(3) + (1)(6)(1) + (5)(2)(2) = 0 + 6 + 20 = 26$.
   - $\det A = 26 - 26 = 0$. $\checkmark$
