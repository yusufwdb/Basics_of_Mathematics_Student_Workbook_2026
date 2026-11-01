# Exercise 13: Fundamental Trigonometric Limit

## 1. Problem Statement
Using
$$\lim_{x\to0}\frac{\sin x}{x}=1,$$
compute
$$\lim_{x\to0}\frac{\sin5x}{x},\qquad \lim_{x\to0}\frac{\sin2x}{\sin3x}.$$
In each case, show how you reduce the expression to the fundamental limit.

## 2. Theoretical Background and Concepts
- **Fundamental Trigonometric Limit:**
  $$\lim_{u\to 0}\frac{\sin u}{u} = 1 \quad \text{and equivalently} \quad \lim_{u\to 0}\frac{u}{\sin u} = 1.$$
- **Substitution / Scaling Principle:** For any non-zero constant $k \neq 0$, as $x \to 0$ ($x \neq 0$), the linear multiple $u = kx$ also satisfies $u \to 0$ ($u \neq 0$). Therefore:
  $$\lim_{x\to 0}\frac{\sin(kx)}{kx} = \lim_{u\to 0}\frac{\sin u}{u} = 1.$$
  Notice that the argument inside $\sin(kx)$ and the denominator $kx$ **must be identical** for the ratio to approach $1$.

## 3. Detailed Step-by-Step Solution

### Part 1: Compute $\lim_{x\to 0}\frac{\sin 5x}{x}$

#### Step 1.1: Match the denominator to the argument of sine
The argument of the sine function is $5x$, whereas the denominator is $x$. For $x \neq 0$, multiply both numerator and denominator by $5$:
$$\frac{\sin 5x}{x} = 5 \cdot \frac{\sin 5x}{5x}.$$

#### Step 1.2: Apply the fundamental limit via substitution
Let $u = 5x$. As $x \to 0$ ($x \neq 0$), we have $u \to 0$ ($u \neq 0$), so:
$$\lim_{x\to 0}\frac{\sin 5x}{5x} = \lim_{u\to 0}\frac{\sin u}{u} = 1.$$
By the constant multiple rule for limits:
$$\lim_{x\to 0}\frac{\sin 5x}{x} = 5 \cdot \lim_{x\to 0}\frac{\sin 5x}{5x} = 5 \cdot 1 = 5.$$

---

### Part 2: Compute $\lim_{x\to 0}\frac{\sin 2x}{\sin 3x}$

#### Step 2.1: Introduce the matching linear arguments $2x$ and $3x$
Both numerator and denominator approach $0$ as $x \to 0$, giving a $\left[\frac{0}{0}\right]$ indeterminate form. To reduce both $\sin 2x$ and $\sin 3x$ to the fundamental pattern $\frac{\sin u}{u}$, we multiply and divide by $2x$ and $3x$ (for $x$ in a punctured neighborhood of $0$ where $\sin 3x \neq 0$):
$$\frac{\sin 2x}{\sin 3x} = \frac{\frac{\sin 2x}{2x} \cdot 2x}{\frac{\sin 3x}{3x} \cdot 3x} = \frac{2}{3} \cdot \frac{\dfrac{\sin 2x}{2x}}{\dfrac{\sin 3x}{3x}}.$$

#### Step 2.2: Evaluate the limit of each block
- With $u = 2x \to 0$ as $x \to 0$:
  $$\lim_{x\to 0}\frac{\sin 2x}{2x} = \lim_{u\to 0}\frac{\sin u}{u} = 1.$$
- With $v = 3x \to 0$ as $x \to 0$:
  $$\lim_{x\to 0}\frac{\sin 3x}{3x} = \lim_{v\to 0}\frac{\sin v}{v} = 1 \neq 0.$$

By the quotient and constant-multiple laws for limits:
$$\lim_{x\to 0}\frac{\sin 2x}{\sin 3x} = \frac{2}{3} \cdot \frac{\lim_{x\to 0}\frac{\sin 2x}{2x}}{\lim_{x\to 0}\frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}.$$

## 4. Verification and Consistency Checks
1. **Small-Angle Approximation ($\sin u \approx u$ for small $u$):**
   For $x$ very close to $0$ (in radians), $\sin(kx) \approx kx$:
   - $\frac{\sin 5x}{x} \approx \frac{5x}{x} = 5$.
   - $\frac{\sin 2x}{\sin 3x} \approx \frac{2x}{3x} = \frac{2}{3}$.
2. **Numerical Check (with $x = 0.001$ radians):**
   - $\frac{\sin(0.005)}{0.001} \approx \frac{0.004999979}{0.001} = 4.999979 \to 5$.
   - $\frac{\sin(0.002)}{\sin(0.003)} \approx \frac{0.0019999987}{0.0029999955} \approx 0.6666671 \to \frac{2}{3} \approx 0.6666667$.
Both numerical checks agree with our exact analytical results.
