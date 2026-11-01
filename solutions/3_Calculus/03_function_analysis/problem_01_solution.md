# Exercise 1: A Cubic Polynomial

## 1. Problem Statement
Analyze the monotonicity and extrema of
$$f(x)=x^3-3x^2+2.$$
Sketch the graph based on the results and mark the critical points.

---

## 2. Theoretical Background and Concepts
- **Critical (Stationary) Points:** For a differentiable function $f: \mathbb{R} \to \mathbb{R}$, critical points are the solutions to $f'(x) = 0$. By **Fermat's Theorem**, any local extremum of a differentiable function on an open interval must occur at a critical point.
- **Monotonicity Criterion:** Let $f$ be continuous on an interval $I$ and differentiable on the interior of $I$:
  - If $f'(x) > 0$ for all $x \in \text{int}(I)$, then $f$ is strictly **increasing** on $I$.
  - If $f'(x) < 0$ for all $x \in \text{int}(I)$, then $f$ is strictly **decreasing** on $I$.
- **First Derivative Test for Local Extrema:** At a critical point $x_0$ where $f'(x_0) = 0$:
  - If $f'(x)$ changes sign from $+$ to $-$ as $x$ passes through $x_0$ from left to right, $f$ has a **strict local maximum** at $x_0$.
  - If $f'(x)$ changes sign from $-$ to $+$ as $x$ passes through $x_0$ from left to right, $f$ has a **strict local minimum** at $x_0$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain and First Derivative
Since $f(x) = x^3 - 3x^2 + 2$ is a polynomial, its domain is $D_f = \mathbb{R}$ and it is differentiable everywhere.
Differentiating $f(x)$ term by term:
$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

### Step 2: Critical Points and Sign Table of $f'(x)$
Setting $f'(x) = 0$:
$$3x(x - 2) = 0 \iff x = 0 \quad \text{or} \quad x = 2$$
Since $f'(x) = 3x(x - 2)$ is a quadratic with positive leading coefficient ($a = 3 > 0$) and roots at $x = 0$ and $x = 2$, $f'(x)$ is positive outside the roots and negative between them:

| Interval / Point | $(-\infty, 0)$ | $x = 0$ | $(0, 2)$ | $x = 2$ | $(2, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Sign of $3x$ | $-$ | $0$ | $+$ | $+$ | $+$ |
| Sign of $(x - 2)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| **Sign of $f'(x)$** | **$+$** | **$0$** | **$-$** | **$0$** | **$+$** |
| **Behavior of $f(x)$** | Strictly increasing $\nearrow$ | **Local max** ($2$) | Strictly decreasing $\searrow$ | **Local min** ($-2$) | Strictly increasing $\nearrow$ |

### Step 3: Monotonicity and Local Extrema
1. **Intervals of Monotonicity:**
   - $f$ is **strictly increasing** on $(-\infty, 0]$ and on $[2, \infty)$.
   - $f$ is **strictly decreasing** on $[0, 2]$.
2. **Local Extrema (Critical Points):**
   - At $x = 0$, $f'(x)$ changes sign from $+$ to $-$, so $f$ attains a **local maximum** of:
     $$f(0) = 0^3 - 3(0)^2 + 2 = 2 \qquad \longrightarrow \qquad P_{\max} = (0, 2)$$
   - At $x = 2$, $f'(x)$ changes sign from $-$ to $+$, so $f$ attains a **local minimum** of:
     $$f(2) = 2^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2 \qquad \longrightarrow \qquad P_{\min} = (2, -2)$$

### Step 4: Additional Features and Graph Sketch
- **Zeros ($x$-intercepts):** Notice $f(1) = 1 - 3 + 2 = 0$. Factoring $x^3 - 3x^2 + 2 = (x - 1)(x^2 - 2x - 2) = 0$ gives three real roots:
  $$x_1 = 1 - \sqrt{3} \approx -0.73, \qquad x_2 = 1, \qquad x_3 = 1 + \sqrt{3} \approx 2.73$$
- **End behavior:** $\lim_{x \to -\infty} f(x) = -\infty$ and $\lim_{x \to +\infty} f(x) = +\infty$.
- **Inflection point:** $f''(x) = 6x - 6 = 0 \implies x = 1$, with $f(1) = 0$.

```
          y
          ^
        3 |       (0, 2) [Local Max]
        2 |---------*---------
        1 |      .     .
   -------+----*----+----*----+---> x
       -1 |  .      1      .  3
       -1 |.                 .
       -2 |         * (2, -2) [Local Min]
       -3 |
```
*Description of the graph:* Starting from $-\infty$ in the third quadrant, the curve crosses the $x$-axis at $x = 1-\sqrt{3} \approx -0.73$, rises to its **local maximum at $(0, 2)$** on the $y$-axis, turns downward and passes through its inflection point and $x$-intercept at $(1, 0)$, reaches its **local minimum at $(2, -2)$**, and then rises to $+\infty$, crossing the $x$-axis again at $x = 1+\sqrt{3} \approx 2.73$.

---

## 4. Verification and Consistency Checks

### Second Derivative Test and Point Symmetry Check
1. **Second Derivative Test:**
   $$f''(x) = 6x - 6$$
   - At $x = 0$: $f''(0) = -6 < 0 \implies$ strict local maximum at $(0, 2)$.
   - At $x = 2$: $f''(2) = 6(2) - 6 = 6 > 0 \implies$ strict local minimum at $(2, -2)$.
2. **Cubic Symmetry Around the Inflection Point $(1, 0)$:**
   Every cubic polynomial is point-symmetric about its inflection point $(1, 0)$. The critical points $x = 0$ and $x = 2$ are symmetric about $x = 1$ ($1 - 1 = 0$ and $1 + 1 = 2$), and their values $f(0) = +2$ and $f(2) = -2$ are opposite in sign and equidistant from $f(1) = 0$.
