# Exercise 12: Several Rules at Once

## 1. Problem Statement
For
$$f(x)=(x^2+1)^3e^x$$
compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

---

## 2. Theoretical Background and Concepts
- **Structural Hierarchy of Differentiation ("Outside-In" Strategy):** When an expression combines products, quotients, and compositions, the rule that governs the outermost operation of the entire formula must be applied first.
  - Here, the top-level operation in $f(x) = (x^2+1)^3 \cdot e^x$ is **multiplication** of two factors: $u(x) = (x^2+1)^3$ and $v(x) = e^x$. Thus, the **Product Rule** $(uv)' = u'v + uv'$ governs the whole expression.
  - Inside the first factor $u(x) = (x^2+1)^3$, the operation is a **composition** of $w^3$ with $w(x) = x^2 + 1$. Thus, the **Chain Rule** is used to compute $u'(x)$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Differentiation Plan
1. **Top-level rule (whole expression):** Treat $f(x)$ as a product $f(x) = u(x)v(x)$, where $u(x) = (x^2+1)^3$ and $v(x) = e^x$, and apply the **Product Rule**:
   $$f'(x) = u'(x)v(x) + u(x)v'(x)$$
2. **Sub-level rule (first factor):** Compute $u'(x) = \frac{d}{dx}\big((x^2+1)^3\big)$ using the **Chain Rule** with outer function $g(w) = w^3$ and inner polynomial $w(x) = x^2 + 1$.
3. **Sub-level rule (second factor):** Compute $v'(x) = \frac{d}{dx}(e^x) = e^x$ using the standard exponential rule.
4. **Algebraic simplification:** Factor out the highest common power of $(x^2+1)$ and $e^x$.

### Step 2: Compute the derivatives of the individual factors
- For $u(x) = (x^2 + 1)^3$, applying the chain rule:
  $$u'(x) = 3(x^2 + 1)^2 \cdot \frac{d}{dx}(x^2 + 1) = 3(x^2 + 1)^2 \cdot (2x) = 6x(x^2 + 1)^2$$
- For $v(x) = e^x$:
  $$v'(x) = e^x$$

### Step 3: Combine using the Product Rule
Substituting $u, u', v, v'$ into $f'(x) = u'(x)v(x) + u(x)v'(x)$:
$$f'(x) = 6x(x^2 + 1)^2 e^x + (x^2 + 1)^3 e^x$$

### Step 4: Organize the result by factoring out common factors
Both terms contain the common factors $(x^2 + 1)^2$ and $e^x$. Factoring out $(x^2 + 1)^2 e^x$ gives:
$$f'(x) = (x^2 + 1)^2 e^x \big[6x + (x^2 + 1)\big]$$
Arranging the polynomial inside the brackets in standard descending order of powers:
$$f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x$$

---

## 4. Verification and Consistency Checks

### Verification via Logarithmic Differentiation
Since $f(x) = (x^2 + 1)^3 e^x > 0$ for all $x \in \mathbb{R}$, we can take the natural logarithm of both sides:
$$\ln f(x) = \ln\big((x^2 + 1)^3 e^x\big) = 3\ln(x^2 + 1) + x$$
Differentiating both sides with respect to $x$:
$$\frac{f'(x)}{f(x)} = 3 \cdot \frac{2x}{x^2 + 1} + 1 = \frac{6x + x^2 + 1}{x^2 + 1} = \frac{x^2 + 6x + 1}{x^2 + 1}$$
Multiplying both sides by $f(x) = (x^2 + 1)^3 e^x$:
$$f'(x) = (x^2 + 1)^3 e^x \cdot \frac{x^2 + 6x + 1}{x^2 + 1} = (x^2 + 1)^2 (x^2 + 6x + 1) e^x$$
This independent method confirms our factored derivative formula.
