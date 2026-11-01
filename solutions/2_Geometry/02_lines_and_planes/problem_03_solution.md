# Exercise 3: Plane Through a Point with a Given Normal Vector

## 1. Problem Statement

Find the equation of the plane through $P=(1,-2,3)$ and perpendicular to $n=(2,1,-1)$. Check the result by substituting the point $P$ and explain the role of the normal vector.

## 2. Theoretical Background and Concepts

1. **Point-Normal Form of a Plane in $\mathbb{R}^3$:**
   Let $P = (x_0, y_0, z_0)$ be a given point on a plane $\Pi$, and let $n = (A, B, C) \neq (0, 0, 0)$ be a **normal vector** (a vector perpendicular to the plane).
   An arbitrary point $X = (x, y, z) \in \mathbb{R}^3$ lies in $\Pi$ if and only if the displacement vector $\overrightarrow{PX} = (x - x_0,\, y - y_0,\, z - z_0)$ lies in the plane, which is equivalent to $\overrightarrow{PX}$ being orthogonal to the normal vector $n$:
   $$n \cdot \overrightarrow{PX} = 0 \iff A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$$

2. **General (Cartesian) Form of a Plane:**
   Expanding the point-normal equation gives:
   $$Ax + By + Cz = D \quad \text{or} \quad Ax + By + Cz - D = 0$$
   where $D = n \cdot P = Ax_0 + By_0 + Cz_0$, and the coefficients $(A, B, C)$ of $(x, y, z)$ are precisely the components of the normal vector $n$.

## 3. Detailed Step-by-Step Solution

Given:
$$P = (1, -2, 3), \qquad n = (2, 1, -1)$$

### Step 1: Write the point-normal form of the plane
For any point $X = (x, y, z)$ on the plane, the vector $\overrightarrow{PX} = (x - 1,\, y - (-2),\, z - 3) = (x - 1,\, y + 2,\, z - 3)$ must be perpendicular to $n = (2, 1, -1)$:
$$n \cdot \overrightarrow{PX} = 0 \implies 2(x - 1) + 1(y + 2) - 1(z - 3) = 0$$

### Step 2: Simplify to general form
Expand and combine the constant terms:
$$2x - 2 + y + 2 - z + 3 = 0 \implies 2x + y - z + 3 = 0$$
or equivalently:
$$2x + y - z = -3$$

### Step 3: Check the result by substituting $P = (1, -2, 3)$
Substitute $x = 1$, $y = -2$, $z = 3$ into the left-hand side of $2x + y - z = -3$:
$$2(1) + (-2) - 3 = 2 - 2 - 3 = -3 \quad \checkmark$$
Since $-3 = -3$, the point $P$ satisfies the equation of the plane.

### Step 4: Explain the role of the normal vector
In three-dimensional space $\mathbb{R}^3$, a plane is a $2$-dimensional flat surface (codimension $1$). Rather than specifying two independent direction vectors inside the plane, it is much simpler to specify the **single direction perpendicular to the plane**, called the **normal vector** $n$.
- Geometrically, the normal vector $n = (2, 1, -1)$ fixes the **orientation (tilt)** of the plane in space: the plane consists of all directions orthogonal to $n$ (via the dot product condition $n \cdot \overrightarrow{PX} = 0$).
- Algebraically, the components of $n = (2, 1, -1)$ become the exact coefficients of $x, y, z$ in the Cartesian equation $2x + y - z = -3$, while the point $P$ fixes the parallel shift (the constant term $D = n \cdot P = -3$) among all parallel planes sharing that normal.

## 4. Verification and Consistency Checks

**Orthogonality Check with Another Point on the Plane:**
Let us pick another point $Q$ that satisfies $2x + y - z = -3$, for example by setting $x = 0, y = 0 \implies -z = -3 \implies z = 3$, so $Q = (0, 0, 3)$.
The displacement vector between $P = (1, -2, 3)$ and $Q = (0, 0, 3)$ is:
$$\overrightarrow{PQ} = Q - P = (0 - 1,\, 0 - (-2),\, 3 - 3) = (-1, 2, 0)$$
Taking the dot product of $\overrightarrow{PQ}$ with the normal vector $n = (2, 1, -1)$:
$$n \cdot \overrightarrow{PQ} = (2)(-1) + (1)(2) + (-1)(0) = -2 + 2 + 0 = 0 \quad \checkmark$$
This confirms that vectors connecting points on the plane $2x + y - z = -3$ are orthogonal to $n = (2, 1, -1)$.
