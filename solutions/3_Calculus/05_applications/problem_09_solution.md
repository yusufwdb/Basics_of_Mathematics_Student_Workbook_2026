# Exercise 9: Minimizing the Material Used for a Can

## 1. Problem Statement

A closed cylinder has fixed volume $V$.

1. Write the volume constraint.
2. Eliminate one of the variables.
3. Express the surface area as a function of the radius $r$.
4. Find the relation between the height $h$ and the radius $r$ for which the material usage is minimal.

Interpret the obtained relation geometrically.

---

## 2. Theoretical Background and Concepts

- **Geometry of a Right Circular Cylinder (Radius $r > 0$, Height $h > 0$):**
  - **Volume:** $V = (\text{base area}) \times (\text{height}) = \pi r^2 h$.
  - **Total Surface Area of a Closed Cylinder:** Consists of two circular lids (top and bottom, each of area $\pi r^2$) and the lateral curved wall (which unrolls into a rectangle of width $2\pi r$ and height $h$, area $2\pi r h$):
    $$S(r, h) = 2\pi r^2 + 2\pi r h.$$
- **Constrained Optimization on an Open Domain $(0, \infty)$:**
  After eliminating $h$ using the fixed volume constraint $V = \pi r^2 h$, we minimize the single-variable objective function $S(r)$ on $r \in (0, \infty)$ using the first and second derivatives $S'(r)$ and $S''(r)$.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Writing the Volume Constraint
Let $r > 0$ be the radius of the circular base and $h > 0$ be the height of the cylinder. For a fixed positive volume $V > 0$, the volume constraint is:
$$\pi r^2 h = V.$$

### Part 2: Eliminating One of the Variables
Since $h$ appears linearly in both the volume constraint and the surface area formula, it is easiest to solve the volume constraint for $h$ in terms of $r$:
$$h = \frac{V}{\pi r^2}, \qquad r \in (0, \infty).$$

### Part 3: Expressing the Surface Area as a Function of the Radius $r$
Substituting $h = \frac{V}{\pi r^2}$ into the total surface area formula $S = 2\pi r^2 + 2\pi r h$:
$$\begin{aligned}
S(r) &= 2\pi r^2 + 2\pi r \left(\frac{V}{\pi r^2}\right) \\
&= 2\pi r^2 + \frac{2V}{r} \\
&= 2\pi r^2 + 2V r^{-1}, \qquad r \in (0, \infty).
\end{aligned}$$

### Part 4: Finding the Optimal Relation Between $h$ and $r$
We differentiate $S(r) = 2\pi r^2 + 2V r^{-1}$ with respect to $r$ on $(0, \infty)$:
$$S'(r) = 4\pi r - 2V r^{-2} = 4\pi r - \frac{2V}{r^2}.$$
Setting $S'(r) = 0$ to find the critical point:
$$4\pi r - \frac{2V}{r^2} = 0 \implies 4\pi r = \frac{2V}{r^2} \implies 2\pi r^3 = V.$$
To find the direct relation between the optimal height $h$ and the optimal radius $r$ without needing to compute cube roots, we substitute the original expression $V = \pi r^2 h$ back into $2\pi r^3 = V$:
$$2\pi r^3 = \pi r^2 h.$$
Dividing both sides by $\pi r^2 > 0$ yields the remarkably simple relation:
$$h = 2r.$$
Explicitly, the optimal dimensions in terms of $V$ are:
$$r^* = \sqrt[3]{\frac{V}{2\pi}}, \qquad h^* = 2r^* = 2\sqrt[3]{\frac{V}{2\pi}} = \sqrt[3]{\frac{4V}{\pi}}.$$

**Verification of Global Minimum:**
Computing the second derivative of $S(r)$ on $(0, \infty)$:
$$S''(r) = 4\pi + \frac{4V}{r^3} > 0 \quad \text{for all } r > 0.$$
Since $S''(r) > 0$ everywhere on $(0, \infty)$, $S(r)$ is strictly convex on $(0, \infty)$, proving that $h = 2r$ gives the unique **global minimum** of material usage.

### Geometric Interpretation of $h = 2r$
Since $2r = d$ is the **diameter** of the circular base, the condition $h = 2r$ means that the **height of the optimal closed cylindrical can is equal to its diameter** ($h = d$). Consequently:
- Every vertical cross-section passing through the central axis of the cylinder is a **square** of side length $2r \times 2r$.
- The cylinder can be circumscribed tightly around a sphere of radius $r$; among all right circular cylinders of fixed volume, this "equilateral cylinder" ($h = 2r$) is the most compact (most sphere-like) shape, minimizing surface area.

---

## 4. Verification and Consistency Checks

1. **Boundary Behavior:**
   - As $r \to 0^+$ (an extremely thin, tall tube), $S(r) \approx \frac{2V}{r} \to +\infty$.
   - As $r \to +\infty$ (an extremely wide, flat disk), $S(r) \approx 2\pi r^2 \to +\infty$.
   This confirms that $S(r)$ has a global minimum and no global maximum on $(0, \infty)$.
2. **AM–GM Inequality Check:**
   Splitting the lateral area term $\frac{2V}{r}$ into two equal halves $\frac{V}{r} + \frac{V}{r}$ and applying the 3-term AM–GM inequality:
   $$S(r) = 2\pi r^2 + \frac{V}{r} + \frac{V}{r} \ge 3\sqrt[3]{2\pi r^2 \cdot \frac{V}{r} \cdot \frac{V}{r}} = 3\sqrt[3]{2\pi V^2},$$
   with equality if and only if $2\pi r^2 = \frac{V}{r} \iff 2\pi r^3 = V \iff h = 2r$.
