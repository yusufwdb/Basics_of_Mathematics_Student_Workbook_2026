# Exercise 14: A System of Equations and the Determinant

## 1. Problem Statement

Consider the system $Ax=b$, where
$$A=\begin{pmatrix}1&2\\k&4\end{pmatrix}.$$
For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

## 2. Theoretical Background and Concepts

- **Determinant Criterion for Unique Solutions (Cramer's Theorem / Invertible Matrix Theorem):** A linear system $Ax = b$ with an $n \times n$ coefficient matrix $A$ has **exactly one (unique) solution** $x = A^{-1}b$ for every right-hand side $b \in \mathbb{R}^n$ **if and only if** $A$ is invertible, i.e.:
  $$\det A \neq 0.$$
- **Singular Case ($\det A = 0$):** When $\det A = 0$, the rows of $A$ are linearly dependent, and the system $Ax = b$ never has a unique solution. Instead, depending on whether the right-hand side vector $b$ satisfies the same linear dependence relation as the rows of $A$ (i.e., whether $b$ lies in the column space of $A$):
  - If $b$ is compatible with the row dependence ($\operatorname{rank}(A) = \operatorname{rank}(A|b)$), the system has **infinitely many solutions**.
  - If $b$ violates the row dependence ($\operatorname{rank}(A) < \operatorname{rank}(A|b)$), the system is inconsistent and has **no solution**.

## 3. Detailed Step-by-Step Solution

### 1. Values of $k$ for Which the System Has a Unique Solution for Every $b$
First compute the determinant of $A$:
$$\det A = \det\begin{pmatrix}1&2\\k&4\end{pmatrix} = 1 \cdot 4 - 2 \cdot k = 4 - 2k.$$
The system $Ax = b$ has a unique solution for every $b \in \mathbb{R}^2$ if and only if $\det A \neq 0$:
$$4 - 2k \neq 0 \iff 2k \neq 4 \iff k \neq 2.$$
Thus, the system has **exactly one solution for every $b$ whenever $k \in \mathbb{R} \setminus \{2\}$** (i.e., **$k \neq 2$**).

### 2. Analyzing the Remaining Value ($k = 2$)
When **$k = 2$**, the coefficient matrix becomes
$$A = \begin{pmatrix}1&2\\2&4\end{pmatrix},$$
and the system $Ax = b$ with $x = \begin{pmatrix}x_1\\x_2\end{pmatrix}$ and $b = \begin{pmatrix}b_1\\b_2\end{pmatrix}$ is written explicitly as:
$$\begin{cases} x_1 + 2x_2 = b_1, \\ 2x_1 + 4x_2 = b_2. \end{cases}$$
Notice that the left-hand side of the second equation is exactly $2$ times the left-hand side of the first equation: $2(x_1 + 2x_2) = 2x_1 + 4x_2$. Subtracting $2$ times the first equation from the second ($R_2 \leftarrow R_2 - 2R_1$ on the augmented matrix) gives:
$$\left(\begin{array}{cc|c} 1 & 2 & b_1 \\ 0 & 0 & b_2 - 2b_1 \end{array}\right).$$
Therefore, for $k = 2$, the second equation reduces to $0 = b_2 - 2b_1$, or **$b_2 = 2b_1$**.

#### (a) Example of $b$ Giving Infinitely Many Solutions (for $k = 2$)
Choose any $b = \begin{pmatrix}b_1\\b_2\end{pmatrix}$ satisfying $b_2 = 2b_1$, for instance:
$$b = \begin{pmatrix}1\\2\end{pmatrix} \qquad \left(\text{or } b = \begin{pmatrix}0\\0\end{pmatrix}\right).$$
For $b = \begin{pmatrix}1\\2\end{pmatrix}$, the system is
$$\begin{cases} x_1 + 2x_2 = 1, \\ 2x_1 + 4x_2 = 2. \end{cases}$$
The second equation is simply $2$ times the first equation, so the system reduces to the single line $x_1 = 1 - 2x_2$. Setting $x_2 = t \in \mathbb{R}$ as a free parameter gives **infinitely many solutions**:
$$x = \begin{pmatrix}1 - 2t\\t\end{pmatrix}, \qquad t \in \mathbb{R}.$$

#### (b) Example of $b$ Giving No Solution (for $k = 2$)
Choose any $b = \begin{pmatrix}b_1\\b_2\end{pmatrix}$ with $b_2 \neq 2b_1$, for instance:
$$b = \begin{pmatrix}1\\0\end{pmatrix} \qquad \left(\text{or } b = \begin{pmatrix}1\\3\end{pmatrix}\right).$$
For $b = \begin{pmatrix}1\\0\end{pmatrix}$, the system is
$$\begin{cases} x_1 + 2x_2 = 1, \\ 2x_1 + 4x_2 = 0. \end{cases}$$
Multiplying the first equation by $2$ gives $2x_1 + 4x_2 = 2$, which directly contradicts the second equation $2x_1 + 4x_2 = 0$ ($2 = 0$, impossible!). Hence the system has **no solution**.

## 4. Verification and Consistency Checks

1. **Unique Solution Formula for $k \neq 2$:** When $k \neq 2$, $A^{-1} = \frac{1}{4-2k}\begin{pmatrix}4&-2\\-k&1\end{pmatrix}$, so for any $b = \begin{pmatrix}b_1\\b_2\end{pmatrix}$ there is the unique solution $x = A^{-1}b = \frac{1}{4-2k}\begin{pmatrix}4b_1 - 2b_2\\-kb_1 + b_2\end{pmatrix}$. Notice that the denominator $4-2k$ vanishes precisely at $k=2$, and the numerator $\begin{pmatrix}2(2b_1 - b_2)\\b_2 - 2b_1\end{pmatrix}$ at $k=2$ vanishes if and only if $b_2 = 2b_1$!
2. **Direct Substitution Check for $k=2, b=\begin{pmatrix}1\\2\end{pmatrix}$:** Taking two distinct values of $t$, say $t=0 \implies x=\begin{pmatrix}1\\0\end{pmatrix}$ and $t=1 \implies x=\begin{pmatrix}-1\\1\end{pmatrix}$:
   $$\begin{pmatrix}1&2\\2&4\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}1\\2\end{pmatrix}, \qquad \begin{pmatrix}1&2\\2&4\end{pmatrix}\begin{pmatrix}-1\\1\end{pmatrix} = \begin{pmatrix}1\\2\end{pmatrix}. \quad \checkmark$$
