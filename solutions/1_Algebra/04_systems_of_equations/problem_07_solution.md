# Exercise 7: Choosing a Method Deliberately

## 1. Problem Statement
Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix
   $$\begin{cases}2x-y=3,\\4y=8;\end{cases}$$
2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

## 2. Theoretical Background and Concepts
Solving a linear system $Ax = b$ efficiently depends on matching the computational method to the **structure of $A$** and the **number of right-hand sides $b_i$**:
- **Back-Substitution (Direct Substitution):** When $A$ is already in upper (or lower) triangular (row echelon) form, the elimination phase is already complete. The last equation contains only one unknown, and each preceding equation introduces just one additional unknown.
- **Multiplication by the Inverse ($x_i = A^{-1}b_i$):** Computing $A^{-1}$ from scratch for an $n \times n$ matrix is computationally expensive (equivalent to solving $n$ linear systems via Gauss–Jordan elimination). However, once $A^{-1}$ is **already known**, solving $Ax = b_i$ for any right-hand side $b_i$ reduces to a single matrix-vector multiplication $x_i = A^{-1}b_i$.
- **Gaussian Elimination on $[A \mid b]$:** When $A$ is a dense $n \times n$ matrix, $A^{-1}$ is not given, and only **one** right-hand side vector $b$ is needed, Gaussian elimination followed by back-substitution requires roughly one-third the work of computing $A^{-1}$.

## 3. Detailed Step-by-Step Solution

### Situation 1: One system with a triangular coefficient matrix
$$\begin{cases}2x-y=3,\\4y=8.\end{cases}$$
- **Chosen Method:** **Direct Back-Substitution** (without any forward elimination or matrix inversion).
- **Justification based on structure:** The coefficient matrix $A = \begin{pmatrix}2&-1\\0&4\end{pmatrix}$ is already **upper triangular** (in row echelon form), because the $(2,1)$-entry is $0$. Performing Gaussian elimination is unnecessary because there are no entries below the main diagonal to eliminate, and computing $A^{-1}$ would do superfluous work.
- **Complete Execution of Back-Substitution:**
  1. Solve the second equation (which involves only $y$) directly:
     $$4y = 8 \implies y = \frac{8}{4} = 2.$$
  2. Substitute $y = 2$ upward into the first equation to find $x$:
     $$2x - y = 3 \implies 2x - 2 = 3 \implies 2x = 5 \implies x = \frac{5}{2} = 2.5.$$
  Thus, the unique solution is $(x, y) = \left(\frac{5}{2}, 2\right)$.

---

### Situation 2: Three systems $Ax = b_i$ ($i = 1, 2, 3$) with the same invertible matrix $A$, when $A^{-1}$ is already known
- **Chosen Method:** **Direct Matrix-Vector Multiplication using the known inverse**, $x_i = A^{-1}b_i$ for $i = 1, 2, 3$.
- **Plan and Justification:**
  1. For each of the three right-hand side vectors $b_1, b_2, b_3$, compute the matrix-vector product:
     $$x_1 = A^{-1}b_1, \qquad x_2 = A^{-1}b_2, \qquad x_3 = A^{-1}b_3.$$
  2. **Reusable part:** The precomputed inverse matrix $A^{-1}$ is **reused** across all three systems (and any future right-hand sides $b_i$). Each system then requires only $n^2$ multiplications and $n(n-1)$ additions.
  3. **Unnecessary part:** Performing Gaussian elimination from scratch on $[A \mid b_1]$, $[A \mid b_2]$, and $[A \mid b_3]$ (or even on $[A \mid b_1 \; b_2 \; b_3]$) would be **unnecessary and redundant**, because the work of inverting the operator $A$ has already been completed and stored in $A^{-1}$.

---

### Situation 3: One $3 \times 3$ system where $A^{-1}$ is not given and the goal is only one solution vector
- **Chosen Method:** **Gaussian Elimination to row echelon form followed by Back-Substitution** on the $3 \times 4$ augmented matrix $[A \mid b]$.
- **Plan and Justification:**
  1. Form the $3 \times 4$ augmented matrix $[A \mid b]$.
  2. Apply elementary row operations to zero out the three entries below the main diagonal (positions $(2,1)$, $(3,1)$, and $(3,2)$), producing an upper triangular system.
  3. Solve for $x_3$, then $x_2$, then $x_1$ via back-substitution.
  4. **Unnecessary part:** Computing the $3 \times 3$ inverse matrix $A^{-1}$ (e.g., via Gauss–Jordan elimination on the $3 \times 6$ matrix $[A \mid I_3]$ or via cofactors) and then multiplying $A^{-1}b$ is **completely unnecessary**. Finding $A^{-1}$ is equivalent to solving **three** $3 \times 3$ systems simultaneously ($Ax_1 = e_1, Ax_2 = e_2, Ax_3 = e_3$) and requires eliminating entries *above* the diagonal as well as operating on three right-hand columns instead of just one column $b$. Since we only have **one** right-hand side $b$, computing $A^{-1}$ wastes more than twice as many arithmetic operations.

## 4. Verification and Consistency Checks
1. **Verification of Situation 1 Solution:**
   Substitute $(x, y) = \left(\frac{5}{2}, 2\right)$ into $\begin{cases}2x-y=3\\4y=8\end{cases}$:
   - Equation 1: $2\left(\frac{5}{2}\right) - 2 = 5 - 2 = 3$ (matches $3$).
   - Equation 2: $4(2) = 8$ (matches $8$).
2. **Operation Count Comparison for Situations 2 & 3 (for $n = 3$):**
   - In Situation 2, multiplying a known $3 \times 3$ matrix $A^{-1}$ by a vector $b_i$ takes $9$ multiplications and $6$ additions per vector ($27$ multiplications total for $3$ vectors), with zero row-reduction steps needed.
   - In Situation 3, Gaussian elimination on a $3 \times 4$ matrix $[A \mid b]$ eliminates $3$ sub-diagonal entries and operates on $1$ right-hand column, whereas Gauss–Jordan inversion on $[A \mid I_3]$ eliminates $6$ off-diagonal entries across $3$ right-hand columns.
   This confirms that each method choice is optimal for its problem structure.
