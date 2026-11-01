# Exercise 8: Linear Combination and Checking the Result

## 1. Problem Statement

Check whether $w=(5,1)$ can be written as
$$w=au+bv,$$
where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

## 2. Theoretical Background and Concepts

1. **Linear Combination in $\mathbb{R}^2$:**
   A vector $w \in \mathbb{R}^2$ is a linear combination of vectors $u, v \in \mathbb{R}^2$ if there exist scalars $a, b \in \mathbb{R}$ such that:
   $$w = au + bv$$
   Writing this equation in coordinates leads to a system of two linear equations in two unknowns $a$ and $b$.

2. **Basis and Spanning in $\mathbb{R}^2$:**
   Two vectors $u, v \in \mathbb{R}^2$ that are not parallel (i.e., linearly independent) form a **basis** of $\mathbb{R}^2$. Geometrically, their directions define an oblique coordinate grid covering the entire plane, meaning **every** vector $w \in \mathbb{R}^2$ can be uniquely decomposed as a sum of a vector along the direction of $u$ and a vector along the direction of $v$ (via the parallelogram law).

## 3. Detailed Step-by-Step Solution

Given vectors:
$$u = (1, 1), \qquad v = (2, -1), \qquad w = (5, 1)$$

### Step 1: Set up the system of equations for $w = au + bv$
Substitute the coordinates of $u$, $v$, and $w$:
$$(5, 1) = a(1, 1) + b(2, -1) = (a + 2b,\, a - b)$$
Equating the first and second coordinates gives the linear system:
$$\begin{cases} a + 2b = 5 & \text{(1)} \\ a - b = 1 & \text{(2)} \end{cases}$$

### Step 2: Solve for $a$ and $b$
Subtract equation (2) from equation (1) to eliminate $a$:
$$(a + 2b) - (a - b) = 5 - 1 \implies 3b = 4 \implies b = \frac{4}{3}$$
Substitute $b = \frac{4}{3}$ into equation (2):
$$a = 1 + b = 1 + \frac{4}{3} = \frac{7}{3}$$
Since a unique solution $(a, b) = \left(\frac{7}{3}, \frac{4}{3}\right)$ exists, $w$ **can** be written as $w = au + bv$.

### Step 3: Reconstruct $w$ from $a$ and $b$
Substitute $a = \frac{7}{3}$ and $b = \frac{4}{3}$ back into $au + bv$:
$$\frac{7}{3}u + \frac{4}{3}v = \frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = \left(\frac{7}{3},\, \frac{7}{3}\right) + \left(\frac{8}{3},\, -\frac{4}{3}\right) = \left(\frac{7+8}{3},\, \frac{7-4}{3}\right) = \left(\frac{15}{3},\, \frac{3}{3}\right) = (5, 1) = w$$

### Step 4: Explain the geometric meaning of the existence of such coefficients
Geometrically, $u = (1,1)$ and $v = (2,-1)$ point in two different (non-collinear) directions in the plane $\mathbb{R}^2$. Because their directions are not parallel, they span the entire $2$-dimensional plane ($\operatorname{span}\{u, v\} = \mathbb{R}^2$).
- The existence of $a = \frac{7}{3}$ and $b = \frac{4}{3}$ means that we can reach the point $w = (5,1)$ from the origin by moving $\frac{7}{3}$ units (in lengths of $u$) along the direction of $u$, and then $\frac{4}{3}$ units (in lengths of $v$) along the direction of $v$.
- Equivalently, $w$ is the diagonal of a parallelogram whose adjacent sides lie along the lines spanned by $u$ and $v$, namely the vectors $\frac{7}{3}u = \left(\frac{7}{3}, \frac{7}{3}\right)$ and $\frac{4}{3}v = \left(\frac{8}{3}, -\frac{4}{3}\right)$.

## 4. Verification and Consistency Checks

1. **Determinant / Basis Check:**
   The matrix whose columns are $u$ and $v$ is $M = \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix}$, with determinant:
   $$\det(M) = (1)(-1) - (2)(1) = -1 - 2 = -3 \neq 0$$
   By Cramer's rule:
   $$a = \frac{\det\begin{pmatrix} 5 & 2 \\ 1 & -1 \end{pmatrix}}{-3} = \frac{-5 - 2}{-3} = \frac{-7}{-3} = \frac{7}{3}, \qquad b = \frac{\det\begin{pmatrix} 1 & 5 \\ 1 & 1 \end{pmatrix}}{-3} = \frac{1 - 5}{-3} = \frac{-4}{-3} = \frac{4}{3}$$
   This independently confirms our values for $a$ and $b$.
