# Exercise 15: Observation Versus Proof

## 1. Problem Statement
Choose one sequence and one function from this set. For the sequence, compute several values for increasingly large $n$. For the function, prepare a table of values with arguments approaching the limit point from the left and right. Sketch the behavior of both objects.

Compare the observation with the analytical result and explain why a finite number of calculations or a sketch does not constitute a proof that the limit exists.

## 2. Theoretical Background and Concepts
- **Sequence Limit Definition ($\lim_{n\to\infty} a_n = L$):**
  $$\forall \varepsilon > 0 \;\; \exists N \in \mathbb{N} \;\; \forall n > N : \quad |a_n - L| < \varepsilon.$$
- **Function Limit Definition ($\lim_{x\to x_0} f(x) = L$):**
  $$\forall \varepsilon > 0 \;\; \exists \delta > 0 \;\; \forall x \in \text{Dom}(f) : \quad 0 < |x - x_0| < \delta \implies |f(x) - L| < \varepsilon.$$
- **Universal Quantification vs. Finite Sampling:** Both definitions contain a universal quantifier ($\forall n > N$ or $\forall x \in (x_0 - \delta, x_0 + \delta) \setminus \{x_0\}$) ranging over an **infinite** set of arguments. A finite table of values tests only finitely many points and cannot verify a universal statement over an infinite set.

## 3. Detailed Step-by-Step Solution

### Part 1: Chosen Sequence from the Set (Exercise 1)
We choose the rational sequence from Exercise 1:
$$a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}, \qquad \text{with analytical limit } \lim_{n\to\infty} a_n = 2.$$

#### Table of values for increasingly large $n$:
| $n$ | Numerator $4n^2 - 3n + 1$ | Denominator $2n^2 + 5n - 7$ | Exact Fraction $a_n$ | Decimal Approximation | Error $|2 - a_n|$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $1$ | $2$ | $0$ | undefined ($n=1$) | — | — |
| $2$ | $11$ | $11$ | $\frac{11}{11}$ | $1.000000$ | $1.000000$ |
| $5$ | $86$ | $68$ | $\frac{43}{34}$ | $1.264706$ | $0.735294$ |
| $10$ | $371$ | $243$ | $\frac{371}{243}$ | $1.526749$ | $0.473251$ |
| $50$ | $9\,851$ | $5\,243$ | $\frac{9851}{5243}$ | $1.878886$ | $0.121114$ |
| $100$ | $39\,701$ | $20\,493$ | $\frac{39701}{20493}$ | $1.937296$ | $0.062704$ |
| $1\,000$ | $3\,997\,001$ | $2\,004\,993$ | $\frac{3997001}{2004993}$ | $1.993524$ | $0.006476$ |
| $10\,000$ | $399\,970\,001$ | $200\,049\,993$ | $\frac{399970001}{200049993}$ | $1.999350$ | $0.000650$ |

#### Sketch of the sequence $a_n$ approaching the horizontal asymptote $L = 2$:
```text
  a_n
   ^
 2 + - - - - - - - - - - - - - - - - - - - - - - - -  Limit L = 2
   |                                     *     *
   |                               *
1.5+                         *
   |                   *
 1 +       *
   |
 0 +-------+-----------+-----+-----+-----+-----+----> n
           2           5    10    50   100  1000
```

---

### Part 2: Chosen Function from the Set (Exercise 8)
We choose the function from Exercise 8:
$$f(x) = \frac{\sqrt{x} - 2}{x - 4} \quad (x \ge 0, \, x \neq 4), \qquad \text{with analytical limit } \lim_{x\to 4} f(x) = \frac{1}{4} = 0.25.$$

#### Table of values approaching $x_0 = 4$ from the left ($x \to 4^-$) and right ($x \to 4^+$):
| Left approach $x \to 4^-$ | $f(x) = \frac{\sqrt{x}-2}{x-4}$ | Right approach $x \to 4^+$ | $f(x) = \frac{\sqrt{x}-2}{x-4}$ |
| :--- | :--- | :--- | :--- |
| $x = 3.0$ | $0.26794919$ | $x = 5.0$ | $0.23606798$ |
| $x = 3.5$ | $0.25834261$ | $x = 4.5$ | $0.24264069$ |
| $x = 3.9$ | $0.25158234$ | $x = 4.1$ | $0.24845673$ |
| $x = 3.99$ | $0.25015644$ | $x = 4.01$ | $0.24984395$ |
| $x = 3.999$ | $0.25001563$ | $x = 4.001$ | $0.24998438$ |
| $x = 3.9999$ | $0.25000156$ | $x = 4.0001$ | $0.24999844$ |

#### Sketch of $f(x) = \frac{\sqrt{x}-2}{x-4}$ near $x = 4$:
```text
  f(x)
    ^
0.50+ * (0, 0.5)
    |   \
    |     ' .
0.25+ - - - - ' - . o . - - - - - - - -   Limit L = 0.25 at hole (4, 0.25)
    |               |   ' - . _
    |               |           ' - . _
  0 +---------------+-------------------> x
    0               4
```

---

### Part 3: Comparison and Explanation of Why Observation Is Not Proof

#### Comparison of observation with analytical results:
In both tables and sketches, the numerical observations strongly agree with the analytical limits:
- For $a_n$, as $n$ increases by a factor of $10$, the distance $|2 - a_n| \approx \frac{6.5}{n}$ shrinks by a factor of $10$, approaching $2$ from below.
- For $f(x)$, as $x \to 4^-$, $f(x)$ decreases toward $0.25$, and as $x \to 4^+$, $f(x)$ increases toward $0.25$, pinching the missing point $(4, 0.25)$ from both sides.

#### Why a finite number of calculations or a sketch does NOT constitute a proof:
1. **Unobserved behavior beyond the table (for sequences):**
   Any table checks only finitely many indices $n_1, n_2, \dots, n_k$. Infinitely many indices remain unchecked. For example, the sequence
   $$b_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} + \left(\frac{n}{10^6}\right)^{50}$$
   agrees with $a_n$ to over $100$ decimal places for $n = 1, 2, \dots, 10\,000$ in our table, yet $\lim_{n\to\infty} b_n = +\infty$.
2. **Hidden behavior closer to the limit point or between sampled points (for functions):**
   Sampling $x = 4 \pm 10^{-k}$ checks only a countable discrete set of points. A function like
   $$g(x) = \frac{\sqrt{x}-2}{x-4} + \sin\left(\frac{\pi}{x - 4}\right)$$
   takes the **exact same values** as $f(x)$ at every single point $x = 4 \pm 10^{-k}$ in our table (because $\sin(\pm 10^k \pi) = 0$), yet $\lim_{x\to 4} g(x)$ does not exist at all due to rapid oscillation between $-0.75$ and $+1.25$ infinitely often near $x = 4$.
3. **Finite precision and visual resolution limits:**
   Sketches have finite line thickness and numerical calculators have rounding error (e.g., catastrophic cancellation when subtracting two nearly equal numbers like $\sqrt{x} - 2$ for $x = 4 + 10^{-16}$). Only an algebraic/analytical deduction (such as factoring out $n^2$ or rationalizing the numerator) proves that the limit holds for **all** $n > N$ or **all** $x$ in $0 < |x - 4| < \delta$.

## 4. Verification and Consistency Checks
Let us verify the error formulas that explain the exact numbers in our two tables:
1. **For $a_n$:**
   $$2 - a_n = 2 - \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{13n - 15}{2n^2 + 5n - 7} \approx \frac{13}{2n} = \frac{6.5}{n}.$$
   At $n = 10\,000$, $\frac{6.5}{10\,000} = 0.000650$, matching our table's error column ($0.000650$) to six decimal places.
2. **For $f(x)$:**
   $$f(x) - \frac{1}{4} = \frac{1}{\sqrt{x} + 2} - \frac{1}{4} = \frac{2 - \sqrt{x}}{4(\sqrt{x} + 2)} = \frac{4 - x}{4(\sqrt{x} + 2)^2} \approx -\frac{x - 4}{64}.$$
   At $x = 4.0001$ ($x - 4 = 10^{-4}$), $f(x) - 0.25 \approx -\frac{10^{-4}}{64} \approx -0.0000015625$, so $f(4.0001) \approx 0.24999844$, matching our table entry exactly.
