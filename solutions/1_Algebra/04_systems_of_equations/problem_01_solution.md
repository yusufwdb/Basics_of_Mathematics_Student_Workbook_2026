# Exercise 1: From a System to a Matrix

## 1. Problem Statement
Write the system
$$\begin{cases}2x-y+z=4,\\x+3y-2z=1,\\3x+y+z=7.\end{cases}$$
in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

## 2. Theoretical Background and Concepts
Any system of $m$ linear equations in $n$ unknowns $x_1, x_2, \dots, x_n$:
$$\begin{cases}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1, \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2, \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m,
\end{cases}$$
can be written compactly as a single matrix equation
$$A\mathbf{x} = \mathbf{b},$$
where:
- $A = (a_{ij})$ is the $m \times n$ **coefficient matrix** whose $(i,j)$-entry is the coefficient of the $j$-th unknown in the $i$-th equation,
- $\mathbf{x} = \begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}$ is the $n \times 1$ **column vector of unknowns**,
- $\mathbf{b} = \begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$ is the $m \times 1$ **right-hand side (constant) column vector**.

By the definition of matrix-vector multiplication, the $i$-th entry of the product $A\mathbf{x}$ is the dot product of the $i$-th row of $A$ with the column vector $\mathbf{x}$, which reproduces the exact left-hand side of the $i$-th linear equation.

## 3. Detailed Step-by-Step Solution

### Step 1: Identify the components of $Ax = b$
1. **Coefficient Matrix $A$:** Reading the coefficients of $x$, $y$, and $z$ in order from each of the three equations:
   - Equation 1 ($2x - 1y + 1z = 4$) gives row 1: $(2, -1, 1)$
   - Equation 2 ($1x + 3y - 2z = 1$) gives row 2: $(1, 3, -2)$
   - Equation 3 ($3x + 1y + 1z = 7$) gives row 3: $(3, 1, 1)$

   Thus,
   $$A = \begin{pmatrix}
   2 & -1 & 1 \\
   1 & 3 & -2 \\
   3 & 1 & 1
   \end{pmatrix}.$$

2. **Vector of Unknowns $\mathbf{x}$ (or $x$):** The three variables ordered consistently with the columns of $A$:
   $$x = \begin{pmatrix}x\\y\\z\end{pmatrix}.$$

3. **Right-Hand Side Vector $b$:** The constant terms on the right-hand side of each equation:
   $$b = \begin{pmatrix}4\\1\\7\end{pmatrix}.$$

### Step 2: Write the complete matrix equation $Ax = b$
$$\begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1
\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}4\\1\\7\end{pmatrix}.$$

### Step 3: Explain how each row of $A$ corresponds to one equation
In the matrix $A$, the columns correspond to the unknowns $x$ (column 1), $y$ (column 2), and $z$ (column 3), while each row $R_i$ contains the coefficients of a single equation. When we multiply $A$ by the column vector $x = \begin{pmatrix}x\\y\\z\end{pmatrix}$, the $i$-th row $R_i = (a_{i1}, a_{i2}, a_{i3})$ forms the dot product $a_{i1}x + a_{i2}y + a_{i3}z$ and equates it to the $i$-th entry $b_i$ of $b$:
- **Row 1:** $(2, -1, 1)\begin{pmatrix}x\\y\\z\end{pmatrix} = 2x - y + z = 4$ (Equation 1).
- **Row 2:** $(1, 3, -2)\begin{pmatrix}x\\y\\z\end{pmatrix} = x + 3y - 2z = 1$ (Equation 2).
- **Row 3:** $(3, 1, 1)\begin{pmatrix}x\\y\\z\end{pmatrix} = 3x + y + z = 7$ (Equation 3).

## 4. Verification and Consistency Checks
We expand the matrix product $Ax$ explicitly and equate entry-by-entry with $b$:
$$Ax = \begin{pmatrix}
2 & -1 & 1 \\
1 & 3 & -2 \\
3 & 1 & 1
\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}
2x + (-1)y + 1z \\
1x + 3y + (-2)z \\
3x + 1y + 1z
\end{pmatrix} = \begin{pmatrix}4\\1\\7\end{pmatrix} = b.$$
Two column vectors are equal if and only if their corresponding components are equal, which immediately recovers the original three equations in the exact order given.
