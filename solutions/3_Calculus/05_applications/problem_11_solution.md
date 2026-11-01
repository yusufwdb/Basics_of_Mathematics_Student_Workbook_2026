# Exercise 11: Volume of a Solid of Revolution

## 1. Problem Statement

The region under the graph
$$y=\sqrt{x},\qquad x\in[0,4],$$
is rotated about the $x$-axis.

1. Construct the integral describing the volume using the disk method.
2. Compute the volume.
3. Explain where the factor $\pi y^2$ in the integral comes from.

---

## 2. Theoretical Background and Concepts

- **Solids of Revolution and the Method of Cross-Sections (Cavalieri's Principle):**
  If a three-dimensional solid lies between the planes $x = a$ and $x = b$, and the area of its cross-section perpendicular to the $x$-axis at position $x$ is $A(x)$, then the volume of the solid is the definite integral of the cross-sectional area:
  $$V = \int_a^b A(x)\,dx.$$
- **The Disk Method (Rotation About the $x$-Axis):**
  When the planar region bounded by $y = f(x) \ge 0$, the $x$-axis, $x = a$, and $x = b$ is revolved by $360^\circ$ ($2\pi$ radians) around the $x$-axis, every vertical line segment from $(x, 0)$ to $(x, f(x))$ sweeps out a circular disk of radius $R(x) = y = f(x)$, giving cross-sectional area $A(x) = \pi [f(x)]^2$.

---

## 3. Detailed Step-by-Step Solution

### Part 3 & Part 1: Explaining the Origin of $\pi y^2$ and Constructing the Integral
*(We address the geometric origin first, as it directly motivates the construction of the integral.)*

1. **Where the factor $\pi y^2$ comes from:**
   - Partition the interval $[0, 4]$ along the $x$-axis into thin subintervals of width $\Delta x$.
   - Over a thin subinterval at coordinate $x$, the planar region under $y = f(x) = \sqrt{x}$ is approximately a thin vertical rectangle of height $y = f(x)$ and width $\Delta x$.
   - When this thin vertical rectangle is rotated completely around the $x$-axis, its top edge stays at distance $R = y = f(x)$ from the $x$-axis, sweeping out a **thin circular cylinder (disk)** of **radius $R = y$** and **thickness (height) $\Delta x$**.
   - The area of a circle of radius $y$ is $A(x) = \pi R^2 = \pi y^2$, so the volume of the thin disk is
     $$\Delta V \approx (\text{circular face area}) \times (\text{thickness}) = \pi y^2\,\Delta x.$$
   - Summing these disk volumes over $[0, 4]$ and taking the limit as $\Delta x \to 0$ produces the definite integral $\int_0^4 \pi y^2\,dx$.

2. **Constructing the Integral for $y = \sqrt{x}$ on $[0, 4]$:**
   Substituting $y = \sqrt{x}$ into $A(x) = \pi y^2$ gives:
   $$A(x) = \pi \left(\sqrt{x}\right)^2 = \pi x \quad \text{for } x \in [0, 4].$$
   Therefore, the integral describing the volume of the paraboloid of revolution is:
   $$V = \int_0^4 \pi \left(\sqrt{x}\right)^2\,dx = \pi \int_0^4 x\,dx.$$

### Part 2: Computing the Volume
Evaluating the definite integral:
$$\begin{aligned}
V &= \pi \int_0^4 x\,dx \\
&= \pi \left[\frac{1}{2}x^2\right]_0^4 \\
&= \pi \left(\frac{1}{2}(4)^2 - \frac{1}{2}(0)^2\right) \\
&= \pi (8 - 0) = 8\pi \approx 25.13.
\end{aligned}$$

---

## 4. Verification and Consistency Checks

1. **Comparison with the Circumscribed Cylinder and Cone (Archimedes' Paraboloid Theorem):**
   - At $x = 4$, the maximum radius of the paraboloid is $R_{\max} = \sqrt{4} = 2$, and its length (height along the $x$-axis) is $H = 4$.
   - A right circular cylinder of radius $R_{\max} = 2$ and height $H = 4$ surrounding our solid has volume
     $$V_{\text{cylinder}} = \pi R_{\max}^2 H = \pi (2)^2 (4) = 16\pi.$$
   - A right circular cone inscribed inside with the same base and apex at $(0,0)$ has volume
     $$V_{\text{cone}} = \frac{1}{3}\pi R_{\max}^2 H = \frac{16\pi}{3} \approx 5.33\pi.$$
   - Because $y = \sqrt{x}$ is concave on $[0, 4]$, the paraboloid strictly contains the cone and is strictly contained inside the cylinder:
     $$\frac{16\pi}{3} < 8\pi < 16\pi.$$
   - Even more specifically, Archimedes proved that the volume of a paraboloid of revolution is **exactly half the volume of its circumscribed cylinder**: $\frac{1}{2}(16\pi) = 8\pi$, confirming our result!
