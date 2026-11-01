# Exercise 7: A Trigonometric Function

## 1. Problem Statement
On $[0,2\pi]$, find the intervals of monotonicity and the extrema of
$$f(x)=\sin x+\cos x.$$
Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

---

## 2. Theoretical Background and Concepts
- **Extrema on a Closed Bounded Interval (Extreme Value Theorem):** A continuous function $f$ on a compact interval $[a, b]$ attains both a global (absolute) maximum and a global (absolute) minimum on $[a, b]$. These extrema can occur either at:
  1. **Interior critical points** $x \in (a, b)$ where $f'(x) = 0$, or
  2. **Boundary endpoints** $x = a$ and $x = b$.
- **Auxiliary Angle Identity:** Any linear combination $\sin x \pm \cos x$ can be written as a single shifted sinusoid:
  $$\sin x + \cos x = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right), \qquad \cos x - \sin x = \sqrt{2}\cos\left(x + \frac{\pi}{4}\right)$$

---

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the derivative and find the critical points in $(0, 2\pi)$
Differentiating $f(x) = \sin x + \cos x$:
$$f'(x) = \cos x - \sin x$$
Setting $f'(x) = 0$ on $[0, 2\pi]$:
$$\cos x - \sin x = 0 \iff \sin x = \cos x \iff \tan x = 1$$
(Note that $\cos x = 0$ does not satisfy $\sin x = \cos x$, since $\sin x = \pm 1$ when $\cos x = 0$.)
On the interval $[0, 2\pi]$, the equation $\tan x = 1$ has two solutions:
$$x_1 = \frac{\pi}{4} \in \left(0, \frac{\pi}{2}\right) \qquad \text{and} \qquad x_2 = \frac{\pi}{4} + \pi = \frac{5\pi}{4} \in \left(\pi, \frac{3\pi}{2}\right)$$

### Step 2: Determine the sign of $f'(x)$ and intervals of monotonicity on $[0, 2\pi]$
The critical points $x_1 = \frac{\pi}{4}$ and $x_2 = \frac{5\pi}{4}$ divide $[0, 2\pi]$ into three subintervals:
1. **On $\left[0, \frac{\pi}{4}\right)$:** Choose test point $x = 0$: $f'(0) = \cos 0 - \sin 0 = 1 > 0$. Thus $f'(x) > 0$ on $\left[0, \frac{\pi}{4}\right)$, and $f$ is **strictly increasing** on $\left[0, \frac{\pi}{4}\right]$.
2. **On $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$:** Choose test point $x = \frac{\pi}{2}$: $f'\left(\frac{\pi}{2}\right) = \cos\frac{\pi}{2} - \sin\frac{\pi}{2} = -1 < 0$. Thus $f'(x) < 0$ on $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$, and $f$ is **strictly decreasing** on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
3. **On $\left(\frac{5\pi}{4}, 2\pi\right]$:** Choose test point $x = 2\pi$: $f'(2\pi) = \cos(2\pi) - \sin(2\pi) = 1 > 0$. Thus $f'(x) > 0$ on $\left(\frac{5\pi}{4}, 2\pi\right]$, and $f$ is **strictly increasing** on $\left[\frac{5\pi}{4}, 2\pi\right]$.

| Point / Interval | $x = 0$ | $\left(0, \frac{\pi}{4}\right)$ | $x = \frac{\pi}{4}$ | $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$ | $x = \frac{5\pi}{4}$ | $\left(\frac{5\pi}{4}, 2\pi\right)$ | $x = 2\pi$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Sign of $f'(x)$** | $+1$ | $+$ | $0$ | $-$ | $0$ | $+$ | $+1$ |
| **$f(x)$** | $1$ | $\nearrow$ | $\sqrt{2}$ | $\searrow$ | $-\sqrt{2}$ | $\nearrow$ | $1$ |
| **Classification** | Endpoint (Local Min) | Increasing | **Global Max** | Decreasing | **Global Min** | Increasing | Endpoint (Local Max) |

### Step 3: Evaluate and compare $f(x)$ at the critical points and endpoints
1. **Left endpoint $x = 0$:**
   $$f(0) = \sin 0 + \cos 0 = 0 + 1 = 1$$
2. **First critical point $x = \frac{\pi}{4}$:**
   $$f\left(\frac{\pi}{4}\right) = \sin\frac{\pi}{4} + \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} \approx 1.414$$
3. **Second critical point $x = \frac{5\pi}{4}$:**
   $$f\left(\frac{5\pi}{4}\right) = \sin\frac{5\pi}{4} + \cos\frac{5\pi}{4} = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} \approx -1.414$$
4. **Right endpoint $x = 2\pi$:**
   $$f(2\pi) = \sin(2\pi) + \cos(2\pi) = 0 + 1 = 1$$

**Comparison and Summary of Extrema:**
Ordering the values gives $-\sqrt{2} < 1 < \sqrt{2}$:
- **Interior Local and Global Maximum:** $f\left(\frac{\pi}{4}\right) = \sqrt{2}$ at $x = \frac{\pi}{4}$.
- **Interior Local and Global Minimum:** $f\left(\frac{5\pi}{4}\right) = -\sqrt{2}$ at $x = \frac{5\pi}{4}$.
- **Endpoint Values:** At both endpoints $x = 0$ and $x = 2\pi$, $f(0) = f(2\pi) = 1$, which lies strictly between the interior global minimum $-\sqrt{2}$ and global maximum $\sqrt{2}$. (Viewed restricted to $[0, 2\pi]$, $x = 0$ is a boundary local minimum since $f$ increases to its right, and $x = 2\pi$ is a boundary local maximum since $f$ increases up to it from the left.)

---

## 4. Verification and Consistency Checks

### Verification via the Auxiliary Angle Identity
Using $\sin\frac{\pi}{4} = \cos\frac{\pi}{4} = \frac{1}{\sqrt{2}}$, we can rewrite $f(x)$ as:
$$f(x) = \sqrt{2}\left(\sin x \cos\frac{\pi}{4} + \cos x \sin\frac{\pi}{4}\right) = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)$$
Since $\sin\theta$ has amplitude $1$, attains its maximum $+1$ at $\theta = \frac{\pi}{2}$, and attains its minimum $-1$ at $\theta = \frac{3\pi}{2}$:
- Maximum of $f(x)$ is $\sqrt{2}(+1) = \sqrt{2}$ when $x + \frac{\pi}{4} = \frac{\pi}{2} \iff x = \frac{\pi}{4}$.
- Minimum of $f(x)$ is $\sqrt{2}(-1) = -\sqrt{2}$ when $x + \frac{\pi}{4} = \frac{3\pi}{2} \iff x = \frac{5\pi}{4}$.
This confirms both the locations and exact values of the extrema.
