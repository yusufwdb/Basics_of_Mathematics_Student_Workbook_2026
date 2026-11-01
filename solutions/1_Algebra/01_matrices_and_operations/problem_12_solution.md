# Exercise 12: Formula for a Matrix Power

## 1. Problem Statement

Let
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}.$$
Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

## 2. Theoretical Background and Concepts

- **Successive Powers of a Matrix:** For a square matrix $A$ and integer $n \ge 1$, powers are defined inductively by $A^1 = A$ and $A^{n+1} = A^n \cdot A$.
- **Principle of Mathematical Induction:** To prove that a statement $P(n)$ holds for all positive integers $n \ge 1$:
  1. **Base Case:** Verify that $P(1)$ is true.
  2. **Inductive Step:** Assume the induction hypothesis that $P(n)$ holds for some arbitrary positive integer $n$, and prove that $P(n+1)$ must also hold.
- **Geometric Meaning:** The matrix $A = \begin{pmatrix}1&1\\0&1\end{pmatrix}$ is a **horizontal shear** transformation that shifts every point $(x,y)$ horizontally by $y$: $(x,y) \mapsto (x+y, y)$. Applying this unit shear $n$ times shifts $(x,y)$ horizontally by $ny$.

## 3. Detailed Step-by-Step Solution

### 1. Computing $A^2$, $A^3$, and $A^4$
- **$A^2 = A \cdot A$:**
  $$A^2 = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}1(1)+1(0) & 1(1)+1(1)\\0(1)+1(0) & 0(1)+1(1)\end{pmatrix} = \begin{pmatrix}1&2\\0&1\end{pmatrix}.$$
- **$A^3 = A^2 \cdot A$:**
  $$A^3 = \begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}1(1)+2(0) & 1(1)+2(1)\\0(1)+1(0) & 0(1)+1(1)\end{pmatrix} = \begin{pmatrix}1&3\\0&1\end{pmatrix}.$$
- **$A^4 = A^3 \cdot A$:**
  $$A^4 = \begin{pmatrix}1&3\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}1(1)+3(0) & 1(1)+3(1)\\0(1)+1(0) & 0(1)+1(1)\end{pmatrix} = \begin{pmatrix}1&4\\0&1\end{pmatrix}.$$

### 2. Formulating the Conjecture for $A^n$
Inspecting $A^1 = \begin{pmatrix}1&1\\0&1\end{pmatrix}$, $A^2 = \begin{pmatrix}1&2\\0&1\end{pmatrix}$, $A^3 = \begin{pmatrix}1&3\\0&1\end{pmatrix}$, and $A^4 = \begin{pmatrix}1&4\\0&1\end{pmatrix}$, we conjecture that for every positive integer $n \in \mathbb{N}$:
$$A^n = \begin{pmatrix}1&n\\0&1\end{pmatrix}.$$

### 3. Inductive Step: Proving the Formula for $n+1$ from $n$
- **Base Case ($n=1$):** For $n=1$, the formula gives $\begin{pmatrix}1&1\\0&1\end{pmatrix} = A^1$, which is true.
- **Inductive Hypothesis:** Suppose that for a given positive integer $n$, the formula holds:
  $$A^n = \begin{pmatrix}1&n\\0&1\end{pmatrix}.$$
- **Inductive Step (for $n+1$):** By definition of matrix powers, $A^{n+1} = A^n \cdot A$. Substituting our inductive hypothesis for $A^n$ and multiplying by $A$:
  $$A^{n+1} = A^n A = \begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix} 1\cdot 1 + n\cdot 0 & 1\cdot 1 + n\cdot 1 \\ 0\cdot 1 + 1\cdot 0 & 0\cdot 1 + 1\cdot 1 \end{pmatrix} = \begin{pmatrix}1 & n+1\\0 & 1\end{pmatrix}.$$
- **Explanation:** In the matrix multiplication $\begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}$, the $(1,1)$, $(2,1)$, and $(2,2)$ entries remain $1, 0, 1$ because the second row is $(0,1)$ and the first column is $(1,0)^T$. Meanwhile, the $(1,2)$-entry is the dot product of the first row $(1, n)$ with the second column $(1, 1)^T$, which adds $1$ to $n$, producing $1\cdot 1 + n\cdot 1 = n+1$. This is the exact conjectured formula with $n$ replaced by $n+1$. By mathematical induction, the formula holds for all $n \ge 1$.

## 4. Verification and Consistency Checks

- **Additive Exponent Law Check:** According to our formula, $A^p A^q$ should equal $A^{p+q}$ for any positive integers $p, q$:
  $$A^p A^q = \begin{pmatrix}1&p\\0&1\end{pmatrix}\begin{pmatrix}1&q\\0&1\end{pmatrix} = \begin{pmatrix}1 & q+p\\0 & 1\end{pmatrix} = A^{p+q}. \quad \checkmark$$
  In particular, for $p=2, q=2$, $A^2 A^2 = \begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix} = \begin{pmatrix}1&4\\0&1\end{pmatrix} = A^4$, matching our earlier computation.
- **Extension to $n=0$ and $n=-1$:** For $n=0$, the formula gives $\begin{pmatrix}1&0\\0&1\end{pmatrix} = I = A^0$, and for $n=-1$, $\begin{pmatrix}1&-1\\0&1\end{pmatrix} = A^{-1}$ since $\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$.
