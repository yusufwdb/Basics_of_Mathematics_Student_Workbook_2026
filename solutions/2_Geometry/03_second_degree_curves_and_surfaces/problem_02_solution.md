# Exercise 2: Circle by Completing the Square

## 1. Problem Statement
Reduce
$$x^2+y^2-6x+4y-3=0$$
to canonical form. Find the center and radius, then substitute two simple points from the circle into both forms of the equation.

## 2. Theoretical Background and Concepts
- **Canonical Equation of a Circle:** A circle with center $S = (x_0, y_0)$ and radius $r > 0$ has the canonical equation:
  $$(x - x_0)^2 + (y - y_0)^2 = r^2.$$
- **General Form of a Circle:** Expanding the squares leads to the general equation:
  $$x^2 + y^2 + Dx + Ey + F = 0.$$
- **Completing the Square:** Any quadratic expression of the form $t^2 + bt$ can be rewritten as a shifted square by adding and subtracting $\left(\frac{b}{2}\right)^2$:
  $$t^2 + bt = \left(t + \frac{b}{2}\right)^2 - \frac{b^2}{4}.$$

## 3. Detailed Step-by-Step Solution

### Step 1: Group the $x$-terms and $y$-terms
Starting from the given equation:
$$x^2 + y^2 - 6x + 4y - 3 = 0$$
Rearrange terms to group $x$ and $y$ variables separately and move the constant term to the right-hand side:
$$(x^2 - 6x) + (y^2 + 4y) = 3.$$

### Step 2: Complete the square for $x$ and $y$
- For $x^2 - 6x$: Half of the linear coefficient is $\frac{-6}{2} = -3$, and its square is $(-3)^2 = 9$:
  $$x^2 - 6x = (x - 3)^2 - 9.$$
- For $y^2 + 4y$: Half of the linear coefficient is $\frac{4}{2} = 2$, and its square is $2^2 = 4$:
  $$y^2 + 4y = (y + 2)^2 - 4.$$

### Step 3: Write the canonical form
Substitute the completed squares back into the equation:
$$\left((x - 3)^2 - 9\right) + \left((y + 2)^2 - 4\right) = 3$$
$$(x - 3)^2 + (y + 2)^2 - 13 = 3$$
Add $13$ to both sides:
$$(x - 3)^2 + (y + 2)^2 = 16.$$
This is the **canonical form** of the circle.

### Step 4: Read the center and radius
Comparing $(x - 3)^2 + (y - (-2))^2 = 4^2$ with $(x - x_0)^2 + (y - y_0)^2 = r^2$:
- **Center:** $S = (3, -2)$
- **Radius:** $r = \sqrt{16} = 4$

### Step 5: Choose two simple points on the circle
Starting from the center $(3, -2)$, we can move by $r = 4$ units parallel to the coordinate axes:
1. Moving $4$ units to the right along the $x$-axis gives $P_1 = (3 + 4, -2) = (7, -2)$.
2. Moving $4$ units upward along the $y$-axis gives $P_2 = (3, -2 + 4) = (3, 2)$.

## 4. Verification and Consistency Checks
We substitute $P_1(7, -2)$ and $P_2(3, 2)$ into both the canonical form and the original general equation.

### Check for $P_1 = (7, -2)$:
- **Canonical form** $(x - 3)^2 + (y + 2)^2 = 16$:
  $$(7 - 3)^2 + (-2 + 2)^2 = 4^2 + 0^2 = 16 \quad (\text{Matches } 16).$$
- **General form** $x^2 + y^2 - 6x + 4y - 3 = 0$:
  $$7^2 + (-2)^2 - 6(7) + 4(-2) - 3 = 49 + 4 - 42 - 8 - 3 = 53 - 53 = 0 \quad (\text{Matches } 0).$$

### Check for $P_2 = (3, 2)$:
- **Canonical form** $(x - 3)^2 + (y + 2)^2 = 16$:
  $$(3 - 3)^2 + (2 + 2)^2 = 0^2 + 4^2 = 16 \quad (\text{Matches } 16).$$
- **General form** $x^2 + y^2 - 6x + 4y - 3 = 0$:
  $$3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3 = 21 - 21 = 0 \quad (\text{Matches } 0).$$

Both points satisfy both forms of the equation, confirming the equivalence of the algebraic transformation.
