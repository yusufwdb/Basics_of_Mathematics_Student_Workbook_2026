# Exercise 12: A Function with an Absolute Value

## 1. Problem Statement
Analyze
$$f(x)=|x^2-4|.$$
First sketch $x^2-4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

---

## 2. Theoretical Background and Concepts
- **Piecewise Definition of the Absolute Value of a Function:** For any function $g(x)$,
  $$|g(x)| = \begin{cases} g(x), & \text{if } g(x) \ge 0, \\ -g(x), & \text{if } g(x) < 0. \end{cases}$$
- **Geometric Effect of the Absolute Value:** Taking $f(x) = |g(x)|$ leaves the portions of the graph of $g(x)$ that lie on or above the $x$-axis ($g(x) \ge 0$) unchanged, and **reflects across the $x$-axis** the portions of the graph that lie below the $x$-axis ($g(x) < 0$).
- **Non-Differentiability at Simple Zeros of $g(x)$:** If $g(x_0) = 0$ and $g'(x_0) \neq 0$, then reflecting $g(x)$ across the $x$-axis flips the sign of the slope on one side of $x_0$, so the one-sided derivatives of $|g(x)|$ at $x_0$ are $\pm g'(x_0)$ (opposite non-zero numbers), producing a **sharp corner (cusp/kink)** where the derivative does not exist.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Sketch and analyze the inner parabola $g(x) = x^2 - 4$
The inner function $g(x) = x^2 - 4 = (x - 2)(x + 2)$ is an upward-opening parabola with:
- **Vertex (global minimum):** $(0, -4)$
- **$x$-intercepts (zeros):** $x = -2$ and $x = 2$
- **Sign:**
  - $g(x) \ge 0$ on $(-\infty, -2] \cup [2, \infty)$
  - $g(x) < 0$ on $(-2, 2)$

### Step 2: Piecewise formula and geometric effect of the absolute value
Applying the definition of absolute value to $g(x) = x^2 - 4$:
$$f(x) = |x^2 - 4| = \begin{cases} x^2 - 4, & \text{for } x \in (-\infty, -2] \cup [2, \infty), \\ 4 - x^2, & \text{for } x \in (-2, 2). \end{cases}$$

**Geometric effect:**
- For $x \le -2$ and $x \ge 2$, the parabola $y = x^2 - 4$ is already on or above the $x$-axis, so its graph remains unchanged.
- For $-2 < x < 2$, the valley of the parabola $y = x^2 - 4$ (which dipped down to $(0, -4)$ below the $x$-axis) is **reflected upward across the $x$-axis** into the arch $y = 4 - x^2$ with peak at $(0, 4)$.

```
       y = x^2 - 4 (Before |.|)                 f(x) = |x^2 - 4| (After |.|)
                 y                                           y
                 ^                                           ^
               4 | .           .                           4 | .     * (0,4)     .
                 |  .         .                              |  .  .   .        .
          -------+---*-------*---> x                  -------+---*-------*---> x
                 | -2 .     . 2                              | -2         2
              -4 |     * (0,-4)                              |  Sharp corners at (-2,0), (2,0)
```

### Step 3: Differentiability, One-Sided Derivatives, and Geometric Justification
On the open intervals where $x^2 - 4 \neq 0$, $f$ is differentiable:
$$f'(x) = \begin{cases} 2x, & \text{for } x \in (-\infty, -2) \cup (2, \infty), \\ -2x, & \text{for } x \in (-2, 2). \end{cases}$$
Let us examine the two boundary points **$x = -2$** and **$x = 2$** where $x^2 - 4 = 0$:
1. **At $x = 2$:**
   - Left-hand derivative: $f'_-(2) = \lim_{x \to 2^-} (-2x) = -4$
   - Right-hand derivative: $f'_+(2) = \lim_{x \to 2^+} (2x) = +4$
   Since $f'_-(2) = -4 \neq +4 = f'_+(2)$, **$f'(2)$ does not exist**.
2. **At $x = -2$:**
   - Left-hand derivative: $f'_-(-2) = \lim_{x \to -2^-} (2x) = -4$
   - Right-hand derivative: $f'_+(-2) = \lim_{x \to -2^+} (-2x) = +4$
   Since $f'_-(-2) = -4 \neq +4 = f'_+(-2)$, **$f'(-2)$ does not exist**.

**Geometric Justification:** The original parabola $y = x^2 - 4$ crosses the $x$-axis at $(-2, 0)$ and $(2, 0)$ transversely with non-zero slopes $\mp 4$. When the portion below the $x$-axis is folded upward across the $x$-axis, the tangent ray from inside $(-2, 2)$ is reflected so its slope flips sign (from $-4$ to $+4$ at $x = -2$, and from $+4$ to $-4$ at $x = 2$). Consequently, the graph has **sharp V-shaped corners** at $(-2, 0)$ and $(2, 0)$ with two distinct one-sided tangent lines (slopes $-4$ and $+4$) rather than a single smooth tangent line.

### Step 4: Summary of Monotonicity and Extrema of $f(x) = |x^2 - 4|$
| Interval / Point | $(-\infty, -2)$ | $x = -2$ | $(-2, 0)$ | $x = 0$ | $(0, 2)$ | $x = 2$ | $(2, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$f'(x)$** | $2x < 0$ ($-$) | DNE (corner) | $-2x > 0$ ($+$) | $0$ | $-2x < 0$ ($-$) | DNE (corner) | $2x > 0$ ($+$) |
| **Behavior of $f$** | $\searrow$ | **Global Min** ($0$) | $\nearrow$ | **Local Max** ($4$) | $\searrow$ | **Global Min** ($0$) | $\nearrow$ |

- **Strictly decreasing:** on $(-\infty, -2]$ and $[0, 2]$.
- **Strictly increasing:** on $[-2, 0]$ and $[2, \infty)$.
- **Local (and Global) Minima:** $f(-2) = 0$ and $f(2) = 0$ — occurring at the **non-differentiable corner points** $x = \pm 2$!
- **Local Maximum:** $f(0) = 4$ — occurring at the smooth stationary point $x = 0$ where $f'(0) = 0$.

---

## 4. Verification and Consistency Checks

### Important Lesson on Critical Points
A critical point of $f$ is defined as a point in $D_f$ where **either $f'(x) = 0$ or $f'(x)$ does not exist**. Here:
- $f'(x) = 0$ finds only the local maximum at $x = 0$.
- The two global minima at $x = -2$ and $x = 2$ occur where $f'(x)$ does not exist! Since $|x^2 - 4| \ge 0$ for all $x \in \mathbb{R}$ and equals $0$ at $x = \pm 2$, this confirms that ignoring points of non-differentiability would miss both global minima of the function.
