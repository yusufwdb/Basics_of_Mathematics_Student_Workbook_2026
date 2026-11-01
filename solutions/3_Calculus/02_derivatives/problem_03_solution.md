# Exercise 3: The Product Rule — Why Is It Needed?

## 1. Problem Statement
For
$$f(x)=(x^2+1)e^x$$
compute the derivative. Then compare the correct result with the incorrect idea
$$f'(x)\stackrel{?}{=}(2x)e^x$$
and explain which term is missing.

---

## 2. Theoretical Background and Concepts
- **The Product Rule (Leibniz Rule):** If $u(x)$ and $v(x)$ are differentiable functions, then their product $f(x) = u(x)v(x)$ is also differentiable, and its derivative is given by:
  $$(u \cdot v)'(x) = u'(x)v(x) + u(x)v'(x)$$
- **Derivative of the Natural Exponential Function:** The function $e^x$ is its own derivative:
  $$\frac{d}{dx}(e^x) = e^x$$
- **Conceptual Origin of the Product Rule:** When $x$ changes by a small increment $\Delta x$, *both* factors $u(x)$ and $v(x)$ change simultaneously:
  $$\Delta(uv) = (u + \Delta u)(v + \Delta v) - uv = \Delta u \cdot v + u \cdot \Delta v + \Delta u \cdot \Delta v$$
  Dividing by $\Delta x$ and taking the limit as $\Delta x \to 0$ yields $u'v + uv'$. Think of $u(x)v(x)$ as the area of a rectangle with sides $u$ and $v$: as both sides grow, the area increases along *both* edges.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the factors and their derivatives
The function $f(x) = (x^2+1)e^x$ is the product of two differentiable functions of $x$:
- First factor: $u(x) = x^2 + 1 \implies u'(x) = \frac{d}{dx}(x^2 + 1) = 2x$
- Second factor: $v(x) = e^x \implies v'(x) = \frac{d}{dx}(e^x) = e^x$

### Step 2: Apply the Product Rule
Substituting $u, u', v, v'$ into the product rule formula $f'(x) = u'(x)v(x) + u(x)v'(x)$:
$$f'(x) = (2x)e^x + (x^2 + 1)e^x$$

Factoring out the common factor $e^x$ gives a clean, simplified expression:
$$f'(x) = (x^2 + 2x + 1)e^x = (x + 1)^2 e^x$$

### Step 3: Compare with the incorrect formula and explain the missing term
The proposed incorrect formula is:
$$f_{\text{wrong}}'(x) = 2xe^x$$
Comparing this with the true derivative:
$$f'(x) = 2xe^x + (x^2 + 1)e^x$$
we see that **the missing term is $(x^2 + 1)e^x$**, which is $u(x)v'(x) = (x^2 + 1)\frac{d}{dx}(e^x)$.

**Why is it wrong to write $(2x)e^x$?**
1. Even if a student falsely believed that $(u \cdot v)' = u' \cdot v'$, since $(e^x)' = e^x$, both the mistaken rule $(u \cdot v)' = u' \cdot v'$ and treating $e^x$ as a constant multiplier produce the same erroneous expression $2xe^x$.
2. Neither is valid: $e^x$ is not a constant (it varies with $x$), and differentiation is not multiplicative. The formula $2xe^x$ accounts only for the rate of change of the polynomial factor $x^2+1$ while holding $e^x$ fixed, completely ignoring the contribution $(x^2+1)e^x$ that arises from the exponential growth of $e^x$ multiplied by the current value of $x^2+1$.

---

## 4. Verification and Consistency Checks

### Evaluation Check at $x = 0$
Let us evaluate $f'(0)$ using the limit definition of the derivative directly and compare it with both formulas:
$$f'(0) = \lim_{h \to 0} \frac{f(h) - f(0)}{h} = \lim_{h \to 0} \frac{(h^2 + 1)e^h - (0^2 + 1)e^0}{h} = \lim_{h \to 0} \frac{h^2 e^h + e^h - 1}{h}$$
Splitting the limit:
$$f'(0) = \lim_{h \to 0} (h e^h) + \lim_{h \to 0} \frac{e^h - 1}{h} = 0 \cdot 1 + 1 = 1$$

Now compare at $x = 0$:
- **Correct derivative:** $f'(0) = (0 + 1)^2 e^0 = 1 \cdot 1 = 1$ (Matches the definition!).
- **Incorrect formula:** $f_{\text{wrong}}'(0) = 2(0)e^0 = 0 \neq 1$ (Fails completely at $x=0$ because at $x=0$ the entire rate of change of $f(x)$ comes from the missing term $(x^2+1)e^x$!).
