# Exercise 10: Complete Function Analysis

## 1. Problem Statement
Perform a complete analysis of
$$f(x)=\frac{x}{x^2+1}.$$
Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

---

## 2. Theoretical Background and Concepts
A complete calculus analysis of a real function $f$ systematically combines:
1. **Domain and Continuity:** Where $f(x)$ is defined and continuous.
2. **Symmetry (Parity):** Whether $f(-x) = f(x)$ (even) or $f(-x) = -f(x)$ (odd).
3. **Intercepts and Sign:** Solutions to $f(x) = 0$, $f(0)$, and the sign of $f(x)$.
4. **Limits and Asymptotes:** Behavior at boundary points of $D_f$ and as $x \to \pm\infty$.
5. **First Derivative ($f'$):** Critical points ($f'(x) = 0$), intervals of monotonicity, and local/global extrema.
6. **Second Derivative ($f''$):** Intervals of convexity ($f'' > 0$) and concavity ($f'' < 0$), and inflection points ($f''(x) = 0$ with sign change).

---

## 3. Detailed Step-by-Step Solution

### 1. Domain
Since $x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$, the denominator never vanishes:
$$D_f = \mathbb{R} = (-\infty, \infty)$$
and $f$ is smooth ($C^\infty$) everywhere on $\mathbb{R}$.

### 2. Symmetry (Parity)
For any $x \in \mathbb{R}$:
$$f(-x) = \frac{-x}{(-x)^2 + 1} = -\frac{x}{x^2 + 1} = -f(x)$$
Therefore, $f$ is an **odd function**, and its graph is symmetric with respect to the origin $(0, 0)$.

### 3. Zeros and Sign of $f(x)$
- **Zero / Intercept:** $f(x) = 0 \iff x = 0$, so the graph passes through the origin $(0, 0)$.
- **Sign:** Since $x^2 + 1 > 0$, $f(x) < 0$ for $x \in (-\infty, 0)$ and $f(x) > 0$ for $x \in (0, \infty)$.

### 4. Limits and Asymptotes
- **Vertical asymptotes:** None, since $D_f = \mathbb{R}$ and $f$ is continuous everywhere.
- **Limits at $\pm\infty$ (Horizontal Asymptote):**
  $$\lim_{x \to \pm\infty} \frac{x}{x^2 + 1} = \lim_{x \to \pm\infty} \frac{\frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{0}{1 + 0} = 0$$
  Thus, **$y = 0$ (the $x$-axis) is a two-sided horizontal asymptote** (approached from above as $x \to +\infty$ and from below as $x \to -\infty$).

### 5. First Derivative, Monotonicity, and Extrema
Applying the quotient rule:
$$f'(x) = \frac{(1)(x^2 + 1) - x(2x)}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2} = \frac{(1 - x)(1 + x)}{(x^2 + 1)^2}$$
Setting $f'(x) = 0$ gives two critical points:
$$1 - x^2 = 0 \iff x = -1 \quad \text{or} \quad x = 1$$

| Interval / Point | $(-\infty, -1)$ | $x = -1$ | $(-1, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f'(x)$** | $-$ | $0$ | $+$ | $0$ | $-$ |
| **Behavior of $f(x)$** | Decreasing $\searrow$ | **Global Min** $\left(-\frac{1}{2}\right)$ | Increasing $\nearrow$ | **Global Max** $\left(\frac{1}{2}\right)$ | Decreasing $\searrow$ |

- **Strictly decreasing:** on $(-\infty, -1]$ and on $[1, \infty)$.
- **Strictly increasing:** on $[-1, 1]$.
- **Local and Global Minimum:** $f(-1) = -\frac{1}{2}$ at $\left(-1, -\frac{1}{2}\right)$.
- **Local and Global Maximum:** $f(1) = \frac{1}{2}$ at $\left(1, \frac{1}{2}\right)$.

### 6. Second Derivative, Convexity, and Inflection Points
Differentiating $f'(x) = \frac{1 - x^2}{(x^2 + 1)^2}$ via the quotient rule:
$$f''(x) = \frac{(-2x)(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1)(2x)}{(x^2 + 1)^4}$$
Factoring out $2x(x^2 + 1)$ and canceling $(x^2 + 1)$:
$$f''(x) = \frac{2x\big[-(x^2 + 1) - 2(1 - x^2)\big]}{(x^2 + 1)^3} = \frac{2x(x^2 - 3)}{(x^2 + 1)^3} = \frac{2x\left(x + \sqrt{3}\right)\left(x - \sqrt{3}\right)}{(x^2 + 1)^3}$$

Setting $f''(x) = 0$ gives three roots where $f''(x)$ changes sign:
$$x_1 = -\sqrt{3} \approx -1.73, \qquad x_2 = 0, \qquad x_3 = \sqrt{3} \approx 1.73$$

| Interval / Point | $\left(-\infty, -\sqrt{3}\right)$ | $x = -\sqrt{3}$ | $\left(-\sqrt{3}, 0\right)$ | $x = 0$ | $\left(0, \sqrt{3}\right)$ | $x = \sqrt{3}$ | $\left(\sqrt{3}, \infty\right)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f''(x)$** | $-$ | $0$ | $+$ | $0$ | $-$ | $0$ | $+$ |
| **Curvature of $f$** | Concave ($\cap$) | **I.P.** | Convex ($\cup$) | **I.P.** | Concave ($\cap$) | **I.P.** | Convex ($\cup$) |

- **Concave (concave down, $\cap$):** on $\left(-\infty, -\sqrt{3}\right]$ and $\left[0, \sqrt{3}\right]$.
- **Convex (concave up, $\cup$):** on $\left[-\sqrt{3}, 0\right]$ and $\left[\sqrt{3}, \infty\right)$.
- **Three Inflection Points:**
  $$I_1 = \left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right), \qquad I_2 = (0, 0), \qquad I_3 = \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$$

### 7. Graph Sketch
```
            y
            ^
        1/2 |                       * (1, 1/2) [Max]
            |                    .     .   o (sqrt(3), sqrt(3)/4) [I.P.]
            |                  .            . . .
   ---------+----.---.---o---*-------------------> x (y = 0 Asymptote)
            |  . . .   .   (0,0) [I.P.]
            |    (-sqrt(3), -sqrt(3)/4) [I.P.]
       -1/2 |          * (-1, -1/2) [Min]
```

---

## 4. Verification and Consistency Checks

### Elementary AM-GM / Completing the Square Bound Check
For any $x \in \mathbb{R}$, $(|x| - 1)^2 \ge 0 \iff x^2 + 1 \ge 2|x| \iff \left|\frac{x}{x^2+1}\right| \le \frac{1}{2}$, with equality if and only if $|x| = 1 \iff x = \pm 1$. This algebraically confirms that the range of $f$ is $\left[-\frac{1}{2}, \frac{1}{2}\right]$ with global minimum $-\frac{1}{2}$ at $x = -1$ and global maximum $+\frac{1}{2}$ at $x = 1$.
