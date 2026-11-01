# Exercise 3: Swapping Two Rows

## 1. Problem Statement

For
$$A=\begin{pmatrix}1&2&0\\0&3&1\\2&1&1\end{pmatrix}$$
compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

## 2. Theoretical Background and Concepts

- **Alternating (Sign-Reversal) Property of Determinants:** If a matrix $B$ is obtained from a square matrix $A$ by interchanging (swapping) any two rows ($R_i \leftrightarrow R_j$, $i \neq j$), then the determinant changes sign:
  $$\det B = -\det A.$$
- **Cofactor Expansion / Sarrus' Rule:** For a $3 \times 3$ matrix, the determinant can be computed either via Sarrus' rule or by Laplace cofactor expansion along any row or column (especially a row or column containing a zero).

## 3. Detailed Step-by-Step Solution

### 1. Computing $\det A$
Given
$$A = \begin{pmatrix}1&2&0\\0&3&1\\2&1&1\end{pmatrix}.$$
Using Sarrus' rule:
- Main diagonals: $(1 \cdot 3 \cdot 1) + (2 \cdot 1 \cdot 2) + (0 \cdot 0 \cdot 1) = 3 + 4 + 0 = 7$.
- Anti-diagonals: $(2 \cdot 3 \cdot 0) + (1 \cdot 1 \cdot 1) + (1 \cdot 0 \cdot 2) = 0 + 1 + 0 = 1$.
Subtracting the anti-diagonal sum from the main-diagonal sum:
$$\det A = 7 - 1 = 6.$$

### 2. Forming Matrix $B$ and Predicting $\det B$
Swapping the first and second rows of $A$ ($R_1 \leftrightarrow R_2$) gives:
$$B = \begin{pmatrix}0&3&1\\1&2&0\\2&1&1\end{pmatrix}.$$
**Prediction:** By the row-swap property of determinants, interchanging two rows of a square matrix multiplies its determinant by $-1$. Therefore, we predict:
$$\det B = -\det A = -6.$$

### 3. Verifying $\det B$ by Direct Calculation
Let us compute $\det B$ directly using Sarrus' rule on $B$:
- Main diagonals: $(0 \cdot 2 \cdot 1) + (3 \cdot 0 \cdot 2) + (1 \cdot 1 \cdot 1) = 0 + 0 + 1 = 1$.
- Anti-diagonals: $(2 \cdot 2 \cdot 1) + (1 \cdot 0 \cdot 0) + (1 \cdot 1 \cdot 3) = 4 + 0 + 3 = 7$.
Subtracting the anti-diagonal sum from the main-diagonal sum:
$$\det B = 1 - 7 = -6.$$
Notice how the main-diagonal sum ($7 \to 1$) and anti-diagonal sum ($1 \to 7$) swapped roles when $R_1$ and $R_2$ were interchanged! Our direct calculation matches the predicted value $\det B = -6$.

## 4. Verification and Consistency Checks

Let us also check both determinants by cofactor expansion along the row containing a zero:
- For $A$, expand along Row 1:
  $$\det A = 1 \cdot \det\begin{pmatrix}3&1\\1&1\end{pmatrix} - 2 \cdot \det\begin{pmatrix}0&1\\2&1\end{pmatrix} + 0 = 1(3 - 1) - 2(0 - 2) = 2 + 4 = 6. \quad \checkmark$$
- For $B$, expand along Row 2 (which is the old Row 1 moved to position 2, so the cofactor signs flip from $(+,-,+)$ to $(-,+,-)$):
  $$\det B = -1 \cdot \det\begin{pmatrix}3&1\\1&1\end{pmatrix} + 2 \cdot \det\begin{pmatrix}0&1\\2&1\end{pmatrix} - 0 = -1(3 - 1) + 2(0 - 2) = -2 - 4 = -6. \quad \checkmark$$
This cofactor sign shift $(-1)^{1+j} \to (-1)^{2+j}$ clearly illustrates why swapping adjacent rows negates the determinant.
