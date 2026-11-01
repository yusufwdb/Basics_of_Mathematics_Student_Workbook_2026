# Exercise 5: The Chain Rule as Working Through Layers

## 1. Problem Statement
For
$$f(x)=(3x^2-2x+1)^5$$
identify the inner and outer functions, compute their derivatives, and combine the result according to the chain rule. Explain the origin of the additional factor.

---

## 2. Theoretical Background and Concepts
- **Composite Function:** A function formed by applying one function to the output of another: $f(x) = (g \circ u)(x) = g(u(x))$, where $u(x)$ is the **inner function** and $g(u)$ is the **outer function**.
- **The Chain Rule:** If $u = u(x)$ is differentiable at $x$ and $g = g(u)$ is differentiable at $u(x)$, then the composite function $f(x) = g(u(x))$ is differentiable at $x$, and:
  $$f'(x) = g'(u(x)) \cdot u'(x) \qquad \text{or in Leibniz notation:} \qquad \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$
- **Origin of the Additional Factor $u'(x)$:** The outer derivative $\frac{dy}{du} = g'(u)$ measures how fast the output $y$ changes *with respect to the intermediate variable $u$*. However, we want the rate of change of $y$ *with respect to $x$*. Since a small change $\Delta x$ causes $u$ to change by approximately $\Delta u \approx u'(x)\Delta x$, and that change in $u$ causes $y$ to change by $\Delta y \approx g'(u)\Delta u \approx g'(u)u'(x)\Delta x$, the rates of change multiply.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the inner and outer functions
In the expression $f(x) = (3x^2 - 2x + 1)^5$:
1. First, $x$ is mapped to the quadratic polynomial $u = 3x^2 - 2x + 1$. This is the **inner function**:
   $$u(x) = 3x^2 - 2x + 1$$
2. Second, the result $u$ is raised to the $5\text{th}$ power. This is the **outer function**:
   $$g(u) = u^5$$

### Step 2: Compute the derivatives of both layers
- **Derivative of the outer function** with respect to $u$:
  $$g'(u) = \frac{d}{du}(u^5) = 5u^4$$
  Substituting $u = 3x^2 - 2x + 1$ back in gives:
  $$g'(u(x)) = 5(3x^2 - 2x + 1)^4$$
- **Derivative of the inner function** with respect to $x$:
  $$u'(x) = \frac{d}{dx}(3x^2 - 2x + 1) = 3(2x) - 2(1) + 0 = 6x - 2$$

### Step 3: Combine the results using the Chain Rule
Multiplying the derivative of the outer function evaluated at the inner function by the derivative of the inner function:
$$f'(x) = g'(u(x)) \cdot u'(x) = 5(3x^2 - 2x + 1)^4 \cdot (6x - 2)$$

We can also factor $2$ out of $(6x - 2) = 2(3x - 1)$ to write:
$$f'(x) = 10(3x - 1)(3x^2 - 2x + 1)^4$$

### Step 4: Explain the origin of the additional factor $(6x - 2)$
If we only wrote $5(3x^2 - 2x + 1)^4$, we would only have calculated the rate of change of $f$ with respect to the *block* $u = 3x^2 - 2x + 1$. Because the block $u(x)$ itself changes at a rate of $u'(x) = 6x - 2$ units per unit change in $x$, the sensitivity of $f$ to changes in $x$ is scaled by $6x - 2$. For instance, at $x = \frac{1}{3}$, the inner quadratic has a horizontal tangent ($u'(1/3) = 0$), so $u$ is momentarily stationary as $x$ varies; consequently, $f(x) = u(x)^5$ must also be momentarily stationary ($f'(1/3) = 0$), which is captured precisely by the factor $6x - 2$.

---

## 4. Verification and Consistency Checks

### Verification via Leading and Low-Order Terms of Binomial Expansion
1. **Leading Term Check:** For large $|x|$, $f(x) = (3x^2 - 2x + 1)^5 = (3x^2)^5 + \dots = 243x^{10} + O(x^9)$.
   Differentiating the leading term gives $\frac{d}{dx}(243x^{10}) = 2430x^9$.
   From our chain rule formula, the leading term of $f'(x) = 5(3x^2 - \dots)^4(6x - 2)$ is $5(3x^2)^4(6x) = 5(81x^8)(6x) = 2430x^9$. They match!
2. **Constant and Linear Term Check at $x = 0$:**
   Let $u = 1 + (-2x + 3x^2)$. By the binomial expansion $(1 + \delta)^5 = 1 + 5\delta + O(\delta^2)$ as $x \to 0$:
   $$f(x) = 1 + 5(-2x + 3x^2) + O(x^2) = 1 - 10x + O(x^2)$$
   Thus $f'(0)$ must equal the coefficient of $x$, which is $-10$.
   Evaluating our formula at $x = 0$:
   $$f'(0) = 5(3(0)^2 - 2(0) + 1)^4 (6(0) - 2) = 5(1)^4(-2) = -10$$
   Both the high-degree and low-degree behaviors agree completely.
