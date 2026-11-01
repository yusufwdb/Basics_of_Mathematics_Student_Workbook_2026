# Exercise 15: Associativity of Multiplication and Different Calculation Paths

## 1. Problem Statement

Given
$$A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix},\quad C=\begin{pmatrix}2&1\\0&-1\end{pmatrix}.$$
Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

## 2. Theoretical Background and Concepts

- **Associativity of Matrix Multiplication:** For any three matrices $A_{m\times n}$, $B_{n\times p}$, and $C_{p\times q}$ of compatible dimensions, matrix multiplication is **associative**:
  $$(AB)C = A(BC).$$
  Therefore, the product $ABC$ is unambiguous without parentheses, as long as the left-to-right order of the factors $A, B, C$ is preserved.
- **Computational Complexity of Multiplying $X_{r\times s}$ by $Y_{s\times t}$:** The product $XY$ has size $r \times t$, meaning there are $rt$ entries to compute. Each entry is a dot product of length $s$, requiring $s$ scalar multiplications and $s-1$ scalar additions. In total, computing $XY$ requires:
  $$\text{Multiplications} = r \cdot s \cdot t, \qquad \text{Additions} = r \cdot (s-1) \cdot t.$$

## 3. Detailed Step-by-Step Solution

Here the dimensions are $A_{2\times 3}$, $B_{3\times 2}$, and $C_{2\times 2}$.

### Path 1: Computing $(AB)C$
- **Step 1a: Compute $AB$** ($A_{2\times 3} \cdot B_{3\times 2} \to (AB)_{2\times 2}$):
  $$AB = \begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix} = \begin{pmatrix} 1(1)+2(2)+0(-1) & 1(0)+2(1)+0(3) \\ 0(1)+1(2)+1(-1) & 0(0)+1(1)+1(3) \end{pmatrix} = \begin{pmatrix}5&2\\1&4\end{pmatrix}.$$
- **Step 1b: Multiply $(AB)_{2\times 2}$ by $C_{2\times 2}$**:
  $$(AB)C = \begin{pmatrix}5&2\\1&4\end{pmatrix}\begin{pmatrix}2&1\\0&-1\end{pmatrix} = \begin{pmatrix} 5(2)+2(0) & 5(1)+2(-1) \\ 1(2)+4(0) & 1(1)+4(-1) \end{pmatrix} = \begin{pmatrix}10&3\\2&-3\end{pmatrix}.$$

### Path 2: Computing $A(BC)$
- **Step 2a: Compute $BC$** ($B_{3\times 2} \cdot C_{2\times 2} \to (BC)_{3\times 2}$):
  $$BC = \begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix}\begin{pmatrix}2&1\\0&-1\end{pmatrix} = \begin{pmatrix} 1(2)+0(0) & 1(1)+0(-1) \\ 2(2)+1(0) & 2(1)+1(-1) \\ -1(2)+3(0) & -1(1)+3(-1) \end{pmatrix} = \begin{pmatrix}2&1\\4&1\\-2&-4\end{pmatrix}.$$
- **Step 2b: Multiply $A_{2\times 3}$ by $(BC)_{3\times 2}$**:
  $$A(BC) = \begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}2&1\\4&1\\-2&-4\end{pmatrix} = \begin{pmatrix} 1(2)+2(4)+0(-2) & 1(1)+2(1)+0(-4) \\ 0(2)+1(4)+1(-2) & 0(1)+1(1)+1(-4) \end{pmatrix} = \begin{pmatrix}10&3\\2&-3\end{pmatrix}.$$

### Comparison of Results and Intermediate Operations

1. **Equality of Final Results:** Both paths yield the exact same $2 \times 2$ matrix:
   $$(AB)C = A(BC) = \begin{pmatrix}10&3\\2&-3\end{pmatrix}.$$
2. **Comparison of Operation Counts:**
   - **Path 1 — $(AB)C$:**
     - Forming $AB$ ($2\times 3$ times $3\times 2 \to 2\times 2$, $4$ intermediate entries): requires $2 \cdot 3 \cdot 2 = 12$ scalar multiplications and $2 \cdot (3-1) \cdot 2 = 8$ additions.
     - Forming $(AB)C$ ($2\times 2$ times $2\times 2 \to 2\times 2$, $4$ final entries): requires $2 \cdot 2 \cdot 2 = 8$ scalar multiplications and $2 \cdot (2-1) \cdot 2 = 4$ additions.
     - **Total for $(AB)C$:** $12 + 8 = \mathbf{20}$ scalar multiplications and $8 + 4 = \mathbf{12}$ scalar additions ($32$ elementary arithmetic operations).
   - **Path 2 — $A(BC)$:**
     - Forming $BC$ ($3\times 2$ times $2\times 2 \to 3\times 2$, $6$ intermediate entries): requires $3 \cdot 2 \cdot 2 = 12$ scalar multiplications and $3 \cdot (2-1) \cdot 2 = 6$ additions.
     - Forming $A(BC)$ ($2\times 3$ times $3\times 2 \to 2\times 2$, $4$ final entries): requires $2 \cdot 3 \cdot 2 = 12$ scalar multiplications and $2 \cdot (3-1) \cdot 2 = 8$ additions.
     - **Total for $A(BC)$:** $12 + 12 = \mathbf{24}$ scalar multiplications and $6 + 8 = \mathbf{14}$ scalar additions ($38$ elementary arithmetic operations).
   - **Conclusion on Efficiency:** Path 1, $(AB)C$, is computationally more efficient because its intermediate matrix $AB$ is smaller ($2 \times 2$, $4$ entries) than the intermediate matrix $BC$ ($3 \times 2$, $6$ entries).

### Meaning of Associativity in This Example
Associativity of matrix multiplication means that **how we group adjacent factors with parentheses in a chain of matrix multiplications does not affect the final result**, even though the intermediate matrices ($AB$ of size $2\times 2$ vs. $BC$ of size $3\times 2$) and the number of arithmetic operations performed along the way are different. In practical computation, this allows us to choose the parenthesization that minimizes the number of intermediate operations while guaranteeing the exact same mathematical output.

## 4. Verification and Consistency Checks

Let us verify the result by applying both expressions to the standard basis vectors $e_1 = \begin{pmatrix}1\\0\end{pmatrix}$ and $e_2 = \begin{pmatrix}0\\1\end{pmatrix}$ via matrix-vector products $A(B(Ce_j))$:
- $Ce_1 = \begin{pmatrix}2\\0\end{pmatrix} \implies B(Ce_1) = 2\begin{pmatrix}1\\2\\-1\end{pmatrix} = \begin{pmatrix}2\\4\\-2\end{pmatrix} \implies A(B(Ce_1)) = \begin{pmatrix}2+8+0\\0+4-2\end{pmatrix} = \begin{pmatrix}10\\2\end{pmatrix}$ (matches Column 1 of $ABC$). $\checkmark$
- $Ce_2 = \begin{pmatrix}1\\-1\end{pmatrix} \implies B(Ce_2) = \begin{pmatrix}1\\2\\-1\end{pmatrix} - \begin{pmatrix}0\\1\\3\end{pmatrix} = \begin{pmatrix}1\\1\\-4\end{pmatrix} \implies A(B(Ce_2)) = \begin{pmatrix}1+2+0\\0+1-4\end{pmatrix} = \begin{pmatrix}3\\-3\end{pmatrix}$ (matches Column 2 of $ABC$). $\checkmark$
