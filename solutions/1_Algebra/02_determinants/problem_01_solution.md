# Exercise 1: Determinant of a 2×2 Matrix

## 1. Problem Statement

Compute
$$\det\begin{pmatrix}3&-2\\5&4\end{pmatrix},\qquad \det\begin{pmatrix}1&7\\2&14\end{pmatrix}.$$
Which matrix is invertible? Justify your answer.

## 2. Theoretical Background and Concepts

- **Determinant of a $2 \times 2$ Matrix:** For a $2 \times 2$ matrix $M = \begin{pmatrix}a&b\\c&d\end{pmatrix}$, the determinant is defined as the product of the entries on the main diagonal minus the product of the entries on the anti-diagonal:
  $$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc.$$
- **Invertibility Criterion:** A square matrix $M$ is **invertible** (nonsingular) if and only if its determinant is nonzero:
  $$M \text{ is invertible} \iff \det M \neq 0.$$
  Specifically, for a $2 \times 2$ matrix with $\det M \neq 0$, its inverse is given explicitly by $M^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$. If $\det M = 0$, the matrix is **singular** (not invertible).

## 3. Detailed Step-by-Step Solution

Let us denote the two given matrices by
$$A = \begin{pmatrix}3&-2\\5&4\end{pmatrix}, \qquad B = \begin{pmatrix}1&7\\2&14\end{pmatrix}.$$

### 1. Determinant of the First Matrix $A$
Applying the $2 \times 2$ determinant formula $\det A = a_{11}a_{22} - a_{12}a_{21}$:
$$\det\begin{pmatrix}3&-2\\5&4\end{pmatrix} = 3 \cdot 4 - (-2) \cdot 5 = 12 - (-10) = 12 + 10 = 22.$$

### 2. Determinant of the Second Matrix $B$
Applying the $2 \times 2$ determinant formula $\det B = b_{11}b_{22} - b_{12}b_{21}$:
$$\det\begin{pmatrix}1&7\\2&14\end{pmatrix} = 1 \cdot 14 - 7 \cdot 2 = 14 - 14 = 0.$$

### 3. Determining Which Matrix Is Invertible
- **Matrix $A = \begin{pmatrix}3&-2\\5&4\end{pmatrix}$ is invertible** because $\det A = 22 \neq 0$.
- **Matrix $B = \begin{pmatrix}1&7\\2&14\end{pmatrix}$ is NOT invertible (singular)** because $\det B = 0$. (Notice also that the second row of $B$, $(2, 14)$, is $2$ times the first row $(1, 7)$, meaning the rows are linearly dependent.)

## 4. Verification and Consistency Checks

1. **Explicit Inverse Check for $A$:** Since $\det A = 22 \neq 0$, we can write down $A^{-1}$ and verify $A A^{-1} = I$:
   $$A^{-1} = \frac{1}{22}\begin{pmatrix}4&2\\-5&3\end{pmatrix} \implies A A^{-1} = \frac{1}{22}\begin{pmatrix}3&-2\\5&4\end{pmatrix}\begin{pmatrix}4&2\\-5&3\end{pmatrix} = \frac{1}{22}\begin{pmatrix}12+10 & 6-6\\20-20 & 10+12\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I. \quad \checkmark$$
2. **Non-invertibility Check for $B$:** Notice that $B\begin{pmatrix}-7\\1\end{pmatrix} = \begin{pmatrix}1(-7)+7(1)\\2(-7)+14(1)\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$. Because $B$ maps a nonzero vector to the zero vector, $B$ cannot have an inverse (otherwise multiplying by $B^{-1}$ would give $\begin{pmatrix}-7\\1\end{pmatrix} = \begin{pmatrix}0\\0\end{pmatrix}$, a contradiction).
