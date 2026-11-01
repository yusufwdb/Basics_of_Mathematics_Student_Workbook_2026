# Exercise 10: Projection of a Point onto a Plane

## 1. Problem Statement

Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane.

## 2. Theoretical Background and Concepts

1. **Orthogonal Projection of a Point onto a Plane:**
   Given a point $P \in \mathbb{R}^3$ and a plane $\Pi: n \cdot x = d$ with normal vector $n$, the **orthogonal projection** $P'$ of $P$ onto $\Pi$ is the foot of the perpendicular dropped from $P$ to $\Pi$.
   - We construct the normal line $L_\perp$ passing through $P$ with direction vector $n$:
     $$L_\perp: x(t) = P + t n, \qquad t \in \mathbb{R}$$
   - The projection $P'$ is the unique intersection point of $L_\perp$ with $\Pi$, found by solving $n \cdot (P + t n) = d$ for $t = t^*$:
     $$t^* = \frac{d - n \cdot P}{\|n\|^2}, \qquad P' = P + t^* n$$

2. **Reflection of a Point Across a Plane:**
   The **reflection** (mirror image) $P''$ of $P$ across $\Pi$ lies on the same normal line $L_\perp$ on the opposite side of $\Pi$ at the exact same distance from $\Pi$ as $P$. Since moving from $P$ to $P'$ uses the displacement $\overrightarrow{PP'} = P' - P = t^* n$, moving an equal displacement beyond $P'$ gives:
   $$P'' = P' + \overrightarrow{PP'} = 2P' - P = P + 2t^* n$$
   Consequently, $P' = \frac{P + P''}{2}$ is the midpoint of the segment $PP''$.

## 3. Detailed Step-by-Step Solution

Given:
- Point $P = (2, 1, 3)$
- Plane $\Pi: x + y + z = 3$, with normal vector $n = (1, 1, 1)$

### Step 1: Write the parametric equation of the line through $P$ perpendicular to $\Pi$
Using $P = (2, 1, 3)$ and direction vector $n = (1, 1, 1)$, the normal line $L_\perp$ is:
$$(x, y, z) = (2, 1, 3) + t(1, 1, 1) = (2 + t,\, 1 + t,\, 3 + t), \qquad t \in \mathbb{R}$$

### Step 2: Find the orthogonal projection $P'$ by intersecting $L_\perp$ with $\Pi$
Substitute $x = 2 + t$, $y = 1 + t$, and $z = 3 + t$ into the plane equation $x + y + z = 3$:
$$(2 + t) + (1 + t) + (3 + t) = 3$$
$$6 + 3t = 3 \implies 3t = -3 \implies t = -1$$
Substitute $t = -1$ into the equation of $L_\perp$ to obtain the orthogonal projection $P'$:
$$P' = (2 + (-1),\, 1 + (-1),\, 3 + (-1)) = (1, 0, 2)$$

### Step 3: Find the reflection $P''$ of $P$ across the plane $\Pi$
The displacement vector from $P$ to the plane is $\overrightarrow{PP'} = P' - P = (1 - 2,\, 0 - 1,\, 2 - 3) = (-1, -1, -1)$ (which corresponds to $t = -1$).
To reach the reflected point $P''$, we add $\overrightarrow{PP'}$ once more to $P'$ (or set $t = 2(-1) = -2$ in $L_\perp$):
$$P'' = P' + \overrightarrow{PP'} = (1, 0, 2) + (-1, -1, -1) = (0, -1, 1)$$
(Equivalently, $P'' = 2P' - P = 2(1, 0, 2) - (2, 1, 3) = (2, 0, 4) - (2, 1, 3) = (0, -1, 1)$.)

## 4. Verification and Consistency Checks

1. **Check that the midpoint $M$ of the segment $PP''$ lies on the plane $\Pi$:**
   Compute the midpoint $M$ of $P = (2, 1, 3)$ and $P'' = (0, -1, 1)$:
   $$M = \left(\frac{2 + 0}{2},\, \frac{1 + (-1)}{2},\, \frac{3 + 1}{2}\right) = (1, 0, 2) = P'$$
   Substitute $M = (1, 0, 2)$ into the plane equation $x + y + z = 3$:
   $$1 + 0 + 2 = 3 \quad \checkmark$$
   Thus, the midpoint $M$ coincides with the orthogonal projection $P'$ and lies on the plane $\Pi$.

2. **Check that the segment $PP''$ is perpendicular to $\Pi$:**
   $$\overrightarrow{PP''} = P'' - P = (0 - 2,\, -1 - 1,\, 1 - 3) = (-2, -2, -2) = -2(1, 1, 1) = -2n$$
   Since $\overrightarrow{PP''}$ is a scalar multiple of the normal vector $n = (1, 1, 1)$, the segment $PP''$ is perpendicular to $\Pi$, and $P, P''$ are at equal distance $\|P - P'\| = \|P'' - P'\| = \sqrt{3}$ from the plane.
