# Exercise 12: Exponential Function Limit

## 1. Problem Statement
Compute
$$\lim_{x\to0}(1+3x)^{1/x}.$$
Connect the result with the limit from Exercise 5 and show the appropriate transformation.

## 2. Theoretical Background and Concepts
- **The Fundamental Exponential Limit (Continuous Version of Exercise 5):**
  In Exercise 5, we studied the discrete limit $\lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n = e$. Extending this to a continuous real variable $u \to \pm\infty$ and substituting $t = \frac{1}{u} \to 0$ yields the equivalent fundamental limit at zero:
  $$\lim_{t\to 0} (1 + t)^{1/t} = e.$$
- **Power Rule for Continuous Limits:** Because the power/exponential function $z \mapsto z^k$ (for fixed $k \in \mathbb{R}$) is continuous at $z = e > 0$, if $\lim_{x\to 0} g(x) = e$, then:
  $$\lim_{x\to 0} \left[g(x)\right]^k = \left(\lim_{x\to 0} g(x)\right)^k = e^k.$$

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the indeterminate form
As $x \to 0$, the base $1 + 3x \to 1$ while the exponent $\frac{1}{x} \to \pm\infty$. Thus, $(1 + 3x)^{1/x}$ is an indeterminate form of type $[1^\infty]$.

### Step 2: Transform the expression to match the fundamental pattern
In the fundamental limit $\lim_{t\to 0}(1 + t)^{1/t} = e$, the reciprocal of the term added to $1$ inside the parentheses must appear in the exponent.
Here, the term added to $1$ is $3x$, so we want $\frac{1}{3x}$ in the exponent. We rewrite the exponent $\frac{1}{x}$ as $\frac{3}{3x} = 3 \cdot \frac{1}{3x}$ (valid for all $x \neq 0$):
$$(1 + 3x)^{1/x} = (1 + 3x)^{\frac{3}{3x}} = \left[(1 + 3x)^{\frac{1}{3x}}\right]^3.$$

### Step 3: Change variables and connect with Exercise 5
Let $t = 3x$ (or $u = \frac{1}{3x}$).
- As $x \to 0$ ($x \neq 0$), we have $t = 3x \to 0$ ($t \neq 0$), or equivalently $u = \frac{1}{t} \to \pm\infty$.
- In terms of $u = \frac{1}{3x}$, the inner expression becomes:
  $$(1 + 3x)^{\frac{1}{3x}} = \left(1 + \frac{1}{u}\right)^u,$$
  which has the **exact same structure as the sequence $\left(1 + \frac{1}{n}\right)^n$ from Exercise 5**, with the discrete integer $n \to \infty$ replaced by the continuous real variable $u \to \pm\infty$ (or $t = \frac{1}{u} \to 0$).

Since $\lim_{t\to 0} (1 + t)^{1/t} = e$:
$$\lim_{x\to 0} (1 + 3x)^{\frac{1}{3x}} = \lim_{t\to 0} (1 + t)^{1/t} = e.$$

### Step 4: Apply continuity of the cubing function $z \mapsto z^3$
Taking the limit of the outer third power:
$$\lim_{x\to 0} (1 + 3x)^{1/x} = \lim_{x\to 0} \left[(1 + 3x)^{\frac{1}{3x}}\right]^3 = \left(\lim_{x\to 0} (1 + 3x)^{\frac{1}{3x}}\right)^3 = e^3.$$

## 4. Verification and Consistency Checks
1. **Alternative Method via Natural Logarithm:**
   For $x > -\frac{1}{3}, \, x \neq 0$, write $(1 + 3x)^{1/x} = \exp\left(\frac{\ln(1 + 3x)}{x}\right)$. Using the standard logarithmic limit $\lim_{t\to 0}\frac{\ln(1+t)}{t} = 1$:
   $$\lim_{x\to 0}\frac{\ln(1 + 3x)}{x} = \lim_{x\to 0} 3 \cdot \frac{\ln(1 + 3x)}{3x} = 3 \cdot 1 = 3.$$
   By continuity of $\exp$, $\lim_{x\to 0}(1 + 3x)^{1/x} = \exp(3) = e^3 \approx 20.085537$.
2. **Numerical Check from Both Sides of $x = 0$:**
   - $x = -0.001$: $(1 - 0.003)^{-1000} = (0.997)^{-1000} \approx 20.1762$.
   - $x = -0.0001$: $(1 - 0.0003)^{-10000} \approx 20.0946$.
   - $x = +0.0001$: $(1 + 0.0003)^{10000} \approx 20.0765$.
   - $x = +0.001$: $(1 + 0.003)^{1000} = (1.003)^{1000} \approx 19.9955$.
   Both one-sided approaches bracket and converge to $e^3 \approx 20.0855$.
