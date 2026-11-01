# Exercise 6: Shifted Ellipse

## 1. Problem Statement
Reduce
$$4x^2+9y^2-16x+18y-11=0$$
to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

## 2. Theoretical Background and Concepts
- **Canonical Equation of a Shifted Ellipse:** An ellipse with center $S = (x_0, y_0)$ and semiaxes $a > 0$ (horizontal) and $b > 0$ (vertical) has the equation:
  $$\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1.$$
- **Completing the Square with Leading Coefficients:** For a quadratic expression $At^2 + Bt$, we first factor out $A$ from the quadratic and linear terms:
  $$At^2 + Bt = A\left(t^2 + \frac{B}{A}t\right) = A\left[\left(t + \frac{B}{2A}\right)^2 - \frac{B^2}{4A^2}\right] = A\left(t + \frac{B}{2A}\right)^2 - \frac{B^2}{4A}.$$

## 3. Detailed Step-by-Step Solution

### Step 1: Group the $x$-terms and $y$-terms and factor out leading coefficients
Starting with:
$$4x^2 + 9y^2 - 16x + 18y - 11 = 0$$
Group the $x$-terms and $y$-terms:
$$(4x^2 - 16x) + (9y^2 + 18y) - 11 = 0$$
Factor out $4$ from the $x$-group and $9$ from the $y$-group:
$$4(x^2 - 4x) + 9(y^2 + 2y) - 11 = 0.$$

### Step 2: Complete the square inside each parenthesis
- For $x^2 - 4x$:
  $$x^2 - 4x = (x - 2)^2 - 4.$$
- For $y^2 + 2y$:
  $$y^2 + 2y = (y + 1)^2 - 1.$$

Substitute these back into the equation:
$$4\left[(x - 2)^2 - 4\right] + 9\left[(y + 1)^2 - 1\right] - 11 = 0$$
Distribute the coefficients $4$ and $9$:
$$4(x - 2)^2 - 16 + 9(y + 1)^2 - 9 - 11 = 0$$
$$4(x - 2)^2 + 9(y + 1)^2 - 36 = 0.$$

### Step 3: Divide to obtain the canonical form
Move $36$ to the right-hand side:
$$4(x - 2)^2 + 9(y + 1)^2 = 36.$$
Divide both sides by $36$:
$$\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = 1$$
$$\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1.$$
This is the **canonical form** of the shifted ellipse.

### Step 4: Read the center and semiaxis lengths
Comparing $\frac{(x - 2)^2}{3^2} + \frac{(y - (-1))^2}{2^2} = 1$ with $\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1$:
- **Center:** $S = (x_0, y_0) = (2, -1)$.
- **Horizontal semiaxis length (along $Ox$):** $a = \sqrt{9} = 3$.
- **Vertical semiaxis length (along $Oy$):** $b = \sqrt{4} = 2$.

## 4. Verification and Consistency Checks
1. **Center Substitution Check (as required in the problem statement):**
   Let $F(x, y) = 4x^2 + 9y^2 - 16x + 18y - 11$ denote the left-hand side of the original equation. From our intermediate completed-square identity:
   $$F(x, y) = 4(x - 2)^2 + 9(y + 1)^2 - 36.$$
   At the center $S = (2, -1)$, the squared terms vanish, so $F(2, -1)$ must equal $-36$. Let us verify this directly in the original polynomial:
   $$F(2, -1) = 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11 = 16 + 9 - 32 - 18 - 11 = 25 - 61 = -36.$$
   The value $-36$ is completely consistent with $4(x - 2)^2 + 9(y + 1)^2 - 36 = 0$.

2. **Vertex Substitution Check:**
   The four vertices of the ellipse are $(2 \pm 3, -1)$ and $(2, -1 \pm 2)$, i.e., $(5, -1)$, $(-1, -1)$, $(2, 1)$, and $(2, -3)$.
   Testing $(5, -1)$ in the original equation:
   $$4(5)^2 + 9(-1)^2 - 16(5) + 18(-1) - 11 = 100 + 9 - 80 - 18 - 11 = 109 - 109 = 0.$$
   Testing $(2, 1)$ in the original equation:
   $$4(2)^2 + 9(1)^2 - 16(2) + 18(1) - 11 = 16 + 9 - 32 + 18 - 11 = 43 - 43 = 0.$$
   Both vertices satisfy the original equation.
