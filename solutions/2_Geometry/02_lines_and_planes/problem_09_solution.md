# Exercise 9: Distances

## 1. Problem Statement

Compute:
1. the distance from $P=(2,3)$ to the line $3x+4y-10=0$,
2. the distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$.

Compare the two formulas and explain their common connection with the normal direction.

## 2. Theoretical Background and Concepts

1. **Distance from a Point to a Line in $\mathbb{R}^2$:**
   The distance from a point $P = (x_0, y_0) \in \mathbb{R}^2$ to a line $L: ax + by + c = 0$ with normal vector $n = (a, b) \neq (0, 0)$ is:
   $$d(P, L) = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}} = \frac{|n \cdot P + c|}{\|n\|}$$

2. **Distance from a Point to a Plane in $\mathbb{R}^3$:**
   The distance from a point $Q = (x_0, y_0, z_0) \in \mathbb{R}^3$ to a plane $\Pi: Ax + By + Cz + D = 0$ with normal vector $n = (A, B, C) \neq (0, 0, 0)$ is:
   $$d(Q, \Pi) = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}} = \frac{|n \cdot Q + D|}{\|n\|}$$

3. **Unified Geometric Derivation via Projection onto the Normal:**
   In both $\mathbb{R}^2$ and $\mathbb{R}^3$, a hyperplane $H = \{X : n \cdot X + c = 0\}$ is defined by a normal vector $n$ and constant $c$. If $X_0 \in H$ is any point on $H$, then $n \cdot X_0 = -c$. The shortest path from an external point $P$ to $H$ is along the direction perpendicular to $H$, i.e., parallel to $n$. Therefore, the distance $d(P, H)$ is simply the magnitude of the scalar projection of the displacement vector $\overrightarrow{X_0 P} = P - X_0$ onto the unit normal vector $\hat{n} = \frac{n}{\|n\|}$:
   $$d(P, H) = \left|\operatorname{comp}_n \overrightarrow{X_0 P}\right| = \frac{|n \cdot (P - X_0)|}{\|n\|} = \frac{|n \cdot P - n \cdot X_0|}{\|n\|} = \frac{|n \cdot P + c|}{\|n\|}$$

## 3. Detailed Step-by-Step Solution

### Part 1: Distance from $P = (2, 3)$ to the line $L: 3x + 4y - 10 = 0$
Here $x_0 = 2, y_0 = 3$, the normal vector to the line is $n_L = (a, b) = (3, 4)$, and $c = -10$.
- Numerator:
  $$|ax_0 + by_0 + c| = |3(2) + 4(3) - 10| = |6 + 12 - 10| = |8| = 8$$
- Denominator (length of the normal vector $n_L$):
  $$\|n_L\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
- Distance:
  $$d(P, L) = \frac{8}{5} = 1.6$$

### Part 2: Distance from $Q = (2, -1, 3)$ to the plane $\Pi: 2x - 2y + z - 4 = 0$
Here $x_0 = 2, y_0 = -1, z_0 = 3$, the normal vector to the plane is $n_\Pi = (A, B, C) = (2, -2, 1)$, and $D = -4$.
- Numerator:
  $$|Ax_0 + By_0 + Cz_0 + D| = |2(2) - 2(-1) + 1(3) - 4| = |4 + 2 + 3 - 4| = |5| = 5$$
- Denominator (length of the normal vector $n_\Pi$):
  $$\|n_\Pi\| = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3$$
- Distance:
  $$d(Q, \Pi) = \frac{5}{3} \approx 1.6667$$

### Part 3: Compare the two formulas and explain their common connection with the normal direction
Both formulas have the exact same vector structure:
$$d = \frac{|n \cdot P + c|}{\|n\|}$$
- **Numerator $|n \cdot P + c|$:** Measures how far $P$ fails to satisfy the equation $n \cdot X + c = 0$, scaled by $\|n\|$. Specifically, if $X_0$ is any point on the line/plane (so $n \cdot X_0 = -c$), then $n \cdot P + c = n \cdot (P - X_0)$ is the dot product of the connecting vector $\overrightarrow{X_0 P}$ with the normal vector $n$.
- **Denominator $\|n\|$:** Normalizes $n$ into a unit normal vector $\hat{n} = \frac{n}{\|n\|}$ so that the formula does not change if we multiply the equation of the line or plane by a non-zero constant $\lambda$.
- **Connection with the normal direction:** The shortest distance from a point to a flat object (line in $\mathbb{R}^2$ or plane in $\mathbb{R}^3$) is measured along the line perpendicular to the object—that is, along the **normal direction** $n$. Projecting any connecting vector $\overrightarrow{X_0 P}$ onto the unit normal $\frac{n}{\|n\|}$ filters out the component parallel to the line/plane and retains only the perpendicular altitude.

## 4. Verification and Consistency Checks

1. **Verification for Part 1 via Closest Point on $L$:**
   The line through $P=(2,3)$ perpendicular to $L$ is $(x, y) = (2 + 3t, 3 + 4t)$. Substituting into $3x + 4y - 10 = 0$:
   $$3(2 + 3t) + 4(3 + 4t) - 10 = 0 \implies 8 + 25t = 0 \implies t = -\frac{8}{25}$$
   The displacement vector from $P$ to the foot of the perpendicular $P'$ is $t n_L = -\frac{8}{25}(3, 4)$, whose length is:
   $$\|t n_L\| = |t|\,\|n_L\| = \frac{8}{25} \cdot 5 = \frac{8}{5} \quad \checkmark$$

2. **Verification for Part 2 via Closest Point on $\Pi$:**
   The line through $Q=(2,-1,3)$ perpendicular to $\Pi$ is $(x, y, z) = (2 + 2s, -1 - 2s, 3 + s)$. Substituting into $2x - 2y + z - 4 = 0$:
   $$2(2 + 2s) - 2(-1 - 2s) + (3 + s) - 4 = 0 \implies 5 + 9s = 0 \implies s = -\frac{5}{9}$$
   The displacement vector from $Q$ to the foot of the perpendicular $Q'$ is $s n_\Pi = -\frac{5}{9}(2, -2, 1)$, whose length is:
   $$\|s n_\Pi\| = |s|\,\|n_\Pi\| = \frac{5}{9} \cdot 3 = \frac{5}{3} \quad \checkmark$$
