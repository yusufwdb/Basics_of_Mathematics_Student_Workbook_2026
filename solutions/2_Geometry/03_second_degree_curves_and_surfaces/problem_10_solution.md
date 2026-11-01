# Exercise 10: Paraboloids

## 1. Problem Statement
Compare
$$z=x^2+y^2$$
and
$$z=x^2-y^2.$$
For each surface, describe the cross-sections $x=0$, $y=0$, and $z=c$, then make a qualitative sketch.

## 2. Theoretical Background and Concepts
Paraboloids are quadric surfaces in which one variable ($z$) appears linearly while the other two variables ($x$ and $y$) appear quadratically:
1. **Elliptic (or Circular) Paraboloid:**
   $$z = \frac{x^2}{a^2} + \frac{y^2}{b^2}.$$
   Both quadratic terms have the **same sign**. Its horizontal cross-sections ($z = c > 0$) are ellipses (or circles when $a = b$), and all vertical cross-sections through the $z$-axis are parabolas opening in the **same** direction. It has a bowl-like shape with an extremum at the vertex.
2. **Hyperbolic Paraboloid:**
   $$z = \frac{x^2}{a^2} - \frac{y^2}{b^2}.$$
   The quadratic terms have **opposite signs**. Its vertical cross-sections parallel to the coordinate planes are parabolas opening in **opposite** directions, while its horizontal cross-sections ($z = c$) are hyperbolas (or a pair of intersecting lines for $z = 0$). It has a saddle-like shape.

## 3. Detailed Step-by-Step Solution

### Surface 1: $z = x^2 + y^2$ (Circular / Elliptic Paraboloid)

1. **Cross-section $x = 0$ (in the $yz$-plane):**
   $$z = 0^2 + y^2 \implies z = y^2.$$
   This is a **parabola** in the $yz$-plane with vertex at $(0,0,0)$, symmetric about the $Oz$ axis, opening **upward** (towards $+Oz$).

2. **Cross-section $y = 0$ (in the $xz$-plane):**
   $$z = x^2 + 0^2 \implies z = x^2.$$
   This is also a **parabola** in the $xz$-plane with vertex at $(0,0,0)$, symmetric about the $Oz$ axis, opening **upward** (towards $+Oz$).

3. **Horizontal cross-sections $z = c$:**
   $$x^2 + y^2 = c.$$
   - For $c < 0$: **Empty set** (since $x^2 + y^2 \ge 0$ for all real $x, y$). The surface lies entirely in the upper half-space $z \ge 0$.
   - For $c = 0$: $x^2 + y^2 = 0 \implies (x,y,z) = (0,0,0)$, a **single point** (the vertex/minimum).
   - For $c > 0$: A **circle** centered at $(0,0,c)$ with radius $r = \sqrt{c}$, which grows as $c$ increases.

4. **Qualitative Sketch of $z = x^2 + y^2$ (Bowl shape):**
```text
            z
            ^
        . - | - .      <-- circle z = c > 0
      / ' - | - ' \
     |      |      |
      \     |     /    <-- upward parabolas z = x^2, z = y^2
        \   |   /
          ' * '--------> y
          / (0,0,0)
        v
       x
```

---

### Surface 2: $z = x^2 - y^2$ (Hyperbolic Paraboloid / Saddle)

1. **Cross-section $x = 0$ (in the $yz$-plane):**
   $$z = 0^2 - y^2 \implies z = -y^2.$$
   This is a **parabola** in the $yz$-plane with vertex at $(0,0,0)$, opening **downward** (towards $-Oz$).

2. **Cross-section $y = 0$ (in the $xz$-plane):**
   $$z = x^2 - 0^2 \implies z = x^2.$$
   This is a **parabola** in the $xz$-plane with vertex at $(0,0,0)$, opening **upward** (towards $+Oz$).

3. **Horizontal cross-sections $z = c$:**
   $$x^2 - y^2 = c.$$
   - For $c > 0$: A **hyperbola** $\frac{x^2}{c} - \frac{y^2}{c} = 1$ opening along the $x$-axis direction (vertices at $(\pm\sqrt{c}, 0, c)$).
   - For $c = 0$: $x^2 - y^2 = 0 \implies (x - y)(x + y) = 0 \implies y = x \text{ or } y = -x$. This is a **pair of intersecting straight lines** passing through the origin $(0,0,0)$ in the $xy$-plane.
   - For $c < 0$: Writing $c = -k$ with $k > 0$, we get $y^2 - x^2 = k$, which is a **hyperbola** $\frac{y^2}{k} - \frac{x^2}{k} = 1$ opening along the $y$-axis direction (vertices at $(0, \pm\sqrt{-c}, c)$).

4. **Qualitative Sketch of $z = x^2 - y^2$ (Saddle shape):**
```text
             z
             ^
      \      |      /   <-- upward parabola z = x^2 (in xz-plane)
       \     |     /
        \    |    /
         ' - * - '------> y
        /  / | \  \     <-- Saddle point at (0,0,0)
       /  /  |  \  \
         /       \      <-- downward parabola z = -y^2 (in yz-plane)
        v
       x
```

### Summary of the Comparison
| Feature | $z = x^2 + y^2$ (Elliptic Paraboloid) | $z = x^2 - y^2$ (Hyperbolic Paraboloid) |
| :--- | :--- | :--- |
| Cross-section $y = 0$ | Parabola $z = x^2$ (opens up) | Parabola $z = x^2$ (opens up) |
| Cross-section $x = 0$ | Parabola $z = y^2$ (opens up) | Parabola $z = -y^2$ (opens **down**) |
| Cross-section $z = 0$ | Single point $(0,0,0)$ | Two intersecting lines $y = \pm x$ |
| Cross-section $z = c \neq 0$ | Circle for $c > 0$; empty for $c < 0$ | Hyperbolas for all $c \neq 0$ |
| Global geometry | Rotational bowl (minimum at origin) | Saddle surface (minimax point at origin) |

## 4. Verification and Consistency Checks
- **Origin $(0,0,0)$:** Lies on both surfaces since $0 = 0^2 \pm 0^2$.
- **Sign behavior along axes at distance $1$ from the origin:**
  - At $(1, 0)$: both surfaces have $z = 1^2 \pm 0^2 = 1 > 0$.
  - At $(0, 1)$: the first surface has $z = 0^2 + 1^2 = +1 > 0$, whereas the second surface has $z = 0^2 - 1^2 = -1 < 0$.
  - Along the diagonal $y = x$: the first surface rises as $z = 2x^2 \ge 0$, whereas the second surface stays completely flat at height $z = x^2 - x^2 = 0$, confirming that the lines $y = \pm x, z = 0$ lie entirely on the hyperbolic paraboloid.
