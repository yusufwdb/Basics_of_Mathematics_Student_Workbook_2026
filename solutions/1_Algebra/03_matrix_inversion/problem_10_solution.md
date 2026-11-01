# Exercise 10: Inverse of a Diagonal Matrix

## 1. Problem Statement
Given
$$D=\begin{pmatrix}2&0&0\\0&-3&0\\0&0&5\end{pmatrix},\qquad E=\begin{pmatrix}2&0&0\\0&0&0\\0&0&5\end{pmatrix}.$$
Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

## 2. Theoretical Background and Concepts
A square matrix $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$ is called a **diagonal matrix** if all entries outside the main diagonal are zero ($D_{ij} = 0$ for all $i \neq j$).
Key properties of diagonal matrices:
1. **Product of diagonal matrices:** Multiplying two diagonal matrices simply multiplies their corresponding diagonal entries:
   $$\operatorname{diag}(d_1, d_2, \dots, d_n)\operatorname{diag}(c_1, c_2, \dots, c_n) = \operatorname{diag}(d_1 c_1, d_2 c_2, \dots, d_n c_n).$$
2. **Determinant:** $\det(D) = d_1 d_2 \cdots d_n$.
3. **Invertibility Criterion:** A diagonal matrix is invertible if and only if **every** main diagonal entry is non-zero ($d_i \neq 0$ for all $i = 1, \dots, n$).
4. **Inverse Formula:** When all $d_i \neq 0$, the inverse is immediately obtained by inverting each diagonal entry:
   $$D^{-1} = \operatorname{diag}\left(\frac{1}{d_1}, \frac{1}{d_2}, \dots, \frac{1}{d_n}\right).$$

## 3. Detailed Step-by-Step Solution

### Step 1: Decide which matrix is invertible
- **Matrix $D$:** The diagonal entries of $D$ are $d_1 = 2$, $d_2 = -3$, and $d_3 = 5$. Since all three diagonal entries are non-zero (and $\det(D) = 2(-3)(5) = -30 \neq 0$), **$D$ is invertible**.
- **Matrix $E$:** The diagonal entries of $E$ are $e_1 = 2$, $e_2 = 0$, and $e_3 = 5$. Because the second diagonal entry is zero ($e_2 = 0$), the entire second row and second column of $E$ consist of zeros, and $\det(E) = 2(0)(5) = 0$. For any $3 \times 3$ matrix $B$, the second row of $EB$ is always $(0, 0, 0)$, so $EB$ can never equal $I_3$. Therefore, **$E$ is not invertible**.

### Step 2: Write the inverse of the invertible matrix $D$
Taking the reciprocal of each non-zero diagonal entry of $D$, we obtain:
$$D^{-1} = \begin{pmatrix}
\frac{1}{2} & 0 & 0 \\[4pt]
0 & -\frac{1}{3} & 0 \\[4pt]
0 & 0 & \frac{1}{5}
\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We check the result by computing the matrix product $DD^{-1}$ (and $D^{-1}D$):
$$DD^{-1} = \begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5
\end{pmatrix}\begin{pmatrix}
\frac{1}{2} & 0 & 0 \\[4pt]
0 & -\frac{1}{3} & 0 \\[4pt]
0 & 0 & \frac{1}{5}
\end{pmatrix} = \begin{pmatrix}
2\left(\frac{1}{2}\right) & 0 & 0 \\[4pt]
0 & (-3)\left(-\frac{1}{3}\right) & 0 \\[4pt]
0 & 0 & 5\left(\frac{1}{5}\right)
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix} = I_3.$$
Similarly, $D^{-1}D = I_3$. This confirms that $D^{-1}$ is the exact inverse of $D$.
