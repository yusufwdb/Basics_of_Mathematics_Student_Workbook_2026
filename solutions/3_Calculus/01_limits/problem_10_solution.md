# Exercise 10: Continuity of a Piecewise Function

## 1. Problem Statement
Find $a$ so that
$$f(x)=\begin{cases}ax+1,&x<2,\\x^2-1,&x\ge2\end{cases}$$
is continuous at $x=2$. Explicitly compare the left-hand limit, right-hand limit, and function value.

## 2. Theoretical Background and Concepts
- **Definition of Continuity at a Point:** A function $f$ defined on an open interval containing $x_0$ is **continuous at $x_0$** if and only if:
  $$\lim_{x\to x_0} f(x) = f(x_0).$$
- **Three-Part Criterion for Continuity at a Boundary Point $x_0$:** Since the two-sided limit $\lim_{x\to x_0} f(x)$ exists and equals $f(x_0)$ if and only if both one-sided limits exist and equal $f(x_0)$, continuity at $x_0 = 2$ requires the simultaneous agreement of three quantities:
  1. $f(2)$ is defined (the function value at $x = 2$),
  2. $\lim_{x\to 2^-} f(x)$ and $\lim_{x\to 2^+} f(x)$ both exist and are equal,
  3. $\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)$.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the function value $f(2)$
At $x = 2$, the condition $x \ge 2$ applies, so we use the second branch $f(x) = x^2 - 1$:
$$f(2) = 2^2 - 1 = 4 - 1 = 3.$$

### Step 2: Compute the right-hand limit $\lim_{x\to 2^+} f(x)$
For $x \to 2^+$, we have $x > 2$, where $f(x) = x^2 - 1$. Since $x^2 - 1$ is a polynomial (continuous everywhere):
$$\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+} (x^2 - 1) = 2^2 - 1 = 3.$$
*(Notice that $\lim_{x\to 2^+} f(x) = f(2) = 3$ holds automatically for every $a \in \mathbb{R}$, so $f$ is always right-continuous at $x = 2$.)*

### Step 3: Compute the left-hand limit $\lim_{x\to 2^-} f(x)$
For $x \to 2^-$, we have $x < 2$, where $f(x) = ax + 1$. Since $ax + 1$ is a linear polynomial:
$$\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-} (ax + 1) = a(2) + 1 = 2a + 1.$$

### Step 4: Equate the three quantities to find $a$
For $f$ to be continuous at $x = 2$, we must have:
$$\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2).$$
Substituting the three computed expressions gives:
$$2a + 1 = 3 = 3.$$
Solving the linear equation $2a + 1 = 3$:
$$2a = 3 - 1 = 2 \implies a = 1.$$

### Final Answer
The function $f$ is continuous at $x = 2$ if and only if **$a = 1$**.

## 4. Verification and Consistency Checks
Let us substitute $a = 1$ back into the definition of $f(x)$:
$$f(x) = \begin{cases} x + 1, & x < 2, \\ x^2 - 1, & x \ge 2. \end{cases}$$
Now let us explicitly check all three quantities at $x = 2$:
1. **Left-hand limit:** $\lim_{x\to 2^-} f(x) = \lim_{x\to 2^-}(x + 1) = 2 + 1 = 3$.
2. **Right-hand limit:** $\lim_{x\to 2^+} f(x) = \lim_{x\to 2^+}(x^2 - 1) = 2^2 - 1 = 3$.
3. **Function value:** $f(2) = 2^2 - 1 = 3$.

All three values equal $3$, and the two branches $y = x + 1$ and $y = x^2 - 1$ meet without any jump at the common point $(2, 3)$ (for example, $f(1.99) = 2.99$ and $f(2.01) = 3.0401$, both approaching $3$).
