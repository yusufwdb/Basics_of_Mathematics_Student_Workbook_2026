# Exercise 8: Choosing the Factors in Integration by Parts

## 1. Problem Statement

Compute
$$\int x\cos x\,dx.$$
Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

---

## 2. Theoretical Background and Concepts

- **Integration by Parts Formula:**
  $$\int u(x)v'(x)\,dx = u(x)v(x) - \int u'(x)v(x)\,dx.$$
- **Strategic Choice of Factors:** The goal of integration by parts is to transform the original integral $\int u v'\,dx$ into a simpler integral $\int u' v\,dx$.
  - Polynomials like $x^k$ drop in degree when differentiated, eventually becoming a constant.
  - Trigonometric functions like $\cos x$ and $\sin x$ cycle between one another whether differentiated or integrated, neither gaining nor losing complexity.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Justifying the Choice of Factors
We compare the two possible assignments for $\int x\cos x\,dx$:
1. **Correct choice ($u = x$, $v' = \cos x$):**
   Differentiating $u = x$ gives $u' = 1$, which eliminates the algebraic factor $x$. Integrating $v' = \cos x$ gives $v = \sin x$. The new integral is $\int 1 \cdot \sin x\,dx = \int \sin x\,dx$, which is an immediate elementary integral.
2. **Reverse choice ($u = \cos x$, $v' = x$):**
   Differentiating $u = \cos x$ gives $u' = -\sin x$, while integrating $v' = x$ raises the power to $v = \frac{1}{2}x^2$. The new integral would be $-\int \frac{1}{2}x^2\sin x\,dx$, which has a higher degree of $x$ than the original integral and is **more complicated** rather than simpler.

### Step 2: Computing the Integral by Parts
Using the convenient choice:
$$\begin{aligned}
u(x) &= x & \implies \quad du &= dx, \\
dv &= \cos x\,dx & \implies \quad v(x) &= \sin x.
\end{aligned}$$
Applying $\int u\,dv = uv - \int v\,du$:
$$\begin{aligned}
\int x\cos x\,dx &= x\sin x - \int \sin x\,dx \\
&= x\sin x - (-\cos x) + C \\
&= x\sin x + \cos x + C, \quad C \in \mathbb{R}.
\end{aligned}$$

---

## 4. Verification and Consistency Checks

We differentiate $F(x) = x\sin x + \cos x + C$ using the product rule on $x\sin x$:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}(x\sin x) + \frac{d}{dx}(\cos x) + \frac{d}{dx}(C) \\
&= \left[(x)'\sin x + x(\sin x)'\right] - \sin x + 0 \\
&= \left(1 \cdot \sin x + x\cos x\right) - \sin x \\
&= x\cos x.
\end{aligned}$$
The derivative equals the original integrand for all $x \in \mathbb{R}$, confirming the solution.
