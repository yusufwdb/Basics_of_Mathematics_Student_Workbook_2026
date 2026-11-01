# Exercise 3: Recognizing Basic Antiderivatives

## 1. Problem Statement

Compute
$$\int\left(2e^x+3\cos x-4\sin x\right)\,dx.$$
Match each term with a known derivative and verify the entire result with one differentiation.

---

## 2. Theoretical Background and Concepts

- **Catalogue of Elementary Derivatives and Antiderivatives:**
  Every elementary integration formula is obtained by reading a standard differentiation formula in reverse:
  1. Since $\frac{d}{dx}\left(e^x\right) = e^x$, we have $\int e^x\,dx = e^x + C$.
  2. Since $\frac{d}{dx}\left(\sin x\right) = \cos x$, we have $\int \cos x\,dx = \sin x + C$.
  3. Since $\frac{d}{dx}\left(\cos x\right) = -\sin x$, multiplying by $-1$ gives $\frac{d}{dx}\left(-\cos x\right) = \sin x$, so $\int \sin x\,dx = -\cos x + C$.
- **Linearity of the Indefinite Integral:**
  $$\int \left(a f(x) + b g(x) + c h(x)\right)\,dx = a\int f(x)\,dx + b\int g(x)\,dx + c\int h(x)\,dx.$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Matching Each Term with a Known Derivative
We inspect the three terms of the integrand $f(x) = 2e^x + 3\cos x - 4\sin x$ (defined for all $x \in \mathbb{R}$):
1. **Exponential term $2e^x$:**
   We know that $\left(e^x\right)' = e^x$. By linearity, $\left(2e^x\right)' = 2e^x$.
2. **Cosine term $3\cos x$:**
   We know that $(\sin x)' = \cos x$. Therefore, $(3\sin x)' = 3\cos x$.
3. **Sine term $-4\sin x$:**
   We know that $(\cos x)' = -\sin x$. Multiplying both sides by $4$ yields $(4\cos x)' = -4\sin x$. (Note how the minus sign in $-4\sin x$ pairs naturally with the minus sign produced when differentiating $\cos x$.)

### Step 2: Computing the Indefinite Integral
Summing the antiderivatives of the individual terms and adding the arbitrary constant $C \in \mathbb{R}$:
$$\begin{aligned}
\int\left(2e^x + 3\cos x - 4\sin x\right)\,dx &= 2\int e^x\,dx + 3\int \cos x\,dx - 4\int \sin x\,dx \\
&= 2e^x + 3\sin x - 4(-\cos x) + C \\
&= 2e^x + 3\sin x + 4\cos x + C.
\end{aligned}$$

---

## 4. Verification and Consistency Checks

We differentiate the resulting family of functions $F(x) = 2e^x + 3\sin x + 4\cos x + C$ in a single calculation:
$$\begin{aligned}
F'(x) &= \frac{d}{dx}\left(2e^x + 3\sin x + 4\cos x + C\right) \\
&= 2\frac{d}{dx}(e^x) + 3\frac{d}{dx}(\sin x) + 4\frac{d}{dx}(\cos x) + \frac{d}{dx}(C) \\
&= 2e^x + 3\cos x + 4(-\sin x) + 0 \\
&= 2e^x + 3\cos x - 4\sin x.
\end{aligned}$$
The derivative matches the integrand identically for all $x \in \mathbb{R}$, paying special attention to the signs of the trigonometric terms.
