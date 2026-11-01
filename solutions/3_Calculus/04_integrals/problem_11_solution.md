# Exercise 11: Choose the Method First

## 1. Problem Statement

For each integral, first write which method you choose and how you recognize it, and then compute:
1. $\int\sin(3x)\,dx$,
2. $\int x\ln x\,dx$,
3. $\int\frac{x}{\sqrt{x^2+1}}\,dx$.

---

## 2. Theoretical Background and Concepts

- **Recognizing Integration by Substitution ($\int f(g(x))g'(x)\,dx$):**
  Used when the integrand is a composite function $f(g(x))$ multiplied (up to a constant factor) by the derivative $g'(x)$ of the inner function $g(x)$. A special case is a linear inner function $g(x) = ax + b$, whose derivative $g'(x) = a$ is a constant.
- **Recognizing Integration by Parts ($\int u\,dv = uv - \int v\,du$):**
  Used when the integrand is a product of two functions from different families (such as a polynomial and a logarithm, exponential, or trigonometric function) where neither factor is the derivative of an inner function of the other, and differentiating one factor simplifies it while the other factor can be integrated.

---

## 3. Detailed Step-by-Step Solution

### Part 1: $\int \sin(3x)\,dx$

- **Choice of Method and Recognition:**
  We choose **linear substitution** ($u = 3x$). We recognize this because $\sin(3x)$ is a composite function with a linear inner function $u = 3x$, whose derivative $u' = 3$ is a constant.
- **Calculation:**
  Let $u = 3x$. Then $du = 3\,dx$, so $dx = \frac{1}{3}\,du$. Substituting gives:
  $$\begin{aligned}
  \int \sin(3x)\,dx &= \int \sin(u) \cdot \frac{1}{3}\,du \\
  &= \frac{1}{3}\int \sin(u)\,du \\
  &= -\frac{1}{3}\cos(u) + C \\
  &= -\frac{1}{3}\cos(3x) + C, \quad C \in \mathbb{R}.
  \end{aligned}$$

---

### Part 2: $\int x\ln x\,dx$ (for $x > 0$)

- **Choice of Method and Recognition:**
  We choose **integration by parts**. We recognize this because the integrand is a product of an algebraic power $x$ and a logarithmic function $\ln x$; there is no composite inner function whose derivative appears outside. Furthermore, differentiating $u = \ln x$ transforms the transcendental logarithm into the simple algebraic power $u' = \frac{1}{x}$, which combines with $v = \frac{1}{2}x^2$ to form a simple power function! (Note: unlike $\int xe^x\,dx$, here we differentiate $\ln x$ and integrate $x$ because $\ln x$ has no elementary one-step antiderivative, whereas its derivative $\frac{1}{x}$ is algebraic.)
- **Calculation:**
  Set
  $$\begin{aligned}
  u &= \ln x & \implies \quad du &= \frac{1}{x}\,dx, \\
  dv &= x\,dx & \implies \quad v &= \frac{1}{2}x^2.
  \end{aligned}$$
  Applying $\int u\,dv = uv - \int v\,du$:
  $$\begin{aligned}
  \int x\ln x\,dx &= \frac{1}{2}x^2\ln x - \int \frac{1}{2}x^2 \cdot \frac{1}{x}\,dx \\
  &= \frac{1}{2}x^2\ln x - \frac{1}{2}\int x\,dx \\
  &= \frac{1}{2}x^2\ln x - \frac{1}{2}\left(\frac{1}{2}x^2\right) + C \\
  &= \frac{1}{2}x^2\ln x - \frac{1}{4}x^2 + C, \quad x > 0, \; C \in \mathbb{R}.
  \end{aligned}$$

---

### Part 3: $\int \frac{x}{\sqrt{x^2+1}}\,dx$

- **Choice of Method and Recognition:**
  We choose **substitution** ($u = x^2 + 1$). We recognize this because the expression under the square root in the denominator is $u = x^2 + 1$, and its derivative $u' = 2x$ is a constant multiple of the factor $x$ in the numerator.
- **Calculation:**
  Let $u = x^2 + 1$ (note $u \ge 1 > 0$ for all $x \in \mathbb{R}$). Then $du = 2x\,dx \implies x\,dx = \frac{1}{2}\,du$. Substituting gives:
  $$\begin{aligned}
  \int \frac{x}{\sqrt{x^2+1}}\,dx &= \int \frac{1}{\sqrt{u}} \cdot \frac{1}{2}\,du \\
  &= \frac{1}{2}\int u^{-1/2}\,du \\
  &= \frac{1}{2} \cdot \frac{u^{1/2}}{1/2} + C \\
  &= \sqrt{u} + C \\
  &= \sqrt{x^2+1} + C, \quad C \in \mathbb{R}.
  \end{aligned}$$

---

## 4. Verification and Consistency Checks

We differentiate all three antiderivatives with respect to $x$:
1. **Part 1:**
   $$\frac{d}{dx}\left(-\frac{1}{3}\cos(3x) + C\right) = -\frac{1}{3}\left(-\sin(3x) \cdot 3\right) = \sin(3x). \quad \checkmark$$
2. **Part 2:**
   $$\frac{d}{dx}\left(\frac{1}{2}x^2\ln x - \frac{1}{4}x^2 + C\right) = \left(x\ln x + \frac{1}{2}x^2 \cdot \frac{1}{x}\right) - \frac{1}{2}x = x\ln x + \frac{1}{2}x - \frac{1}{2}x = x\ln x. \quad \checkmark$$
3. **Part 3:**
   $$\frac{d}{dx}\left((x^2+1)^{1/2} + C\right) = \frac{1}{2}(x^2+1)^{-1/2} \cdot (2x) = \frac{x}{\sqrt{x^2+1}}. \quad \checkmark$$
All three results are verified.
