# Exercise 7: Limit at a Point and Canceling a Factor

## 1. Problem Statement
Compute
$$\lim_{x\to3}\frac{x^2-4x+3}{x-3}.$$
Explain why the value of the function at $x=3$ is not needed to compute the limit.

## 2. Theoretical Background and Concepts
- **Definition of the Limit of a Function at a Point $x_0$:**
  $$\lim_{x\to x_0} f(x) = L$$
  means that for every $\varepsilon > 0$ there exists $\delta > 0$ such that for all $x$ in the **punctured neighborhood** $0 < |x - x_0| < \delta$, we have $|f(x) - L| < \varepsilon$.
- **Locality and Independence from $f(x_0)$:** If two functions $f(x)$ and $g(x)$ satisfy $f(x) = g(x)$ for all $x \neq x_0$ in some neighborhood of $x_0$, and $\lim_{x\to x_0} g(x)$ exists, then:
  $$\lim_{x\to x_0} f(x) = \lim_{x\to x_0} g(x).$$
- **Indeterminate Form $\left[\frac{0}{0}\right]$ for Rational Functions:** If $P(x_0) = 0$ and $Q(x_0) = 0$ for polynomials $P$ and $Q$, then by Bézout's theorem $(x - x_0)$ is a common factor of both $P(x)$ and $Q(x)$ that can be canceled for all $x \neq x_0$.

## 3. Detailed Step-by-Step Solution

### Step 1: Check direct substitution (indeterminate form)
Let $f(x) = \frac{x^2 - 4x + 3}{x - 3}$. As $x \to 3$:
- Numerator: $3^2 - 4(3) + 3 = 9 - 12 + 3 = 0$.
- Denominator: $3 - 3 = 0$.
Thus we have an indeterminate form of type $\left[\frac{0}{0}\right]$, and $x = 3$ is a root of both the numerator and denominator.

### Step 2: Factor the numerator and cancel $(x - 3)$ for $x \neq 3$
Factor the quadratic polynomial $x^2 - 4x + 3$. Looking for two numbers whose sum is $-4$ and product is $3$, we find $-1$ and $-3$:
$$x^2 - 4x + 3 = (x - 1)(x - 3).$$
For every $x \neq 3$, the factor $x - 3 \neq 0$, so we can divide both numerator and denominator by $(x - 3)$:
$$\frac{x^2 - 4x + 3}{x - 3} = \frac{(x - 1)(x - 3)}{x - 3} = x - 1 \quad \text{for all } x \neq 3.$$

### Step 3: Evaluate the limit
Since the linear function $g(x) = x - 1$ is continuous everywhere, and $f(x) = g(x)$ for all $x \neq 3$:
$$\lim_{x\to 3}\frac{x^2 - 4x + 3}{x - 3} = \lim_{x\to 3}(x - 1) = 3 - 1 = 2.$$

---

### Step 4: Explain why the value of the function at $x = 3$ is not needed
1. **By definition, the limit examines $x$ approaching $3$ with $x \neq 3$:**
   In the definition of $\lim_{x\to 3} f(x)$, the condition $0 < |x - 3| < \delta$ explicitly excludes $x = 3$ via the strict inequality $0 < |x - 3|$. The limit describes how $f(x)$ behaves for arguments *arbitrarily close to* $3$, never at $x = 3$ itself.
2. **In fact, $f(3)$ does not even exist here:**
   The domain of $f(x) = \frac{x^2-4x+3}{x-3}$ is $\mathbb{R} \setminus \{3\}$ because substituting $x = 3$ causes division by zero ($\frac{0}{0}$). Geometrically, the graph of $f(x)$ is the straight line $y = x - 1$ with a single **hole (removable discontinuity)** at the point $(3, 2)$. Even though the point $(3, 2)$ is missing from the graph, as $x$ approaches $3$ from either side along the line $y = x - 1$, the $y$-values approach $2$.

## 4. Verification and Consistency Checks
Let us evaluate $f(x) = \frac{x^2-4x+3}{x-3}$ directly from the original unfactored formula for values of $x$ approaching $3$ from the left and right:
- $x = 2.9$: $f(2.9) = \frac{(2.9)^2 - 4(2.9) + 3}{2.9 - 3} = \frac{8.41 - 11.6 + 3}{-0.1} = \frac{-0.19}{-0.1} = 1.9$.
- $x = 2.999$: $f(2.999) = \frac{(2.999)^2 - 4(2.999) + 3}{2.999 - 3} = \frac{8.994001 - 11.996 + 3}{-0.001} = \frac{-0.001999}{-0.001} = 1.999$.
- $x = 3.001$: $f(3.001) = \frac{(3.001)^2 - 4(3.001) + 3}{3.001 - 3} = \frac{9.006001 - 12.004 + 3}{0.001} = \frac{0.002001}{0.001} = 2.001$.

Both one-sided approaches converge to $2$, matching $x - 1$ at $x = 3$.
