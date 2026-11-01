# Exercise 6: Angle Between Planes

## 1. Problem Statement

Given
$$\Pi_1:x+y+z=1,\qquad \Pi_2:x-y=2.$$
First use the normal vectors to decide whether the planes are parallel. If not, compute the angle between them and explain why the normal vectors alone are enough for this calculation.

## 2. Theoretical Background and Concepts

1. **Normal Vectors and Parallelism of Planes:**
   Two planes $\Pi_1: A_1 x + B_1 y + C_1 z = D_1$ and $\Pi_2: A_2 x + B_2 y + C_2 z = D_2$ have normal vectors $n_1 = (A_1, B_1, C_1)$ and $n_2 = (A_2, B_2, C_2)$.
   The planes $\Pi_1$ and $\Pi_2$ are **parallel** (or identical) if and only if their normal vectors are collinear:
   $$\Pi_1 \parallel \Pi_2 \iff n_1 = \lambda n_2 \text{ for some } \lambda \neq 0 \iff n_1 \times n_2 = \mathbf{0}$$

2. **Dihedral Angle Between Two Planes:**
   By convention, the angle $\theta$ between two intersecting planes is chosen to be the acute (or right) dihedral angle $\theta \in \left[0, \frac{\pi}{2}\right]$, which is given by the angle between the lines spanned by their normal vectors $n_1$ and $n_2$:
   $$\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\|\,\|n_2\|}$$
   (Notice that even if we consider the directed angle between $n_1$ and $n_2$ without the absolute value, here $n_1 \cdot n_2 = 0$, so both definitions yield $\theta = \frac{\pi}{2}$.)

## 3. Detailed Step-by-Step Solution

Given planes:
$$\Pi_1: x + y + z = 1, \qquad \Pi_2: x - y + 0z = 2$$

### Step 1: Identify the normal vectors and decide whether the planes are parallel
Reading the coefficients of $x, y, z$ from each equation:
$$n_1 = (1, 1, 1), \qquad n_2 = (1, -1, 0)$$
Comparing $n_1$ and $n_2$, we see that $n_1$ is not a scalar multiple of $n_2$ (for example, the $z$-component of $n_1$ is $1 \neq 0$ while the $z$-component of $n_2$ is $0$; also in the first two components $\frac{1}{1} \neq \frac{1}{-1}$).
Therefore, the planes $\Pi_1$ and $\Pi_2$ are **not parallel**; they intersect along a line.

### Step 2: Compute the angle between the planes
Compute the dot product of $n_1$ and $n_2$:
$$n_1 \cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0$$
For completeness, their norms are $\|n_1\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$ and $\|n_2\| = \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{2}$, so:
$$\cos\theta = \frac{|n_1 \cdot n_2|}{\|n_1\|\,\|n_2\|} = \frac{0}{\sqrt{3}\sqrt{2}} = 0$$
Therefore, the angle between $\Pi_1$ and $\Pi_2$ is:
$$\theta = \arccos(0) = \frac{\pi}{2}\text{ radians} = 90^\circ$$
That is, the two planes are **mutually perpendicular** ($\Pi_1 \perp \Pi_2$).

### Step 3: Explain why the normal vectors alone are enough for this calculation
1. **Translation Invariance of Angles:** The constants $D_1 = 1$ and $D_2 = 2$ only shift the planes parallel to themselves without rotating them, so the angle between $\Pi_1$ and $\Pi_2$ depends solely on their orientations, which are completely determined by $n_1$ and $n_2$.
2. **Plane Cross-Section Geometry:** Consider a plane $\Sigma$ perpendicular to the line of intersection $L = \Pi_1 \cap \Pi_2$. In this $2$-dimensional cross-sectional plane $\Sigma$, the traces of $\Pi_1$ and $\Pi_2$ are two lines meeting at the dihedral angle $\theta$, and the normal vectors $n_1, n_2$ also lie in $\Sigma$ and are obtained by rotating those two trace lines by $90^\circ$. Rotating two lines in a plane by $90^\circ$ preserves the angle between them (up to supplement $\pi - \theta$). Thus, the angle between the planes equals the angle between their normal vectors.

## 4. Verification and Consistency Checks

**Check via Cross Product and Orthogonal Vectors in Each Plane:**
- The line of intersection $L = \Pi_1 \cap \Pi_2$ has direction vector $v = n_1 \times n_2 = (1, 1, 1) \times (1, -1, 0) = (1, 1, -2)$.
- A vector in $\Pi_1$ perpendicular to $L$ is $u_1 = v \times n_1 = (1, 1, -2) \times (1, 1, 1) = (3, -3, 0)$.
- A vector in $\Pi_2$ perpendicular to $L$ is $u_2 = v \times n_2 = (1, 1, -2) \times (1, -1, 0) = (-2, -2, -2)$.
- By definition of the dihedral angle, $\theta$ is the angle between $u_1$ and $u_2$. Their dot product is:
  $$u_1 \cdot u_2 = (3)(-2) + (-3)(-2) + (0)(-2) = -6 + 6 + 0 = 0 \quad \checkmark$$
  Since $u_1 \cdot u_2 = 0$, the dihedral angle between $\Pi_1$ and $\Pi_2$ is indeed $90^\circ$.
