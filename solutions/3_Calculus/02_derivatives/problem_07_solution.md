# Exercise 7: A Trigonometric Composition

## 1. Problem Statement
For
$$f(x)=\sin(x^2+1)$$
compute the derivative. Explicitly identify the outer function, the inner function, and the derivative of the inner function. Finally, determine the sign of $f'(0)$.

---

## 2. Theoretical Background and Concepts
- **Chain Rule for Trigonometric Compositions:** When a trigonometric function is applied to an inner expression $u(x)$, i.e., $f(x) = \sin(u(x))$, the chain rule states:
  $$f'(x) = \frac{d}{du}(\sin u)\Big|_{u=u(x)} \cdot u'(x) = \cos(u(x)) \cdot u'(x)$$
- **Sign Classification of Real Numbers:** Every real number is either positive ($> 0$), negative ($< 0$), or zero ($= 0$, which is neither positive nor negative).

---

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the components of the composition
Writing $f(x) = \sin(x^2 + 1)$ as $f(x) = g(u(x))$:
- **Inner function:** $u(x) = x^2 + 1$
- **Outer function:** $g(u) = \sin u$

### Step 2: Compute the derivatives of the outer and inner functions
- **Derivative of the outer function** with respect to $u$:
  $$g'(u) = \frac{d}{du}(\sin u) = \cos u \implies g'(u(x)) = \cos(x^2 + 1)$$
- **Derivative of the inner function** with respect to $x$:
  $$u'(x) = \frac{d}{dx}(x^2 + 1) = 2x$$

### Step 3: Apply the Chain Rule
Multiplying the outer derivative evaluated at $u(x)$ by the inner derivative $u'(x)$:
$$f'(x) = \cos(x^2 + 1) \cdot 2x = 2x\cos(x^2 + 1)$$

### Step 4: Determine $f'(0)$ and its sign
Substitute $x = 0$ into $f'(x)$:
$$f'(0) = 2(0)\cos(0^2 + 1) = 0 \cdot \cos(1) = 0$$
- **Sign of $f'(0)$:** Since $f'(0) = 0$, the value is **zero** (neither positive nor negative). Geometrically, the graph of $f(x) = \sin(x^2+1)$ has a horizontal tangent line at $x = 0$.
- Moreover, for small $x \neq 0$, since $1\text{ radian} \approx 57.3^\circ \in \left(0, \frac{\pi}{2}\right)$, we have $\cos(x^2+1) \approx \cos(1) > 0$, so $f'(x) = 2x\cos(x^2+1)$ is negative for small $x < 0$ and positive for small $x > 0$ (meaning $x = 0$ is a local minimum).

---

## 4. Verification and Consistency Checks

### Symmetry and Difference Quotient Verification
1. **Even Symmetry Check:** Because $f(-x) = \sin((-x)^2 + 1) = \sin(x^2 + 1) = f(x)$, the function $f$ is an even function on $\mathbb{R}$. Its derivative $f'(x) = 2x\cos(x^2 + 1)$ is an odd function ($f'(-x) = -f'(x)$), which necessarily vanishes at the origin: $f'(0) = 0$.
2. **Difference Quotient Check near $x = 1$:**
   At $x = 1$, our formula predicts:
   $$f'(1) = 2(1)\cos(1^2 + 1) = 2\cos(2) \approx 2(-0.4161468) \approx -0.8322937$$
   Using a central difference quotient with $h = 0.001$:
   $$\frac{f(1.001) - f(0.999)}{0.002} = \frac{\sin(1.001^2 + 1) - \sin(0.999^2 + 1)}{0.002} = \frac{\sin(2.002001) - \sin(1.998001)}{0.002} \approx \frac{0.9084644 - 0.9101290}{0.002} \approx -0.83229$$
   This matches $2\cos(2)$ to five decimal places.
