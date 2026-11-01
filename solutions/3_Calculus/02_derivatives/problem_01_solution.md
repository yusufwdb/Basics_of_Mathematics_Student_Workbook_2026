# Exercise 1: Derivative of a Polynomial and the Slope of a Tangent Line

## 1. Problem Statement
For
$$f(x)=3x^5-2x^3+7x-4$$
find $f'(x)$. Then compute $f'(0)$ and $f'(1)$, determine the signs of the obtained values, and explain what they say about the slope of the tangent line to the graph at these two points.

---

## 2. Theoretical Background and Concepts
- **Derivative as the Slope of the Tangent Line:** For a differentiable function $y = f(x)$, the value of the derivative $f'(x_0)$ at a point $x_0$ represents the instantaneous rate of change of $f$ with respect to $x$ and equals the slope $m$ of the tangent line to the graph of $f$ at $(x_0, f(x_0))$.
  - If $f'(x_0) > 0$, the tangent line slopes upward from left to right, and the function is locally increasing near $x_0$.
  - If $f'(x_0) < 0$, the tangent line slopes downward from left to right, and the function is locally decreasing near $x_0$.
  - If $f'(x_0) = 0$, the tangent line is horizontal.
- **Basic Differentiation Rules for Polynomials:**
  - **Power Rule:** $\frac{d}{dx}(x^n) = nx^{n-1}$ for any constant exponent $n$.
  - **Constant Multiple Rule:** $\frac{d}{dx}[c \cdot g(x)] = c \cdot g'(x)$ for any constant $c \in \mathbb{R}$.
  - **Sum and Difference Rule:** $\frac{d}{dx}[g(x) \pm h(x)] = g'(x) \pm h'(x)$.
  - **Derivative of a Constant:** $\frac{d}{dx}(c) = 0$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the derivative $f'(x)$
We differentiate $f(x) = 3x^5 - 2x^3 + 7x - 4$ term by term using the linearity of differentiation (sum/difference and constant multiple rules) together with the power rule:
$$f'(x) = \frac{d}{dx}(3x^5) - \frac{d}{dx}(2x^3) + \frac{d}{dx}(7x) - \frac{d}{dx}(4)$$

Applying the power rule to each term:
- $\frac{d}{dx}(3x^5) = 3 \cdot (5x^{5-1}) = 15x^4$
- $\frac{d}{dx}(2x^3) = 2 \cdot (3x^{3-1}) = 6x^2$
- $\frac{d}{dx}(7x) = 7 \cdot (1x^{1-1}) = 7$
- $\frac{d}{dx}(4) = 0$

Combining these results gives:
$$f'(x) = 15x^4 - 6x^2 + 7$$

### Step 2: Evaluate $f'(0)$ and $f'(1)$
Substitute $x = 0$ into $f'(x)$:
$$f'(0) = 15(0)^4 - 6(0)^2 + 7 = 0 - 0 + 7 = 7$$

Substitute $x = 1$ into $f'(x)$:
$$f'(1) = 15(1)^4 - 6(1)^2 + 7 = 15 - 6 + 7 = 16$$

### Step 3: Determine the signs and interpret the slopes of the tangent lines
- **At $x = 0$:** We have $f'(0) = 7 > 0$. Because the derivative is positive, the tangent line to the graph of $f$ at the point $(0, f(0)) = (0, -4)$ has a positive slope of $m = 7$. Geometrically, the tangent line rises steeply from left to right (rising $7$ units vertically for each $1$ unit of horizontal run), indicating that $f(x)$ is strictly increasing as it passes through $x = 0$.
- **At $x = 1$:** We have $f'(1) = 16 > 0$. The derivative is again positive and even larger in magnitude. The tangent line at $(1, f(1)) = (1, 4)$ has a positive slope of $m = 16$, meaning the graph is rising even more steeply at $x = 1$ than at $x = 0$.

---

## 4. Verification and Consistency Checks

### Global Sign Analysis of $f'(x)$
We can complete the square on the quadratic in $u = x^2$ for $f'(x) = 15x^4 - 6x^2 + 7$:
$$f'(x) = 15\left(x^4 - \frac{2}{5}x^2\right) + 7 = 15\left(x^2 - \frac{1}{5}\right)^2 - \frac{3}{5} + 7 = 15\left(x^2 - \frac{1}{5}\right)^2 + \frac{32}{5}$$
Since $15\left(x^2 - \frac{1}{5}\right)^2 \ge 0$ for all $x \in \mathbb{R}$, we see that $f'(x) \ge \frac{32}{5} = 6.4 > 0$ everywhere. Both $f'(0) = 7$ and $f'(1) = 16$ are strictly greater than $6.4$, confirming our values are consistent with the global behavior of the polynomial.

### Difference Quotient Check at $x = 0$ and $x = 1$
For a tiny step $h = 0.001$:
- Near $x = 0$:
  $$\frac{f(0.001) - f(0)}{0.001} = \frac{3(0.001)^5 - 2(0.001)^3 + 7(0.001) - 4 - (-4)}{0.001} \approx 7 - 2(10^{-6}) \approx 7 = f'(0)$$
- Near $x = 1$:
  $$f(1) = 3 - 2 + 7 - 4 = 4$$
  $$f(1.001) = 3(1.001)^5 - 2(1.001)^3 + 7(1.001) - 4 \approx 3(1.00501001) - 2(1.003003) + 7.007 - 4 = 4.016024$$
  $$\frac{f(1.001) - f(1)}{0.001} \approx \frac{0.016024}{0.001} = 16.024 \approx 16 = f'(1)$$
Both checks confirm our exact derivative evaluations.
