# Exercise 13: A Logarithm and an Asymptote

## 1. Problem Statement
Perform a complete analysis of
$$f(x)=\frac{\ln x}{x},\qquad x>0.$$
Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

---

## 2. Theoretical Background and Concepts
- **Quotient Rule with the Natural Logarithm:**
  $$\frac{d}{dx}\left(\frac{\ln x}{x}\right) = \frac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}$$
- **Asymptotic Comparison of Logarithms and Powers:** As $x \to +\infty$, the natural logarithm $\ln x$ grows much more slowly than any positive power $x^\alpha$ ($\alpha > 0$):
  $$\lim_{x \to \infty} \frac{\ln x}{x} = 0$$

---

## 3. Detailed Step-by-Step Solution

### 1. Domain, Zeros, and Sign
- **Domain:** Given explicitly as $D_f = (0, \infty)$, which matches the natural domain of $\ln x$ with $x \neq 0$.
- **Zero ($x$-intercept):** Since $x > 0$,
  $$f(x) = \frac{\ln x}{x} = 0 \iff \ln x = 0 \iff x = 1$$
  Thus $(1, 0)$ is the unique $x$-intercept.
- **Sign of $f(x)$:**
  - On $(0, 1)$: $\ln x < 0$ and $x > 0 \implies f(x) < 0$.
  - On $(1, \infty)$: $\ln x > 0$ and $x > 0 \implies f(x) > 0$.

### 2. Behavior at the Ends of the Domain (Asymptotes)
1. **Left end of the domain ($x \to 0^+$):**
   As $x \to 0^+$, $\ln x \to -\infty$ and $\frac{1}{x} \to +\infty$. The product of $-\infty$ and $+\infty$ is not indeterminate:
   $$\lim_{x \to 0^+} \frac{\ln x}{x} = \lim_{x \to 0^+} (\ln x) \cdot \frac{1}{x} = (-\infty)(+\infty) = -\infty$$
   Therefore, **$x = 0$ (the $y$-axis) is a right-hand vertical asymptote**.
2. **Right end of the domain ($x \to +\infty$):**
   As $x \to +\infty$, both $\ln x \to \infty$ and $x \to \infty$, giving an indeterminate form $\left[\frac{\infty}{\infty}\right]$. Applying L'Hôpital's Rule (or the standard growth hierarchy $\ln x \ll x$):
   $$\lim_{x \to \infty} \frac{\ln x}{x} \stackrel{\text{H}}{=} \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = 0^+$$
   Therefore, **$y = 0$ (the positive $x$-axis) is a right-hand horizontal asymptote**, approached from above.

### 3. First Derivative, Monotonicity, and Maximum
Differentiating $f(x) = \frac{\ln x}{x}$ using the quotient rule for $x > 0$:
$$f'(x) = \frac{\left(\frac{1}{x}\right)x - (\ln x)(1)}{x^2} = \frac{1 - \ln x}{x^2}$$
Setting $f'(x) = 0$:
$$1 - \ln x = 0 \iff \ln x = 1 \iff x = e \approx 2.718$$

Since $x^2 > 0$ for all $x > 0$, the sign of $f'(x)$ matches the sign of $1 - \ln x$:
- On $(0, e)$: $\ln x < 1 \implies 1 - \ln x > 0 \implies f'(x) > 0$ (**strictly increasing**).
- At $x = e$: $f'(e) = 0$.
- On $(e, \infty)$: $\ln x > 1 \implies 1 - \ln x < 0 \implies f'(x) < 0$ (**strictly decreasing**).

| Interval / Point | $(0, e)$ | $x = e$ | $(e, \infty)$ |
| :--- | :---: | :---: | :---: |
| **Sign of $f'(x)$** | $+$ | $0$ | $-$ |
| **Behavior of $f(x)$** | Strictly increasing ($-\infty \nearrow \frac{1}{e}$) | **Global Maximum** $\left(\frac{1}{e}\right)$ | Strictly decreasing ($\frac{1}{e} \searrow 0^+$) |

Thus $f$ attains its **unique local and global maximum** at $x = e$:
$$f_{\max} = f(e) = \frac{\ln e}{e} = \frac{1}{e} \approx 0.368$$

### 4. Second Derivative, Convexity, and Inflection Point
Differentiating $f'(x) = \frac{1 - \ln x}{x^2}$:
$$f''(x) = \frac{\left(-\frac{1}{x}\right)x^2 - (1 - \ln x)(2x)}{x^4} = \frac{-x - 2x + 2x\ln x}{x^4} = \frac{2\ln x - 3}{x^3}$$
Setting $f''(x) = 0$:
$$2\ln x - 3 = 0 \iff \ln x = \frac{3}{2} \iff x = e^{3/2} = e\sqrt{e} \approx 4.48$$
- On $\left(0, e^{3/2}\right]$: $f''(x) \le 0 \implies f$ is **concave (concave down, $\cap$)**.
- On $\left[e^{3/2}, \infty\right)$: $f''(x) \ge 0 \implies f$ is **convex (concave up, $\cup$)**.
- **Inflection Point:** $\left(e^{3/2}, \frac{3}{2e^{3/2}}\right) \approx (4.48, 0.335)$.

### 5. Which Information Is Necessary for a Correct Sketch (and Graph)
To sketch $f(x) = \frac{\ln x}{x}$ accurately, five pieces of information are indispensable:
1. **Domain $x > 0$ and vertical asymptote $\lim_{x \to 0^+} f(x) = -\infty$:** Shows the graph exists only to the right of the $y$-axis and plunges down along it.
2. **Unique $x$-intercept at $(1, 0)$:** Shows where the graph crosses from negative to positive values.
3. **Global maximum at $\left(e, \frac{1}{e}\right)$:** Shows the curve peaks at $x = e \approx 2.72$ with height $\frac{1}{e} \approx 0.37$.
4. **Horizontal asymptote $\lim_{x \to \infty} f(x) = 0^+$:** Shows that after peaking at $x = e$, the curve does *not* cross the $x$-axis again, but decays toward $y = 0$ from above.
5. **Inflection point at $x = e^{3/2} \approx 4.48$:** Shows where the curve transitions from concave down (around the peak) to concave up (as it flattens along the $x$-axis).

```
          y
          ^
      1/e |             * (e, 1/e) [Global Max]
          |          .     .   o (e^(3/2), 3/(2e^(3/2))) [Inflection Point]
          |        .           . . . . . . .
   -------+------*-------------------------------> x (y = 0 Asymptote)
          |    (1,0)   2    e        4.5
       -1 |    .
       -2 |   . (x = 0 Vertical Asymptote)
```

---

## 4. Verification and Consistency Checks

### Classic Application: Comparing $e^\pi$ and $\pi^e$
Since $f(x) = \frac{\ln x}{x}$ attains its strict global maximum at $x = e$ and is strictly decreasing on $[e, \infty)$, for $e < \pi$ we immediately have:
$$f(e) > f(\pi) \implies \frac{\ln e}{e} > \frac{\ln \pi}{\pi} \implies \pi \ln e > e \ln \pi \implies \ln\left(e^\pi\right) > \ln\left(\pi^e\right) \implies e^\pi > \pi^e$$
Indeed, $e^\pi \approx 23.14 > 22.46 \approx \pi^e$, providing a famous verification of the global maximum of $\frac{\ln x}{x}$ at $x = e$.
