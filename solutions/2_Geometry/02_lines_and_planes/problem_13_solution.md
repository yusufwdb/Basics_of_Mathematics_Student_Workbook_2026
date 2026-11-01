# Exercise 13: Closest Point on a Plane

## 1. Problem Statement

Find the point on the plane $x+2y+2z=4$ closest to $P=(3,0,0)$. Give the distance and check that the segment joining the two points is perpendicular to the plane.

## 2. Theoretical Background and Concepts

1. **Closest Point on a Plane as Orthogonal Projection:**
   By the Pythagorean theorem in $\mathbb{R}^3$, for any point $P \in \mathbb{R}^3$ and any plane $\Pi: Ax + By + Cz = D$ with normal vector $n = (A, B, C)$, the point $Q \in \Pi$ that minimizes the Euclidean distance $\|P - X\|$ over all $X \in \Pi$ is the **orthogonal projection** of $P$ onto $\Pi$.
   - The closest point $Q$ lies on the normal line through $P$:
     $$L_\perp: X(t) = P + t n, \qquad t \in \mathbb{R}$$
   - Solving $n \cdot (P + t n) = D$ yields the unique parameter $t = t^* = \frac{D - n \cdot P}{\|n\|^2}$, and hence $Q = P + t^* n$.

2. **Distance to the Plane:**
   The distance from $P$ to $\Pi$ is the Euclidean distance between $P$ and the closest point $Q$:
   $$d(P, \Pi) = \|\overrightarrow{PQ}\| = \|Q - P\| = |t^*|\,\|n\| = \frac{|n \cdot P - D|}{\|n\|}$$

## 3. Detailed Step-by-Step Solution

Given:
- Plane $\Pi: x + 2y + 2z = 4$, with normal vector $n = (1, 2, 2)$
- Point $P = (3, 0, 0)$

### Step 1: Write the equation of the normal line through $P$
The line $L_\perp$ passing through $P = (3, 0, 0)$ in the direction of the normal vector $n = (1, 2, 2)$ is:
$$(x, y, z) = (3, 0, 0) + t(1, 2, 2) = (3 + t,\, 2t,\, 2t), \qquad t \in \mathbb{R}$$

### Step 2: Find the closest point $Q$ by intersecting $L_\perp$ with $\Pi$
Substitute $x = 3 + t$, $y = 2t$, and $z = 2t$ into the plane equation $x + 2y + 2z = 4$:
$$(3 + t) + 2(2t) + 2(2t) = 4$$
$$3 + t + 4t + 4t = 4 \implies 3 + 9t = 4 \implies 9t = 1 \implies t = \frac{1}{9}$$
Substitute $t = \frac{1}{9}$ back into the normal line equation to obtain the closest point $Q$:
$$Q = \left(3 + \frac{1}{9},\, 2\left(\frac{1}{9}\right),\, 2\left(\frac{1}{9}\right)\right) = \left(\frac{28}{9},\, \frac{2}{9},\, \frac{2}{9}\right)$$

### Step 3: Compute the distance from $P$ to the plane
First, find the displacement vector $\overrightarrow{PQ}$ connecting $P$ and $Q$:
$$\overrightarrow{PQ} = Q - P = \left(\frac{28}{9} - 3,\, \frac{2}{9} - 0,\, \frac{2}{9} - 0\right) = \left(\frac{1}{9},\, \frac{2}{9},\, \frac{2}{9}\right)$$
Compute its length:
$$d(P, \Pi) = \left\|\overrightarrow{PQ}\right\| = \sqrt{\left(\frac{1}{9}\right)^2 + \left(\frac{2}{9}\right)^2 + \left(\frac{2}{9}\right)^2} = \frac{1}{9}\sqrt{1 + 4 + 4} = \frac{\sqrt{9}}{9} = \frac{3}{9} = \frac{1}{3}$$

### Step 4: Check that the segment $PQ$ is perpendicular to the plane
The segment $PQ$ is perpendicular to the plane $\Pi$ if and only if the vector $\overrightarrow{PQ}$ is parallel to the normal vector $n = (1, 2, 2)$ (or orthogonal to any two independent vectors in $\Pi$).
- **Parallelism with $n$:**
  $$\overrightarrow{PQ} = \left(\frac{1}{9},\, \frac{2}{9},\, \frac{2}{9}\right) = \frac{1}{9}(1, 2, 2) = \frac{1}{9}n$$
  Since $\overrightarrow{PQ}$ is a scalar multiple of the normal vector $n$, $\overrightarrow{PQ} \perp \Pi$.
- **Direct dot-product check with two independent vectors in $\Pi$:**
  Two independent direction vectors in the plane $x + 2y + 2z = 4$ are $u_1 = (2, -1, 0)$ and $u_2 = (2, 0, -1)$. Taking their dot products with $\overrightarrow{PQ}$:
  $$\overrightarrow{PQ} \cdot u_1 = \frac{1}{9}(2) + \frac{2}{9}(-1) + \frac{2}{9}(0) = \frac{2 - 2}{9} = 0 \quad \checkmark$$
  $$\overrightarrow{PQ} \cdot u_2 = \frac{1}{9}(2) + \frac{2}{9}(0) + \frac{2}{9}(-1) = \frac{2 - 2}{9} = 0 \quad \checkmark$$
  Thus, $\overrightarrow{PQ}$ is orthogonal to the plane $\Pi$.

## 4. Verification and Consistency Checks

1. **Check that $Q = \left(\frac{28}{9}, \frac{2}{9}, \frac{2}{9}\right)$ lies on the plane $x + 2y + 2z = 4$:**
   $$\frac{28}{9} + 2\left(\frac{2}{9}\right) + 2\left(\frac{2}{9}\right) = \frac{28 + 4 + 4}{9} = \frac{36}{9} = 4 \quad \checkmark$$

2. **Check the distance using the point-to-plane distance formula:**
   For $P = (3, 0, 0)$ and $\Pi: x + 2y + 2z - 4 = 0$:
   $$d(P, \Pi) = \frac{|1(3) + 2(0) + 2(0) - 4|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|3 - 4|}{\sqrt{1 + 4 + 4}} = \frac{|-1|}{3} = \frac{1}{3} \quad \checkmark$$
   Both methods yield the exact same distance $\frac{1}{3}$.
