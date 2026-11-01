# Exercise 2: Distance as the Length of a Vector

## 1. Problem Statement

The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

## 2. Theoretical Background and Concepts

1. **Displacement Vector Between Two Points:**
   Given two points $A = (x_A, y_A, z_A)$ and $B = (x_B, y_B, z_B)$ in $\mathbb{R}^3$, the directed segment (vector) from $A$ to $B$ is obtained by subtracting the coordinates of the initial point $A$ from the coordinates of the terminal point $B$:
   $$\overrightarrow{AB} = B - A = (x_B - x_A,\, y_B - y_A,\, z_B - z_A)$$

2. **Euclidean Norm (Length of a Vector):**
   For a vector $v = (v_1, v_2, v_3) \in \mathbb{R}^3$, its length (norm) $\|v\|$ is derived from applying the Pythagorean theorem twice in three mutually orthogonal coordinate directions:
   $$\|v\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$$

3. **Euclidean Distance Formula:**
   The distance $d(A, B)$ between points $A$ and $B$ is defined as:
   $$d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$$

## 3. Detailed Step-by-Step Solution

Given points:
$$A = (1, 2, 3), \qquad B = (4, -2, 6)$$

### Part 1: Construct $\overrightarrow{AB}$
Subtract the coordinates of the initial point $A$ from the terminal point $B$:
$$\overrightarrow{AB} = (4 - 1,\, -2 - 2,\, 6 - 3) = (3, -4, 3)$$

### Part 2: Compute the length of $\overrightarrow{AB}$
Using the Euclidean norm formula for $\overrightarrow{AB} = (3, -4, 3)$:
$$\left\|\overrightarrow{AB}\right\| = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}$$

### Part 3: Compute the distance between $A$ and $B$ using the coordinate formula
Applying the distance formula directly to $A=(1,2,3)$ and $B=(4,-2,6)$:
$$d(A, B) = \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (6 - 3)^2} = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}$$

### Part 4: Explanation of why both calculations give the same result
Both calculations yield $\sqrt{34}$ because the Euclidean distance between two points $A$ and $B$ is, by definition, the length of the displacement vector $\overrightarrow{AB} = B - A$ connecting them. 
- When we compute $\overrightarrow{AB}$ first, we find the coordinate changes $\Delta x = x_B - x_A = 3$, $\Delta y = y_B - y_A = -4$, and $\Delta z = z_B - z_A = 3$, and then compute $\sqrt{(\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2}$.
- The coordinate distance formula simply combines these two steps into a single algebraic expression. Geometrically, translating the segment $AB$ so that $A$ is at the origin $(0,0,0)$ places $B$ at $(3,-4,3)$ without changing the length of the segment (since translation is an isometry).

## 4. Verification and Consistency Checks

1. **Endpoint Reconstruction Check:**
   Adding $\overrightarrow{AB}$ to $A$ must recover $B$:
   $$A + \overrightarrow{AB} = (1, 2, 3) + (3, -4, 3) = (1+3,\, 2-4,\, 3+3) = (4, -2, 6) = B \quad \checkmark$$

2. **Symmetry Check:**
   If we construct $\overrightarrow{BA}$ instead, we get $\overrightarrow{BA} = (-3, 4, -3) = -\overrightarrow{AB}$, whose length is:
   $$\left\|\overrightarrow{BA}\right\| = \sqrt{(-3)^2 + 4^2 + (-3)^2} = \sqrt{9 + 16 + 9} = \sqrt{34} = \left\|\overrightarrow{AB}\right\| \quad \checkmark$$
   Since $5^2 = 25 < 34 < 36 = 6^2$, the distance is $\sqrt{34} \approx 5.831$, which is larger than the largest single coordinate difference $|\Delta y| = 4$, as required by the properties of the Euclidean norm.
