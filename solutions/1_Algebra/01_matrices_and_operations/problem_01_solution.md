# Exercise 1: Matrix Size and Entries

## 1. Problem Statement

Given
$$A=\begin{pmatrix}2&-1&3\\0&4&5\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\-2&3\\4&1\end{pmatrix}.$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

## 2. Theoretical Background and Concepts

- **Matrix Dimensions (Size):** A matrix with $m$ horizontal rows and $n$ vertical columns is said to have size (or dimension) $m \times n$ (read "$m$ by $n$"). The number of rows is always stated first, followed by the number of columns.
- **Matrix Entries (Elements):** The entry located in the $i$-th row and $j$-th column of a matrix $M$ is denoted by $m_{ij}$, where $1 \le i \le m$ is the row index and $1 \le j \le n$ is the column index.
- **Row and Column Vectors:** The $i$-th row of an $m \times n$ matrix can be extracted as a $1 \times n$ row vector, while the $j$-th column can be extracted as an $m \times 1$ column vector.

## 3. Detailed Step-by-Step Solution

### Part 1: Sizes of Matrices $A$ and $B$
- Matrix $A$ has $2$ horizontal rows and $3$ vertical columns:
  $$\text{Size of } A = 2 \times 3.$$
- Matrix $B$ has $3$ horizontal rows and $2$ vertical columns:
  $$\text{Size of } B = 3 \times 2.$$

### Part 2: Reading Off Specific Entries
Using the notation $m_{ij}$ (row $i$, column $j$):
- $a_{12}$ is the entry in row $1$, column $2$ of $A$:
  $$a_{12} = -1.$$
- $a_{23}$ is the entry in row $2$, column $3$ of $A$:
  $$a_{23} = 5.$$
- $b_{21}$ is the entry in row $2$, column $1$ of $B$:
  $$b_{21} = -2.$$
- $b_{32}$ is the entry in row $3$, column $2$ of $B$:
  $$b_{32} = 1.$$

### Part 3: Row and Column Vectors
- The **second row of $A$** consists of the entries $a_{21}, a_{22}, a_{23}$, written as a row vector (or column vector representation):
  $$r_2(A) = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix} \quad \left(\text{or as a column vector in } \mathbb{R}^3: \begin{pmatrix} 0 \\ 4 \\ 5 \end{pmatrix}\right).$$
- The **first column of $B$** consists of the entries $b_{11}, b_{21}, b_{31}$, written as a column vector:
  $$c_1(B) = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}.$$

## 4. Verification and Consistency Checks

- **Entry Count Check:** Matrix $A$ of size $2 \times 3$ must contain $2 \cdot 3 = 6$ entries. Counting the entries $\{2, -1, 3, 0, 4, 5\}$ confirms there are $6$ elements. Similarly, $B$ of size $3 \times 2$ contains $3 \cdot 2 = 6$ entries: $\{1, 0, -2, 3, 4, 1\}$.
- **Index Bound Check:** For $A_{2\times 3}$, valid indices satisfy $1 \le i \le 2$ and $1 \le j \le 3$, which holds for $a_{12}$ and $a_{23}$. Moreover, $a_{23} = 5$ is the third element of the second row $\begin{pmatrix}0 & 4 & 5\end{pmatrix}$, and $b_{21} = -2$ is the second element of the first column $\begin{pmatrix}1 & -2 & 4\end{pmatrix}^T$, confirming full consistency between Parts 2 and 3.
