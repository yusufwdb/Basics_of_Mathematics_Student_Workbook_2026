# Exercise 9: A Logarithm and the Chain Rule

## 1. Problem Statement
For
$$f(x)=\ln(x^2+1)$$
compute the derivative. Then determine the sign of $f'(x)$ for $x<0$, $x=0$, and $x>0$, and describe qualitatively how the function behaves around zero.

---

## 2. Theoretical Background and Concepts
- **Derivative of the Natural Logarithm and Logarithmic Differentiation Rule:**
  For $u > 0$, $\frac{d}{du}(\ln u) = \frac{1}{u}$. Combined with the chain rule for a positive differentiable function $u(x) > 0$:
  $$\frac{d}{dx}\big(\ln(u(x))\big) = \frac{1}{u(x)} \cdot u'(x) = \frac{u'(x)}{u(x)}$$
- **Connection Between the Sign of $f'(x)$ and Function Behavior:**
  - If $f'(x) < 0$ on an interval, $f$ is strictly **decreasing** on that interval.
  - If $f'(x) > 0$ on an interval, $f$ is strictly **increasing** on that interval.
  - If $f'(x_0) = 0$ and $f'(x)$ changes sign from negative (for $x < x_0$) to positive (for $x > x_0$), then $f$ attains a **strict local (and here global) minimum** at $x_0$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Check the domain and compute the derivative $f'(x)$
Since $x^2 \ge 0$ for all $x \in \mathbb{R}$, we have $u(x) = x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$. Thus the domain of $f$ is $D_f = \mathbb{R}$.

Applying the chain rule to $f(x) = \ln(u(x))$ with outer function $g(u) = \ln u$ and inner function $u(x) = x^2 + 1$:
- Outer derivative: $g'(u) = \frac{1}{u} = \frac{1}{x^2 + 1}$
- Inner derivative: $u'(x) = \frac{d}{dx}(x^2 + 1) = 2x$

Multiplying them together gives:
$$f'(x) = \frac{1}{x^2 + 1} \cdot 2x = \frac{2x}{x^2 + 1}$$

### Step 2: Determine the sign of $f'(x)$ for $x < 0$, $x = 0$, and $x > 0$
Notice that the denominator $x^2 + 1$ is strictly positive ($x^2 + 1 \ge 1 > 0$) for every real number $x$. Therefore, the sign of $f'(x) = \frac{2x}{x^2+1}$ is determined entirely by the sign of the numerator $2x$:
1. **For $x < 0$:** $2x < 0$ and $x^2 + 1 > 0 \implies f'(x) < 0$ (negative).
2. **For $x = 0$:** $2(0) = 0 \implies f'(0) = \frac{0}{1} = 0$ (zero).
3. **For $x > 0$:** $2x > 0$ and $x^2 + 1 > 0 \implies f'(x) > 0$ (positive).

We can summarize this in a sign table:

| Interval / Point | $(-\infty, 0)$ | $x = 0$ | $(0, \infty)$ |
| :--- | :---: | :---: | :---: |
| Sign of $2x$ | $-$ | $0$ | $+$ |
| Sign of $x^2 + 1$ | $+$ | $+$ | $+$ |
| **Sign of $f'(x)$** | **$-$** | **$0$** | **$+$** |
| **Behavior of $f(x)$** | Strictly decreasing $\searrow$ | Global minimum ($f(0)=0$) | Strictly increasing $\nearrow$ |

### Step 3: Qualitative description of how $f(x)$ behaves around zero
- As $x$ approaches $0$ from the left ($x < 0$), $f'(x) < 0$, so the function $f(x)$ decreases steadily toward $f(0) = \ln(1) = 0$.
- At $x = 0$, $f'(0) = 0$, so the graph levels off with a horizontal tangent line at the origin $(0, 0)$ and attains its global minimum value of $0$.
- As $x$ moves to the right of $0$ ($x > 0$), $f'(x) > 0$, so $f(x)$ increases steadily away from $0$.
- Because $f(-x) = \ln((-x)^2 + 1) = \ln(x^2 + 1) = f(x)$, the graph is symmetric with respect to the $y$-axis and has a smooth, U-shaped (parabola-like) valley centered at the origin $(0, 0)$.

---

## 4. Verification and Consistency Checks

### Taylor Approximation and Second Derivative Check Near $x = 0$
1. **Maclaurin Expansion Check:** Using $\ln(1 + u) = u - \frac{u^2}{2} + O(u^3)$ with $u = x^2$:
   $$f(x) = \ln(1 + x^2) = x^2 - \frac{x^4}{2} + O(x^6)$$
   Very close to $x = 0$, $f(x) \approx x^2$, which clearly decreases for $x < 0$, has a horizontal tangent and minimum $0$ at $x = 0$, and increases for $x > 0$. Differentiating the expansion gives $f'(x) = 2x - 2x^3 + O(x^5)$, matching the Taylor expansion of $\frac{2x}{1+x^2} = 2x(1 - x^2 + x^4 - \dots)$.
2. **Second Derivative Check at $x = 0$:**
   $$f''(x) = \frac{2(x^2+1) - 2x(2x)}{(x^2+1)^2} = \frac{2(1 - x^2)}{(x^2+1)^2} \implies f''(0) = 2 > 0$$
   Since $f'(0) = 0$ and $f''(0) = 2 > 0$, the second derivative test confirms a strict local minimum and upward convexity around $x = 0$.
