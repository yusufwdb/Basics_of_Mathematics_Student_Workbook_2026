# Exercise 4: Parabola

## 1. Problem Statement
For
$$y^2=12x,$$
identify the vertex, axis of symmetry, and opening direction. Find points on the parabola for $x=3$ and use them to make a sketch.

## 2. Theoretical Background and Concepts
- **Canonical Equation of a Horizontal Parabola:**
  $$y^2 = 2px \quad (p \neq 0).$$
- **Key Geometric Properties:**
  - **Vertex:** $(0,0)$, the point where the parabola turns and intersects its axis of symmetry.
  - **Axis of Symmetry:** Since replacing $y$ with $-y$ leaves $y^2 = 2px$ unchanged, the curve is symmetric with respect to the line $y = 0$ (the $x$-axis).
  - **Opening Direction:** Since $y^2 \ge 0$ for all real $y$, we must have $2px \ge 0$. When $p > 0$, this requires $x \ge 0$, so the parabola opens to the right (in the positive $x$-direction).
  - **Focus and Directrix:** The focus is at $F = \left(\frac{p}{2}, 0\right)$ and the directrix is the vertical line $x = -\frac{p}{2}$. The chord through the focus perpendicular to the axis is the *latus rectum*, at $x = \frac{p}{2}$, where $y = \pm p$.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the vertex, axis of symmetry, and opening direction
Comparing $y^2 = 12x$ with the canonical form $y^2 = 2px$:
- $2p = 12 \implies p = 6 > 0$.
- **Vertex:** $(0, 0)$ (setting $x = 0$ gives $y^2 = 0 \implies y = 0$).
- **Axis of symmetry:** The $x$-axis, i.e., the line $y = 0$, because $(-y)^2 = y^2 = 12x$, meaning for every point $(x, y)$ on the curve, $(x, -y)$ is also on the curve.
- **Opening direction:** Towards the **right** (positive $x$-axis, $+Ox$), because $y^2 \ge 0 \implies 12x \ge 0 \implies x \ge 0$.
- *(Additional feature)* **Focus:** $F = \left(\frac{p}{2}, 0\right) = (3, 0)$; **Directrix:** $x = -3$.

### Step 2: Find points on the parabola for $x = 3$
Substitute $x = 3$ into the equation $y^2 = 12x$:
$$y^2 = 12 \cdot 3 = 36 \implies y = \pm \sqrt{36} = \pm 6.$$
Thus, for $x = 3$, the two corresponding points on the parabola are:
$$A = (3, 6) \quad \text{and} \quad B = (3, -6).$$
*(Note: Since $F=(3,0)$ is the focus, the segment $AB$ of length $12 = 2p$ is the latus rectum of the parabola.)*

### Step 3: Sketch of the parabola
```text
        y
        ^            / (3,6)
        |          /  |
      6 + - - - - *   |
        |      /  |
        |   /     |
        | /       |
--------+---------+-------> x
      (0,0)      (3,0)
        | \       |
        |   \     |
     -6 + - - - - *   |
        |          \  |
                     \ (3,-6)
```

## 4. Verification and Consistency Checks
1. **Direct substitution:**
   - At the vertex $(0,0)$: $0^2 = 12(0) \implies 0 = 0$.
   - At $A(3,6)$: $\text{LHS} = 6^2 = 36$, $\text{RHS} = 12 \cdot 3 = 36$.
   - At $B(3,-6)$: $\text{LHS} = (-6)^2 = 36$, $\text{RHS} = 12 \cdot 3 = 36$.
2. **Focus-directrix definition check:** A parabola is the locus of points equidistant from the focus $F(3,0)$ and the directrix $x = -3$. For $A(3,6)$:
   - Distance to focus $F(3,0)$: $\sqrt{(3-3)^2 + (6-0)^2} = 6$.
   - Distance to directrix $x = -3$: $|3 - (-3)| = 6$.
   Both distances equal $6$, confirming the geometric properties of the parabola.
