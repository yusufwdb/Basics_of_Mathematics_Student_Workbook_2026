# Exercise 12: A Normal Vector to a Plane

## 1. Problem Statement

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

## 2. Theoretical Background and Concepts

1. **Vectors Spanning a Plane:**
   Three non-collinear points $A, B, C \in \mathbb{R}^3$ determine a unique plane $\Pi$. Any displacement vector between two points in the plane—such as $\overrightarrow{AB} = B - A$ and $\overrightarrow{AC} = C - A$—lies parallel to (in the direction space of) the plane $\Pi$.

2. **Normal Vector to a Plane:**
   A non-zero vector $n$ is a **normal vector** to the plane $\Pi$ if it is orthogonal to every vector lying in $\Pi$. By linearity of the dot product, $n$ is orthogonal to every linear combination $\alpha \overrightarrow{AB} + \beta \overrightarrow{AC}$ if and only if it is orthogonal to both basis vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
   $$n \cdot \overrightarrow{AB} = 0 \quad \text{and} \quad n \cdot \overrightarrow{AC} = 0$$
   The **cross product** $n = \overrightarrow{AB} \times \overrightarrow{AC}$ automatically produces such a vector (and is non-zero whenever $A, B, C$ are not collinear).

## 3. Detailed Step-by-Step Solution

Given points:
$$A = (1, 0, 2), \qquad B = (2, 1, 0), \qquad C = (0, 3, 1)$$

### Step 1: Construct two vectors lying in the plane
Using $A$ as the common initial point, we construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$:
$$\overrightarrow{AB} = B - A = (2 - 1,\, 1 - 0,\, 0 - 2) = (1, 1, -2)$$
$$\overrightarrow{AC} = C - A = (0 - 1,\, 3 - 0,\, 1 - 2) = (-1, 3, -1)$$

### Step 2: Find a vector perpendicular to both using the cross product
Compute $n = \overrightarrow{AB} \times \overrightarrow{AC}$:
$$n = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & -2 \\ -1 & 3 & -1 \end{vmatrix}$$
Expanding by cofactors along the first row:
- First component ($x$): $(1)(-1) - (-2)(3) = -1 + 6 = 5$
- Second component ($y$): $-\big((1)(-1) - (-2)(-1)\big) = -(-1 - 2) = 3$
- Third component ($z$): $(1)(3) - (1)(-1) = 3 + 1 = 4$

Thus, a normal vector to the plane is:
$$n = (5, 3, 4)$$
(Any non-zero scalar multiple $\lambda(5, 3, 4)$ is also a valid normal vector.)

### Step 3: Check perpendicularity using dot products
Compute the dot product of $n = (5, 3, 4)$ with $\overrightarrow{AB} = (1, 1, -2)$:
$$n \cdot \overrightarrow{AB} = (5)(1) + (3)(1) + (4)(-2) = 5 + 3 - 8 = 0 \quad \checkmark$$
Compute the dot product of $n = (5, 3, 4)$ with $\overrightarrow{AC} = (-1, 3, -1)$:
$$n \cdot \overrightarrow{AC} = (5)(-1) + (3)(3) + (4)(-1) = -5 + 9 - 4 = 0 \quad \checkmark$$
Since both dot products equal $0$ and $n \neq \mathbf{0}$, $n = (5, 3, 4)$ is perpendicular to both $\overrightarrow{AB}$ and $\overrightarrow{AC}$, and hence normal to the plane through $A, B, C$.

## 4. Verification and Consistency Checks

**Check with the Third Edge Vector $\overrightarrow{BC}$:**
The third side of the triangle $\triangle ABC$ is the vector:
$$\overrightarrow{BC} = C - B = (0 - 2,\, 3 - 1,\, 1 - 0) = (-2, 2, 1)$$
Since $\overrightarrow{BC}$ also lies in the plane, $n$ must be perpendicular to $\overrightarrow{BC}$ as well:
$$n \cdot \overrightarrow{BC} = (5)(-2) + (3)(2) + (4)(1) = -10 + 6 + 4 = 0 \quad \checkmark$$
Furthermore, if we form the plane equation $5(x - 1) + 3(y - 0) + 4(z - 2) = 0 \iff 5x + 3y + 4z = 13$, substituting $A, B, C$ gives:
- For $A(1,0,2)$: $5(1) + 3(0) + 4(2) = 5 + 8 = 13 \quad \checkmark$
- For $B(2,1,0)$: $5(2) + 3(1) + 4(0) = 10 + 3 = 13 \quad \checkmark$
- For $C(0,3,1)$: $5(0) + 3(3) + 4(1) = 9 + 4 = 13 \quad \checkmark$
All three points satisfy the plane equation defined by $n = (5, 3, 4)$.
