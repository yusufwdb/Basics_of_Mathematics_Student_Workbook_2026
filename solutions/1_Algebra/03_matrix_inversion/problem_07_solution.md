# Exercise 7: Inverse of a Product

## 1. Problem Statement
For
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\0&3\end{pmatrix}$$
compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

## 2. Theoretical Background and Concepts
If $A$ and $B$ are invertible $n \times n$ matrices, then their product $AB$ is also invertible, and the **inverse of a product** is the product of the inverses in the **reverse order**:
$$(AB)^{-1} = B^{-1}A^{-1}.$$
**Why the order is reversed (Algebraic and Conceptual Meaning):**
1. *Algebraic reason:* To reduce $AB$ to the identity matrix $I$, we must place $B^{-1}$ adjacent to $B$ so that $BB^{-1} = I$ collapses in the middle:
   $$(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I.$$
   Because matrix multiplication is generally non-commutative ($AB \neq BA$), $(AB)(A^{-1}B^{-1})$ does not cancel in general.
2. *Operational ("socks and shoes") analogy:* If a composite transformation $AB$ is applied to a vector $x$ as $(AB)x = A(Bx)$, then $B$ acts first and $A$ acts second. To undo the composite process, we must first undo the *last* operation performed (apply $A^{-1}$), and then undo the *first* operation performed (apply $B^{-1}$), resulting in $B^{-1}(A^{-1}y) = (B^{-1}A^{-1})y$.

## 3. Detailed Step-by-Step Solution

### Method 1: Compute $AB$ first, then find $(AB)^{-1}$
First, multiply $A$ and $B$:
$$AB = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&3\end{pmatrix} = \begin{pmatrix}1(2)+1(0) & 1(0)+1(3)\\0(2)+1(0) & 0(0)+1(3)\end{pmatrix} = \begin{pmatrix}2&3\\0&3\end{pmatrix}.$$
Next, compute $\det(AB) = (2)(3) - (3)(0) = 6$, and apply the $2 \times 2$ inverse formula to $AB$:
$$(AB)^{-1} = \frac{1}{6}\begin{pmatrix}3&-3\\0&2\end{pmatrix} = \begin{pmatrix}\frac{3}{6}&-\frac{3}{6}\\[4pt]0&\frac{2}{6}\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&\frac{1}{3}\end{pmatrix}.$$

### Method 2: Compute $A^{-1}$ and $B^{-1}$ separately, then multiply $B^{-1}A^{-1}$
1. Find $A^{-1}$: Since $\det(A) = 1(1) - 1(0) = 1$,
   $$A^{-1} = \frac{1}{1}\begin{pmatrix}1&-1\\0&1\end{pmatrix} = \begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
2. Find $B^{-1}$: Since $B$ is a diagonal matrix with non-zero diagonal entries $2$ and $3$ (or by $\det(B) = 6$),
   $$B^{-1} = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&\frac{1}{3}\end{pmatrix}.$$
3. Multiply $B^{-1}A^{-1}$ in that order:
   $$B^{-1}A^{-1} = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&\frac{1}{3}\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix} = \begin{pmatrix}\frac{1}{2}(1)+0(0) & \frac{1}{2}(-1)+0(1)\\[4pt]0(1)+\frac{1}{3}(0) & 0(-1)+\frac{1}{3}(1)\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&\frac{1}{3}\end{pmatrix}.$$

### Comparison
Both calculations yield the exact same matrix:
$$(AB)^{-1} = B^{-1}A^{-1} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&\frac{1}{3}\end{pmatrix}.$$

## 4. Verification and Consistency Checks
1. **Direct Multiplication Check:**
   $$(AB)(B^{-1}A^{-1}) = \begin{pmatrix}2&3\\0&3\end{pmatrix}\begin{pmatrix}\frac{1}{2}&-\frac{1}{2}\\[4pt]0&\frac{1}{3}\end{pmatrix} = \begin{pmatrix}2\left(\frac{1}{2}\right)+3(0) & 2\left(-\frac{1}{2}\right)+3\left(\frac{1}{3}\right)\\[4pt]0\left(\frac{1}{2}\right)+3(0) & 0\left(-\frac{1}{2}\right)+3\left(\frac{1}{3}\right)\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
2. **Checking that the unreversed product $A^{-1}B^{-1}$ is different:**
   $$A^{-1}B^{-1} = \begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}\frac{1}{2}&0\\[4pt]0&\frac{1}{3}\end{pmatrix} = \begin{pmatrix}\frac{1}{2}&-\frac{1}{3}\\[4pt]0&\frac{1}{3}\end{pmatrix} \neq (AB)^{-1}.$$
   Indeed, $(AB)(A^{-1}B^{-1}) = \begin{pmatrix}2&3\\0&3\end{pmatrix}\begin{pmatrix}\frac{1}{2}&-\frac{1}{3}\\0&\frac{1}{3}\end{pmatrix} = \begin{pmatrix}1&\frac{1}{3}\\0&1\end{pmatrix} \neq I_2$, confirming why the reversed order is essential.
