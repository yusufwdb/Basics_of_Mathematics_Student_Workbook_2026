# Exercise 8: The Second Derivative

## 1. Problem Statement
For
$$f(x)=x^4-4x^2$$
find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

---

## 2. Theoretical Background and Concepts
- **Convexity and Concavity via the Second Derivative:** Let $f$ be twice differentiable on an open interval $I$:
  - If $f''(x) > 0$ on $I$, then $f'(x)$ is strictly increasing on $I$, and $f$ is **convex (concave up, $\cup$)** on $I$.
  - If $f''(x) < 0$ on $I$, then $f'(x)$ is strictly decreasing on $I$, and $f$ is **concave (concave down, $\cap$)** on $I$.
- **Inflection Point:** A point $(x_0, f(x_0))$ on the graph of a continuous function $f$ at which $f$ changes from convex to concave (or vice versa), i.e., $f''(x)$ changes sign across $x_0$. For a twice differentiable function, any inflection point satisfies $f''(x_0) = 0$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain, Symmetry, and Intercepts
- **Domain:** $D_f = \mathbb{R}$ (quartic polynomial).
- **Symmetry:** $f(-x) = (-x)^4 - 4(-x)^2 = x^4 - 4x^2 = f(x)$, so $f$ is an **even function** (symmetric about the $y$-axis).
- **Zeros:** $f(x) = x^2(x^2 - 4) = x^2(x - 2)(x + 2) = 0 \implies x = -2, 0, 2$ (with $x = 0$ a double root).

### Step 2: First Derivative, Monotonicity, and Local Extrema
Differentiating $f(x) = x^4 - 4x^2$:
$$f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 4x\left(x + \sqrt{2}\right)\left(x - \sqrt{2}\right)$$
Setting $f'(x) = 0$ yields three critical points:
$$x_1 = -\sqrt{2} \approx -1.41, \qquad x_2 = 0, \qquad x_3 = \sqrt{2} \approx 1.41$$

| Interval / Point | $\left(-\infty, -\sqrt{2}\right)$ | $x = -\sqrt{2}$ | $\left(-\sqrt{2}, 0\right)$ | $x = 0$ | $\left(0, \sqrt{2}\right)$ | $x = \sqrt{2}$ | $\left(\sqrt{2}, \infty\right)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f'(x)$** | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| **Behavior of $f(x)$** | $\searrow$ | **Local Min** ($-4$) | $\nearrow$ | **Local Max** ($0$) | $\searrow$ | **Local Min** ($-4$) | $\nearrow$ |

Evaluating $f$ at the critical points:
- $f\left(\pm\sqrt{2}\right) = \left(\pm\sqrt{2}\right)^4 - 4\left(\pm\sqrt{2}\right)^2 = 4 - 8 = -4$
- $f(0) = 0$

Thus:
- **Local (and Global) Minima:** $f\left(-\sqrt{2}\right) = -4$ at $\left(-\sqrt{2}, -4\right)$ and $f\left(\sqrt{2}\right) = -4$ at $\left(\sqrt{2}, -4\right)$.
- **Local Maximum:** $f(0) = 0$ at $(0, 0)$.

### Step 3: Second Derivative, Convexity/Concavity, and Inflection Points
Differentiating $f'(x) = 4x^3 - 8x$:
$$f''(x) = 12x^2 - 8 = 4(3x^2 - 2) = 12\left(x + \sqrt{\frac{2}{3}}\right)\left(x - \sqrt{\frac{2}{3}}\right)$$
Setting $f''(x) = 0$:
$$3x^2 - 2 = 0 \iff x^2 = \frac{2}{3} \iff x = \pm\sqrt{\frac{2}{3}} = \pm\frac{\sqrt{6}}{3} \approx \pm 0.82$$

| Interval / Point | $\left(-\infty, -\frac{\sqrt{6}}{3}\right)$ | $x = -\frac{\sqrt{6}}{3}$ | $\left(-\frac{\sqrt{6}}{3}, \frac{\sqrt{6}}{3}\right)$ | $x = \frac{\sqrt{6}}{3}$ | $\left(\frac{\sqrt{6}}{3}, \infty\right)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f''(x)$** | $+$ | $0$ | $-$ | $0$ | $+$ |
| **Curvature of $f$** | Convex ($\cup$) | **Inflection Point** | Concave ($\cap$) | **Inflection Point** | Convex ($\cup$) |

Evaluating $f$ at $x = \pm\sqrt{\frac{2}{3}}$:
$$f\left(\pm\sqrt{\frac{2}{3}}\right) = \left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) = \frac{4}{9} - \frac{24}{9} = -\frac{20}{9} \approx -2.22$$

Summary of curvature and inflection points:
- **Convex (concave up, $\cup$):** on $\left(-\infty, -\frac{\sqrt{6}}{3}\right]$ and $\left[\frac{\sqrt{6}}{3}, \infty\right)$.
- **Concave (concave down, $\cap$):** on $\left[-\frac{\sqrt{6}}{3}, \frac{\sqrt{6}}{3}\right]$.
- **Inflection Points:** $I_1 = \left(-\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$ and $I_2 = \left(\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$.

### Step 4: Graph Sketch (W-Shaped Symmetric Quartic)
```
          y
          ^
        2 |  .                                       .
        1 |   .                 (0,0)               .
          |    (-2,0)        [Local Max]         (2,0)
   -------+------*----------------*----------------*------> x
       -1 |       .            .     .            .
       -2 |        .        o           o        .   o = Inflection Points
       -3 |         .     .               .     .        (+/-0.82, -20/9)
       -4 |          * .                     . *
                (-sqrt(2), -4)           (sqrt(2), -4)
                 [Local Min]              [Local Min]
```

---

## 4. Verification and Consistency Checks

### Second Derivative Test at Critical Points and Completing the Square
1. **Second Derivative Test at Critical Points:**
   - $f''(0) = -8 < 0 \implies (0, 0)$ lies strictly inside the concave-down interval $\left(-\frac{\sqrt{6}}{3}, \frac{\sqrt{6}}{3}\right)$ and is a strict local maximum.
   - $f''\left(\pm\sqrt{2}\right) = 12(2) - 8 = 16 > 0 \implies \left(\pm\sqrt{2}, -4\right)$ lie strictly inside the convex intervals and are strict local minima.
2. **Completing the Square in $x^2$:**
   $$f(x) = x^4 - 4x^2 = (x^2 - 2)^2 - 4 \ge -4$$
   Since $(x^2 - 2)^2 \ge 0$ with equality if and only if $x^2 = 2 \iff x = \pm\sqrt{2}$, $-4$ is confirmed as the exact global minimum attained at $x = \pm\sqrt{2}$.
