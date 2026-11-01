# Exercise 6: Average Value of a Function

## 1. Problem Statement

Compute the average value of the function
$$f(x)=x^2$$
on the interval $[0,3]$.

Find a point $c\in[0,3]$ for which $f(c)$ is equal to this average value, and interpret the result geometrically.

---

## 2. Theoretical Background and Concepts

- **Average Value of a Continuous Function on $[a,b]$:**
  Generalizing the arithmetic mean of $n$ discrete values $\frac{1}{n}\sum_{i=1}^n y_i$ to a continuum of values on $[a,b]$, the average (mean) value $f_{\text{avg}}$ of a continuous function $f(x)$ on $[a,b]$ is defined as the integral divided by the interval length:
  $$f_{\text{avg}} = \frac{1}{b - a}\int_a^b f(x)\,dx.$$
- **Mean Value Theorem for Integrals:**
  If $f$ is continuous on $[a,b]$, there exists at least one point $c \in [a,b]$ such that $f(c)$ equals the average value of $f$:
  $$f(c) = \frac{1}{b - a}\int_a^b f(x)\,dx \iff \int_a^b f(x)\,dx = f(c)(b - a).$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Computing the Average Value of $f(x) = x^2$ on $[0, 3]$
Applying the average value formula with $a = 0$, $b = 3$, and $f(x) = x^2$:
$$\begin{aligned}
f_{\text{avg}} &= \frac{1}{3 - 0}\int_0^3 x^2\,dx \\
&= \frac{1}{3}\left[\frac{1}{3}x^3\right]_0^3 \\
&= \frac{1}{3}\left(\frac{3^3}{3} - 0\right) \\
&= \frac{1}{3}(9) = 3.
\end{aligned}$$
Thus, the average value of $f(x) = x^2$ on $[0, 3]$ is $f_{\text{avg}} = 3$.

### Step 2: Finding $c \in [0, 3]$ Such That $f(c) = f_{\text{avg}}$
We solve the equation $f(c) = 3$ for $c \in [0, 3]$:
$$c^2 = 3 \implies c = \pm\sqrt{3}.$$
Since $c$ must belong to the interval $[0, 3]$, we reject $-\sqrt{3}$ and obtain:
$$c = \sqrt{3} \approx 1.732 \in [0, 3].$$

### Step 3: Geometric Interpretation of the Result
Rewriting $f_{\text{avg}} = \frac{1}{3}\int_0^3 x^2\,dx = 3$ in the form
$$\int_0^3 x^2\,dx = f(c) \cdot (3 - 0) = 3 \times 3 = 9$$
gives a direct geometric interpretation:
- The **area under the parabola $y = x^2$** on the interval $[0, 3]$ (which equals $9$) is **exactly equal to the area of a rectangle** over the same base $[0, 3]$ (width $3$) with constant height $y = f(\sqrt{3}) = 3$.
- Equivalently, if the horizontal line $y = 3$ is drawn across $[0, 3]$, the area of the region where the parabola rises **above** the line $y = 3$ (on $[\sqrt{3}, 3]$) exactly fills the empty region where the parabola lies **below** the line $y = 3$ (on $[0, \sqrt{3}]$), as if "leveling out" sand piled in the shape of $y = x^2$ to a flat horizontal layer of depth $3$.

---

## 4. Verification and Consistency Checks

Let us verify the "equal-area leveling" property directly by checking that $\int_0^3 (x^2 - 3)\,dx = 0$:
- Area deficit on $[0, \sqrt{3}]$:
  $$\int_0^{\sqrt{3}} (3 - x^2)\,dx = \left[3x - \frac{1}{3}x^3\right]_0^{\sqrt{3}} = 3\sqrt{3} - \frac{3\sqrt{3}}{3} = 2\sqrt{3}.$$
- Area surplus on $[\sqrt{3}, 3]$:
  $$\int_{\sqrt{3}}^3 (x^2 - 3)\,dx = \left[\frac{1}{3}x^3 - 3x\right]_{\sqrt{3}}^3 = (9 - 9) - \left(\sqrt{3} - 3\sqrt{3}\right) = 2\sqrt{3}.$$
The deficit below $y = 3$ and the surplus above $y = 3$ are both equal to $2\sqrt{3}$, confirming $f_{\text{avg}} = 3$ and $c = \sqrt{3}$.
