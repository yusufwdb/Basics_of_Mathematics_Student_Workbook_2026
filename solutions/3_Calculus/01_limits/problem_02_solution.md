# Exercise 2: Different Growth Rates

## 1. Problem Statement
Compute
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4},\qquad \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}.$$
Compare the two cases and formulate a general observation about the degrees of the polynomials in the numerator and denominator.

## 2. Theoretical Background and Concepts
Let $P(n) = a_p n^p + \dots + a_0$ ($a_p \neq 0$) and $Q(n) = b_q n^q + \dots + b_0$ ($b_q \neq 0$) be polynomials of degrees $p = \deg P$ and $q = \deg Q$. By factoring out $n^p$ from $P(n)$ and $n^q$ from $Q(n)$:
$$\frac{P(n)}{Q(n)} = n^{p-q} \cdot \frac{a_p + \frac{a_{p-1}}{n} + \dots + \frac{a_0}{n^p}}{b_q + \frac{b_{q-1}}{n} + \dots + \frac{b_0}{n^q}}.$$
As $n \to \infty$, the second factor converges to the non-zero constant $\frac{a_p}{b_q}$, while the behavior of $n^{p-q}$ depends on the sign of $p - q$.

## 3. Detailed Step-by-Step Solution

### Part 1: First Limit $\lim_{n\to\infty}\frac{3n+1}{n^2+4}$
Here, the numerator has degree $p = 1$ and the denominator has degree $q = 2$.
Factor out the highest power of the denominator ($n^2$) from both numerator and denominator:
$$\frac{3n + 1}{n^2 + 4} = \frac{n^2\left(\frac{3}{n} + \frac{1}{n^2}\right)}{n^2\left(1 + \frac{4}{n^2}\right)} = \frac{\frac{3}{n} + \frac{1}{n^2}}{1 + \frac{4}{n^2}}.$$
As $n \to \infty$, we have $\frac{3}{n} \to 0$, $\frac{1}{n^2} \to 0$, and $\frac{4}{n^2} \to 0$. Therefore:
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4} = \frac{0 + 0}{1 + 0} = \frac{0}{1} = 0.$$

---

### Part 2: Second Limit $\lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}$
Here, the numerator has degree $p = 3$ and the denominator has degree $q = 2$.
Factor out the highest power of the denominator ($n^2$) from both numerator and denominator (or factor $n^3$ from the top and $n^2$ from the bottom):
$$\frac{2n^3 - n}{5n^2 + 1} = \frac{n^3\left(2 - \frac{1}{n^2}\right)}{n^2\left(5 + \frac{1}{n^2}\right)} = n \cdot \frac{2 - \frac{1}{n^2}}{5 + \frac{1}{n^2}}.$$
As $n \to \infty$:
- The fraction $\frac{2 - \frac{1}{n^2}}{5 + \frac{1}{n^2}}$ converges to $\frac{2 - 0}{5 + 0} = \frac{2}{5} > 0$.
- The first factor $n$ diverges to $+\infty$.

A product of a sequence diverging to $+\infty$ and a sequence converging to a positive limit $\frac{2}{5} > 0$ diverges to $+\infty$:
$$\lim_{n\to\infty}\frac{2n^3 - n}{5n^2 + 1} = +\infty.$$

---

### Part 3: Comparison and General Observation
Comparing the two limits (together with Exercise 1):
1. In $\frac{3n+1}{n^2+4}$, the denominator ($n^2$) grows much faster than the numerator ($3n$), pulling the quotient down to $0$.
2. In $\frac{2n^3-n}{5n^2+1}$, the numerator ($2n^3$) grows an order of magnitude faster than the denominator ($5n^2$), causing the quotient to grow without bound ($+\infty$).

**General Rule for Rational Sequences $\lim_{n\to\infty}\frac{a_p n^p + \dots + a_0}{b_q n^q + \dots + b_0}$ ($a_p, b_q \neq 0$):**
$$\lim_{n\to\infty}\frac{P(n)}{Q(n)} = \begin{cases} 0 & \text{if } \deg P < \deg Q \quad (p < q), \\[6pt] \dfrac{a_p}{b_q} & \text{if } \deg P = \deg Q \quad (p = q), \\[8pt] +\infty \text{ (if } \frac{a_p}{b_q} > 0\text{) or } -\infty \text{ (if } \frac{a_p}{b_q} < 0\text{)} & \text{if } \deg P > \deg Q \quad (p > q). \end{cases}$$

## 4. Verification and Consistency Checks
1. **Asymptotic Equivalence Check:**
   - For the first sequence: $a_n = \frac{3n+1}{n^2+4} \sim \frac{3n}{n^2} = \frac{3}{n} \to 0$. At $n = 1000$, $a_{1000} = \frac{3001}{1000004} \approx 0.00300$, matching $\frac{3}{1000} = 0.003$.
   - For the second sequence: $b_n = \frac{2n^3-n}{5n^2+1} \sim \frac{2n^3}{5n^2} = 0.4n \to +\infty$. At $n = 1000$, $b_{1000} = \frac{1999999000}{5000001} \approx 399.9997$, matching $0.4(1000) = 400$.
2. **Squeeze / Inequality Verification for Part 2:**
   For all $n \ge 1$, $2n^3 - n \ge n^3$ and $5n^2 + 1 \le 6n^2$, so $\frac{2n^3-n}{5n^2+1} \ge \frac{n^3}{6n^2} = \frac{n}{6} \to +\infty$, rigorously confirming divergence to $+\infty$.
