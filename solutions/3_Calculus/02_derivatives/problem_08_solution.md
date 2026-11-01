# Exercise 8: Two Exponential Functions

## 1. Problem Statement
For
$$f(x)=e^{2x-3}+5^x$$
compute the derivative. Explain why the factor $2$ appears in the first term and why $\ln5$ appears in the second.

---

## 2. Theoretical Background and Concepts
- **Derivative of the Natural Exponential with a Chain Rule Layer:**
  $$\frac{d}{dx}\left(e^{u(x)}\right) = e^{u(x)} \cdot u'(x)$$
- **Derivative of a General Exponential Function ($a > 0, a \neq 1$):**
  Since $a^x = \left(e^{\ln a}\right)^x = e^{x\ln a}$, differentiating with respect to $x$ yields:
  $$\frac{d}{dx}\left(a^x\right) = \frac{d}{dx}\left(e^{x\ln a}\right) = e^{x\ln a} \cdot \ln a = a^x \ln a$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Differentiate the first term $e^{2x-3}$
The term $e^{2x-3}$ is a composite function with outer function $g(u) = e^u$ and inner linear function $u(x) = 2x - 3$.
- Outer derivative: $\frac{d}{du}(e^u) = e^u = e^{2x-3}$
- Inner derivative: $u'(x) = \frac{d}{dx}(2x - 3) = 2$

By the chain rule:
$$\frac{d}{dx}\left(e^{2x-3}\right) = 2e^{2x-3}$$

### Step 2: Differentiate the second term $5^x$
The term $5^x$ is an exponential function with base $a = 5 \neq e$. Applying the general exponential derivative rule:
$$\frac{d}{dx}\left(5^x\right) = 5^x \ln 5$$

### Step 3: Combine the results
By the sum rule:
$$f'(x) = 2e^{2x-3} + 5^x \ln 5$$

### Step 4: Explain the origins of the factors $2$ and $\ln 5$
Both factors actually originate from the **chain rule** applied to the natural exponential function $e^u$, but for two conceptually distinct reasons:
1. **Why $2$ appears in $2e^{2x-3}$:** Here the base of the exponential is already the natural base $e$ (for which $\ln e = 1$), so no base-conversion factor is needed. However, the exponent is $u(x) = 2x - 3$ rather than $x$. Because $u(x)$ changes twice as fast as $x$ ($u'(x) = 2$), the chain rule multiplies the derivative by $2$.
2. **Why $\ln 5$ appears in $5^x \ln 5$:** Here the exponent is simply $x$, so its derivative is $1$, but the base is $5$ instead of $e$. Because $e$ is the unique base whose rate of change equals its own value at every point, we express base $5$ in terms of base $e$ via the identity $5 = e^{\ln 5}$, giving:
   $$5^x = \left(e^{\ln 5}\right)^x = e^{(\ln 5)x}$$
   When we differentiate $e^{(\ln 5)x}$ using the chain rule, the constant coefficient of $x$ in the exponent is $\ln 5$, which comes down as a multiplier:
   $$\frac{d}{dx}\left(e^{(\ln 5)x}\right) = e^{(\ln 5)x} \cdot \frac{d}{dx}((\ln 5)x) = 5^x \ln 5$$

---

## 4. Verification and Consistency Checks

### Alternative Algebraic Method for the First Term
We can rewrite the first term using exponent laws before differentiating:
$$e^{2x-3} = e^{-3} \cdot e^{2x} = e^{-3} \cdot \left(e^2\right)^x$$
Treating $e^{-3}$ as a constant multiplier and $a = e^2$ as the base of an exponential function $a^x$:
$$\frac{d}{dx}\left(e^{-3}(e^2)^x\right) = e^{-3} (e^2)^x \ln(e^2) = e^{-3} e^{2x} \cdot 2 = 2e^{2x-3}$$
This shows that both mechanisms (chain rule on a linear exponent and the $\ln a$ factor from changing the base) are completely unified and yield the exact same derivative $2e^{2x-3}$.
