# Exercise 13: Undoing a Composite Transformation

## 1. Problem Statement
The matrices
$$S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad H=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$
describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

## 2. Theoretical Background and Concepts
When linear transformations are composed, their matrices are multiplied. Specifically, for $T = HS$ acting on a vector $v$:
$$Tv = (HS)v = H(Sv).$$
This means that $S$ (horizontal scaling by a factor of $2$) is applied **first**, and $H$ (horizontal shear) is applied **second**.

By the inverse of a product theorem, if $H$ and $S$ are invertible, then $T = HS$ is invertible and
$$T^{-1} = (HS)^{-1} = S^{-1}H^{-1}.$$
**Explanation of the rule “when undoing a composition of operations, we undo them from the end”:**
When $T = HS$ acts on a vector $v$ to produce $w = H(Sv)$, the most recent operation applied is $H$. To recover $v$ from $w$, we cannot undo $S$ first because the vector has been sheared by $H$ after being scaled. We must first apply $H^{-1}$ to undo the last operation $H$:
$$H^{-1}w = H^{-1}(H(Sv)) = (H^{-1}H)(Sv) = Sv.$$
Only after $H$ is undone can we apply $S^{-1}$ to undo the initial operation $S$:
$$S^{-1}(H^{-1}w) = S^{-1}(Sv) = (S^{-1}S)v = v.$$
Thus, acting with $S^{-1}$ after $H^{-1}$ corresponds to the matrix product $S^{-1}H^{-1}$.

## 3. Detailed Step-by-Step Solution

### Method 1: Compute $T = HS$ first, then find $T^{-1}$
1. Compute the product $T = HS$:
   $$T = HS = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix} = \begin{pmatrix}1(2)+1(0) & 1(0)+1(1)\\0(2)+1(0) & 0(0)+1(1)\end{pmatrix} = \begin{pmatrix}2&1\\0&1\end{pmatrix}.$$
2. Compute $\det(T) = (2)(1) - (1)(0) = 2$, and apply the $2 \times 2$ inverse formula:
   $$T^{-1} = \frac{1}{2}\begin{pmatrix}1&-1\\0&2\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&1\end{pmatrix}.$$

### Method 2: Compute $S^{-1}$ and $H^{-1}$, then multiply $S^{-1}H^{-1}$
1. Find $S^{-1}$: Since $S = \begin{pmatrix}2&0\\0&1\end{pmatrix}$ is diagonal,
   $$S^{-1} = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&1\end{pmatrix}.$$
2. Find $H^{-1}$: Since $\det(H) = 1(1) - 1(0) = 1$,
   $$H^{-1} = \frac{1}{1}\begin{pmatrix}1&-1\\0&1\end{pmatrix} = \begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
3. Multiply $S^{-1}H^{-1}$:
   $$S^{-1}H^{-1} = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&1\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix} = \begin{pmatrix}\frac{1}{2}(1)+0(0) & \frac{1}{2}(-1)+0(1)\\[4pt]0(1)+1(0) & 0(-1)+1(1)\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&1\end{pmatrix}.$$

### Comparison of Methods 1 and 2
Both methods yield the exact same inverse matrix:
$$T^{-1} = S^{-1}H^{-1} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&1\end{pmatrix}.$$

### Additional Computation: Verify that the incorrect order $H^{-1}S^{-1}$ gives a different matrix
Multiplying in the unreversed order $H^{-1}S^{-1}$ gives:
$$H^{-1}S^{-1} = \begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}\frac{1}{2}&0\\[4pt]0&1\end{pmatrix} = \begin{pmatrix}1\left(\frac{1}{2}\right)+(-1)(0) & 1(0)+(-1)(1)\\[4pt]0\left(\frac{1}{2}\right)+1(0) & 0(0)+1(1)\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-1\\[4pt]0&1\end{pmatrix}.$$
Comparing the $(1,2)$-entries, we see that $-\frac{1}{2} \neq -1$, so:
$$H^{-1}S^{-1} = \begin{pmatrix}\frac{1}{2}&-1\\[4pt]0&1\end{pmatrix} \neq \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&1\end{pmatrix} = T^{-1}.$$

## 4. Verification and Consistency Checks
1. **Verify $T T^{-1} = I_2$:**
   $$TT^{-1} = \begin{pmatrix}2&1\\0&1\end{pmatrix}\begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&1\end{pmatrix} = \begin{pmatrix}2\left(\frac{1}{2}\right)+1(0) & 2\left(-\frac{1}{2}\right)+1(1)\\[4pt]0 & 1\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
2. **Verify that $T(H^{-1}S^{-1}) \neq I_2$:**
   $$T(H^{-1}S^{-1}) = \begin{pmatrix}2&1\\0&1\end{pmatrix}\begin{pmatrix}\frac{1}{2}&-1\\[4pt]0&1\end{pmatrix} = \begin{pmatrix}1&-2+1\\0&1\end{pmatrix} = \begin{pmatrix}1&-1\\0&1\end{pmatrix} \neq I_2.$$
   This confirms that only the reversed order $S^{-1}H^{-1}$ properly inverts $T = HS$.
