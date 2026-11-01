# Exercise 6: Solving a System Using the Inverse

## 1. Problem Statement
Solve
$$Ax=b,$$
where
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}5\\7\end{pmatrix},$$
using $x=A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

## 2. Theoretical Background and Concepts
Consider a system of $n$ linear equations in $n$ unknowns written in matrix form as
$$Ax = b,$$
where $A$ is an $n \times n$ coefficient matrix, $x$ is the $n \times 1$ column vector of unknowns, and $b$ is the $n \times 1$ right-hand side column vector. If $A$ is invertible ($\det(A) \neq 0$), we can multiply both sides of the equation on the left by $A^{-1}$:
$$A^{-1}(Ax) = A^{-1}b \implies (A^{-1}A)x = A^{-1}b \implies I_n x = A^{-1}b \implies x = A^{-1}b.$$
Thus, the system has the unique solution $x = A^{-1}b$.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute the determinant of $A$ and find $A^{-1}$
For
$$A = \begin{pmatrix}2&1\\1&3\end{pmatrix},$$
the determinant is:
$$\det(A) = (2)(3) - (1)(1) = 6 - 1 = 5 \neq 0.$$
Using the $2 \times 2$ inverse formula:
$$A^{-1} = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix} = \begin{pmatrix}\frac{3}{5}&-\frac{1}{5}\\[4pt]-\frac{1}{5}&\frac{2}{5}\end{pmatrix}.$$

### Step 2: Compute the solution vector $x = A^{-1}b$
Multiply $A^{-1}$ by $b = \begin{pmatrix}5\\7\end{pmatrix}$:
$$x = A^{-1}b = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix}\begin{pmatrix}5\\7\end{pmatrix}.$$
First, compute the matrix-vector product before dividing by $5$:
$$\begin{pmatrix}3&-1\\-1&2\end{pmatrix}\begin{pmatrix}5\\7\end{pmatrix} = \begin{pmatrix}3(5) + (-1)(7)\\(-1)(5) + 2(7)\end{pmatrix} = \begin{pmatrix}15 - 7\\-5 + 14\end{pmatrix} = \begin{pmatrix}8\\9\end{pmatrix}.$$
Now multiply by $\frac{1}{5}$:
$$x = \frac{1}{5}\begin{pmatrix}8\\9\end{pmatrix} = \begin{pmatrix}\frac{8}{5}\\[4pt]\frac{9}{5}\end{pmatrix} = \begin{pmatrix}1.6\\1.8\end{pmatrix}.$$

## 4. Verification and Consistency Checks
We substitute $x = \begin{pmatrix}\frac{8}{5}\\[4pt]\frac{9}{5}\end{pmatrix}$ back into the left-hand side of the original equation $Ax = b$:
$$Ax = \begin{pmatrix}2&1\\1&3\end{pmatrix}\begin{pmatrix}\frac{8}{5}\\[4pt]\frac{9}{5}\end{pmatrix} = \begin{pmatrix}2\left(\frac{8}{5}\right) + 1\left(\frac{9}{5}\right)\\[6pt]1\left(\frac{8}{5}\right) + 3\left(\frac{9}{5}\right)\end{pmatrix} = \begin{pmatrix}\frac{16 + 9}{5}\\[6pt]\frac{8 + 27}{5}\end{pmatrix} = \begin{pmatrix}\frac{25}{5}\\[6pt]\frac{35}{5}\end{pmatrix} = \begin{pmatrix}5\\7\end{pmatrix} = b.$$
Since $Ax = b$ holds identically, the solution $x = \begin{pmatrix}\frac{8}{5}\\[4pt]\frac{9}{5}\end{pmatrix}$ is verified.
