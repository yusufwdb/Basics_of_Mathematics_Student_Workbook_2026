# Exercise 8: Inverse of a Transformation

## 1. Problem Statement
The matrix
$$S=\begin{pmatrix}2&0\\0&\frac12\end{pmatrix}$$
describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

## 2. Theoretical Background and Concepts
A $2 \times 2$ diagonal matrix of the form
$$S = \begin{pmatrix}s_x & 0 \\ 0 & s_y\end{pmatrix}$$
represents a **scaling transformation** of the Cartesian plane $\mathbb{R}^2$: for any vector $v = \begin{pmatrix}x\\y\end{pmatrix}$,
$$Sv = \begin{pmatrix}s_x x \\ s_y y\end{pmatrix},$$
which scales (stretches or compresses) the horizontal $x$-coordinate by a factor of $s_x$ and the vertical $y$-coordinate by a factor of $s_y$.

When $s_x \neq 0$ and $s_y \neq 0$, the inverse matrix is obtained by taking the reciprocals of the diagonal scaling factors:
$$S^{-1} = \begin{pmatrix}\frac{1}{s_x} & 0 \\[4pt] 0 & \frac{1}{s_y}\end{pmatrix}.$$
Geometrically, $S^{-1}$ represents the **inverse scaling transformation** that undoes the distortion of $S$ by scaling each coordinate by the reciprocal factor.

## 3. Detailed Step-by-Step Solution

### Step 1: Find the inverse matrix $S^{-1}$
Since $S = \begin{pmatrix}2&0\\0&\frac{1}{2}\end{pmatrix}$ is a diagonal matrix with non-zero diagonal entries $s_x = 2$ and $s_y = \frac{1}{2}$, its inverse is the diagonal matrix whose diagonal entries are the reciprocals $\frac{1}{2}$ and $\frac{1}{1/2} = 2$:
$$S^{-1} = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&2\end{pmatrix}.$$
(We obtain the same result from the $2 \times 2$ formula since $\det(S) = 2 \cdot \frac{1}{2} - 0 = 1$, so $S^{-1} = \frac{1}{1}\begin{pmatrix}\frac{1}{2}&0\\0&2\end{pmatrix}$.)

### Step 2: Geometric explanation of $S$ and $S^{-1}$
- **Action of $S$:** For any point $(x,y)$ in the plane, $S\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}2x\\\frac{1}{2}y\end{pmatrix}$. Thus, $S$ **stretches** the plane horizontally (along the $x$-axis) by a factor of $2$ and **compresses** the plane vertically (along the $y$-axis) by a factor of $\frac{1}{2}$ (note that areas are preserved since $\det(S) = 1$).
- **Action of $S^{-1}$:** For any point $(u,w)$, $S^{-1}\begin{pmatrix}u\\w\end{pmatrix} = \begin{pmatrix}\frac{1}{2}u\\2w\end{pmatrix}$. Geometrically, $S^{-1}$ **compresses** the plane horizontally by a factor of $\frac{1}{2}$ (undoing the horizontal doubling) and **stretches** the plane vertically by a factor of $2$ (undoing the vertical halving), restoring every point in the plane to its original position.

### Step 3: Check the action of $S$ and $S^{-1}$ on a simple vector
Choose the vector $v = \begin{pmatrix}3\\4\end{pmatrix}$.
1. First, apply $S$ to $v$:
   $$w = Sv = \begin{pmatrix}2&0\\0&\frac{1}{2}\end{pmatrix}\begin{pmatrix}3\\4\end{pmatrix} = \begin{pmatrix}2(3) + 0(4)\\0(3) + \frac{1}{2}(4)\end{pmatrix} = \begin{pmatrix}6\\2\end{pmatrix}.$$
   The $x$-component doubled from $3$ to $6$, and the $y$-component was halved from $4$ to $2$.
2. Next, apply $S^{-1}$ to the transformed vector $w = \begin{pmatrix}6\\2\end{pmatrix}$:
   $$S^{-1}w = S^{-1}(Sv) = \begin{pmatrix}\frac{1}{2}&0\\[4pt]0&2\end{pmatrix}\begin{pmatrix}6\\2\end{pmatrix} = \begin{pmatrix}\frac{1}{2}(6) + 0(2)\\[4pt]0(6) + 2(2)\end{pmatrix} = \begin{pmatrix}3\\4\end{pmatrix} = v.$$
   The original vector $v = \begin{pmatrix}3\\4\end{pmatrix}$ is completely recovered.

## 4. Verification and Consistency Checks
We verify that $SS^{-1} = I_2$ and $S^{-1}S = I_2$ by direct matrix multiplication:
$$SS^{-1} = \begin{pmatrix}2&0\\0&\frac{1}{2}\end{pmatrix}\begin{pmatrix}\frac{1}{2}&0\\[4pt]0&2\end{pmatrix} = \begin{pmatrix}2\left(\frac{1}{2}\right)&0\\[4pt]0&\frac{1}{2}(2)\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
Thus, $S^{-1}$ is verified both algebraically and geometrically.
