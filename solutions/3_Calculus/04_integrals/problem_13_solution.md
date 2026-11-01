# Exercise 13: An Integral Depending on the Upper Limit

## 1. Problem Statement

Let
$$F(x)=\int_0^x(t^2+1)\,dt.$$
Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

---

## 2. Theoretical Background and Concepts

- **Area Accumulation Function:** Given a continuous function $f(t)$, the function defined by integrating from a fixed lower limit $a$ to a variable upper limit $x$,
  $$F(x) = \int_a^x f(t)\,dt,$$
  represents the net signed area accumulated under the graph of $y = f(t)$ from $t = a$ to $t = x$. (Note: a dummy variable $t$ is used inside the integral to avoid confusion with the upper limit $x$.)
- **First Fundamental Theorem of Calculus (Derivative of an Integral with Respect to Its Upper Limit):**
  If $f$ is continuous on an interval $I$ containing $a$, then the accumulation function $F(x) = \int_a^x f(t)\,dt$ is differentiable on $I$, and its derivative is simply the integrand evaluated at the upper limit $x$:
  $$F'(x) = \frac{d}{dx}\int_a^x f(t)\,dt = f(x).$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Determining the Explicit Formula for $F(x)$
An antiderivative of $f(t) = t^2 + 1$ with respect to $t$ is $\frac{1}{3}t^3 + t$. Evaluating this antiderivative from the lower limit $t = 0$ to the upper limit $t = x$:
$$\begin{aligned}
F(x) &= \int_0^x (t^2 + 1)\,dt \\
&= \left[\frac{1}{3}t^3 + t\right]_{t=0}^{t=x} \\
&= \left(\frac{1}{3}x^3 + x\right) - \left(\frac{1}{3}(0)^3 + 0\right) \\
&= \frac{1}{3}x^3 + x.
\end{aligned}$$

### Step 2: Computing $F'(x)$ and Comparing with the Integrand
Differentiating the explicit expression $F(x) = \frac{1}{3}x^3 + x$ with respect to $x$:
$$F'(x) = \frac{d}{dx}\left(\frac{1}{3}x^3 + x\right) = \frac{1}{3}(3x^2) + 1 = x^2 + 1.$$
**Comparison:** The derivative $F'(x) = x^2 + 1$ is **identical to the integrand $f(t) = t^2 + 1$ evaluated at $t = x$**. This explicitly demonstrates the First Fundamental Theorem of Calculus.

### Step 3: Explaining Why the Height of the Function Describes the Local Rate of Increase of Accumulated Area
Imagine moving the right boundary $x$ slightly to the right by a tiny increment $\Delta x > 0$, to $x + \Delta x$.
1. The change in accumulated area is the thin vertical strip of area added between $x$ and $x + \Delta x$:
   $$\Delta F = F(x + \Delta x) - F(x) = \int_x^{x+\Delta x} f(t)\,dt.$$
2. When the width $\Delta x$ is very small, the curve $y = f(t)$ is nearly constant over $[x, x + \Delta x]$ and approximately equal to the height $f(x)$ at the left edge. Thus, the thin strip is approximately a rectangle of **width $\Delta x$** and **height $f(x)$**:
   $$\Delta F \approx \text{height} \times \text{width} = f(x) \cdot \Delta x.$$
3. Dividing both sides by the width $\Delta x$ gives the average rate of change of the area per unit change in $x$:
   $$\frac{\Delta F}{\Delta x} \approx f(x).$$
4. Taking the limit as $\Delta x \to 0$, the approximation becomes exact: the instantaneous rate at which accumulated area grows as the right boundary $x$ moves is equal to the height $f(x)$ of the curve at that boundary:
   $$F'(x) = \lim_{\Delta x \to 0}\frac{\Delta F}{\Delta x} = f(x).$$

---

## 4. Verification and Consistency Checks

1. **Initial Value Check at $x = 0$:** When the upper limit equals the lower limit ($x = 0$), no area has been accumulated, so $F(0) = \int_0^0 (t^2+1)\,dt = 0$. Substituting $x = 0$ into our formula $F(x) = \frac{1}{3}x^3 + x$ gives $F(0) = 0$.
2. **Consistency with Exercise 10 at $x = 2$:** In Exercise 10 we found $\int_0^2 (t^2+1)\,dt = \frac{14}{3}$. Substituting $x = 2$ into $F(x) = \frac{1}{3}x^3 + x$ gives $F(2) = \frac{8}{3} + 2 = \frac{14}{3}$, confirming consistency.
