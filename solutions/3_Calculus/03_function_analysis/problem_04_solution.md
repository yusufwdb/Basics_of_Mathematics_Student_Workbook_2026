# Exercise 4: A Function with Two Vertical Asymptotes

## 1. Problem Statement
Analyze
$$f(x)=\frac1{x^2-1}.$$
Determine the domain, asymptotes, sign, and monotonicity on the intervals of the domain. Explain why each interval must be analyzed separately.

---

## 2. Theoretical Background and Concepts
- **Domain and Disjoint Connected Components:** When a rational function's denominator vanishes at $k$ distinct points, the real line is partitioned into $k + 1$ disjoint open intervals.
- **Why Each Interval Must Be Analyzed Separately:**
  1. **Mean Value Theorem Requirement:** The theorem linking the sign of $f'(x)$ to monotonicity ($f' > 0 \implies f$ strictly increasing) relies on the **Mean Value Theorem** ($f(b) - f(a) = f'(c)(b - a)$), which holds *only when $f$ is continuous on the closed interval $[a, b]$ and differentiable on $(a, b)$*.
  2. **Infinite Jumps at Vertical Asymptotes:** If $x_1$ and $x_2$ lie in different intervals separated by a vertical asymptote (where $f$ is undefined and jumps between $-\infty$ and $+\infty$), the Mean Value Theorem does not apply between $x_1$ and $x_2$, so monotonicity cannot be extended across the asymptote.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain and Symmetry
The denominator vanishes when:
$$x^2 - 1 = (x - 1)(x + 1) = 0 \iff x = -1 \quad \text{or} \quad x = 1$$
Thus the domain consists of **three disjoint open intervals**:
$$D_f = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)$$
Notice also that $f(-x) = \frac{1}{(-x)^2 - 1} = \frac{1}{x^2 - 1} = f(x)$, so $f$ is an **even function** (symmetric about the $y$-axis).

### Step 2: Sign of $f(x)$ on Each Interval
Since the numerator is $1 > 0$, the sign of $f(x)$ matches the sign of the quadratic $x^2 - 1 = (x + 1)(x - 1)$:
- On $(-\infty, -1)$: $x^2 - 1 > 0 \implies f(x) > 0$ (strictly positive).
- On $(-1, 1)$: $x^2 - 1 < 0 \implies f(x) < 0$ (strictly negative; $y$-intercept is $f(0) = -1$).
- On $(1, \infty)$: $x^2 - 1 > 0 \implies f(x) > 0$ (strictly positive).
- $f(x)$ has **no zeros** ($1 \neq 0$).

### Step 3: Asymptotes
1. **Vertical Asymptotes at $x = -1$ and $x = 1$:**
   Using the sign of $x^2 - 1$ on each interval:
   - At $x = -1$:
     $$\lim_{x \to -1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty, \qquad \lim_{x \to -1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty$$
   - At $x = 1$:
     $$\lim_{x \to 1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty, \qquad \lim_{x \to 1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty$$
   Thus, **$x = -1$ and $x = 1$ are two-sided vertical asymptotes**.
2. **Horizontal Asymptote as $x \to \pm\infty$:**
   $$\lim_{x \to \pm\infty} \frac{1}{x^2 - 1} = 0$$
   Thus, **$y = 0$ (the $x$-axis) is a horizontal asymptote** at both $-\infty$ and $+\infty$.

### Step 4: Derivative, Monotonicity, and Extrema
Writing $f(x) = (x^2 - 1)^{-1}$ and applying the chain rule for $x \neq \pm 1$:
$$f'(x) = -1(x^2 - 1)^{-2} \cdot (2x) = \frac{-2x}{(x^2 - 1)^2}$$
Setting $f'(x) = 0$ gives $x = 0 \in (-1, 1)$. Since $(x^2 - 1)^2 > 0$ on all three intervals of $D_f$, the sign of $f'(x)$ is determined solely by $-2x$:

| Interval / Point | $(-\infty, -1)$ | $x = -1$ | $(-1, 0)$ | $x = 0$ | $(0, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f(x)$** | $+$ | undef. | $-$ | $-1$ | $-$ | undef. | $+$ |
| **Sign of $f'(x)$** | $+$ | undef. | $+$ | $0$ | $-$ | undef. | $-$ |
| **Behavior of $f(x)$** | $\nearrow$ ($0$ to $+\infty$) | V.A. | $\nearrow$ ($-\infty$ to $-1$) | **Local Max** | $\searrow$ ($-1$ to $-\infty$) | V.A. | $\searrow$ ($+\infty$ to $0$) |

- **Strictly increasing** on $(-\infty, -1)$ and on $(-1, 0]$ (analyzed separately!).
- **Strictly decreasing** on $[0, 1)$ and on $(1, \infty)$ (analyzed separately!).
- **Local maximum:** At $x = 0$, $f'(x)$ changes sign from $+$ to $-$, giving a local maximum of $f(0) = -1$.

### Step 5: Why Each Interval Must Be Analyzed Separately
Look at the two intervals $(-\infty, -1)$ and $(-1, 0]$: on both intervals $f'(x) > 0$, so $f$ is strictly increasing on $(-\infty, -1)$ and strictly increasing on $(-1, 0]$. However, $f$ is **not** increasing on $(-\infty, -1) \cup (-1, 0]$! For example, $-2 < -0.5$, yet:
$$f(-2) = \frac{1}{3} > -\frac{4}{3} = f(-0.5)$$
Because of the infinite discontinuity at the vertical asymptote $x = -1$ (where $f$ jumps from $+\infty$ to $-\infty$), monotonicity holds only within each individual connected interval of the domain.

---

## 4. Verification and Consistency Checks

### Elementary Inequality Check of Monotonicity
Without derivatives:
- On $(0, 1)$, if $0 \le x_1 < x_2 < 1$, then $-1 \le x_1^2 - 1 < x_2^2 - 1 < 0$. Taking reciprocals of two negative numbers reverses the inequality: $\frac{1}{x_1^2-1} > \frac{1}{x_2^2-1}$, confirming $f$ is decreasing on $[0, 1)$ with maximum $f(0) = -1$ on $(-1, 1)$.
- On $(1, \infty)$, if $1 < x_1 < x_2$, then $0 < x_1^2 - 1 < x_2^2 - 1$, so $\frac{1}{x_1^2-1} > \frac{1}{x_2^2-1} > 0$, confirming $f$ is positive and decreasing on $(1, \infty)$. By even symmetry, the mirror behavior holds on $(-\infty, -1)$ and $(-1, 0]$.
