# Exercise 15: Comparing Directions Using the Cosine of the Angle

## 1. Problem Statement

Given
$$a=(1,2,1),\qquad b=(2,4,2),\qquad c=(2,0,3).$$
For each pair, compute
$$\frac{u\cdot v}{\|u\|\,\|v\|}.$$
Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths.

## 2. Theoretical Background and Concepts

1. **Cosine of the Angle Between Vectors:**
   For any two non-zero vectors $u, v \in \mathbb{R}^3$, the cosine of the angle $\theta \in [0, \pi]$ between them is:
   $$\cos\theta = \frac{u \cdot v}{\|u\|\,\|v\|} = \left(\frac{u}{\|u\|}\right) \cdot \left(\frac{v}{\|v\|}\right)$$
   Notice that $\frac{u \cdot v}{\|u\|\,\|v\|}$ is the dot product of the **normalized unit vectors** $\hat{u} = \frac{u}{\|u\|}$ and $\hat{v} = \frac{v}{\|v\|}$.

2. **Monotonicity of Cosine on $[0, \pi]$:**
   On the interval $\theta \in [0, \pi]$, the function $\cos\theta$ is **strictly decreasing** from $\cos(0) = 1$ down to $\cos(\pi) = -1$. Consequently, for angles $\theta_1, \theta_2 \in [0, \pi]$:
   $$\theta_1 \le \theta_2 \iff \cos\theta_1 \ge \cos\theta_2$$
   Smaller angles correspond to larger cosine values (closer to $1$).

## 3. Detailed Step-by-Step Solution

Given vectors:
$$a = (1, 2, 1), \qquad b = (2, 4, 2), \qquad c = (2, 0, 3)$$

### Step 1: Compute the norms of $a$, $b$, and $c$
$$\|a\| = \sqrt{1^2 + 2^2 + 1^2} = \sqrt{1 + 4 + 1} = \sqrt{6}$$
$$\|b\| = \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24} = 2\sqrt{6}$$
$$\|c\| = \sqrt{2^2 + 0^2 + 3^2} = \sqrt{4 + 0 + 9} = \sqrt{13}$$

### Step 2: Compute $\frac{u \cdot v}{\|u\|\,\|v\|}$ for each pair

1. **Pair $(a, b)$:**
   $$a \cdot b = (1)(2) + (2)(4) + (1)(2) = 2 + 8 + 2 = 12$$
   $$\cos\theta_{ab} = \frac{a \cdot b}{\|a\|\,\|b\|} = \frac{12}{\sqrt{6} \cdot 2\sqrt{6}} = \frac{12}{12} = 1$$
   Hence $\theta_{ab} = \arccos(1) = 0$.

2. **Pair $(a, c)$:**
   $$a \cdot c = (1)(2) + (2)(0) + (1)(3) = 2 + 0 + 3 = 5$$
   $$\cos\theta_{ac} = \frac{a \cdot c}{\|a\|\,\|c\|} = \frac{5}{\sqrt{6}\sqrt{13}} = \frac{5}{\sqrt{78}} \approx 0.5661$$
   Hence $\theta_{ac} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$.

3. **Pair $(b, c)$:**
   $$b \cdot c = (2)(2) + (4)(0) + (2)(3) = 4 + 0 + 6 = 10$$
   $$\cos\theta_{bc} = \frac{b \cdot c}{\|b\|\,\|c\|} = \frac{10}{2\sqrt{6}\sqrt{13}} = \frac{5}{\sqrt{78}} \approx 0.5661$$
   Hence $\theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$.

### Step 3: Order the pairs by increasing angle between the vectors
Since $1 > \frac{5}{\sqrt{78}}$ and $\cos\theta$ is strictly decreasing on $[0, \pi]$, we have:
$$\cos\theta_{ab} = 1 > \cos\theta_{ac} = \cos\theta_{bc} = \frac{5}{\sqrt{78}}$$
which gives the ordering by increasing angle:
$$\theta_{ab} = 0^\circ < \theta_{ac} = \theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 55.52^\circ$$
Thus, $(a, b)$ has the smallest angle ($0^\circ$), followed by $(a, c)$ and $(b, c)$ which are tied with the exact same angle ($\arccos\frac{5}{\sqrt{78}}$).

### Step 4: Explain why the value for $a$ and $b$ is $1$ despite different lengths
Notice that $b = (2, 4, 2) = 2(1, 2, 1) = 2a$, so $b$ is a positive scalar multiple of $a$: it points in the **exact same direction and orientation** as $a$, with twice the length ($\|b\| = 2\|a\|$).
When we compute $\frac{a \cdot b}{\|a\|\,\|b\|}$, dividing by the norms $\|a\|$ and $\|b\|$ **normalizes** both vectors before taking their dot product:
$$\frac{a \cdot b}{\|a\|\,\|b\|} = \frac{a \cdot (2a)}{\|a\| \cdot (2\|a\|)} = \frac{2\|a\|^2}{2\|a\|^2} = 1$$
The scaling factor $2$ in the numerator ($a \cdot (2a) = 2(a \cdot a)$) cancels out completely with the scaling factor $2$ in the denominator ($\|2a\| = 2\|a\|$). Because the cosine formula measures **pure direction** (it depends only on the unit vectors $\hat{a} = \hat{b} = \frac{1}{\sqrt{6}}(1,2,1)$), differences in length have no effect on $\cos\theta$. For the exact same reason, $\cos\theta_{ac} = \cos\theta_{bc} = \frac{5}{\sqrt{78}}$.

## 4. Verification and Consistency Checks

**Cauchy–Schwarz Inequality Check ($|u \cdot v| \le \|u\|\,\|v\|$):**
- For $(a, b)$: $|a \cdot b| = 12$ and $\|a\|\,\|b\| = \sqrt{6}\sqrt{24} = 12$. Equality holds in Cauchy–Schwarz if and only if one vector is a scalar multiple of the other, which matches $b = 2a$.
- For $(a, c)$ and $(b, c)$: $0 < \frac{5}{\sqrt{78}} = \sqrt{\frac{25}{78}} < 1$ since $25 < 78$, confirming that $\cos\theta_{ac} = \cos\theta_{bc} \in (0, 1)$ is a valid cosine of an acute angle.
