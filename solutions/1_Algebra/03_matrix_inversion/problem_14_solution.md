# Exercise 14: A Matrix That Is Its Own Inverse

## 1. Problem Statement
Assume that a square matrix $A$ satisfies
$$A^2=I.$$
Show that
$$A^{-1}=A.$$
Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

## 2. Theoretical Background and Concepts
By definition, a square matrix $B$ is the inverse of an $n \times n$ matrix $A$ (written $B = A^{-1}$) if and only if
$$AB = I_n \quad \text{and} \quad BA = I_n.$$
The inverse of a matrix, when it exists, is **unique**.

A matrix $A$ satisfying $A^2 = I_n$ (equivalently, $A = A^{-1}$) is called an **involutory matrix** (or an **involution**). Geometrically, reflections across a line in $\mathbb{R}^2$ or swapping coordinates are classic examples of involutions: repeating the transformation twice returns every point to its starting position.

## 3. Detailed Step-by-Step Solution

### Part 1: Proof that $A^2 = I \implies A^{-1} = A$
By the definition of a matrix square, $A^2 = AA$. Therefore, the given equation $A^2 = I$ can be written as:
$$A \cdot A = I.$$
Comparing this directly with the definition of the inverse ($AB = I$ and $BA = I$ for $B = A$), we see that the matrix $B = A$ satisfies both:
$$AB = A \cdot A = I \quad \text{and} \quad BA = A \cdot A = I.$$
By the uniqueness of the matrix inverse, $A$ is invertible and its inverse is $A$ itself:
$$A^{-1} = A.$$

### Part 2: Example of a $2 \times 2$ matrix $A \neq I, -I$ with $A^2 = I$
Consider the reflection matrix across the $x$-axis (or alternatively the permutation matrix swapping coordinates):
$$A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
Clearly, $A \neq I_2 = \begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $A \neq -I_2 = \begin{pmatrix}-1&0\\0&-1\end{pmatrix}$.

*(Note: Another valid non-diagonal example is the coordinate-swap reflection matrix $P = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, or more generally $\begin{pmatrix}a&b\\c&-a\end{pmatrix}$ with $a^2 + bc = 1$.)*

### Part 3: Verify the example by multiplication
We compute $A^2 = A \cdot A$ for $A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$:
$$A^2 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix} = \begin{pmatrix}1(1)+0(0) & 1(0)+0(-1)\\0(1)+(-1)(0) & 0(0)+(-1)(-1)\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
Thus $A^2 = I_2$, so $A^{-1} = A$.

## 4. Verification and Consistency Checks
1. **Formula Verification for $A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$:**
   Here $\det(A) = (1)(-1) - 0 = -1$. Applying the $2 \times 2$ inverse formula gives:
   $$A^{-1} = \frac{1}{-1}\begin{pmatrix}-1&0\\0&1\end{pmatrix} = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = A.$$
2. **Verification for a non-diagonal example $P = \begin{pmatrix}0&1\\1&0\end{pmatrix}$:**
   $$P^2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0+1 & 0+0\\0+0 & 1+0\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2,$$
   and $\det(P) = -1$, $P^{-1} = \frac{1}{-1}\begin{pmatrix}0&-1\\-1&0\end{pmatrix} = \begin{pmatrix}0&1\\1&0\end{pmatrix} = P$. Both examples are consistent.
