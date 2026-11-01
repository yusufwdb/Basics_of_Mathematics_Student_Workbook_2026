# Exercise 12: Finding Inverses Without Starting from Scratch

## 1. Problem Statement
It is known that
$$A^{-1}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}.$$
Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

## 2. Theoretical Background and Concepts
Let $A$ be an invertible $n \times n$ matrix and let $c \neq 0$ be a non-zero scalar. The following algebraic properties of matrix inverses allow us to compute inverses of related matrices directly from $A^{-1}$ without ever computing $A$:
1. **Inverse of a Scalar Multiple:**
   $$(cA)^{-1} = \frac{1}{c}A^{-1},$$
   because $(cA)\left(\frac{1}{c}A^{-1}\right) = \left(c \cdot \frac{1}{c}\right)(AA^{-1}) = 1 \cdot I_n = I_n$.
2. **Inverse of a Transpose:**
   $$(A^T)^{-1} = (A^{-1})^T,$$
   because $A^T (A^{-1})^T = (A^{-1}A)^T = I_n^T = I_n$ (using the transpose of a product rule $(XY)^T = Y^T X^T$).
3. **Inverse of a Matrix Power:**
   $$(A^k)^{-1} = (A^{-1})^k \quad \text{for any positive integer } k.$$
   In particular, for $k = 2$, applying the product rule $(AB)^{-1} = B^{-1}A^{-1}$ with $B = A$ gives:
   $$(A^2)^{-1} = (AA)^{-1} = A^{-1}A^{-1} = (A^{-1})^2.$$

## 3. Detailed Step-by-Step Solution

### Part 1: Compute $(3A)^{-1}$
**Justification:** Using the scalar multiple property $(cA)^{-1} = \frac{1}{c}A^{-1}$ with $c = 3$:
$$(3A)^{-1} = \frac{1}{3}A^{-1} = \frac{1}{3}\begin{pmatrix}2&-1\\-3&2\end{pmatrix} = \begin{pmatrix}\frac{2}{3}&-\frac{1}{3}\\[4pt]-1&\frac{2}{3}\end{pmatrix}.$$

### Part 2: Compute $(A^T)^{-1}$
**Justification:** Using the transpose property $(A^T)^{-1} = (A^{-1})^T$, we simply transpose the given matrix $A^{-1}$ (interchanging its rows and columns):
$$(A^T)^{-1} = (A^{-1})^T = \begin{pmatrix}2&-1\\-3&2\end{pmatrix}^T = \begin{pmatrix}2&-3\\-1&2\end{pmatrix}.$$

### Part 3: Compute $(A^2)^{-1}$
**Justification:** Using the product/power property $(A^2)^{-1} = (AA)^{-1} = A^{-1}A^{-1} = (A^{-1})^2$, we multiply $A^{-1}$ by itself:
$$(A^2)^{-1} = (A^{-1})^2 = \begin{pmatrix}2&-1\\-3&2\end{pmatrix}\begin{pmatrix}2&-1\\-3&2\end{pmatrix}.$$
Computing each entry of the product:
- $(1,1)$-entry: $2(2) + (-1)(-3) = 4 + 3 = 7$
- $(1,2)$-entry: $2(-1) + (-1)(2) = -2 - 2 = -4$
- $(2,1)$-entry: $(-3)(2) + 2(-3) = -6 - 6 = -12$
- $(2,2)$-entry: $(-3)(-1) + 2(2) = 3 + 4 = 7$

Thus,
$$(A^2)^{-1} = \begin{pmatrix}7&-4\\-12&7\end{pmatrix}.$$

## 4. Verification and Consistency Checks
Although the problem required finding the inverses without finding $A$, we can now independently verify our answers by noting that $A = (A^{-1})^{-1} = \frac{1}{4-3}\begin{pmatrix}2&1\\3&2\end{pmatrix} = \begin{pmatrix}2&1\\3&2\end{pmatrix}$:
1. **Check $(3A)(3A)^{-1}$:** $3A = \begin{pmatrix}6&3\\9&6\end{pmatrix}$, and
   $$\begin{pmatrix}6&3\\9&6\end{pmatrix}\begin{pmatrix}\frac{2}{3}&-\frac{1}{3}\\-1&\frac{2}{3}\end{pmatrix} = \begin{pmatrix}4-3 & -2+2\\6-6 & -3+4\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
2. **Check $A^T(A^T)^{-1}$:** $A^T = \begin{pmatrix}2&3\\1&2\end{pmatrix}$, and
   $$\begin{pmatrix}2&3\\1&2\end{pmatrix}\begin{pmatrix}2&-3\\-1&2\end{pmatrix} = \begin{pmatrix}4-3 & -6+6\\2-2 & -3+4\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
3. **Check $A^2(A^2)^{-1}$:** $A^2 = \begin{pmatrix}2&1\\3&2\end{pmatrix}\begin{pmatrix}2&1\\3&2\end{pmatrix} = \begin{pmatrix}7&4\\12&7\end{pmatrix}$, and
   $$\begin{pmatrix}7&4\\12&7\end{pmatrix}\begin{pmatrix}7&-4\\-12&7\end{pmatrix} = \begin{pmatrix}49-48 & -28+28\\84-84 & -48+49\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
All three results are verified.
