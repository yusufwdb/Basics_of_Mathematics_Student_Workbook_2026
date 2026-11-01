# Exercise 14: A $0/0$ Limit with Trigonometry

## 1. Problem Statement
Compute
$$\lim_{x\to0}\frac{1-\cos x}{x^2}.$$
Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

## 2. Theoretical Background and Concepts
- **Fundamental Trigonometric Limit:**
  $$\lim_{u\to 0}\frac{\sin u}{u} = 1.$$
- **Trigonometric Identities for $1 - \cos x$:**
  There are two standard trigonometric identities that convert $1 - \cos x$ (which vanishes to second order at $x = 0$) into an expression involving $\sin^2$:
  1. **Half-angle / Power-reduction identity:**
     $$\cos x = 1 - 2\sin^2\left(\frac{x}{2}\right) \implies 1 - \cos x = 2\sin^2\left(\frac{x}{2}\right).$$
  2. **Pythagorean identity via the conjugate $1 + \cos x$:**
     $$(1 - \cos x)(1 + \cos x) = 1 - \cos^2 x = \sin^2 x \implies 1 - \cos x = \frac{\sin^2 x}{1 + \cos x}.$$

## 3. Detailed Step-by-Step Solution

As $x \to 0$, we have $\cos x \to \cos 0 = 1$, so $1 - \cos x \to 0$ and $x^2 \to 0$, giving an indeterminate form of type $\left[\frac{0}{0}\right]$. Below we present both standard trigonometric proofs (neither uses l'Hôpital's rule).

### Method 1: Using the Half-Angle Identity $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$
1. **Apply the identity:**
   Substitute $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$ into the quotient for $x \neq 0$:
   $$\frac{1 - \cos x}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{x^2}.$$
2. **Match the denominator to the half-angle $\frac{x}{2}$:**
   Notice that $x^2 = 4 \cdot \left(\frac{x}{2}\right)^2$. Rewriting the denominator accordingly gives:
   $$\frac{2\sin^2\left(\frac{x}{2}\right)}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{4\left(\frac{x}{2}\right)^2} = \frac{1}{2}\left(\frac{\sin\left(\frac{x}{2}\right)}{\frac{x}{2}}\right)^2.$$
3. **Reduce to the fundamental trigonometric limit:**
   Let $u = \frac{x}{2}$. As $x \to 0$ ($x \neq 0$), we have $u \to 0$ ($u \neq 0$), so $\lim_{x\to 0}\frac{\sin(x/2)}{x/2} = \lim_{u\to 0}\frac{\sin u}{u} = 1$.
   By the product and constant-multiple rules for limits:
   $$\lim_{x\to 0}\frac{1 - \cos x}{x^2} = \frac{1}{2}\left(\lim_{x\to 0}\frac{\sin\left(\frac{x}{2}\right)}{\frac{x}{2}}\right)^2 = \frac{1}{2} \cdot 1^2 = \frac{1}{2}.$$

---

### Method 2: Using the Pythagorean Identity $\sin^2 x + \cos^2 x = 1$
1. **Multiply numerator and denominator by $1 + \cos x$:**
   For $x$ near $0$ ($x \neq 0$), $1 + \cos x \neq 0$, so:
   $$\frac{1 - \cos x}{x^2} = \frac{(1 - \cos x)(1 + \cos x)}{x^2(1 + \cos x)} = \frac{1 - \cos^2 x}{x^2(1 + \cos x)} = \frac{\sin^2 x}{x^2(1 + \cos x)}.$$
2. **Group $\frac{\sin^2 x}{x^2}$ as $\left(\frac{\sin x}{x}\right)^2$:**
   $$\frac{1 - \cos x}{x^2} = \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}.$$
3. **Evaluate the limit of each factor:**
   Since $\lim_{x\to 0}\frac{\sin x}{x} = 1$ and $\lim_{x\to 0}\cos x = \cos 0 = 1$:
   $$\lim_{x\to 0}\frac{1 - \cos x}{x^2} = \left(\lim_{x\to 0}\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \lim_{x\to 0}\cos x} = 1^2 \cdot \frac{1}{1 + 1} = \frac{1}{2}.$$

## 4. Verification and Consistency Checks
1. **Consistency of Both Methods:** Both Method 1 (half-angle formula) and Method 2 (Pythagorean identity via conjugation) yield the exact same limit $\frac{1}{2}$.
2. **Numerical Evaluation for Small $x$ (in radians):**
   - For $x = 0.1$: $\frac{1 - \cos(0.1)}{(0.1)^2} \approx \frac{1 - 0.995004165}{0.01} = \frac{0.004995835}{0.01} \approx 0.4995835$.
   - For $x = 0.01$: $\frac{1 - \cos(0.01)}{(0.01)^2} \approx \frac{0.00004999958}{0.0001} \approx 0.4999958 \to 0.5 = \frac{1}{2}$.
   *(This also matches the second-order Taylor approximation $\cos x \approx 1 - \frac{x^2}{2}$, which gives $\frac{1 - (1 - x^2/2)}{x^2} = \frac{1}{2}$.)*
