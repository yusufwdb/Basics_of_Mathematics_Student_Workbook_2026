# Exercise 8: Number of Requests Handled by a Server

## 1. Problem Statement

The rate at which requests arrive at a server during the first 5 minutes is described by the function
$$r(t)=100+20t\quad [\text{requests/min}],\qquad 0\le t\le5.$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

---

## 2. Theoretical Background and Concepts

- **Accumulation of a Varying Rate:**
  If $r(t)$ represents the instantaneous rate at which a quantity arrives or accumulates (here in $\text{requests/min}$), then the total amount $N_{\text{total}}$ accumulated over the time interval $[a, b]$ is given by the definite integral of the rate function:
  $$N_{\text{total}} = \int_a^b r(t)\,dt.$$
  Notice the dimensional consistency: $[\text{requests/min}] \times [\text{min}] = [\text{requests}]$.
- **Average Value of a Rate Function on $[a,b]$:**
  $$r_{\text{avg}} = \frac{1}{b - a}\int_a^b r(t)\,dt = \frac{N_{\text{total}}}{b - a}.$$

---

## 3. Detailed Step-by-Step Solution

### Part 1: Computing the Total Number of Requests in $[0, 5]$
Integrating the arrival rate $r(t) = 100 + 20t$ from $t = 0$ to $t = 5$ minutes:
$$\begin{aligned}
N_{\text{total}} &= \int_0^5 (100 + 20t)\,dt \\
&= \left[100t + 10t^2\right]_0^5 \\
&= \left(100(5) + 10(5)^2\right) - \left(100(0) + 10(0)^2\right) \\
&= 500 + 250 = 750\text{ requests}.
\end{aligned}$$

### Part 2: Computing the Average Rate of Incoming Requests Over $[0, 5]$
Dividing the total number of requests $N_{\text{total}} = 750$ by the length of the time interval $5 - 0 = 5\text{ minutes}$:
$$r_{\text{avg}} = \frac{1}{5 - 0}\int_0^5 r(t)\,dt = \frac{750\text{ requests}}{5\text{ min}} = 150\text{ requests/min}.$$

### Part 3: Comparing the Average Rate with $r(0)$ and $r(5)$
We evaluate the rate at the endpoints of the interval $[0, 5]$:
- At $t = 0$: $r(0) = 100 + 20(0) = 100\text{ requests/min}$.
- At $t = 5$: $r(5) = 100 + 20(5) = 200\text{ requests/min}$.

Computing the arithmetic mean of the initial and final rates gives:
$$\frac{r(0) + r(5)}{2} = \frac{100 + 200}{2} = 150\text{ requests/min} = r_{\text{avg}}.$$
**Comparison and Explanation:** Because $r(t) = 100 + 20t$ is a **linear function** of time $t$, its graph is a straight line segment. Consequently, its integral average value $r_{\text{avg}} = 150\text{ requests/min}$ over $[0, 5]$ is equal to the **exact arithmetic mean of its endpoint values** $r(0) = 100$ and $r(5) = 200$, and is attained exactly at the midpoint of the time interval, $t = 2.5\text{ min}$ ($r(2.5) = 100 + 20(2.5) = 150$).

---

## 4. Verification and Consistency Checks

### Geometric Trapezoid Area Check
The region under the line $r(t) = 100 + 20t$ on $[0, 5]$ is a right trapezoid with parallel vertical bases $b_1 = r(0) = 100$ and $b_2 = r(5) = 200$, and horizontal width $h = 5$:
$$\text{Area} = \frac{b_1 + b_2}{2} \cdot h = \frac{100 + 200}{2} \times 5 = 150 \times 5 = 750\text{ requests}.$$
This matches the integral calculation identically.
