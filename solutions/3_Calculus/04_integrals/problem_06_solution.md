# Exercise 6: When Does a Logarithm Appear from an Integral?

## 1. Problem Statement

Compute
$$\int\frac{2x}{x^2+5}\,dx.$$
Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

---

## 2. Theoretical Background and Concepts

- **The Missing Case $n = -1$ in the Power Rule:** The power rule $\int u^n\,du = \frac{u^{n+1}}{n+1} + C$ fails when $n = -1$ because it would cause division by zero. Instead, because $\frac{d}{du}\left(\ln|u|\right) = \frac{1}{u}$ for $u \neq 0$, the antiderivative of $u^{-1} = \frac{1}{u}$ is the natural logarithm:
  $$\int \frac{1}{u}\,du = \ln|u| + C.$$
- **Logarithmic Integration Pattern ("Derivative over Function"):** Combining $\int \frac{1}{u}\,du = \ln|u| + C$ with the substitution $u = g(x)$, $du = g'(x)\,dx$ yields the fundamental formula:
  $$\int \frac{g'(x)}{g(x)}\,dx = \ln|g(x)| + C.$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Comparing the Denominator and the Numerator
Let the denominator be our candidate for the new variable:
$$u = g(x) = x^2 + 5.$$
Note that $x^2 + 5 \ge 5 > 0$ for all $x \in \mathbb{R}$, so the denominator is never zero and the integrand is defined on all of $\mathbb{R}$.
Differentiating the denominator gives:
$$\frac{du}{dx} = 2x \implies du = 2x\,dx.$$
Comparing this with the numerator, we see that the numerator $2x$ is **precisely the derivative of the denominator** $x^2 + 5$.

### Step 2: Explaining the Source of the Logarithm
When we substitute $u = x^2 + 5$ and $du = 2x\,dx$, the entire fraction $\frac{2x\,dx}{x^2+5}$ collapses into $\frac{du}{u} = u^{-1}\,du$. Because the exponent of $u$ is $-1$, reversing differentiation requires a function whose derivative is $\frac{1}{u}$, which is the natural logarithm $\ln|u|$.

### Step 3: Computing the Integral
Performing the substitution:
$$\begin{aligned}
\int \frac{2x}{x^2+5}\,dx &= \int \frac{1}{u}\,du \\
&= \ln|u| + C \\
&= \ln|x^2+5| + C.
\end{aligned}$$
Since $x^2 + 5 > 0$ for every real number $x$, the absolute value bars are redundant and can be replaced with standard parentheses:
$$\int \frac{2x}{x^2+5}\,dx = \ln(x^2+5) + C, \quad C \in \mathbb{R}.$$

---

## 4. Verification and Consistency Checks

We differentiate $F(x) = \ln(x^2+5) + C$ with respect to $x$ using the chain rule $\frac{d}{dx}[\ln(g(x))] = \frac{g'(x)}{g(x)}$:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left[\ln(x^2+5) + C\right] \\
&= \frac{1}{x^2+5} \cdot \frac{d}{dx}(x^2+5) + 0 \\
&= \frac{2x}{x^2+5}.
\end{aligned}$$
This matches the integrand for all $x \in \mathbb{R}$, confirming the solution.
