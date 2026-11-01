# Exercise 7: Exponential Growth

## 1. Problem Statement

Assume the model
$$N(t)=N_0e^{kt},\qquad k>0.$$

1. Verify by differentiation that the model satisfies the relation $N'(t)=kN(t)$.
2. Find the population doubling time.
3. Explain why the doubling time does not depend on $N_0$.

---

## 2. Theoretical Background and Concepts

- **Law of Natural (Exponential) Growth:**
  A quantity $N(t)$ grows exponentially when its instantaneous rate of change $N'(t)$ at any time $t$ is directly proportional to its current size $N(t)$:
  $$N'(t) = k N(t), \quad k > 0,$$
  where $k$ is the relative (per-capita) growth rate and $N_0 = N(0) > 0$ is the initial population size at $t = 0$.
- **Chain Rule for Exponential Functions:**
  $$\frac{d}{dt}\left(e^{kt}\right) = k e^{kt}.$$
- **Doubling Time ($T_d$):** The time interval $T_d$ required for the population to double from its initial value $N_0$ to $2N_0$ (or from any current value $N(t)$ to $2N(t)$).

---

## 3. Detailed Step-by-Step Solution

### Part 1: Verifying That $N'(t) = kN(t)$ by Differentiation
Given $N(t) = N_0 e^{kt}$ where $N_0$ and $k > 0$ are constants, we differentiate with respect to $t$ using linearity and the chain rule:
$$\begin{aligned}
N'(t) &= \frac{d}{dt}\left(N_0 e^{kt}\right) \\
&= N_0 \frac{d}{dt}\left(e^{kt}\right) \\
&= N_0 \left(e^{kt} \cdot \frac{d}{dt}(kt)\right) \\
&= N_0 k e^{kt} \\
&= k \left(N_0 e^{kt}\right) \\
&= k N(t).
\end{aligned}$$
This confirms that $N(t) = N_0 e^{kt}$ satisfies the differential equation $N'(t) = k N(t)$ for all $t \in \mathbb{R}$.

### Part 2: Finding the Population Doubling Time $T_d$
The doubling time $T_d$ is the time at which the population reaches twice its initial size, $N(T_d) = 2N_0$ (assuming $N_0 > 0$):
$$N_0 e^{k T_d} = 2 N_0.$$
Dividing both sides by the non-zero initial population $N_0$:
$$e^{k T_d} = 2.$$
Taking the natural logarithm $\ln$ of both sides:
$$\ln\left(e^{k T_d}\right) = \ln 2 \implies k T_d = \ln 2.$$
Solving for $T_d$ (since $k > 0$):
$$T_d = \frac{\ln 2}{k} \approx \frac{0.6931}{k}.$$

### Part 3: Explaining Why the Doubling Time Does Not Depend on $N_0$
- **Algebraic explanation:** In the equation $N_0 e^{k T_d} = 2N_0$, the initial population $N_0$ appears as a linear scaling factor on both sides and cancels out upon division, leaving $e^{k T_d} = 2$, which depends only on the relative growth rate $k$.
- **Physical/biological explanation:** Because the absolute growth rate $N'(t) = k N(t)$ scales in direct proportion to the current population size, a population that is twice as large grows twice as fast in absolute terms (e.g., twice as many organisms reproducing at the same per-capita rate $k$), and also needs to gain twice as many individuals to double. The larger absolute gain required and the faster absolute growth rate cancel each other out, so the **relative growth factor** over any time span $\Delta t$ is $\frac{N(t + \Delta t)}{N(t)} = e^{k\Delta t}$, independent of the starting size.

---

## 4. Verification and Consistency Checks

Let us check that starting from **any** time $t$ and advancing by $T_d = \frac{\ln 2}{k}$ doubles the population $N(t)$:
$$\begin{aligned}
N(t + T_d) &= N_0 e^{k\left(t + \frac{\ln 2}{k}\right)} \\
&= N_0 e^{kt + \ln 2} \\
&= N_0 e^{kt} \cdot e^{\ln 2} \\
&= 2 N_0 e^{kt} = 2 N(t).
\end{aligned}$$
This confirms that $T_d = \frac{\ln 2}{k}$ is the universal doubling time at any point along the trajectory, regardless of $N_0$ or $t$.
