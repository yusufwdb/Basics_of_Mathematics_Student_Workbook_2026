# Exercise 5: Angle Between Vectors

## 1. Problem Statement

Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

## 2. Theoretical Background and Concepts

For any two non-zero vectors $u, v \in \mathbb{R}^3$, the angle $\theta \in [0, \pi]$ between them is determined by the formula:
$$\cos\theta = \frac{u \cdot v}{\|u\|\,\|v\|}$$
Because $\|u\| > 0$ and $\|v\| > 0$, the sign of $\cos\theta$ is identical to the sign of the dot product $u \cdot v$:
- If $u \cdot v > 0$, then $\cos\theta > 0$, which means $\theta \in \left[0, \frac{\pi}{2}\right)$ (**acute angle**, or $0$ if parallel).
- If $u \cdot v = 0$, then $\cos\theta = 0$, which means $\theta = \frac{\pi}{2}$ (**right angle** / perpendicular).
- If $u \cdot v < 0$, then $\cos\theta < 0$, which means $\theta \in \left(\frac{\pi}{2}, \pi\right]$ (**obtuse angle**, or $\pi$ if antiparallel).

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (1, 1, 0), \qquad v = (1, 0, 1)$$

### Part 1: Predict the type of angle from the sign of $u \cdot v$
Compute the dot product:
$$u \cdot v = (1)(1) + (1)(0) + (0)(1) = 1 + 0 + 0 = 1$$
Since $u \cdot v = 1 > 0$ (and $u, v$ are not scalar multiples of each other), $\cos\theta > 0$. Therefore, we predict that the angle $\theta$ between $u$ and $v$ is **acute** ($0 < \theta < \frac{\pi}{2}$, or between $0^\circ$ and $90^\circ$).

### Part 2: Compute the exact angle $\theta$
First, compute the lengths of $u$ and $v$:
$$\|u\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}$$
$$\|v\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1 + 0 + 1} = \sqrt{2}$$
Now substitute $u \cdot v = 1$, $\|u\| = \sqrt{2}$, and $\|v\| = \sqrt{2}$ into the cosine formula:
$$\cos\theta = \frac{u \cdot v}{\|u\|\,\|v\|} = \frac{1}{\sqrt{2}\cdot\sqrt{2}} = \frac{1}{2}$$
Since $\theta \in [0, \pi]$ and $\cos\theta = \frac{1}{2}$, we obtain:
$$\theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3}\text{ radians} = 60^\circ$$

### Part 3: Compare the result with the prediction
Our exact calculation yielded $\theta = 60^\circ$ ($\frac{\pi}{3}$ radians). Since $0^\circ < 60^\circ < 90^\circ$ ($0 < \frac{\pi}{3} < \frac{\pi}{2}$), the angle is indeed **acute**, which is in complete agreement with our prediction from Part 1 based on $u \cdot v > 0$.

## 4. Verification and Consistency Checks

**Equilateral Triangle Geometric Check:**
Consider the difference vector between $u$ and $v$:
$$u - v = (1 - 1,\, 1 - 0,\, 0 - 1) = (0, 1, -1)$$
Let us compute the length of this third side of the triangle formed by $u$, $v$, and $u-v$:
$$\|u - v\| = \sqrt{0^2 + 1^2 + (-1)^2} = \sqrt{2}$$
Notice that all three sides of the triangle with vertices at $(0,0,0)$, $u=(1,1,0)$, and $v=(1,0,1)$ have the exact same length:
$$\|u\| = \|v\| = \|u - v\| = \sqrt{2}$$
Therefore, the triangle is **equilateral**, and every interior angle of an equilateral triangle is $\frac{\pi}{3} = 60^\circ$. This independently confirms our result $\theta = 60^\circ$.
