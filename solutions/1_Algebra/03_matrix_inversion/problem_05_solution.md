# Exercise 5: A 3×3 Matrix

## 1. Problem Statement
Use Gauss–Jordan elimination to find the inverse of
$$A=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.$$
Check the result by multiplication.

## 2. Theoretical Background and Concepts
For a $3 \times 3$ matrix $A$, the simple $2 \times 2$ swap-and-negate shortcut does not apply. Instead, we use **Gauss–Jordan elimination**:
1. Form the $3 \times 6$ augmented matrix $[A \mid I_3]$.
2. Use elementary row operations (row swapping, multiplying a row by a non-zero scalar, adding a scalar multiple of one row to another) to transform the left $3 \times 3$ block into the reduced row echelon form $I_3$.
3. Once the left block becomes $I_3$, the right $3 \times 3$ block is $A^{-1}$.

## 3. Detailed Step-by-Step Solution

### Step 1: Construct the augmented matrix $[A \mid I_3]$
$$\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 1
\end{array}\right]$$

### Step 2: Eliminate the entry in position $(3,1)$
Apply $R_3 \leftarrow R_3 - R_1$:
$$\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & -1 & 1 & -1 & 0 & 1
\end{array}\right]$$

### Step 3: Eliminate the entry in position $(3,2)$
The second pivot at $(2,2)$ is already $1$. Apply $R_3 \leftarrow R_3 + R_2$:
$$\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 2 & -1 & 1 & 1
\end{array}\right]$$

### Step 4: Normalize the third pivot at $(3,3)$ to $1$
Apply $R_3 \leftarrow \frac{1}{2}R_3$:
$$\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 1 & 0 \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]$$

### Step 5: Eliminate above the third pivot in position $(2,3)$
Apply $R_2 \leftarrow R_2 - R_3$:
- New $R_2$ right side: $\left(0 - \left(-\frac{1}{2}\right),\; 1 - \frac{1}{2},\; 0 - \frac{1}{2}\right) = \left(\frac{1}{2},\; \frac{1}{2},\; -\frac{1}{2}\right)$.

$$\left[\begin{array}{ccc|ccc}
1 & 1 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]$$

### Step 6: Eliminate above the second pivot in position $(1,2)$
Apply $R_1 \leftarrow R_1 - R_2$:
- New $R_1$ right side: $\left(1 - \frac{1}{2},\; 0 - \frac{1}{2},\; 0 - \left(-\frac{1}{2}\right)\right) = \left(\frac{1}{2},\; -\frac{1}{2},\; \frac{1}{2}\right)$.

$$\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\[4pt]
0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\[4pt]
0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{array}\right]$$

### Step 7: Write the inverse matrix $A^{-1}$
Factoring out $\frac{1}{2}$ for clarity:
$$A^{-1} = \begin{pmatrix}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\[4pt]
\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\[4pt]
-\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{pmatrix} = \frac{1}{2}\begin{pmatrix}
1 & -1 & 1 \\
1 & 1 & -1 \\
-1 & 1 & 1
\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We check the result by computing the product $AA^{-1}$:
$$AA^{-1} = \begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix} \cdot \frac{1}{2}\begin{pmatrix}1&-1&1\\1&1&-1\\-1&1&1\end{pmatrix} = \frac{1}{2}\begin{pmatrix}
1+1+0 & -1+1+0 & 1-1+0 \\
0+1-1 & 0+1+1 & 0-1+1 \\
1+0-1 & -1+0+1 & 1+0+1
\end{pmatrix}$$
Simplifying the entries inside the matrix:
$$AA^{-1} = \frac{1}{2}\begin{pmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} = I_3.$$
Similarly, $A^{-1}A = I_3$. The inverse is verified.
