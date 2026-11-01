# Exercise 1: Motion — from Position to Velocity

## 1. Problem Statement

The position of a point is described by
$$s(t)=t^3-6t^2+9t+2,\qquad t\ge0.$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

---

## 2. Theoretical Background and Concepts

- **Kinematic Derivatives (One-Dimensional Motion):**
  - **Position $s(t)$:** Location of the particle along the coordinate axis at time $t \ge 0$.
  - **Instantaneous Velocity $v(t)$:** The first derivative of position with respect to time, measuring the instantaneous rate of change of position:
    $$v(t) = s'(t) = \frac{ds}{dt}.$$
  - **Instantaneous Acceleration $a(t)$:** The derivative of velocity (and second derivative of position) with respect to time:
    $$a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}.$$
- **Physical Interpretation of the Sign of $v(t)$:**
  - $v(t) = 0$: The particle is instantaneously at rest (stopped).
  - $v(t) > 0$: $s(t)$ is strictly increasing, meaning the particle moves in the **positive direction** of the coordinate axis.
  - $v(t) < 0$: $s(t)$ is strictly decreasing, meaning the particle moves in the **negative direction** of the coordinate axis.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Determining the Velocity and Acceleration
Differentiating $s(t) = t^3 - 6t^2 + 9t + 2$ with respect to $t$ ($t \ge 0$) gives the velocity function:
$$v(t) = s'(t) = \frac{d}{dt}\left(t^3 - 6t^2 + 9t + 2\right) = 3t^2 - 12t + 9.$$
Differentiating $v(t)$ with respect to $t$ gives the acceleration function:
$$a(t) = v'(t) = s''(t) = \frac{d}{dt}\left(3t^2 - 12t + 9\right) = 6t - 12.$$

### Part 2: Finding the Times at Which the Point Stops
The point stops when its instantaneous velocity is zero, $v(t) = 0$. We factor $v(t)$:
$$\begin{aligned}
3t^2 - 12t + 9 &= 0 \\
3(t^2 - 4t + 3) &= 0 \\
3(t - 1)(t - 3) &= 0.
\end{aligned}$$
Since both roots lie in the domain $t \ge 0$, the point stops at two instants:
$$t_1 = 1 \quad \text{and} \quad t_2 = 3.$$

### Part 3: Intervals of Motion in the Positive and Negative Directions
We analyze the sign of $v(t) = 3(t - 1)(t - 3)$ on the domain $[0, \infty)$ split by the roots $t = 1$ and $t = 3$:

| Interval | Sign of $(t-1)$ | Sign of $(t-3)$ | Sign of $v(t) = 3(t-1)(t-3)$ | Direction of Motion |
| :--- | :---: | :---: | :---: | :--- |
| $[0, 1)$ | $-$ | $-$ | $+$ | **Positive direction** (forward) |
| $t = 1$ | $0$ | $-$ | $0$ | Stopped (reverses from $+$ to $-$) |
| $(1, 3)$ | $+$ | $-$ | $-$ | **Negative direction** (backward) |
| $t = 3$ | $+$ | $0$ | $0$ | Stopped (reverses from $-$ to $+$) |
| $(3, \infty)$ | $+$ | $+$ | $+$ | **Positive direction** (forward) |

- **Motion in the positive direction ($v(t) > 0$):** for $t \in [0, 1) \cup (3, \infty)$.
- **Motion in the negative direction ($v(t) < 0$):** for $t \in (1, 3)$.

---

## 4. Verification and Consistency Checks

We evaluate the position $s(t) = t^3 - 6t^2 + 9t + 2$ at the start and at the turning points:
- At $t = 0$: $s(0) = 0 - 0 + 0 + 2 = 2$.
- At $t = 1$: $s(1) = 1 - 6 + 9 + 2 = 6$. Since $s(1) = 6 > s(0) = 2$, the point moved in the positive direction from $x = 2$ to $x = 6$ during $[0, 1]$.
- At $t = 3$: $s(3) = 27 - 54 + 27 + 2 = 2$. Since $s(3) = 2 < s(1) = 6$, the point moved backward (in the negative direction) from $x = 6$ to $x = 2$ during $[1, 3]$.
- At $t = 4$: $s(4) = 64 - 96 + 36 + 2 = 6 > s(3) = 2$, confirming motion in the positive direction for $t > 3$.
- Also note that $a(1) = 6(1) - 12 = -6 < 0$ (local maximum of $s(t)$ at $t = 1$) and $a(3) = 6(3) - 12 = 6 > 0$ (local minimum of $s(t)$ at $t = 3$), which is fully consistent with the sign changes of $v(t)$.
