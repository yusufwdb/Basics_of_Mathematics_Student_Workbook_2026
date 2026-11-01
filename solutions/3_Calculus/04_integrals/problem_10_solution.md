# Exercise 10: Definite Integral and Checking the Result

## 1. Problem Statement

Before carrying out the exact calculation, estimate the possible range of values of the integral
$$\int_0^2(x^2+1)\,dx,$$
using
$$1\le x^2+1\le5$$
on $[0,2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

---

## 2. Theoretical Background and Concepts

- **Comparison Property (Bounds) of the Definite Integral:** If $f(x)$ is integrable on $[a,b]$ and satisfies
  $$m \le f(x) \le M \quad \text{for all } x \in [a,b],$$
  then the definite integral is bounded by the areas of the rectangles of width $(b-a)$ and heights $m$ and $M$:
  $$m(b - a) \le \int_a^b f(x)\,dx \le M(b - a).$$
- **Fundamental Theorem of Calculus:**
  $$\int_a^b f(x)\,dx = F(b) - F(a), \quad \text{where } F'(x) = f(x).$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Estimating the Range of Values Before Calculating
On the interval $[0, 2]$, the function $f(x) = x^2 + 1$ is strictly increasing because $f'(x) = 2x > 0$ for $x \in (0, 2]$. Therefore, its minimum value on $[0, 2]$ is $m = f(0) = 0^2 + 1 = 1$, and its maximum value on $[0, 2]$ is $M = f(2) = 2^2 + 1 = 5$:
$$1 \le x^2 + 1 \le 5 \quad \text{for all } x \in [0, 2].$$
The length of the interval $[0, 2]$ is $b - a = 2 - 0 = 2$. Applying the bounding inequality $m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$:
$$1 \cdot (2 - 0) \le \int_0^2 (x^2+1)\,dx \le 5 \cdot (2 - 0),$$
$$2 \le \int_0^2 (x^2+1)\,dx \le 10.$$
Geometrically, the area under the parabola $y = x^2+1$ on $[0,2]$ contains a rectangle of width $2$ and height $1$ (area $2$) and is contained inside a rectangle of width $2$ and height $5$ (area $10$).

### Step 2: Computing the Integral Exactly
An antiderivative of $f(x) = x^2 + 1$ is $F(x) = \frac{1}{3}x^3 + x$. Evaluating between $x = 0$ and $x = 2$:
$$\begin{aligned}
\int_0^2 (x^2 + 1)\,dx &= \left[\frac{1}{3}x^3 + x\right]_0^2 \\
&= \left(\frac{1}{3}(2)^3 + 2\right) - \left(\frac{1}{3}(0)^3 + 0\right) \\
&= \frac{8}{3} + 2 \\
&= \frac{8}{3} + \frac{6}{3} = \frac{14}{3} = 4\frac{2}{3} \approx 4.67.
\end{aligned}$$

### Step 3: Comparing the Exact Result with the Estimate and Explaining What Errors It Detects
Comparing $\frac{14}{3} \approx 4.67$ with the interval $[2, 10]$:
$$2 \le \frac{14}{3} \le 10 \quad \left(\text{since } \frac{6}{3} \le \frac{14}{3} \le \frac{30}{3}\right).$$
The exact value lies comfortably inside the predicted range (in fact, slightly below the midpoint $6$ because $x^2+1$ is convex on $[0,2]$).

**What types of computational errors this check detects:**
1. **Sign errors or reversed limits of integration:** e.g., computing $F(0) - F(2) = -\frac{14}{3} < 2$.
2. **Differentiating instead of integrating:** e.g., writing $[2x]_0^2 = 4$, or forgetting to integrate the constant term $1$ (which would give $\frac{8}{3}$—still in $[2,10]$, though a tighter trapezoid upper bound $\frac{1+5}{2}\cdot 2 = 6$ also helps).
3. **Gross arithmetic or power-rule errors:** e.g., multiplying by $3$ instead of dividing by $3$ in the power rule ($[3x^3+x]_0^2 = 26 > 10$), or substituting the wrong upper bound.

---

## 4. Verification and Consistency Checks

### Convexity / Trapezoidal Bound Check
Since $f''(x) = 2 > 0$, the function $f(x) = x^2 + 1$ is strictly convex on $[0, 2]$. Consequently, the graph of $f$ lies below the secant line connecting $(0, 1)$ and $(2, 5)$, and above the tangent line at the midpoint $x = 1$ (where $f(1) = 2$):
- **Midpoint tangent lower bound:** $f(1) \cdot (2 - 0) = 2 \cdot 2 = 4 = \frac{12}{3}$.
- **Trapezoidal secant upper bound:** $\frac{f(0) + f(2)}{2} \cdot (2 - 0) = \frac{1 + 5}{2} \cdot 2 = 6 = \frac{18}{3}$.

Indeed, $4 < \frac{14}{3} < 6$, providing an even sharper verification of our exact result $\frac{14}{3}$.
