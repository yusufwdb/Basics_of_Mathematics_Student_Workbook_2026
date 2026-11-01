# Exercise 10: A Cable Through Water and Land

## 1. Problem Statement

Point $A$ lies on one bank of a river of width $100$ m, and point $B$ lies on the other bank, $500$ m along the bank from the point directly opposite $A$.

The cost per meter of cable underwater is twice the cost per meter of cable on land.

Build a cost function depending on the point where the cable comes out of the water, determine the domain, and find the solution that minimizes the cost.

---

## 2. Theoretical Background and Concepts

- **Pythagorean Theorem and Weighted Distance Optimization (Snell's Law Analogue):**
  When connecting two points across two media with different unit costs $c_1$ and $c_2$, the total cost is $C = c_1 L_{\text{water}} + c_2 L_{\text{land}}$, where the underwater path length $L_{\text{water}} = \sqrt{w^2 + x^2}$ is found by the Pythagorean theorem.
- **Optimization on a Closed Bounded Interval $[a, b]$:**
  By the Extreme Value (Weierstrass) Theorem, a continuous function $C(x)$ on a closed interval $[a, b]$ attains its global minimum either at an interior critical point where $C'(x) = 0$ or at one of the boundary endpoints $x = a$ or $x = b$.

---

## 3. Detailed Step-by-Step Solution

### Step 1: Geometric Setup and Building the Cost Function
Let $O$ be the point on the opposite bank directly across from $A$, so that $AO \perp OB$, $|AO| = 100\text{ m}$ (river width), and $|OB| = 500\text{ m}$ (distance along the bank).
Let $P$ be the point on the segment $OB$ where the cable emerges from the water onto the land, and let
$$x = |OP|\quad [\text{m}]$$
be the distance along the bank from $O$ to $P$.

```
    O -------- x -------- P ------------- (500 - x) ------------- B   (Opposite bank)
    |                    /
100 |   sqrt(100^2+x^2) /
    |                  /
    A ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   (Starting bank)
```

- **Underwater cable length $|AP|$:** By the Pythagorean theorem in right triangle $\triangle AOP$,
  $$L_{\text{water}}(x) = \sqrt{100^2 + x^2} = \sqrt{10\,000 + x^2}\quad [\text{m}].$$
- **Overland cable length $|PB|$:**
  $$L_{\text{land}}(x) = 500 - x\quad [\text{m}].$$
- **Cost Function:** Let $k > 0$ denote the cost per meter of cable on land (in currency units per meter). Then the cost per meter underwater is $2k$. The total cost $C(x)$ is:
  $$C(x) = 2k\sqrt{10\,000 + x^2} + k(500 - x) = k\left(2\sqrt{10\,000 + x^2} + 500 - x\right).$$

### Step 2: Determining the Domain
Geometrically, the landing point $P$ should lie on the segment $OB$ between $O$ ($x = 0$, going straight across the river) and $B$ ($x = 500$, going diagonally all the way underwater to $B$). Thus, the natural domain is the closed interval:
$$D_C = [0, 500]\quad [\text{m}].$$
*(Note: Any $x < 0$ or $x > 500$ would strictly increase both or one of the segment lengths unnecessarily.)*

### Step 3: Finding the Critical Point and Minimizing the Cost
We differentiate $C(x)$ with respect to $x$ on $(0, 500)$:
$$\begin{aligned}
C'(x) &= k\left(2 \cdot \frac{2x}{2\sqrt{10\,000 + x^2}} - 1\right) \\
&= k\left(\frac{2x}{\sqrt{10\,000 + x^2}} - 1\right).
\end{aligned}$$
Setting $C'(x) = 0$ (since $k > 0$):
$$\frac{2x}{\sqrt{10\,000 + x^2}} = 1 \implies 2x = \sqrt{10\,000 + x^2}.$$
Since $\sqrt{10\,000 + x^2} > 0$, this requires $x > 0$. Squaring both sides gives:
$$4x^2 = 10\,000 + x^2 \implies 3x^2 = 10\,000 \implies x^2 = \frac{10\,000}{3}.$$
Taking the positive square root:
$$x^* = \frac{100}{\sqrt{3}} = \frac{100\sqrt{3}}{3}\text{ m} \approx 57.74\text{ m} \in [0, 500].$$

### Step 4: Justification of the Global Minimum
- For $x \in [0, x^*)$, $2x < \sqrt{10\,000 + x^2} \implies C'(x) < 0$, so $C(x)$ is strictly decreasing.
- For $x \in (x^*, 500]$, $2x > \sqrt{10\,000 + x^2} \implies C'(x) > 0$, so $C(x)$ is strictly increasing.
- Also, $C''(x) = \frac{20\,000k}{(10\,000+x^2)^{3/2}} > 0$ for all $x \in [0, 500]$.

Thus, the cost is minimized when the cable comes out of the water at:
$$x^* = \frac{100\sqrt{3}}{3}\text{ m} \approx 57.74\text{ m}$$
downstream from the point $O$ directly opposite $A$ (and $500 - \frac{100\sqrt{3}}{3} \approx 442.26\text{ m}$ from $B$).

---

## 4. Verification and Consistency Checks

Let us compare the exact and numerical values of the cost at the critical point $x^* = \frac{100}{\sqrt{3}}$ with the two boundary strategies $x = 0$ and $x = 500$:
1. **Optimal strategy ($x^* = \frac{100}{\sqrt{3}} \approx 57.74\text{ m}$):**
   Since $\sqrt{10\,000 + (x^*)^2} = \sqrt{10\,000 + \frac{10\,000}{3}} = \frac{200}{\sqrt{3}}$, the minimum cost is:
   $$C(x^*) = k\left(2\cdot\frac{200}{\sqrt{3}} + 500 - \frac{100}{\sqrt{3}}\right) = k\left(500 + \frac{300}{\sqrt{3}}\right) = k\left(500 + 100\sqrt{3}\right) \approx 673.21k.$$
2. **Boundary $x = 0$ (straight across the river, then $500\text{ m}$ on land):**
   $$C(0) = k\left(2\sqrt{10\,000} + 500\right) = k(200 + 500) = 700k > 673.21k.$$
3. **Boundary $x = 500$ (straight line diagonally underwater from $A$ to $B$):**
   $$C(500) = k\left(2\sqrt{10\,000 + 250\,000} + 0\right) = 200\sqrt{26}\,k \approx 1019.80k > 673.21k.$$
4. **Trigonometric Check (Snell's Law):** The angle $\theta$ between $AP$ and the normal $AO$ satisfies $\sin\theta = \frac{x^*}{\sqrt{100^2+(x^*)^2}} = \frac{1}{2} = \frac{c_{\text{land}}}{c_{\text{water}}}$, i.e., $\theta = 30^\circ$, which is the classic refraction/Snell's law condition for minimum cost!
