# Exercise 4: Matrix Multiplication and Noncommutativity

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\3&1\end{pmatrix}$$
compute $AB$ and $BA$. Is $AB=BA$? Use this example to explain what noncommutativity of matrix multiplication means.

## 2. Theoretical Background and Concepts

- **Matrix Multiplication Definition:** For two $2 \times 2$ matrices $A = (a_{ij})$ and $B = (b_{ij})$, the product $C = AB$ is a $2 \times 2$ matrix whose $(i,j)$-entry is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$:
  $$c_{ij} = \sum_{k=1}^{2} a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j}.$$
- **Noncommutativity:** An operation $\cdot$ is commutative if $x \cdot y = y \cdot x$ for all elements $x, y$. Matrix multiplication is **not commutative** in general: even when both $AB$ and $BA$ are defined and have the same size (i.e., $A$ and $B$ are square matrices of the same order), it is generally the case that $AB \neq BA$.

## 3. Detailed Step-by-Step Solution

### 1. Computing $AB$
$$AB = \begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}2&0\\3&1\end{pmatrix} = \begin{pmatrix} 1\cdot 2 + 2\cdot 3 & 1\cdot 0 + 2\cdot 1 \\ 0\cdot 2 + 1\cdot 3 & 0\cdot 0 + 1\cdot 1 \end{pmatrix} = \begin{pmatrix} 2+6 & 0+2 \\ 0+3 & 0+1 \end{pmatrix} = \begin{pmatrix}8&2\\3&1\end{pmatrix}.$$

### 2. Computing $BA$
$$BA = \begin{pmatrix}2&0\\3&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix} = \begin{pmatrix} 2\cdot 1 + 0\cdot 0 & 2\cdot 2 + 0\cdot 1 \\ 3\cdot 1 + 1\cdot 0 & 3\cdot 2 + 1\cdot 1 \end{pmatrix} = \begin{pmatrix} 2+0 & 4+0 \\ 3+0 & 6+1 \end{pmatrix} = \begin{pmatrix}2&4\\3&7\end{pmatrix}.$$

### 3. Comparing $AB$ and $BA$
Two matrices are equal if and only if they have the same size and all their corresponding entries are equal. Comparing the entries:
$$\begin{pmatrix}8&2\\3&1\end{pmatrix} \neq \begin{pmatrix}2&4\\3&7\end{pmatrix}$$
(for example, $(AB)_{11} = 8 \neq 2 = (BA)_{11}$). Therefore, **$AB \neq BA$**.

### 4. Explanation of Noncommutativity of Matrix Multiplication
Noncommutativity means that **the order of factors in a matrix product matters**. Unlike real or complex numbers where $ab = ba$ always holds, swapping the order of two matrices in a product typically changes the resulting matrix because in $AB$ we take rows of $A$ with columns of $B$, whereas in $BA$ we take rows of $B$ with columns of $A$. Geometrically, $A$ and $B$ represent linear transformations (here, shears and scalings), and applying transformation $B$ followed by $A$ ($AB$) produces a different composite effect on space than applying $A$ followed by $B$ ($BA$).

## 4. Verification and Consistency Checks

1. **Trace Invariance Check:** A fundamental theorem of linear algebra states that although $AB \neq BA$, the trace (sum of main diagonal entries) always satisfies $\operatorname{tr}(AB) = \operatorname{tr}(BA)$:
   $$\operatorname{tr}(AB) = 8 + 1 = 9, \qquad \operatorname{tr}(BA) = 2 + 7 = 9. \quad \checkmark$$
2. **Determinant Multiplicativity Check:** Similarly, $\det(AB) = \det(BA) = \det(A)\det(B)$. Here $\det(A) = 1\cdot 1 - 2\cdot 0 = 1$ and $\det(B) = 2\cdot 1 - 0\cdot 3 = 2$, so both products must have determinant $1 \cdot 2 = 2$:
   $$\det(AB) = 8\cdot 1 - 2\cdot 3 = 8 - 6 = 2, \qquad \det(BA) = 2\cdot 7 - 4\cdot 3 = 14 - 12 = 2. \quad \checkmark$$
Both checks confirm our arithmetic for $AB$ and $BA$ is completely accurate.
