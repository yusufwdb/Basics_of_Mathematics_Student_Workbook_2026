# Exercise 5: Distance from Velocity

## 1. Problem Statement

The velocity of a car during the first five seconds is described by the function
$$v(t)=4t+2\quad [\mathrm{m/s}].$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

---

## 2. Theoretical Background and Concepts

- **Net Change Theorem (Displacement as Integral of Velocity):**
  Since velocity is the derivative of position, $v(t) = s'(t)$, the position $s(t)$ is an antiderivative of $v(t)$. By the Fundamental Theorem of Calculus, integrating velocity over $[t_1, t_2]$ gives the **net change in position (displacement)**:
  $$\Delta s = s(t_2) - s(t_1) = \int_{t_1}^{t_2} s'(t)\,dt = \int_{t_1}^{t_2} v(t)\,dt.$$
- **Displacement vs. Total Distance Traveled:**
  - **Displacement ($\Delta s$):** $\int_{t_1}^{t_2} v(t)\,dt$, where backward motion ($v(t) < 0$) subtracts from forward motion ($v(t) > 0$).
  - **Total Distance Traveled ($d$):** The integral of **speed** $|v(t)|$:
    $$d = \int_{t_1}^{t_2} |v(t)|\,dt.$$
    When $v(t) \ge 0$ on the entire interval $[t_1, t_2]$, speed equals velocity ($|v(t)| = v(t)$), so total distance traveled and displacement are equal.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Explaining Why the Integral of Velocity Gives the Change in Position
1. **Riemann Sum (Physical Intuition):** Divide the time interval $[0, 5]$ into many tiny subintervals of duration $\Delta t$. Over each tiny interval $[t_i, t_i + \Delta t]$, the velocity is nearly constant at $v(t_i)$, so the small change in position is approximately $\Delta s_i \approx v(t_i)\,\Delta t$. Summing these small changes over all subintervals and taking the limit as $\Delta t \to 0$ gives the definite integral $\int_0^5 v(t)\,dt = s(5) - s(0)$.
2. **Fundamental Theorem of Calculus:** Because $s'(t) = v(t)$, $s(t)$ is an antiderivative of $v(t)$, so $\int_0^5 v(t)\,dt = [s(t)]_0^5 = s(5) - s(0)$.

### Step 2: Computing the Distance Traveled Over $[0, 5]$
First, observe that on the time interval $t \in [0, 5]$, the velocity is strictly positive:
$$v(t) = 4t + 2 \ge 2 > 0 \quad \text{for all } t \in [0, 5].$$
Because the car moves exclusively forward without reversing direction, the total distance traveled $d$ equals the definite integral of $v(t)$ on $[0, 5]$:
$$\begin{aligned}
d &= \int_0^5 (4t + 2)\,dt \\
&= \left[2t^2 + 2t\right]_0^5 \\
&= \left(2(5)^2 + 2(5)\right) - \left(2(0)^2 + 2(0)\right) \\
&= (50 + 10) - 0 = 60\text{ m}.
\end{aligned}$$

### Step 3: What Must Change If the Velocity Also Takes Negative Values
If $v(t)$ took negative values on part of the interval $[0, 5]$ (meaning the car moved in reverse during that subinterval):
1. The simple definite integral $\int_0^5 v(t)\,dt = s(5) - s(0)$ would compute only the **net displacement** (final position minus initial position), because negative velocity intervals would cancel positive velocity intervals.
2. To compute the **actual (total) distance traveled** recorded by the car's odometer, we must integrate the **speed** $|v(t)|$:
   $$d = \int_0^5 |v(t)|\,dt.$$
   In practice, this requires:
   - Finding all roots $t^*$ in $(0, 5)$ where $v(t^*) = 0$ and changes sign.
   - Splitting the integral $[0, 5]$ at those roots.
   - Integrating $v(t)$ where $v(t) \ge 0$ and integrating $-v(t)$ where $v(t) < 0$, then summing the positive magnitudes of the distances traveled on each subinterval.

---

## 4. Verification and Consistency Checks

1. **Kinematics of Uniformly Accelerated Motion:**
   Here $v(t) = 4t + 2$ represents motion with initial velocity $v_0 = v(0) = 2\text{ m/s}$ and constant acceleration $a = 4\text{ m/s}^2$. Using the classical kinematic formula $d = v_0 t + \frac{1}{2}at^2$ for $t = 5\text{ s}$:
   $$d = 2(5) + \frac{1}{2}(4)(5)^2 = 10 + 50 = 60\text{ m}. \quad \checkmark$$
2. **Average Velocity / Trapezoid Area Check:**
   Since $v(t)$ is linear, the average velocity on $[0, 5]$ is the arithmetic mean of the initial velocity $v(0) = 2\text{ m/s}$ and final velocity $v(5) = 22\text{ m/s}$:
   $$v_{\text{avg}} = \frac{v(0) + v(5)}{2} = \frac{2 + 22}{2} = 12\text{ m/s}.$$
   Multiplying by the elapsed time $\Delta t = 5\text{ s}$ gives $d = 12\text{ m/s} \times 5\text{ s} = 60\text{ m}$.
