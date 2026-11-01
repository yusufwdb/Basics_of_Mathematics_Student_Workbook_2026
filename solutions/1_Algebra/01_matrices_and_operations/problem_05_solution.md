# Exercise 5: Matrix Times Vector

## 1. Problem Statement

Let
$$A=\begin{pmatrix}2&-1\\1&3\end{pmatrix},\qquad x=\begin{pmatrix}4\\2\end{pmatrix}.$$
Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

## 2. Theoretical Background and Concepts

- **Row-Vector Rule for $Ax$:** If $A$ is an $m \times n$ matrix and $x \in \mathbb{R}^n$ is an $n \times 1$ column vector, the product $Ax$ is an $m \times 1$ column vector whose $i$-th entry is the dot product of the $i$-th row of $A$ with $x$.
- **Column-Combination Interpretation of $Ax$:** Let $a_1, a_2, \ldots, a_n \in \mathbb{R}^m$ be the columns of $A$ and let $x = (x_1, x_2, \ldots, x_n)^T$. Then the matrix-vector product $Ax$ is identical to the linear combination of the columns of $A$ weighted by the entries of $x$:
  $$Ax = \begin{pmatrix} | & | & & | \\ a_1 & a_2 & \cdots & a_n \\ | & | & & | \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n.$$

## 3. Detailed Step-by-Step Solution

### 1. Direct Computation of $Ax$ (Row-by-Column)
Since $A$ has size $2 \times 2$ and $x$ has size $2 \times 1$, the product $Ax$ has size $2 \times 1$:
$$Ax = \begin{pmatrix}2&-1\\1&3\end{pmatrix}\begin{pmatrix}4\\2\end{pmatrix} = \begin{pmatrix} 2\cdot 4 + (-1)\cdot 2 \\ 1\cdot 4 + 3\cdot 2 \end{pmatrix} = \begin{pmatrix} 8 - 2 \\ 4 + 6 \end{pmatrix} = \begin{pmatrix}6\\10\end{pmatrix}.$$

### 2. Expressing $Ax$ as a Linear Combination of the Columns of $A$
Identify the columns of $A$ and the entries of $x$:
$$a_1 = \begin{pmatrix}2\\1\end{pmatrix}, \qquad a_2 = \begin{pmatrix}-1\\3\end{pmatrix}, \qquad x_1 = 4, \qquad x_2 = 2.$$
Writing $Ax$ as the linear combination $x_1 a_1 + x_2 a_2$:
$$Ax = 4\begin{pmatrix}2\\1\end{pmatrix} + 2\begin{pmatrix}-1\\3\end{pmatrix}.$$
Evaluating this linear combination step by step:
$$4\begin{pmatrix}2\\1\end{pmatrix} + 2\begin{pmatrix}-1\\3\end{pmatrix} = \begin{pmatrix}8\\4\end{pmatrix} + \begin{pmatrix}-2\\6\end{pmatrix} = \begin{pmatrix}8 + (-2)\\4 + 6\end{pmatrix} = \begin{pmatrix}6\\10\end{pmatrix}.$$

## 4. Verification and Consistency Checks

- **Comparison of Methods:** Both the standard row-by-column dot-product calculation and the column-space linear combination yield the exact same vector $\begin{pmatrix}6\\10\end{pmatrix}$.
- **Decomposition via Standard Basis Vectors:** Notice that $x = 4e_1 + 2e_2$, where $e_1 = \begin{pmatrix}1\\0\end{pmatrix}$ and $e_2 = \begin{pmatrix}0\\1\end{pmatrix}$. By linearity of matrix multiplication:
  $$Ax = A(4e_1 + 2e_2) = 4(Ae_1) + 2(Ae_2) = 4a_1 + 2a_2 = \begin{pmatrix}6\\10\end{pmatrix},$$
  which provides a theoretical verification of why the column-combination rule works.
