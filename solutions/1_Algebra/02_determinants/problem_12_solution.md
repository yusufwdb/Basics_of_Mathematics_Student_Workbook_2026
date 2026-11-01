# Exercise 12: A Parameter Revealed by a Row Operation

## 1. Problem Statement

For
$$A(t)=\begin{pmatrix}1&2&3\\2&4&t\\0&1&1\end{pmatrix}$$
find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation
$$R_2\leftarrow R_2-2R_1$$
and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

## 2. Theoretical Background and Concepts

- **Invariance of Determinant and Invertibility Under Row Replacement:** Performing the row replacement operation $R_2 \leftarrow R_2 - 2R_1$ yields a row-equivalent matrix $B(t)$ with the exact same determinant:
  $$\det B(t) = \det A(t).$$
  Consequently, $A(t)$ is not invertible if and only if $B(t)$ is not invertible ($\det B(t) = 0$).
- **Linear Dependence of Rows:** If a row operation produces a row of all zeros, then the original rows were linearly dependent, and the matrix is singular ($\det = 0$).

## 3. Detailed Step-by-Step Solution

### Step 1: Perform the Row Operation $R_2 \leftarrow R_2 - 2R_1$
Subtracting $2$ times row 1, $R_1 = (1, 2, 3)$, from row 2, $R_2 = (2, 4, t)$:
$$\text{New } R_2 = (2 - 2(1),\ 4 - 2(2),\ t - 2(3)) = (0,\ 0,\ t - 6).$$
Thus, after $R_2 \leftarrow R_2 - 2R_1$, the matrix becomes:
$$B(t) = \begin{pmatrix}1&2&3\\0&0&t-6\\0&1&1\end{pmatrix}.$$

### Step 2: Use the Resulting Structure to Find $\det A(t)$ and Noninvertibility
Notice that in $B(t)$, the first two entries of the second row are both $0$!
We can find when $A(t)$ is not invertible in two equivalent ways from this structure:
1. **Direct Inspection of Row 2:** The second row of $B(t)$ is $(0,\ 0,\ t-6)$. If $t - 6 = 0$, i.e., **$t = 6$**, this entire row becomes $(0, 0, 0)$, making the determinant zero.
2. **Computing the Determinant from $B(t)$:** Swapping row 2 and row 3 of $B(t)$ ($R_2 \leftrightarrow R_3$, which multiplies the determinant by $-1$) gives an upper triangular matrix:
   $$\det A(t) = \det B(t) = -\det\begin{pmatrix}1&2&3\\0&1&1\\0&0&t-6\end{pmatrix} = -1 \cdot 1 \cdot (t - 6) = 6 - t.$$
   Setting $\det A(t) = 0$ gives:
   $$6 - t = 0 \iff t = 6.$$

Therefore, the matrix $A(t)$ is not invertible if and only if **$t = 6$**.

### Step 3: Explain What Special Thing Happens to the Rows When $t = 6$
When we substitute $t = 6$ into the original matrix $A(t)$, we get:
$$A(6) = \begin{pmatrix}1&2&3\\2&4&6\\0&1&1\end{pmatrix}.$$
For $t = 6$, the second row $R_2 = (2, 4, 6)$ becomes **an exact scalar multiple of the first row** $R_1 = (1, 2, 3)$, namely:
$$R_2 = 2R_1.$$
That is why the row operation $R_2 \leftarrow R_2 - 2R_1$ completely annihilated the second row into $(0, 0, 0)$ when $t = 6$: the first two entries of $R_2$ ($2$ and $4$) were already $2$ times the first two entries of $R_1$ ($1$ and $2$), and choosing $t = 6$ makes the third entry of $R_2$ also equal to $2$ times the third entry of $R_1$ ($2 \cdot 3 = 6$).

## 4. Verification and Consistency Checks

Let us verify $\det A(t) = 6 - t$ by expanding the original matrix $A(t)$ along its first column:
$$\det A(t) = 1 \cdot \det\begin{pmatrix}4&t\\1&1\end{pmatrix} - 2 \cdot \det\begin{pmatrix}2&3\\1&1\end{pmatrix} + 0 = 1(4 - t) - 2(2 - 3) = (4 - t) - 2(-1) = 4 - t + 2 = 6 - t. \quad \checkmark$$
When $t = 6$, $\det A(6) = 6 - 6 = 0$, and when $t \neq 6$, $\det A(t) = 6 - t \neq 0$, confirming that $t = 6$ is the unique value for which $A(t)$ is not invertible.
