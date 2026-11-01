# Exercise 3: A Box Made from Cardboard

## 1. Problem Statement

From a $30\text{ cm}\times40\text{ cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

---

## 2. Theoretical Background and Concepts

- **3D Geometric Modeling from a 2D Net:**
  When a square of side $x$ is cut from each of the four corners of a rectangular sheet of dimensions $L \times W$ and the four flaps are folded up by $90^\circ$:
  - Both ends of the length $L$ lose $x$, so the base length becomes $L - 2x$.
  - Both ends of the width $W$ lose $x$, so the base width becomes $W - 2x$.
  - The height of the resulting open-top rectangular box is $x$.
  - The volume of the rectangular box is $V = \text{length} \times \text{width} \times \text{height}$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Writing the Volume as a Function of $x$
Given the cardboard sheet of dimensions $30\text{ cm} \times 40\text{ cm}$, after cutting a square of side $x\text{ cm}$ from each corner and folding up the sides, the dimensions of the box are:
- Base width: $30 - 2x\text{ cm}$
- Base length: $40 - 2x\text{ cm}$
- Height: $x\text{ cm}$

Therefore, the volume $V(x)$ (in $\text{cm}^3$) as a function of $x$ is:
$$\begin{aligned}
V(x) &= x(30 - 2x)(40 - 2x) \\
&= x\left(1200 - 60x - 80x + 4x^2\right) \\
&= 4x^3 - 140x^2 + 1200x.
\end{aligned}$$

### Step 2: Determining the Physically Meaningful Domain
All three dimensions of the box must be strictly positive:
1. Height: $x > 0$.
2. Shorter base side: $30 - 2x > 0 \implies 2x < 30 \implies x < 15$.
3. Longer base side: $40 - 2x > 0 \implies 2x < 40 \implies x < 20$.

Intersecting $x > 0$, $x < 15$, and $x < 20$, the physically meaningful domain is restricted by the shorter side of the cardboard:
$$D_V = (0, 15)\quad [\text{cm}].$$

### Step 3: Finding the Value of $x$ That Maximizes the Volume
We differentiate $V(x) = 4x^3 - 140x^2 + 1200x$ with respect to $x$:
$$V'(x) = 12x^2 - 280x + 1200.$$
Setting $V'(x) = 0$ and dividing both sides by $4$:
$$3x^2 - 70x + 300 = 0.$$
Using the quadratic formula with $a = 3$, $b = -70$, $c = 300$:
$$\Delta = (-70)^2 - 4(3)(300) = 4900 - 3600 = 1300 = 100 \times 13 \implies \sqrt{\Delta} = 10\sqrt{13}.$$
Thus the roots of $V'(x) = 0$ are:
$$x = \frac{70 \pm 10\sqrt{13}}{6} = \frac{35 \pm 5\sqrt{13}}{3}.$$
Since $\sqrt{13} \approx 3.60555$, we evaluate both roots numerically to check which lies in the domain $D_V = (0, 15)$:
1. $x_1 = \frac{35 - 5\sqrt{13}}{3} \approx \frac{35 - 18.0278}{3} \approx 5.6574\text{ cm} \in (0, 15)$.
2. $x_2 = \frac{35 + 5\sqrt{13}}{3} \approx \frac{35 + 18.0278}{3} \approx 17.6759\text{ cm} \notin (0, 15)$ (rejected because $30 - 2x_2 < 0$).

### Step 4: Verifying That $x_1 = \frac{35 - 5\sqrt{13}}{3}$ Gives the Maximum Volume
- **First Derivative Sign Analysis on $(0, 15)$:**
  Since $V'(x) = 4(3x^2 - 70x + 300)$ is an upward-opening parabola with roots $x_1 \approx 5.66$ and $x_2 \approx 17.68$:
  - On $(0, x_1)$, $V'(x) > 0$, so $V(x)$ is strictly increasing.
  - On $(x_1, 15)$, $V'(x) < 0$, so $V(x)$ is strictly decreasing.
- **Second Derivative Check:**
  $$V''(x) = 24x - 280 \implies V''\left(\frac{35 - 5\sqrt{13}}{3}\right) = 8(35 - 5\sqrt{13}) - 280 = -40\sqrt{13} < 0.$$

Therefore, the volume is greatest for:
$$x_{\max} = \frac{35 - 5\sqrt{13}}{3}\text{ cm} \approx 5.66\text{ cm}.$$
The maximum volume is $V(x_{\max}) = \frac{35000 + 13000\sqrt{13}}{27}\text{ cm}^3 = \frac{1000(35 + 13\sqrt{13})}{27}\text{ cm}^3 \approx 3032.30\text{ cm}^3$.

---

## 4. Verification and Consistency Checks

- **Boundary Behavior:** At the endpoints of $[0, 15]$, $V(0) = 0$ (zero height) and $V(15) = 15(0)(10) = 0$ (zero width). Since $V(x) > 0$ on $(0, 15)$ and $V$ is continuous, Rolle's / Weierstrass's theorem guarantees an interior maximum on $(0, 15)$.
- **Numerical Comparison Near $x_{\max} \approx 5.657\text{ cm}$:**
  - $V(5) = 5(20)(30) = 3000\text{ cm}^3$,
  - $V(5.6574) \approx 5.6574 \times 18.6852 \times 28.6852 \approx 3032.30\text{ cm}^3$,
  - $V(6) = 6(18)(28) = 3024\text{ cm}^3$.
  Both $V(5)$ and $V(6)$ are smaller than $V(5.6574)$, confirming the local and global maximum.
