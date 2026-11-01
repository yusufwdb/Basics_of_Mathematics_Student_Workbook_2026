# Exercise 2: Powers, Roots, and the Domain

## 1. Problem Statement
For
$$f(x)=2\sqrt{x}-\frac{3}{x^2}+x^{3/2}$$
1. rewrite the function using powers,
2. determine the domain,
3. compute the derivative,
4. compare the domain of the function with the domain of its derivative.

---

## 2. Theoretical Background and Concepts
- **Algebraic Laws of Exponents and Radicals:**
  - Fractional exponents represent roots: $\sqrt[n]{x^m} = x^{m/n}$ (specifically, $\sqrt{x} = x^{1/2}$).
  - Negative exponents represent reciprocals: $\frac{1}{x^n} = x^{-n}$ for $x \neq 0$.
- **Domain of a Function:** The maximal subset of $\mathbb{R}$ for which all operations in the formula $f(x)$ yield well-defined real numbers. Even-indexed roots require non-negative arguments ($\ge 0$), and denominators cannot equal zero ($\neq 0$).
- **General Power Rule:** For any real exponent $\alpha \in \mathbb{R}$,
  $$\frac{d}{dx}\left(x^\alpha\right) = \alpha x^{\alpha - 1}$$
  where $x$ belongs to the open interval on which $x^\alpha$ and $x^{\alpha-1}$ are defined and differentiable.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Rewrite the function using powers
Converting the square root $\sqrt{x} = x^{1/2}$ and the reciprocal $\frac{1}{x^2} = x^{-2}$ into power form $x^\alpha$:
$$f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}$$

### Step 2: Determine the domain of $f$
We inspect each term of $f(x)$ for domain restrictions over the real numbers:
1. The term $2\sqrt{x} = 2x^{1/2}$ requires the radicand to be non-negative: $x \ge 0$.
2. The term $-\frac{3}{x^2} = -3x^{-2}$ has $x^2$ in the denominator, which requires $x^2 \neq 0 \implies x \neq 0$.
3. The term $x^{3/2} = (\sqrt{x})^3$ requires $x \ge 0$.

Taking the intersection of all three conditions ($x \ge 0$ and $x \neq 0$):
$$D_f = (0, \infty)$$

### Step 3: Compute the derivative $f'(x)$
Using the power representation $f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}$, we differentiate term by term via the power rule:
$$f'(x) = 2 \cdot \frac{d}{dx}\left(x^{1/2}\right) - 3 \cdot \frac{d}{dx}\left(x^{-2}\right) + \frac{d}{dx}\left(x^{3/2}\right)$$

Calculating each derivative:
- $2 \cdot \left(\frac{1}{2}x^{\frac{1}{2}-1}\right) = x^{-1/2} = \frac{1}{\sqrt{x}}$
- $-3 \cdot \left(-2x^{-2-1}\right) = 6x^{-3} = \frac{6}{x^3}$
- $\frac{3}{2}x^{\frac{3}{2}-1} = \frac{3}{2}x^{1/2} = \frac{3}{2}\sqrt{x}$

Thus, in power form:
$$f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2}$$
And in radical/fraction form:
$$f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$$

### Step 4: Compare the domain of $f$ with the domain of $f'$
Let us find the domain $D_{f'}$ of $f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3}{2}\sqrt{x}$:
- $\frac{1}{\sqrt{x}}$ requires $x > 0$ (since $\sqrt{x}$ is in the denominator).
- $\frac{6}{x^3}$ requires $x \neq 0$.
- $\frac{3}{2}\sqrt{x}$ requires $x \ge 0$.

Intersecting these requirements gives:
$$D_{f'} = (0, \infty)$$

**Comparison:** In this problem, $D_f = D_{f'} = (0, \infty)$, so the domain of the function and the domain of its derivative are **identical**. Note that although differentiating $\sqrt{x}$ moves the root into the denominator ($\frac{1}{2\sqrt{x}}$), which normally excludes $x = 0$ from the domain upon differentiation, $x = 0$ was *already* excluded from $D_f$ because of the $-\frac{3}{x^2}$ term!

---

## 4. Verification and Consistency Checks

### Numerical Check at $x = 1$ and $x = 4$
At $x = 1$:
- $f(1) = 2(1) - 3(1) + 1 = 0$
- From our formula, $f'(1) = 1 + 6 + \frac{3}{2} = 8.5$.
- Using a central difference quotient with $h = 0.001$:
  $$\frac{f(1.001) - f(0.999)}{0.002} = \frac{\left(2\sqrt{1.001} - 3(1.001)^{-2} + 1.001^{1.5}\right) - \left(2\sqrt{0.999} - 3(0.999)^{-2} + 0.999^{1.5}\right)}{0.002} \approx \frac{0.008509 - (-0.008491)}{0.002} = 8.500006 \approx 8.5$$

At $x = 4$:
- $f'(4) = \frac{1}{\sqrt{4}} + \frac{6}{4^3} + \frac{3}{2}\sqrt{4} = \frac{1}{2} + \frac{6}{64} + 3 = 3.5 + 0.09375 = 3.59375 = \frac{115}{32}$.
- Checking each term's exponent decrease: $\frac{1}{2} \to -\frac{1}{2}$, $-2 \to -3$, and $\frac{3}{2} \to \frac{1}{2}$. Every exponent decreased by exactly $1$, confirming the power rule was applied accurately.
