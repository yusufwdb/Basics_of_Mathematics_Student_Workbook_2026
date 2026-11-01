# Exercise 14: Reconstructing Information from the Derivative

## 1. Problem Statement
It is known that
$$f'(x)=(x-1)(x+2).$$
Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for
$$g(x)=\frac{x^3}{3}+\frac{x^2}{2}-2x$$
verify that $g'(x)=(x-1)(x+2)$, and compare the specific graph with the earlier qualitative sketch.

---

## 2. Theoretical Background and Concepts
- **Reading Function Behavior Directly from $f'(x)$:**
  - The zeros of $f'(x)$ give the **$x$-coordinates of the critical points**.
  - The intervals where $f'(x) > 0$ or $f'(x) < 0$ determine the **intervals of monotonicity** of $f(x)$.
  - The sign changes of $f'(x)$ determine whether each critical point is a **local maximum** ($+ \to -$) or **local minimum** ($- \to +$).
  - The derivative of $f'(x)$, namely $f''(x)$, gives the **concavity/convexity** and **inflection point** of $f(x)$.
- **Ambiguity Up to a Vertical Shift ($+C$):** Knowing $f'(x)$ determines $f(x)$ uniquely **up to an additive constant $C \in \mathbb{R}$**: if $g'(x) = f'(x)$ on $\mathbb{R}$, then $f(x) = g(x) + C$. Thus the *qualitative shape*, monotonicity intervals, $x$-coordinates of extrema, and vertical distance $f(x_{\max}) - f(x_{\min})$ are completely fixed by $f'(x)$, while the vertical position relative to the $x$-axis depends on $C$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Determine Monotonicity and Locations of Extrema from $f'(x) = (x - 1)(x + 2)$
The derivative $f'(x) = (x - 1)(x + 2) = x^2 + x - 2$ is defined for all $x \in \mathbb{R}$ and is an upward-opening parabola with zeros at:
$$f'(x) = 0 \iff (x - 1)(x + 2) = 0 \iff x = -2 \quad \text{or} \quad x = 1$$

| Interval / Point | $(-\infty, -2)$ | $x = -2$ | $(-2, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Sign of $(x + 2)$ | $-$ | $0$ | $+$ | $+$ | $+$ |
| Sign of $(x - 1)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| **Sign of $f'(x)$** | **$+$** | **$0$** | **$-$** | **$0$** | **$+$** |
| **Behavior of $f(x)$** | Strictly increasing $\nearrow$ | **Local Maximum** | Strictly decreasing $\searrow$ | **Local Minimum** | Strictly increasing $\nearrow$ |

From the sign table alone (without knowing a formula for $f(x)$), we deduce:
1. **Monotonicity:**
   - $f$ is **strictly increasing** on $(-\infty, -2]$ and on $[1, \infty)$.
   - $f$ is **strictly decreasing** on $[-2, 1]$.
2. **Locations of Extrema:**
   - $f$ has a **strict local maximum at $x = -2$** (since $f'$ changes sign from $+$ to $-$).
   - $f$ has a **strict local minimum at $x = 1$** (since $f'$ changes sign from $-$ to $+$).
3. **Curvature:** Since $f''(x) = \frac{d}{dx}(x^2 + x - 2) = 2x + 1$, $f$ is concave down on $\left(-\infty, -\frac{1}{2}\right]$, convex on $\left[-\frac{1}{2}, \infty\right)$, and has an inflection point at $x = -\frac{1}{2}$.

### Step 2: Qualitative Sketch of Any Antiderivative $f(x)$
Any function $f(x)$ with $f'(x) = (x-1)(x+2)$ is an S-shaped cubic curve that rises from $-\infty$ to a peak at $x = -2$, falls through an inflection point at $x = -0.5$ to a valley at $x = 1$, and then rises to $+\infty$:
```
          y
          ^
          |      * (x = -2, Local Max)        .
          |    .   .                         .
          |   .     o (x = -0.5, I.P.)      .
   -------+--+-------+-------+-------------+---> x
          | . -2    -0.5     1            .
          |.                  * (x = 1, Local Min)
```

### Step 3: Verify $g'(x) = (x - 1)(x + 2)$ for $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$
Differentiating $g(x)$ term by term using the power rule:
$$g'(x) = \frac{d}{dx}\left(\frac{x^3}{3}\right) + \frac{d}{dx}\left(\frac{x^2}{2}\right) - \frac{d}{dx}(2x) = \frac{3x^2}{3} + \frac{2x}{2} - 2 = x^2 + x - 2$$
Factoring the quadratic $x^2 + x - 2$:
$$g'(x) = (x - 1)(x + 2)$$
which matches $f'(x)$ identically!

### Step 4: Compute Exact Values for $g(x)$ and Compare with the Qualitative Sketch
Evaluating $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$ at the key points identified in Step 1:
- **Local maximum at $x = -2$:**
  $$g(-2) = \frac{(-2)^3}{3} + \frac{(-2)^2}{2} - 2(-2) = -\frac{8}{3} + 2 + 4 = \frac{10}{3} \approx 3.33 \implies \left(-2, \frac{10}{3}\right)$$
- **Inflection point at $x = -\frac{1}{2}$:**
  $$g\left(-\frac{1}{2}\right) = \frac{-1/8}{3} + \frac{1/4}{2} - 2\left(-\frac{1}{2}\right) = -\frac{1}{24} + \frac{3}{24} + 1 = \frac{13}{12} \approx 1.08 \implies \left(-\frac{1}{2}, \frac{13}{12}\right)$$
- **Origin / $y$-intercept at $x = 0$:**
  $$g(0) = 0 \implies (0, 0)$$
- **Local minimum at $x = 1$:**
  $$g(1) = \frac{1}{3} + \frac{1}{2} - 2 = -\frac{7}{6} \approx -1.17 \implies \left(1, -\frac{7}{6}\right)$$

**Comparison:** The specific function $g(x)$ has the **exact same qualitative shape**, intervals of monotonicity, $x$-coordinates of extrema ($x = -2$ and $x = 1$), and inflection point ($x = -1/2$) predicted from $f'(x)$, and fixes the vertical position of the curve by anchoring it through $(0, 0)$ (setting the integration constant $C = 0$).

---

## 4. Verification and Consistency Checks

### Fundamental Theorem of Calculus Check on the Vertical Drop
The total drop in function value from the local maximum at $x = -2$ to the local minimum at $x = 1$ is:
$$g(1) - g(-2) = -\frac{7}{6} - \frac{10}{3} = -\frac{7}{6} - \frac{20}{6} = -\frac{27}{6} = -\frac{9}{2} = -4.5$$
This matches the standard cubic integral formula $\int_{\alpha}^{\beta} (x - \alpha)(x - \beta)\,dx = -\frac{1}{6}(\beta - \alpha)^3 = -\frac{1}{6}(1 - (-2))^3 = -\frac{27}{6} = -\frac{9}{2}$, confirming all function evaluations.
