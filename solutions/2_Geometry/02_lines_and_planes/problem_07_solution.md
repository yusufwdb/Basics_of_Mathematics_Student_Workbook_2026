# Exercise 7: A Line Relative to a Plane

## 1. Problem Statement

For
$$L:(x,y,z)=(1,1,0)+t(1,-1,0),\qquad \Pi:x+y+z=2,$$
determine whether the line intersects the plane at one point, is parallel to it, or lies in it. Explain the role of the dot product of the direction vector and the normal vector.

## 2. Theoretical Background and Concepts

Consider a line $L: p_0 + t v$ ($t \in \mathbb{R}$) with initial point $p_0$ and direction vector $v$, and a plane $\Pi: n \cdot x = d$ with normal vector $n$.
Substituting $x = p_0 + t v$ into the plane equation yields a single linear equation in $t$:
$$n \cdot (p_0 + t v) = d \iff (n \cdot v)\, t = d - n \cdot p_0$$

1. **Case 1 ($n \cdot v \neq 0$):** The direction vector $v$ is not perpendicular to $n$, so $L$ is not parallel to $\Pi$ and intersects $\Pi$ at the unique point given by $t = \frac{d - n \cdot p_0}{n \cdot v}$.
2. **Case 2 ($n \cdot v = 0$ and $n \cdot p_0 \neq d$):** The direction vector $v$ is parallel to $\Pi$, and the initial point $p_0 \notin \Pi$, so the equation $0 \cdot t = d - n \cdot p_0 \neq 0$ has **no solution** ($L$ is strictly parallel to $\Pi$, with $L \cap \Pi = \emptyset$).
3. **Case 3 ($n \cdot v = 0$ and $n \cdot p_0 = d$):** The direction vector $v$ is parallel to $\Pi$, and the initial point $p_0 \in \Pi$, so $0 \cdot t = 0$ holds for **all $t \in \mathbb{R}$** ($L$ lies entirely inside $\Pi$, i.e., $L \subset \Pi$).

## 3. Detailed Step-by-Step Solution

Given:
- Line $L: (x, y, z) = (1, 1, 0) + t(1, -1, 0)$, with reference point $P_0 = (1, 1, 0)$ and direction vector $v = (1, -1, 0)$.
- Plane $\Pi: x + y + z = 2$, with normal vector $n = (1, 1, 1)$ and right-hand side $d = 2$.

### Step 1: Compute the dot product $n \cdot v$
$$n \cdot v = (1, 1, 1) \cdot (1, -1, 0) = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0$$
Because $n \cdot v = 0$, the direction vector $v$ of the line is orthogonal to the normal vector $n$ of the plane. This means the direction of $L$ is **parallel to the plane $\Pi$**, so $L$ either lies entirely in $\Pi$ or is strictly parallel to $\Pi$ with no common points.

### Step 2: Check whether the initial point $P_0 = (1, 1, 0)$ lies in $\Pi$
Substitute $P_0 = (1, 1, 0)$ into the plane equation $x + y + z = 2$:
$$n \cdot P_0 = 1 + 1 + 0 = 2 = d \quad \checkmark$$
Since $P_0 = (1, 1, 0)$ satisfies $x + y + z = 2$, and the direction $v$ is parallel to $\Pi$, **every point on $L$ lies in $\Pi$**.
Conclusion: **The line $L$ lies entirely in the plane $\Pi$ ($L \subset \Pi$).**

### Step 3: Explain the role of the dot product $n \cdot v$
The normal vector $n$ points perpendicular to the plane $\Pi$, so the plane's directions are precisely those vectors orthogonal to $n$.
- The dot product $n \cdot v = \|n\|\,\|v\|\cos\alpha$ measures the rate of change of the quantity $n \cdot x$ as a point $x = p_0 + t v$ moves along the line $L$ (since $\frac{d}{dt}(n \cdot (p_0 + tv)) = n \cdot v$).
- If $n \cdot v \neq 0$, moving along the line changes the height relative to the plane, forcing the line to cross the plane at exactly one value of $t$.
- If $n \cdot v = 0$, moving along the line keeps $n \cdot x$ constant (parallel to the plane); whether the line lies inside the plane or misses it completely then depends only on whether a single point $p_0$ of the line starts on the plane ($n \cdot p_0 = d$).

## 4. Verification and Consistency Checks

**Direct Parametric Substitution Check for All $t \in \mathbb{R}$:**
An arbitrary point on $L$ has coordinates:
$$x = 1 + t, \qquad y = 1 - t, \qquad z = 0$$
Substituting these coordinates into the left-hand side of $\Pi: x + y + z = 2$:
$$x + y + z = (1 + t) + (1 - t) + 0 = 2 + (t - t) = 2 \quad \forall t \in \mathbb{R} \quad \checkmark$$
Because the equation $2 = 2$ is satisfied identically for every real number $t \in \mathbb{R}$, the entire line $L$ is contained in $\Pi$.
