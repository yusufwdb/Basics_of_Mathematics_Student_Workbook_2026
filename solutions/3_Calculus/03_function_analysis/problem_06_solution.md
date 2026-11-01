# Exercise 6: A Logarithmic Function

## 1. Problem Statement
Analyze the domain, zero, and monotonicity of
$$f(x)=\ln x-x+1.$$
Explain why the analysis must begin with the domain.

---

## 2. Theoretical Background and Concepts
- **Domain of the Natural Logarithm:** Over the real numbers, $\ln x$ is defined if and only if $x > 0$.
- **Why Function Analysis Must Begin with the Domain:**
  1. Algebraic transformations of the derivative can hide domain restrictions that were present in the original formula $f(x)$. For example, here $f'(x) = \frac{1 - x}{x}$ looks algebraically valid for any $x \neq 0$ (including negative $x$), even though $f(x)$ does not exist for $x \le 0$!
  2. Knowing the domain upfront prevents us from falsely constructing sign intervals for $x < 0$ or claiming behavior at points where $f$ is undefined.
- **Uniqueness of Zeros via Monotonicity:** If $f$ is strictly increasing on $(0, x_0]$, attains a maximum $f(x_0) = 0$ at $x_0$, and is strictly decreasing on $[x_0, \infty)$, then $f(x) < 0$ for all $x \neq x_0$ and $x_0$ is the **unique zero** of $f$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Determine the domain (and why it comes first)
In the formula $f(x) = \ln x - x + 1$, the term $-x + 1$ is defined for all $x \in \mathbb{R}$, whereas $\ln x$ is defined only for strictly positive real numbers:
$$x > 0 \implies D_f = (0, \infty)$$
**Why we must start here:** Every subsequent step—solving $f'(x) = 0$, building the sign table of $f'(x)$, and finding zeros—is restricted strictly to $x \in (0, \infty)$. Without fixing $D_f = (0, \infty)$ first, looking at $f'(x) = \frac{1-x}{x}$ could mislead one into analyzing the interval $(-\infty, 0)$, where $f(x)$ does not exist at all.

### Step 2: Compute the derivative and analyze monotonicity
Differentiating $f(x) = \ln x - x + 1$ for $x \in (0, \infty)$:
$$f'(x) = \frac{1}{x} - 1 + 0 = \frac{1 - x}{x}$$

Setting $f'(x) = 0$ on $(0, \infty)$:
$$\frac{1 - x}{x} = 0 \iff 1 - x = 0 \iff x = 1 \in (0, \infty)$$

Since $x > 0$ throughout the entire domain $D_f = (0, \infty)$, the denominator of $f'(x) = \frac{1-x}{x}$ is always positive, so the sign of $f'(x)$ is determined solely by the numerator $1 - x$:
- On $(0, 1)$: $1 - x > 0$ and $x > 0 \implies f'(x) > 0$, so $f$ is **strictly increasing** on $(0, 1]$.
- At $x = 1$: $f'(1) = 0$.
- On $(1, \infty)$: $1 - x < 0$ and $x > 0 \implies f'(x) < 0$, so $f$ is **strictly decreasing** on $[1, \infty)$.

| Interval / Point | $(0, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: |
| Sign of $(1 - x)$ | $+$ | $0$ | $-$ |
| Sign of $x$ | $+$ | $+$ | $+$ |
| **Sign of $f'(x)$** | **$+$** | **$0$** | **$-$** |
| **Behavior of $f(x)$** | Strictly increasing $\nearrow$ | **Global Maximum** ($0$) | Strictly decreasing $\searrow$ |

### Step 3: Find the zero(s) of $f(x)$ using monotonicity and the maximum
Evaluating $f$ at the critical point $x = 1$:
$$f(1) = \ln 1 - 1 + 1 = 0 - 1 + 1 = 0$$
Because $f$ is strictly increasing on $(0, 1]$ up to $f(1) = 0$ and strictly decreasing on $[1, \infty)$ down from $f(1) = 0$, we have:
- For all $x \in (0, 1)$, $f(x) < f(1) = 0$.
- For all $x \in (1, \infty)$, $f(x) < f(1) = 0$.

Therefore, $f(x) \le 0$ for all $x > 0$, with equality $f(x) = 0$ **if and only if $x = 1$**. Thus **$x = 1$ is the unique zero of $f(x)$**, and $(1, 0)$ is simultaneously the global maximum and the sole point where the graph touches the $x$-axis!

---

## 4. Verification and Consistency Checks

### Fundamental Logarithm Inequality and End-Behavior Limits
1. **Fundamental Inequality $\ln x \le x - 1$:** Our analysis proves the classic calculus inequality:
   $$\ln x - x + 1 \le 0 \iff \ln x \le x - 1 \qquad \text{for all } x > 0$$
   with equality if and only if $x = 1$. Geometrically, $y = x - 1$ is the tangent line to the concave curve $y = \ln x$ at $(1, 0)$, so $\ln x$ lies strictly below $x - 1$ for all $x \neq 1$.
2. **Boundary Limits:**
   - As $x \to 0^+$: $\lim_{x \to 0^+} (\ln x - x + 1) = -\infty - 0 + 1 = -\infty$ (vertical asymptote $x = 0$).
   - As $x \to \infty$: $\lim_{x \to \infty} x\left(\frac{\ln x}{x} - 1 + \frac{1}{x}\right) = \infty(0 - 1 + 0) = -\infty$.
   Both boundary limits are $-\infty$, consistent with $f$ rising from $-\infty$ to $0$ at $x = 1$ and then falling back to $-\infty$.
