# Exercise 15: The Difference Quotient as a Check of the Derivative

## 1. Problem Statement
Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate
$$\frac{f(x_0+h)-f(x_0)}h$$
for $h=1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

---

## 2. Theoretical Background and Concepts
- **Difference Quotient vs. Derivative:**
  For a step size $h \neq 0$, the difference quotient
  $$Q(h) = \frac{f(x_0 + h) - f(x_0)}{h}$$
  is the average rate of change of $f$ on $[x_0, x_0+h]$ (the slope of the secant line). The derivative is the limit:
  $$f'(x_0) = \lim_{h \to 0} Q(h)$$
- **Numerical Approximation vs. Mathematical Proof:**
  Evaluating $Q(h)$ at a finite collection of small values (such as $h = 1, 0.1, 0.01$) provides a **numerical sanity check** and empirical illustration of convergence, because if $\lim_{h \to 0} Q(h) = f'(x_0)$, then $Q(h)$ must be close to $f'(x_0)$ when $h$ is sufficiently small. However, a limit statement $\lim_{h \to 0} Q(h) = L$ is a universal statement about **all** $h$ in deleted neighborhoods $(-\delta, \delta) \setminus \{0\}$ as $\delta \to 0^+$, including negative $h$ and arbitrarily small scales beyond $0.01$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Choose a function and a point $x_0$, and compute $f'(x_0)$ exactly
We choose the quadratic function from **Problem 10**:
$$f(x) = x^2 - 3x + 1 \qquad \text{at the point } x_0 = 2$$
As found in Problem 10:
- $f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1$
- $f'(x) = 2x - 3$
- Therefore, the exact derivative at $x_0 = 2$ is:
  $$f'(2) = 2(2) - 3 = 1$$

### Step 2: Calculate the difference quotient for $h = 1$, $0.1$, and $0.01$
Let us first compute $f(2 + h)$ for each value of $h$ and then evaluate $Q(h) = \frac{f(2+h) - f(2)}{h}$:

1. **For $h = 1$ ($x_0 + h = 3$):**
   $$f(3) = 3^2 - 3(3) + 1 = 9 - 9 + 1 = 1$$
   $$\frac{f(2 + 1) - f(2)}{1} = \frac{1 - (-1)}{1} = \frac{2}{1} = 2$$

2. **For $h = 0.1$ ($x_0 + h = 2.1$):**
   $$f(2.1) = (2.1)^2 - 3(2.1) + 1 = 4.41 - 6.3 + 1 = -0.89$$
   $$\frac{f(2 + 0.1) - f(2)}{0.1} = \frac{-0.89 - (-1)}{0.1} = \frac{0.11}{0.1} = 1.1$$

3. **For $h = 0.01$ ($x_0 + h = 2.01$):**
   $$f(2.01) = (2.01)^2 - 3(2.01) + 1 = 4.0401 - 6.03 + 1 = -0.9899$$
   $$\frac{f(2 + 0.01) - f(2)}{0.01} = \frac{-0.9899 - (-1)}{0.01} = \frac{0.0101}{0.01} = 1.01$$

### Step 3: Compare the values with $f'(2) = 1$
Summarizing the results in a comparison table:

| Step size $h$ | $x_0 + h$ | $f(x_0 + h)$ | Difference quotient $Q(h) = \frac{f(2+h)-f(2)}{h}$ | Exact derivative $f'(2)$ | Approximation error $Q(h) - f'(2)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $3$ | $1$ | $2$ | $1$ | $1$ |
| $0.1$ | $2.1$ | $-0.89$ | $1.1$ | $1$ | $0.1$ |
| $0.01$ | $2.01$ | $-0.9899$ | $1.01$ | $1$ | $0.01$ |

As $h$ decreases from $1 \to 0.1 \to 0.01$, the difference quotient takes the values $2 \to 1.1 \to 1.01$, approaching the exact derivative $f'(2) = 1$, with the error shrinking proportionally to $h$.

### Step 4: Explain consistency with the definition vs. why a few computations do not replace a limit argument
1. **Why this is consistent with the definition of the derivative:**
   By definition, $f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h)-f(x_0)}{h}$ means that the secant slope $\frac{f(x_0+h)-f(x_0)}{h}$ gets arbitrarily close to $f'(x_0)$ as $h$ gets closer to $0$. Indeed, algebraically:
   $$\frac{f(2+h) - f(2)}{h} = \frac{(2+h)^2 - 3(2+h) + 1 - (-1)}{h} = \frac{h + h^2}{h} = 1 + h \qquad (h \neq 0)$$
   Substituting $h = 1, 0.1, 0.01$ into $1 + h$ immediately gives $2, 1.1, 1.01$, which converges to $1$ as $h \to 0$.
2. **Why a few computations do NOT replace a limit proof:**
   - **Only positive values were tested:** Testing $h = 1, 0.1, 0.01$ checks only the right-hand side ($h > 0$). For instance, in Problem 14 with $a = -5$, testing $h = 1, 0.1, 0.01$ at $x_0 = 0$ gives $1, 0.1, 0.01 \to 0$, even though the derivative at $0$ does not exist because the left-hand difference quotients equal $-5$!
   - **Behavior at smaller scales or non-sampled points:** A function could behave differently for $h < 10^{-6}$ (e.g., $g(x) = x + \sqrt{|x|}\,10^{-4}$) or oscillate wildly between sampled points (like $x\sin(\pi / \ln|x|)$). Only an analytical limit argument proves convergence for *every* path $h \to 0$.

---

## 4. Verification and Consistency Checks

### Additional Check with Negative Step Sizes ($h < 0$)
To verify that the left-hand difference quotients for $f(x) = x^2 - 3x + 1$ at $x_0 = 2$ also converge to $f'(2) = 1$:
- For $h = -1$: $Q(-1) = \frac{f(1) - f(2)}{-1} = \frac{-1 - (-1)}{-1} = 0 = 1 + (-1)$
- For $h = -0.1$: $Q(-0.1) = \frac{f(1.9) - f(2)}{-0.1} = \frac{-1.09 - (-1)}{-0.1} = 0.9 = 1 + (-0.1)$
- For $h = -0.01$: $Q(-0.01) = \frac{f(1.99) - f(2)}{-0.01} = \frac{-1.0099 - (-1)}{-0.01} = 0.99 = 1 + (-0.01)$

Both left-hand ($0, 0.9, 0.99 \nearrow 1$) and right-hand ($2, 1.1, 1.01 \searrow 1$) difference quotients sandwich the exact derivative $f'(2) = 1$, and their average $\frac{Q(h) + Q(-h)}{2} = \frac{(1+h) + (1-h)}{2} = 1$ gives the exact derivative for every $h \neq 0$.
