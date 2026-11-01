# Exercise 12: Recognizing a Surface from Cross-Sections

## 1. Problem Statement
A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\text{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

## 2. Theoretical Background and Concepts
- **Surfaces of Revolution:** If every horizontal cross-section $z = c$ is a circle centered on the $Oz$ axis, the equation of the surface depends on $x$ and $y$ only through the combination $x^2 + y^2 = r^2$, where $r = \sqrt{x^2 + y^2}$ is the distance to the $Oz$ axis.
- **Relating Horizontal Radius to Vertical Profile:** If a surface of revolution around the $Oz$ axis has equation $z = f(r) = f(\sqrt{x^2 + y^2})$, then intersecting the surface with any vertical plane containing the $Oz$ axis (for example, $y = 0$, where $r = |x|$) yields the plane curve $z = f(x)$.

## 3. Detailed Step-by-Step Solution

### Step 1: Translate each geometric condition into algebra
1. **Horizontal cross-sections for $z = c > 0$ are circles:**
   A circle in the plane $z = c$ (assuming its center lies on the $Oz$ axis) has an equation of the form
   $$x^2 + y^2 = R(z)^2,$$
   where $R(z) > 0$ is the radius of the circle at height $z$.

2. **Vertical cross-sections through the $Oz$ axis are parabolas:**
   Any vertical plane containing the $Oz$ axis can be parameterized by a signed horizontal coordinate $u$ (for instance, in the plane $y = 0$, $u = x$; in the plane $x = 0$, $u = y$). Since the intersection curve is a parabola symmetric about $Oz$ with its vertex at $z = 0$ and opening upward ($z \ge 0$), its equation in that vertical plane must have the form:
   $$z = a u^2 \quad (a > 0).$$
   Choosing the simplest positive constant $a = 1$ gives the parabola $z = u^2$.

3. **Combine the horizontal and vertical conditions:**
   Since the distance squared from the $Oz$ axis is $u^2 = x^2 + y^2$, replacing $u^2$ by $x^2 + y^2$ gives the simplest equation:
   $$z = x^2 + y^2.$$
   *(More generally, $z = a(x^2 + y^2)$ for any constant $a > 0$ satisfies all three conditions; we choose $a = 1$ for simplicity.)*

### Step 2: Justify that $z = x^2 + y^2$ satisfies all three required properties
1. **Property 1 — Cross-section $z = 0$ is a point:**
   Setting $z = 0$ in $z = x^2 + y^2$ yields:
   $$x^2 + y^2 = 0.$$
   Since $x^2 \ge 0$ and $y^2 \ge 0$ for real $x, y$, their sum is zero if and only if $x = 0$ and $y = 0$. Thus, the cross-section $z = 0$ consists of the single point $(0, 0, 0)$.

2. **Property 2 — For $z > 0$, the cross-sections $z = c$ are circles with increasing radius:**
   Setting $z = c$ with $c > 0$ yields:
   $$x^2 + y^2 = c = (\sqrt{c})^2.$$
   This is a circle in the plane $z = c$ centered at $(0, 0, c)$ with radius $r(c) = \sqrt{c}$. Since the square-root function $r(c) = \sqrt{c}$ is strictly increasing for $c > 0$ ($0 < c_1 < c_2 \implies \sqrt{c_1} < \sqrt{c_2}$), the circles have strictly increasing radius as $z$ increases.

3. **Property 3 — Vertical cross-sections through the $Oz$ axis are parabolas:**
   Any vertical plane through the $Oz$ axis can be written in cylindrical coordinates as $\theta = \theta_0$ (or $x = u\cos\theta_0, \, y = u\sin\theta_0$, where $u \in \mathbb{R}$ is the horizontal coordinate along the plane). Substituting this into $z = x^2 + y^2$ gives:
   $$z = (u\cos\theta_0)^2 + (u\sin\theta_0)^2 = u^2(\cos^2\theta_0 + \sin^2\theta_0) = u^2.$$
   In every such vertical plane, the cross-section is the parabola $z = u^2$.

### Final Answer
The simplest equation is the circular paraboloid:
$$z = x^2 + y^2.$$

## 4. Verification and Consistency Checks
Why couldn't the surface be the upper half-cone $z = \sqrt{x^2 + y^2}$ (i.e., $z^2 = x^2 + y^2, \, z \ge 0$)?
- For the upper half-cone, $z = 0$ is also a single point $(0,0,0)$, and for $z = c > 0$ the cross-sections $x^2 + y^2 = c^2$ are also circles of increasing radius $r(c) = c$.
- **However**, intersecting the cone with a vertical plane through $Oz$ (e.g., $y = 0$) gives $z = |x|$, which is a pair of half-lines (a V-shape), **not** a parabola.
This confirms that the third condition (parabolic vertical cross-sections) uniquely selects the paraboloid $z = a(x^2 + y^2)$ ($a > 0$) over a cone or other surfaces of revolution.
