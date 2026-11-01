# Exercise 3: A Square Root and Removing an Indeterminate Form

## 1. Problem Statement
Compute
$$\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right).$$
Use the conjugate expression and explain why this transformation removes the difficulty.

## 2. Theoretical Background and Concepts
- **Indeterminate Form $[\infty - \infty]$:** When two terms both tend to $+\infty$, their difference $A_n - B_n$ cannot be evaluated directly by limit arithmetic because the result depends on the fine cancellation between their leading growth rates.
- **Rationalization via the Conjugate Expression:** Using the difference-of-squares algebraic identity
  $$(a - b)(a + b) = a^2 - b^2 \implies \sqrt{A} - B = \frac{(\sqrt{A} - B)(\sqrt{A} + B)}{\sqrt{A} + B} = \frac{A - B^2}{\sqrt{A} + B},$$
  we convert a difference of square roots into a quotient where the leading quadratic terms $n^2$ in the numerator cancel out, and the denominator involves a **sum** $\sqrt{A} + B \to +\infty$ rather than a difference.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the difficulty
As $n \to \infty$, we have $\sqrt{n^2 + 5n} \to +\infty$ and $n \to +\infty$. Thus, $\sqrt{n^2 + 5n} - n$ is an indeterminate form of type $[\infty - \infty]$. Factoring $n$ out directly gives $n\left(\sqrt{1 + \frac{5}{n}} - 1\right)$, which is of type $[\infty \cdot 0]$—still indeterminate.

### Step 2: Multiply and divide by the conjugate expression
Multiply $\sqrt{n^2 + 5n} - n$ by $\frac{\sqrt{n^2 + 5n} + n}{\sqrt{n^2 + 5n} + n}$:
$$\sqrt{n^2 + 5n} - n = \frac{\left(\sqrt{n^2 + 5n} - n\right)\left(\sqrt{n^2 + 5n} + n\right)}{\sqrt{n^2 + 5n} + n}.$$
Apply the difference-of-squares formula $(a-b)(a+b) = a^2 - b^2$ in the numerator:
$$\sqrt{n^2 + 5n} - n = \frac{(n^2 + 5n) - n^2}{\sqrt{n^2 + 5n} + n} = \frac{5n}{\sqrt{n^2 + 5n} + n}.$$

### Step 3: Explain why this transformation removes the difficulty
1. **Cancellation of the leading $n^2$ terms in the numerator:** Squaring $\sqrt{n^2 + 5n}$ and $n$ eliminates the radical in the numerator and cancels the dominant $n^2$ term: $(n^2 + 5n) - n^2 = 5n$.
2. **Replacement of subtraction by addition in the denominator:** In the denominator $\sqrt{n^2 + 5n} + n$, both terms are positive and **added** together, so their leading terms reinforce each other ($\approx n + n = 2n$) instead of canceling. This turns the $[\infty - \infty]$ problem into a standard $\left[\frac{\infty}{\infty}\right]$ quotient where the numerator and denominator both have degree $1$ in $n$.

### Step 4: Factor out $n$ and compute the limit
For $n \ge 1$, we have $n = \sqrt{n^2}$, so:
$$\sqrt{n^2 + 5n} = \sqrt{n^2\left(1 + \frac{5}{n}\right)} = n\sqrt{1 + \frac{5}{n}}.$$
Substitute this into the denominator and cancel $n$:
$$\frac{5n}{\sqrt{n^2 + 5n} + n} = \frac{5n}{n\left(\sqrt{1 + \frac{5}{n}} + 1\right)} = \frac{5}{\sqrt{1 + \frac{5}{n}} + 1}.$$
Now take the limit as $n \to \infty$. Since $\lim_{n\to\infty}\frac{5}{n} = 0$ and the square root function is continuous at $1$:
$$\lim_{n\to\infty}\left(\sqrt{n^2 + 5n} - n\right) = \frac{5}{\sqrt{1 + 0} + 1} = \frac{5}{1 + 1} = \frac{5}{2}.$$

## 4. Verification and Consistency Checks
1. **Completing the Square / Binomial Approximation Check:**
   Notice that under the square root we can complete the square:
   $$n^2 + 5n = \left(n + \frac{5}{2}\right)^2 - \frac{25}{4}.$$
   For very large $n$, the constant $-\frac{25}{4}$ is negligible compared to $\left(n + \frac{5}{2}\right)^2$, so:
   $$\sqrt{n^2 + 5n} - n \approx \sqrt{\left(n + \frac{5}{2}\right)^2} - n = \left(n + \frac{5}{2}\right) - n = \frac{5}{2}.$$
2. **Numerical Evaluation:**
   - For $n = 100$: $\sqrt{10000 + 500} - 100 = \sqrt{10500} - 100 \approx 102.4695 - 100 = 2.4695$.
   - For $n = 10000$: $\sqrt{100050000} - 10000 \approx 10002.49969 - 10000 = 2.49969 \to 2.5 = \frac{5}{2}$.
   This confirms the analytical result $\frac{5}{2}$.
