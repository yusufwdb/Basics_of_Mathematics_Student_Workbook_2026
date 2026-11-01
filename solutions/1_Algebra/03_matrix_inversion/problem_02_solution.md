# Exercise 2: Formula for a 2×2 Matrix

## 1. Problem Statement
Find the inverse of
$$A=\begin{pmatrix}3&2\\5&4\end{pmatrix}$$
using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

## 2. Theoretical Background and Concepts
For a general $2 \times 2$ matrix
$$A = \begin{pmatrix}a&b\\c&d\end{pmatrix},$$
its determinant is defined as $\det(A) = ad - bc$. The matrix $A$ is invertible if and only if $\det(A) \neq 0$. When $\det(A) \neq 0$, the explicit formula for the inverse matrix is obtained by swapping the main diagonal entries, negating the off-diagonal entries, and dividing by the determinant:
$$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the entries and compute the determinant
For the given matrix
$$A = \begin{pmatrix}3&2\\5&4\end{pmatrix},$$
we have $a = 3$, $b = 2$, $c = 5$, and $d = 4$.

The determinant of $A$ is:
$$\det(A) = ad - bc = (3)(4) - (2)(5) = 12 - 10 = 2.$$
Since $\det(A) = 2 \neq 0$, the matrix $A$ is invertible.

### Step 2: Apply the $2 \times 2$ inverse formula
Substituting the entries and determinant into the formula gives:
$$A^{-1} = \frac{1}{2}\begin{pmatrix}4&-2\\-5&3\end{pmatrix}.$$
Multiplying each entry of the adjugate matrix by the scalar $\frac{1}{2}$ yields:
$$A^{-1} = \begin{pmatrix}\frac{4}{2}&\frac{-2}{2}\\[4pt]\frac{-5}{2}&\frac{3}{2}\end{pmatrix} = \begin{pmatrix}2&-1\\-\frac{5}{2}&\frac{3}{2}\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We verify the result by computing the product $AA^{-1}$:
$$AA^{-1} = \begin{pmatrix}3&2\\5&4\end{pmatrix}\begin{pmatrix}2&-1\\-\frac{5}{2}&\frac{3}{2}\end{pmatrix}$$
Computing each entry of the product:
- $(1,1)$-entry: $3(2) + 2\left(-\frac{5}{2}\right) = 6 - 5 = 1$
- $(1,2)$-entry: $3(-1) + 2\left(\frac{3}{2}\right) = -3 + 3 = 0$
- $(2,1)$-entry: $5(2) + 4\left(-\frac{5}{2}\right) = 10 - 10 = 0$
- $(2,2)$-entry: $5(-1) + 4\left(\frac{3}{2}\right) = -5 + 6 = 1$

Thus,
$$AA^{-1} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2,$$
which confirms that our formula-derived inverse $A^{-1}$ is completely accurate.
