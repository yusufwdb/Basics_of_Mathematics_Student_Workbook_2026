# Exercise 10: Triangle Area from Vectors

## 1. Problem Statement

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

## 2. Theoretical Background and Concepts

1. **Area of a Parallelogram via the Cross Product:**
   For two vectors $u = \overrightarrow{AB}$ and $v = \overrightarrow{AC}$ in $\mathbb{R}^3$ with angle $\theta \in [0, \pi]$ between them, the magnitude of their cross product is:
   $$\|u \times v\| = \|u\|\,\|v\|\sin\theta$$
   In a parallelogram spanned by $u$ and $v$, $\|u\|$ is the length of the base and $\|v\|\sin\theta$ is the perpendicular height $h$. Therefore, the area of the parallelogram is:
   $$\text{Area}_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\|$$

2. **Area of a Triangle:**
   A triangle with vertices $A, B, C$ has base $\|u\|$ and the same altitude $h = \|v\|\sin\theta$, so its area is half that of the parallelogram:
   $$\text{Area}_{\triangle ABC} = \frac{1}{2}\|\overrightarrow{AB} \times \overrightarrow{AC}\|$$

## 3. Detailed Step-by-Step Solution

Given vertices:
$$A = (0, 0, 0), \qquad B = (2, 1, 0), \qquad C = (1, 3, 2)$$

### Step 1: Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$
Subtract the coordinates of $A = (0,0,0)$ from $B$ and $C$:
$$\overrightarrow{AB} = B - A = (2 - 0,\, 1 - 0,\, 0 - 0) = (2, 1, 0)$$
$$\overrightarrow{AC} = C - A = (1 - 0,\, 3 - 0,\, 2 - 0) = (1, 3, 2)$$

### Step 2: Compute $\overrightarrow{AB} \times \overrightarrow{AC}$ and the area of the parallelogram
Evaluate the cross product:
$$\overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 1 & 0 \\ 1 & 3 & 2 \end{vmatrix} = \big((1)(2) - (0)(3),\, (0)(1) - (2)(2),\, (2)(3) - (1)(1)\big) = (2, -4, 5)$$
The area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ is the norm of this cross product:
$$\text{Area}_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{2^2 + (-4)^2 + 5^2} = \sqrt{4 + 16 + 25} = \sqrt{45} = 3\sqrt{5}$$

### Step 3: Find the area of the triangle $\triangle ABC$
Multiplying the parallelogram area by $\frac{1}{2}$:
$$\text{Area}_{\triangle ABC} = \frac{1}{2}\|\overrightarrow{AB} \times \overrightarrow{AC}\| = \frac{\sqrt{45}}{2} = \frac{3\sqrt{5}}{2} \approx 3.3541$$

### Step 4: Explain the factor $\frac{1}{2}$
Geometrically, the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ has vertices at $A$, $B$, $C$, and $D = A + \overrightarrow{AB} + \overrightarrow{AC}$. The diagonal $BC$ cuts this parallelogram into two congruent triangles ($\triangle ABC$ and $\triangle DCB$) having equal side lengths (by the SSS congruence criterion). Since the areas of the two congruent triangles are equal and together they form the entire parallelogram, the area of $\triangle ABC$ is exactly $\frac{1}{2}$ of the area of the parallelogram (just as $\text{Area}_{\triangle} = \frac{1}{2}\text{base} \times \text{height}$ is half of $\text{Area}_{\text{parallelogram}} = \text{base} \times \text{height}$).

## 4. Verification and Consistency Checks

**Verification via Dot Product and Trigonometric Identity ($\sin^2\theta + \cos^2\theta = 1$):**
We can compute the area of $\triangle ABC$ without the cross product using the formula:
$$\text{Area}_{\triangle ABC} = \frac{1}{2}\sqrt{\|\overrightarrow{AB}\|^2\|\overrightarrow{AC}\|^2 - (\overrightarrow{AB} \cdot \overrightarrow{AC})^2}$$
Let us compute each quantity:
- $\|\overrightarrow{AB}\|^2 = 2^2 + 1^2 + 0^2 = 5$
- $\|\overrightarrow{AC}\|^2 = 1^2 + 3^2 + 2^2 = 1 + 9 + 4 = 14$
- $\overrightarrow{AB} \cdot \overrightarrow{AC} = (2)(1) + (1)(3) + (0)(2) = 2 + 3 + 0 = 5$

Substituting into the formula:
$$\text{Area}_{\triangle ABC} = \frac{1}{2}\sqrt{(5)(14) - 5^2} = \frac{1}{2}\sqrt{70 - 25} = \frac{1}{2}\sqrt{45} = \frac{3\sqrt{5}}{2} \quad \checkmark$$
This matches our cross-product calculation.
