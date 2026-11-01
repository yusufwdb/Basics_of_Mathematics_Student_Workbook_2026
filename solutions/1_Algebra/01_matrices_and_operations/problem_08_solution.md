# Exercise 8: Row Operations and Their Reversibility

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2&-1\\2&4&1\\-1&1&3\end{pmatrix}$$
perform, in order:
1. $R_2\leftarrow R_2-2R_1$,
2. $R_3\leftarrow R_3+R_1$,
3. interchange $R_2$ and $R_3$.

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

## 2. Theoretical Background and Concepts

- **Elementary Row Operations:** There are three types of elementary row operations on a matrix:
  1. **Row Replacement (Addition):** Replace row $i$ by the sum of row $i$ and $c$ times row $j$ ($R_i \leftarrow R_i + c R_j$, with $i \neq j$).
  2. **Row Interchange (Swap):** Interchange two rows $i$ and $j$ ($R_i \leftrightarrow R_j$).
  3. **Row Scaling:** Multiply all entries in row $i$ by a nonzero scalar $c \neq 0$ ($R_i \leftarrow c R_i$).
- **Reversibility (Invertibility) of Row Operations:** Every elementary row operation is reversible by another elementary row operation of the same type:
  - The inverse of $R_i \leftarrow R_i + c R_j$ is $R_i \leftarrow R_i - c R_j$ (since row $j$ was unchanged by the operation).
  - The inverse of $R_i \leftrightarrow R_j$ is $R_i \leftrightarrow R_j$ itself (swapping the two rows a second time restores their original positions).
  - The inverse of $R_i \leftarrow c R_i$ ($c \neq 0$) is $R_i \leftarrow \frac{1}{c} R_i$.

## 3. Detailed Step-by-Step Solution

Start with the initial matrix:
$$A = \begin{pmatrix}1&2&-1\\2&4&1\\-1&1&3\end{pmatrix}.$$

### Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$
We subtract $2$ times the first row $R_1 = (1, 2, -1)$ from the second row $R_2 = (2, 4, 1)$:
$$\text{New } R_2 = (2 - 2(1),\ 4 - 2(2),\ 1 - 2(-1)) = (0,\ 0,\ 3).$$
The matrix after Step 1 is:
$$A_1 = \begin{pmatrix}1&2&-1\\0&0&3\\-1&1&3\end{pmatrix}.$$

### Step 2: Perform $R_3 \leftarrow R_3 + R_1$
We add the first row $R_1 = (1, 2, -1)$ to the third row $R_3 = (-1, 1, 3)$ of $A_1$:
$$\text{New } R_3 = (-1 + 1,\ 1 + 2,\ 3 + (-1)) = (0,\ 3,\ 2).$$
The matrix after Step 2 is:
$$A_2 = \begin{pmatrix}1&2&-1\\0&0&3\\0&3&2\end{pmatrix}.$$

### Step 3: Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)
We swap the second and third rows of $A_2$:
$$A_3 = \begin{pmatrix}1&2&-1\\0&3&2\\0&0&3\end{pmatrix}.$$
(Notice that $A_3$ is now in upper triangular / row echelon form!)

### Reversing Each Operation
1. **To reverse Step 1 ($R_2 \leftarrow R_2 - 2R_1$):** Add $2$ times row $1$ back to row $2$:
   $$R_2 \leftarrow R_2 + 2R_1.$$
2. **To reverse Step 2 ($R_3 \leftarrow R_3 + R_1$):** Subtract row $1$ from row $3$:
   $$R_3 \leftarrow R_3 - R_1.$$
3. **To reverse Step 3 ($R_2 \leftrightarrow R_3$):** Interchange row $2$ and row $3$ again:
   $$R_2 \leftrightarrow R_3.$$

*(Note: To return from $A_3$ all the way back to $A$, we apply these reverse operations in the **reverse order**: first $R_2 \leftrightarrow R_3$, then $R_3 \leftarrow R_3 - R_1$, and finally $R_2 \leftarrow R_2 + 2R_1$.)*

## 4. Verification and Consistency Checks

Let us apply the three reverse operations in reverse order to $A_3$ to verify that we recover $A$:
1. Start from $A_3 = \begin{pmatrix}1&2&-1\\0&3&2\\0&0&3\end{pmatrix}$ and apply $R_2 \leftrightarrow R_3$:
   $$\begin{pmatrix}1&2&-1\\0&0&3\\0&3&2\end{pmatrix} = A_2. \quad \checkmark$$
2. Apply $R_3 \leftarrow R_3 - R_1$:
   $$\text{New } R_3 = (0-1,\ 3-2,\ 2-(-1)) = (-1,\ 1,\ 3) \implies \begin{pmatrix}1&2&-1\\0&0&3\\-1&1&3\end{pmatrix} = A_1. \quad \checkmark$$
3. Apply $R_2 \leftarrow R_2 + 2R_1$:
   $$\text{New } R_2 = (0+2(1),\ 0+2(2),\ 3+2(-1)) = (2,\ 4,\ 1) \implies \begin{pmatrix}1&2&-1\\2&4&1\\-1&1&3\end{pmatrix} = A. \quad \checkmark$$
Every intermediate matrix and the original matrix $A$ are recovered identically.
