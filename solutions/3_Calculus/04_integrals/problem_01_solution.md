# Exercise 1: Antiderivative and Verification

## 1. Problem Statement

For
$$f(x)=3x^2-4x+5$$
find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

---

## 2. Theoretical Background and Concepts

- **Antiderivative (Primitive Function):** A function $F(x)$ is called an antiderivative of $f(x)$ on an interval $I$ if $F$ is differentiable on $I$ and satisfies
  $$F'(x) = f(x) \quad \text{for all } x \in I.$$
- **Indefinite Integral (Family of Antiderivatives):** By the Mean Value Theorem, if $F(x)$ is one antiderivative of $f(x)$ on an interval $I$, then any other antiderivative of $f(x)$ on $I$ differs from $F(x)$ by a constant $C \in \mathbb{R}$. The set of all antiderivatives is called the indefinite integral and is denoted by
  $$\int f(x)\,dx = F(x) + C, \quad C \in \mathbb{R}.$$
- **Power Rule for Integration:** For any real exponent $n \neq -1$, reversing the power rule for derivatives $\frac{d}{dx}\left(x^{n+1}\right) = (n+1)x^n$ yields
  $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$
- **Linearity of Integration:** For constants $\alpha, \beta \in \mathbb{R}$ and integrable functions $g, h$,
  $$\int \left(\alpha g(x) + \beta h(x)\right)\,dx = \alpha \int g(x)\,dx + \beta \int h(x)\,dx.$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Finding One Specific Antiderivative $F(x)$
We integrate $f(x) = 3x^2 - 4x + 5$ term by term using linearity and the power rule:
1. For the quadratic term $3x^2$: since $\frac{d}{dx}(x^3) = 3x^2$, an antiderivative is $3 \cdot \frac{x^{2+1}}{2+1} = x^3$.
2. For the linear term $-4x$: since $\frac{d}{dx}(x^2) = 2x$, an antiderivative is $-4 \cdot \frac{x^{1+1}}{1+1} = -2x^2$.
3. For the constant term $5$: since $\frac{d}{dx}(x) = 1$, an antiderivative is $5x$.

Combining these terms (and choosing the constant of integration to be $0$), one particular antiderivative is:
$$F_0(x) = x^3 - 2x^2 + 5x.$$

### Step 2: Writing the Entire Family of Antiderivatives
Adding an arbitrary real constant $C \in \mathbb{R}$ gives the complete family of antiderivatives (the indefinite integral):
$$\int (3x^2 - 4x + 5)\,dx = x^3 - 2x^2 + 5x + C, \quad C \in \mathbb{R}.$$

### Step 3: Explaining the Meaning of the Constant $C$
- **Analytical meaning:** Differentiation measures the rate of change of a function, so the derivative of any constant function is zero: $\frac{d}{dx}(C) = 0$. Consequently, knowing only the derivative $f(x) = F'(x)$ determines the function $F(x)$ only up to an additive constant.
- **Geometric meaning:** The family $F(x) = x^3 - 2x^2 + 5x + C$ represents an infinite collection of curves that are **vertical translations** of one another. At any given coordinate $x_0$, every curve in this family has the exact same tangent slope $F'(x_0) = 3x_0^2 - 4x_0 + 5$. To select a single curve from this family, one extra piece of information—an initial condition $F(x_0) = y_0$—is required.

---

## 4. Verification and Consistency Checks

### Differentiation Check
We differentiate the general family $F(x) = x^3 - 2x^2 + 5x + C$ with respect to $x$:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left(x^3 - 2x^2 + 5x + C\right) \\
&= \frac{d}{dx}(x^3) - 2\frac{d}{dx}(x^2) + 5\frac{d}{dx}(x) + \frac{d}{dx}(C) \\
&= 3x^2 - 2(2x) + 5(1) + 0 \\
&= 3x^2 - 4x + 5 = f(x).
\end{aligned}$$
Since $F'(x) = f(x)$ for all $x \in \mathbb{R}$, our antiderivative is verified.
