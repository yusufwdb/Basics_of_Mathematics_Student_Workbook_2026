# Exercise 14: Contrast: Intersection and Parallelism

## 1. Problem Statement

From the point $P=(0,0,1)$, two lines are drawn with direction vectors
$$v_1=(2,1,-1),\qquad v_2=(2,1,0).$$
For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

## 2. Theoretical Background and Concepts

1. **Coordinate Plane $z = 0$ (the $xy$-plane):**
   The plane $\Pi: z = 0$ (i.e., $0x + 0y + 1z = 0$) has unit normal vector $n = (0, 0, 1) = \mathbf{k}$, pointing vertically along the $z$-axis.

2. **Position of a Line Relative to $z = 0$:**
   For a line $L: P + t v$ starting at $P = (x_0, y_0, z_0)$ with direction vector $v = (v_x, v_y, v_z)$:
   - The dot product of the direction vector with the normal vector is simply the $z$-component of $v$:
     $$n \cdot v = (0, 0, 1) \cdot (v_x, v_y, v_z) = v_z$$
   - **If $v_z \neq 0$:** Moving along the line changes the $z$-coordinate at rate $v_z \neq 0$, so the line must cross the plane $z = 0$ at a unique point.
   - **If $v_z = 0$:** Moving along the line produces zero change in the $z$-coordinate ($z(t) = z_0 + 0t = z_0$), so the line stays at constant height $z = z_0$ parallel to the plane $z = 0$. Since $z_0 = 1 \neq 0$, it is strictly parallel to $z = 0$ and never intersects it.

## 3. Detailed Step-by-Step Solution

Given:
- Initial point $P = (0, 0, 1)$
- Plane $\Pi: z = 0$, with normal vector $n = (0, 0, 1)$
- First line $L_1: (x, y, z) = (0, 0, 1) + t(2, 1, -1)$
- Second line $L_2: (x, y, z) = (0, 0, 1) + s(2, 1, 0)$

### Part 1: Analysis of $L_1$ with direction vector $v_1 = (2, 1, -1)$
1. **Relative position:**
   Compute the dot product of $v_1 = (2, 1, -1)$ with the plane normal $n = (0, 0, 1)$:
   $$n \cdot v_1 = (0)(2) + (0)(1) + (1)(-1) = -1 \neq 0$$
   Because $n \cdot v_1 \neq 0$ (the $z$-component of $v_1$ is non-zero), **the line $L_1$ intersects the plane $z = 0$ at a unique point**.

2. **Finding the intersection point of $L_1$ with $z = 0$:**
   The parametric equations of $L_1$ are:
   $$x = 2t, \qquad y = t, \qquad z = 1 - t$$
   Substitute $z = 1 - t$ into the plane equation $z = 0$:
   $$1 - t = 0 \implies t = 1$$
   Substitute $t = 1$ back into the equations of $L_1$:
   $$(x, y, z) = (2(1),\, 1,\, 1 - 1) = (2, 1, 0)$$
   Thus, $L_1$ intersects the plane $z = 0$ at the point:
   $$Q = (2, 1, 0)$$

### Part 2: Analysis of $L_2$ with direction vector $v_2 = (2, 1, 0)$
1. **Relative position:**
   Compute the dot product of $v_2 = (2, 1, 0)$ with the plane normal $n = (0, 0, 1)$:
   $$n \cdot v_2 = (0)(2) + (0)(1) + (1)(0) = 0$$
   Since $n \cdot v_2 = 0$ and the starting point $P = (0, 0, 1)$ does not lie on the plane $z = 0$ (as $z_P = 1 \neq 0$), **the line $L_2$ is strictly parallel to the plane $z = 0$** (they have no common points).

2. **How to recognize parallelism without solving an equation:**
   We can recognize immediately by inspection that $L_2$ is parallel to $z = 0$ because the third ($z$-) component of its direction vector $v_2 = (2, 1, 0)$ is **$0$**.
   Geometrically, a zero $z$-component in $v_2$ means that displacement along $L_2$ occurs purely horizontally (only in the $x$- and $y$-directions, with zero vertical rise or fall). Since the line starts at height $z = 1$ at $P = (0, 0, 1)$ and its direction vector has no vertical component ($v_z = 0$), every point on $L_2$ remains at constant height $z = 1$, parallel to the horizontal floor $z = 0$ at distance $1$.

## 4. Verification and Consistency Checks

1. **Check for $L_1$ and $Q = (2, 1, 0)$:**
   - $Q = (2, 1, 0)$ has $z$-coordinate $0$, so $Q$ lies on the plane $z = 0$. $\checkmark$
   - $\overrightarrow{PQ} = Q - P = (2 - 0,\, 1 - 0,\, 0 - 1) = (2, 1, -1) = 1 \cdot v_1$, so $Q$ lies on $L_1$ (at $t = 1$). $\checkmark$

2. **Check for $L_2$:**
   Any point on $L_2$ has coordinates $(x, y, z) = (2s,\, s,\, 1 + 0s) = (2s, s, 1)$. For every $s \in \mathbb{R}$, the $z$-coordinate is identically $z = 1 \neq 0$, confirming that $L_2$ lies entirely in the parallel plane $z = 1$ and never meets $z = 0$.
