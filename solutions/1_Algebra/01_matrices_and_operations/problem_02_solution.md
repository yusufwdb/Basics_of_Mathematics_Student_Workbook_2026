# Exercise 2: Addition and Scalar Multiplication

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2\\-1&3\end{pmatrix},\qquad B=\begin{pmatrix}4&-2\\0&5\end{pmatrix}$$
compute
$$A+B,\qquad A-B,\qquad 3A-2B.$$
Explain why matrix addition is possible only for matrices of the same size.

## 2. Theoretical Background and Concepts

- **Matrix Addition and Subtraction:** Given two matrices $A = (a_{ij})$ and $B = (b_{ij})$ of the same size $m \times n$, their sum $A+B$ and difference $A-B$ are $m \times n$ matrices defined entrywise:
  $$(A \pm B)_{ij} = a_{ij} \pm b_{ij} \quad \text{for all } 1 \le i \le m,\ 1 \le j \le n.$$
- **Scalar Multiplication:** Given a scalar $c \in \mathbb{R}$ and an $m \times n$ matrix $A = (a_{ij})$, the scalar multiple $cA$ is the $m \times n$ matrix obtained by multiplying every entry of $A$ by $c$:
  $$(cA)_{ij} = c \cdot a_{ij}.$$
- **Linear Combinations of Matrices:** Combining scalar multiplication and matrix addition allows us to compute expressions of the form $\alpha A + \beta B$ entry by entry: $(\alpha A + \beta B)_{ij} = \alpha a_{ij} + \beta b_{ij}$.

## 3. Detailed Step-by-Step Solution

Both $A$ and $B$ have size $2 \times 2$, so all requested operations are well-defined.

### 1. Computing $A+B$
Adding corresponding entries:
$$A+B = \begin{pmatrix}1&2\\-1&3\end{pmatrix} + \begin{pmatrix}4&-2\\0&5\end{pmatrix} = \begin{pmatrix}1+4 & 2+(-2)\\-1+0 & 3+5\end{pmatrix} = \begin{pmatrix}5&0\\-1&8\end{pmatrix}.$$

### 2. Computing $A-B$
Subtracting corresponding entries of $B$ from $A$:
$$A-B = \begin{pmatrix}1&2\\-1&3\end{pmatrix} - \begin{pmatrix}4&-2\\0&5\end{pmatrix} = \begin{pmatrix}1-4 & 2-(-2)\\-1-0 & 3-5\end{pmatrix} = \begin{pmatrix}-3&4\\-1&-2\end{pmatrix}.$$

### 3. Computing $3A-2B$
First, compute the scalar multiples $3A$ and $2B$:
$$3A = 3\begin{pmatrix}1&2\\-1&3\end{pmatrix} = \begin{pmatrix}3&6\\-3&9\end{pmatrix}, \qquad 2B = 2\begin{pmatrix}4&-2\\0&5\end{pmatrix} = \begin{pmatrix}8&-4\\0&10\end{pmatrix}.$$
Now subtract $2B$ from $3A$:
$$3A - 2B = \begin{pmatrix}3&6\\-3&9\end{pmatrix} - \begin{pmatrix}8&-4\\0&10\end{pmatrix} = \begin{pmatrix}3-8 & 6-(-4)\\-3-0 & 9-10\end{pmatrix} = \begin{pmatrix}-5&10\\-3&-1\end{pmatrix}.$$

### 4. Why Matrix Addition Requires the Same Size
Matrix addition is defined entry-by-entry: each entry $a_{ij}$ at position $(i,j)$ in $A$ must be paired with the corresponding entry $b_{ij}$ at the exact same position $(i,j)$ in $B$. If two matrices have different numbers of rows or different numbers of columns, one matrix will have entries at positions $(i,j)$ that do not exist in the other matrix, leaving those sums undefined. Furthermore, from a linear transformation perspective, matrices of size $m \times n$ represent linear maps from $\mathbb{R}^n$ to $\mathbb{R}^m$; two functions can be added pointwise only when they share the same domain ($\mathbb{R}^n$) and codomain ($\mathbb{R}^m$).

## 4. Verification and Consistency Checks

1. **Identity Check between $A+B$ and $A-B$:**
   We know that $(A+B) + (A-B) = 2A$. Let us verify this with our computed matrices:
   $$\begin{pmatrix}5&0\\-1&8\end{pmatrix} + \begin{pmatrix}-3&4\\-1&-2\end{pmatrix} = \begin{pmatrix}2&4\\-2&6\end{pmatrix} = 2\begin{pmatrix}1&2\\-1&3\end{pmatrix} = 2A. \quad \checkmark$$
2. **Decomposition Check for $3A-2B$:**
   Notice that $3A - 2B = \frac{1}{2}(A+B) + \frac{5}{2}(A-B)$, or more simply $3A - 2B = A + 2(A-B)$:
   $$A + 2(A-B) = \begin{pmatrix}1&2\\-1&3\end{pmatrix} + 2\begin{pmatrix}-3&4\\-1&-2\end{pmatrix} = \begin{pmatrix}1-6 & 2+8\\-1-2 & 3-4\end{pmatrix} = \begin{pmatrix}-5&10\\-3&-1\end{pmatrix},$$
   which matches our direct calculation of $3A-2B$ in every entry.
