# Exercise 9: Definite Integral and Geometric Area

## 1. Problem Statement

Compute
$$\int_{-1}^{2}x\,dx.$$
Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

---

## 2. Theoretical Background and Concepts

- **Fundamental Theorem of Calculus (Newton–Leibniz Formula):** If $f$ is continuous on $[a,b]$ and $F$ is any antiderivative of $f$ ($F' = f$), then
  $$\int_a^b f(x)\,dx = \left[F(x)\right]_a^b = F(b) - F(a).$$
- **Definite Integral (Signed Area) vs. Geometric Area:**
  - The **definite integral** $\int_a^b f(x)\,dx$ computes the **net signed area** between the graph of $y = f(x)$ and the $x$-axis: regions where $f(x) > 0$ (above the $x$-axis) contribute positively, while regions where $f(x) < 0$ (below the $x$-axis) contribute negatively:
    $$\int_a^b f(x)\,dx = A_{\text{above}} - A_{\text{below}}.$$
  - The **total geometric area** bounded by the graph of $f(x)$ and the $x$-axis on $[a,b]$ is always non-negative and equals the integral of the absolute value $|f(x)|$:
    $$A_{\text{total}} = \int_a^b |f(x)|\,dx = A_{\text{above}} + A_{\text{below}}.$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Computing the Definite Integral Directly
An antiderivative of $f(x) = x$ is $F(x) = \frac{1}{2}x^2$. By the Fundamental Theorem of Calculus:
$$\int_{-1}^{2} x\,dx = \left[\frac{1}{2}x^2\right]_{-1}^{2} = \frac{1}{2}(2)^2 - \frac{1}{2}(-1)^2 = \frac{4}{2} - \frac{1}{2} = 2 - \frac{1}{2} = \frac{3}{2} = 1.5.$$

### Step 2: Computing the Areas Below and Above the $x$-Axis Separately
The function $f(x) = x$ crosses the $x$-axis at $x = 0$:
- On $[-1, 0]$, we have $x \le 0$ (the graph lies **below** the $x$-axis).
- On $[0, 2]$, we have $x \ge 0$ (the graph lies **above** the $x$-axis).

1. **Part below the $x$-axis on $[-1, 0]$:**
   The signed integral on $[-1, 0]$ is
   $$\int_{-1}^{0} x\,dx = \left[\frac{1}{2}x^2\right]_{-1}^{0} = 0 - \frac{1}{2}(-1)^2 = -\frac{1}{2}.$$
   The **geometric area** of this region is the positive magnitude:
   $$A_{\text{below}} = \int_{-1}^{0} (-x)\,dx = \frac{1}{2} = 0.5.$$
   (Geometrically, this is a right triangle with base $1$ and height $1$, so $A_{\text{below}} = \frac{1}{2} \cdot 1 \cdot 1 = \frac{1}{2}$.)

2. **Part above the $x$-axis on $[0, 2]$:**
   Since $x \ge 0$ on $[0, 2]$, the geometric area equals the integral:
   $$A_{\text{above}} = \int_{0}^{2} x\,dx = \left[\frac{1}{2}x^2\right]_{0}^{2} = \frac{1}{2}(2)^2 - 0 = 2.$$
   (Geometrically, this is a right triangle with base $2$ and height $2$, so $A_{\text{above}} = \frac{1}{2} \cdot 2 \cdot 2 = 2$.)

### Step 3: Explaining the Difference Between the Definite Integral and Geometric Area
- **Definite Integral (Net Signed Area):** Subtracting the area below the axis from the area above the axis gives
  $$\int_{-1}^{2} x\,dx = A_{\text{above}} - A_{\text{below}} = 2 - \frac{1}{2} = \frac{3}{2} = 1.5.$$
  This represents net accumulation (where negative values partially cancel positive values).
- **Total Geometric Area:** Summing the positive areas of both triangles gives
  $$A_{\text{total}} = \int_{-1}^{2} |x|\,dx = A_{\text{above}} + A_{\text{below}} = 2 + \frac{1}{2} = \frac{5}{2} = 2.5.$$

---

## 4. Verification and Consistency Checks

Using the additivity of the definite integral over intervals, $\int_{-1}^{2} x\,dx = \int_{-1}^{0} x\,dx + \int_{0}^{2} x\,dx$:
$$-\frac{1}{2} + 2 = \frac{3}{2}.$$
Both the elementary triangle area formulas ($\frac{1}{2}\text{base}\times\text{height}$) and the Newton–Leibniz evaluation yield identical results.
