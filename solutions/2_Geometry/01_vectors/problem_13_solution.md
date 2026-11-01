# Exercise 13: Do Four Points Lie in One Plane?

## 1. Problem Statement

Given
$$A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

## 2. Theoretical Background and Concepts

1. **Plane Determined by Three Non-Collinear Points:**
   Three points $A, B, C \in \mathbb{R}^3$ that are not collinear define a unique plane $\Pi$ passing through $A$ with direction space spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$. The cross product $n = \overrightarrow{AB} \times \overrightarrow{AC} \neq \mathbf{0}$ is a normal vector to $\Pi$.

2. **Coplanarity Criterion via Cross and Dot Products (Scalar Triple Product):**
   A fourth point $D$ lies in the plane $\Pi$ if and only if the displacement vector $\overrightarrow{AD} = D - A$ lies in $\Pi$, which occurs if and only if $\overrightarrow{AD}$ is perpendicular to the normal vector $n$:
   $$D \in \Pi \iff \overrightarrow{AD} \cdot n = \overrightarrow{AD} \cdot (\overrightarrow{AB} \times \overrightarrow{AC}) = 0$$
   Geometrically, $|\overrightarrow{AD} \cdot (\overrightarrow{AB} \times \overrightarrow{AC})|$ is the volume of the parallelepiped spanned by $\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD}$; this volume is zero if and only if the three vectors are coplanar.

## 3. Detailed Step-by-Step Solution

Given points:
$$A = (0, 0, 0), \qquad B = (1, 2, 0), \qquad C = (0, 1, 1), \qquad D = (2, 5, 1)$$

### Part 1: Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$
Since $A = (0, 0, 0)$ is the origin:
$$\overrightarrow{AB} = B - A = (1 - 0,\, 2 - 0,\, 0 - 0) = (1, 2, 0)$$
$$\overrightarrow{AC} = C - A = (0 - 0,\, 1 - 0,\, 1 - 0) = (0, 1, 1)$$

### Part 2: Find $n = \overrightarrow{AB} \times \overrightarrow{AC}$
Compute the cross product:
$$n = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 1 \end{vmatrix} = \big((2)(1) - (0)(1),\, (0)(0) - (1)(1),\, (1)(1) - (2)(0)\big) = (2, -1, 1)$$
Since $n = (2, -1, 1) \neq \mathbf{0}$, the points $A, B, C$ are non-collinear and uniquely determine a plane with normal vector $n = (2, -1, 1)$.

### Part 3: Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD} \cdot n = 0$
First, construct $\overrightarrow{AD}$:
$$\overrightarrow{AD} = D - A = (2 - 0,\, 5 - 0,\, 1 - 0) = (2, 5, 1)$$
Now compute the dot product $\overrightarrow{AD} \cdot n$:
$$\overrightarrow{AD} \cdot n = (2, 5, 1) \cdot (2, -1, 1) = (2)(2) + (5)(-1) + (1)(1) = 4 - 5 + 1 = 0$$
Thus, $\overrightarrow{AD} \cdot n = 0$ holds.

### Part 4: Decision and justification of the criterion
- **Decision:** **Yes**, the point $D = (2, 5, 1)$ lies in the plane $\Pi$ determined by $A, B, C$ (the four points $A, B, C, D$ are coplanar).
- **Justification of the criterion:** The plane $\Pi$ passing through $A$ with normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$ consists of precisely those points $X \in \mathbb{R}^3$ for which the displacement vector $\overrightarrow{AX}$ is orthogonal to $n$ (because $n \perp \Pi$ and $\dim \Pi = 2 = 3 - 1$, so the orthogonal complement of $n$ is exactly the direction space $\operatorname{span}\{\overrightarrow{AB}, \overrightarrow{AC}\}$). Since $\overrightarrow{AD} \cdot n = 0$, the vector $\overrightarrow{AD}$ has zero component in the normal direction perpendicular to $\Pi$, meaning $D$ lies entirely within the plane $\Pi$.

## 4. Verification and Consistency Checks

**Explicit Linear Combination Check ($\overrightarrow{AD} = \alpha \overrightarrow{AB} + \beta \overrightarrow{AC}$):**
If $D$ lies in the plane of $A, B, C$, then $\overrightarrow{AD} = (2, 5, 1)$ must be a linear combination of $\overrightarrow{AB} = (1, 2, 0)$ and $\overrightarrow{AC} = (0, 1, 1)$:
$$(2, 5, 1) = \alpha(1, 2, 0) + \beta(0, 1, 1) = (\alpha,\, 2\alpha + \beta,\, \beta)$$
From the first and third coordinates, we immediately read off $\alpha = 2$ and $\beta = 1$. Checking the middle coordinate:
$$2\alpha + \beta = 2(2) + 1 = 5 \quad \checkmark$$
Thus $\overrightarrow{AD} = 2\overrightarrow{AB} + 1\overrightarrow{AC}$, which directly proves that $\overrightarrow{AD} \in \operatorname{span}\{\overrightarrow{AB}, \overrightarrow{AC}\}$ and confirms that $A, B, C, D$ lie in the same plane $2x - y + z = 0$.
