# Exercise 11: Two Similar Surfaces

## 1. Problem Statement
Compare
$$x^2+y^2-z^2=1$$
and
$$x^2+y^2-z^2=-1.$$
For several values $z=c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches.

## 2. Theoretical Background and Concepts
- **Hyperboloids of Revolution:** When a quadric equation contains three squared variables where two have one sign and the third has the opposite sign, the surface is a **hyperboloid**:
  1. **Hyperboloid of One Sheet:**
     $$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c_0^2} = 1.$$
     There is **one minus sign** when written with $+1$ on the right-hand side. Horizontal cross-sections exist for every $z = c \in \mathbb{R}$, so the surface is a single connected tube ("cooling tower" shape).
  2. **Hyperboloid of Two Sheets:**
     $$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c_0^2} = -1 \quad \Longleftrightarrow \quad \frac{z^2}{c_0^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1.$$
     There are **two minus signs** when written with $+1$ on the right-hand side. Horizontal cross-sections do not exist near $z = 0$, splitting the surface into two disconnected bowls ("two sheets").

## 3. Detailed Step-by-Step Solution

### Part 1: Cross-Sections $z = c$ for Surface 1 ($x^2 + y^2 - z^2 = 1$)
Substitute $z = c$:
$$x^2 + y^2 = 1 + c^2.$$
Since $1 + c^2 \ge 1 > 0$ for **all** real numbers $c \in \mathbb{R}$, a circular cross-section centered at $(0,0,c)$ exists at every height $z = c$, with radius:
$$r_1(c) = \sqrt{1 + c^2}.$$
Let us evaluate $r_1(c)$ for several concrete values of $c$:
- $c = 0$: $x^2 + y^2 = 1 \implies$ circle of minimum radius $r_1(0) = 1$ (the "waist" or "throat" circle in the $xy$-plane).
- $c = \pm 1$: $x^2 + y^2 = 2 \implies$ circles of radius $r_1(\pm 1) = \sqrt{2} \approx 1.414$.
- $c = \pm 2$: $x^2 + y^2 = 5 \implies$ circles of radius $r_1(\pm 2) = \sqrt{5} \approx 2.236$.
- $c = \pm 3$: $x^2 + y^2 = 10 \implies$ circles of radius $r_1(\pm 3) = \sqrt{10} \approx 3.162$.

---

### Part 2: Cross-Sections $z = c$ for Surface 2 ($x^2 + y^2 - z^2 = -1$)
Substitute $z = c$:
$$x^2 + y^2 = c^2 - 1.$$
Since $x^2 + y^2 \ge 0$, real points exist if and only if $c^2 - 1 \ge 0 \iff |c| \ge 1$. When $|c| > 1$, the cross-section is a circle centered at $(0,0,c)$ with radius:
$$r_2(c) = \sqrt{c^2 - 1}.$$
Let us check several values of $c$:
- $c = 0$: $x^2 + y^2 = -1 \implies$ **does not exist** (empty set).
- $c = \pm \frac{1}{2}$: $x^2 + y^2 = -\frac{3}{4} \implies$ **does not exist** (empty set).
- $c = \pm 1$: $x^2 + y^2 = 0 \implies$ **single point** $(0, 0, 1)$ and $(0, 0, -1)$ (radius $r_2(\pm 1) = 0$; these are the two vertices).
- $c = \pm 2$: $x^2 + y^2 = 3 \implies$ circles of radius $r_2(\pm 2) = \sqrt{3} \approx 1.732$.
- $c = \pm 3$: $x^2 + y^2 = 8 \implies$ circles of radius $r_2(\pm 3) = \sqrt{8} = 2\sqrt{2} \approx 2.828$.

---

### Part 3: Qualitative Comparison and Sketches

| Property | $x^2 + y^2 - z^2 = 1$ (Hyperboloid of One Sheet) | $x^2 + y^2 - z^2 = -1$ (Hyperboloid of Two Sheets) |
| :--- | :--- | :--- |
| Range of $z$ | All $z \in (-\infty, \infty)$ | $z \in (-\infty, -1] \cup [1, \infty)$ (gap for $\|z\| < 1$) |
| Connectedness | **Connected** (one single piece) | **Disconnected** (two separate sheets: $z \ge 1$ and $z \le -1$) |
| Cross-section at $z=0$ | Waist circle of radius $1$ | Empty set |
| Vertical trace ($y=0$) | Hyperbola $x^2 - z^2 = 1$ (opens left/right) | Hyperbola $z^2 - x^2 = 1$ (opens up/down) |

#### Sketch of $x^2 + y^2 - z^2 = 1$ (One Sheet) vs. $x^2 + y^2 - z^2 = -1$ (Two Sheets):
```text
   Hyperboloid of One Sheet              Hyperboloid of Two Sheets
      x^2 + y^2 - z^2 = 1                   x^2 + y^2 - z^2 = -1

               z                                     z
               ^                                     ^
         \  . -|- .  /                         \  . -|- .  /
          \ ' -|- ' /                           \ ' -|- ' /
           |   |   |                             ' - * - '   z = 1
          ( . -|- . )  z = 0 (r=1)                   |       (empty for |z|<1)
           |   |   |----+-> y                    ----+----> y
          / . -|- . \   |                        . - * - .   z = -1
         /  ' -|- '  \                          / . -|- . \
        v                                      /  ' -|- '  \
       x                                      v
                                             x
```

## 4. Verification and Consistency Checks
1. **Vertical cross-section check ($y = 0$):**
   - For $x^2 + y^2 - z^2 = 1$, setting $y = 0$ gives the hyperbola $x^2 - z^2 = 1$, whose vertices are $(\pm 1, 0, 0)$. Rotating this hyperbola around the $z$-axis sweeps out a single connected hourglass/cooling-tower surface.
   - For $x^2 + y^2 - z^2 = -1$, setting $y = 0$ gives $z^2 - x^2 = 1$, whose vertices are $(0, 0, \pm 1)$. Rotating this hyperbola around the $z$-axis sweeps out two separate cup-like sheets above $z = 1$ and below $z = -1$.
2. **Asymptoticcone check:** Both surfaces share the same asymptotic cone $x^2 + y^2 - z^2 = 0$ (where $r(c) = |c|$). Indeed, for large $|c|$, both $r_1(c) = \sqrt{c^2+1}$ and $r_2(c) = \sqrt{c^2-1}$ approach $|c|$, with $r_2(c) < |c| < r_1(c)$.
