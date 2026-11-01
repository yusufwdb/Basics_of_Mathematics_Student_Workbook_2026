# Exercise 14: Rotation Matrices

## 1. Problem Statement

The matrix for a rotation through an angle $\theta$ is
$$R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.$$
Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that
$$R(\alpha)R(\beta)=R(\alpha+\beta).$$
Explain the result geometrically.

## 2. Theoretical Background and Concepts

- **2D Rotation Matrix:** In the Euclidean plane $\mathbb{R}^2$, the linear transformation that rotates every vector counterclockwise about the origin by an angle $\theta$ is represented in the standard basis $\{e_1, e_2\}$ by:
  $$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},$$
  since $e_1 = \begin{pmatrix}1\\0\end{pmatrix} \mapsto \begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}$ and $e_2 = \begin{pmatrix}0\\1\end{pmatrix} \mapsto \begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix}$.
- **Trigonometric Angle-Sum Identities:** For any real angles $\alpha, \beta \in \mathbb{R}$:
  $$\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta,$$
  $$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta.$$

## 3. Detailed Step-by-Step Solution

### 1. Computing the Matrix Product $R(\alpha)R(\beta)$
Write out the two rotation matrices and multiply them using the row-by-column rule:
$$R(\alpha)R(\beta) = \begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix} \begin{pmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{pmatrix}$$
$$= \begin{pmatrix} \cos\alpha\cos\beta + (-\sin\alpha)\sin\beta & \cos\alpha(-\sin\beta) + (-\sin\alpha)\cos\beta \\ \sin\alpha\cos\beta + \cos\alpha\sin\beta & \sin\alpha(-\sin\beta) + \cos\alpha\cos\beta \end{pmatrix}$$
$$= \begin{pmatrix} \cos\alpha\cos\beta - \sin\alpha\sin\beta & -(\sin\alpha\cos\beta + \cos\alpha\sin\beta) \\ \sin\alpha\cos\beta + \cos\alpha\sin\beta & \cos\alpha\cos\beta - \sin\alpha\sin\beta \end{pmatrix}.$$

### 2. Applying the Angle-Sum Identities
Substitute $\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ and $\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$ into each of the four entries:
$$R(\alpha)R(\beta) = \begin{pmatrix} \cos(\alpha+\beta) & -\sin(\alpha+\beta) \\ \sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix} = R(\alpha+\beta).$$

### 3. Geometric Explanation
Matrix multiplication corresponds to the **composition of linear transformations**. When we apply $R(\alpha)R(\beta)$ to any vector $v \in \mathbb{R}^2$:
1. First, $R(\beta)v$ rotates the vector $v$ counterclockwise about the origin through an angle $\beta$.
2. Second, $R(\alpha)\big(R(\beta)v\big)$ rotates the resulting vector counterclockwise about the origin through an additional angle $\alpha$.
Geometrically, rotating a plane figure about the origin by angle $\beta$ and then rotating it about the same origin by angle $\alpha$ has the exact same net effect as a single rotation about the origin through the total angle $\alpha + \beta$. Moreover, because real addition is commutative ($\alpha + \beta = \beta + \alpha$), planar rotations about the same center commute: $R(\alpha)R(\beta) = R(\alpha+\beta) = R(\beta+\alpha) = R(\beta)R(\alpha)$.

## 4. Verification and Consistency Checks

1. **Special Case Check ($\alpha = \frac{\pi}{2}, \beta = \frac{\pi}{2}$):**
   For $\alpha = \beta = \frac{\pi}{2}$ ($90^\circ$), $\cos\frac{\pi}{2} = 0$ and $\sin\frac{\pi}{2} = 1$, so $R\left(\frac{\pi}{2}\right) = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$. Multiplying:
   $$R\left(\frac{\pi}{2}\right)R\left(\frac{\pi}{2}\right) = \begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix} = \begin{pmatrix}-1&0\\0&-1\end{pmatrix} = \begin{pmatrix}\cos\pi&-\sin\pi\\\sin\pi&\cos\pi\end{pmatrix} = R(\pi). \quad \checkmark$$
2. **Inverse Rotation Check ($\beta = -\alpha$):**
   Setting $\beta = -\alpha$ gives $R(\alpha)R(-\alpha) = R(\alpha - \alpha) = R(0) = \begin{pmatrix}\cos 0 & -\sin 0\\\sin 0 & \cos 0\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$, confirming that rotating by $-\alpha$ undoes a rotation by $\alpha$, and $R(\alpha)^{-1} = R(-\alpha) = R(\alpha)^T$.
3. **Determinant Check:**
   $$\det R(\alpha+\beta) = \cos^2(\alpha+\beta) + \sin^2(\alpha+\beta) = 1 = 1 \cdot 1 = \det R(\alpha)\det R(\beta). \quad \checkmark$$
