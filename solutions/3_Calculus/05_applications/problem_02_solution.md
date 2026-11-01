# Exercise 2: Maximum Area of a Rectangle

## 1. Problem Statement

A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

---

## 2. Theoretical Background and Concepts

- **Constrained Geometric Optimization:**
  When optimizing a geometric quantity $A(x,y)$ subject to a constraint $g(x,y) = c$:
  1. Express one variable in terms of the other using the constraint equation.
  2. Substitute into the objective function to obtain a single-variable function $A(x)$.
  3. Determine the feasible domain $D$ where all geometric dimensions remain strictly positive.
  4. Locate critical points where $A'(x) = 0$ in $D$, and verify the global maximum using the Second Derivative Test ($A''(x_0) < 0$ for a concave function) or sign change of $A'(x)$.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Area as a Function of One Side Length
Let $x$ and $y$ denote the lengths of the two adjacent sides of the rectangle.
- The **perimeter constraint** is:
  $$2x + 2y = 40 \implies x + y = 20 \implies y = 20 - x.$$
- The **area** of the rectangle is $A = x \cdot y$. Substituting $y = 20 - x$ gives the area as a function of $x$ alone:
  $$A(x) = x(20 - x) = 20x - x^2.$$

### Part 2: Geometric Domain of $A(x)$
For a non-degenerate rectangle to exist, both side lengths must be strictly positive:
$$x > 0 \quad \text{and} \quad y = 20 - x > 0 \implies x < 20.$$
Therefore, the geometrically meaningful domain is the open interval:
$$D_A = (0, 20).$$

### Part 3: Finding the Dimensions That Maximize the Area
We differentiate $A(x) = 20x - x^2$ on $(0, 20)$:
$$A'(x) = \frac{d}{dx}(20x - x^2) = 20 - 2x.$$
Setting $A'(x) = 0$ to find the critical point:
$$20 - 2x = 0 \implies 2x = 20 \implies x = 10 \in (0, 20).$$
The corresponding second side length is:
$$y = 20 - 10 = 10.$$
Thus, the dimensions that maximize the area are $x = 10$ and $y = 10$ (a **square** of side length $10$), yielding the maximum area:
$$A_{\max} = A(10) = 10 \times 10 = 100.$$

### Part 4: Justification That $x = 10$ Gives a Global Maximum
We can justify that $x = 10$ is the global maximum on $(0, 20)$ in three complementary ways:
1. **First Derivative Sign Test:**
   - For $x \in (0, 10)$, $A'(x) = 20 - 2x > 0$, so $A(x)$ is strictly increasing on $(0, 10]$.
   - For $x \in (10, 20)$, $A'(x) = 20 - 2x < 0$, so $A(x)$ is strictly decreasing on $[10, 20)$.
   Hence $x = 10$ is the unique global maximum on $(0, 20)$.
2. **Second Derivative Test:**
   $$A''(x) = -2 < 0 \quad \text{for all } x \in (0, 20).$$
   Since $A''(x) < 0$ everywhere, $A(x)$ is strictly concave, so the critical point $x = 10$ is the global maximum.
3. **Completing the Square (Algebraic Verification):**
   $$A(x) = 20x - x^2 = 100 - (x - 10)^2 \le 100,$$
   with equality if and only if $x = 10$.

---

## 4. Verification and Consistency Checks

- **Boundary Check:** As $x \to 0^+$ or $x \to 20^-$, the rectangle flattens into a line segment and $A(x) \to 0 < 100$.
- **Sample Test Values:** For $x = 9, y = 11$ (perimeter $2(9+11) = 40$), the area is $9 \times 11 = 99 < 100$. For $x = 5, y = 15$ (perimeter $40$), the area is $5 \times 15 = 75 < 100$.
- **AM–GM Inequality Check:** For $x, y > 0$ with $x + y = 20$, $\sqrt{xy} \le \frac{x+y}{2} = 10 \implies xy \le 100$, with equality iff $x = y = 10$.
