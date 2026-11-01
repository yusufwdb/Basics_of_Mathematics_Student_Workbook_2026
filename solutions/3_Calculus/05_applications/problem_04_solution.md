# Exercise 4: Area Between Curves

## 1. Problem Statement

Find the area of the region bounded by the graphs
$$y=x$$
and
$$y=x^2.$$

First find the intersection points and justify which function is greater on the relevant interval.

---

## 2. Theoretical Background and Concepts

- **Area Between Two Curves:** If $f(x)$ and $g(x)$ are continuous on $[a,b]$ and $f(x) \ge g(x)$ for all $x \in [a,b]$ (i.e., the graph of $f$ lies on or above the graph of $g$), then the area $A$ of the region bounded between the two curves on $[a,b]$ is given by subtracting the lower function from the upper function:
  $$A = \int_a^b \left(f(x) - g(x)\right)\,dx.$$
- **Finding the Limits of Integration:** When the interval $[a,b]$ is not specified explicitly, the bounded region is enclosed between the points of intersection of the two curves, which are found by solving $f(x) = g(x)$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Finding the Intersection Points
To find the points where the line $y = x$ and the parabola $y = x^2$ intersect, we equate their formulas:
$$x^2 = x \implies x^2 - x = 0 \implies x(x - 1) = 0.$$
This yields two intersection abscissas:
$$x_1 = 0 \quad \text{and} \quad x_2 = 1.$$
The corresponding intersection points in the plane are $(0,0)$ and $(1,1)$, so the bounded region lies over the interval $[0, 1]$.

### Step 2: Justifying Which Function Is Greater on $[0, 1]$
For any $x \in (0, 1)$, we have $0 < x < 1$. Multiplying the inequality $x < 1$ by the positive number $x > 0$ preserves the inequality direction:
$$x \cdot x < 1 \cdot x \implies x^2 < x \quad \text{for all } x \in (0, 1).$$
(Equivalently, $x - x^2 = x(1 - x) > 0$ on $(0, 1)$ because both factors $x$ and $1-x$ are positive, or testing the midpoint $x = \frac{1}{2}$ gives $f(\frac{1}{2}) = \frac{1}{2} > g(\frac{1}{2}) = \frac{1}{4}$.)

Thus, the line $f(x) = x$ is the **upper curve** and the parabola $g(x) = x^2$ is the **lower curve** on $[0, 1]$.

### Step 3: Computing the Area by Integration
Using $A = \int_0^1 (x - x^2)\,dx$:
$$\begin{aligned}
A &= \int_0^1 \left(x - x^2\right)\,dx \\
&= \left[\frac{1}{2}x^2 - \frac{1}{3}x^3\right]_0^1 \\
&= \left(\frac{1}{2}(1)^2 - \frac{1}{3}(1)^3\right) - \left(0 - 0\right) \\
&= \frac{1}{2} - \frac{1}{3} = \frac{3 - 2}{6} = \frac{1}{6}.
\end{aligned}$$

---

## 4. Verification and Consistency Checks

1. **Positivity and Bounding Box Check:**
   The region is contained entirely inside the unit square $[0,1] \times [0,1]$, and more specifically inside the lower right triangle under $y = x$ (whose area is $\frac{1}{2} \cdot 1 \cdot 1 = \frac{1}{2}$). Our result $A = \frac{1}{6} > 0$ satisfies $0 < \frac{1}{6} < \frac{1}{2}$.
2. **Archimedes' Quadrature of the Parabola:**
   By Archimedes' classical theorem, the area under the parabola $y = x^2$ on $[0,1]$ is $\frac{1}{3}$ of the circumscribed $1 \times 1$ square ($\frac{1}{3}$), while the area of the triangle under $y = x$ is $\frac{1}{2}$ of the square. Subtracting gives $\frac{1}{2} - \frac{1}{3} = \frac{1}{6}$, matching our integral calculation.
3. **Integrating with Respect to $y$ (Horizontal Slices):**
   For $y \in [0, 1]$, the left boundary is $x = y$ and the right boundary is $x = \sqrt{y}$. Integrating with respect to $y$:
   $$A = \int_0^1 \left(\sqrt{y} - y\right)\,dy = \left[\frac{2}{3}y^{3/2} - \frac{1}{2}y^2\right]_0^1 = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}. \quad \checkmark$$
