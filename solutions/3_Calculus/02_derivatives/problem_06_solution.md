# Exercise 6: Product Rule and Trigonometry

## 1. Problem Statement
For
$$f(x)=x\sin x+\cos x$$
compute the derivative and simplify the result. Then compute $f'(0)$ and interpret the direction of the tangent line at that point.

---

## 2. Theoretical Background and Concepts
- **Derivatives of Basic Trigonometric Functions:**
  $$\frac{d}{dx}(\sin x) = \cos x, \qquad \frac{d}{dx}(\cos x) = -\sin x$$
- **Sum Rule and Product Rule:**
  $$(g + h)'(x) = g'(x) + h'(x), \qquad (u \cdot v)'(x) = u'(x)v(x) + u(x)v'(x)$$
- **Horizontal Tangent Line:** When $f'(x_0) = 0$, the tangent line to the graph of $f$ at $(x_0, f(x_0))$ has slope $m = 0$, meaning it is **horizontal** (parallel to the $x$-axis) with equation $y = f(x_0)$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Differentiate the two terms of $f(x)$
By the sum rule:
$$f'(x) = \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x)$$

1. **First term $x\sin x$:** This is a product of $u(x) = x$ and $v(x) = \sin x$, where $u'(x) = 1$ and $v'(x) = \cos x$. Applying the product rule:
   $$\frac{d}{dx}(x\sin x) = (1)(\sin x) + x(\cos x) = \sin x + x\cos x$$
2. **Second term $\cos x$:** Using the standard trigonometric derivative:
   $$\frac{d}{dx}(\cos x) = -\sin x$$

### Step 2: Combine and simplify the derivative
Adding the derivatives of both terms:
$$f'(x) = (\sin x + x\cos x) + (-\sin x)$$
The terms $\sin x$ and $-\sin x$ cancel out completely, leaving the simple expression:
$$f'(x) = x\cos x$$

### Step 3: Compute $f'(0)$ and interpret the tangent line
Evaluating $f'(x) = x\cos x$ at $x = 0$:
$$f'(0) = 0 \cdot \cos(0) = 0 \cdot 1 = 0$$
Also, the function value at $x = 0$ is $f(0) = 0\cdot\sin(0) + \cos(0) = 1$.

**Geometric Interpretation:** Because $f'(0) = 0$, the slope of the tangent line to the graph of $f$ at the point $(0, 1)$ is zero. Therefore, the tangent line at $(0, 1)$ is **horizontal** (parallel to the $x$-axis), given by the equation $y = 1$.

---

## 4. Verification and Consistency Checks

### Parity (Symmetry) and Taylor Series Check near $x = 0$
1. **Even Function Symmetry:** Notice that $f(-x) = (-x)\sin(-x) + \cos(-x) = (-x)(-\sin x) + \cos x = x\sin x + \cos x = f(x)$. Thus $f(x)$ is an **even function** (symmetric across the $y$-axis). Every differentiable even function has an odd derivative ($f'(-x) = -f'(x)$) and therefore must satisfy $f'(0) = 0$. Indeed, $f'(x) = x\cos x$ is the product of an odd function ($x$) and an even function ($\cos x$), so $f'(x)$ is odd and $f'(0) = 0$.
2. **Small-$x$ Taylor Approximation:** For $x \approx 0$, $\sin x = x - \frac{x^3}{6} + O(x^5)$ and $\cos x = 1 - \frac{x^2}{2} + O(x^4)$. Thus:
   $$f(x) = x\left(x - \frac{x^3}{6} + \dots\right) + \left(1 - \frac{x^2}{2} + \dots\right) = 1 + \frac{1}{2}x^2 + O(x^4)$$
   Differentiating this series gives $f'(x) = x + O(x^3)$, which matches $x\cos x = x\left(1 - \frac{x^2}{2} + \dots\right) = x + O(x^3)$ and confirms $f'(0) = 0$ (in fact, $x = 0$ is a local minimum of $f$ near $0$).
