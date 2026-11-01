# Exercise 5: An Exponential Function with a Maximum

## 1. Problem Statement
Analyze the monotonicity and extrema of
$$f(x)=xe^{-x}.$$
Also examine the behavior as $x\to\infty$ and explain how the limit affects the shape of the graph on the right-hand side.

---

## 2. Theoretical Background and Concepts
- **Product and Chain Rules for Exponential Functions:**
  $$\frac{d}{dx}\left(e^{-x}\right) = -e^{-x}, \qquad (uv)' = u'v + uv'$$
- **Strict Positivity of Exponential Functions:** For every real number $x \in \mathbb{R}$, $e^{-x} > 0$. Therefore, a product $g(x)e^{-x}$ has the exact same zeros and sign as the polynomial factor $g(x)$.
- **Relative Growth Rate of Polynomials vs. Exponentials (L'Hôpital's Rule / Standard Limit):**
  For any $\alpha > 0$, exponential growth $e^x$ dominates power growth $x^\alpha$ as $x \to +\infty$:
  $$\lim_{x \to \infty} \frac{x^\alpha}{e^x} = 0$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Domain and Derivative
The function $f(x) = xe^{-x}$ is defined and smooth on the entire real line: $D_f = \mathbb{R}$.
Applying the product rule with $u(x) = x$ ($u'(x) = 1$) and $v(x) = e^{-x}$ ($v'(x) = -e^{-x}$):
$$f'(x) = (1)e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}$$

### Step 2: Critical Point and Sign Table of $f'(x)$
Since $e^{-x} > 0$ for all $x \in \mathbb{R}$, the equation $f'(x) = 0$ reduces to:
$$1 - x = 0 \iff x = 1$$
The sign of $f'(x) = (1 - x)e^{-x}$ matches the sign of $1 - x$:
- For $x < 1$: $1 - x > 0 \implies f'(x) > 0$.
- For $x = 1$: $1 - x = 0 \implies f'(1) = 0$.
- For $x > 1$: $1 - x < 0 \implies f'(x) < 0$.

| Interval / Point | $(-\infty, 1)$ | $x = 1$ | $(1, \infty)$ |
| :--- | :---: | :---: | :---: |
| Sign of $(1 - x)$ | $+$ | $0$ | $-$ |
| Sign of $e^{-x}$ | $+$ | $+$ | $+$ |
| **Sign of $f'(x)$** | **$+$** | **$0$** | **$-$** |
| **Behavior of $f(x)$** | Strictly increasing $\nearrow$ | **Global Maximum** $\left(\frac{1}{e}\right)$ | Strictly decreasing $\searrow$ |

### Step 3: Monotonicity and Extrema
1. **Intervals of Monotonicity:**
   - $f$ is **strictly increasing** on $(-\infty, 1]$.
   - $f$ is **strictly decreasing** on $[1, \infty)$.
2. **Extrema:**
   - At $x = 1$, $f'(x)$ changes sign from $+$ to $-$. Since $f$ increases on the entire interval $(-\infty, 1]$ and decreases on the entire interval $[1, \infty)$, $f$ attains both a **local and global maximum** at $x = 1$:
     $$f_{\max} = f(1) = 1 \cdot e^{-1} = \frac{1}{e} \approx 0.368$$
   - There is no local minimum.

### Step 4: Behavior as $x \to \infty$ (and $x \to -\infty$) and Its Effect on the Graph
Rewriting $f(x)$ as a quotient for $x > 0$:
$$\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{x}{e^x}$$
This is an indeterminate form of type $\left[\frac{\infty}{\infty}\right]$. Because exponential growth $e^x$ grows much faster than linear growth $x$ (or by L'Hôpital's rule, $\lim_{x \to \infty} \frac{x}{e^x} = \lim_{x \to \infty} \frac{1}{e^x} = 0$), we obtain:
$$\lim_{x \to \infty} xe^{-x} = 0^+$$
(Meanwhile, as $x \to -\infty$, $x \to -\infty$ and $e^{-x} \to +\infty$, so $\lim_{x \to -\infty} xe^{-x} = -\infty$.)

**How the limit as $x \to \infty$ affects the shape of the graph on the right-hand side:**
1. After reaching its peak at $\left(1, \frac{1}{e}\right)$, the function is strictly decreasing ($f'(x) < 0$ for $x > 1$), yet for all $x > 0$ we have $f(x) = xe^{-x} > 0$.
2. Because $f(x)$ decreases while remaining strictly positive and $\lim_{x \to \infty} f(x) = 0$, the graph **cannot fall to $-\infty$ or cross the $x$-axis** for $x > 1$. Instead, the curve must bend from concave down (near the peak at $x = 1$) to **concave up** (via an inflection point at $x = 2$) and flatten out, approaching the positive $x$-axis ($y = 0$) from above as a **right-hand horizontal asymptote**.

---

## 4. Verification and Consistency Checks

### Second Derivative and Inflection Point Check
Computing $f''(x)$ using the product rule on $f'(x) = (1 - x)e^{-x}$:
$$f''(x) = (-1)e^{-x} + (1 - x)(-e^{-x}) = (x - 2)e^{-x}$$
- **At $x = 1$:** $f''(1) = (1 - 2)e^{-1} = -\frac{1}{e} < 0$, which confirms via the second derivative test that $x = 1$ is a strict local maximum.
- **Inflection point at $x = 2$:** $f''(x) = 0 \iff x = 2$, where $f''(x)$ changes sign from $-$ (concave down on $(-\infty, 2)$) to $+$ (concave up on $(2, \infty)$). This confirms our qualitative conclusion in Step 4 that the curve must switch from concave down to concave up at $x = 2$ (where $f(2) = \frac{2}{e^2} \approx 0.271$) in order to approach the horizontal asymptote $y = 0$ smoothly from above.
