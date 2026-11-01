# Exercise 11: A Parameter and the Number of Extrema

## 1. Problem Statement
For
$$f_a(x)=x^3-3ax$$
depending on $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

---

## 2. Theoretical Background and Concepts
- **Family of Functions Parameterized by $a \in \mathbb{R}$:** A single formula $f_a(x)$ defines a continuous family of functions whose qualitative geometry (number of stationary points and extrema) can undergo a qualitative change (**bifurcation**) as the parameter $a$ crosses a critical threshold.
- **Necessary vs. Sufficient Conditions for Extrema:**
  - $f'_a(x_0) = 0$ defines a **critical (stationary) point**.
  - For $x_0$ to be a **local extremum**, $f'_a(x)$ must **change sign** across $x_0$ (which happens for simple roots of $f'_a(x) = 0$, whereas at a double root of $f'_a(x) = 0$ the sign does not change and we get a horizontal inflection point instead).

---

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the derivative $f'_a(x)$
For any real parameter $a \in \mathbb{R}$, $f_a(x) = x^3 - 3ax$ is defined and smooth on $\mathbb{R}$, with derivative:
$$f'_a(x) = 3x^2 - 3a = 3(x^2 - a)$$
Critical points are the real solutions to $f'_a(x) = 0$, which is equivalent to:
$$x^2 = a$$
Because $x^2 \ge 0$ for all real $x$, the number and nature of real solutions to $x^2 = a$ depend on the sign of $a$: $a < 0$, $a = 0$, or $a > 0$.

---

### Step 2: Case-by-Case Analysis of the Parameter $a$

#### Case 1: $a < 0$ (No critical points, no extrema)
- Since $a < 0$, we have $-a > 0$, so $x^2 - a \ge -a > 0$ for all $x \in \mathbb{R}$.
- The equation $x^2 = a$ has **no real solutions**, so there are **$0$ critical points**.
- Since $f'_a(x) = 3(x^2 - a) > 0$ for all $x \in \mathbb{R}$, $f_a$ is **strictly increasing on all of $\mathbb{R}$** with slope at the origin $f'_a(0) = -3a > 0$, and has **no local extrema**.

#### Case 2: $a = 0$ (One critical point, which is a horizontal inflection point, not an extremum)
- For $a = 0$, $f_0(x) = x^3$ and $f'_0(x) = 3x^2$.
- Setting $f'_0(x) = 0 \iff 3x^2 = 0 \iff x = 0$ (a double root). Thus there is **$1$ critical point** at $x = 0$.
- However, $f'_0(x) = 3x^2 > 0$ for both $x < 0$ and $x > 0$. Because $f'_0(x)$ **does not change sign** at $x = 0$, $f_0(x) = x^3$ is **strictly increasing on all of $\mathbb{R}$**.
- Character of $x = 0$: It is **not a local extremum**, but a **stationary (horizontal) inflection point** (since $f''_0(x) = 6x$ changes sign at $x = 0$).

#### Case 3: $a > 0$ (Two critical points: one local maximum and one local minimum)
- When $a > 0$, we can factor $f'_a(x)$ as a difference of squares:
  $$f'_a(x) = 3\left(x + \sqrt{a}\right)\left(x - \sqrt{a}\right)$$
- Setting $f'_a(x) = 0$ yields **$2$ distinct critical points**:
  $$x_1 = -\sqrt{a} \qquad \text{and} \qquad x_2 = +\sqrt{a}$$
- Sign table for $f'_a(x)$ when $a > 0$:

| Interval / Point | $\left(-\infty, -\sqrt{a}\right)$ | $x = -\sqrt{a}$ | $\left(-\sqrt{a}, \sqrt{a}\right)$ | $x = \sqrt{a}$ | $\left(\sqrt{a}, \infty\right)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f'_a(x)$** | $+$ | $0$ | $-$ | $0$ | $+$ |
| **Behavior of $f_a(x)$** | Increasing $\nearrow$ | **Local Max** | Decreasing $\searrow$ | **Local Min** | Increasing $\nearrow$ |

- Character of the critical points:
  - At $x_1 = -\sqrt{a}$, $f'_a(x)$ changes sign from $+$ to $-$, so $f_a$ has a **strict local maximum**:
    $$f_a\left(-\sqrt{a}\right) = \left(-\sqrt{a}\right)^3 - 3a\left(-\sqrt{a}\right) = 2a\sqrt{a} = 2a^{3/2}$$
  - At $x_2 = \sqrt{a}$, $f'_a(x)$ changes sign from $-$ to $+$, so $f_a$ has a **strict local minimum**:
    $$f_a\left(\sqrt{a}\right) = \left(\sqrt{a}\right)^3 - 3a\left(\sqrt{a}\right) = -2a\sqrt{a} = -2a^{3/2}$$

---

### Step 3: Why the Structure of the Graph Changes as $a$ Varies
1. **Competition between $x^3$ and $-3ax$:** For large $|x|$, the cubic term $x^3$ always dominates, making $f_a(x)$ increase for large $|x|$. Near the origin $x = 0$, the linear term $-3ax$ dominates, giving the graph at $(0,0)$ the slope $f'_a(0) = -3a$.
   - When $a < 0$, the linear term $-3ax$ has a **positive** slope ($-3a > 0$), which reinforces the upward trend of $x^3$, so the graph rises monotonically everywhere.
   - When $a > 0$, the linear term $-3ax$ has a **negative** slope ($-3a < 0$), pulling the function downward near $x = 0$ against the upward pull of $x^3$ at $\pm\infty$. This competition creates a decreasing middle region $\left[-\sqrt{a}, \sqrt{a}\right]$ bounded by a local maximum at $-\sqrt{a}$ and a local minimum at $+\sqrt{a}$.
2. **Coalescence of roots of the derivative parabola:** The graph of the derivative $y = f'_a(x) = 3x^2 - 3a$ is a parabola shifted vertically by $-3a$. For $a < 0$ it lies strictly above the $x$-axis; at $a = 0$ its vertex touches the $x$-axis at $x = 0$ (without crossing); for $a > 0$ its vertex drops below the $x$-axis, creating two simple crossings at $\pm\sqrt{a}$ where $f'_a$ changes sign.

---

## 4. Verification and Consistency Checks

### Second Derivative Test Confirmation for $a > 0$
Since $f''_a(x) = 6x$:
- $f''_a\left(-\sqrt{a}\right) = -6\sqrt{a} < 0 \implies$ strict local maximum at $x = -\sqrt{a}$.
- $f''_a\left(\sqrt{a}\right) = 6\sqrt{a} > 0 \implies$ strict local minimum at $x = \sqrt{a}$.
As $a \to 0^+$, the distance between the two extrema $2\sqrt{a} \to 0$ and their height difference $4a^{3/2} \to 0$, confirming that the local maximum and local minimum merge into the single horizontal inflection point $(0, 0)$ at $a = 0$.
