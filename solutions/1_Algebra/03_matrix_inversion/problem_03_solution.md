# Exercise 3: When Does the Inverse Not Exist?

## 1. Problem Statement
For
$$A=\begin{pmatrix}2&4\\1&2\end{pmatrix}$$
explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

## 2. Theoretical Background and Concepts
A square $n \times n$ matrix $A$ is called **singular** (or **noninvertible**) if it has no inverse. By the Invertible Matrix Theorem, the following conditions are equivalent for any square matrix $A$:
1. $A^{-1}$ does not exist.
2. $\det(A) = 0$.
3. The rows of $A$ are linearly dependent (for a $2 \times 2$ matrix, one row is a scalar multiple of the other), which means row reduction produces a row of all zeros, and $\operatorname{rank}(A) < n$.

## 3. Detailed Step-by-Step Solution

### Way 1: Using the Determinant
For the matrix
$$A = \begin{pmatrix}2&4\\1&2\end{pmatrix},$$
we compute the determinant using $\det(A) = ad - bc$:
$$\det(A) = (2)(2) - (4)(1) = 4 - 4 = 0.$$
Because the determinant is zero ($\det(A) = 0$), the matrix $A$ is singular. In particular, attempting to apply the $2 \times 2$ inverse formula $A^{-1} = \frac{1}{\det(A)}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ would require dividing by zero, which is undefined. More fundamentally, for any matrix $B$, $\det(AB) = \det(A)\det(B) = 0 \cdot \det(B) = 0 \neq 1 = \det(I_2)$, so no matrix $B$ can satisfy $AB = I_2$.

### Way 2: Using Linear Dependence Between the Rows
Let $R_1 = (2, 4)$ and $R_2 = (1, 2)$ denote the first and second rows of $A$. Observe that the first row is an exact scalar multiple of the second row:
$$R_1 = 2 R_2 \quad \text{or equivalently} \quad R_1 - 2R_2 = (0, 0).$$
Because the rows are linearly dependent:
- If we attempt Gauss–Jordan elimination on $[A \mid I_2]$, applying the elementary row operation $R_1 \leftarrow R_1 - 2R_2$ creates a row of zeros on the left side, making it impossible to reduce $A$ to the identity matrix $I_2$.
- For any $2 \times 2$ matrix $B$, the first row of the product $AB$ is $R_1 B = (2R_2)B = 2(R_2 B)$, meaning the first row of $AB$ must always be twice the second row of $AB$. However, in the identity matrix $I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$, the first row $(1,0)$ is not twice the second row $(0,1)$. Hence, $AB = I_2$ has no solution.

## 4. Verification and Consistency Checks
Let us perform row reduction on $A$ to verify both perspectives simultaneously:
$$\begin{pmatrix}2&4\\1&2\end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_2} \begin{pmatrix}1&2\\2&4\end{pmatrix} \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \begin{pmatrix}1&2\\0&0\end{pmatrix}.$$
1. The row echelon form has only $1$ non-zero row (one pivot), so $\operatorname{rank}(A) = 1 < 2$.
2. Also, notice that the vector $x = \begin{pmatrix}-2\\1\end{pmatrix} \neq \begin{pmatrix}0\\0\end{pmatrix}$ satisfies
   $$Ax = \begin{pmatrix}2&4\\1&2\end{pmatrix}\begin{pmatrix}-2\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}.$$
   If $A^{-1}$ existed, multiplying $Ax = 0$ on the left by $A^{-1}$ would force $x = A^{-1}0 = 0$, a contradiction. This confirms that $A^{-1}$ cannot exist.
