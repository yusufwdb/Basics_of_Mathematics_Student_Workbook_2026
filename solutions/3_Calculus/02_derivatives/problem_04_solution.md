# Exercise 4: A Quotient and Domain Control

## 1. Problem Statement
For
$$f(x)=\frac{x^2+1}{x-1}$$
determine the domain, compute the derivative, simplify the result, and explain why the restriction $x\neq1$ remains important.

---

## 2. Theoretical Background and Concepts
- **Domain of a Rational Function:** A rational function $f(x) = \frac{P(x)}{Q(x)}$, where $P$ and $Q$ are polynomials, is defined for all real numbers $x$ where the denominator is non-zero:
  $$D_f = \{x \in \mathbb{R} : Q(x) \neq 0\}$$
- **The Quotient Rule:** If $u(x)$ and $v(x)$ are differentiable at $x$ and $v(x) \neq 0$, then the quotient $f(x) = \frac{u(x)}{v(x)}$ is differentiable at $x$, and its derivative is:
  $$\left(\frac{u}{v}\right)'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2}$$
- **Differentiability Requires Continuity and Definition:** A function $f$ cannot have a derivative at a point $x_0 \notin D_f$ where the function itself is undefined.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Determine the domain of $f$
The denominator of $f(x) = \frac{x^2+1}{x-1}$ vanishes when:
$$x - 1 = 0 \iff x = 1$$
Therefore, the domain of $f$ is:
$$D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)$$

### Step 2: Compute the derivative using the Quotient Rule
Let $u(x) = x^2 + 1$ be the numerator and $v(x) = x - 1$ be the denominator. Their derivatives are:
- $u'(x) = \frac{d}{dx}(x^2 + 1) = 2x$
- $v'(x) = \frac{d}{dx}(x - 1) = 1$

Applying the quotient rule for $x \neq 1$:
$$f'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{[v(x)]^2} = \frac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2}$$

### Step 3: Simplify the result
Expand the numerator and combine like terms:
$$f'(x) = \frac{2x^2 - 2x - x^2 - 1}{(x - 1)^2} = \frac{x^2 - 2x - 1}{(x - 1)^2}$$

### Step 4: Explain why the restriction $x \neq 1$ remains important
The restriction $x \neq 1$ remains essential for three interrelated reasons:
1. **Algebraic validity:** At $x = 1$, the denominator $(x - 1)^2$ in $f'(x)$ equals $0$, while the numerator equals $1^2 - 2(1) - 1 = -2 \neq 0$. Division by zero is undefined.
2. **Geometric / analytical meaning:** $x = 1$ is a vertical asymptote of $f(x)$ (since $\lim_{x \to 1^\pm} \frac{x^2+1}{x-1} = \pm\infty$). A point not in the domain of $f$ cannot have a tangent line or a rate of change.
3. **Splitting intervals of monotonicity:** Because $x = 1$ splits the domain into two separate open intervals $(-\infty, 1)$ and $(1, \infty)$, any subsequent analysis of monotonicity using the sign of $f'(x)$ must treat $(-\infty, 1)$ and $(1, \infty)$ separately rather than merging them across the discontinuity at $x = 1$.

---

## 4. Verification and Consistency Checks

### Verification via Algebraic Decomposition (Polynomial Division)
We can rewrite $f(x)$ by dividing $x^2 + 1$ by $x - 1$:
$$x^2 + 1 = (x^2 - 1) + 2 = (x - 1)(x + 1) + 2$$
For $x \neq 1$, dividing through by $x - 1$ gives:
$$f(x) = x + 1 + \frac{2}{x - 1} = x + 1 + 2(x - 1)^{-1}$$
Differentiating this decomposed form directly using the power/chain rule:
$$f'(x) = 1 + 0 + 2(-1)(x - 1)^{-2} = 1 - \frac{2}{(x - 1)^2}$$
Putting this over the common denominator $(x - 1)^2$:
$$f'(x) = \frac{(x - 1)^2 - 2}{(x - 1)^2} = \frac{x^2 - 2x + 1 - 2}{(x - 1)^2} = \frac{x^2 - 2x - 1}{(x - 1)^2}$$
Both methods produce the exact same derivative formula, confirming the calculation.
