# Exercise 9: Composing Transformations

## 1. Problem Statement

Let
$$S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$
The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For
$$x=\begin{pmatrix}1\\2\end{pmatrix}$$
compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

## 2. Theoretical Background and Concepts

- **Linear Transformations and Matrices:** Every $2 \times 2$ matrix $M$ defines a linear transformation $T_M: \mathbb{R}^2 \to \mathbb{R}^2$ via $T_M(x) = Mx$.
  - $S = \begin{pmatrix}2&0\\0&1\end{pmatrix}$ maps $\begin{pmatrix}x_1\\x_2\end{pmatrix} \mapsto \begin{pmatrix}2x_1\\x_2\end{pmatrix}$, which stretches the plane horizontally (along the $x_1$-axis) by a factor of $2$ while leaving the vertical coordinate ($x_2$-axis) unchanged.
  - $R = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ maps $\begin{pmatrix}x_1\\x_2\end{pmatrix} \mapsto \begin{pmatrix}-x_2\\x_1\end{pmatrix}$, which rotates every vector in the plane by $90^\circ$ counterclockwise about the origin.
- **Composition of Transformations:** Applying transformation $B$ first and then transformation $A$ to a vector $x$ yields $A(Bx) = (AB)x$. The matrix acting **closest to the vector $x$** (on the right) is the transformation applied **first**.

## 3. Detailed Step-by-Step Solution

### 1. Computing $RSx$ (Scale First, Rotate Second)
First apply the scaling $S$ to $x$:
$$Sx = \begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix} = \begin{pmatrix}2\cdot 1 + 0\cdot 2\\0\cdot 1 + 1\cdot 2\end{pmatrix} = \begin{pmatrix}2\\2\end{pmatrix}.$$
Next apply the $90^\circ$ counterclockwise rotation $R$ to $Sx$:
$$RSx = R(Sx) = \begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}2\\2\end{pmatrix} = \begin{pmatrix}0\cdot 2 + (-1)\cdot 2\\1\cdot 2 + 0\cdot 2\end{pmatrix} = \begin{pmatrix}-2\\2\end{pmatrix}.$$

### 2. Computing $SRx$ (Rotate First, Scale Second)
First apply the $90^\circ$ counterclockwise rotation $R$ to $x$:
$$Rx = \begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix} = \begin{pmatrix}0\cdot 1 + (-1)\cdot 2\\1\cdot 1 + 0\cdot 2\end{pmatrix} = \begin{pmatrix}-2\\1\end{pmatrix}.$$
Next apply the horizontal scaling $S$ to $Rx$:
$$SRx = S(Rx) = \begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}-2\\1\end{pmatrix} = \begin{pmatrix}2\cdot(-2) + 0\cdot 1\\0\cdot(-2) + 1\cdot 1\end{pmatrix} = \begin{pmatrix}-4\\1\end{pmatrix}.$$

### 3. Comparison and Geometric Explanation
Comparing the results:
$$RSx = \begin{pmatrix}-2\\2\end{pmatrix} \neq \begin{pmatrix}-4\\1\end{pmatrix} = SRx.$$
Even the lengths of the resulting vectors are different: $\|RSx\| = \sqrt{(-2)^2+2^2} = \sqrt{8}$, whereas $\|SRx\| = \sqrt{(-4)^2+1^2} = \sqrt{17}$.

**Geometric Explanation:**
The scaling $S$ only stretches the **horizontal ($x_1$) component** of whatever vector it acts upon, by a factor of $2$:
- In **$RSx$**, we scale **before** rotating. The original horizontal component of $x=\begin{pmatrix}1\\2\end{pmatrix}$ is $x_1 = 1$, which gets doubled to $2$, giving $\begin{pmatrix}2\\2\end{pmatrix}$. Then rotating by $90^\circ$ moves that stretched horizontal component into the vertical position, while the original vertical component ($x_2 = 2$) moves into the horizontal position (with a minus sign), yielding $\begin{pmatrix}-2\\2\end{pmatrix}$. Effectively, the original $x_1$-coordinate was doubled.
- In **$SRx$**, we rotate **before** scaling. Rotating $x=\begin{pmatrix}1\\2\end{pmatrix}$ by $90^\circ$ puts the original vertical component ($2$) onto the horizontal axis (as $-2$), giving $\begin{pmatrix}-2\\1\end{pmatrix}$. Then applying the horizontal stretch $S$ doubles this new horizontal coordinate from $-2$ to $-4$, yielding $\begin{pmatrix}-4\\1\end{pmatrix}$. Effectively, the original $x_2$-coordinate was doubled!
Because a $90^\circ$ rotation swaps the horizontal and vertical axes, stretching horizontally before rotating stretches the original $x_1$-direction, whereas stretching horizontally after rotating stretches what used to be the $x_2$-direction.

## 4. Verification and Consistency Checks

Let us compute the composite matrices $RS$ and $SR$ first, and then multiply by $x = \begin{pmatrix}1\\2\end{pmatrix}$:
- $$RS = \begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix} = \begin{pmatrix}0&-1\\2&0\end{pmatrix} \implies (RS)x = \begin{pmatrix}0&-1\\2&0\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix} = \begin{pmatrix}-2\\2\end{pmatrix}. \quad \checkmark$$
- $$SR = \begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix} = \begin{pmatrix}0&-2\\1&0\end{pmatrix} \implies (SR)x = \begin{pmatrix}0&-2\\1&0\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix} = \begin{pmatrix}-4\\1\end{pmatrix}. \quad \checkmark$$
Both by associativity $(RS)x = R(Sx)$ and $(SR)x = S(Rx)$, the results match.
