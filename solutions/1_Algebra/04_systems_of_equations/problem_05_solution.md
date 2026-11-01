# Exercise 5: Row Echelon Form and Number of Solutions

## 1. Problem Statement
For the augmented matrix
$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&2&1\\0&0&0&0\end{array}\right]$$
determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

## 2. Theoretical Background and Concepts
Given an augmented matrix $[A \mid b]$ that is already in **row echelon form**:
1. **Consistency:** We inspect any rows whose coefficient entries are all zero. If the right-hand side entry in such a row is also $0$ (i.e., $[0 \;\; 0 \;\; 0 \mid 0]$, representing $0 = 0$), the system is **consistent** ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b])$).
2. **Counting Free Variables (Rank–Nullity / Rouché–Capelli):**
   Let $n$ be the total number of unknowns (columns of $A$) and let $r = \operatorname{rank}(A)$ be the number of non-zero rows (which equals the number of **pivots**, i.e., leading non-zero entries in each row).
   - The $r$ variables corresponding to pivot columns are **basic variables** (uniquely determined once the remaining variables are fixed).
   - The remaining **$n - r$ variables** corresponding to non-pivot columns are **free variables**, which can be chosen freely as independent real parameters.
   - When $n - r \ge 1$ in a consistent system over $\mathbb{R}$, the system has **infinitely many solutions**.

## 3. Detailed Step-by-Step Solution

### Step 1: Determine the number of solutions and explain how many variables are free
Inspecting the given row echelon augmented matrix
$$\left[\begin{array}{ccc|c}
\mathbf{1} & 2 & -1 & 3 \\
0 & \mathbf{1} & 2 & 1 \\
0 & 0 & 0 & 0
\end{array}\right]$$
we observe:
- The third row is $[0 \;\; 0 \;\; 0 \mid 0]$ ($0 = 0$), so there is **no contradiction** and the system is **consistent**.
- The total number of unknowns (columns to the left of the bar) is $n = 3$ (let us denote them $x_1, x_2, x_3$).
- There are $r = 2$ non-zero rows, with **pivots** located at $(1,1)$ (in column 1 for $x_1$) and $(2,2)$ (in column 2 for $x_2$).
- Column 3 (for $x_3$) contains **no pivot**.

Therefore, the number of variables that may be chosen freely is:
$$\text{Number of free variables} = n - r = 3 - 2 = 1.$$
Because the system is consistent and has $1$ free variable ($x_3 \in \mathbb{R}$), the system has **infinitely many solutions**.

### Step 2: Write the solutions in parametric form
Let the unknowns be $x_1, x_2, x_3$, and set the single free variable (corresponding to the non-pivot third column) to a real parameter $t \in \mathbb{R}$:
$$x_3 = t.$$
Now use back-substitution to express the basic variables $x_2$ and $x_1$ in terms of $t$:
1. **From Row 2:**
   $$1\cdot x_2 + 2x_3 = 1 \implies x_2 = 1 - 2x_3 = 1 - 2t.$$
2. **From Row 1:**
   $$1\cdot x_1 + 2x_2 - x_3 = 3 \implies x_1 = 3 - 2x_2 + x_3.$$
   Substitute $x_2 = 1 - 2t$ and $x_3 = t$:
   $$x_1 = 3 - 2(1 - 2t) + t = 3 - 2 + 4t + t = 1 + 5t.$$

Thus, the parametric form of the solution set is:
$$\begin{cases}
x_1 = 1 + 5t, \\
x_2 = 1 - 2t, \\
x_3 = t,
\end{cases} \quad t \in \mathbb{R},$$
or in vector notation:
$$\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix} = \begin{pmatrix}1 + 5t\\1 - 2t\\t\end{pmatrix} = \begin{pmatrix}1\\1\\0\end{pmatrix} + t\begin{pmatrix}5\\-2\\1\end{pmatrix}, \quad t \in \mathbb{R}.$$

## 4. Verification and Consistency Checks
We substitute $x_1 = 1 + 5t$, $x_2 = 1 - 2t$, and $x_3 = t$ back into the equations represented by the rows of the augmented matrix:
1. **Row 1 check:**
   $$x_1 + 2x_2 - x_3 = (1 + 5t) + 2(1 - 2t) - t = 1 + 5t + 2 - 4t - t = 3 \quad (\text{matches } 3).$$
2. **Row 2 check:**
   $$0x_1 + x_2 + 2x_3 = (1 - 2t) + 2t = 1 \quad (\text{matches } 1).$$
3. **Row 3 check:**
   $$0x_1 + 0x_2 + 0x_3 = 0 \quad (\text{matches } 0).$$

All equations hold identically for every $t \in \mathbb{R}$.
