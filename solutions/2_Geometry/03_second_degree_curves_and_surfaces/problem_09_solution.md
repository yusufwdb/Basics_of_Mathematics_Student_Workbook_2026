# Exercise 9: Ellipsoid and Its Cross-Sections

## 1. Problem Statement
Consider
$$\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{16}=1.$$
Give the semiaxis lengths, describe the cross-section $z=0$, and explain how the cross-sections $z=c$ change for $|c|<4$.

## 2. Theoretical Background and Concepts
- **Canonical Equation of an Ellipsoid:**
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c_0^2} = 1 \quad (a, b, c_0 > 0).$$
  The surface is symmetric with respect to all three coordinate planes, centered at the origin $(0,0,0)$, and bounded within the box $[-a, a] \times [-b, b] \times [-c_0, c_0]$.
- **Method of Cross-Sections (Traces):** Intersecting a 3D surface $F(x,y,z) = 0$ with a horizontal plane $z = c$ yields a 2D curve $F(x,y,c) = 0$ lying in that plane. By tracking how the size and shape of these 2D curves vary with height $c$, we reconstruct the 3D geometry of the surface.

## 3. Detailed Step-by-Step Solution

### Step 1: Find the semiaxis lengths
Comparing the given equation
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1$$
with $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c_0^2} = 1$, we read off the squares of the semiaxes:
- **Along the $x$-axis ($Ox$):** $a^2 = 9 \implies a = 3$ (intercepts at $(\pm 3, 0, 0)$).
- **Along the $y$-axis ($Oy$):** $b^2 = 4 \implies b = 2$ (intercepts at $(0, \pm 2, 0)$).
- **Along the $z$-axis ($Oz$):** $c_0^2 = 16 \implies c_0 = 4$ (intercepts at $(0, 0, \pm 4)$).

*(Note: The ellipsoid is most elongated vertically along the $z$-axis since $c_0 = 4$ is the largest semiaxis, and narrowest along the $y$-axis where $b = 2$.)*

### Step 2: Describe the cross-section $z = 0$
Setting $z = 0$ in the ellipsoid equation gives:
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{0^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1, \quad z = 0.$$
This cross-section is an **ellipse** in the $xy$-plane centered at $(0,0,0)$, with:
- horizontal semiaxis $a = 3$ (along the $x$-axis),
- vertical semiaxis $b = 2$ (along the $y$-axis).

### Step 3: Analyze the cross-sections $z = c$ for $|c| < 4$
Substitute $z = c$ into the surface equation:
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{c^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}.$$
Since $|c| < 4$, we have $c^2 < 16$, so the right-hand side $k(c) = 1 - \frac{c^2}{16}$ is strictly positive ($0 < k(c) \le 1$). Dividing both sides by $1 - \frac{c^2}{16}$ puts the cross-section into canonical ellipse form:
$$\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1.$$
From this equation, we see how the cross-sections behave as $c$ varies:
1. **Shape:** For every $c \in (-4, 4)$, the cross-section in the plane $z = c$ is an **ellipse** centered at $(0, 0, c)$ with semiaxes:
   $$a(c) = 3\sqrt{1 - \frac{c^2}{16}} \quad \text{and} \quad b(c) = 2\sqrt{1 - \frac{c^2}{16}}.$$
2. **Constant Aspect Ratio (Similarity):** The ratio of the semiaxes is
   $$\frac{a(c)}{b(c)} = \frac{3}{2},$$
   which is independent of $c$. Thus, all horizontal cross-sections for $|c| < 4$ are geometrically similar ellipses scaled by the factor $\sqrt{1 - \frac{c^2}{16}}$.
3. **Evolution with height $c$:**
   - At the equator $c = 0$, the ellipse is largest, with semiaxes $a(0) = 3$ and $b(0) = 2$.
   - As $|c|$ increases from $0$ toward $4$ (moving either upward toward $z = 4$ or downward toward $z = -4$), the scaling factor $\sqrt{1 - \frac{c^2}{16}}$ decreases monotonically toward $0$, so the ellipses **shrink symmetrically**.
   - At the poles $c = \pm 4$, the cross-section degenerates into a single point $(0, 0, \pm 4)$, and for $|c| > 4$ the cross-section is empty.

## 4. Verification and Consistency Checks
Let us check a specific intermediate plane, say $c = 2\sqrt{3}$ (so $c^2 = 12 < 16$):
- Scaling factor: $1 - \frac{12}{16} = \frac{1}{4} \implies \sqrt{1 - \frac{c^2}{16}} = \frac{1}{2}$.
- The semiaxes at $z = 2\sqrt{3}$ are $a(2\sqrt{3}) = \frac{3}{2}$ and $b(2\sqrt{3}) = 1$.
- Substituting the point $\left(\frac{3}{2}, 0, 2\sqrt{3}\right)$ into the original ellipsoid equation gives:
  $$\frac{(3/2)^2}{9} + \frac{0^2}{4} + \frac{(2\sqrt{3})^2}{16} = \frac{9/4}{9} + 0 + \frac{12}{16} = \frac{1}{4} + \frac{3}{4} = 1.$$
  This confirms our formula for the cross-sectional ellipses.
