# Exercise 6: Parameter and Invertibility

## 1. Problem Statement

For
$$A(t)=\begin{pmatrix}t&1\\2&t\end{pmatrix}$$
find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

## 2. Theoretical Background and Concepts

- **Invertibility Criterion via Determinants:** A square matrix $A$ over $\mathbb{R}$ (or $\mathbb{C}$) is **not invertible** (singular) if and only if its determinant equals zero:
  $$A(t) \text{ is not invertible} \iff \det A(t) = 0.$$
- **Why $\det A = 0$ Implies Non-Invertibility:**
  1. *Algebraic reason:* If $A$ were invertible with inverse $A^{-1}$, then $A A^{-1} = I$, and by the multiplicativity of determinants we would have $(\det A)(\det A^{-1}) = \det I = 1$. If $\det A = 0$, the left side is $0 \cdot \det A^{-1} = 0 \neq 1$, a contradiction.
  2. *Row/Column Dependence reason:* $\det A = 0$ if and only if the rows (and columns) of $A$ are linearly dependent, which means $A$ fails to be a one-to-one and onto linear transformation.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant $\det A(t)$ as a Function of $t$
Using the formula for a $2 \times 2$ determinant, $\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad - bc$:
$$\det A(t) = \det\begin{pmatrix}t&1\\2&t\end{pmatrix} = t \cdot t - 1 \cdot 2 = t^2 - 2.$$

### Step 2: Solve $\det A(t) = 0$ for the Parameter $t$
Set the determinant equal to zero:
$$t^2 - 2 = 0 \iff t^2 = 2 \iff (t - \sqrt{2})(t + \sqrt{2}) = 0.$$
Therefore, the values of $t$ for which $A(t)$ is **not invertible** are:
$$t = \sqrt{2} \quad \text{and} \quad t = -\sqrt{2} \qquad (t = \pm\sqrt{2}).$$

### Step 3: Explaining the Relation to $\det A(t) = 0$
A square matrix $A(t)$ has an inverse $A(t)^{-1}$ if and only if $\det A(t) \neq 0$ (in fact, for a $2 \times 2$ matrix, the formula for the inverse is $A(t)^{-1} = \frac{1}{\det A(t)}\begin{pmatrix}t&-1\\-2&t\end{pmatrix}$, which involves division by $\det A(t) = t^2 - 2$). When $\det A(t) = 0$ (which happens precisely at $t = \sqrt{2}$ and $t = -\sqrt{2}$), division by $\det A(t)$ is undefined, the two rows of $A(t)$ become scalar multiples of each other, the linear transformation collapses $\mathbb{R}^2$ onto a 1-dimensional line, and the matrix cannot be inverted. For all other values $t \in \mathbb{R} \setminus \{-\sqrt{2}, \sqrt{2}\}$, $\det A(t) \neq 0$ and $A(t)$ is invertible.

## 4. Verification and Consistency Checks

Let us substitute $t = \sqrt{2}$ and $t = -\sqrt{2}$ directly into $A(t)$ and check that the rows are linearly dependent in both cases:
1. **Case $t = \sqrt{2}$:**
   $$A(\sqrt{2}) = \begin{pmatrix}\sqrt{2}&1\\2&\sqrt{2}\end{pmatrix}.$$
   Notice that multiplying the first row $R_1 = (\sqrt{2}, 1)$ by $\sqrt{2}$ gives $(\sqrt{2}\cdot\sqrt{2}, \sqrt{2}\cdot 1) = (2, \sqrt{2}) = R_2$. Since $R_2 = \sqrt{2} R_1$, the rows are linearly dependent and $\det A(\sqrt{2}) = 2 - 2 = 0$. $\checkmark$
2. **Case $t = -\sqrt{2}$:**
   $$A(-\sqrt{2}) = \begin{pmatrix}-\sqrt{2}&1\\2&-\sqrt{2}\end{pmatrix}.$$
   Multiplying the first row $R_1 = (-\sqrt{2}, 1)$ by $-\sqrt{2}$ gives $(2, -\sqrt{2}) = R_2$. Since $R_2 = -\sqrt{2} R_1$, the rows are linearly dependent and $\det A(-\sqrt{2}) = (-\sqrt{2})^2 - 2 = 2 - 2 = 0$. $\checkmark$
