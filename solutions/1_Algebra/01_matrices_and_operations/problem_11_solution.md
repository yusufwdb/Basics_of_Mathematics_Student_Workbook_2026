# Exercise 11: When Do Matrices Commute?

## 1. Problem Statement

Given
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}a&b\\c&d\end{pmatrix}.$$
Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

## 2. Theoretical Background and Concepts

- **Commuting Matrices:** Two square matrices $A$ and $B$ of the same size are said to **commute** if $AB = BA$.
- **Matrix Equality:** Two $2 \times 2$ matrices are equal if and only if all four of their corresponding entries are equal:
  $$(AB)_{ij} = (BA)_{ij} \quad \text{for all } i,j \in \{1,2\}.$$
- **Centralizer of a Matrix:** The set of all matrices $B$ that commute with a fixed matrix $A$, denoted $C(A) = \{B : AB = BA\}$, forms a subspace (and subalgebra) of the space of matrices, always containing all scalar multiples of $I$ and powers of $A$.

## 3. Detailed Step-by-Step Solution

### Step 1: Compute $AB$ and $BA$
Multiplying $A$ on the left of $B$:
$$AB = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix} = \begin{pmatrix}1\cdot a + 1\cdot c & 1\cdot b + 1\cdot d\\0\cdot a + 1\cdot c & 0\cdot b + 1\cdot d\end{pmatrix} = \begin{pmatrix}a+c & b+d\\c & d\end{pmatrix}.$$
Multiplying $B$ on the left of $A$:
$$BA = \begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}a\cdot 1 + b\cdot 0 & a\cdot 1 + b\cdot 1\\c\cdot 1 + d\cdot 0 & c\cdot 1 + d\cdot 1\end{pmatrix} = \begin{pmatrix}a & a+b\\c & c+d\end{pmatrix}.$$

### Step 2: Set $AB = BA$ and Solve for the Conditions on $a, b, c, d$
Equating the two resulting matrices entry by entry:
$$\begin{pmatrix}a+c & b+d\\c & d\end{pmatrix} = \begin{pmatrix}a & a+b\\c & c+d\end{pmatrix}.$$
This gives a system of four equations corresponding to the four matrix positions:
1. Position $(1,1)$: $a + c = a \implies c = 0$.
2. Position $(1,2)$: $b + d = a + b \implies d = a$.
3. Position $(2,1)$: $c = c$ (always holds, gives no new constraint).
4. Position $(2,2)$: $d = c + d \implies c = 0$.

Notice that there is no restriction connecting $b$ to $a$; both $a$ and $b$ are free parameters in $\mathbb{R}$. Thus, the necessary and sufficient conditions on $a,b,c,d$ are:
$$c = 0 \quad \text{and} \quad d = a, \qquad \text{with } a, b \in \mathbb{R} \text{ arbitrary}.$$

### Step 3: Describe the General Form of All Matrices $B$ Commuting with $A$
Substituting $c = 0$ and $d = a$ into $B$ gives the general form:
$$B = \begin{pmatrix}a&b\\0&a\end{pmatrix}, \qquad a, b \in \mathbb{R}.$$
In words, the matrices that commute with $A$ are precisely the **$2 \times 2$ upper triangular matrices with equal entries on the main diagonal**. Equivalently, any such matrix can be written as a linear combination of the identity matrix $I$ and the nilpotent matrix $N = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ (or as a linear combination of $I$ and $A$):
$$B = a\begin{pmatrix}1&0\\0&1\end{pmatrix} + b\begin{pmatrix}0&1\\0&0\end{pmatrix} = (a-b)I + bA.$$

## 4. Verification and Consistency Checks

Let us substitute $B = \begin{pmatrix}a&b\\0&a\end{pmatrix}$ back into both products $AB$ and $BA$ to verify that they commute for all $a, b \in \mathbb{R}$:
- $$AB = \begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&b\\0&a\end{pmatrix} = \begin{pmatrix}a+0 & b+a\\0+0 & 0+a\end{pmatrix} = \begin{pmatrix}a & a+b\\0 & a\end{pmatrix}.$$
- $$BA = \begin{pmatrix}a&b\\0&a\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix} = \begin{pmatrix}a+0 & a+b\\0+0 & 0+a\end{pmatrix} = \begin{pmatrix}a & a+b\\0 & a\end{pmatrix}.$$
Since $AB = BA = \begin{pmatrix}a & a+b\\0 & a\end{pmatrix}$ for all real numbers $a$ and $b$, our characterization is verified. Furthermore, for $a=1, b=0$ we get $B=I$, and for $a=1, b=1$ we get $B=A$, both of which trivially commute with $A$.
