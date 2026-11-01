# Exercise 5: The Same Substitution in a Different Context

## 1. Problem Statement

Compute
$$\int xe^{x^2}\,dx.$$
First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

---

## 2. Theoretical Background and Concepts

- **Structural Pattern of Substitution:** Both Problem 4 and Problem 5 have the composite structure
  $$\int c \cdot g'(x) \cdot f(g(x))\,dx,$$
  where $g(x) = x^2 + \text{const}$ is a quadratic inner function and the factor $x$ outside is a constant multiple of the inner derivative $g'(x) = 2x$.
- **Adjusting for a Constant Factor:** When $du = g'(x)\,dx$ differs from the factor present in the integrand only by a non-zero multiplicative constant (here $du = 2x\,dx$ whereas the integrand has $x\,dx$), we can divide by the constant:
  $$x\,dx = \frac{1}{2}\,du.$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Comparing Structure with Problem 4
In Problem 4, we integrated $\int 2x(x^2+1)^4\,dx$, where the outer function was a power function $f(u) = u^4$ and the inner function was $u = x^2+1$.
In the current problem, $\int xe^{x^2}\,dx$:
- The **outer function** is now the exponential function $f(u) = e^u$ instead of $u^4$.
- The **inner function** is $u = x^2$ (whose derivative is $u' = 2x$, identical to the derivative of $x^2+1$).
- In both problems, the factor $x$ multiplying the composite function is proportional to the derivative of the inner quadratic expression. Thus, the exact same substitution mechanism applies.

### Step 2: Performing the Substitution
Let
$$u = x^2.$$
Differentiating with respect to $x$ gives:
$$du = 2x\,dx \implies x\,dx = \frac{1}{2}\,du.$$

Substituting $u = x^2$ and $x\,dx = \frac{1}{2}\,du$ into the integral:
$$\begin{aligned}
\int xe^{x^2}\,dx &= \int e^{x^2} \cdot (x\,dx) \\
&= \int e^u \cdot \frac{1}{2}\,du \\
&= \frac{1}{2}\int e^u\,du \\
&= \frac{1}{2}e^u + C.
\end{aligned}$$

### Step 3: Back-Substituting to $x$
Replacing $u$ with $x^2$, we obtain:
$$\int xe^{x^2}\,dx = \frac{1}{2}e^{x^2} + C, \quad C \in \mathbb{R}.$$

---

## 4. Verification and Consistency Checks

We differentiate $F(x) = \frac{1}{2}e^{x^2} + C$ using the chain rule:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left(\frac{1}{2}e^{x^2} + C\right) \\
&= \frac{1}{2} e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 \\
&= \frac{1}{2} e^{x^2} \cdot (2x) \\
&= xe^{x^2}.
\end{aligned}$$
The factor $\frac{1}{2}$ cancels the $2$ from $\frac{d}{dx}(x^2) = 2x$, reproducing the original integrand $xe^{x^2}$.
