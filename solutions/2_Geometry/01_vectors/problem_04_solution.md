# Exercise 4: Dot Product and Perpendicularity

## 1. Problem Statement

For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

## 2. Theoretical Background and Concepts

1. **Algebraic Definition of the Dot Product (Scalar Product):**
   For two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, their dot product is the real number defined by:
   $$u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$$

2. **Geometric Definition and Orthogonality (Perpendicularity) Criterion:**
   Geometrically, the dot product is related to the angle $\theta \in [0, \pi]$ between $u$ and $v$ by:
   $$u \cdot v = \|u\|\,\|v\|\cos\theta$$
   For non-zero vectors $u$ and $v$, $\|u\| > 0$ and $\|v\| > 0$, so $u \cdot v = 0$ if and only if $\cos\theta = 0$, which corresponds to $\theta = \frac{\pi}{2}$ ($90^\circ$). Therefore:
   $$u \perp v \iff u \cdot v = 0$$

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (1, 2, -1), \qquad v = (2, -1, 3)$$

### Part 1: Compute $u \cdot v$ and determine whether $u$ and $v$ are perpendicular
Multiply corresponding components and add them together:
$$u \cdot v = (1)(2) + (2)(-1) + (-1)(3) = 2 - 2 - 3 = -3$$
Since $u \cdot v = -3 \neq 0$, the vectors $u$ and $v$ are **not perpendicular** (in fact, since $u \cdot v < 0$, the angle between them is obtuse).

### Part 2: Find $a$ so that $w = (2, -1, a)$ is perpendicular to $u$
For $w = (2, -1, a)$ to be perpendicular to $u = (1, 2, -1)$, their dot product must vanish:
$$u \cdot w = 0$$
Substitute the coordinates of $u$ and $w$:
$$(1)(2) + (2)(-1) + (-1)(a) = 0$$
Simplify the left-hand side:
$$2 - 2 - a = 0 \implies -a = 0 \implies a = 0$$
Thus, the required parameter value is $a = 0$, giving the vector $w = (2, -1, 0)$.

## 4. Verification and Consistency Checks

1. **Direct Substitution Check for $w = (2, -1, 0)$:**
   Compute the dot product of $u = (1, 2, -1)$ and $w = (2, -1, 0)$:
   $$u \cdot w = 1 \cdot 2 + 2 \cdot (-1) + (-1) \cdot 0 = 2 - 2 + 0 = 0 \quad \checkmark$$
   Since $u \neq \mathbf{0}$ and $w \neq \mathbf{0}$ and $u \cdot w = 0$, $u$ and $w$ are indeed mutually perpendicular.

2. **Pythagorean Theorem Check:**
   Two vectors $u$ and $w$ are perpendicular if and only if $\|u\|^2 + \|w\|^2 = \|u - w\|^2$. Let us check:
   - $\|u\|^2 = 1^2 + 2^2 + (-1)^2 = 1 + 4 + 1 = 6$
   - $\|w\|^2 = 2^2 + (-1)^2 + 0^2 = 4 + 1 + 0 = 5$
   - $u - w = (1-2,\, 2-(-1),\, -1-0) = (-1, 3, -1)$, so $\|u - w\|^2 = (-1)^2 + 3^2 + (-1)^2 = 1 + 9 + 1 = 11$
   Since $\|u\|^2 + \|w\|^2 = 6 + 5 = 11 = \|u - w\|^2$, the right-triangle relation holds exactly, confirming $u \perp w$.
