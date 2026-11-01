# Exercise 9: Area and the Determinant

## 1. Problem Statement

The vectors
$$u=\begin{pmatrix}3\\1\end{pmatrix},\qquad v=\begin{pmatrix}1\\4\end{pmatrix}$$
span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

## 2. Theoretical Background and Concepts

- **Area of a Parallelogram Spanned by Two Vectors in $\mathbb{R}^2$:** Given two vectors $u = \begin{pmatrix}u_1\\u_2\end{pmatrix}$ and $v = \begin{pmatrix}v_1\\v_2\end{pmatrix}$ in the plane, the area of the parallelogram spanned by $u$ and $v$ is equal to the **absolute value** of the determinant of the $2 \times 2$ matrix formed with $u$ and $v$ as its columns (or rows):
  $$\text{Area} = \left|\det\begin{pmatrix} u & v \end{pmatrix}\right| = \left|\det\begin{pmatrix}u_1&v_1\\u_2&v_2\end{pmatrix}\right| = |u_1 v_2 - u_2 v_1|.$$
- **Signed Area and Orientation:** The determinant $\det\begin{pmatrix} u & v \end{pmatrix}$ itself is called the **signed (or oriented) area** of the parallelogram:
  - Its **magnitude** $|\det\begin{pmatrix} u & v \end{pmatrix}| = \|u\|\|v\|\sin\theta$ is the geometric area.
  - Its **sign** indicates the **orientation** of the ordered pair $(u, v)$: positive ($+$) if turning from $u$ to $v$ through the smaller angle ($<\pi$) is **counterclockwise**, and negative ($-$) if turning from $u$ to $v$ is **clockwise**.

## 3. Detailed Step-by-Step Solution

### 1. Computing the Determinant and Area for the Ordered Pair $(u, v)$
Form the $2 \times 2$ matrix with $u$ as the first column and $v$ as the second column:
$$M_1 = \begin{pmatrix} u & v \end{pmatrix} = \begin{pmatrix}3&1\\1&4\end{pmatrix}.$$
Compute its determinant:
$$\det M_1 = \det\begin{pmatrix}3&1\\1&4\end{pmatrix} = 3 \cdot 4 - 1 \cdot 1 = 12 - 1 = 11.$$
Taking the absolute value gives the area of the parallelogram:
$$\text{Area} = |\det M_1| = |11| = 11.$$

### 2. Reversing the Order of the Vectors to $(v, u)$
Now form the $2 \times 2$ matrix with $v$ as the first column and $u$ as the second column:
$$M_2 = \begin{pmatrix} v & u \end{pmatrix} = \begin{pmatrix}1&3\\4&1\end{pmatrix}.$$
Compute its determinant:
$$\det M_2 = \det\begin{pmatrix}1&3\\4&1\end{pmatrix} = 1 \cdot 1 - 3 \cdot 4 = 1 - 12 = -11.$$
Compute the area:
$$\text{Area} = |\det M_2| = |-11| = 11.$$

### 3. Explanation of What Changes and What Does Not Change
- **What changes in the determinant:** Reversing the order of the vectors swaps the two columns of the matrix, which **reverses the sign of the determinant** from $+11$ to $-11$. Geometrically, this reflects a change in **orientation**: rotating from $u = (3,1)^T$ to $v = (1,4)^T$ is counterclockwise (positive orientation), whereas rotating from $v = (1,4)^T$ to $u = (3,1)^T$ is clockwise (negative orientation).
- **What does not change in the area:** The **geometric area** of the parallelogram (and the absolute value $|\det| = 11$) **does not change**, because the two vectors $u$ and $v$ span the exact same geometric parallelogram in $\mathbb{R}^2$ regardless of which vector we list first, and geometric area is always a non-negative quantity.

## 4. Verification and Consistency Checks

Let us verify the area $= 11$ using the classical Euclidean formula $\text{Area} = \|u\|\|v\|\sin\theta$:
- $\|u\| = \sqrt{3^2 + 1^2} = \sqrt{10}$ and $\|v\| = \sqrt{1^2 + 4^2} = \sqrt{17}$.
- $u \cdot v = 3(1) + 1(4) = 7$, so $\cos\theta = \frac{u \cdot v}{\|u\|\|v\|} = \frac{7}{\sqrt{170}}$.
- Since $\sin\theta = \sqrt{1 - \cos^2\theta} = \sqrt{1 - \frac{49}{170}} = \sqrt{\frac{121}{170}} = \frac{11}{\sqrt{170}}$, we obtain:
  $$\text{Area} = \|u\|\|v\|\sin\theta = \sqrt{10}\sqrt{17} \cdot \frac{11}{\sqrt{170}} = \sqrt{170} \cdot \frac{11}{\sqrt{170}} = 11. \quad \checkmark$$
This confirms the determinant formula gives the exact geometric area.
