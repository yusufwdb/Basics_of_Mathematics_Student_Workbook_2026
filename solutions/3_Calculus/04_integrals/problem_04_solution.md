# Exercise 4: Substitution as Reversing the Chain Rule

## 1. Problem Statement

Compute
$$\int 2x(x^2+1)^4\,dx.$$
Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

---

## 2. Theoretical Background and Concepts

- **Chain Rule for Differentiation:** If $G(u)$ and $u = g(x)$ are differentiable functions, then the derivative of the composite function $F(x) = G(g(x))$ is
  $$\frac{d}{dx}\left[G(g(x))\right] = G'(g(x)) \cdot g'(x).$$
- **Integration by Substitution ($u$-Substitution):** Reading the chain rule in reverse, if $G'(u) = f(u)$, then
  $$\int f(g(x)) \cdot g'(x)\,dx = \int f(u)\,du = G(u) + C = G(g(x)) + C,$$
  where we substitute $u = g(x)$ and $du = g'(x)\,dx$.
- **How to Recognize a Substitution:** Look for an "inner function" $u = g(x)$ nested inside another operation (here, raised to the 4th power) whose derivative $g'(x)$ multiplies the rest of the integrand (up to a constant factor).

---

## 3. Detailed Step-by-Step Solution

### Step 1: Identifying the Candidate for $u$ and Its Derivative
In the integrand $2x(x^2+1)^4$, the expression $x^2+1$ is raised to the power $4$. This makes the inner function
$$u = g(x) = x^2 + 1$$
the natural candidate for substitution. Differentiating $u$ with respect to $x$ gives:
$$\frac{du}{dx} = 2x \implies du = 2x\,dx.$$
Observe that the exact factor $2x\,dx$ appears explicitly in the integrand:
$$\int 2x(x^2+1)^4\,dx = \int \underbrace{(x^2+1)^4}_{u^4} \cdot \underbrace{2x\,dx}_{du}.$$

### Step 2: Transforming and Computing the Integral in Terms of $u$
Substituting $u = x^2 + 1$ and $du = 2x\,dx$ reduces the integral to a basic power-rule integral:
$$\int 2x(x^2+1)^4\,dx = \int u^4\,du = \frac{u^{4+1}}{4+1} + C = \frac{u^5}{5} + C.$$

### Step 3: Back-Substituting to the Original Variable $x$
Replacing $u$ with $x^2 + 1$, we obtain the final family of antiderivatives:
$$\int 2x(x^2+1)^4\,dx = \frac{1}{5}(x^2+1)^5 + C, \quad C \in \mathbb{R}.$$

---

## 4. Verification and Consistency Checks

### Check 1: Differentiation via the Chain Rule
Let $F(x) = \frac{1}{5}(x^2+1)^5 + C$. Applying the chain rule:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left[\frac{1}{5}(x^2+1)^5 + C\right] \\
&= \frac{1}{5} \cdot 5(x^2+1)^{5-1} \cdot \frac{d}{dx}(x^2+1) + 0 \\
&= (x^2+1)^4 \cdot (2x) \\
&= 2x(x^2+1)^4.
\end{aligned}$$
This recovers the exact integrand.

### Check 2: Leading-Term Degree Check
If expanded as a polynomial, $2x(x^2+1)^4$ has leading term $2x \cdot (x^2)^4 = 2x^9$, whose antiderivative has leading term $\frac{2}{10}x^{10} = \frac{1}{5}x^{10}$. Indeed, the leading term of $\frac{1}{5}(x^2+1)^5$ is $\frac{1}{5}(x^2)^5 = \frac{1}{5}x^{10}$, confirming consistency.
