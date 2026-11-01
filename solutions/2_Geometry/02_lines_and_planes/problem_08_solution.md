# Exercise 8: Intersection Point of a Line and a Plane

## 1. Problem Statement

Find the intersection point of
$$(x,y,z)=(1,0,2)+t(1,2,-1)$$
with the plane $x+y+z=4$. Check the result by substituting it into both descriptions.

## 2. Theoretical Background and Concepts

To find the intersection of a line $L$ given in parametric form:
$$(x, y, z) = (x_0 + t v_1,\, y_0 + t v_2,\, z_0 + t v_3), \qquad t \in \mathbb{R}$$
with a plane $\Pi$ given in Cartesian (general) form:
$$Ax + By + Cz = D$$
we substitute the parametric expressions $x(t), y(t), z(t)$ directly into the plane equation:
$$A(x_0 + t v_1) + B(y_0 + t v_2) + C(z_0 + t v_3) = D$$
Whenever $n \cdot v = A v_1 + B v_2 + C v_3 \neq 0$, this linear equation has a unique solution $t = t^*$. Substituting $t = t^*$ back into the parametric equation of $L$ gives the unique intersection point $Q = (x(t^*), y(t^*), z(t^*))$.

## 3. Detailed Step-by-Step Solution

Given:
- Line $L: (x, y, z) = (1, 0, 2) + t(1, 2, -1)$
- Plane $\Pi: x + y + z = 4$

### Step 1: Write the coordinates of a point on the line in terms of $t$
From the parametric equation of $L$, any point on the line has coordinates:
$$\begin{cases} x = 1 + t \\ y = 2t \\ z = 2 - t \end{cases} \quad (t \in \mathbb{R})$$

### Step 2: Substitute into the plane equation and solve for $t$
Substitute $x = 1 + t$, $y = 2t$, and $z = 2 - t$ into $x + y + z = 4$:
$$(1 + t) + 2t + (2 - t) = 4$$
Combine like terms on the left-hand side:
$$(1 + 2) + (t + 2t - t) = 4 \implies 3 + 2t = 4$$
Subtract $3$ from both sides and divide by $2$:
$$2t = 1 \implies t = \frac{1}{2}$$

### Step 3: Find the coordinates of the intersection point
Substitute $t = \frac{1}{2}$ back into the parametric equations of the line $L$:
$$\begin{aligned}
x &= 1 + \frac{1}{2} = \frac{3}{2} \\
y &= 0 + 2\left(\frac{1}{2}\right) = 1 \\
z &= 2 - \frac{1}{2} = \frac{3}{2}
\end{aligned}$$
Thus, the unique intersection point of the line and the plane is:
$$Q = \left(\frac{3}{2},\, 1,\, \frac{3}{2}\right) = (1.5,\, 1,\, 1.5)$$

## 4. Verification and Consistency Checks

1. **Check by substituting $Q = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$ into the plane equation $x + y + z = 4$:**
   $$x + y + z = \frac{3}{2} + 1 + \frac{3}{2} = 3 + 1 = 4 \quad \checkmark$$
   So $Q \in \Pi$.

2. **Check by substituting $Q = \left(\frac{3}{2}, 1, \frac{3}{2}\right)$ into the line description:**
   We check whether $Q - P_0$ is a scalar multiple of the direction vector $v = (1, 2, -1)$, where $P_0 = (1, 0, 2)$:
   $$Q - P_0 = \left(\frac{3}{2} - 1,\, 1 - 0,\, \frac{3}{2} - 2\right) = \left(\frac{1}{2},\, 1,\, -\frac{1}{2}\right) = \frac{1}{2}(1, 2, -1) = \frac{1}{2}v \quad \checkmark$$
   Indeed, $P_0 + \frac{1}{2}v = Q$, confirming that $Q$ lies on $L$ at $t = \frac{1}{2}$. Therefore, $Q = \left(\frac{3}{2}, 1, \frac{3}{2}\right) \in L \cap \Pi$.
