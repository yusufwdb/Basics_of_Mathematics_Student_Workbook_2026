# Exercise 13: Parametric Generalization and Budget Sensitivity Analysis (Cross-Sectional Extension of Problem 12)

## 1. Problem Statement

> **Note on Problem Set Structure:** As noted in `exercises/3_Calculus/05_applications_en.md` (*"This problem set is cross-sectional in nature and is intentionally shorter than the others"*), the exercise file contains 12 numbered problems (Problems 1–12), while the repository solution template provides 15 files (`problem_01_solution.md`–`problem_15_solution.md`). In this file (Problem 13), we present and solve the direct parametric generalization and marginal budget sensitivity analysis of the Museum Exhibition Room problem (Problem 12).

Consider the general museum exhibition room model from Problem 12, where the two walls perpendicular to the existing wall each have unit cost $c_x > 0$ per meter, the single wall parallel to the existing wall has unit cost $c_y > 0$ per meter, and the total available budget is $B > 0$:
1. Express the maximum achievable floor area $A_{\max}(B)$ and optimal dimensions $(x^*, y^*)$ in terms of the parameters $c_x, c_y, B$, and prove the **Equal Budget Split Principle**.
2. Compute the derivative $\frac{dA_{\max}}{dB}$ (the marginal area per unit of budget, or shadow price of the budget constraint) and evaluate it for the data of Problem 12 ($c_x = 300\ \mathrm{PLN/m}$, $c_y = 500\ \mathrm{PLN/m}$, $B = 30\,000\ \mathrm{PLN}$).
3. Use differential approximation to estimate the increase in maximum floor area if the museum's budget is increased by $\Delta B = 1\,000\ \mathrm{PLN}$, and compare it with the exact new maximum area.

---

## 2. Theoretical Background and Concepts

- **Parametric Optimization and Envelope / Shadow Price Interpretation:**
  When an optimization problem depends on an external parameter $B$ (such as a budget), solving the problem symbolically yields the optimal value function $A_{\max}(B)$.
- **Derivative of the Value Function ($\frac{dA_{\max}}{dB}$):**
  The derivative $\frac{dA_{\max}}{dB}$ measures the instantaneous rate at which the maximum achievable area grows per additional unit of budget ($\mathrm{m^2/PLN}$).
- **Linear (Differential) Approximation:**
  For a small change $\Delta B$ in the budget around $B_0$,
  $$\Delta A_{\max} = A_{\max}(B_0 + \Delta B) - A_{\max}(B_0) \approx A'_{\max}(B_0)\,\Delta B.$$

---

## 3. Detailed Step-by-Step Solution

### Part 1: Symbolic Optimization and the Equal Budget Split Principle
Let $x > 0$ be the length of each perpendicular wall and $y > 0$ be the length of the parallel wall.
- **General Budget Constraint:**
  $$2c_x x + c_y y = B \implies y = \frac{B - 2c_x x}{c_y}, \qquad x \in \left(0, \frac{B}{2c_x}\right).$$
- **General Area Function:**
  $$A(x) = x \cdot y = \frac{B}{c_y}x - \frac{2c_x}{c_y}x^2.$$
- **Differentiation with Respect to $x$:**
  $$A'(x) = \frac{B}{c_y} - \frac{4c_x}{c_y}x, \qquad A''(x) = -\frac{4c_x}{c_y} < 0.$$
  Setting $A'(x) = 0$ gives the unique global maximum on $\left(0, \frac{B}{2c_x}\right)$:
  $$x^* = \frac{B}{4c_x}, \qquad y^* = \frac{B - 2c_x\left(\frac{B}{4c_x}\right)}{c_y} = \frac{B}{2c_y}.$$
- **Proof of the Equal Budget Split Principle:**
  - Total expenditure on the two perpendicular walls: $2c_x x^* = 2c_x\left(\frac{B}{4c_x}\right) = \frac{B}{2}$.
  - Total expenditure on the parallel wall: $c_y y^* = c_y\left(\frac{B}{2c_y}\right) = \frac{B}{2}$.
  Regardless of the specific prices $c_x$ and $c_y$, maximizing the rectangular area **always allocates exactly $50\%$ of the budget to the perpendicular walls and $50\%$ to the parallel wall**!
- **Maximum Area as a Function of Budget $B$:**
  $$A_{\max}(B) = x^* y^* = \left(\frac{B}{4c_x}\right)\left(\frac{B}{2c_y}\right) = \frac{B^2}{8c_x c_y}.$$

---

### Part 2: Computing the Marginal Area $\frac{dA_{\max}}{dB}$
Differentiating $A_{\max}(B) = \frac{B^2}{8c_x c_y}$ with respect to the budget $B$:
$$\frac{dA_{\max}}{dB} = \frac{2B}{8c_x c_y} = \frac{B}{4c_x c_y}.$$
Substituting the parameters from Problem 12 ($c_x = 300\ \mathrm{PLN/m}$, $c_y = 500\ \mathrm{PLN/m}$, $B = 30\,000\ \mathrm{PLN}$):
$$\frac{dA_{\max}}{dB}(30\,000) = \frac{30\,000}{4 \times 300 \times 500} = \frac{30\,000}{600\,000} = \frac{1}{20} = 0.05\ \mathrm{m^2/PLN}.$$
At the current budget of $30\,000\ \mathrm{PLN}$, each additional $1\ \mathrm{PLN}$ of budget increases the maximum floor area at a rate of $0.05\ \mathrm{m^2}$ (i.e., $20\ \mathrm{PLN}$ per additional $\mathrm{m^2}$ at the margin).

---

### Part 3: Estimating the Area Gain for $\Delta B = 1\,000\ \mathrm{PLN}$
1. **Linear (Differential) Estimate:**
   $$\Delta A_{\max} \approx \frac{dA_{\max}}{dB}(30\,000) \cdot \Delta B = 0.05\ \mathrm{m^2/PLN} \times 1\,000\ \mathrm{PLN} = 50\ \mathrm{m^2},$$
   giving an estimated new area of $750 + 50 = 800\ \mathrm{m^2}$.
2. **Exact New Maximum Area at $B_1 = 31\,000\ \mathrm{PLN}$:**
   $$A_{\max}(31\,000) = \frac{(31\,000)^2}{8 \times 300 \times 500} = \frac{961\,000\,000}{1\,200\,000} = \frac{9610}{12} = 800.833...\ \mathrm{m^2}.$$
    Thus the exact gain is $\Delta A_{\max,\text{exact}} = 800.8\overline{3} - 750 = 50.8\overline{3}\ \mathrm{m^2}$.

---

## 4. Verification and Consistency Checks

1. **Consistency with Problem 12:**
   Substituting $B = 30\,000$, $c_x = 300$, $c_y = 500$ into our general formulas gives:
   $$x^* = \frac{30\,000}{4 \times 300} = 25\ \mathrm{m}, \quad y^* = \frac{30\,000}{2 \times 500} = 30\ \mathrm{m}, \quad A_{\max} = \frac{(30\,000)^2}{1\,200\,000} = 750\ \mathrm{m^2},$$
   reproducing the exact solution of Problem 12.
2. **Quadratic Scaling Check:**
   Because linear dimensions $(x^*, y^*)$ scale linearly with $B$ ($x^*, y^* \propto B$), the area $A_{\max} = x^* y^*$ scales **quadratically** with $B$ ($A_{\max} \propto B^2$). Using the exact second-order Taylor expansion:
   $$\Delta A_{\max} = A'_{\max}(B_0)\Delta B + \frac{1}{2}A''_{\max}(B_0)(\Delta B)^2 = 0.05(1000) + \frac{1}{2}\left(\frac{1}{600\,000}\right)(1000)^2 = 50 + \frac{5}{6} = 50.8\overline{3}\ \mathrm{m^2},$$
   which accounts for the exact $0.8\overline{3}\ \mathrm{m^2}$ difference between the linear approximation and the exact new maximum!
