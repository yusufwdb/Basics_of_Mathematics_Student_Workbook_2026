# Exercise 7: Classifying a Second-Degree Equation

## 1. Problem Statement
Determine the type of object described by:
1. $4x^2+9y^2=36$,
2. $x^2-y^2=1$,
3. $x^2-4y=0$,
4. $x^2+y^2+1=0$.

In the last case, explain why there are no real points.

## 2. Theoretical Background and Concepts
A second-degree equation in two variables without a mixed term ($xy$) has the form:
$$Ax^2 + Cy^2 + Dx + Ey + F = 0.$$
After reducing to canonical form, its geometric nature depends on the signs of the quadratic coefficients $A$ and $C$ and the sign of the constant term:
- **$A$ and $C$ have the same sign ($AC > 0$):** Ellipse (or circle if $A = C$), a single point (if the right-hand side is $0$), or the **empty set** (an imaginary ellipse/circle if the sum of squares equals a negative number).
- **$A$ and $C$ have opposite signs ($AC < 0$):** Hyperbola (if the constant term after completing the square is non-zero) or a pair of intersecting lines (if the constant is zero).
- **Exactly one of $A, C$ is zero ($AC = 0$, not both zero):** Parabola (when the other variable is present linearly).

## 3. Detailed Step-by-Step Solution

### 1. Equation: $4x^2 + 9y^2 = 36$
- **Reduction to canonical form:** Divide both sides by $36$:
  $$\frac{4x^2}{36} + \frac{9y^2}{36} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1.$$
- **Classification:** **Ellipse** centered at $(0,0)$ with horizontal semiaxis $a = 3$ and vertical semiaxis $b = 2$. Both quadratic terms have positive coefficients and their sum equals a positive constant.

---

### 2. Equation: $x^2 - y^2 = 1$
- **Canonical form:** Already in canonical form:
  $$\frac{x^2}{1^2} - \frac{y^2}{1^2} = 1.$$
- **Classification:** **Hyperbola** (specifically, an equilateral/rectangular hyperbola) centered at $(0,0)$ with semiaxes $a = 1$ and $b = 1$, vertices at $(\pm 1, 0)$, and perpendicular asymptotes $y = \pm x$. The quadratic terms $x^2$ and $-y^2$ have opposite signs.

---

### 3. Equation: $x^2 - 4y = 0$
- **Reduction to canonical form:** Isolate the quadratic term:
  $$x^2 = 4y \quad \left(\text{or } y = \frac{1}{4}x^2\right).$$
- **Classification:** **Parabola** with vertex at $(0,0)$, axis of symmetry along the $y$-axis ($x = 0$), opening upward (towards $+Oy$), with parameter $2p = 4 \implies p = 2$ (focus at $(0,1)$ and directrix $y = -1$). Only $x$ is squared while $y$ is linear.

---

### 4. Equation: $x^2 + y^2 + 1 = 0$
- **Rearrangement:**
  $$x^2 + y^2 = -1.$$
- **Classification:** **Empty set in $\mathbb{R}^2$** (often called an *imaginary circle*).
- **Explanation of why there are no real points:**
  For any real number $t \in \mathbb{R}$, its square is non-negative: $t^2 \ge 0$. Therefore, for any pair of real coordinates $(x, y) \in \mathbb{R}^2$, we have:
  $$x^2 \ge 0 \quad \text{and} \quad y^2 \ge 0 \implies x^2 + y^2 \ge 0.$$
  Adding $1$ to both sides yields:
  $$x^2 + y^2 + 1 \ge 1 > 0.$$
  Since the left-hand side is always at least $1$ for all $(x,y) \in \mathbb{R}^2$, it can never equal $0$. Hence, no real point $(x, y)$ satisfies the equation.

## 4. Verification and Consistency Checks
Let us verify that each real curve (1–3) contains expected points and that equation 4 fails for every test point:
1. **Ellipse ($4x^2+9y^2=36$):** Substituting $(3,0)$ gives $4(9) + 9(0) = 36$; substituting $(0,2)$ gives $4(0) + 9(4) = 36$.
2. **Hyperbola ($x^2-y^2=1$):** Substituting $(1,0)$ gives $1 - 0 = 1$; substituting $(\sqrt{2}, 1)$ gives $2 - 1 = 1$.
3. **Parabola ($x^2-4y=0$):** Substituting $(2,1)$ gives $2^2 - 4(1) = 4 - 4 = 0$.
4. **Empty set ($x^2+y^2+1=0$):** The minimum possible value of $f(x,y) = x^2+y^2+1$ on $\mathbb{R}^2$ occurs at $(0,0)$, where $f(0,0) = 1 > 0$, confirming the absence of real solutions.
