# Exercise 3: Vector Normalization

## 1. Problem Statement

For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

## 2. Theoretical Background and Concepts

1. **Euclidean Norm in $\mathbb{R}^2$:**
   For a vector $v = (v_1, v_2) \in \mathbb{R}^2$, its length (magnitude) is:
   $$\|v\| = \sqrt{v_1^2 + v_2^2}$$

2. **Unit Vector and Normalization:**
   A vector $e$ is called a **unit vector** if $\|e\| = 1$. Any non-zero vector $v \neq \mathbf{0}$ can be normalized by multiplying it by the positive scalar $\frac{1}{\|v\|}$:
   $$e = \frac{v}{\|v\|} = \left(\frac{v_1}{\|v\|},\, \frac{v_2}{\|v\|}\right)$$
   Because $\frac{1}{\|v\|} > 0$, multiplying $v$ by $\frac{1}{\|v\|}$ scales its length to $1$ while preserving both its line of action (direction) and its sense (orientation).

3. **Magnitude–Direction Decomposition:**
   Every non-zero vector $v$ can be uniquely factored as:
   $$v = \|v\|\, e$$
   where $\|v\| > 0$ encodes pure length (magnitude) and $e$ (with $\|e\|=1$) encodes pure direction and orientation.

## 3. Detailed Step-by-Step Solution

Given vector:
$$v = (3, 4)$$

### Step 1: Compute the length $\|v\|$
$$\|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

### Step 2: Find the normalized unit vector $e$
Divide $v$ by its length $\|v\| = 5$:
$$e = \frac{1}{\|v\|}v = \frac{1}{5}(3, 4) = \left(\frac{3}{5},\, \frac{4}{5}\right) = (0.6,\, 0.8)$$

### Step 3: Check that $\|e\| = 1$
Compute the norm of $e$:
$$\|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = \sqrt{1} = 1$$

### Step 4: Reconstruct $v$ in the form $v = \|v\|e$
Multiplying the unit direction vector $e$ by the magnitude $\|v\| = 5$:
$$\|v\|e = 5 \cdot \left(\frac{3}{5},\, \frac{4}{5}\right) = \left(5 \cdot \frac{3}{5},\, 5 \cdot \frac{4}{5}\right) = (3, 4) = v$$

### Step 5: Explain what changes and what remains unchanged during normalization
- **What changes:** The **length (magnitude)** of the vector changes from $\|v\| = 5$ to $\|e\| = 1$ (unless the original vector already had length $1$). Consequently, the individual coordinates are scaled proportionally by $\frac{1}{\|v\|}$.
- **What remains unchanged:**
  1. The **direction** (the slope / line of action, since the ratio of coordinates $y/x = \frac{4/5}{3/5} = \frac{4}{3}$ is preserved).
  2. The **orientation** (sense along that line, because the scaling factor $\frac{1}{\|v\|} = \frac{1}{5} > 0$ is strictly positive, so the signs of all coordinates and the angle $\theta$ with the positive $x$-axis remain identical: $\cos\theta = \frac{3}{5}$, $\sin\theta = \frac{4}{5}$).

## 4. Verification and Consistency Checks

We can verify that $v$ and $e$ point in the exact same direction and orientation by computing the cosine of the angle $\theta$ between them using the dot product:
$$\cos\theta = \frac{v \cdot e}{\|v\|\,\|e\|} = \frac{3 \cdot \frac{3}{5} + 4 \cdot \frac{4}{5}}{5 \cdot 1} = \frac{\frac{9}{5} + \frac{16}{5}}{5} = \frac{5}{5} = 1$$
Since $\cos\theta = 1$, the angle between $v$ and $e$ is $\theta = 0$, confirming that $e$ has the exact same direction and orientation as $v$, and $\|e\| = 1$ confirms it lies on the unit circle.
