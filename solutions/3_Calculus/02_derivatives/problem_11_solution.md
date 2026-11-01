# Exercise 11: Derivative from the Definition

## 1. Problem Statement
Using only
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,$$
find the derivative of $f(x)=x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

---

## 2. Theoretical Background and Concepts
- **Limit Definition of the Derivative:** A function $f$ is differentiable at $x$ if the limit of the difference quotient
  $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
  exists and is finite.
  - For any $h \neq 0$, the difference quotient $\frac{f(x+h) - f(x)}{h}$ represents the **slope of the secant line** passing through $(x, f(x))$ and $(x+h, f(x+h))$, or equivalently the average rate of change of $f$ over the interval $[x, x+h]$.
  - Taking the limit as $h \to 0$ transitions from the secant slope to the **slope of the tangent line** (instantaneous rate of change).
- **Important Subtlety About $h \to 0$:** In the limit $\lim_{h \to 0}$, $h$ approaches $0$ through non-zero values ($h \neq 0$). This guarantees that dividing by $h$ is valid before taking the limit.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Set up the difference quotient for $f(x) = x^2$
For $f(x) = x^2$, we evaluate the function at the shifted argument $x + h$:
$$f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$$
Substituting $f(x+h)$ and $f(x)$ into the difference quotient for $h \neq 0$:
$$\frac{f(x+h) - f(x)}{h} = \frac{(x^2 + 2xh + h^2) - x^2}{h}$$

### Step 2: Simplify the difference quotient algebraically (for $h \neq 0$)
Canceling $x^2 - x^2 = 0$ in the numerator gives:
$$\frac{f(x+h) - f(x)}{h} = \frac{2xh + h^2}{h} = \frac{h(2x + h)}{h}$$
Since $h \neq 0$ inside the limit process, we can divide the numerator and denominator by $h$:
$$\frac{f(x+h) - f(x)}{h} = 2x + h \qquad (h \neq 0)$$

### Step 3: Take the limit as $h \to 0$
Now we apply the limit as $h \to 0$:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = \lim_{h \to 0} (2x + h)$$
Since $2x + h$ is a continuous linear function of $h$ (with $x$ held fixed during the limit), we evaluate the limit by direct substitution $h = 0$:
$$f'(x) = 2x + 0 = 2x$$

### Step 4: Compare with the power rule and explain where the limit is used
1. **Comparison with the Power Rule:** Applying the power rule $\frac{d}{dx}(x^n) = nx^{n-1}$ with $n = 2$ gives:
   $$f'(x) = 2x^{2-1} = 2x$$
   Both methods yield the exact same result $2x$; in fact, the limit calculation above is the proof of the power rule for $n = 2$.
2. **Where the limit is used in the calculation:**
   - Before simplifying, direct substitution $h = 0$ into $\frac{(x+h)^2 - x^2}{h}$ produces the indeterminate form $\frac{0}{0}$.
   - The definition of the limit $\lim_{h \to 0}$ is first used to justify that **$h \neq 0$**, allowing us to cancel the common factor $h$ from $\frac{h(2x+h)}{h}$ to obtain $2x + h$.
   - The limit is then used in the final step $\lim_{h \to 0}(2x + h) = 2x$ to make the higher-order perturbation term $h$ vanish as the secant line approaches the tangent line.

---

## 4. Verification and Consistency Checks

### Alternative Limit Definition ($t \to x$)
We can also verify the derivative using the equivalent limit definition $f'(x) = \lim_{t \to x} \frac{f(t) - f(x)}{t - x}$:
$$f'(x) = \lim_{t \to x} \frac{t^2 - x^2}{t - x} = \lim_{t \to x} \frac{(t - x)(t + x)}{t - x} = \lim_{t \to x} (t + x) = x + x = 2x$$
This confirms $f'(x) = 2x$ via factoring a difference of squares.
