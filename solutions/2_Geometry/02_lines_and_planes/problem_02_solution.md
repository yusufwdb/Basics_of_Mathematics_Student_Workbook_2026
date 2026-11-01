# Exercise 2: A Line in Space

## 1. Problem Statement

Given
$$L:(x,y,z)=(2,-1,3)+t(1,2,-2).$$
State a point on the line and its direction vector, check whether $P=(4,3,-1)$ lies on $L$, and find the point corresponding to $t=-1$.

## 2. Theoretical Background and Concepts

1. **Vector / Parametric Equation of a Line in $\mathbb{R}^3$:**
   A line $L$ in three-dimensional space is described in parametric vector form as:
   $$(x, y, z) = p_0 + t v, \qquad t \in \mathbb{R}$$
   where:
   - $p_0 = (x_0, y_0, z_0)$ is a fixed **initial (reference) point** on the line (corresponding to $t = 0$),
   - $v = (v_1, v_2, v_3) \neq \mathbf{0}$ is a **direction vector** of the line,
   - $t \in \mathbb{R}$ is the real parameter specifying how many multiples of $v$ we move away from $p_0$.

2. **Point Membership Test:**
   A point $P = (x_P, y_P, z_P)$ lies on $L$ if and only if there exists a **single, consistent** real parameter $t \in \mathbb{R}$ that simultaneously satisfies all three coordinate equations:
   $$\begin{cases} x_P = x_0 + t v_1 \\ y_P = y_0 + t v_2 \\ z_P = z_0 + t v_3 \end{cases}$$

## 3. Detailed Step-by-Step Solution

Given line:
$$L: (x, y, z) = (2, -1, 3) + t(1, 2, -2), \qquad t \in \mathbb{R}$$

### Part 1: State a point on the line and its direction vector
Directly from the parametric representation $p_0 + tv$:
- **A point on the line (for $t = 0$):** $P_0 = (2, -1, 3)$
- **Direction vector of the line:** $v = (1, 2, -2)$

### Part 2: Check whether $P = (4, 3, -1)$ lies on $L$
Substitute $(x, y, z) = (4, 3, -1)$ into the parametric equations of $L$:
$$\begin{cases} 2 + t = 4 & \text{(1)} \\ -1 + 2t = 3 & \text{(2)} \\ 3 - 2t = -1 & \text{(3)} \end{cases}$$
Solve each equation for $t$:
- From (1): $t = 4 - 2 = 2$
- From (2): $2t = 3 + 1 = 4 \implies t = 2$
- From (3): $-2t = -1 - 3 = -4 \implies t = 2$

Because all three coordinate equations yield the **exact same parameter value** $t = 2$, the point $P = (4, 3, -1)$ **does lie on the line $L$**.

### Part 3: Find the point corresponding to $t = -1$
Substitute $t = -1$ into the equation of $L$:
$$(x, y, z) = (2, -1, 3) + (-1)(1, 2, -2) = (2 - 1,\, -1 - 2,\, 3 - (-2)) = (1, -3, 5)$$
Thus, the point on $L$ corresponding to $t = -1$ is:
$$Q = (1, -3, 5)$$

## 4. Verification and Consistency Checks

1. **Collinearity Check for $P_0 = (2, -1, 3)$, $P = (4, 3, -1)$, and $Q = (1, -3, 5)$:**
   - The displacement from $P_0$ to $P$ is:
     $$\overrightarrow{P_0 P} = P - P_0 = (4 - 2,\, 3 - (-1),\, -1 - 3) = (2, 4, -4) = 2(1, 2, -2) = 2v \quad \checkmark$$
   - The displacement from $P_0$ to $Q$ is:
     $$\overrightarrow{P_0 Q} = Q - P_0 = (1 - 2,\, -3 - (-1),\, 5 - 3) = (-1, -2, 2) = -1(1, 2, -2) = -v \quad \checkmark$$
   Both displacement vectors are exact scalar multiples of the direction vector $v = (1, 2, -2)$, confirming that $P$ and $Q$ lie on $L$ at $t=2$ and $t=-1$ respectively.
