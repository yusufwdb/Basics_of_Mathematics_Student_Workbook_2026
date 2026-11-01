# Exercise 11: An n-th Root

## 1. Problem Statement
Compute
$$\lim_{n\to\infty}\sqrt[n]{5^n+2^n}.$$
Explain which term dominates and why the transformation looks different from the case of a quotient of polynomials.

## 2. Theoretical Background and Concepts
- **Dominance Among Exponential Terms ($a^n$ vs. $b^n$):** For positive bases $a > b > 0$, the exponential $a^n$ grows exponentially faster than $b^n$ because their ratio $\left(\frac{b}{a}\right)^n$ is a geometric sequence with base $0 < \frac{b}{a} < 1$, so:
  $$\lim_{n\to\infty}\left(\frac{b}{a}\right)^n = 0.$$
- **Squeeze Theorem for $n$-th Roots:** If $A^n \le x_n \le c \cdot A^n$ for all $n \ge 1$ (with $A > 0, c \ge 1$), taking the $n$-th root preserves inequalities:
  $$A \le \sqrt[n]{x_n} \le \sqrt[n]{c} \cdot A.$$
  Since $\lim_{n\to\infty} \sqrt[n]{c} = 1$ for any constant $c > 0$, the Squeeze Theorem forces $\lim_{n\to\infty} \sqrt[n]{x_n} = A$.
- **Continuity of Power/Exponential Operations:** Equivalently, factoring $a^n$ out from under the $n$-th root gives $\sqrt[n]{a^n\left(1 + (b/a)^n\right)} = a\left(1 + (b/a)^n\right)^{1/n} \to a \cdot 1^0 = a$.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the dominant term and factor it out
Inside the $n$-th root $\sqrt[n]{5^n + 2^n}$, we have two exponential terms: $5^n$ and $2^n$. Since $5 > 2 > 0$, the term **$5^n$ dominates** $2^n$ as $n \to \infty$ (for example, at $n = 10$, $5^{10} = 9\,765\,625$ while $2^{10} = 1\,024$).

Factor $5^n$ out of the sum inside the $n$-th root:
$$\sqrt[n]{5^n + 2^n} = \sqrt[n]{5^n\left(1 + \frac{2^n}{5^n}\right)} = \sqrt[n]{5^n} \cdot \sqrt[n]{1 + \left(\frac{2}{5}\right)^n} = 5 \cdot \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n}.$$

### Step 2: Compute the limit using two rigorous approaches

#### Method A: Using the Squeeze Theorem (Two-Crowds / Sandwich Theorem)
Since $2^n > 0$ and $2^n < 5^n$ for all $n \ge 1$, we can bound $5^n + 2^n$ from below and above by multiples of the dominant term $5^n$:
$$5^n < 5^n + 2^n < 5^n + 5^n = 2 \cdot 5^n.$$
Taking the $n$-th root across the inequality (which preserves order since $t \mapsto t^{1/n}$ is strictly increasing on $(0, \infty)$):
$$\sqrt[n]{5^n} < \sqrt[n]{5^n + 2^n} < \sqrt[n]{2 \cdot 5^n}$$
$$5 < \sqrt[n]{5^n + 2^n} < 5\sqrt[n]{2}.$$
Since $\lim_{n\to\infty} \sqrt[n]{2} = 1$, both the lower bound $5$ and the upper bound $5\sqrt[n]{2}$ converge to $5$:
$$\lim_{n\to\infty} 5 = 5 \quad \text{and} \quad \lim_{n\to\infty} 5\sqrt[n]{2} = 5 \cdot 1 = 5.$$
By the Squeeze Theorem:
$$\lim_{n\to\infty}\sqrt[n]{5^n + 2^n} = 5.$$

#### Method B: Direct evaluation of the factored form
From Step 1, $\sqrt[n]{5^n + 2^n} = 5\left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n}$. As $n \to \infty$, $\left(\frac{2}{5}\right)^n \to 0$ (since $\left|\frac{2}{5}\right| < 1$) and $\frac{1}{n} \to 0$, so the base $1 + \left(\frac{2}{5}\right)^n \to 1$ and the exponent $\frac{1}{n} \to 0$ (which is a non-indeterminate form $[1^0] = 1$). Thus:
$$\lim_{n\to\infty}\sqrt[n]{5^n + 2^n} = 5 \cdot 1^0 = 5.$$

---

### Step 3: Why the transformation looks different from a quotient of polynomials
1. **Polynomials vs. Exponentials:**
   - In a **quotient of polynomials** (such as $\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}$), the variable $n$ is in the **base** while the exponents are fixed constants ($2, 1, 0$). Dominance is determined by the **largest exponent** ($n^2$), and factoring $n^2$ out of numerator and denominator causes $n^2/n^2 = 1$ to **cancel between top and bottom**, leaving behind the ratio of leading coefficients ($\frac{4}{2} = 2$).
   - In $\sqrt[n]{5^n + 2^n}$, the variable $n$ is in the **exponent** (and in the index of the root $\frac{1}{n}$), while the bases ($5$ and $2$) are fixed constants. Dominance is determined by the **largest base** ($5^n$ over $2^n$).
2. **Role of the $n$-th root instead of a denominator:**
   Here there is no denominator to cancel $5^n$; instead, the outer operation is the **$n$-th root** $(\cdot)^{1/n}$, which undoes the $n$-th power via $\sqrt[n]{5^n} = (5^n)^{1/n} = 5$, while turning the remaining factor into $\sqrt[n]{1 + (2/5)^n} \to 1$.

## 4. Verification and Consistency Checks
Let us compute $\sqrt[n]{5^n + 2^n}$ numerically for small and moderate $n$:
- $n = 1$: $\sqrt[1]{5^1 + 2^1} = 7$.
- $n = 2$: $\sqrt{25 + 4} = \sqrt{29} \approx 5.38516$.
- $n = 5$: $\sqrt[5]{3125 + 32} = \sqrt[5]{3157} \approx 5.01020$.
- $n = 10$: $\sqrt[10]{9765625 + 1024} = 5\left(1 + 0.4^{10}\right)^{0.1} \approx 5.000052$.
The sequence converges rapidly to $5$ from above, because the error is roughly $\frac{5}{n}\left(\frac{2}{5}\right)^n$, which decays both algebraically and exponentially.
