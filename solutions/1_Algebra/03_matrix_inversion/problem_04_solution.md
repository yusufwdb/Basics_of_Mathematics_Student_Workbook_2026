# Exercise 4: Gauss–Jordan

## 1. Problem Statement
Find $A^{-1}$ using the Gauss–Jordan method for
$$A=\begin{pmatrix}1&2\\3&5\end{pmatrix}.$$
Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

## 2. Theoretical Background and Concepts
The **Gauss–Jordan elimination method** for inverting an $n \times n$ matrix $A$ works by constructing the $n \times 2n$ augmented matrix $[A \mid I_n]$ and applying a sequence of elementary row operations to transform the left block $A$ into the identity matrix $I_n$.

**Why obtaining $I$ on the left gives $A^{-1}$ on the right:**
Every elementary row operation corresponds to multiplying on the left by an invertible elementary matrix $E_k$. If a sequence of $m$ row operations transforms $A$ into $I_n$, then letting $E = E_m \cdots E_2 E_1$ be the product of those elementary matrices, we have:
$$EA = I_n.$$
By definition of the inverse, this implies $E = A^{-1}$. Since the exact same row operations are simultaneously applied to the right block $I_n$ of the augmented matrix $[A \mid I_n]$, the entire augmented matrix is multiplied on the left by $E$:
$$E[A \mid I_n] = [EA \mid EI_n] = [I_n \mid E] = [I_n \mid A^{-1}].$$
Equivalently, solving $AX = I_2$ for the columns $x_1, x_2$ of $X = A^{-1}$ means simultaneously solving the two linear systems $Ax_1 = e_1$ and $Ax_2 = e_2$.

## 3. Detailed Step-by-Step Solution

### Step 1: Set up the augmented matrix $[A \mid I_2]$
$$\left[\begin{array}{cc|cc}1&2&1&0\\3&5&0&1\end{array}\right]$$

### Step 2: Eliminate the entry below the first pivot
The $(1,1)$-entry is already $1$. To eliminate the $3$ in the $(2,1)$-position, apply the row operation $R_2 \leftarrow R_2 - 3R_1$:
- New $R_2$: $(3 - 3(1),\; 5 - 3(2) \mid 0 - 3(1),\; 1 - 3(0)) = (0, -1 \mid -3, 1)$.

The augmented matrix becomes:
$$\left[\begin{array}{cc|cc}1&2&1&0\\0&-1&-3&1\end{array}\right]$$

### Step 3: Normalize the second pivot to $1$
Multiply the second row by $-1$ ($R_2 \leftarrow -R_2$):
$$\left[\begin{array}{cc|cc}1&2&1&0\\0&1&3&-1\end{array}\right]$$

### Step 4: Eliminate the entry above the second pivot
To eliminate the $2$ in the $(1,2)$-position, apply the row operation $R_1 \leftarrow R_1 - 2R_2$:
- New $R_1$: $(1 - 2(0),\; 2 - 2(1) \mid 1 - 2(3),\; 0 - 2(-1)) = (1, 0 \mid -5, 2)$.

The augmented matrix is now in reduced row echelon form:
$$\left[\begin{array}{cc|cc}1&0&-5&2\\0&1&3&-1\end{array}\right]$$

### Step 5: Read off the inverse matrix
Since the left side is now $I_2$, the right side is $A^{-1}$:
$$A^{-1} = \begin{pmatrix}-5&2\\3&-1\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We verify our result by multiplying $A$ and $A^{-1}$:
$$AA^{-1} = \begin{pmatrix}1&2\\3&5\end{pmatrix}\begin{pmatrix}-5&2\\3&-1\end{pmatrix} = \begin{pmatrix}1(-5)+2(3) & 1(2)+2(-1)\\3(-5)+5(3) & 3(2)+5(-1)\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I_2.$$
We can also check using the $2 \times 2$ determinant formula: $\det(A) = 1(5) - 2(3) = -1$, so
$$A^{-1} = \frac{1}{-1}\begin{pmatrix}5&-2\\-3&1\end{pmatrix} = \begin{pmatrix}-5&2\\3&-1\end{pmatrix},$$
which matches our Gauss–Jordan result.
