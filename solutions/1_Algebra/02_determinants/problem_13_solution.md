# Exercise 13: Determinant by Elimination

## 1. Problem Statement

Compute the determinant
$$A=\begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}$$
using elimination. Record the effect of every row operation used on the value of the determinant.

## 2. Theoretical Background and Concepts

- **Gaussian Elimination for Determinants:** Any square matrix $A$ can be reduced to an upper triangular matrix $U$ using elementary row operations:
  - **Row replacement ($R_i \leftarrow R_i + c R_j$, $i \neq j$):** Leaves the determinant unchanged ($\det A_{\text{new}} = \det A_{\text{old}}$).
  - **Row swap ($R_i \leftrightarrow R_j$, $i \neq j$):** Reverses the sign of the determinant ($\det A_{\text{new}} = -\det A_{\text{old}}$).
  - **Row scaling ($R_i \leftarrow c R_i$, $c \neq 0$):** Multiplies the determinant by $c$ ($\det A_{\text{new}} = c \det A_{\text{old}}$).
- Once $A$ is reduced to upper triangular form $U$ using only row replacements (and $s$ row swaps, if needed), $\det A = (-1)^s u_{11} u_{22} \cdots u_{nn}$.

## 3. Detailed Step-by-Step Solution

Start with
$$A = \begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}.$$

### Step 1: Eliminate the $(2,1)$-entry using $R_2 \leftarrow R_2 - 2R_1$
Subtract $2$ times row 1 from row 2:
$$\text{New } R_2 = (2 - 2(1),\ 5 - 2(2),\ 7 - 2(3)) = (0,\ 1,\ 1).$$
This produces
$$A_1 = \begin{pmatrix}1&2&3\\0&1&1\\1&0&2\end{pmatrix}.$$
- **Effect on the determinant:** Row replacement does **not** change the determinant:
  $$\det A_1 = \det A.$$

### Step 2: Eliminate the $(3,1)$-entry using $R_3 \leftarrow R_3 - R_1$
Subtract row 1 from row 3:
$$\text{New } R_3 = (1 - 1,\ 0 - 2,\ 2 - 3) = (0,\ -2,\ -1).$$
This produces
$$A_2 = \begin{pmatrix}1&2&3\\0&1&1\\0&-2&-1\end{pmatrix}.$$
- **Effect on the determinant:** Row replacement does **not** change the determinant:
  $$\det A_2 = \det A_1 = \det A.$$

### Step 3: Eliminate the $(3,2)$-entry using $R_3 \leftarrow R_3 + 2R_2$
Add $2$ times row 2 to row 3:
$$\text{New } R_3 = (0 + 2(0),\ -2 + 2(1),\ -1 + 2(1)) = (0,\ 0,\ 1).$$
This produces the upper triangular matrix
$$U = \begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix}.$$
- **Effect on the determinant:** Row replacement does **not** change the determinant:
  $$\det U = \det A_2 = \det A.$$

### Step 4: Compute $\det A$ from the Upper Triangular Matrix $U$
Since $U$ is upper triangular and none of the three row replacement operations changed the determinant, $\det A$ equals the product of the main diagonal entries of $U$:
$$\det A = \det U = 1 \cdot 1 \cdot 1 = 1.$$

## 4. Verification and Consistency Checks

Let us verify $\det A = 1$ using cofactor expansion along the third row of $A = \begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}$ (which contains a zero):
$$\det A = 1 \cdot \det\begin{pmatrix}2&3\\5&7\end{pmatrix} - 0 \cdot \det\begin{pmatrix}1&3\\2&7\end{pmatrix} + 2 \cdot \det\begin{pmatrix}1&2\\2&5\end{pmatrix}$$
$$= 1(2\cdot 7 - 3\cdot 5) + 2(1\cdot 5 - 2\cdot 2) = 1(14 - 15) + 2(5 - 4) = -1 + 2 = 1. \quad \checkmark$$
This confirms our elimination result $\det A = 1$.
