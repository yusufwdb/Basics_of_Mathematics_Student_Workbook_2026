# Exercise 1: Definition of the Inverse

## 1. Problem Statement
For
$$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

## 2. Theoretical Background and Concepts
Let $A$ be an $n \times n$ square matrix. A matrix $B$ of the same size is called the **inverse** of $A$ (denoted $A^{-1}$) if and only if multiplying $A$ by $B$ on both the left and the right yields the $n \times n$ identity matrix $I_n$:
$$AB = I_n \quad \text{and} \quad BA = I_n$$
For $2 \times 2$ matrices, the identity matrix is
$$I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}.$$
Matrix multiplication is performed row-by-column: the $(i,j)$-entry of the product $AB$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the product $AB$
We multiply $A$ by $B$ using standard row-by-column matrix multiplication:
$$AB = \begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
Calculating each entry individually:
- $(1,1)$-entry: $2(1) + 1(-1) = 2 - 1 = 1$
- $(1,2)$-entry: $2(-1) + 1(2) = -2 + 2 = 0$
- $(2,1)$-entry: $1(1) + 1(-1) = 1 - 1 = 0$
- $(2,2)$-entry: $1(-1) + 1(2) = -1 + 2 = 1$

Combining these entries gives:
$$AB = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$

### Step 2: Compute the product $BA$
Next, we multiply $B$ by $A$:
$$BA = \begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}2&1\\1&1\end{pmatrix}$$
Calculating each entry individually:
- $(1,1)$-entry: $1(2) + (-1)(1) = 2 - 1 = 1$
- $(1,2)$-entry: $1(1) + (-1)(1) = 1 - 1 = 0$
- $(2,1)$-entry: $(-1)(2) + 2(1) = -2 + 2 = 0$
- $(2,2)$-entry: $(-1)(1) + 2(1) = -1 + 2 = 1$

Combining these entries gives:
$$BA = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$

### Step 3: Relate the result to the definition of the inverse
Since both $AB = I_2$ and $BA = I_2$ hold, $B$ satisfies the exact defining condition of the inverse matrix of $A$. Therefore, $B = A^{-1}$.

## 4. Verification and Consistency Checks
To independently verify that $B = A^{-1}$ is consistent with the properties of determinants and action on vectors:
1. **Determinant Check:** $\det(A) = 2(1) - 1(1) = 1$ and $\det(B) = 1(2) - (-1)(-1) = 2 - 1 = 1$. Since $\det(AB) = \det(A)\det(B) = 1 \cdot 1 = 1 = \det(I_2)$, the determinants are consistent.
2. **Action on a Test Vector:** Let $v = \begin{pmatrix}3\\4\end{pmatrix}$. Then
   $$Av = \begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}3\\4\end{pmatrix} = \begin{pmatrix}10\\7\end{pmatrix},$$
   and applying $B$ to $Av$ gives
   $$B(Av) = \begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}10\\7\end{pmatrix} = \begin{pmatrix}10-7\\-10+14\end{pmatrix} = \begin{pmatrix}3\\4\end{pmatrix} = v,$$
   confirming that $B$ undoes the linear transformation defined by $A$.
