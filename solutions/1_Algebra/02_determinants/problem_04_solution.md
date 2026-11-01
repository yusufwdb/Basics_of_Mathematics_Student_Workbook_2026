# Exercise 4: Triangular Matrix

## 1. Problem Statement

Without expanding the determinant, compute
$$\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}.$$
State the rule for an arbitrary triangular matrix and explain it using this example.

## 2. Theoretical Background and Concepts

- **Upper and Lower Triangular Matrices:** A square matrix $T = (t_{ij})$ of order $n \times n$ is called:
  - **upper triangular** if all entries strictly below the main diagonal are zero ($t_{ij} = 0$ for all $i > j$),
  - **lower triangular** if all entries strictly above the main diagonal are zero ($t_{ij} = 0$ for all $i < j$).
- **Determinant of a Triangular Matrix:** The determinant of any (upper or lower) triangular matrix—or diagonal matrix—is simply the **product of the entries on its main diagonal**:
  $$\det T = t_{11} t_{22} \cdots t_{nn} = \prod_{i=1}^n t_{ii}.$$

## 3. Detailed Step-by-Step Solution

### 1. Computing the Determinant Without Full Expansion
Let
$$T = \begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}.$$
All entries below the main diagonal are $0$ ($t_{21} = 0, t_{31} = 0, t_{32} = 0$), so $T$ is an **upper triangular matrix**. Its main diagonal entries are $t_{11} = 2$, $t_{22} = -3$, and $t_{33} = 7$. Multiplying the main diagonal entries gives:
$$\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix} = 2 \cdot (-3) \cdot 7 = -42.$$

### 2. General Rule and Explanation Using This Example
- **General Rule:** For any $n \times n$ upper triangular or lower triangular matrix, the determinant is equal to the product of the entries on the main diagonal.
- **Explanation Using This Example:**
  Why do the off-diagonal entries ($4, 1, 5$) have no effect on the determinant?
  1. **From the perspective of cofactor expansion along the first column:** In the first column $\begin{pmatrix}2\\0\\0\end{pmatrix}$, the only potentially nonzero entry is the top entry $t_{11} = 2$; the other entries are $0$. Therefore, when we expand along the first column, the terms multiplied by $t_{21} = 0$ and $t_{31} = 0$ vanish immediately regardless of the values of $4$ and $1$ in the first row! We are left with $2$ times the determinant of the remaining $2 \times 2$ submatrix $\begin{pmatrix}-3&5\\0&7\end{pmatrix}$. In that $2 \times 2$ submatrix, the first column is $\begin{pmatrix}-3\\0\end{pmatrix}$, so the entry $5$ is multiplied by $0$ and also vanishes, leaving $2 \cdot (-3) \cdot 7 = -42$.
  2. **From the perspective of permutation products (or Sarrus' rule):** Every term in the determinant formula is a signed product of $n$ entries chosen with one entry from each row and one from each column. The only way to avoid picking a zero from below the main diagonal is to pick $t_{33} = 7$ in row 3, which then forces us to pick $t_{22} = -3$ in row 2, which then forces $t_{11} = 2$ in row 1. All other five products contain at least one zero entry below the diagonal.

## 4. Verification and Consistency Checks

Let us verify using Sarrus' rule that all five non-main-diagonal products vanish:
- Main diagonals: $(2)(-3)(7) + (4)(5)(0) + (1)(0)(0) = -42 + 0 + 0 = -42$.
- Anti-diagonals: $(0)(-3)(1) + (0)(5)(2) + (7)(0)(4) = 0 + 0 + 0 = 0$.
Thus $\det T = -42 - 0 = -42$, confirming that every term except the main diagonal product $2 \cdot (-3) \cdot 7 = -42$ is zero.
