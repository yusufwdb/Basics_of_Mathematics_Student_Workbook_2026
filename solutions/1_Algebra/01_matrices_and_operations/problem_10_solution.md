# Exercise 10: Columns of a Matrix Product

## 1. Problem Statement

Given
$$A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix}.$$
Denote the columns of $B$ by $b_1,b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

## 2. Theoretical Background and Concepts

- **Column-by-Column Rule for Matrix Multiplication:** Let $A$ be an $m \times n$ matrix and $B = \begin{pmatrix} b_1 & b_2 & \cdots & b_p \end{pmatrix}$ be an $n \times p$ matrix with columns $b_1, b_2, \ldots, b_p \in \mathbb{R}^n$. Then the matrix product $AB$ is an $m \times p$ matrix whose $j$-th column is the matrix-vector product $Ab_j$:
  $$AB = A \begin{pmatrix} b_1 & b_2 & \cdots & b_p \end{pmatrix} = \begin{pmatrix} Ab_1 & Ab_2 & \cdots & Ab_p \end{pmatrix}.$$
- **Theoretical Justification:** By definition, the $(i,j)$-entry of $AB$ is $\sum_{k=1}^n a_{ik} b_{kj}$. Meanwhile, the $j$-th column $b_j$ has entries $(b_{1j}, b_{2j}, \ldots, b_{nj})^T$, so the $i$-th entry of the vector $Ab_j$ is also $\sum_{k=1}^n a_{ik} b_{kj}$. Since every entry of the $j$-th column of $AB$ equals the corresponding entry of $Ab_j$, the $j$-th column of $AB$ is $Ab_j$.

## 3. Detailed Step-by-Step Solution

The columns of $B$ are:
$$b_1 = \begin{pmatrix}1\\-1\\3\end{pmatrix}, \qquad b_2 = \begin{pmatrix}2\\0\\1\end{pmatrix}.$$

### Part 1: Compute $Ab_1$ and $Ab_2$
- Multiplying $A_{2\times 3}$ by $b_1$ ($3\times 1$):
  $$Ab_1 = \begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}1\\-1\\3\end{pmatrix} = \begin{pmatrix} 1(1) + 2(-1) + 0(3) \\ 0(1) + 1(-1) + 1(3) \end{pmatrix} = \begin{pmatrix} 1 - 2 + 0 \\ 0 - 1 + 3 \end{pmatrix} = \begin{pmatrix}-1\\2\end{pmatrix}.$$
- Multiplying $A_{2\times 3}$ by $b_2$ ($3\times 1$):
  $$Ab_2 = \begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}2\\0\\1\end{pmatrix} = \begin{pmatrix} 1(2) + 2(0) + 0(1) \\ 0(2) + 1(0) + 1(1) \end{pmatrix} = \begin{pmatrix} 2 + 0 + 0 \\ 0 + 0 + 1 \end{pmatrix} = \begin{pmatrix}2\\1\end{pmatrix}.$$

### Part 2: Compute the Matrix $AB$
Multiplying $A_{2\times 3}$ by $B_{3\times 2}$ directly gives a $2 \times 2$ matrix:
$$AB = \begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix} = \begin{pmatrix} 1(1)+2(-1)+0(3) & 1(2)+2(0)+0(1) \\ 0(1)+1(-1)+1(3) & 0(2)+1(0)+1(1) \end{pmatrix} = \begin{pmatrix}-1&2\\2&1\end{pmatrix}.$$

### Part 3: Comparison and Explanation
Comparing the results of Parts 1 and 2:
- The first column of $AB$ is $\begin{pmatrix}-1\\2\end{pmatrix}$, which is equal to $Ab_1$.
- The second column of $AB$ is $\begin{pmatrix}2\\1\end{pmatrix}$, which is equal to $Ab_2$.
Thus, $AB = \begin{pmatrix} Ab_1 & Ab_2 \end{pmatrix}$.

**Why this holds:** When we compute the $j$-th column of $AB$, we take the dot product of each row of $A$ with the $j$-th column of $B$ ($b_j$). The columns of $B$ do not interact with each other during multiplication by $A$: the first column of $AB$ depends only on $A$ and $b_1$ (forming $Ab_1$), and the second column of $AB$ depends only on $A$ and $b_2$ (forming $Ab_2$).

## 4. Verification and Consistency Checks

Let us also check the **linear combination of columns of $A$** interpretation for each column of $AB$. Let $a_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $a_2 = \begin{pmatrix}2\\1\end{pmatrix}$, $a_3 = \begin{pmatrix}0\\1\end{pmatrix}$ be the columns of $A$:
- $Ab_1 = 1a_1 - 1a_2 + 3a_3 = \begin{pmatrix}1\\0\end{pmatrix} - \begin{pmatrix}2\\1\end{pmatrix} + \begin{pmatrix}0\\3\end{pmatrix} = \begin{pmatrix}-1\\2\end{pmatrix}. \quad \checkmark$
- $Ab_2 = 2a_1 + 0a_2 + 1a_3 = \begin{pmatrix}2\\0\end{pmatrix} + \begin{pmatrix}0\\0\end{pmatrix} + \begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}2\\1\end{pmatrix}. \quad \checkmark$
This confirms that every column of $AB$ is a linear combination of the columns of $A$.
