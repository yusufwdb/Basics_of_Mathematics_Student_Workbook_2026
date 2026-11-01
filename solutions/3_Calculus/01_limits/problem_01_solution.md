# Exercise 1: Dominant Terms in a Sequence

## 1. Problem Statement
Compute
$$\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7}.$$
Explain why the highest-degree terms determine the result.

## 2. Theoretical Background and Concepts
- **Limit of a Rational Sequence:** For a sequence $a_n = \frac{P(n)}{Q(n)}$ where $P(n)$ and $Q(n)$ are polynomials in $n$, direct substitution as $n \to \infty$ typically yields an indeterminate form $\left[\frac{\infty}{\infty}\right]$.
- **Factoring Out the Highest Power:** To resolve $\left[\frac{\infty}{\infty}\right]$, we factor out the highest power of $n$ present in the denominator (here $n^2$) from both the numerator and the denominator.
- **Basic Reciprocal Limits:** For any constant $c \in \mathbb{R}$ and any positive exponent $k > 0$:
  $$\lim_{n \to \infty} \frac{c}{n^k} = 0.$$
- **Arithmetic of Limits:** If $\lim_{n\to\infty} x_n = X$ and $\lim_{n\to\infty} y_n = Y \neq 0$, then $\lim_{n\to\infty} \frac{x_n}{y_n} = \frac{X}{Y}$.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the indeterminate form and highest power
As $n \to \infty$, both the numerator $4n^2 - 3n + 1 \to \infty$ and the denominator $2n^2 + 5n - 7 \to \infty$, producing an indeterminate form of type $\left[\frac{\infty}{\infty}\right]$. Both polynomials have degree $2$, so the highest power of $n$ is $n^2$.

### Step 2: Factor out $n^2$ from numerator and denominator
For $n \ge 1$ ($n \neq 0$), we factor $n^2$ out of the numerator and denominator and cancel the common factor $n^2$:
$$\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{n^2\left(4 - \frac{3}{n} + \frac{1}{n^2}\right)}{n^2\left(2 + \frac{5}{n} - \frac{7}{n^2}\right)} = \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}}.$$

### Step 3: Evaluate the limit of each term
Using the basic limits $\lim_{n\to\infty} \frac{1}{n} = 0$ and $\lim_{n\to\infty} \frac{1}{n^2} = 0$:
- Limit of the numerator:
  $$\lim_{n\to\infty}\left(4 - \frac{3}{n} + \frac{1}{n^2}\right) = 4 - 3(0) + 0 = 4.$$
- Limit of the denominator:
  $$\lim_{n\to\infty}\left(2 + \frac{5}{n} - \frac{7}{n^2}\right) = 2 + 5(0) - 7(0) = 2 \neq 0.$$

By the quotient rule for limits:
$$\lim_{n\to\infty}\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{4}{2} = 2.$$

### Step 4: Explain why the highest-degree terms determine the result
When $n$ grows very large, $n^2$ grows much faster than $n$ and $1$: specifically, the ratios of the lower-degree terms to the leading term $n^2$ are $\frac{-3n}{4n^2} = -\frac{3}{4n} \to 0$ and $\frac{1}{4n^2} \to 0$. Thus, relative to $4n^2$, the contributions of $-3n$ and $+1$ become negligible as $n \to \infty$ (and similarly $5n - 7$ is negligible compared to $2n^2$). Consequently, for large $n$:
$$\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} \approx \frac{4n^2}{2n^2} = \frac{4}{2} = 2,$$
so the limit is governed solely by the ratio of the leading coefficients of the highest-degree terms.

## 4. Verification and Consistency Checks
1. **Exact Difference from the Limit ($2$):**
   Let us compute the difference between the sequence $a_n$ and its limit $2$:
   $$a_n - 2 = \frac{4n^2 - 3n + 1 - 2(2n^2 + 5n - 7)}{2n^2 + 5n - 7} = \frac{-13n + 15}{2n^2 + 5n - 7}.$$
   For large $n$, $|a_n - 2| \approx \frac{13n}{2n^2} = \frac{13}{2n} \to 0$ as $n \to \infty$.
2. **Numerical Check:**
   - For $n = 10$: $a_{10} = \frac{400 - 30 + 1}{200 + 50 - 7} = \frac{371}{243} \approx 1.5267$.
   - For $n = 100$: $a_{100} = \frac{40000 - 300 + 1}{20000 + 500 - 7} = \frac{39701}{20493} \approx 1.9373$.
   - For $n = 1000$: $a_{1000} = \frac{3997001}{2004993} \approx 1.9935$.
   The terms approach $2$ steadily from below, consistent with $a_n - 2 \approx -\frac{6.5}{n}$.
