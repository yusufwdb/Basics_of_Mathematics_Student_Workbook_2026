# Exercise 10: The Tangent Line as an Application of the Derivative

## 1. Problem Statement
For
$$f(x)=x^2-3x+1$$
find the equation of the tangent line at the point with $x=2$. Give the point of tangency, the value $f'(2)$, the equation of the line, and verify that the point lies on the obtained tangent line.

---

## 2. Theoretical Background and Concepts
- **Point of Tangency:** For a function $y = f(x)$ and an $x$-coordinate $x_0 \in D_f$, the point of tangency on the graph is $P = (x_0, y_0) = (x_0, f(x_0))$.
- **Equation of the Tangent Line:** If $f$ is differentiable at $x_0$, the tangent line to the graph of $f$ at $(x_0, f(x_0))$ is the unique line passing through $(x_0, f(x_0))$ with slope $m = f'(x_0)$. In point-slope form:
  $$y - f(x_0) = f'(x_0)(x - x_0)$$
  and in slope-intercept form:
  $$y = f'(x_0)(x - x_0) + f(x_0)$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Find the point of tangency
Evaluate $f(x) = x^2 - 3x + 1$ at $x_0 = 2$:
$$y_0 = f(2) = (2)^2 - 3(2) + 1 = 4 - 6 + 1 = -1$$
Thus, the **point of tangency** is:
$$P = (2, -1)$$

### Step 2: Compute the derivative $f'(x)$ and find the slope $f'(2)$
Differentiating $f(x) = x^2 - 3x + 1$ using the power and sum rules:
$$f'(x) = \frac{d}{dx}(x^2) - \frac{d}{dx}(3x) + \frac{d}{dx}(1) = 2x - 3$$
Evaluating the derivative at $x_0 = 2$:
$$m = f'(2) = 2(2) - 3 = 4 - 3 = 1$$

### Step 3: Write the equation of the tangent line
Substituting $x_0 = 2$, $f(2) = -1$, and $f'(2) = 1$ into the tangent line formula $y - f(2) = f'(2)(x - 2)$:
$$y - (-1) = 1(x - 2)$$
$$y + 1 = x - 2$$
Solving for $y$ gives the slope-intercept form of the **tangent line**:
$$y = x - 3$$

### Step 4: Verify that the point of tangency lies on the obtained tangent line
Substituting the coordinates of the point of tangency $P = (2, -1)$ into the tangent line equation $y = x - 3$:
- Left-hand side: $y = -1$
- Right-hand side: $x - 3 = 2 - 3 = -1$

Since $-1 = -1$, the point $(2, -1)$ indeed lies on the line $y = x - 3$.

---

## 4. Verification and Consistency Checks

### Algebraic Double-Root Verification for a Parabola
A non-vertical line $y = mx + b$ is tangent to the parabola $y = f(x)$ at $x = 2$ if and only if the system of equations $f(x) = mx + b$ has a **double root** (multiplicity $2$) at $x = 2$. Let us check the intersection of $f(x) = x^2 - 3x + 1$ and $y = x - 3$:
$$x^2 - 3x + 1 = x - 3 \iff x^2 - 4x + 4 = 0 \iff (x - 2)^2 = 0$$
The quadratic equation factors as a perfect square $(x - 2)^2 = 0$, confirming that $x = 2$ is a root of multiplicity $2$ and that $y = x - 3$ is the exact tangent line to the parabola at $(2, -1)$. Moreover, the difference $f(x) - (x - 3) = (x - 2)^2 \ge 0$ shows that the parabola lies entirely on or above its tangent line, as expected for a convex parabola ($f''(x) = 2 > 0$).
