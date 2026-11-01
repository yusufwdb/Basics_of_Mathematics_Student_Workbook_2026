# Exercise 15: Complete Classification of a Line Relative to a Plane

## 1. Problem Statement

Let
$$L:p+tv,\qquad \Pi:n\cdot x=d.$$
State the conditions distinguishing the three cases: one intersection point, parallel with no common points, and the line contained in the plane. Then illustrate each case with your own simple numerical example.

## 2. Theoretical Background and Concepts

Let $L = \{p + t v : t \in \mathbb{R}\}$ be a line in $\mathbb{R}^3$ passing through a given point $p \in \mathbb{R}^3$ with non-zero direction vector $v \in \mathbb{R}^3 \setminus \{\mathbf{0}\}$, and let $\Pi = \{x \in \mathbb{R}^3 : n \cdot x = d\}$ be a plane with non-zero normal vector $n \in \mathbb{R}^3 \setminus \{\mathbf{0}\}$ and scalar $d \in \mathbb{R}$.

A point $x = p + t v \in L$ lies in $\Pi$ if and only if $t \in \mathbb{R}$ satisfies:
$$n \cdot (p + t v) = d$$
By bilinearity (distributivity) of the dot product, this equation rearranges to the fundamental scalar linear equation in $t$:
$$(n \cdot v)\, t = d - n \cdot p$$
This is a single linear equation of the form $A t = B$ where $A = n \cdot v$ and $B = d - n \cdot p$. A linear equation $At = B$ in one real variable $t$ has:
- **Exactly one solution** ($t = B/A$) if and only if $A \neq 0$,
- **No solutions** if and only if $A = 0$ and $B \neq 0$,
- **Infinitely many solutions** (all $t \in \mathbb{R}$) if and only if $A = 0$ and $B = 0$.

## 3. Detailed Step-by-Step Solution

### Part 1: General Algebraic and Geometric Conditions for the Three Cases

1. **Case 1: One Intersection Point ($L \cap \Pi = \{x^*\}$)**
   - **Condition:**
     $$n \cdot v \neq 0$$
     (Regardless of whether $n \cdot p = d$ or $n \cdot p \neq d$.)
   - **Geometric Meaning:** The direction vector $v$ of the line is **not orthogonal** to the normal vector $n$, so the line is not parallel to the plane. It pierces the plane at the unique parameter value:
     $$t^* = \frac{d - n \cdot p}{n \cdot v}, \qquad x^* = p + \left(\frac{d - n \cdot p}{n \cdot v}\right) v$$

2. **Case 2: Parallel with No Common Points ($L \parallel \Pi$ and $L \cap \Pi = \emptyset$)**
   - **Condition:**
     $$n \cdot v = 0 \quad \text{and} \quad n \cdot p \neq d$$
   - **Geometric Meaning:** Because $n \cdot v = 0$, the direction vector $v$ is perpendicular to the plane's normal vector $n$, meaning the line's direction is parallel to the plane. Because $n \cdot p \neq d$, the starting point $p$ does **not** lie on the plane. The equation $(n \cdot v)t = d - n \cdot p$ becomes $0 \cdot t = d - n \cdot p \neq 0$, which is a contradiction for all $t \in \mathbb{R}$.

3. **Case 3: Line Contained in the Plane ($L \subset \Pi$, so $L \cap \Pi = L$)**
   - **Condition:**
     $$n \cdot v = 0 \quad \text{and} \quad n \cdot p = d$$
   - **Geometric Meaning:** Because $n \cdot v = 0$, the line's direction is parallel to the plane, and because $n \cdot p = d$, the reference point $p$ already lies in the plane. The equation $(n \cdot v)t = d - n \cdot p$ becomes $0 \cdot t = 0$, which is satisfied for **every** $t \in \mathbb{R}$, so every point of $L$ lies in $\Pi$.

---

### Part 2: Simple Numerical Examples Illustrating Each Case

For clarity, let us fix the plane $\Pi$ to be the horizontal plane $z = 2$, i.e.:
$$\Pi: (0, 0, 1) \cdot (x, y, z) = 2 \qquad \big(n = (0, 0, 1),\; d = 2\big)$$

#### Example for Case 1 (One Intersection Point: $n \cdot v \neq 0$)
- Choose $p = (0, 0, 0)$ and $v = (1, 0, 1)$, so $L_1: (x, y, z) = (0, 0, 0) + t(1, 0, 1) = (t, 0, t)$.
- Check the condition:
  $$n \cdot v = (0, 0, 1) \cdot (1, 0, 1) = 1 \neq 0$$
- Substituting into $\Pi: z = 2$ gives $t = 2$, yielding the unique intersection point $x^* = (2, 0, 2)$.

#### Example for Case 2 (Parallel with No Common Points: $n \cdot v = 0$ and $n \cdot p \neq d$)
- Choose $p = (0, 0, 0)$ and $v = (1, 0, 0)$, so $L_2: (x, y, z) = (0, 0, 0) + t(1, 0, 0) = (t, 0, 0)$ (the $x$-axis).
- Check the conditions:
  $$n \cdot v = (0, 0, 1) \cdot (1, 0, 0) = 0, \qquad n \cdot p = (0, 0, 1) \cdot (0, 0, 0) = 0 \neq 2 = d$$
- Substituting into $\Pi: z = 2$ gives $0 = 2$ (no solution). The line $L_2$ stays at height $z = 0$ and never meets the plane $z = 2$.

#### Example for Case 3 (Line Contained in the Plane: $n \cdot v = 0$ and $n \cdot p = d$)
- Choose $p = (0, 0, 2)$ and $v = (1, 0, 0)$, so $L_3: (x, y, z) = (0, 0, 2) + t(1, 0, 0) = (t, 0, 2)$.
- Check the conditions:
  $$n \cdot v = (0, 0, 1) \cdot (1, 0, 0) = 0, \qquad n \cdot p = (0, 0, 1) \cdot (0, 0, 2) = 2 = d$$
- Substituting into $\Pi: z = 2$ gives $2 = 2$, which holds for all $t \in \mathbb{R}$. Every point $(t, 0, 2)$ lies in the plane $z = 2$.

## 4. Verification and Consistency Checks

Let us summarize and verify that our three conditions are **mutually exclusive and collectively exhaustive**:

| Case | Condition on $n \cdot v$ | Condition on $n \cdot p$ | Equation $(n \cdot v)t = d - n \cdot p$ | Solution Set for $t$ | Geometric Position |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | $n \cdot v \neq 0$ | Any ($= d$ or $\neq d$) | $At = B$ ($A \neq 0$) | $\{t^* = \frac{d - n \cdot p}{n \cdot v}\}$ | Intersects at $1$ point |
| **2** | $n \cdot v = 0$ | $n \cdot p \neq d$ | $0 \cdot t = B$ ($B \neq 0$) | $\emptyset$ | Strictly parallel ($L \cap \Pi = \emptyset$) |
| **3** | $n \cdot v = 0$ | $n \cdot p = d$ | $0 \cdot t = 0$ | $\mathbb{R}$ | Contained in plane ($L \subset \Pi$) |

Because by the law of trichotomy either $n \cdot v \neq 0$ or $n \cdot v = 0$, and within $n \cdot v = 0$ either $n \cdot p \neq d$ or $n \cdot p = d$, every possible line $L$ and plane $\Pi$ in $\mathbb{R}^3$ falls into one and only one of these three cases.
