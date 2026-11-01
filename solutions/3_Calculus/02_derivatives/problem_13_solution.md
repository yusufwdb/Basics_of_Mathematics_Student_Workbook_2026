# Exercise 13: A Multi-Layer Composition

## 1. Problem Statement
For
$$f(x)=e^{\sin(x^2)}$$
compute the derivative. First write the layers
$$x\longrightarrow x^2\longrightarrow \sin(x^2)\longrightarrow e^{\sin(x^2)}$$
and explain why differentiation moves through them in the reverse order.

---

## 2. Theoretical Background and Concepts
- **Multi-Layer Chain Rule:** If $y = f(x) = h(g(u(x)))$ is a composition of three differentiable functions, where:
  $$u = u(x), \qquad v = g(u), \qquad y = h(v)$$
  then $f$ is differentiable and its derivative is the product of the derivatives of all three layers:
  $$f'(x) = \frac{dy}{dx} = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx} = h'(g(u(x))) \cdot g'(u(x)) \cdot u'(x)$$
- **Why Evaluation and Differentiation Move in Opposite Orders:**
  - When **evaluating** $f(x)$ at a number $x$, we work **from the inside out**: we must first compute $u = x^2$, then feed $u$ into $\sin(u)$ to get $v = \sin(x^2)$, and finally compute $e^v$.
  - When **differentiating** $f(x) = h(g(u(x)))$, we work **from the outside in** ("peeling the onion"): at the outermost level, $f$ is an exponential function $e^v$ whose argument happens to be $v = \sin(x^2)$. To find how $e^v$ responds to changes in $x$, we first differentiate the outer operation $e^v$ with respect to its immediate input $v$, and then multiply by $\frac{dv}{dx}$—which itself requires differentiating the middle operation $\sin(u)$ with respect to $u$ and finally multiplying by $\frac{du}{dx}$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Write down the chain of layers
When we evaluate $f(x)$ starting from the input $x$, the sequence of operations is:
$$x \xrightarrow{\;u(x) = x^2\;} u = x^2 \xrightarrow{\;v(u) = \sin u\;} v = \sin(x^2) \xrightarrow{\;y(v) = e^v\;} y = e^{\sin(x^2)}$$

Specifically:
1. **Innermost layer (Layer 1):** $u(x) = x^2$
2. **Middle layer (Layer 2):** $v(u) = \sin u$
3. **Outermost layer (Layer 3):** $y(v) = e^v$

### Step 2: Differentiate through the layers in reverse order (outside-in)
Working from the outermost layer inward:
1. **Differentiate the outermost layer $y(v) = e^v$ with respect to $v = \sin(x^2)$:**
   $$\frac{dy}{dv} = e^v = e^{\sin(x^2)}$$
   This leaves us needing to multiply by $\frac{d}{dx}\big(\sin(x^2)\big)$.
2. **Differentiate the middle layer $v(u) = \sin u$ with respect to $u = x^2$:**
   $$\frac{dv}{du} = \cos u = \cos(x^2)$$
   This leaves us needing to multiply by $\frac{d}{dx}(x^2)$.
3. **Differentiate the innermost layer $u(x) = x^2$ with respect to $x$:**
   $$\frac{du}{dx} = 2x$$

### Step 3: Multiply the derivatives of all layers together
Combining the three factors via the chain rule:
$$f'(x) = \frac{dy}{dv} \cdot \frac{dv}{du} \cdot \frac{du}{dx} = e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x$$
Writing the factors in standard order:
$$f'(x) = 2x\cos(x^2)e^{\sin(x^2)}$$

---

## 4. Verification and Consistency Checks

### Verification via Logarithmic Differentiation and Taylor Series
1. **Logarithmic Differentiation:** Since $f(x) = e^{\sin(x^2)} > 0$ for all $x \in \mathbb{R}$, taking the natural logarithm yields:
   $$\ln f(x) = \sin(x^2)$$
   Differentiating both sides with respect to $x$ reduces the right-hand side to a two-layer chain rule problem:
   $$\frac{f'(x)}{f(x)} = \cos(x^2) \cdot 2x \implies f'(x) = 2x\cos(x^2)f(x) = 2x\cos(x^2)e^{\sin(x^2)}$$
2. **Maclaurin Expansion Check near $x = 0$:**
   For small $x$, $\sin(x^2) = x^2 - \frac{x^6}{6} + O(x^{10})$, so:
   $$f(x) = e^{x^2 + O(x^6)} = 1 + x^2 + \frac{x^4}{2} + O(x^6)$$
   Differentiating term-by-term gives $f'(x) = 2x + 2x^3 + O(x^5)$.
   Expanding our derivative formula for small $x$:
   $$2x\cos(x^2)e^{\sin(x^2)} = 2x\big(1 - O(x^4)\big)\big(1 + x^2 + O(x^4)\big) = 2x + 2x^3 + O(x^5)$$
   The expansions match up to order $x^5$.
