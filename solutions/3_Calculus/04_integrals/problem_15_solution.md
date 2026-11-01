# Exercise 15: Recovering a Function from Its Derivative and a Condition

## 1. Problem Statement

The function $F$ satisfies
$$F'(x)=2xe^{x^2}$$
and
$$F(0)=3.$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0)=3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x=0$.

---

## 2. Theoretical Background and Concepts

- **Initial Value Problem (IVP) for Antiderivatives:**
  Given a derivative $F'(x) = f(x)$ and an initial (or point) condition $F(x_0) = y_0$:
  1. First, compute the indefinite integral $F(x) = \int f(x)\,dx = G(x) + C$ to obtain the general one-parameter family of antiderivatives.
  2. Second, substitute $x = x_0$ and $F(x_0) = y_0$ into $G(x_0) + C = y_0$ to solve uniquely for the constant $C = y_0 - G(x_0)$.
- **Substitution Rule ($\int f(g(x))g'(x)\,dx$):**
  When an integrand has the form $g'(x)e^{g(x)}$, substituting $u = g(x)$ and $du = g'(x)\,dx$ yields $\int e^u\,du = e^u + C = e^{g(x)} + C$.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Recognizing the Integration Method
To find $F(x)$ from $F'(x) = 2xe^{x^2}$, we need to compute $\int 2xe^{x^2}\,dx$.
We choose **integration by substitution** ($u$-substitution). We recognize this method because $e^{x^2}$ is a composite function with inner function $u = x^2$, and its exact derivative $u' = 2x$ multiplies $e^{x^2}$ in the integrand.

### Part 2: Determining the Entire Family of Antiderivatives
Let $u = x^2$. Differentiating with respect to $x$ gives:
$$du = 2x\,dx.$$
Substituting $u = x^2$ and $du = 2x\,dx$ into the indefinite integral:
$$F(x) = \int 2xe^{x^2}\,dx = \int e^u\,du = e^u + C = e^{x^2} + C, \quad C \in \mathbb{R}.$$
Thus, the general family of functions with derivative $2xe^{x^2}$ is $F(x) = e^{x^2} + C$.

### Part 3: Using the Condition $F(0) = 3$ to Determine $C$
We substitute $x = 0$ into the general formula $F(x) = e^{x^2} + C$ and set it equal to $3$:
$$F(0) = e^{0^2} + C = 3.$$
Since $e^0 = 1$, this gives:
$$1 + C = 3 \implies C = 3 - 1 = 2.$$
*(Note: A common mistake is to assume $C = F(0) = 3$ without evaluating $e^0 = 1$; always substitute $x = 0$ explicitly!)*

Therefore, the unique function satisfying both conditions is:
$$F(x) = e^{x^2} + 2.$$

---

## 4. Verification and Consistency Checks

### Part 4: Verification by Differentiation and Substitution of $x = 0$
1. **Differentiation Check:**
   Applying the chain rule to $F(x) = e^{x^2} + 2$:
   $$F'(x) = \frac{d}{dx}\left(e^{x^2} + 2\right) = e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 = 2xe^{x^2}. \quad \checkmark$$
2. **Initial Condition Check at $x = 0$:**
   Evaluating $F(x) = e^{x^2} + 2$ at $x = 0$:
   $$F(0) = e^{0^2} + 2 = e^0 + 2 = 1 + 2 = 3. \quad \checkmark$$

Both conditions of the problem are satisfied identically.
