# Exercise 11: Shortening the Calculation with Row Operations

## 1. Problem Statement

Compute
$$\det\begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}$$
by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

## 2. Theoretical Background and Concepts

- **Determinant-Preserving Row Operations:** Elementary **row replacement** operations of the form
  $$R_i \leftarrow R_i + c R_j \qquad (i \neq j,\ c \in \mathbb{R}),$$
  where we add a scalar multiple of one row to a *different* row, **do not change the value of the determinant**.
  *(In contrast, swapping two rows $R_i \leftrightarrow R_j$ changes the sign of the determinant, and scaling a row $R_i \leftarrow c R_i$ multiplies the determinant by $c$.)*
- **Elimination Strategy:** Because the first column of the given matrix consists entirely of $1$s, subtracting the first row from the second and third rows immediately creates two zeros in the first column without changing the determinant. One more row replacement then yields an upper triangular matrix.

## 3. Detailed Step-by-Step Solution

Let
$$A = \begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}.$$

### Step 1: Create Zeros in the First Column
Perform two row replacement operations using $R_1 = (1, 2, 3)$ as the pivot row:
1. $R_2 \leftarrow R_2 - R_1$: $\quad (1-1,\ 3-2,\ 4-3) = (0,\ 1,\ 1)$,
2. $R_3 \leftarrow R_3 - R_1$: $\quad (1-1,\ 4-2,\ 6-3) = (0,\ 2,\ 3)$.

Because both operations are row replacements ($R_i \leftarrow R_i + c R_j$ with $i \neq j$), **neither operation changes the determinant**:
$$\det A = \det\begin{pmatrix}1&2&3\\0&1&1\\0&2&3\end{pmatrix}.$$

### Step 2: Create a Zero in Position $(3,2)$ (or Expand Along Column 1)
Perform one more row replacement operation:
$$R_3 \leftarrow R_3 - 2R_2: \quad (0 - 2(0),\ 2 - 2(1),\ 3 - 2(1)) = (0,\ 0,\ 1).$$
Again, this row replacement **does not change the determinant**, and reduces the matrix to upper triangular form:
$$\det A = \det\begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix}.$$

### Step 3: Evaluate the Determinant of the Triangular Matrix
Since the resulting matrix is upper triangular, its determinant is the product of its main diagonal entries:
$$\det A = 1 \cdot 1 \cdot 1 = 1.$$

*(Note: Even after Step 1, expanding along the first column $\begin{pmatrix}1\\0\\0\end{pmatrix}$ immediately gives $\det A = 1 \cdot \det\begin{pmatrix}1&1\\2&3\end{pmatrix} = 1(3 - 2) = 1$.)*

## 4. Verification and Consistency Checks

Let us verify $\det A = 1$ using Sarrus' rule on the original matrix $A = \begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}$:
- Main diagonals: $(1 \cdot 3 \cdot 6) + (2 \cdot 4 \cdot 1) + (3 \cdot 1 \cdot 4) = 18 + 8 + 12 = 38$.
- Anti-diagonals: $(1 \cdot 3 \cdot 3) + (4 \cdot 4 \cdot 1) + (6 \cdot 1 \cdot 2) = 9 + 16 + 12 = 37$.
- Subtracting: $\det A = 38 - 37 = 1$. $\checkmark$
Notice how row operations allowed us to work only with small integers $(0, 1, 2, 3)$ instead of computing products up to $18$ and $38$.
