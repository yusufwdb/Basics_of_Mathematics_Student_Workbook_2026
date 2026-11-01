# Exercise 2: A Parabola from the Perspective of the Derivative

## 1. Problem Statement
For $f(x)=x^2-4x+1$, find the minimum using the derivative. Compare the result with the vertex form and explain why both approaches lead to the same point.

---

## 2. Theoretical Background and Concepts
- **Calculus Approach to Extrema:** For a differentiable function $f(x)$, any local extremum occurs at a stationary point where $f'(x) = 0$. If $f'(x) < 0$ for $x < x_0$ and $f'(x) > 0$ for $x > x_0$, then $x_0$ is the unique global minimum of $f$.
- **Algebraic Vertex Form of a Quadratic Function:** Every quadratic function $f(x) = ax^2 + bx + c$ ($a \neq 0$) can be rewritten by completing the square as:
  $$f(x) = a(x - p)^2 + q, \qquad \text{where } p = -\frac{b}{2a}, \quad q = f(p)$$
  When $a > 0$, $(x - p)^2 \ge 0$ for all $x \in \mathbb{R}$, with equality if and only if $x = p$, so $q$ is the global minimum attained at the vertex $(p, q)$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Find the minimum using the derivative
The function $f(x) = x^2 - 4x + 1$ is defined and differentiable for all $x \in \mathbb{R}$.
1. **Compute the derivative:**
   $$f'(x) = \frac{d}{dx}(x^2 - 4x + 1) = 2x - 4$$
2. **Find the critical point:**
   $$f'(x) = 0 \iff 2x - 4 = 0 \iff x = 2$$
3. **Analyze the sign of $f'(x)$:**
   - For $x < 2$: $f'(x) = 2(x - 2) < 0$, so $f$ is strictly decreasing on $(-\infty, 2]$.
   - For $x > 2$: $f'(x) = 2(x - 2) > 0$, so $f$ is strictly increasing on $[2, \infty)$.
4. **Compute the minimum value:**
   Since $f$ decreases up to $x = 2$ and increases thereafter, $f$ attains its **global minimum** at $x = 2$:
   $$f(2) = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3$$
   Thus, the minimum point is **$(2, -3)$**.

### Step 2: Find the minimum using the vertex form (completing the square)
We complete the square in $f(x) = x^2 - 4x + 1$ by adding and subtracting $\left(\frac{-4}{2}\right)^2 = 4$:
$$f(x) = (x^2 - 4x + 4) - 4 + 1 = (x - 2)^2 - 3$$
Since $(x - 2)^2 \ge 0$ for every real number $x$, we have:
$$f(x) = (x - 2)^2 - 3 \ge -3$$
with equality $(x - 2)^2 = 0 \iff x = 2$. Thus, the vertex of the parabola is **$(2, -3)$**, giving the exact same minimum value $-3$ at $x = 2$.

### Step 3: Explain why both approaches lead to the same point
Differentiating the general vertex form $f(x) = a(x - p)^2 + q$ directly via the chain rule yields:
$$f'(x) = \frac{d}{dx}\big[a(x - p)^2 + q\big] = 2a(x - p)$$
Setting $f'(x) = 0$ gives $2a(x - p) = 0 \iff x = p$.
- **Algebraically:** The squared term $(x - p)^2$ has a double root at $x = p$, so its derivative $2(x - p)$ vanishes at $x = p$ and changes sign across $x = p$.
- **Geometrically:** A parabola is symmetric about the vertical axis $x = p$ passing through its vertex $(p, q)$. At the bottom of the valley (the vertex), the curve turns from decreasing to increasing, so the tangent line at the vertex must be horizontal ($f'(p) = 0$).

---

## 4. Verification and Consistency Checks

### Symmetry Check Around $x = 2$
Using $x = 2 + h$ in the original formula $f(x) = x^2 - 4x + 1$:
$$f(2 + h) = (2 + h)^2 - 4(2 + h) + 1 = (4 + 4h + h^2) - (8 + 4h) + 1 = -3 + h^2$$
- The linear term in $h$ ($4h - 4h = 0$) vanishes completely! Since the coefficient of the linear perturbation $h$ in the Taylor expansion $f(x_0 + h) = f(x_0) + f'(x_0)h + \frac{1}{2}f''(x_0)h^2$ is $f'(x_0)$, the vanishing of the $h$-term is simultaneously why $f'(2) = 0$ (calculus) and why $f(2+h) = -3 + h^2$ is a pure shifted square (vertex form).
