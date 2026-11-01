# Exercise 8: Sphere

## 1. Problem Statement
Reduce
$$x^2+y^2+z^2-4x+2y-6z-2=0$$
to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation.

## 2. Theoretical Background and Concepts
- **Canonical Equation of a Sphere in $\mathbb{R}^3$:** A sphere is the set of all points $(x, y, z) \in \mathbb{R}^3$ at a constant distance $r > 0$ (the radius) from a fixed point $S = (x_0, y_0, z_0)$ (the center). By the three-dimensional Euclidean distance formula:
  $$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2.$$
- **General Equation of a Sphere:**
  $$x^2 + y^2 + z^2 + Dx + Ey + Fz + G = 0.$$
  By completing the square independently in $x$, $y$, and $z$, we reduce the general form to the canonical form (provided $r^2 > 0$).

## 3. Detailed Step-by-Step Solution

### Step 1: Group terms by variable
Start with the given equation:
$$x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0.$$
Group the $x$-terms, $y$-terms, and $z$-terms, and move the constant term to the right-hand side:
$$(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = 2.$$

### Step 2: Complete the square for each variable
- For $x^2 - 4x$:
  $$x^2 - 4x = (x - 2)^2 - 4.$$
- For $y^2 + 2y$:
  $$y^2 + 2y = (y + 1)^2 - 1.$$
- For $z^2 - 6z$:
  $$z^2 - 6z = (z - 3)^2 - 9.$$

### Step 3: Write the canonical form
Substitute the completed squares into the grouped equation:
$$\left[(x - 2)^2 - 4\right] + \left[(y + 1)^2 - 1\right] + \left[(z - 3)^2 - 9\right] = 2$$
$$(x - 2)^2 + (y + 1)^2 + (z - 3)^2 - 14 = 2.$$
Add $14$ to both sides:
$$(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16.$$
This is the **canonical form** of the sphere.

### Step 4: Identify the center and radius
Comparing $(x - 2)^2 + (y - (-1))^2 + (z - 3)^2 = 4^2$ with $(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2$:
- **Center:** $S = (2, -1, 3)$.
- **Radius:** $r = \sqrt{16} = 4$.

### Step 5: Find two points on the sphere
Starting at the center $S = (2, -1, 3)$ and moving by $r = 4$ along the coordinate axes:
1. Moving $+4$ units along the $x$-axis gives $P_1 = (2 + 4, -1, 3) = (6, -1, 3)$.
2. Moving $-4$ units along the $z$-axis gives $P_2 = (2, -1, 3 - 4) = (2, -1, -1)$.

## 4. Verification and Consistency Checks
Let us substitute $P_1(6, -1, 3)$ and $P_2(2, -1, -1)$ into both the canonical equation and the original general equation:

### Check for $P_1 = (6, -1, 3)$:
- **Canonical equation:**
  $$(6 - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = 4^2 + 0^2 + 0^2 = 16 \quad (\text{Holds}).$$
- **Original equation** $x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$:
  $$6^2 + (-1)^2 + 3^2 - 4(6) + 2(-1) - 6(3) - 2 = 36 + 1 + 9 - 24 - 2 - 18 - 2 = 46 - 46 = 0 \quad (\text{Holds}).$$

### Check for $P_2 = (2, -1, -1)$:
- **Canonical equation:**
  $$(2 - 2)^2 + (-1 + 1)^2 + (-1 - 3)^2 = 0^2 + 0^2 + (-4)^2 = 16 \quad (\text{Holds}).$$
- **Original equation** $x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$:
  $$2^2 + (-1)^2 + (-1)^2 - 4(2) + 2(-1) - 6(-1) - 2 = 4 + 1 + 1 - 8 - 2 + 6 - 2 = 12 - 12 = 0 \quad (\text{Holds}).$$
