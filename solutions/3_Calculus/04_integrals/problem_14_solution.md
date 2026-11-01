# Exercise 14: A Piecewise-Defined Function

## 1. Problem Statement

Let
$$f(x)=\begin{cases}x+1,&-1\le x<1,\\2,&1\le x\le3.\end{cases}$$
Sketch the graph, decide where to split the integral, compute
$$\int_{-1}^{3}f(x)\,dx$$
and verify the result geometrically.

---

## 2. Theoretical Background and Concepts

- **Additivity of the Definite Integral Over Adjacent Intervals:** If $f$ is integrable on $[a,b]$ and $c \in (a,b)$, then
  $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx.$$
- **Integrating Piecewise-Defined Functions:** When a function $f(x)$ is defined by different algebraic formulas on subintervals of $[a,b]$, we split the definite integral at the transition points (breakpoints) where the formula changes, and apply the Fundamental Theorem of Calculus on each subinterval separately.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Sketching the Graph and Checking Continuity at the Breakpoint
We analyze the two pieces of $f(x)$ on $[-1, 3]$:
1. On $[-1, 1)$, $f(x) = x + 1$ is a straight line segment rising from $(-1, 0)$ to $(1, 2)$ with slope $1$.
2. On $[1, 3]$, $f(x) = 2$ is a horizontal line segment at height $y = 2$ from $(1, 2)$ to $(3, 2)$.

Notice that at the transition point $x = 1$, $\lim_{x \to 1^-} (x+1) = 2 = f(1)$, so $f(x)$ is continuous on the entire interval $[-1, 3]$.

```
      y
    3 |
    2 |         *-------------*  y = 2
      |       / |             |
    1 |     *   |   Square    |
      |   / Tri |   (2 x 2)   |
    0 +-*-------+-------------+--- x
     -1 0       1             3
```

### Step 2: Deciding Where to Split the Integral
Because the algebraic formula defining $f(x)$ changes at $x = 1$, we split the integral $\int_{-1}^{3} f(x)\,dx$ at $c = 1$:
$$\int_{-1}^{3} f(x)\,dx = \int_{-1}^{1} f(x)\,dx + \int_{1}^{3} f(x)\,dx = \int_{-1}^{1} (x + 1)\,dx + \int_{1}^{3} 2\,dx.$$

### Step 3: Computing Each Integral Analytically
1. **First subinterval $[-1, 1]$:**
   $$\int_{-1}^{1} (x + 1)\,dx = \left[\frac{1}{2}x^2 + x\right]_{-1}^{1} = \left(\frac{1}{2}(1)^2 + 1\right) - \left(\frac{1}{2}(-1)^2 + (-1)\right) = \frac{3}{2} - \left(-\frac{1}{2}\right) = 2.$$
2. **Second subinterval $[1, 3]$:**
   $$\int_{1}^{3} 2\,dx = \left[2x\right]_{1}^{3} = 2(3) - 2(1) = 6 - 2 = 4.$$
3. **Total Integral:**
   $$\int_{-1}^{3} f(x)\,dx = 2 + 4 = 6.$$

---

## 4. Verification and Consistency Checks

### Geometric Area Verification
Since $f(x) \ge 0$ on $[-1, 3]$, the definite integral equals the geometric area under the graph:
1. **Region on $[-1, 1]$:** A right triangle with base $b_1 = 1 - (-1) = 2$ and height $h_1 = 2$. Its area is
   $$A_1 = \frac{1}{2} \cdot b_1 \cdot h_1 = \frac{1}{2} \cdot 2 \cdot 2 = 2.$$
2. **Region on $[1, 3]$:** A rectangle (specifically a $2 \times 2$ square) with width $b_2 = 3 - 1 = 2$ and height $h_2 = 2$. Its area is
   $$A_2 = b_2 \cdot h_2 = 2 \cdot 2 = 4.$$
3. **Combined Trapezoid Check:** Alternatively, the entire region on $[-1, 3]$ is a right trapezoid with bottom base $a = 3 - (-1) = 4$, top base $b = 3 - 1 = 2$, and height $h = 2$:
   $$A_{\text{total}} = \frac{a + b}{2} \cdot h = \frac{4 + 2}{2} \cdot 2 = 6.$$
All geometric and analytical methods yield the exact same value, $6$.
