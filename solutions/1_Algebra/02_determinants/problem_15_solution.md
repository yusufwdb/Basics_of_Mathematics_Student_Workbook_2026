# Exercise 15: Combining Determinant Properties

## 1. Problem Statement

Let $A$ and $B$ be invertible $2\times2$ matrices with
$$\det A=-2,\qquad \det B=3.$$
Without finding the entries of the matrices, compute
$$\det\left(B^{-1}A^TB\right).$$
State the determinant properties you use in order and explain why the factors involving $B$ eventually cancel.

## 2. Theoretical Background and Concepts

For any $n \times n$ square matrices $X, Y, Z$ (with $B$ invertible), the determinant satisfies three key algebraic properties:
1. **Multiplicativity of the Determinant (Product Rule):**
   $$\det(XY) = (\det X)(\det Y), \quad \text{and by associativity,} \quad \det(XYZ) = (\det X)(\det Y)(\det Z).$$
2. **Determinant of an Inverse Matrix:** Since $B B^{-1} = I$ and $\det I = 1$,
   $$\det(B^{-1}) = \frac{1}{\det B} = (\det B)^{-1}.$$
3. **Determinant of a Transpose:**
   $$\det(A^T) = \det A.$$

## 3. Detailed Step-by-Step Solution

We wish to compute $\det\left(B^{-1} A^T B\right)$ given $\det A = -2$ and $\det B = 3$.

### Step-by-Step Calculation with Properties Stated in Order

1. **Property 1 — Multiplicativity of the Determinant ($\det(XYZ) = \det X \cdot \det Y \cdot \det Z$):**
   Split the determinant of the triple matrix product $B^{-1} A^T B$ into the product of the three individual determinants:
   $$\det\left(B^{-1} A^T B\right) = \det(B^{-1}) \cdot \det(A^T) \cdot \det(B).$$

2. **Property 2 — Determinant of an Inverse Matrix ($\det(B^{-1}) = \frac{1}{\det B}$):**
   Since $B$ is invertible ($\det B = 3 \neq 0$), replace $\det(B^{-1})$ with $\frac{1}{\det B}$:
   $$\det\left(B^{-1} A^T B\right) = \frac{1}{\det B} \cdot \det(A^T) \cdot \det(B).$$

3. **Property 3 — Invariance Under Transposition ($\det(A^T) = \det A$):**
   Replace $\det(A^T)$ with $\det A$:
   $$\det\left(B^{-1} A^T B\right) = \frac{1}{\det B} \cdot \det A \cdot \det B.$$

4. **Cancellation and Substitution of Numerical Values:**
   Using the commutativity and associativity of real-number multiplication:
   $$\det\left(B^{-1} A^T B\right) = \left(\frac{1}{\det B} \cdot \det B\right) \cdot \det A = \left(\frac{1}{3} \cdot 3\right) \cdot (-2) = 1 \cdot (-2) = -2.$$

### Explanation of Why the Factors Involving $B$ Cancel
In the matrix expression $B^{-1} A^T B$, we cannot directly cancel $B^{-1}$ and $B$ as matrices because matrix multiplication is not commutative ($A^T B \neq B A^T$ in general, so $B^{-1} A^T B \neq A^T$).
However, once we apply the determinant, the matrix product becomes a **product of real numbers** (scalars): $\det(B^{-1}) \cdot \det(A^T) \cdot \det(B)$. Because multiplication of real numbers **is commutative and associative**, we can rearrange the scalar factors to pair $\det(B^{-1}) = \frac{1}{\det B}$ directly with $\det B$. Since $\det B = 3 \neq 0$, a nonzero number multiplied by its multiplicative inverse is always $1$:
$$\det(B^{-1})\det(B) = \frac{1}{\det B}\det(B) = 1 \quad \left(\text{equivalently, } \det(B^{-1}B) = \det(I) = 1\right).$$
Geometrically, $B^{-1} A^T B$ is a **similarity transformation** (change of basis) of $A^T$: $B$ changes coordinates into a new basis, $A^T$ acts in that basis, and $B^{-1}$ converts back to the original basis, so the net area/volume scaling factor ($\det$) is completely independent of the basis change $B$.

## 4. Verification and Consistency Checks

Let us verify this result with concrete $2 \times 2$ non-commuting matrices $A$ and $B$ satisfying $\det A = -2$ and $\det B = 3$:
Choose
$$A = \begin{pmatrix}2&1\\0&-1\end{pmatrix} \quad (\det A = -2), \qquad B = \begin{pmatrix}3&1\\0&1\end{pmatrix} \quad (\det B = 3).$$
Then
$$A^T = \begin{pmatrix}2&0\\1&-1\end{pmatrix}, \qquad B^{-1} = \frac{1}{3}\begin{pmatrix}1&-1\\0&3\end{pmatrix}.$$
Computing $B^{-1} A^T B$ explicitly:
$$A^T B = \begin{pmatrix}2&0\\1&-1\end{pmatrix}\begin{pmatrix}3&1\\0&1\end{pmatrix} = \begin{pmatrix}6&2\\3&0\end{pmatrix},$$
$$B^{-1} A^T B = \frac{1}{3}\begin{pmatrix}1&-1\\0&3\end{pmatrix}\begin{pmatrix}6&2\\3&0\end{pmatrix} = \frac{1}{3}\begin{pmatrix}3&2\\9&0\end{pmatrix} = \begin{pmatrix}1 & 2/3\\3 & 0\end{pmatrix}.$$
Notice that $B^{-1}A^TB \neq A^T$, yet its determinant is:
$$\det\left(B^{-1} A^T B\right) = 1 \cdot 0 - \frac{2}{3} \cdot 3 = 0 - 2 = -2. \quad \checkmark$$
This confirms both that $B^{-1} A^T B \neq A^T$ in general and that its determinant is always $-2$.
