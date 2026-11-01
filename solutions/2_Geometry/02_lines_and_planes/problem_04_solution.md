# Exercise 4: Plane Through Three Points

## 1. Problem Statement

Find the equation of the plane through
$$A=(1,0,0),\quad B=(0,1,0),\quad C=(0,0,1).$$
First construct two vectors lying in the plane, and then use the cross product. Check the resulting equation on all three points.

## 2. Theoretical Background and Concepts

1. **Constructing a Plane from Three Non-Collinear Points:**
   Given three non-collinear points $A, B, C \in \mathbb{R}^3$:
   - First, form two displacement vectors anchored at one of the points (say $A$):
     $$u = \overrightarrow{AB} = B - A, \qquad v = \overrightarrow{AC} = C - A$$
     Both $u$ and $v$ lie in the plane $\Pi$.
   - Second, compute their cross product:
     $$n = u \times v = \overrightarrow{AB} \times \overrightarrow{AC}$$
     Since $u \times v$ is perpendicular to both $u$ and $v$, $n$ is a **normal vector** to the plane $\Pi$.
   - Third, write the plane equation using the normal vector $n$ and the point $A$:
     $$n \cdot ((x, y, z) - A) = 0$$

## 3. Detailed Step-by-Step Solution

Given points:
$$A = (1, 0, 0), \qquad B = (0, 1, 0), \qquad C = (0, 0, 1)$$

### Step 1: Construct two vectors lying in the plane
Using $A = (1, 0, 0)$ as the initial point:
$$\overrightarrow{AB} = B - A = (0 - 1,\, 1 - 0,\, 0 - 0) = (-1, 1, 0)$$
$$\overrightarrow{AC} = C - A = (0 - 1,\, 0 - 0,\, 1 - 0) = (-1, 0, 1)$$

### Step 2: Use the cross product to find a normal vector $n$
Compute $n = \overrightarrow{AB} \times \overrightarrow{AC}$:
$$n = \overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{vmatrix}$$
Evaluate the components:
- First component ($x$): $(1)(1) - (0)(0) = 1$
- Second component ($y$): $-\big((-1)(1) - (0)(-1)\big) = -(-1) = 1$
- Third component ($z$): $(-1)(0) - (1)(-1) = 0 + 1 = 1$

Thus, the normal vector is:
$$n = (1, 1, 1)$$

### Step 3: Write the equation of the plane
Using the normal vector $n = (1, 1, 1)$ and the point $A = (1, 0, 0)$:
$$1(x - 1) + 1(y - 0) + 1(z - 0) = 0$$
Simplifying gives the Cartesian equation of the plane:
$$x + y + z = 1 \quad (\text{or } x + y + z - 1 = 0)$$

### Step 4: Check the resulting equation on all three points
Substitute the coordinates of $A$, $B$, and $C$ into $x + y + z = 1$:
- **Point $A = (1, 0, 0)$:**
  $$1 + 0 + 0 = 1 \quad \checkmark$$
- **Point $B = (0, 1, 0)$:**
  $$0 + 1 + 0 = 1 \quad \checkmark$$
- **Point $C = (0, 0, 1)$:**
  $$0 + 0 + 1 = 1 \quad \checkmark$$

All three points satisfy the equation $x + y + z = 1$.

## 4. Verification and Consistency Checks

1. **Orthogonality Check of $n$ with $\overrightarrow{AB}$ and $\overrightarrow{AC}$:**
   - $n \cdot \overrightarrow{AB} = (1)(-1) + (1)(1) + (1)(0) = -1 + 1 + 0 = 0 \quad \checkmark$
   - $n \cdot \overrightarrow{AC} = (1)(-1) + (1)(0) + (1)(1) = -1 + 0 + 1 = 0 \quad \checkmark$

2. **Intercept Form of a Plane Check:**
   A plane with non-zero $x$-, $y$-, and $z$-axis intercepts $(a, 0, 0)$, $(0, b, 0)$, and $(0, 0, c)$ has the standard intercept equation:
   $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$
   Here $a = 1$, $b = 1$, $c = 1$, which immediately gives $x + y + z = 1$, matching our cross-product derivation.
