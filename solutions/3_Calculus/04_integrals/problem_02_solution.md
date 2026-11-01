# Exercise 2: Powers, Roots, and the Domain

## 1. Problem Statement

Compute
$$\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx.$$
First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

---

## 2. Theoretical Background and Concepts

- **Algebraic Laws of Exponents:** Radicals and reciprocals can be converted into standard power form $x^n$:
  $$\sqrt[m]{x^k} = x^{k/m}, \qquad \frac{1}{x^k} = x^{-k} \quad (x \neq 0).$$
- **Power Rule for Integration:** For any real number $n \neq -1$,
  $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$
- **Domain Considerations:** The domain of an integrand $f(x)$ is the intersection of the domains of its constituent terms. When finding an antiderivative $F(x)$, the relation $F'(x) = f(x)$ holds on the open intervals contained within the domain of $f(x)$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Determining the Domain of the Integrand
Let $f(x) = 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}$. We examine each term:
1. The square root $\sqrt{x}$ is defined in $\mathbb{R}$ only for $x \ge 0$.
2. The fraction $\frac{3}{x^2}$ requires a non-zero denominator, so $x \neq 0$.
3. The cube root $x^{1/3} = \sqrt[3]{x}$ is defined for all $x \in \mathbb{R}$ (though when written as a fractional power $x^{1/3}$, standard real power conventions often restrict the base to $x \ge 0$).

Intersecting these conditions ($x \ge 0$ and $x \neq 0$), the domain of the integrand is the open half-line:
$$D_f = (0, \infty).$$
Because $(0, \infty)$ is a single connected open interval, a single constant of integration $C$ describes the entire family of antiderivatives on $D_f$.

### Step 2: Rewriting Terms as Powers of $x$
For $x \in (0, \infty)$, we rewrite each term in the form $a x^n$:
- $2\sqrt{x} = 2x^{1/2}$
- $\frac{3}{x^2} = 3x^{-2}$
- $-x^{1/3} = -x^{1/3}$

Thus the integral becomes:
$$I = \int \left(2x^{1/2} + 3x^{-2} - x^{1/3}\right)\,dx.$$

### Step 3: Term-by-Term Integration Using the Power Rule
Applying $\int x^n\,dx = \frac{x^{n+1}}{n+1}$ to each term:
1. First term ($n = \frac{1}{2}$):
   $$\int 2x^{1/2}\,dx = 2 \cdot \frac{x^{\frac{1}{2}+1}}{\frac{1}{2}+1} = 2 \cdot \frac{x^{3/2}}{\frac{3}{2}} = \frac{4}{3}x^{3/2} = \frac{4}{3}x\sqrt{x}.$$
2. Second term ($n = -2$):
   $$\int 3x^{-2}\,dx = 3 \cdot \frac{x^{-2+1}}{-2+1} = 3 \cdot \frac{x^{-1}}{-1} = -3x^{-1} = -\frac{3}{x}.$$
3. Third term ($n = \frac{1}{3}$):
   $$\int \left(-x^{1/3}\right)\,dx = -\frac{x^{\frac{1}{3}+1}}{\frac{1}{3}+1} = -\frac{x^{4/3}}{\frac{4}{3}} = -\frac{3}{4}x^{4/3} = -\frac{3}{4}x\sqrt[3]{x}.$$

### Step 4: Final Result
Combining all terms with the constant of integration $C \in \mathbb{R}$ for $x > 0$:
$$\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx = \frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C, \quad x \in (0, \infty).$$

---

## 4. Verification and Consistency Checks

We differentiate $F(x) = \frac{4}{3}x^{3/2} - 3x^{-1} - \frac{3}{4}x^{4/3} + C$ on $(0, \infty)$:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left(\frac{4}{3}x^{3/2} - 3x^{-1} - \frac{3}{4}x^{4/3} + C\right) \\
&= \frac{4}{3}\cdot\frac{3}{2}x^{\frac{3}{2}-1} - 3(-1)x^{-1-1} - \frac{3}{4}\cdot\frac{4}{3}x^{\frac{4}{3}-1} + 0 \\
&= 2x^{1/2} + 3x^{-2} - x^{1/3} \\
&= 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}.
\end{aligned}$$
This matches the original integrand on $(0, \infty)$, confirming the solution.
