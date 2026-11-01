# Exercise 9: One-Sided Limits and an Asymptote

## 1. Problem Statement
Analyze the left-hand and right-hand limits of
$$f(x)=\frac1{x-2}$$
as $x\to2$. Does the two-sided limit exist? Interpret the result on a sketch of the graph and identify the vertical asymptote.

## 2. Theoretical Background and Concepts
- **One-Sided Limits:**
  - The **left-hand limit** $\lim_{x\to x_0^-} f(x)$ describes the behavior of $f(x)$ as $x$ approaches $x_0$ through values strictly less than $x_0$ ($x < x_0$).
  - The **right-hand limit** $\lim_{x\to x_0^+} f(x)$ describes the behavior of $f(x)$ as $x$ approaches $x_0$ through values strictly greater than $x_0$ ($x > x_0$).
- **Existence of the Two-Sided Limit:** The two-sided limit $\lim_{x\to x_0} f(x)$ exists (in the finite or infinite sense) if and only if both one-sided limits exist and are **equal**:
  $$\lim_{x\to x_0} f(x) = L \iff \lim_{x\to x_0^-} f(x) = \lim_{x\to x_0^+} f(x) = L.$$
- **Vertical Asymptote:** The vertical line $x = x_0$ is a vertical asymptote of the graph of $y = f(x)$ if at least one of the one-sided limits $\lim_{x\to x_0^-} f(x)$ or $\lim_{x\to x_0^+} f(x)$ equals $+\infty$ or $-\infty$.

## 3. Detailed Step-by-Step Solution

### Step 1: Left-hand limit as $x \to 2^-$
When $x \to 2^-$ (i.e., $x < 2$ and $x$ is arbitrarily close to $2$):
- The numerator is the positive constant $1$.
- The denominator $x - 2$ approaches $0$ through **negative** values ($x - 2 \to 0^-$).
Dividing $1$ by a negative number that is arbitrarily close to $0$ yields a negative number of arbitrarily large magnitude:
$$\lim_{x\to 2^-} \frac{1}{x - 2} = \left[\frac{1}{0^-}\right] = -\infty.$$

### Step 2: Right-hand limit as $x \to 2^+$
When $x \to 2^+$ (i.e., $x > 2$ and $x$ is arbitrarily close to $2$):
- The numerator is the positive constant $1$.
- The denominator $x - 2$ approaches $0$ through **positive** values ($x - 2 \to 0^+$).
Dividing $1$ by a positive number that is arbitrarily close to $0$ yields a positive number of arbitrarily large magnitude:
$$\lim_{x\to 2^+} \frac{1}{x - 2} = \left[\frac{1}{0^+}\right] = +\infty.$$

### Step 3: Does the two-sided limit exist?
**No, the two-sided limit $\lim_{x\to 2}\frac{1}{x-2}$ does not exist** (not even as an improper infinite limit), because the left-hand limit and the right-hand limit are different:
$$\lim_{x\to 2^-} \frac{1}{x - 2} = -\infty \neq +\infty = \lim_{x\to 2^+} \frac{1}{x - 2}.$$

### Step 4: Identify the vertical asymptote and sketch the graph
- **Vertical asymptote:** Because $\lim_{x\to 2^-} f(x) = -\infty$ and $\lim_{x\to 2^+} f(x) = +\infty$, the vertical line
  $$x = 2$$
  is a **vertical asymptote** of the graph of $f(x) = \frac{1}{x-2}$.
- **Geometric interpretation on the graph:**
  The graph of $f(x) = \frac{1}{x-2}$ is the rectangular hyperbola $y = \frac{1}{x}$ shifted $2$ units to the right:
  - As $x$ approaches the line $x = 2$ from the left ($x \to 2^-$), the left branch plunges downward without bound along the vertical line $x = 2$ toward $-\infty$.
  - As $x$ approaches the line $x = 2$ from the right ($x \to 2^+$), the right branch shoots upward without bound along the vertical line $x = 2$ toward $+\infty$.
  *(Additionally, $y = 0$ is a horizontal asymptote since $\lim_{x\to\pm\infty}\frac{1}{x-2} = 0$.)*

```text
          y
          ^       |  /
          |       |  |   x -> 2+ : f(x) -> +infinity
          |       |  |
          |       |   \
          |       |     ' - - . _
----------+-------+-----------------> x
    _ . - | - '   | 2
(0,-1/2)  |     / |
          |    |  |
          |    |  |      x -> 2- : f(x) -> -infinity
          |   /   |
                  x = 2 (Vertical Asymptote)
```

## 4. Verification and Consistency Checks
Let us evaluate $f(x) = \frac{1}{x-2}$ at points approaching $x = 2$ from the left and from the right:

| Approach from the left ($x \to 2^-$) | $f(x) = \frac{1}{x-2}$ | Approach from the right ($x \to 2^+$) | $f(x) = \frac{1}{x-2}$ |
| :--- | :--- | :--- | :--- |
| $x = 1.9$ | $\frac{1}{-0.1} = -10$ | $x = 2.1$ | $\frac{1}{0.1} = +10$ |
| $x = 1.99$ | $\frac{1}{-0.01} = -100$ | $x = 2.01$ | $\frac{1}{0.01} = +100$ |
| $x = 1.999$ | $\frac{1}{-0.001} = -1000$ | $x = 2.001$ | $\frac{1}{0.001} = +1000$ |

The table clearly confirms $\lim_{x\to 2^-} f(x) = -\infty$ and $\lim_{x\to 2^+} f(x) = +\infty$.
