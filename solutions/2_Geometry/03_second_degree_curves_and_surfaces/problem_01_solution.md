# Exercise 1: Recognizing Curves from Canonical Form

## 1. Problem Statement
Recognize the curves
$$x^2+y^2=9,$$
$$\frac{x^2}{16}+\frac{y^2}{9}=1,$$
$$y^2=8x,$$
$$\frac{x^2}{9}-\frac{y^2}{4}=1.$$
For each one, identify the most important features and make a sketch. Explain which parts of the equation let you recognize the type of curve.

## 2. Theoretical Background and Concepts
Second-degree curves (conic sections) centered at or having their vertex at the origin $(0,0)$ have four standard canonical forms in Cartesian coordinates $(x,y)$:

1. **Circle:**
   $$x^2 + y^2 = r^2 \quad (r > 0)$$
   Both $x^2$ and $y^2$ appear with the same positive coefficient (or equal denominators when divided by $r^2$). It represents the set of all points at distance $r$ from the center $(0,0)$.

2. **Ellipse:**
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a, b > 0, \, a \neq b)$$
   Both $x^2$ and $y^2$ are squared and added (same signs), equal to $1$, with different positive denominators $a^2$ and $b^2$. The values $a$ and $b$ are the horizontal and vertical semiaxis lengths.

3. **Parabola:**
   $$y^2 = 2px \quad \text{or} \quad x^2 = 2py \quad (p \neq 0)$$
   Only one variable is squared ($y^2$ or $x^2$), while the other variable appears strictly linearly ($x$ or $y$).

4. **Hyperbola:**
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \quad \text{or} \quad \frac{y^2}{b^2} - \frac{x^2}{a^2} = 1 \quad (a, b > 0)$$
   Both $x^2$ and $y^2$ appear squared, but with **opposite signs** when brought to the same side of the equation.

## 3. Detailed Step-by-Step Solution

### Curve 1: $x^2 + y^2 = 9$
- **How to recognize it:** Both variables $x$ and $y$ are squared, have the same positive coefficient ($1$), and their sum equals a positive constant ($9 = 3^2$). This matches the canonical equation of a **circle** $x^2 + y^2 = r^2$.
- **Important features:**
  - **Type:** Circle.
  - **Center:** $(0,0)$.
  - **Radius:** $r = \sqrt{9} = 3$.
  - **Axis intercepts:** $(\pm 3, 0)$ on the $x$-axis and $(0, \pm 3)$ on the $y$-axis.
  - **Domain and Range:** $x \in [-3, 3]$, $y \in [-3, 3]$.
- **Sketch:**
```text
          y
          ^
          |   (0,3)
        . - - .
      /   |     \
-----+----+------+-----> x
(-3,0)   (0,0)  (3,0)
      \   |     /
        ' - - '
          |  (0,-3)
```

---

### Curve 2: $\frac{x^2}{16} + \frac{y^2}{9} = 1$
- **How to recognize it:** Both $x^2$ and $y^2$ appear with positive signs in a sum equal to $1$, but with different denominators ($16 \neq 9$). This is the canonical form of an **ellipse** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$.
- **Important features:**
  - **Type:** Ellipse.
  - **Center:** $(0,0)$.
  - **Semi-major axis (horizontal):** $a = \sqrt{16} = 4$ along the $x$-axis.
  - **Semi-minor axis (vertical):** $b = \sqrt{9} = 3$ along the $y$-axis.
  - **Vertices (intercepts):** $(\pm 4, 0)$ and $(0, \pm 3)$.
  - **Foci:** $c = \sqrt{a^2 - b^2} = \sqrt{16 - 9} = \sqrt{7}$, so the foci are at $(\pm\sqrt{7}, 0)$.
- **Sketch:**
```text
            y
            ^
            |  (0,3)
       . - -+- - .
    /       |       \
---+--------+--------+---> x
(-4,0)    (0,0)     (4,0)
    \       |       /
       ' - -+- - '
            |  (0,-3)
```

---

### Curve 3: $y^2 = 8x$
- **How to recognize it:** Only $y$ is squared ($y^2$), whereas $x$ appears in the first power ($8x$). This asymmetry between a quadratic variable and a linear variable immediately identifies a **parabola** of the form $y^2 = 2px$.
- **Important features:**
  - **Type:** Parabola.
  - **Vertex:** $(0,0)$.
  - **Axis of symmetry:** The $x$-axis ($y = 0$).
  - **Opening direction:** Opens to the right (towards $+x$) because $y^2 \ge 0$ forces $8x \ge 0 \implies x \ge 0$.
  - **Parameter and Focus/Directrix:** $2p = 8 \implies p = 4$, so the focus is at $\left(\frac{p}{2}, 0\right) = (2, 0)$ and the directrix is $x = -2$.
  - **Sample points:** For $x = 2$, $y^2 = 16 \implies y = \pm 4$, giving $(2, 4)$ and $(2, -4)$.
- **Sketch:**
```text
       y
       ^         / (2,4)
       |      /
       |   /
       | /
-------+---------*-------> x
     (0,0)      (2,0)
       | \
       |   \
       |      \
                 \ (2,-4)
```

---

### Curve 4: $\frac{x^2}{9} - \frac{y^2}{4} = 1$
- **How to recognize it:** Both $x$ and $y$ are squared, but the terms $\frac{x^2}{9}$ and $\frac{y^2}{4}$ have **opposite signs** (a difference equal to $1$). This is the canonical equation of a **hyperbola** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$.
- **Important features:**
  - **Type:** Hyperbola (opening left and right along the $x$-axis).
  - **Center:** $(0,0)$.
  - **Real semiaxis:** $a = \sqrt{9} = 3$ (along the $x$-axis).
  - **Imaginary semiaxis:** $b = \sqrt{4} = 2$ (along the $y$-axis).
  - **Vertices ($x$-intercepts):** $(\pm 3, 0)$. There are no $y$-intercepts because setting $x=0$ yields $-\frac{y^2}{4} = 1$, which has no real solutions.
  - **Asymptotes:** $y = \pm \frac{b}{a}x = \pm \frac{2}{3}x$.
  - **Foci:** $c = \sqrt{a^2 + b^2} = \sqrt{9 + 4} = \sqrt{13}$, located at $(\pm\sqrt{13}, 0)$.
- **Sketch:**
```text
      \     y     /
       \    ^    /   y = (2/3)x
   \    \   |   /    /
    |    \  |  /    |
----+-----+---+-----+----> x
  (-3,0)  / | \   (3,0)
    |    /  |  \    |
   /    /   |   \    \
       /    |    \   y = -(2/3)x
```

## 4. Verification and Consistency Checks
Let us verify key points on each curve by direct substitution into the original equations:
1. **Circle ($x^2+y^2=9$):**
   - Point $(3,0)$: $3^2 + 0^2 = 9 = 9$ (holds).
   - Point $(0,-3)$: $0^2 + (-3)^2 = 9 = 9$ (holds).
2. **Ellipse ($\frac{x^2}{16}+\frac{y^2}{9}=1$):**
   - Point $(4,0)$: $\frac{16}{16} + \frac{0}{9} = 1 + 0 = 1$ (holds).
   - Point $(0,3)$: $\frac{0}{16} + \frac{9}{9} = 0 + 1 = 1$ (holds).
3. **Parabola ($y^2=8x$):**
   - Vertex $(0,0)$: $0^2 = 8(0) \implies 0 = 0$ (holds).
   - Point $(2,4)$: $4^2 = 16$ and $8(2) = 16$ (holds).
4. **Hyperbola ($\frac{x^2}{9}-\frac{y^2}{4}=1$):**
   - Vertex $(3,0)$: $\frac{9}{9} - \frac{0}{4} = 1 - 0 = 1$ (holds).
   - Point $(6, 2\sqrt{3})$: $\frac{36}{9} - \frac{12}{4} = 4 - 3 = 1$ (holds).
