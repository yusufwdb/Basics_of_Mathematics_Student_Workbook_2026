# Exercise 7: Identity Matrix, Zero Matrix, and Powers

## 1. Problem Statement

For
$$A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$$
compute
$$AI,\qquad IA,\qquad A+0,\qquad A^2,\qquad A^3.$$
Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

## 2. Theoretical Background and Concepts

- **Zero Matrix ($0$):** The $m \times n$ zero matrix $0_{m\times n}$ has all entries equal to $0$. It serves as the **additive identity** (neutral element for addition): $A + 0 = 0 + A = A$.
- **Identity Matrix ($I$):** The $n \times n$ identity matrix $I_n$ has $1$s on the main diagonal and $0$s elsewhere. For $n=2$, $I = \begin{pmatrix}1&0\\0&1\end{pmatrix}$. It serves as the **multiplicative identity** (neutral element for matrix multiplication): $AI = IA = A$.
- **Matrix Powers:** For a square matrix $A$ and positive integer $k$, the power $A^k$ is defined recursively by $A^1 = A$ and $A^k = A^{k-1}A$ (multiplying $k$ copies of $A$).

## 3. Detailed Step-by-Step Solution

Here $A$ is a $2 \times 2$ matrix, so $I = I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $0 = 0_{2\times 2} = \begin{pmatrix}0&0\\0&0\end{pmatrix}$.

### 1. Computing $AI$, $IA$, and $A+0$
- **$AI$:**
  $$AI = \begin{pmatrix}2&1\\0&2\end{pmatrix}\begin{pmatrix}1&0\\0&1\end{pmatrix} = \begin{pmatrix}2(1)+1(0) & 2(0)+1(1)\\0(1)+2(0) & 0(0)+2(1)\end{pmatrix} = \begin{pmatrix}2&1\\0&2\end{pmatrix} = A.$$
- **$IA$:**
  $$IA = \begin{pmatrix}1&0\\0&1\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix} = \begin{pmatrix}1(2)+0(0) & 1(1)+0(2)\\0(2)+1(0) & 0(1)+1(2)\end{pmatrix} = \begin{pmatrix}2&1\\0&2\end{pmatrix} = A.$$
- **$A+0$:**
  $$A+0 = \begin{pmatrix}2&1\\0&2\end{pmatrix} + \begin{pmatrix}0&0\\0&0\end{pmatrix} = \begin{pmatrix}2+0 & 1+0\\0+0 & 2+0\end{pmatrix} = \begin{pmatrix}2&1\\0&2\end{pmatrix} = A.$$

### 2. Computing $A^2$ and $A^3$
- **$A^2 = A \cdot A$:**
  $$A^2 = \begin{pmatrix}2&1\\0&2\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix} = \begin{pmatrix}2(2)+1(0) & 2(1)+1(2)\\0(2)+2(0) & 0(1)+2(2)\end{pmatrix} = \begin{pmatrix}4&4\\0&4\end{pmatrix}.$$
- **$A^3 = A^2 \cdot A$:**
  $$A^3 = \begin{pmatrix}4&4\\0&4\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix} = \begin{pmatrix}4(2)+4(0) & 4(1)+4(2)\\0(2)+4(0) & 0(1)+4(2)\end{pmatrix} = \begin{pmatrix}8&12\\0&8\end{pmatrix}.$$

### 3. Roles of $I$ and $0$, and Observed Pattern in $A^n$
- **Roles of $I$ and $0$:** The matrix $0$ plays the exact same role in matrix addition as the number $0$ plays in real addition ($A+0=A$). The identity matrix $I$ plays the exact same role in matrix multiplication as the number $1$ plays in real multiplication ($AI=IA=A$).
- **Pattern in $A^n$:** Writing $A^1, A^2, A^3$ in terms of powers of $2$:
  $$A^1 = \begin{pmatrix}2^1 & 1\cdot 2^0\\0 & 2^1\end{pmatrix}, \qquad A^2 = \begin{pmatrix}2^2 & 2\cdot 2^1\\0 & 2^2\end{pmatrix}, \qquad A^3 = \begin{pmatrix}2^3 & 3\cdot 2^2\\0 & 2^3\end{pmatrix}.$$
  We observe that for every positive integer $n$:
  1. The matrix remains upper triangular (the $(2,1)$-entry is always $0$).
  2. The diagonal entries are powers of $2$, namely $2^n$.
  3. The $(1,2)$-entry follows the formula $n \cdot 2^{n-1}$.
  Thus, the general formula is:
  $$A^n = \begin{pmatrix}2^n & n 2^{n-1}\\0 & 2^n\end{pmatrix}.$$

## 4. Verification and Consistency Checks

- **Binomial Decomposition Verification:** We can write $A = 2I + N$, where $N = \begin{pmatrix}0&1\\0&0\end{pmatrix}$. Since $I$ and $N$ commute and $N^2 = \begin{pmatrix}0&0\\0&0\end{pmatrix} = 0$, the binomial theorem gives:
  $$A^n = (2I + N)^n = (2I)^n + \binom{n}{1}(2I)^{n-1}N = 2^n I + n 2^{n-1} N = \begin{pmatrix}2^n & n 2^{n-1}\\0 & 2^n\end{pmatrix}.$$
  For $n=2$, this gives $\begin{pmatrix}4 & 2\cdot 2^1\\0 & 4\end{pmatrix} = \begin{pmatrix}4&4\\0&4\end{pmatrix}$, and for $n=3$, $\begin{pmatrix}8 & 3\cdot 2^2\\0 & 8\end{pmatrix} = \begin{pmatrix}8&12\\0&8\end{pmatrix}$, confirming our calculations.
- **Determinant Check:** $\det(A) = 4$, so $\det(A^2) = 4^2 = 16$ ($\det\begin{pmatrix}4&4\\0&4\end{pmatrix} = 16$) and $\det(A^3) = 4^3 = 64$ ($\det\begin{pmatrix}8&12\\0&8\end{pmatrix} = 64$). $\checkmark$
