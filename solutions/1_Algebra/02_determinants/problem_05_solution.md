# Exercise 5: Row Operations

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}$$
find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

## 2. Theoretical Background and Concepts

- **Effect of Elementary Row Operations on the Determinant:**
  1. **Row replacement ($R_i \leftarrow R_i + cR_j$, $i \neq j$):** Does **not** change the determinant ($\det A_{\text{new}} = \det A_{\text{old}}$).
  2. **Row swap ($R_i \leftrightarrow R_j$, $i \neq j$):** Multiplies the determinant by $-1$ ($\det A_{\text{new}} = -\det A_{\text{old}}$).
  3. **Row scaling ($R_i \leftarrow cR_i$, $c \neq 0$):** Multiplies the determinant by $c$ ($\det A_{\text{new}} = c \det A_{\text{old}}$).
- **Strategy:** Use row replacement operations (which preserve the determinant) to reduce $A$ to an upper triangular matrix $U$, and then compute $\det A = \det U$ as the product of the main diagonal entries of $U$.

## 3. Detailed Step-by-Step Solution

Start with
$$A = \begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}.$$

### Step 1: Eliminate the $(2,1)$-entry using $R_2 \leftarrow R_2 - 2R_1$
We subtract $2$ times row 1 from row 2:
$$\text{New } R_2 = (2 - 2(1),\ 1 - 2(2),\ 0 - 2(3)) = (0,\ -3,\ -6).$$
This yields
$$A_1 = \begin{pmatrix}1&2&3\\0&-3&-6\\-1&4&2\end{pmatrix}.$$
- **Effect on the determinant:** Because this is a row replacement operation (adding a multiple of one row to another), **the determinant does not change**: $\det A_1 = \det A$.

### Step 2: Eliminate the $(3,1)$-entry using $R_3 \leftarrow R_3 + R_1$
We add row 1 to row 3:
$$\text{New } R_3 = (-1 + 1,\ 4 + 2,\ 2 + 3) = (0,\ 6,\ 5).$$
This yields
$$A_2 = \begin{pmatrix}1&2&3\\0&-3&-6\\0&6&5\end{pmatrix}.$$
- **Effect on the determinant:** Again, this is a row replacement operation, so **the determinant does not change**: $\det A_2 = \det A_1 = \det A$.

### Step 3: Eliminate the $(3,2)$-entry using $R_3 \leftarrow R_3 + 2R_2$
We add $2$ times row 2 to row 3:
$$\text{New } R_3 = (0 + 2(0),\ 6 + 2(-3),\ 5 + 2(-6)) = (0,\ 0,\ -7).$$
This yields the upper triangular matrix
$$U = \begin{pmatrix}1&2&3\\0&-3&-6\\0&0&-7\end{pmatrix}.$$
- **Effect on the determinant:** This is a row replacement operation, so **the determinant does not change**: $\det U = \det A_2 = \det A$.

### Step 4: Compute the Determinant of the Upper Triangular Matrix $U$
Since $U$ is upper triangular, its determinant is the product of its diagonal entries:
$$\det A = \det U = 1 \cdot (-3) \cdot (-7) = 21.$$

*(Alternative Option at Step 2: If one instead factored $-3$ out of row 2 via $R_2 \leftarrow -\frac{1}{3}R_2$ to get $(0, 1, 2)$, that scaling would divide the determinant by $-3$, requiring us to multiply the final determinant by $-3$: $(-3)\cdot(1\cdot 1\cdot(-7)) = 21$.)*

## 4. Verification and Consistency Checks

Let us verify $\det A = 21$ independently using Sarrus' rule on the original matrix $A = \begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}$:
- Main diagonals: $(1 \cdot 1 \cdot 2) + (2 \cdot 0 \cdot (-1)) + (3 \cdot 2 \cdot 4) = 2 + 0 + 24 = 26$.
- Anti-diagonals: $((-1) \cdot 1 \cdot 3) + (4 \cdot 0 \cdot 1) + (2 \cdot 2 \cdot 2) = -3 + 0 + 8 = 5$.
- Determinant: $\det A = 26 - 5 = 21$. $\checkmark$
Both methods produce the exact same value, $21$.
