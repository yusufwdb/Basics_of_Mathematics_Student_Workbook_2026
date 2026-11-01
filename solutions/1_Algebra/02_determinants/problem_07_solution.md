# Exercise 7: Using Properties Instead of Recomputing

## 1. Problem Statement

Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute
$$\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).$$
Justify each answer using the appropriate property.

## 2. Theoretical Background and Concepts

Let $A$ be an $n \times n$ square matrix and $c \in \mathbb{R}$ be a scalar. The determinant satisfies the following fundamental algebraic properties:
1. **Homogeneity of Degree $n$ (Scalar Multiplication):** Multiplying an $n \times n$ matrix $A$ by a scalar $c$ multiplies every one of its $n$ rows by $c$. Since factoring $c$ out of a single row multiplies the determinant by $c$, factoring $c$ out of all $n$ rows multiplies the determinant by $c^n$:
   $$\det(cA) = c^n \det A.$$
2. **Transpose Invariance:** Transposing a matrix interchanges its rows and columns, which leaves the determinant unchanged:
   $$\det(A^T) = \det A.$$
3. **Multiplicativity (Binet's Theorem):** For any two $n \times n$ matrices $A$ and $B$, $\det(AB) = (\det A)(\det B)$. In particular, for powers of $A$:
   $$\det(A^k) = (\det A)^k.$$

## 3. Detailed Step-by-Step Solution

Here $A$ is a $3 \times 3$ matrix, so **$n = 3$** and $\det A = -4$.

### 1. Computing $\det(2A)$
Using the scalar multiplication property $\det(cA) = c^n \det A$ with $c = 2$ and $n = 3$:
$$\det(2A) = 2^3 \det A = 8 \cdot (-4) = -32.$$
- **Justification:** Because $A$ has $3$ rows, multiplying $A$ by $2$ multiplies each of the $3$ rows by $2$, which scales the determinant by $2 \cdot 2 \cdot 2 = 2^3 = 8$.

### 2. Computing $\det(A^T)$
Using the transpose invariance property $\det(A^T) = \det A$:
$$\det(A^T) = \det A = -4.$$
- **Justification:** The determinant of the transpose of any square matrix is always equal to the determinant of the original matrix.

### 3. Computing $\det(A^2)$
Using the multiplicativity of the determinant $\det(AB) = (\det A)(\det B)$ with $B = A$:
$$\det(A^2) = \det(A \cdot A) = (\det A)(\det A) = (\det A)^2 = (-4)^2 = 16.$$
- **Justification:** The determinant of a product of square matrices equals the product of their determinants, so the determinant of the square of a matrix is the square of its determinant.

### 4. Computing $\det(-A)$
Note that $-A = (-1)A$. Using the scalar multiplication property $\det(cA) = c^n \det A$ with $c = -1$ and $n = 3$:
$$\det(-A) = (-1)^3 \det A = (-1) \cdot (-4) = 4.$$
- **Justification:** Multiplying a $3 \times 3$ matrix by $-1$ negates each of its $3$ rows, multiplying the determinant by $(-1)^3 = -1$.

## 4. Verification and Consistency Checks

Let us verify all four results using a concrete $3 \times 3$ diagonal test matrix $A = \begin{pmatrix}-4&0&0\\0&1&0\\0&0&1\end{pmatrix}$, which clearly has $\det A = (-4)(1)(1) = -4$:
1. $2A = \begin{pmatrix}-8&0&0\\0&2&0\\0&0&2\end{pmatrix} \implies \det(2A) = (-8)(2)(2) = -32$. $\checkmark$
2. $A^T = \begin{pmatrix}-4&0&0\\0&1&0\\0&0&1\end{pmatrix} \implies \det(A^T) = (-4)(1)(1) = -4$. $\checkmark$
3. $A^2 = \begin{pmatrix}16&0&0\\0&1&0\\0&0&1\end{pmatrix} \implies \det(A^2) = (16)(1)(1) = 16$. $\checkmark$
4. $-A = \begin{pmatrix}4&0&0\\0&-1&0\\0&0&-1\end{pmatrix} \implies \det(-A) = (4)(-1)(-1) = 4$. $\checkmark$
Notice also that $\det(2A) = \det((-2)(-A)) = (-2)^3 \det(-A) = (-8)(4) = -32$, which is internally consistent.
