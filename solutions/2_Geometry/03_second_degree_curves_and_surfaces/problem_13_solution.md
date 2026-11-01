# Exercise 13: Intersection of a Sphere and a Plane

## 1. Problem Statement
Given the sphere
$$x^2+y^2+z^2=25$$
and the plane $z=3$, find the equation of the intersection curve and its radius. Then describe what happens for $z=c$ depending on $c$.

## 2. Theoretical Background and Concepts
- **Sphere Centered at the Origin:** The equation $x^2 + y^2 + z^2 = R^2$ describes a sphere of radius $R > 0$ centered at $(0,0,0)$. Here $R^2 = 25 \implies R = 5$.
- **Intersection of a Sphere with a Horizontal Plane $z = c$:**
  The set of points belonging to both the sphere and the plane satisfies the system of equations:
  $$\begin{cases} x^2 + y^2 + z^2 = R^2, \\ z = c. \end{cases}$$
  Substituting $z = c$ into the sphere equation yields $x^2 + y^2 = R^2 - c^2$ inside the plane $z = c$. Geometrically, by the Pythagorean theorem in the right triangle formed by the sphere's center $(0,0,0)$, the circle's center $(0,0,c)$, and a point on the intersection circle, the cross-section radius is $r = \sqrt{R^2 - c^2}$ whenever $|c| \le R$.

## 3. Detailed Step-by-Step Solution

### Step 1: Intersection of $x^2 + y^2 + z^2 = 25$ with the plane $z = 3$
Substitute $z = 3$ into the equation of the sphere:
$$x^2 + y^2 + 3^2 = 25$$
$$x^2 + y^2 + 9 = 25$$
$$x^2 + y^2 = 16.$$
Therefore, the **equation of the intersection curve** in 3D space is:
$$\begin{cases} x^2 + y^2 = 16, \\ z = 3. \end{cases}$$
- **Geometric interpretation:** This is a **circle** lying in the horizontal plane $z = 3$, centered at the point $(0, 0, 3)$.
- **Radius of the intersection curve:**
  $$r = \sqrt{16} = 4.$$

---

### Step 2: Behavior of the cross-section $z = c$ depending on $c \in \mathbb{R}$
Substituting $z = c$ into $x^2 + y^2 + z^2 = 25$ gives:
$$x^2 + y^2 = 25 - c^2, \quad z = c.$$
Depending on the value of $c$ relative to the sphere's radius $R = 5$, there are three distinct cases (plus the special subcase $c = 0$):

1. **Case 1: $|c| < 5$ (i.e., $-5 < c < 5$) — Secant Plane:**
   Here $25 - c^2 > 0$. The intersection is a **circle** centered at $(0, 0, c)$ with radius:
   $$r(c) = \sqrt{25 - c^2} > 0.$$
   - At $c = 0$ (the equatorial plane), the radius attains its maximum value $r(0) = 5$ (a **great circle** of the sphere).
   - As $|c|$ increases from $0$ toward $5$, the quantity $25 - c^2$ decreases, so the circle's radius $r(c) = \sqrt{25 - c^2}$ **shrinks continuously** from $5$ toward $0$.

2. **Case 2: $|c| = 5$ (i.e., $c = 5$ or $c = -5$) — Tangent Plane:**
   Here $25 - c^2 = 0$, so the equation becomes:
   $$x^2 + y^2 = 0, \quad z = \pm 5.$$
   Since $x^2 + y^2 = 0 \iff x = 0, y = 0$, the intersection degenerates into a **single point** (radius $r = 0$):
   - For $c = 5$: the north pole $(0, 0, 5)$.
   - For $c = -5$: the south pole $(0, 0, -5)$.
   The planes $z = 5$ and $z = -5$ are tangent to the sphere at its poles.

3. **Case 3: $|c| > 5$ (i.e., $c > 5$ or $c < -5$) — Non-Intersecting Plane:**
   Here $25 - c^2 < 0$. Since $x^2 + y^2 \ge 0$ for all real $(x, y)$, the equation $x^2 + y^2 = 25 - c^2 < 0$ has **no real solutions**. The intersection is the **empty set** ($\emptyset$); the plane $z = c$ passes completely above or below the sphere without touching it.

## 4. Verification and Consistency Checks
1. **Pythagorean Theorem Check for $z = 3$:**
   - Distance from sphere center $(0,0,0)$ to plane $z = 3$ is $d = 3$.
   - Sphere radius is $R = 5$.
   - By the Pythagorean theorem, $r^2 + d^2 = R^2 \implies r = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = 4$, which matches our algebraic derivation.
2. **Sample Point Check:**
   Take the point $(4, 0, 3)$ on the circle $x^2 + y^2 = 16, \, z = 3$. Substituting into the sphere equation:
   $$4^2 + 0^2 + 3^2 = 16 + 0 + 9 = 25,$$
   and its $z$-coordinate is $3$, confirming it lies on both the sphere and the plane.
