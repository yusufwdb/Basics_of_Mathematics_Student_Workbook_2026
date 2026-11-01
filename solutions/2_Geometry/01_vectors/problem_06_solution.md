# Exercise 6: Projection and Perpendicular Component

## 1. Problem Statement

Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute
$$r=u-\operatorname{proj}_v u$$
and verify that $r\cdot v=0$. Explain this result geometrically.

## 2. Theoretical Background and Concepts

1. **Orthogonal Projection of a Vector onto a Direction:**
   Given a vector $u$ and a non-zero direction vector $v \neq \mathbf{0}$, the orthogonal projection of $u$ onto $v$, denoted $\operatorname{proj}_v u$, is the vector parallel to $v$ given by:
   $$\operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \left(\frac{u \cdot v}{\|v\|^2}\right) v$$
   Here, $\frac{u \cdot v}{\|v\|}$ is the signed scalar projection (the component of $u$ along the unit vector $\hat{v} = \frac{v}{\|v\|}$).

2. **Orthogonal Decomposition:**
   Subtracting the parallel projection from $u$ yields the residual (perpendicular component):
   $$r = u - \operatorname{proj}_v u$$
   By construction, $r$ is orthogonal to $v$:
   $$r \cdot v = (u - \operatorname{proj}_v u) \cdot v = u \cdot v - \left(\frac{u \cdot v}{v \cdot v}\right)(v \cdot v) = u \cdot v - u \cdot v = 0$$

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (4, 2), \qquad v = (1, 1)$$

### Step 1: Compute $\operatorname{proj}_v u$
First, compute the dot products $u \cdot v$ and $v \cdot v$:
$$u \cdot v = (4)(1) + (2)(1) = 4 + 2 = 6$$
$$v \cdot v = \|v\|^2 = 1^2 + 1^2 = 2$$
Substitute these into the projection formula:
$$\operatorname{proj}_v u = \frac{u \cdot v}{v \cdot v}\, v = \frac{6}{2}(1, 1) = 3(1, 1) = (3, 3)$$

### Step 2: Compute the residual vector $r = u - \operatorname{proj}_v u$
Subtract $\operatorname{proj}_v u = (3, 3)$ from $u = (4, 2)$:
$$r = u - \operatorname{proj}_v u = (4, 2) - (3, 3) = (4 - 3,\, 2 - 3) = (1, -1)$$

### Step 3: Verify that $r \cdot v = 0$
Compute the dot product of $r = (1, -1)$ and $v = (1, 1)$:
$$r \cdot v = (1)(1) + (-1)(1) = 1 - 1 = 0$$
Thus $r \perp v$ as required.

### Step 4: Geometric Explanation
Geometrically, if we place the tails of $u$ and $v$ at the origin $O=(0,0)$, the vector $v=(1,1)$ defines the line $y=x$. Dropping a perpendicular from the tip of $u=(4,2)$ onto the line $y=x$ lands at the point $(3,3)$, which is the tip of $\operatorname{proj}_v u = (3,3)$ (the "shadow" of $u$ on the line spanned by $v$). 
The vector $r = u - \operatorname{proj}_v u = (1,-1)$ is the directed segment from the foot of the perpendicular $(3,3)$ to the tip of $u=(4,2)$. Because $\operatorname{proj}_v u$ was constructed by dropping an orthogonal segment onto the line of $v$, the connecting vector $r$ forms the altitude of a right triangle and is therefore perpendicular to $v$ ($r \cdot v = 0$).

## 4. Verification and Consistency Checks

1. **Reconstruction Check ($u = \operatorname{proj}_v u + r$):**
   $$\operatorname{proj}_v u + r = (3, 3) + (1, -1) = (4, 2) = u \quad \checkmark$$

2. **Pythagorean Identity Check:**
   Since $\operatorname{proj}_v u$ and $r$ are orthogonal ($(\operatorname{proj}_v u) \cdot r = 3(1) + 3(-1) = 0$), their squared lengths must sum to $\|u\|^2$:
   - $\|\operatorname{proj}_v u\|^2 = 3^2 + 3^2 = 9 + 9 = 18$
   - $\|r\|^2 = 1^2 + (-1)^2 = 1 + 1 = 2$
   - $\|u\|^2 = 4^2 + 2^2 = 16 + 4 = 20$
   Indeed, $\|\operatorname{proj}_v u\|^2 + \|r\|^2 = 18 + 2 = 20 = \|u\|^2$.
