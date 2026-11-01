# Exercise 6: From a Sequence to a Function — Limit at Infinity

## 1. Problem Statement
Compute
$$\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2}.$$
Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

## 2. Theoretical Background and Concepts
- **Limit of a Function at $+\infty$ (Cauchy Definition):** $\lim_{x\to\infty} f(x) = L$ means that for every $\varepsilon > 0$ there exists a real threshold $M > 0$ such that for all real $x > M$, $|f(x) - L| < \varepsilon$.
- **Heine's (Sequential) Definition of a Function Limit:** $\lim_{x\to\infty} f(x) = L$ if and only if for **every** sequence of real numbers $(x_n)$ satisfying $\lim_{n\to\infty} x_n = +\infty$, the sequence of values $(f(x_n))$ converges to $L$.
- **Rational Functions at Infinity:** Just as for rational sequences, dividing numerator and denominator by the highest power $x^k$ uses $\lim_{x\to\infty} \frac{c}{x^m} = 0$ ($m > 0$) to isolate the leading coefficients.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the limit by factoring out the highest power $x^2$
As $x \to \infty$, both $3x^2 - x + 1 \to \infty$ and $5x^2 + 4x - 2 \to \infty$, giving an indeterminate form $\left[\frac{\infty}{\infty}\right]$.
For $x > 0$ (sufficiently large so that the denominator is also non-zero), factor $x^2$ out of both numerator and denominator and cancel $x^2$:
$$\frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{x^2\left(3 - \frac{1}{x} + \frac{1}{x^2}\right)}{x^2\left(5 + \frac{4}{x} - \frac{2}{x^2}\right)} = \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}}.$$
Since $\lim_{x\to\infty} \frac{1}{x} = 0$ and $\lim_{x\to\infty} \frac{1}{x^2} = 0$, the limit laws for functions give:
$$\lim_{x\to\infty}\frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{\lim_{x\to\infty}\left(3 - \frac{1}{x} + \frac{1}{x^2}\right)}{\lim_{x\to\infty}\left(5 + \frac{4}{x} - \frac{2}{x^2}\right)} = \frac{3 - 0 + 0}{5 + 0 - 0} = \frac{3}{5}.$$

---

### Step 2: Comparison with Exercise 1 — What Stays the Same vs. What Changes

#### What stays the same:
1. **The algebraic mechanism:** In both Exercise 1 (for $n \to \infty$) and here (for $x \to \infty$), we resolve the $\left[\frac{\infty}{\infty}\right]$ indeterminate form by factoring out the highest degree power ($n^2$ or $x^2$) and canceling it.
2. **Dominance of highest-degree terms:** Because $\frac{1}{x} \to 0$ and $\frac{1}{x^2} \to 0$ just like $\frac{1}{n} \to 0$ and $\frac{1}{n^2} \to 0$, lower-degree terms become negligible for large arguments, and the limit equals the ratio of the leading coefficients ($\frac{3}{5}$).
3. **Limit arithmetic:** The sum, difference, product, and quotient laws for limits operate identically once the elementary limits are known.

#### What changes when moving from $n \in \mathbb{N}$ to a real variable $x \in \mathbb{R}$:
1. **Continuous vs. discrete domain:** In a sequence, $n$ takes only discrete positive integer values ($n = 1, 2, 3, \dots$). In a function limit as $x \to \infty$, $x$ varies continuously over all real numbers in an interval $(M, \infty)$ (including irrational and non-integer values).
2. **Domain exclusions (zeros of the denominator):** A rational function $f(x) = \frac{3x^2-x+1}{5x^2+4x-2}$ is undefined where $5x^2 + 4x - 2 = 0$ (namely at $x = \frac{-2 \pm \sqrt{14}}{5}$). Because we take $x \to +\infty$, we restrict attention to $x > 1$, which safely avoids these roots.
3. **Direction of infinity and oscillatory traps:** For a real variable $x$, one can study both $x \to +\infty$ and $x \to -\infty$ (giving a horizontal asymptote $y = \frac{3}{5}$ in both directions). Moreover, for general functions, $\lim_{n\to\infty} f(n)$ existing for integers $n$ does **not** always imply $\lim_{x\to\infty} f(x)$ exists (e.g., $\sin(\pi n) = 0$ for all $n \in \mathbb{N}$, whereas $\lim_{x\to\infty}\sin(\pi x)$ does not exist because $x$ passes through non-integers). For rational functions, however, no such oscillation occurs.

## 4. Verification and Consistency Checks
1. **Horizontal Asymptote Distance Check:**
   Compute $f(x) - \frac{3}{5}$:
   $$\frac{3x^2 - x + 1}{5x^2 + 4x - 2} - \frac{3}{5} = \frac{5(3x^2 - x + 1) - 3(5x^2 + 4x - 2)}{5(5x^2 + 4x - 2)} = \frac{-17x + 11}{25x^2 + 20x - 10}.$$
   As $x \to \infty$, $\left|f(x) - \frac{3}{5}\right| \sim \frac{17}{25x} \to 0$.
2. **Numerical Evaluation:**
   - At $x = 100$: $f(100) = \frac{30000 - 100 + 1}{50000 + 400 - 2} = \frac{29901}{50398} \approx 0.593297$ (close to $\frac{3}{5} = 0.6$).
   - At $x = 10000$: $f(10000) = \frac{299990001}{500039998} \approx 0.599932 \to 0.6 = \frac{3}{5}$.
