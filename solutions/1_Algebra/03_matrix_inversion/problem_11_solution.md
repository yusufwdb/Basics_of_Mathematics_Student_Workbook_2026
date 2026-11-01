# Exercise 11: Parameter and Invertibility

## 1. Problem Statement
For
$$A(t)=\begin{pmatrix}1&t\\t&1\end{pmatrix}$$
find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

## 2. Theoretical Background and Concepts
A parameterized $2 \times 2$ matrix $A(t) = \begin{pmatrix}a(t)&b(t)\\c(t)&d(t)\end{pmatrix}$ is invertible for a given real (or complex) number $t$ if and only if its determinant is non-zero:
$$\det(A(t)) = a(t)d(t) - b(t)c(t) \neq 0.$$
For all values of $t$ satisfying $\det(A(t)) \neq 0$, the explicit formula for the inverse is:
$$A(t)^{-1} = \frac{1}{\det(A(t))}\begin{pmatrix}d(t)&-b(t)\\-c(t)&a(t)\end{pmatrix}.$$

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the determinant $\det(A(t))$ and find invertible values of $t$
For
$$A(t) = \begin{pmatrix}1&t\\t&1\end{pmatrix},$$
the determinant is:
$$\det(A(t)) = (1)(1) - (t)(t) = 1 - t^2 = (1 - t)(1 + t).$$
The matrix $A(t)$ is invertible if and only if $\det(A(t)) \neq 0$:
$$1 - t^2 \neq 0 \iff t^2 \neq 1 \iff t \neq 1 \quad \text{and} \quad t \neq -1.$$
Thus, $A(t)$ is invertible for all $t \in \mathbb{R} \setminus \{-1, 1\}$.

### Step 2: Give the formula for $A(t)^{-1}$
For $t \neq \pm 1$, applying the $2 \times 2$ inverse formula yields:
$$A(t)^{-1} = \frac{1}{1 - t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix} = \begin{pmatrix}\frac{1}{1-t^2} & -\frac{t}{1-t^2}\\[6pt]-\frac{t}{1-t^2} & \frac{1}{1-t^2}\end{pmatrix}.$$

### Step 3: Explain what happens at the excluded values $t = 1$ and $t = -1$
At the excluded values $t = 1$ and $t = -1$:
1. **In the formula for $A(t)^{-1}$:** The denominator $1 - t^2$ equals $0$, causing a **division by zero** in the scalar factor $\frac{1}{1-t^2}$ (and in every entry of $A(t)^{-1}$). Furthermore, as $t \to \pm 1$, the entries $\frac{1}{1-t^2}$ and $-\frac{t}{1-t^2}$ diverge to $\pm\infty$.
2. **In the matrix $A(t)$ itself:**
   - For $t = 1$, $A(1) = \begin{pmatrix}1&1\\1&1\end{pmatrix}$, whose two rows are identical ($R_1 = R_2$).
   - For $t = -1$, $A(-1) = \begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, whose rows are opposite ($R_1 = -R_2$).
   In both cases, the rows of $A(t)$ are linearly dependent ($\operatorname{rank}(A(\pm 1)) = 1 < 2$), so $A(\pm 1)$ collapses the entire plane $\mathbb{R}^2$ onto a single line and cannot be inverted.

## 4. Verification and Consistency Checks
1. **Direct Multiplication for $t \neq \pm 1$:**
   $$A(t)A(t)^{-1} = \begin{pmatrix}1&t\\t&1\end{pmatrix} \cdot \frac{1}{1-t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix} = \frac{1}{1-t^2}\begin{pmatrix}1 - t^2 & -t + t\\t - t & -t^2 + 1\end{pmatrix} = \frac{1}{1-t^2}\begin{pmatrix}1-t^2 & 0\\0 & 1-t^2\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
2. **Special Case $t = 0$:** When $t = 0$, $A(0) = I_2$, and the formula gives $A(0)^{-1} = \frac{1}{1-0}\begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2$, which is consistent with $I_2^{-1} = I_2$.
