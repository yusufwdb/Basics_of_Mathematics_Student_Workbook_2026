# Exercise 10: A Polynomial Through Three Points

## 1. Problem Statement
Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

## 2. Theoretical Background and Concepts
A point $(x_0, y_0)$ lies on the graph of the quadratic polynomial $p(x) = ax^2 + bx + c$ if and only if
$$p(x_0) = a x_0^2 + b x_0 + c = y_0.$$
Although $p(x)$ is nonlinear in $x$, once a specific $x$-coordinate $x_0$ is substituted, $x_0^2$ and $x_0$ become known numerical constants, and the equation $x_0^2 a + x_0 b + 1\cdot c = y_0$ is **linear in the unknown coefficients $a, b, c$**.

Given three points $(x_1, y_1), (x_2, y_2), (x_3, y_3)$ with distinct $x$-coordinates ($x_1, x_2, x_3$ pairwise distinct), this yields a $3 \times 3$ linear system (with a Vandermonde coefficient matrix) that always has a unique solution $(a, b, c)$.

## 3. Detailed Step-by-Step Solution

### Step 1: Reduce the interpolation conditions to a linear system in $a, b, c$
Substitute each of the three given points $(x_i, y_i)$ into $p(x) = ax^2 + bx + c = y$:
1. **Point $(0, 1)$ ($x = 0, p(0) = 1$):**
   $$a(0)^2 + b(0) + c = 1 \implies 0a + 0b + c = 1 \implies c = 1.$$
2. **Point $(1, 3)$ ($x = 1, p(1) = 3$):**
   $$a(1)^2 + b(1) + c = 3 \implies a + b + c = 3.$$
3. **Point $(2, 9)$ ($x = 2, p(2) = 9$):**
   $$a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9.$$

This gives the $3 \times 3$ linear system for the unknown coefficients $(a, b, c)$:
$$\begin{cases}
c = 1, \\
a + b + c = 3, \\
4a + 2b + c = 9,
\end{cases} \quad \text{or in matrix form } \begin{pmatrix}0&0&1\\1&1&1\\4&2&1\end{pmatrix}\begin{pmatrix}a\\b\\c\end{pmatrix} = \begin{pmatrix}1\\3\\9\end{pmatrix}.$$

### Step 2: Solve the linear system for $a, b, c$
1. From the first equation, we immediately have:
   $$c = 1.$$
2. Substitute $c = 1$ into the second and third equations:
   $$\begin{cases}
   a + b + 1 = 3 \implies a + b = 2, \\
   4a + 2b + 1 = 9 \implies 4a + 2b = 8 \implies 2a + b = 4.
   \end{cases}$$
3. Subtract the equation $a + b = 2$ from $2a + b = 4$ (or in matrix form, $R_2 \leftarrow R_2 - R_1$):
   $$(2a + b) - (a + b) = 4 - 2 \implies a = 2.$$
4. Substitute $a = 2$ into $a + b = 2$:
   $$2 + b = 2 \implies b = 0.$$

### Step 3: Write the resulting polynomial $p(x)$
Substituting $a = 2$, $b = 0$, and $c = 1$ into $p(x) = ax^2 + bx + c$ gives:
$$p(x) = 2x^2 + 0x + 1 = 2x^2 + 1.$$

## 4. Verification and Consistency Checks
We verify our polynomial $p(x) = 2x^2 + 1$ by substituting the $x$-coordinate of each of the three given points and checking that the output matches the given $y$-coordinate:
1. **At $(0, 1)$:**
   $$p(0) = 2(0)^2 + 1 = 0 + 1 = 1 \quad \checkmark \; (\text{matches } y = 1).$$
2. **At $(1, 3)$:**
   $$p(1) = 2(1)^2 + 1 = 2 + 1 = 3 \quad \checkmark \; (\text{matches } y = 3).$$
3. **At $(2, 9)$:**
   $$p(2) = 2(2)^2 + 1 = 2(4) + 1 = 8 + 1 = 9 \quad \checkmark \; (\text{matches } y = 9).$$

All three points lie on the graph of $p(x) = 2x^2 + 1$.
