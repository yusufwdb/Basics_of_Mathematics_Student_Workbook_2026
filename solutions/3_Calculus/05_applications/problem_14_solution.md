# Exercise 14: Kinematics with Velocity Sign Change — Displacement vs. Total Distance (Cross-Sectional Problem)

## 1. Problem Statement

> **Note on Problem Set Structure:** As noted in `exercises/3_Calculus/05_applications_en.md` (*"This problem set is cross-sectional in nature and is intentionally shorter than the others"*), the exercise file contains 12 numbered problems (Problems 1–12), while the repository solution template provides 15 files (`problem_01_solution.md`–`problem_15_solution.md`). In this file (Problem 14), we formulate and solve a complete cross-sectional problem that directly bridges Problem 1 (motion with stopping points) and the final question of Problem 5 (computing distance when velocity takes negative values).

A particle moves along a coordinate axis with velocity given by
$$v(t) = 3t^2 - 12t + 9\quad [\mathrm{m/s}], \qquad t \in [0, 4]\ [\mathrm{s}],$$
and initial position $s(0) = 2\ \mathrm{m}$.
1. Recover the position function $s(t)$ by integration using the initial condition $s(0) = 2$.
2. Compute the **net displacement** $\Delta s = \int_0^4 v(t)\,dt$ over the time interval $[0, 4]$.
3. Compute the **total distance traveled** $d = \int_0^4 |v(t)|\,dt$ over $[0, 4]$ by splitting the integral at the points where $v(t)$ changes sign, and compare $d$ with $\Delta s$.

---

## 2. Theoretical Background and Concepts

- **Recovering Position from Velocity (Initial Value Problem):**
  Since $s'(t) = v(t)$, the position function is given by
  $$s(t) = s(0) + \int_0^t v(\tau)\,d\tau.$$
- **Displacement vs. Total Distance When Velocity Changes Sign:**
  - **Net Displacement:** $\Delta s = s(b) - s(a) = \int_a^b v(t)\,dt$. Forward and backward segments cancel.
  - **Total Distance Traveled:** $d = \int_a^b |v(t)|\,dt$. When $v(t) < 0$ on a subinterval $[t_1, t_2]$, we integrate $-v(t)$ on $[t_1, t_2]$ so that all segments of motion contribute positively.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Recovering the Position Function $s(t)$
We integrate the velocity $v(t) = 3t^2 - 12t + 9$:
$$s(t) = \int (3t^2 - 12t + 9)\,dt = t^3 - 6t^2 + 9t + C.$$
Using the initial condition $s(0) = 2$:
$$s(0) = 0^3 - 6(0)^2 + 9(0) + C = 2 \implies C = 2.$$
Therefore, the position function is:
$$s(t) = t^3 - 6t^2 + 9t + 2\quad [\mathrm{m}],$$
which is the exact motion trajectory studied in Problem 1.

---

### Part 2: Computing the Net Displacement $\Delta s$ on $[0, 4]$
Evaluating the definite integral of $v(t)$ from $t = 0$ to $t = 4$:
$$\begin{aligned}
\Delta s &= \int_0^4 (3t^2 - 12t + 9)\,dt \\
&= \left[t^3 - 6t^2 + 9t\right]_0^4 \\
&= \left(4^3 - 6(4)^2 + 9(4)\right) - 0 \\
&= 64 - 96 + 36 = 4\ \mathrm{m}.
\end{aligned}$$
At $t = 4\ \mathrm{s}$, the particle is located at $s(4) = s(0) + \Delta s = 2 + 4 = 6\ \mathrm{m}$, which is $4\ \mathrm{m}$ in the positive direction from its starting point $s(0) = 2\ \mathrm{m}$.

---

### Part 3: Computing the Total Distance Traveled $d$ on $[0, 4]$
First, we find where $v(t)$ changes sign on $[0, 4]$ by factoring $v(t)$:
$$v(t) = 3(t^2 - 4t + 3) = 3(t - 1)(t - 3) = 0 \implies t = 1\ \mathrm{s} \text{ and } t = 3\ \mathrm{s}.$$
- On $[0, 1]$: $v(t) \ge 0$, so $|v(t)| = v(t)$.
- On $[1, 3]$: $v(t) \le 0$, so $|v(t)| = -v(t)$.
- On $[3, 4]$: $v(t) \ge 0$, so $|v(t)| = v(t)$.

Splitting $\int_0^4 |v(t)|\,dt$ at $t = 1$ and $t = 3$:
$$d = \int_0^1 v(t)\,dt - \int_1^3 v(t)\,dt + \int_3^4 v(t)\,dt.$$
Using the antiderivative $F(t) = t^3 - 6t^2 + 9t$ (where $F(0) = 0$, $F(1) = 4$, $F(3) = 0$, $F(4) = 4$):
1. Distance on $[0, 1]$ (forward):
   $$d_1 = \int_0^1 (3t^2 - 12t + 9)\,dt = F(1) - F(0) = 4 - 0 = 4\ \mathrm{m}.$$
2. Distance on $[1, 3]$ (backward):
   $$d_2 = -\int_1^3 (3t^2 - 12t + 9)\,dt = -(F(3) - F(1)) = -(0 - 4) = 4\ \mathrm{m}.$$
3. Distance on $[3, 4]$ (forward):
   $$d_3 = \int_3^4 (3t^2 - 12t + 9)\,dt = F(4) - F(3) = 4 - 0 = 4\ \mathrm{m}.$$

Summing the three positive distances:
$$d = d_1 + d_2 + d_3 = 4 + 4 + 4 = 12\ \mathrm{m}.$$

**Comparison:** The net displacement is $\Delta s = 4 - 4 + 4 = 4\ \mathrm{m}$, whereas the actual total distance traveled is $d = 4 + 4 + 4 = 12\ \mathrm{m}$, because the particle traveled $4\ \mathrm{m}$ forward (from $x=2$ to $x=6$), then $4\ \mathrm{m}$ backward (from $x=6$ back to $x=2$), and finally $4\ \mathrm{m}$ forward again (from $x=2$ to $x=6$).

---

## 4. Verification and Consistency Checks

We verify using the position values $s(t) = t^3 - 6t^2 + 9t + 2$ from Problem 1:
- $s(0) = 2\ \mathrm{m}$, $s(1) = 6\ \mathrm{m}$, $s(3) = 2\ \mathrm{m}$, $s(4) = 6\ \mathrm{m}$.
- Net displacement: $s(4) - s(0) = 6 - 2 = 4\ \mathrm{m}$. $\checkmark$
- Sum of segment lengths along the trajectory:
  $$|s(1) - s(0)| + |s(3) - s(1)| + |s(4) - s(3)| = |6 - 2| + |2 - 6| + |6 - 2| = 4 + 4 + 4 = 12\ \mathrm{m}. \quad \checkmark$$
Both differentiation/position tracking and definite integration yield identical results.
