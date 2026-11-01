# Exercise 14: Continuity and Differentiability of a Piecewise Function

## 1. Problem Statement
Investigate the behavior at $x=0$ of
$$f(x)=\begin{cases}x^2,&x\ge0,\\ax,&x<0.\end{cases}$$
For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

---

## 2. Theoretical Background and Concepts
- **Continuity at a Point $x_0$:** A function $f$ is continuous at $x_0$ if and only if its left-hand limit, right-hand limit, and function value at $x_0$ all exist and are equal:
  $$\lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = f(x_0)$$
- **One-Sided Derivatives at $x_0$:**
  - **Right-hand derivative:** $f'_+(x_0) = \lim_{h \to 0^+} \frac{f(x_0+h) - f(x_0)}{h}$
  - **Left-hand derivative:** $f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0+h) - f(x_0)}{h}$
- **Differentiability Criterion:** A function $f$ is differentiable at $x_0$ if and only if both one-sided derivatives $f'_-(x_0)$ and $f'_+(x_0)$ exist (as finite real numbers) and are equal:
  $$f'_-(x_0) = f'_+(x_0)$$
- **Relationship Between Differentiability and Continuity:** Differentiability at $x_0$ implies continuity at $x_0$, but **continuity does NOT imply differentiability**. A continuous graph can still have a sharp corner (kink) where the left-hand and right-hand slopes meet at different angles.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Analyze continuity at $x = 0$
1. **Function value at $x = 0$:** Using the first branch ($x \ge 0$),
   $$f(0) = 0^2 = 0$$
2. **Right-hand limit at $x = 0$:** For $x > 0$, $f(x) = x^2$, so
   $$\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} x^2 = 0$$
3. **Left-hand limit at $x = 0$:** For $x < 0$, $f(x) = ax$, so
   $$\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (ax) = a \cdot 0 = 0$$

Since $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0) = 0$ regardless of the value of $a$, **the function $f$ is continuous at $x = 0$ (and hence on all of $\mathbb{R}$) for every real parameter $a \in \mathbb{R}$.**

### Step 2: Compute the one-sided derivatives at $x = 0$
Using the definition of one-sided derivatives with $f(0) = 0$:
1. **Right-hand derivative ($h \to 0^+$, so $h > 0$):**
   $$f'_+(0) = \lim_{h \to 0^+} \frac{f(0+h) - f(0)}{h} = \lim_{h \to 0^+} \frac{h^2 - 0}{h} = \lim_{h \to 0^+} h = 0$$
2. **Left-hand derivative ($h \to 0^-$, so $h < 0$):**
   $$f'_-(0) = \lim_{h \to 0^-} \frac{f(0+h) - f(0)}{h} = \lim_{h \to 0^-} \frac{ah - 0}{h} = \lim_{h \to 0^-} a = a$$

Therefore:
- Both one-sided derivatives $f'_+(0) = 0$ and $f'_-(0) = a$ **exist for all $a \in \mathbb{R}$**.
- They **agree** ($f'_-(0) = f'_+(0)$) if and only if:
  $$a = 0$$

### Step 3: Determine differentiability at $x = 0$
Since a function is differentiable at $x = 0$ if and only if $f'_-(0) = f'_+(0)$, **$f$ is differentiable at $x = 0$ if and only if $a = 0$** (in which case $f'(0) = 0$).

### Step 4: Explain why continuity alone is not sufficient for differentiability
- Continuity at $x = 0$ only guarantees that the two branches of the graph **connect at the same point** $(0, 0)$ without a jump or break. Because $ax = 0$ at $x = 0$ for *every* $a \in \mathbb{R}$, the ray $y = ax$ ($x < 0$) always meets the parabola $y = x^2$ ($x \ge 0$) at the origin $(0,0)$.
- Differentiability requires a stronger geometric property: the two branches must join **smoothly with the same tangent slope**. The parabola $y = x^2$ approaches the origin horizontally with slope $f'_+(0) = 0$, whereas the line $y = ax$ approaches the origin with slope $f'_-(0) = a$. Whenever $a \neq 0$, the graph has a **sharp corner (kink)** at $(0, 0)$, so no unique tangent line exists there despite the function being continuous.

---

## 4. Verification and Consistency Checks

### Specific Case Comparison ($a = 1$ vs. $a = 0$)
- **Case $a = 1$:** For $x \approx 0$, $f(x) = x$ for $x < 0$ and $f(x) = x^2$ for $x \ge 0$. At $x = -0.01$, the slope is $1$; at $x = +0.01$, the slope is $2(0.01) = 0.02$. As $x \to 0$, the left slope stays at $1$ while the right slope approaches $0$, forming a $45^\circ$-to-$0^\circ$ corner at $(0,0)$.
- **Case $a = 0$:** For $x < 0$, $f(x) = 0$, which is the negative $x$-axis (slope $0$). At $(0,0)$, it transitions smoothly into the parabola $y = x^2$, whose tangent line at $(0,0)$ is also the $x$-axis (slope $0$). Here $f'(x) = \max(0, 2x)$ is continuous and well-defined everywhere, with $f'(0) = 0$.
