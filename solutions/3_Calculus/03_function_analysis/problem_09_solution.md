# Exercise 9: An Oblique Asymptote

## 1. Problem Statement
Analyze the asymptotes of
$$f(x)=\frac{x^2+1}{x-1}.$$
Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

---

## 2. Theoretical Background and Concepts
- **Vertical Asymptote:** The line $x = x_0$ is a vertical asymptote if $\lim_{x \to x_0^-} f(x) = \pm\infty$ or $\lim_{x \to x_0^+} f(x) = \pm\infty$.
- **Oblique (Slant) Asymptote:** A line $y = ax + b$ is an oblique asymptote of $f(x)$ as $x \to \pm\infty$ if:
  $$\lim_{x \to \pm\infty} \big[f(x) - (ax + b)\big] = 0$$
  For a rational function $f(x) = \frac{P(x)}{Q(x)}$ where $\deg P = \deg Q + 1$, dividing $P(x)$ by $Q(x)$ yields:
  $$f(x) = ax + b + \frac{R(x)}{Q(x)}, \qquad \deg R < \deg Q$$
  Because $\deg R < \deg Q$, the proper rational remainder term $\frac{R(x)}{Q(x)}$ converges to $0$ as $x \to \pm\infty$, making the quotient $y = ax + b$ the oblique asymptote.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain and Vertical Asymptote
The domain of $f(x) = \frac{x^2+1}{x-1}$ is $D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)$.
We examine the one-sided limits at the excluded point $x = 1$:
- As $x \to 1$, the numerator $x^2 + 1 \to 1^2 + 1 = 2 > 0$.
- For $x \to 1^-$ ($x < 1$), $x - 1 \to 0^-$, so:
  $$\lim_{x \to 1^-} \frac{x^2 + 1}{x - 1} = \left[\frac{2}{0^-}\right] = -\infty$$
- For $x \to 1^+$ ($x > 1$), $x - 1 \to 0^+$, so:
  $$\lim_{x \to 1^+} \frac{x^2 + 1}{x - 1} = \left[\frac{2}{0^+}\right] = +\infty$$

Therefore, **$x = 1$ is a two-sided vertical asymptote**.

### Step 2: Perform Polynomial Division
We divide the numerator $P(x) = x^2 + 1$ by the denominator $Q(x) = x - 1$:
- First step: $\frac{x^2}{x} = x$. Multiply $x(x - 1) = x^2 - x$, and subtract from $x^2 + 1$:
  $$(x^2 + 1) - (x^2 - x) = x + 1$$
- Second step: $\frac{x}{x} = 1$. Multiply $1(x - 1) = x - 1$, and subtract from $x + 1$:
  $$(x + 1) - (x - 1) = 2$$

This gives the polynomial identity $x^2 + 1 = (x - 1)(x + 1) + 2$. Dividing both sides by $x - 1$ (for $x \neq 1$) yields the decomposed form:
$$f(x) = x + 1 + \frac{2}{x - 1}$$
where $q(x) = x + 1$ is the linear quotient and $\frac{2}{x - 1}$ is the remainder term.

### Step 3: Find the Oblique Asymptote and Explain Why the Remainder Term Vanishes for Large $|x|$
From the decomposition $f(x) = (x + 1) + \frac{2}{x - 1}$, the vertical distance between the graph of $f(x)$ and the line $y = x + 1$ is:
$$f(x) - (x + 1) = \frac{2}{x - 1}$$

**Why $\frac{2}{x - 1}$ vanishes for large $|x|$:**
1. The numerator of the remainder term $\frac{2}{x - 1}$ is a fixed constant ($2$), whereas the denominator $x - 1$ grows unboundedly in magnitude as $|x| \to \infty$ ($\lim_{|x| \to \infty} |x - 1| = \infty$).
2. Dividing a fixed number $2$ by a quantity whose absolute value grows without bound produces a fraction arbitrarily close to zero:
   $$\lim_{x \to +\infty} \frac{2}{x - 1} = 0^+ \qquad \text{and} \qquad \lim_{x \to -\infty} \frac{2}{x - 1} = 0^-$$

Consequently:
$$\lim_{x \to \pm\infty} \big[f(x) - (x + 1)\big] = 0$$
which proves that **$y = x + 1$ is the two-sided oblique asymptote** of $f(x)$ as $x \to \pm\infty$ (and there are no horizontal asymptotes). Moreover:
- For $x > 1$ (including $x \to +\infty$), $\frac{2}{x-1} > 0$, so the graph of $f$ approaches $y = x + 1$ **from above**.
- For $x < 1$ (including $x \to -\infty$), $\frac{2}{x-1} < 0$, so the graph of $f$ approaches $y = x + 1$ **from below**.

---

## 4. Verification and Consistency Checks

### Verification Using Standard Limit Formulas for $a$ and $b$
By Cauchy's limit formulas for an oblique asymptote $y = ax + b$:
1. **Slope $a$:**
   $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x} = \lim_{x \to \pm\infty} \frac{x^2 + 1}{x(x - 1)} = \lim_{x \to \pm\infty} \frac{x^2 + 1}{x^2 - x} = \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x^2}}{1 - \frac{1}{x}} = 1$$
2. **Intercept $b$:**
   $$b = \lim_{x \to \pm\infty} \big(f(x) - ax\big) = \lim_{x \to \pm\infty} \left(\frac{x^2 + 1}{x - 1} - x\right) = \lim_{x \to \pm\infty} \frac{x^2 + 1 - x^2 + x}{x - 1} = \lim_{x \to \pm\infty} \frac{x + 1}{x - 1} = 1$$
This independently confirms the oblique asymptote $y = x + 1$.
