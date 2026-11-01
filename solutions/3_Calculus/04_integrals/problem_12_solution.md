# Exercise 12: Symmetry, Sign, and Absolute Value

## 1. Problem Statement

Compare
$$\int_{-2}^{2}x\,dx$$
and
$$\int_{-2}^{2}|x|\,dx.$$
Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

---

## 2. Theoretical Background and Concepts

- **Definite Integrals of Odd and Even Functions on Symmetric Intervals $[-a, a]$:**
  - A function $f$ is **odd** if $f(-x) = -f(x)$ for all $x \in [-a, a]$. Its graph is symmetric with respect to the origin $(0,0)$, so the negative signed area on $[-a, 0]$ cancels the positive signed area on $[0, a]$:
    $$\int_{-a}^{a} f(x)\,dx = 0.$$
  - A function $g$ is **even** if $g(-x) = g(x)$ for all $x \in [-a, a]$. Its graph is symmetric with respect to the $y$-axis, so the signed area on $[-a, 0]$ equals the signed area on $[0, a]$:
    $$\int_{-a}^{a} g(x)\,dx = 2\int_{0}^{a} g(x)\,dx.$$
- **Piecewise Definition of Absolute Value:**
  $$|x| = \begin{cases} -x, & x < 0, \\ x, & x \ge 0. \end{cases}$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Prediction from Symmetry and Geometric Sketch

```
       y = x (Odd)                        y = |x| (Even)
            y                                   y
          2 |      /                          2 |\      /
            |    /                              |  \  /
     -2     |  /                         -2     |   \/     2
   ---------+--------- x               ---------+--------- x
       /    |    2                              |
     /      | -2                                |
```

1. **For $f(x) = x$ on $[-2, 2]$:**
   Since $f(-x) = -x = -f(x)$, $f(x) = x$ is an **odd function**. On $[-2, 0]$, the line $y = x$ forms a right triangle of base $2$ and height $2$ **below** the $x$-axis (signed area $-\frac{1}{2}\cdot 2\cdot 2 = -2$). On $[0, 2]$, it forms an congruent right triangle **above** the $x$-axis (signed area $+2$). By odd symmetry, the two signed areas cancel completely, so we predict:
   $$\int_{-2}^{2} x\,dx = 0.$$
2. **For $g(x) = |x|$ on $[-2, 2]$:**
   Since $g(-x) = |-x| = |x| = g(x)$, $g(x) = |x|$ is an **even function**, and $|x| \ge 0$ everywhere. The V-shaped graph forms two congruent right triangles of base $2$ and height $2$, **both above** the $x$-axis. Each triangle has area $\frac{1}{2} \cdot 2 \cdot 2 = 2$, so we predict:
   $$\int_{-2}^{2} |x|\,dx = 2 + 2 = 4.$$

---

### Step 2: Analytical Calculation

1. **First Integral:**
   $$\int_{-2}^{2} x\,dx = \left[\frac{1}{2}x^2\right]_{-2}^{2} = \frac{1}{2}(2)^2 - \frac{1}{2}(-2)^2 = 2 - 2 = 0.$$

2. **Second Integral:**
   Splitting the interval $[-2, 2]$ at $x = 0$ where $|x|$ changes its formula:
   $$\begin{aligned}
   \int_{-2}^{2} |x|\,dx &= \int_{-2}^{0} (-x)\,dx + \int_{0}^{2} x\,dx \\
   &= \left[-\frac{1}{2}x^2\right]_{-2}^{0} + \left[\frac{1}{2}x^2\right]_{0}^{2} \\
   &= \left(0 - \left(-\frac{1}{2}(-2)^2\right)\right) + \left(\frac{1}{2}(2)^2 - 0\right) \\
   &= 2 + 2 = 4.
   \end{aligned}$$
   Alternatively, using even symmetry directly:
   $$\int_{-2}^{2} |x|\,dx = 2\int_{0}^{2} x\,dx = 2\left[\frac{1}{2}x^2\right]_{0}^{2} = 2(2 - 0) = 4.$$

---

### Step 3: Explaining the Difference
The integral $\int_{-2}^{2} x\,dx = 0$ measures the **net signed area** (where negative values on $[-2, 0]$ cancel positive values on $[0, 2]$). In contrast, taking the absolute value $|x|$ reflects the negative portion of the graph across the $x$-axis into the upper half-plane, so $\int_{-2}^{2} |x|\,dx = 4$ measures the **total geometric area** of the two triangles without sign cancellation.

---

## 4. Verification and Consistency Checks

- Notice that the antiderivative of the odd function $f(x) = x$ is the even function $F(x) = \frac{1}{2}x^2$, which satisfies $F(2) = F(-2) = 2$, immediately giving $F(2) - F(-2) = 0$.
- The antiderivative of the even function $g(x) = |x|$ is the odd function $G(x) = \frac{1}{2}x|x|$, which satisfies $G(2) = 2$ and $G(-2) = -2$, giving $G(2) - G(-2) = 2 - (-2) = 4$. Both analytical and geometric checks agree completely.
