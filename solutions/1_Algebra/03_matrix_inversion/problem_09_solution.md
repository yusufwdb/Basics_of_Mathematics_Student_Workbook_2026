# Exercise 9: Matrix Equation

## 1. Problem Statement
Given
$$A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}3&1\\2&4\end{pmatrix}.$$
Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

## 2. Theoretical Background and Concepts
In a matrix equation of the form
$$AX = B,$$
where $A$ is an invertible $n \times n$ matrix and $X, B$ are $n \times m$ matrices, $A$ multiplies $X$ on the **left**. Because matrix multiplication is **not commutative** ($BA^{-1} \neq A^{-1}B$ in general), we must multiply both sides of the equation by $A^{-1}$ on the **left** (pre-multiplication) so that $A^{-1}$ is adjacent to $A$:
$$A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies I_n X = A^{-1}B \implies X = A^{-1}B.$$
If instead we multiplied on the right to get $AXA^{-1} = BA^{-1}$, the matrices $A$ and $A^{-1}$ would be separated by $X$ and could not cancel to $I_n$. (By contrast, an equation of the form $XA = B$ would require multiplying by $A^{-1}$ on the right: $X = BA^{-1}$.)

## 3. Detailed Step-by-Step Solution

### Step 1: Decide which side to multiply by $A^{-1}$
Since $A$ appears on the **left** of $X$ in $AX = B$, we must multiply both sides on the **left** by $A^{-1}$, giving the formula:
$$X = A^{-1}B.$$

### Step 2: Find $A^{-1}$
For
$$A = \begin{pmatrix}1&2\\0&1\end{pmatrix},$$
the determinant is $\det(A) = (1)(1) - (2)(0) = 1 \neq 0$. Using the $2 \times 2$ inverse formula:
$$A^{-1} = \frac{1}{1}\begin{pmatrix}1&-2\\0&1\end{pmatrix} = \begin{pmatrix}1&-2\\0&1\end{pmatrix}.$$

### Step 3: Compute $X = A^{-1}B$
We multiply $A^{-1}$ on the left of $B$:
$$X = A^{-1}B = \begin{pmatrix}1&-2\\0&1\end{pmatrix}\begin{pmatrix}3&1\\2&4\end{pmatrix}.$$
Computing each entry of $X$:
- $(1,1)$-entry: $1(3) + (-2)(2) = 3 - 4 = -1$
- $(1,2)$-entry: $1(1) + (-2)(4) = 1 - 8 = -7$
- $(2,1)$-entry: $0(3) + 1(2) = 0 + 2 = 2$
- $(2,2)$-entry: $0(1) + 1(4) = 0 + 4 = 4$

Therefore, the solution matrix is:
$$X = \begin{pmatrix}-1&-7\\2&4\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We verify our solution by computing the product $AX$ and checking that it equals $B$:
$$AX = \begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}-1&-7\\2&4\end{pmatrix} = \begin{pmatrix}1(-1)+2(2) & 1(-7)+2(4)\\0(-1)+1(2) & 0(-7)+1(4)\end{pmatrix} = \begin{pmatrix}-1+4 & -7+8\\0+2 & 0+4\end{pmatrix} = \begin{pmatrix}3&1\\2&4\end{pmatrix} = B.$$
Note also that if we had mistakenly multiplied on the right ($BA^{-1}$), we would have obtained
$$BA^{-1} = \begin{pmatrix}3&1\\2&4\end{pmatrix}\begin{pmatrix}1&-2\\0&1\end{pmatrix} = \begin{pmatrix}3&-5\\2&0\end{pmatrix} \neq X,$$
which does not satisfy $AX = B$. This confirms both the solution $X$ and the necessity of left-multiplication by $A^{-1}$.
