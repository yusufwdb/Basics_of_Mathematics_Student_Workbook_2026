# Exercise 4: Powers and Oscillation

## 1. Problem Statement
Analyze
$$\left(\frac23\right)^n,\qquad \left(\frac32\right)^n,\qquad (-1)^n,\qquad \frac{(-1)^n}{n}.$$
For each sequence, describe the type of behavior and justify your answer.

## 2. Theoretical Background and Concepts
- **Geometric Sequence $a_n = q^n$:**
  - If $|q| < 1$, then $\lim_{n\to\infty} q^n = 0$.
  - If $q > 1$, then $\lim_{n\to\infty} q^n = +\infty$ (monotonically increasing without bound).
  - If $q = -1$, the sequence $(-1)^n$ oscillates between $-1$ and $1$ and has no limit.
- **Subsequence Criterion for Convergence:** If a sequence $(a_n)$ converges to $L$, then every subsequence (in particular, the even-indexed subsequence $a_{2k}$ and the odd-indexed subsequence $a_{2k-1}$) must converge to the same limit $L$.
- **Squeeze Theorem (or Product of a Bounded Sequence and a Null Sequence):** If $|a_n| \le b_n$ for all $n$ and $\lim_{n\to\infty} b_n = 0$, then $\lim_{n\to\infty} a_n = 0$.

## 3. Detailed Step-by-Step Solution

### 1. Sequence $a_n = \left(\frac{2}{3}\right)^n$
- **Type of behavior:** **Monotonically decreasing and convergent to $0$.**
- **Justification:**
  This is a geometric sequence $q^n$ with base $q = \frac{2}{3}$, which satisfies $0 < q < 1$.
  - **Monotonicity:** Since $\frac{a_{n+1}}{a_n} = \frac{2}{3} < 1$ and $a_n > 0$, we have $a_{n+1} < a_n$ for all $n \ge 1$.
  - **Limit:** Writing $\frac{2}{3} = \frac{1}{3/2} = \frac{1}{1 + 1/2}$, by Bernoulli's inequality $\left(1 + \frac{1}{2}\right)^n \ge 1 + \frac{n}{2}$, so:
    $$0 < \left(\frac{2}{3}\right)^n = \frac{1}{\left(1 + \frac{1}{2}\right)^n} \le \frac{1}{1 + \frac{n}{2}} < \frac{2}{n}.$$
    By the Squeeze Theorem, since $\lim_{n\to\infty}\frac{2}{n} = 0$, we conclude:
    $$\lim_{n\to\infty} \left(\frac{2}{3}\right)^n = 0.$$

---

### 2. Sequence $b_n = \left(\frac{3}{2}\right)^n$
- **Type of behavior:** **Monotonically increasing and divergent to $+\infty$.**
- **Justification:**
  This is a geometric sequence $q^n$ with base $q = \frac{3}{2} = 1 + \frac{1}{2} > 1$.
  - **Monotonicity:** $b_{n+1} = \frac{3}{2}b_n > b_n > 0$, so the sequence is strictly increasing.
  - **Divergence to $+\infty$:** By Bernoulli's inequality $(1 + h)^n \ge 1 + nh$ for $h = \frac{1}{2} > 0$:
    $$\left(\frac{3}{2}\right)^n = \left(1 + \frac{1}{2}\right)^n \ge 1 + \frac{n}{2}.$$
    Since $\lim_{n\to\infty}\left(1 + \frac{n}{2}\right) = +\infty$, comparison yields:
    $$\lim_{n\to\infty} \left(\frac{3}{2}\right)^n = +\infty.$$

---

### 3. Sequence $c_n = (-1)^n$
- **Type of behavior:** **Bounded, periodic oscillation; divergent (the limit does not exist).**
- **Justification:**
  The terms alternate indefinitely between $-1$ and $+1$: $(-1, 1, -1, 1, -1, 1, \dots)$.
  Consider the two subsequences of even and odd indices:
  - For even $n = 2k$: $c_{2k} = (-1)^{2k} = 1 \implies \lim_{k\to\infty} c_{2k} = 1$.
  - For odd $n = 2k-1$: $c_{2k-1} = (-1)^{2k-1} = -1 \implies \lim_{k\to\infty} c_{2k-1} = -1$.
  Because the two subsequences converge to different limits ($1 \neq -1$), the sequence $((-1)^n)$ **does not have a limit** (it diverges by oscillation).

---

### 4. Sequence $d_n = \frac{(-1)^n}{n}$
- **Type of behavior:** **Damped oscillation; convergent to $0$.**
- **Justification:**
  The sequence alternates in sign: $\left(-1, \frac{1}{2}, -\frac{1}{3}, \frac{1}{4}, -\frac{1}{5}, \dots\right)$, oscillating above and below $0$. However, the amplitude of oscillation is $\left|\frac{(-1)^n}{n}\right| = \frac{1}{n}$, which shrinks to $0$.
  For all $n \ge 1$, we have the two-sided inequality:
  $$-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}.$$
  Since $\lim_{n\to\infty}\left(-\frac{1}{n}\right) = 0$ and $\lim_{n\to\infty}\frac{1}{n} = 0$, the **Squeeze Theorem** implies:
  $$\lim_{n\to\infty} \frac{(-1)^n}{n} = 0.$$
  This shows that oscillation does **not** rule out convergence if the amplitude of the oscillation decays to zero.

## 4. Verification and Consistency Checks
Let us tabulate the first few terms and large-$n$ values of all four sequences to verify their qualitative and quantitative behavior:

| $n$ | $\left(\frac{2}{3}\right)^n$ | $\left(\frac{3}{2}\right)^n$ | $(-1)^n$ | $\frac{(-1)^n}{n}$ |
| :--- | :--- | :--- | :--- | :--- |
| $1$ | $0.6667$ | $1.5000$ | $-1$ | $-1.0000$ |
| $2$ | $0.4444$ | $2.2500$ | $+1$ | $+0.5000$ |
| $3$ | $0.2963$ | $3.3750$ | $-1$ | $-0.3333$ |
| $10$ | $0.0173$ | $57.665$ | $+1$ | $+0.1000$ |
| $20$ | $0.0003$ | $3325.3$ | $+1$ | $+0.0500$ |
| **$n\to\infty$** | **$0$** | **$+\infty$** | **Does not exist** | **$0$** |
