# Exercise 11: Plane Containing a Line and a Point

## 1. Problem Statement

Find the equation of the plane containing
$$(x,y,z)=(1,0,2)+t(1,1,-1)$$
and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain.

## 2. Theoretical Background and Concepts

1. **Plane Determined by a Line and an External Point:**
   Let $L: A + t v$ ($t \in \mathbb{R}$) be a line passing through $A$ with direction vector $v \neq \mathbf{0}$, and let $P \notin L$ be a point not on $L$. There is a unique plane $\Pi$ containing both $L$ and $P$:
   - First, the direction vector $v$ of the line $L$ lies in $\Pi$.
   - Second, since both $A \in L \subset \Pi$ and $P \in \Pi$, the displacement vector $w = \overrightarrow{AP} = P - A$ also lies in $\Pi$.
   - Because $P \notin L$, the vectors $v$ and $w$ are linearly independent and span the direction space of $\Pi$.
   - Therefore, their cross product $n = v \times w = v \times \overrightarrow{AP} \neq \mathbf{0}$ is a **normal vector** to the plane $\Pi$, and the equation of $\Pi$ is $n \cdot ((x, y, z) - A) = 0$.

## 3. Detailed Step-by-Step Solution

Given:
- Line $L: (x, y, z) = (1, 0, 2) + t(1, 1, -1)$, with reference point $A = (1, 0, 2)$ and direction vector $v = (1, 1, -1)$.
- Point $P = (0, 2, 1)$.

### Step 1: Construct two linearly independent vectors lying in the plane
1. The first vector in the plane is the direction vector of the line $L$:
   $$v = (1, 1, -1)$$
2. The second vector in the plane is the displacement vector from $A = (1, 0, 2)$ on the line to $P = (0, 2, 1)$:
   $$w = \overrightarrow{AP} = P - A = (0 - 1,\, 2 - 0,\, 1 - 2) = (-1, 2, -1)$$

### Step 2: Find a normal vector $n$ to the plane using the cross product
Compute $n = v \times w$:
$$n = v \times \overrightarrow{AP} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & -1 \\ -1 & 2 & -1 \end{vmatrix}$$
Expanding by cofactors along the first row:
- First component ($x$): $(1)(-1) - (-1)(2) = -1 + 2 = 1$
- Second component ($y$): $-\big((1)(-1) - (-1)(-1)\big) = -(-1 - 1) = 2$
- Third component ($z$): $(1)(2) - (1)(-1) = 2 + 1 = 3$

Thus, a normal vector to the plane is:
$$n = (1, 2, 3)$$

### Step 3: Write the equation of the plane
Using the normal vector $n = (1, 2, 3)$ and the point $A = (1, 0, 2)$:
$$1(x - 1) + 2(y - 0) + 3(z - 2) = 0$$
Expand and simplify:
$$x - 1 + 2y + 3z - 6 = 0 \implies x + 2y + 3z = 7 \quad (\text{or } x + 2y + 3z - 7 = 0)$$

## 4. Verification and Consistency Checks

1. **Check that the point $P = (0, 2, 1)$ lies in the plane $x + 2y + 3z = 7$:**
   Substitute $x = 0, y = 2, z = 1$ into the left-hand side:
   $$0 + 2(2) + 3(1) = 0 + 4 + 3 = 7 \quad \checkmark$$

2. **Check that the entire line $L: (x, y, z) = (1 + t,\, t,\, 2 - t)$ lies in the plane $x + 2y + 3z = 7$:**
   Substitute the parametric coordinates $x = 1 + t$, $y = t$, and $z = 2 - t$ into the left-hand side for an arbitrary $t \in \mathbb{R}$:
   $$x + 2y + 3z = (1 + t) + 2(t) + 3(2 - t) = 1 + t + 2t + 6 - 3t = 7 + (1 + 2 - 3)t = 7 + 0t = 7 \quad \forall t \in \mathbb{R} \quad \checkmark$$
   Because the equation holds identically for every $t \in \mathbb{R}$, the entire line $L$ (as well as the point $P$) is contained in the plane $x + 2y + 3z = 7$.
