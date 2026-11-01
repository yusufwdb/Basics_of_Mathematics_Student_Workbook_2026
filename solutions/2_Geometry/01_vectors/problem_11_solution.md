# Exercise 11: Decomposition into Parallel and Perpendicular Components

## 1. Problem Statement

Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check
$$u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.$$
Explain why these are two independent checks of correctness.

## 2. Theoretical Background and Concepts

1. **Orthogonal Decomposition Theorem:**
   Given any vector $u \in \mathbb{R}^n$ and any non-zero reference vector $v \in \mathbb{R}^n$, $u$ can be **uniquely** decomposed as:
   $$u = u_{\parallel} + u_{\perp}$$
   where:
   - $u_{\parallel}$ lies in the subspace spanned by $v$ (i.e., $u_{\parallel} = \alpha v$ for some scalar $\alpha \in \mathbb{R}$), given by the orthogonal projection:
     $$u_{\parallel} = \operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v$$
   - $u_{\perp}$ is orthogonal to $v$ (i.e., $u_{\perp} \cdot v = 0$), given by the remainder:
     $$u_{\perp} = u - u_{\parallel}$$

2. **Uniqueness of the Decomposition:**
   The conditions (i) $u_{\parallel} = \alpha v$, (ii) $u_{\parallel} + u_{\perp} = u$, and (iii) $u_{\perp} \cdot v = 0$ uniquely determine both $u_{\parallel}$ and $u_{\perp}$.

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (3, 4), \qquad v = (1, 2)$$

### Step 1: Compute the parallel component $u_{\parallel}$
First, evaluate the dot products $u \cdot v$ and $v \cdot v$:
$$u \cdot v = (3)(1) + (4)(2) = 3 + 8 = 11$$
$$v \cdot v = \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5$$
Therefore, the projection of $u$ onto $v$ is:
$$u_{\parallel} = \frac{u \cdot v}{v \cdot v}\, v = \frac{11}{5}(1, 2) = \left(\frac{11}{5},\, \frac{22}{5}\right) = (2.2,\, 4.4)$$

### Step 2: Compute the perpendicular component $u_{\perp}$
Subtract $u_{\parallel}$ from $u$:
$$u_{\perp} = u - u_{\parallel} = (3, 4) - \left(\frac{11}{5},\, \frac{22}{5}\right) = \left(\frac{15}{5} - \frac{11}{5},\, \frac{20}{5} - \frac{22}{5}\right) = \left(\frac{4}{5},\, -\frac{2}{5}\right) = (0.8,\, -0.4)$$

### Step 3: Check $u = u_{\parallel} + u_{\perp}$ and $u_{\perp} \cdot v = 0$
1. **Sum check ($u = u_{\parallel} + u_{\perp}$):**
   $$u_{\parallel} + u_{\perp} = \left(\frac{11}{5},\, \frac{22}{5}\right) + \left(\frac{4}{5},\, -\frac{2}{5}\right) = \left(\frac{11 + 4}{5},\, \frac{22 - 2}{5}\right) = \left(\frac{15}{5},\, \frac{20}{5}\right) = (3, 4) = u \quad \checkmark$$
2. **Orthogonality check ($u_{\perp} \cdot v = 0$):**
   $$u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4}{5} - \frac{4}{5} = 0 \quad \checkmark$$

### Step 4: Explain why these are two independent checks of correctness
- **Check 1 ($u_{\parallel} + u_{\perp} = u$)** verifies **completeness of the decomposition** (that no part of $u$ was lost or miscalculated during subtraction). However, by itself, $a + b = u$ holds for infinitely many pairs of vectors (for instance, taking any wrong scalar multiple $u_{\parallel} = c v$ and setting $u_{\perp} = u - c v$ automatically satisfies $u_{\parallel} + u_{\perp} = u$, even when $c \neq \frac{11}{5}$).
- **Check 2 ($u_{\perp} \cdot v = 0$)** verifies the **geometric orthogonality condition** (that the projection scalar $c = \frac{u \cdot v}{v \cdot v}$ was computed correctly so that the residual is genuinely perpendicular to $v$). Conversely, by itself, $u_{\perp} \cdot v = 0$ holds for any scalar multiple of $(2, -1)$, such as $(0,0)$ or $(2,-1)$, which would not sum with $u_{\parallel}$ to give $u$.
- Only when **both** conditions hold simultaneously (along with $u_{\parallel}$ being a multiple of $v$) are we guaranteed that $u_{\parallel}$ and $u_{\perp}$ are the unique parallel and perpendicular components of $u$.

## 4. Verification and Consistency Checks

**Pythagorean Theorem Check ($\|u\|^2 = \|u_{\parallel}\|^2 + \|u_{\perp}\|^2$):**
- $\|u\|^2 = 3^2 + 4^2 = 9 + 16 = 25$
- $\|u_{\parallel}\|^2 = \left(\frac{11}{5}\right)^2 + \left(\frac{22}{5}\right)^2 = \frac{121 + 484}{25} = \frac{605}{25} = \frac{121}{5} = 24.2$
- $\|u_{\perp}\|^2 = \left(\frac{4}{5}\right)^2 + \left(-\frac{2}{5}\right)^2 = \frac{16 + 4}{25} = \frac{20}{25} = \frac{4}{5} = 0.8$

Summing the squared norms of the components:
$$\|u_{\parallel}\|^2 + \|u_{\perp}\|^2 = \frac{121}{5} + \frac{4}{5} = \frac{125}{5} = 25 = \|u\|^2 \quad \checkmark$$
This confirms the accuracy of both components.
