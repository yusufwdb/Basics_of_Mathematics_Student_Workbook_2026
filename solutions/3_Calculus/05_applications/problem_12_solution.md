# Exercise 12: Complete Model and Computer Verification

## 1. Problem Statement

A museum wants to create a rectangular exhibition room next to an existing straight wall. The side along the wall does not need to be built. The remaining three sides are to be constructed to two different standards: the two sides perpendicular to the wall cost $300\ \mathrm{PLN/m}$ each, while the side parallel to the wall costs $500\ \mathrm{PLN/m}$. The budget is $30\,000\ \mathrm{PLN}$.

Build a model that maximizes the area of the room and prepare a complete analysis containing:
- definition of variables and units,
- mathematical model,
- domain resulting from the problem statement,
- computation of the derivative,
- determination and verification of the optimum,
- interpretation of the result,
- graph of the objective function,
- numerical verification of several values near the optimum found.

Finally, indicate which part of the solution required modeling the problem and which part was only the execution of the calculation. Produce the graph and computer calculations only after completing the mathematical solution, and treat them as verification.

---

## 2. Theoretical Background and Concepts

- **Constrained Economic-Geometric Optimization:**
  Unlike standard perimeter-constrained problems where all sides have equal weight, here the constraint is a **linear budget equation** with unequal unit prices ($300\text{ PLN/m}$ vs. $500\text{ PLN/m}$).
  1. **Budget utilization:** To maximize the enclosed rectangular area $A = xy$, the entire available budget of $30\,000\text{ PLN}$ must be used (any unused budget could be used to lengthen the walls and increase the area).
  2. **Reduction to one variable:** Express one dimension in terms of the other via the budget equation, establish the feasible interval where both dimensions are positive, and use differential calculus ($A'(x) = 0$, $A''(x) < 0$) to locate and prove the global maximum.

---

## 3. Detailed Step-by-Step Solution

### 1. Definition of Variables and Units
```
       ================== Existing Straight Wall ==================
       |                                                          |
     x | (300 PLN/m)         Exhibition Room          (300 PLN/m) | x
       |                         Area A = xy                      |
       +----------------------------------------------------------+
                             y (500 PLN/m)
```
- Let $x\ [\mathrm{m}]$ be the length of each of the **two sides perpendicular** to the existing wall.
- Let $y\ [\mathrm{m}]$ be the length of the **single side parallel** to the existing wall.
- Let $A\ [\mathrm{m^2}]$ be the floor area of the rectangular exhibition room.
- Unit costs: $c_x = 300\ \mathrm{PLN/m}$ for each perpendicular wall, $c_y = 500\ \mathrm{PLN/m}$ for the parallel wall, and total budget $B = 30\,000\ \mathrm{PLN}$.

---

### 2. Mathematical Model
- **Cost Constraint:** There are two perpendicular walls of length $x$ (costing $2 \times 300x = 600x\ \mathrm{PLN}$) and one parallel wall of length $y$ (costing $500y\ \mathrm{PLN}$). Using the full budget of $30\,000\ \mathrm{PLN}$ gives:
  $$600x + 500y = 30\,000.$$
  Dividing both sides by $100$:
  $$6x + 5y = 300 \implies y = \frac{300 - 6x}{5} = 60 - \frac{6}{5}x = 60 - 1.2x.$$
- **Objective Function (Area to Maximize):**
  Substituting $y = 60 - \frac{6}{5}x$ into $A = x \cdot y$ gives the single-variable objective function:
  $$A(x) = x\left(60 - \frac{6}{5}x\right) = 60x - \frac{6}{5}x^2 = 60x - 1.2x^2\quad [\mathrm{m^2}].$$

---

### 3. Domain Resulting from the Problem Statement
For the exhibition room to be a physically meaningful rectangle, both side lengths $x$ and $y$ must be strictly positive:
$$x > 0 \quad \text{and} \quad y = 60 - \frac{6}{5}x > 0 \implies \frac{6}{5}x < 60 \implies x < 50.$$
Therefore, the feasible domain of the objective function $A(x)$ is the open interval:
$$D_A = (0, 50)\quad [\mathrm{m}].$$

---

### 4. Computation of the Derivative
Differentiating $A(x) = 60x - \frac{6}{5}x^2$ with respect to $x$ on $(0, 50)$:
$$A'(x) = \frac{d}{dx}\left(60x - \frac{6}{5}x^2\right) = 60 - \frac{12}{5}x = 60 - 2.4x.$$

---

### 5. Determination and Verification of the Optimum
- **Finding the critical point:** Setting $A'(x) = 0$:
  $$60 - \frac{12}{5}x = 0 \implies \frac{12}{5}x = 60 \implies x^* = \frac{60 \times 5}{12} = 25\ \mathrm{m} \in (0, 50).$$
- **Verification of Global Maximum:**
  1. **First Derivative Sign Test:**
     - For $x \in (0, 25)$, $A'(x) = 60 - 2.4x > 0$, so $A(x)$ is strictly increasing on $(0, 25]$.
     - For $x \in (25, 50)$, $A'(x) = 60 - 2.4x < 0$, so $A(x)$ is strictly decreasing on $[25, 50)$.
  2. **Second Derivative Test:**
     $$A''(x) = -\frac{12}{5} = -2.4 < 0 \quad \text{for all } x \in (0, 50).$$
     Because $A''(x) < 0$ everywhere on the domain, $A(x)$ is strictly concave and $x^* = 25\ \mathrm{m}$ is the unique **global maximum**.
- **Optimal second dimension and maximum area:**
  $$y^* = 60 - \frac{6}{5}(25) = 60 - 30 = 30\ \mathrm{m},$$
  $$A_{\max} = A(25) = 25\ \mathrm{m} \times 30\ \mathrm{m} = 750\ \mathrm{m^2}.$$

---

### 6. Interpretation of the Result
To achieve the largest possible exhibition room floor area of **$750\ \mathrm{m^2}$** within the $30\,000\ \mathrm{PLN}$ budget:
- The two walls perpendicular to the existing wall should each have length **$x^* = 25\ \mathrm{m}$** (costing $2 \times 25 \times 300 = 15\,000\ \mathrm{PLN}$, exactly half the budget).
- The wall parallel to the existing wall should have length **$y^* = 30\ \mathrm{m}$** (costing $30 \times 500 = 15\,000\ \mathrm{PLN}$, the other half of the budget).
- Notice the economic symmetry principle: at the optimum, the total budget is split **equally ($15\,000\ \mathrm{PLN}$ each)** between the total cost of the perpendicular walls ($600x^*$) and the cost of the parallel wall ($500y^*$).

---

### 7. Distinction: Modeling vs. Execution of Calculation
- **Modeling the problem (translating reality into mathematics):**
  1. Recognizing that only $3$ sides require construction and introducing variables $x$ and $y$ with appropriate units.
  2. Formulating the budget constraint $600x + 500y = 30\,000$ and the area objective $A = xy$.
  3. Determining the physical domain $x \in (0, 50)$ from positivity requirements $x > 0, y > 0$.
  4. Interpreting the mathematical output $(x^*, y^*, A_{\max}) = (25, 30, 750)$ back in architectural and financial terms.
- **Execution of the calculation (purely mathematical procedure):**
  1. Solving the linear equation $600x + 500y = 30\,000$ for $y = 60 - 1.2x$ and expanding $A(x) = 60x - 1.2x^2$.
  2. Computing the derivatives $A'(x) = 60 - 2.4x$ and $A''(x) = -2.4$.
  3. Solving the linear equation $60 - 2.4x = 0 \implies x = 25$ and evaluating $A(25) = 750$.

---

## 4. Verification and Consistency Checks

### 1. Graph of the Objective Function $A(x) = 60x - 1.2x^2$ on $(0, 50)$
The graph is a downward-opening parabola with roots at $x = 0$ and $x = 50$, symmetric about its vertex at $(25, 750)$:

```
    A(x) [m^2]
     750 |                     * (25, 750) [Maximum]
     700 |                *    :    *
     600 |            *        :        *
     480 |         *           :           *
     300 |      *              :              *
     100 |   *                 :                 *
       0 +---*-----------------+-----------------*---> x [m]
         0   5        10       25       40       50
```

### 2. Numerical Verification Table Near the Optimum $x^* = 25\ \mathrm{m}$
We compute $y(x) = 60 - 1.2x$, the total cost $600x + 500y$, and the resulting area $A(x) = xy$ for several values of $x$ around $x^* = 25\ \mathrm{m}$:

| $x\ [\mathrm{m}]$ | $y = 60 - 1.2x\ [\mathrm{m}]$ | Cost $600x + 500y\ [\mathrm{PLN}]$ | Area $A(x) = xy\ [\mathrm{m^2}]$ | Difference from $A_{\max}$ |
| :---: | :---: | :---: | :---: | :---: |
| $20.0$ | $36.0$ | $12\,000 + 18\,000 = 30\,000$ | $720.00$ | $-30.00\ \mathrm{m^2}$ |
| $24.0$ | $31.2$ | $14\,400 + 15\,600 = 30\,000$ | $748.80$ | $-1.20\ \mathrm{m^2}$ |
| $24.5$ | $30.6$ | $14\,700 + 15\,300 = 30\,000$ | $749.70$ | $-0.30\ \mathrm{m^2}$ |
| $24.9$ | $30.12$ | $14\,940 + 15\,060 = 30\,000$ | $749.988$ | $-0.012\ \mathrm{m^2}$ |
| **$25.0$** | **$30.0$** | **$15\,000 + 15\,000 = 30\,000$** | **$750.00$** | **$0.00\ \mathrm{m^2}$ (Max)** |
| $25.1$ | $29.88$ | $15\,060 + 14\,940 = 30\,000$ | $749.988$ | $-0.012\ \mathrm{m^2}$ |
| $25.5$ | $29.4$ | $15\,300 + 14\,700 = 30\,000$ | $749.70$ | $-0.30\ \mathrm{m^2}$ |
| $26.0$ | $28.8$ | $15\,600 + 14\,400 = 30\,000$ | $748.80$ | $-1.20\ \mathrm{m^2}$ |
| $30.0$ | $24.0$ | $18\,000 + 12\,000 = 30\,000$ | $720.00$ | $-30.00\ \mathrm{m^2}$ |

Every perturbation $x = 25 \pm \delta$ reduces the area by exactly $1.2\delta^2\ \mathrm{m^2}$ (since $A(25 \pm \delta) = 750 - 1.2\delta^2$), confirming that $x^* = 25\ \mathrm{m}$, $y^* = 30\ \mathrm{m}$, $A_{\max} = 750\ \mathrm{m^2}$ is the exact global maximum.
