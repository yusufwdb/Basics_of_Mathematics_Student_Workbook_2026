# Exercise 5: Hyperbola and Asymptotes

## 1. Problem Statement
For
$$\frac{x^2}{16}-\frac{y^2}{9}=1,$$
find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

## 2. Theoretical Background and Concepts
- **Canonical Equation of a Horizontal Hyperbola:**
  $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \quad (a > 0, \, b > 0).$$
- **Vertices and Axes:**
  - The center of symmetry is $(0,0)$.
  - The transverse (real) axis lies along the $x$-axis with semiaxis length $a$; the vertices ($x$-intercepts) are $(\pm a, 0)$.
  - The conjugate (imaginary) semiaxis length is $b$; the curve does not intersect the $y$-axis because setting $x=0$ yields $-\frac{y^2}{b^2} = 1$, which has no real solutions.
- **Asymptotes:** The two straight lines passing through the center with equations
  $$y = \pm \frac{b}{a}x$$
  form the diagonals of the central rectangle $[-a, a] \times [-b, b]$ and guide the branches of the hyperbola as $|x| \to \infty$.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify $a$ and $b$ and find the $x$-intercepts
Comparing $\frac{x^2}{16} - \frac{y^2}{9} = 1$ with $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
$$a^2 = 16 \implies a = 4, \qquad b^2 = 9 \implies b = 3.$$
To find the intercepts with the $x$-axis, set $y = 0$:
$$\frac{x^2}{16} - 0 = 1 \implies x^2 = 16 \implies x = \pm 4.$$
Thus, the **$x$-axis intercepts (vertices)** are:
$$V_1 = (-4, 0) \quad \text{and} \quad V_2 = (4, 0).$$

### Step 2: Find the equations of the asymptotes
Using the formula $y = \pm \frac{b}{a}x$ with $a = 4$ and $b = 3$:
$$y = \frac{3}{4}x \quad \text{and} \quad y = -\frac{3}{4}x.$$

### Step 3: Explain why the asymptotes describe the behavior far from the center
We can explain this in two complementary ways:

1. **Factoring / Algebraic Rearrangement:**
   Solve the hyperbola equation for $y^2$:
   $$\frac{y^2}{9} = \frac{x^2}{16} - 1 = \frac{x^2}{16}\left(1 - \frac{16}{x^2}\right) \implies y = \pm \frac{3}{4}x \sqrt{1 - \frac{16}{x^2}}.$$
   When $|x|$ is very large ($|x| \to \infty$, i.e., far from the center $(0,0)$), the fraction $\frac{16}{x^2}$ approaches $0$. Consequently, $\sqrt{1 - \frac{16}{x^2}} \to 1$, and so
   $$y \approx \pm \frac{3}{4}x.$$

2. **Exact Vertical Distance Approaches Zero:**
   In the first quadrant ($x \ge 4, y \ge 0$), compare $y_{\text{line}} = \frac{3}{4}x$ and $y_{\text{hyp}} = \frac{3}{4}\sqrt{x^2 - 16}$:
   $$y_{\text{line}} - y_{\text{hyp}} = \frac{3}{4}\left(x - \sqrt{x^2 - 16}\right) = \frac{3}{4} \cdot \frac{x^2 - (x^2 - 16)}{x + \sqrt{x^2 - 16}} = \frac{12}{x + \sqrt{x^2 - 16}}.$$
   As $x \to \infty$, the denominator grows without bound, so $\lim_{x \to \infty} (y_{\text{line}} - y_{\text{hyp}}) = 0$. Furthermore, since $y_{\text{hyp}} < y_{\text{line}}$, the hyperbola stays strictly closer to the $x$-axis than the asymptotes and approaches them arbitrarily closely at infinity.

### Step 4: Sketch of the hyperbola and its asymptotes
```text
      \       y       /
       \      ^      /   y = (3/4)x
   \    \     |3    /    /
    |    \ .--+--. /    |
----+-----+---+---+-----+----> x
  (-4,0)  | (0,0) |   (4,0)
    |    / '--+--' \    |
   /    /    -3     \    \
       /      |      \   y = -(3/4)x
```

## 4. Verification and Consistency Checks
Let us evaluate a point on the hyperbola and compare it with the asymptote for increasing values of $x$:
- At $x = 5$:
  $$\frac{25}{16} - \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = \frac{9}{16} \implies y = \pm \frac{9}{4} = \pm 2.25.$$
  On the asymptote $y = \frac{3}{4}x$, at $x = 5$ we have $y_{\text{line}} = \frac{15}{4} = 3.75$ (difference: $1.50$).
- At $x = 20$:
  $$y_{\text{hyp}} = \frac{3}{4}\sqrt{400 - 16} = \frac{3}{4}\sqrt{384} \approx 14.697, \quad y_{\text{line}} = \frac{3}{4}(20) = 15.000 \quad (\text{difference: } \approx 0.303).$$
This numerical check confirms both that $(5, \pm 2.25)$ lies on the curve and that the curve converges toward the asymptotes $y = \pm \frac{3}{4}x$ as $|x|$ increases.
