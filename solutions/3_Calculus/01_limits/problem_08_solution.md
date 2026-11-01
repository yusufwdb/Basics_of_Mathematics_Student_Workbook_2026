# Exercise 8: A Square Root in a Function Limit

## 1. Problem Statement
Compute
$$\lim_{x\to4}\frac{\sqrt{x}-2}{x-4}$$
by rationalizing the numerator. Compare the idea with Exercise 3 involving a sequence.

## 2. Theoretical Background and Concepts
- **Indeterminate Form $\left[\frac{0}{0}\right]$ Involving Radicals:** When a quotient $\frac{\sqrt{u(x)} - \sqrt{v(x)}}{w(x)}$ tends to $\frac{0}{0}$ as $x \to x_0$, multiplying the numerator and denominator by the **conjugate radical expression** $\sqrt{u(x)} + \sqrt{v(x)}$ uses $(a - b)(a + b) = a^2 - b^2$ to turn the numerator into $u(x) - v(x)$, exposing the zero-producing factor $(x - x_0)$ so it can be canceled.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the indeterminate form
As $x \to 4$, the numerator approaches $\sqrt{4} - 2 = 2 - 2 = 0$ and the denominator approaches $4 - 4 = 0$, giving an indeterminate form of type $\left[\frac{0}{0}\right]$.

### Step 2: Rationalize the numerator using the conjugate expression
For $x \ge 0, \, x \neq 4$, multiply both the numerator and the denominator by the conjugate of the numerator, $\sqrt{x} + 2$ (which is non-zero since $\sqrt{x} + 2 \ge 2 > 0$):
$$\frac{\sqrt{x} - 2}{x - 4} = \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)}.$$
Using $(a - b)(a + b) = a^2 - b^2$ in the numerator, we have $(\sqrt{x})^2 - 2^2 = x - 4$:
$$\frac{\sqrt{x} - 2}{x - 4} = \frac{x - 4}{(x - 4)(\sqrt{x} + 2)}.$$

### Step 3: Cancel the common factor $(x - 4)$ and evaluate the limit
Since $x \neq 4$ in the limit as $x \to 4$, we cancel the non-zero factor $(x - 4)$:
$$\frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \quad (x \ge 0, \, x \neq 4).$$
Now the denominator $\sqrt{x} + 2$ is continuous at $x = 4$ and its value at $x = 4$ is $\sqrt{4} + 2 = 4 \neq 0$. Taking the limit gives:
$$\lim_{x\to 4}\frac{\sqrt{x} - 2}{x - 4} = \lim_{x\to 4}\frac{1}{\sqrt{x} + 2} = \frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4}.$$

---

### Step 4: Comparison with Exercise 3 ($\lim_{n\to\infty}(\sqrt{n^2+5n} - n)$)

| Aspect | Exercise 3 (Sequence Limit) | Exercise 8 (Function Limit) |
| :--- | :--- | :--- |
| **Limit point** | $n \to \infty$ (discrete variable at infinity) | $x \to 4$ (continuous variable at a finite point) |
| **Indeterminate form** | $[\infty - \infty]$ | $\left[\frac{0}{0}\right]$ |
| **Core algebraic tool** | Multiply by $\frac{\sqrt{n^2+5n}+n}{\sqrt{n^2+5n}+n}$ using $(a-b)(a+b)=a^2-b^2$ | Multiply by $\frac{\sqrt{x}+2}{\sqrt{x}+2}$ using $(a-b)(a+b)=a^2-b^2$ |
| **Effect of conjugation** | Cancels the dominant $n^2$ terms in $(n^2+5n)-n^2=5n$, leaving a clean $\left[\frac{\infty}{\infty}\right]$ ratio of degree $1$ | Produces the exact factor $x - 4$ in the numerator so that $\frac{x-4}{x-4}$ cancels, removing the $\frac{0}{0}$ singularity |

**Key takeaway:** In both problems, the difficulty stems from subtracting two quantities that are nearly equal ($\sqrt{n^2+5n} \approx n$ as $n\to\infty$, and $\sqrt{x} \approx 2$ as $x\to 4$). Multiplying by the conjugate converts the **difference** of two nearly equal terms into a **sum** of two non-zero terms ($\sqrt{n^2+5n}+n \approx 2n$, and $\sqrt{x}+2 \to 4$), while squaring removes the square root so the leading cancellation can be performed algebraically.

## 4. Verification and Consistency Checks
1. **Alternative Method — Factoring $x - 4$ directly as a difference of squares:**
   For $x \ge 0$, we can view $x - 4 = (\sqrt{x})^2 - 2^2 = (\sqrt{x} - 2)(\sqrt{x} + 2)$. Then for $x \neq 4$:
   $$\frac{\sqrt{x} - 2}{x - 4} = \frac{\sqrt{x} - 2}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \xrightarrow{x \to 4} \frac{1}{4}.$$
2. **Derivative Interpretation Check:**
   By definition of the derivative, $\lim_{x\to 4}\frac{\sqrt{x} - \sqrt{4}}{x - 4}$ is the derivative of $g(x) = \sqrt{x}$ at $x = 4$. Since $g'(x) = \frac{1}{2\sqrt{x}}$, we have $g'(4) = \frac{1}{2\sqrt{4}} = \frac{1}{4}$, which confirms our result.
