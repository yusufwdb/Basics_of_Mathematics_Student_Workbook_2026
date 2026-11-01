# Exercise 3: Ellipse

## 1. Problem Statement
For
$$\frac{x^2}{25}+\frac{y^2}{9}=1,$$
find the semiaxis lengths, the intercepts with the coordinate axes, and make a sketch. Explain along which axis the ellipse is more stretched and how this is visible in the equation.

## 2. Theoretical Background and Concepts
- **Canonical Equation of an Ellipse:** An ellipse centered at the origin $(0,0)$ with axes aligned along the coordinate axes has the equation:
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a > 0, \, b > 0).$$
- **Semiaxes and Intercepts:**
  - $a$ is the horizontal semiaxis length (along the $Ox$ axis), and the $x$-intercepts are $(\pm a, 0)$.
  - $b$ is the vertical semiaxis length (along the $Oy$ axis), and the $y$-intercepts are $(0, \pm b)$.
- **Stretching / Orientation:**
  - If $a > b$ (i.e., $a^2 > b^2$), the ellipse is stretched horizontally along the $x$-axis (major axis on $Ox$).
  - If $b > a$ (i.e., $b^2 > a^2$), the ellipse is stretched vertically along the $y$-axis (major axis on $Oy$).

## 3. Detailed Step-by-Step Solution

### Step 1: Find the semiaxis lengths
Comparing the given equation
$$\frac{x^2}{25} + \frac{y^2}{9} = 1$$
with the canonical form $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, we have:
$$a^2 = 25 \implies a = 5 \quad (\text{since } a > 0),$$
$$b^2 = 9 \implies b = 3 \quad (\text{since } b > 0).$$
Thus:
- The horizontal semiaxis length (semi-major axis) is $a = 5$.
- The vertical semiaxis length (semi-minor axis) is $b = 3$.

### Step 2: Find the intercepts with the coordinate axes
- **$x$-axis intercepts** (set $y = 0$):
  $$\frac{x^2}{25} + \frac{0^2}{9} = 1 \implies \frac{x^2}{25} = 1 \implies x^2 = 25 \implies x = \pm 5.$$
  The $x$-intercepts (major vertices) are $(-5, 0)$ and $(5, 0)$.

- **$y$-axis intercepts** (set $x = 0$):
  $$\frac{0^2}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = 1 \implies y^2 = 9 \implies y = \pm 3.$$
  The $y$-intercepts (minor vertices) are $(0, -3)$ and $(0, 3)$.

### Step 3: Explain the stretching direction
The ellipse is **more stretched along the $x$-axis** (horizontally).
- **How this is visible in the equation:** The denominator under $x^2$ is $25$, which is larger than the denominator $9$ under $y^2$ ($25 > 9$, so $a = 5 > b = 3$). Because $\frac{x^2}{a^2} \le 1$, a larger denominator $a^2$ allows $x$ to reach larger absolute values ($|x| \le 5$) before $\frac{x^2}{25}$ reaches $1$, whereas $y$ can only reach $|y| \le 3$.

### Step 4: Sketch of the ellipse
```text
               y
               ^
               | (0,3)
         . - - + - - .
      /        |        \
-----+---------+---------+-----> x
  (-5,0)     (0,0)     (5,0)
      \        |        /
         ' - - + - - '
               | (0,-3)
```

## 4. Verification and Consistency Checks
1. **Boundary check:** Since $\frac{y^2}{9} = 1 - \frac{x^2}{25} \ge 0$, real values of $y$ exist if and only if $x^2 \le 25 \iff x \in [-5, 5]$. Similarly, $y \in [-3, 3]$. This confirms the horizontal span has length $2a = 10$ and the vertical span has length $2b = 6$.
2. **Test point check:** Consider $x = 4 \in [-5, 5]$. Substituting into the equation gives:
   $$\frac{16}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = \frac{9}{25} \implies y^2 = \frac{81}{25} \implies y = \pm \frac{9}{5} = \pm 1.8.$$
   Indeed, $|1.8| < 3$, and substituting $(4, 1.8)$ back yields $\frac{16}{25} + \frac{3.24}{9} = 0.64 + 0.36 = 1$.
