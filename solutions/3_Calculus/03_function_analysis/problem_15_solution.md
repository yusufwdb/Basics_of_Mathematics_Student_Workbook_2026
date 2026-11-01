# Exercise 15: Find the Error in the Monotonicity Analysis

## 1. Problem Statement
For the function
$$f(x)=x^3-3x$$
the derivative was correctly computed as
$$f'(x)=3(x-1)(x+1).$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty,-1)\cup(1,\infty)$, increasing on $(-1,1)$, has a local minimum at $x=-1$, and a local maximum at $x=1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

---

## 2. Theoretical Background and Concepts
- **Sign of a Factored Quadratic Expression:** A quadratic function in factored form
  $$Q(x) = a(x - x_1)(x - x_2) \qquad (x_1 < x_2)$$
  has roots at $x_1$ and $x_2$, but its sign on the intervals $(-\infty, x_1)$, $(x_1, x_2)$, and $(x_2, \infty)$ depends critically on the **sign of the leading coefficient $a$** (or equivalently, the signs of the individual factors):
  - If **$a > 0$** (parabola opens **upward**, $\cup$): $Q(x) > 0$ **outside** the roots $(-\infty, x_1) \cup (x_2, \infty)$, and $Q(x) < 0$ **between** the roots $(x_1, x_2)$.
  - If **$a < 0$** (parabola opens **downward**, $\cap$): $Q(x) < 0$ **outside** the roots, and $Q(x) > 0$ **between** the roots.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Why identifying the zeros is not enough, and diagnosis of the student's error
1. **Why zeros alone do not determine the sign chart:**
   The zeros $x = -1$ and $x = 1$ only tell us where $f'(x)$ equals zero (the boundary points where the sign *can* change). For example, both $f'(x) = +3(x-1)(x+1)$ and $h'(x) = -3(x-1)(x+1)$ have the exact same zeros ($x = -1$ and $x = 1$), yet they have completely opposite signs on every interval! To know the sign on each interval, one must also take into account the **leading coefficient** (or check the signs of the factors $(x-1)$ and $(x+1)$ on each interval).
2. **The error in the student's reasoning:**
   In $f'(x) = 3(x - 1)(x + 1) = 3x^2 - 3$, the leading coefficient is **$a = +3 > 0$**, so the parabola $y = f'(x)$ opens **upward** ($\cup$). An upward-opening parabola is **negative between its roots** $(-1, 1)$ and **positive outside its roots** $(-\infty, -1) \cup (1, \infty)$. The student stated the exact opposite ("positive between its zeros and negative outside them"), which would only be true if the leading coefficient were negative ($a < 0$). Because every sign in the student's derivative chart was inverted, every conclusion about increasing/decreasing intervals and local maximum/minimum was also completely reversed.

---

### Part 2: Correct Sign Chart for $f'(x) = 3(x - 1)(x + 1)$
Analyzing the sign of each factor across the critical points $x = -1$ and $x = 1$:

| Interval / Point | $(-\infty, -1)$ | $x = -1$ | $(-1, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Constant factor $3$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| Factor $(x + 1)$ | $-$ | $0$ | $+$ | $+$ | $+$ |
| Factor $(x - 1)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| **Sign of $f'(x) = 3(x-1)(x+1)$** | **$+$** | **$0$** | **$-$** | **$0$** | **$+$** |
| **Behavior of $f(x)$** | Strictly increasing $\nearrow$ | **Local Max** ($2$) | Strictly decreasing $\searrow$ | **Local Min** ($-2$) | Strictly increasing $\nearrow$ |

---

### Part 3: Correct Intervals of Monotonicity and Character of the Extrema
1. **Intervals of Monotonicity:**
   - $f$ is **strictly increasing** on $(-\infty, -1]$ and on $[1, \infty)$ (separately).
   - $f$ is **strictly decreasing** on $[-1, 1]$.
   *(Note: Even when a function has the same direction of monotonicity on two disjoint intervals, it is best practice to list $(-\infty, -1]$ and $[1, \infty)$ separately rather than using the union symbol $\cup$, because $f(-2) = -2$ while $f(1.5) = -1.125$, etc.)*
2. **Character and Values of the Extrema:**
   - At **$x = -1$**, $f'(x)$ changes sign from **$+$ to $-$** (the function stops rising and starts falling), so $f$ attains a **local maximum** of:
     $$f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2$$
   - At **$x = 1$**, $f'(x)$ changes sign from **$-$ to $+$** (the function stops falling and starts rising), so $f$ attains a **local minimum** of:
     $$f(1) = (1)^3 - 3(1) = 1 - 3 = -2$$

---

### Part 4: Test Points in Each of the Three Intervals
We select one convenient test point inside each open interval and evaluate $f'(x) = 3(x - 1)(x + 1)$:
1. **Interval $(-\infty, -1)$ — choose test point $x = -2$:**
   $$f'(-2) = 3(-2 - 1)(-2 + 1) = 3(-3)(-1) = +9 > 0$$
   Since $f'(-2) > 0$, $f'(x)$ is positive on $(-\infty, -1)$, confirming $f$ is **increasing** on $(-\infty, -1]$.
2. **Interval $(-1, 1)$ — choose test point $x = 0$:**
   $$f'(0) = 3(0 - 1)(0 + 1) = 3(-1)(1) = -3 < 0$$
   Since $f'(0) < 0$, $f'(x)$ is negative on $(-1, 1)$, confirming $f$ is **decreasing** on $[-1, 1]$.
3. **Interval $(1, \infty)$ — choose test point $x = 2$:**
   $$f'(2) = 3(2 - 1)(2 + 1) = 3(1)(3) = +9 > 0$$
   Since $f'(2) > 0$, $f'(x)$ is positive on $(1, \infty)$, confirming $f$ is **increasing** on $[1, \infty)$.

---

## 4. Verification and Consistency Checks

### Direct Comparison of Function Values and Second Derivative Test
1. **Direct Comparison of $f(-1)$ and $f(1)$:**
   Notice that $f(-1) = +2$ while $f(1) = -2$. On $[-1, 1]$, as $x$ goes from $-1$ to $1$, the function value drops from $+2$ down to $-2$, which immediately proves that $f$ is **decreasing** on $[-1, 1]$ (and that $x = -1$ is the local maximum while $x = 1$ is the local minimum), directly refuting the student's claim that $f$ increases on $(-1, 1)$.
2. **Second Derivative Test:**
   $$f''(x) = 6x \implies f''(-1) = -6 < 0 \text{ (local maximum)}, \qquad f''(1) = +6 > 0 \text{ (local minimum)}$$
   This provides an independent confirmation of the character of both extrema.
