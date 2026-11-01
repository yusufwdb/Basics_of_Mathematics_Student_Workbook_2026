# Exercise 6: Transpose

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix}$$
compute $A^T$, $B^T$, and $AB$. Then verify in this example that
$$(AB)^T=B^TA^T.$$

## 2. Theoretical Background and Concepts

- **Transpose of a Matrix:** Given an $m \times n$ matrix $M = (m_{ij})$, its transpose $M^T$ is the $n \times m$ matrix obtained by interchanging rows and columns, so that the $i$-th row of $M$ becomes the $i$-th column of $M^T$:
  $$(M^T)_{ij} = m_{ji} \quad \text{for all } 1 \le i \le n,\ 1 \le j \le m.$$
- **Transpose of a Product (Reverse-Order Law):** For any two matrices $A_{m\times n}$ and $B_{n\times p}$, their product $AB$ has size $m \times p$, so $(AB)^T$ has size $p \times m$. Since $B^T$ has size $p \times n$ and $A^T$ has size $n \times m$, the product $B^T A^T$ is defined and has size $p \times m$, and for every $(i,j)$:
  $$((AB)^T)_{ij} = (AB)_{ji} = \sum_{k=1}^n a_{jk} b_{ki} = \sum_{k=1}^n (B^T)_{ik} (A^T)_{kj} = (B^T A^T)_{ij}.$$
  Hence $(AB)^T = B^T A^T$.

## 3. Detailed Step-by-Step Solution

### 1. Computing $A^T$ and $B^T$
- Matrix $A$ has size $2 \times 3$, so $A^T$ has size $3 \times 2$ (rows of $A$ become columns of $A^T$):
  $$A^T = \begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$
- Matrix $B$ has size $3 \times 2$, so $B^T$ has size $2 \times 3$ (rows of $B$ become columns of $B^T$):
  $$B^T = \begin{pmatrix}1&2&-1\\0&1&3\end{pmatrix}.$$

### 2. Computing $AB$
Multiplying $A_{2\times 3}$ by $B_{3\times 2}$ gives a $2 \times 2$ matrix:
$$AB = \begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix} = \begin{pmatrix} 1(1)+2(2)+3(-1) & 1(0)+2(1)+3(3) \\ 4(1)+5(2)+6(-1) & 4(0)+5(1)+6(3) \end{pmatrix}$$
$$AB = \begin{pmatrix} 1+4-3 & 0+2+9 \\ 4+10-6 & 0+5+18 \end{pmatrix} = \begin{pmatrix}2&11\\8&23\end{pmatrix}.$$

### 3. Verifying $(AB)^T = B^T A^T$
- **Left-hand side $(AB)^T$:** Transposing our result for $AB$:
  $$(AB)^T = \begin{pmatrix}2&11\\8&23\end{pmatrix}^T = \begin{pmatrix}2&8\\11&23\end{pmatrix}.$$
- **Right-hand side $B^T A^T$:** Multiplying $B^T_{2\times 3}$ by $A^T_{3\times 2}$:
  $$B^T A^T = \begin{pmatrix}1&2&-1\\0&1&3\end{pmatrix}\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix} = \begin{pmatrix} 1(1)+2(2)+(-1)(3) & 1(4)+2(5)+(-1)(6) \\ 0(1)+1(2)+3(3) & 0(4)+1(5)+3(6) \end{pmatrix}$$
  $$B^T A^T = \begin{pmatrix} 1+4-3 & 4+10-6 \\ 0+2+9 & 0+5+18 \end{pmatrix} = \begin{pmatrix}2&8\\11&23\end{pmatrix}.$$
Since both sides equal $\begin{pmatrix}2&8\\11&23\end{pmatrix}$, the identity $(AB)^T = B^T A^T$ is verified.

## 4. Verification and Consistency Checks

- **Why $A^T B^T$ would be wrong here:** Although $A^T_{3\times 2}$ and $B^T_{2\times 3}$ happen to be multipliable in the order $A^T B^T$, their product $A^T B^T$ has size $3 \times 3$, whereas $(AB)^T$ has size $2 \times 2$. Thus $(AB)^T$ could not possibly equal $A^T B^T$ even by dimension inspection!
- **Diagonal Preservation Check:** Transposing a square matrix leaves its main diagonal entries unchanged. The diagonal of $AB$ is $(2, 23)$, and the diagonal of $B^T A^T$ is also $(2, 23)$, while the off-diagonal entries $11$ and $8$ are swapped, as expected.
