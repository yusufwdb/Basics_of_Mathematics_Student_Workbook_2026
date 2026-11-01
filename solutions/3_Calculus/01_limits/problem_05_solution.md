# Exercise 5: The Classical Limit Leading to the Number $e$

## 1. Problem Statement
Compute
$$\lim_{n\to\infty}\left(1+\frac1n\right)^n.$$
Calculate several values for increasing $n$ and compare the observed behavior with the value of the limit. Explain why a few values do not constitute a proof.

## 2. Theoretical Background and Concepts
- **Definition of Euler's Number $e$:** The sequence $e_n = \left(1 + \frac{1}{n}\right)^n$ represents an indeterminate form of type $[1^\infty]$ as $n \to \infty$: the base $1 + \frac{1}{n}$ approaches $1$ from above (which tries to keep the power near $1$), while the exponent $n$ grows to $+\infty$ (which tries to make a number greater than $1$ grow large).
- **Monotone Convergence Theorem for Sequences:** Every sequence that is **monotonically increasing** ($e_n < e_{n+1}$) and **bounded above** ($e_n < M$ for all $n$) converges to a finite real limit (its supremum). For $e_n = \left(1 + \frac{1}{n}\right)^n$, this limit is Euler's constant:
  $$e = \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n \approx 2.718281828459\dots$$

## 3. Detailed Step-by-Step Solution

### Step 1: Analytical justification and value of the limit
By the Binomial Theorem, for any positive integer $n$:
$$e_n = \left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^n \binom{n}{k}\frac{1}{n^k} = 1 + 1 + \frac{1}{2!}\left(1 - \frac{1}{n}\right) + \frac{1}{3!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) + \dots + \frac{1}{n!}\prod_{j=1}^{n-1}\left(1 - \frac{j}{n}\right).$$
From this expansion, two key facts follow for all $n \ge 1$:
1. **Strict Monotonicity ($e_n < e_{n+1}$):** Passing from $n$ to $n+1$ increases each factor $\left(1 - \frac{j}{n}\right) < \left(1 - \frac{j}{n+1}\right)$ and adds one more positive term at $k = n+1$. Hence $e_n$ is strictly increasing.
2. **Upper Bound ($2 \le e_n < 3$):** Since $1 - \frac{j}{n} < 1$ and $k! \ge 2^{k-1}$ for $k \ge 2$:
   $$e_n < 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \dots + \frac{1}{n!} \le 1 + 1 + \frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2^{n-1}} = 1 + \left(2 - \frac{1}{2^{n-1}}\right) < 3.$$

By the Monotone Convergence Theorem, the limit exists, lies in $(2, 3)$, and equals Euler's number $e$:
$$\lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n = e \approx 2.718281828\dots$$

---

### Step 2: Calculate several values for increasing $n$
Let us evaluate $e_n = \left(1 + \frac{1}{n}\right)^n$ for progressively larger values of $n$:

| $n$ | Expression $\left(1 + \frac{1}{n}\right)^n$ | Exact or Decimal Value | Difference $e - e_n$ |
| :--- | :--- | :--- | :--- |
| $n = 1$ | $\left(1 + 1\right)^1 = 2^1$ | $2.000000$ | $0.718282$ |
| $n = 2$ | $\left(1 + \frac{1}{2}\right)^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$ | $2.250000$ | $0.468282$ |
| $n = 5$ | $\left(1 + \frac{1}{5}\right)^5 = (1.2)^5$ | $2.488320$ | $0.229962$ |
| $n = 10$ | $(1.1)^{10}$ | $2.593742$ | $0.124539$ |
| $n = 100$ | $(1.01)^{100}$ | $2.704814$ | $0.013468$ |
| $n = 1\,000$ | $(1.001)^{1000}$ | $2.716924$ | $0.001358$ |
| $n = 10\,000$ | $(1.0001)^{10000}$ | $2.718146$ | $0.000136$ |
| $n = 1\,000\,000$ | $(1.000001)^{1000000}$ | $2.718280$ | $0.000001$ |
| **$n \to \infty$** | $\lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n$ | **$e \approx 2.718282$** | **$0$** |

**Comparison of observed behavior with the limit:**
As $n$ increases, the sequence values grow monotonically (each term is larger than the previous one), yet the rate of growth slows down dramatically: increasing $n$ tenfold reduces the remaining distance to $e$ by roughly a factor of $10$ (since $e - e_n \approx \frac{e}{2n}$). All observed values stay strictly below $e \approx 2.718282$ and approach it from below.

---

### Step 3: Explain why a few values do not constitute a proof
Computing $e_n$ for finitely many values of $n$ (even millions of terms) **never constitutes a mathematical proof** of convergence or of the limit's value, for three fundamental reasons:
1. **A limit is a statement about infinitely many terms ($n > N$ for all $N$):** What happens at the first $N$ terms has zero effect on $\lim_{n\to\infty} a_n$. A sequence could behave nicely for $1 \le n \le 10^6$ and then suddenly diverge or jump for $n > 10^6$ (for example, $a_n = e_n + 10^{-100}n$).
2. **Slow divergence can mimic convergence:** Consider the harmonic partial sums $H_n = \sum_{k=1}^n \frac{1}{k}$ or $\ln(\ln n)$. Between $n = 10^6$ and $n = 10^6 + 10$, the terms barely change, creating a false visual impression of stabilizing to a finite limit even though they diverge to $+\infty$.
3. **Numerical rounding errors:** Floating-point arithmetic has finite precision. In fact, if one evaluates $(1 + 1/n)^n$ on a standard 64-bit computer for $n = 10^{16}$, floating-point rounding rounds $1 + 10^{-16}$ to $1.0$, giving the completely false numerical result $1^{10^{16}} = 1$! Only an analytical proof (showing monotonicity and an upper bound) guarantees convergence.

## 4. Verification and Consistency Checks
We can also bracket $e$ from both sides using the known inequality:
$$\left(1 + \frac{1}{n}\right)^n < e < \left(1 + \frac{1}{n}\right)^{n+1}.$$
For $n = 100$:
- Lower bound: $(1.01)^{100} \approx 2.704814$.
- Upper bound: $(1.01)^{101} = 1.01 \times 2.704814 \approx 2.731862$.
Indeed, $e \approx 2.718282 \in (2.704814, 2.731862)$, and the width of the interval is $\frac{e_n}{n} < \frac{3}{n} \to 0$ as $n \to \infty$.
