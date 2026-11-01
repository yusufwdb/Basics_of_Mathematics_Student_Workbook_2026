# Exercise 15: Combining Integration and Optimization — From Marginal Rates to Maximum Profit (Cross-Sectional Synthesis)

## 1. Problem Statement

> **Note on Problem Set Structure:** As noted in `exercises/3_Calculus/05_applications_en.md` (*"This problem set is cross-sectional in nature and is intentionally shorter than the others"*), the exercise file contains 12 numbered problems (Problems 1–12), while the repository solution template provides 15 files (`problem_01_solution.md`–`problem_15_solution.md`). In this file (Problem 15), we present and solve a capstone cross-sectional problem that requires **both** integration and differentiation in a single model—recovering total functions from marginal rates via integration and optimizing the resulting objective function.

A software company offers cloud compute units. For a daily production level of $x \ge 0$ thousand units:
- The **marginal revenue** (rate of change of revenue with respect to $x$) is
  $$R'(x) = 60 - 2x \quad [\text{thousand PLN per thousand units}].$$
- The **marginal cost** (rate of change of cost with respect to $x$) is
  $$C'(x) = 12 + x^2 \quad [\text{thousand PLN per thousand units}].$$
- Fixed daily overhead costs are $C(0) = 20$ thousand PLN, and revenue at zero production is $R(0) = 0$.

1. Decide which calculus tool (derivative or integral) is needed to find the total revenue $R(x)$, total cost $C(x)$, and total profit $P(x) = R(x) - C(x)$, and determine their explicit formulas.
2. Find the daily production level $x^* > 0$ that maximizes the total daily profit $P(x)$, justify that it is a global maximum on $[0, \infty)$, and compute the maximum profit.
3. Interpret the optimality condition $P'(x^*) = 0$ in terms of the area between the marginal revenue curve $y = R'(x)$ and the marginal cost curve $y = C'(x)$ on $[0, x^*]$.

---

## 2. Theoretical Background and Concepts

- **From Marginal Rates to Total Quantities (Integration):**
  In economics and operations research, "marginal" means the derivative with respect to production quantity $x$. Given $R'(x)$ and $C'(x)$ along with initial values $R(0)$ and $C(0)$, we recover the total functions via definite/indefinite integration:
  $$R(x) = R(0) + \int_0^x R'(t)\,dt, \qquad C(x) = C(0) + \int_0^x C'(t)\,dt.$$
- **Profit Maximization (Differentiation):**
  Total profit is $P(x) = R(x) - C(x)$. By the Fundamental Theorem of Calculus, its derivative is the marginal profit:
  $$P'(x) = R'(x) - C'(x).$$
  Thus, profit is maximized at the critical point $x^* > 0$ where marginal revenue equals marginal cost ($R'(x^*) = C'(x^*)$) and $P''(x^*) < 0$.
- **Net Profit Gain as Area Between Curves:**
  $$P(x^*) - P(0) = \int_0^{x^*} \left(R'(x) - C'(x)\right)\,dx.$$

---

## 3. Detailed Step-by-Step Solution

### Part 1: Recovering Total Revenue $R(x)$, Total Cost $C(x)$, and Total Profit $P(x)$
Because we are given rates of change $R'(x)$ and $C'(x)$ and want to find the total accumulated quantities, we use **integration** with initial conditions:

1. **Total Revenue $R(x)$:**
   $$R(x) = R(0) + \int_0^x (60 - 2t)\,dt = 0 + \left[60t - t^2\right]_0^x = 60x - x^2 \quad [\text{thousand PLN}].$$
2. **Total Cost $C(x)$:**
   $$C(x) = C(0) + \int_0^x (12 + t^2)\,dt = 20 + \left[12t + \frac{1}{3}t^3\right]_0^x = \frac{1}{3}x^3 + 12x + 20 \quad [\text{thousand PLN}].$$
3. **Total Profit $P(x) = R(x) - C(x)$:**
   $$P(x) = \left(60x - x^2\right) - \left(\frac{1}{3}x^3 + 12x + 20\right) = -\frac{1}{3}x^3 - x^2 + 48x - 20 \quad [\text{thousand PLN}].$$

---

### Part 2: Finding and Verifying the Profit-Maximizing Production Level $x^*$
To maximize $P(x)$ on $[0, \infty)$, we use **differentiation**. By construction, the derivative of $P(x)$ is $P'(x) = R'(x) - C'(x)$:
$$P'(x) = (60 - 2x) - (12 + x^2) = -x^2 - 2x + 48 = -(x^2 + 2x - 48) = -(x + 8)(x - 6).$$
Setting $P'(x) = 0$ yields $x = -8$ (outside the domain $x \ge 0$) or
$$x^* = 6 \quad [\text{thousand units}].$$

**Justification of Global Maximum on $[0, \infty)$:**
- For $x \in [0, 6)$, $(x+8) > 0$ and $(x-6) < 0 \implies P'(x) > 0$, so $P(x)$ is strictly increasing on $[0, 6]$.
- For $x \in (6, \infty)$, $(x+8) > 0$ and $(x-6) > 0 \implies P'(x) < 0$, so $P(x)$ is strictly decreasing on $[6, \infty)$.
- Also, $P''(x) = -2x - 2 < 0$ for all $x \ge 0$ (in particular $P''(6) = -14 < 0$), so $P(x)$ is strictly concave on $[0, \infty)$.

**Maximum Daily Profit:**
Evaluating $P(x)$ at $x^* = 6$:
$$\begin{aligned}
P(6) &= -\frac{1}{3}(6)^3 - (6)^2 + 48(6) - 20 \\
&= -72 - 36 + 288 - 20 \\
&= 160\text{ thousand PLN} = 160\,000\ \mathrm{PLN}.
\end{aligned}$$

---

### Part 3: Geometric Interpretation via the Area Between $R'(x)$ and $C'(x)$
At the optimal output $x^* = 6$, the marginal revenue and marginal cost curves intersect:
$$R'(6) = 60 - 2(6) = 48, \qquad C'(6) = 12 + 6^2 = 48.$$
- On the interval $[0, 6)$, we have $R'(x) > C'(x)$: every additional unit produced adds more to revenue than to cost, contributing positively to the area between the curves:
  $$\text{Area} = \int_0^6 \left(R'(x) - C'(x)\right)\,dx = \int_0^6 (-x^2 - 2x + 48)\,dx = \left[-\frac{1}{3}x^3 - x^2 + 48x\right]_0^6 = -72 - 36 + 288 = 180\text{ thousand PLN}.$$
- Subtracting the fixed cost $C(0) = 20$ thousand PLN (since $P(0) = -20$) gives the maximum net profit:
  $$P(6) = P(0) + \int_0^6 \left(R'(x) - C'(x)\right)\,dx = -20 + 180 = 160\text{ thousand PLN}.$$
- If production were pushed beyond $x^* = 6$, $C'(x)$ would exceed $R'(x)$, creating negative signed area that would subtract from the accumulated profit.

---

## 4. Verification and Consistency Checks

1. **Direct Revenue Minus Cost Check at $x^* = 6$:**
   - $R(6) = 60(6) - 6^2 = 360 - 36 = 324$ thousand PLN.
   - $C(6) = \frac{1}{3}(6)^3 + 12(6) + 20 = 72 + 72 + 20 = 164$ thousand PLN.
   - $P(6) = R(6) - C(6) = 324 - 164 = 160$ thousand PLN. $\checkmark$
2. **Neighboring Values Check:**
   - At $x = 5$: $P(5) = -\frac{125}{3} - 25 + 240 - 20 = 153.\overline{3} < 160$.
   - At $x = 7$: $P(7) = -\frac{343}{3} - 49 + 336 - 20 = 152.\overline{6} < 160$.
   Both neighboring production levels yield strictly lower profit, confirming the optimum at $x^* = 6$.
