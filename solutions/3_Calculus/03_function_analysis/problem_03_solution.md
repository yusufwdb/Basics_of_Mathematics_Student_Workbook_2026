# Exercise 3: A Rational Function

## 1. Problem Statement
Analyze the domain, zeros, asymptotes, and monotonicity of
$$f(x)=\frac{x+1}{x-2}.$$
Finally, sketch a graph consistent with all the information obtained.

---

## 2. Theoretical Background and Concepts
- **Homographic Function:** A rational function of the form $f(x) = \frac{ax+b}{cx+d}$ ($c \neq 0, ad - bc \neq 0$) whose graph is a rectangular hyperbola.
- **Vertical Asymptote:** The line $x = x_0$ is a vertical asymptote if $\lim_{x \to x_0^-} f(x) = \pm\infty$ or $\lim_{x \to x_0^+} f(x) = \pm\infty$.
- **Horizontal Asymptote:** The line $y = L$ is a horizontal asymptote as $x \to \pm\infty$ if $\lim_{x \to \pm\infty} f(x) = L$.
- **Monotonicity on Disjoint Intervals:** If $f'(x) < 0$ on $(-\infty, x_0)$ and on $(x_0, \infty)$, then $f$ is strictly decreasing on $(-\infty, x_0)$ and strictly decreasing on $(x_0, \infty)$ **separately** (not on their union, because $f$ jumps from $-\infty$ to $+\infty$ across $x = x_0$).

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain and Zeros (Intercepts)
1. **Domain:** The denominator cannot be zero:
   $$x - 2 \neq 0 \iff x \neq 2 \implies D_f = (-\infty, 2) \cup (2, \infty)$$
2. **Zeros ($x$-intercepts):** A fraction equals zero when its numerator is zero and its denominator is non-zero:
   $$f(x) = 0 \iff x + 1 = 0 \iff x = -1 \in D_f$$
   Thus the unique zero is at $(-1, 0)$.
3. **$y$-intercept:** Evaluating at $x = 0$:
   $$f(0) = \frac{0 + 1}{0 - 2} = -\frac{1}{2} \implies \left(0, -\frac{1}{2}\right)$$

### Step 2: Asymptotes
1. **Vertical asymptote at $x = 2$:**
   As $x \to 2$, the numerator approaches $2 + 1 = 3 > 0$, while the denominator $x - 2 \to 0$:
   - $\lim_{x \to 2^-} \frac{x+1}{x-2} = \left[\frac{3}{0^-}\right] = -\infty$
   - $\lim_{x \to 2^+} \frac{x+1}{x-2} = \left[\frac{3}{0^+}\right] = +\infty$
   Therefore, **$x = 2$ is a two-sided vertical asymptote**.
2. **Horizontal asymptote as $x \to \pm\infty$:**
   $$\lim_{x \to \pm\infty} \frac{x+1}{x-2} = \lim_{x \to \pm\infty} \frac{1 + \frac{1}{x}}{1 - \frac{2}{x}} = \frac{1 + 0}{1 - 0} = 1$$
   Therefore, **$y = 1$ is a horizontal asymptote** at both $-\infty$ and $+\infty$ (and there are no oblique asymptotes).

### Step 3: Derivative and Monotonicity
Applying the quotient rule for $x \neq 2$:
$$f'(x) = \frac{(1)(x - 2) - (x + 1)(1)}{(x - 2)^2} = \frac{x - 2 - x - 1}{(x - 2)^2} = \frac{-3}{(x - 2)^2}$$
Since $(x - 2)^2 > 0$ for all $x \neq 2$ and the numerator is $-3 < 0$, we have:
$$f'(x) < 0 \qquad \text{for all } x \in (-\infty, 2) \cup (2, \infty)$$

| Interval | $(-\infty, 2)$ | $x = 2$ | $(2, \infty)$ |
| :--- | :---: | :---: | :---: |
| **Sign of $f'(x)$** | $-$ | undefined | $-$ |
| **Behavior of $f(x)$** | Strictly decreasing ($1 \searrow -\infty$) | Vertical asymptote | Strictly decreasing ($+\infty \searrow 1$) |

- $f$ is **strictly decreasing on $(-\infty, 2)$** and **strictly decreasing on $(2, \infty)$**.
- $f$ has **no local extrema** (since $f'(x) \neq 0$ everywhere).

### Step 4: Graph Sketch
```
          y
          ^
        4 |             |  .
        3 |             |   .
        2 |             |     . (5, 2)
        1 | - - - - - - + - - - - . . . -> y = 1 (Horizontal Asymptote)
   . . .  |       (-1,0)|
   -------+------*------+-------------> x
          |    .  (0,-1/2)
       -1 |     .       |
       -2 |      .      |
       -3 |       .     |
                        x = 2 (Vertical Asymptote)
```
*Description of the graph:* A hyperbola with two branches separated by $x = 2$ and $y = 1$:
- **Left branch ($x < 2$):** Starts just below the horizontal asymptote $y = 1$ as $x \to -\infty$, decreases through $(-1, 0)$ and $(0, -1/2)$, and plunges to $-\infty$ along the left side of the vertical asymptote $x = 2$.
- **Right branch ($x > 2$):** Descends from $+\infty$ along the right side of $x = 2$, passes through $(3, 4)$ and $(5, 2)$, and approaches the horizontal asymptote $y = 1$ from above as $x \to +\infty$.

---

## 4. Verification and Consistency Checks

### Canonical Shifted Form Verification
Rewriting $f(x)$ by extracting the integer part:
$$f(x) = \frac{(x - 2) + 3}{x - 2} = 1 + \frac{3}{x - 2}$$
This shows that the graph of $f(x)$ is simply the standard hyperbola $y = \frac{3}{x}$ shifted $2$ units right and $1$ unit up:
- Center of symmetry (intersection of asymptotes): $(2, 1) \implies$ asymptotes $x = 2$ and $y = 1$.
- For $x < 2$, $\frac{3}{x-2} < 0 \implies f(x) < 1$ (left branch stays below $y = 1$).
- For $x > 2$, $\frac{3}{x-2} > 0 \implies f(x) > 1$ (right branch stays above $y = 1$).
- Differentiating $1 + 3(x-2)^{-1}$ directly gives $-3(x-2)^{-2}$, confirming our quotient rule result.
