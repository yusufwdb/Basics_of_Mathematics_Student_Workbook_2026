# Exercise 3: When Can Matrices Be Multiplied?

## 1. Problem Statement

The matrix sizes are
$$A_{2\times3},\qquad B_{3\times4},\qquad C_{4\times2},\qquad D_{2\times2}.$$
For the products
$$AB,\ BA,\ BC,\ CB,\ AC,\ CA,\ AD,\ DA$$
determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

## 2. Theoretical Background and Concepts

- **Dimension Compatibility Condition for Matrix Multiplication:** Let $X$ be a matrix of size $m \times n$ and $Y$ be a matrix of size $p \times q$. The matrix product $XY$ is defined **if and only if** the number of columns of the left factor $X$ equals the number of rows of the right factor $Y$, that is:
  $$n = p \quad (\text{inner dimensions must match}).$$
- **Size of the Resulting Product:** When $n = p$, the product $XY$ has size determined by the outer dimensions:
  $$\underset{(m \times n)}{X} \cdot \underset{(n \times q)}{Y} = \underset{(m \times q)}{(XY)}.$$
- Reason: Each $(i,j)$-entry of $XY$ is the dot product of the $i$-th row of $X$ (which has $n$ entries) with the $j$-th column of $Y$ (which has $p$ entries). A dot product requires two vectors of the same length ($n=p$).

## 3. Detailed Step-by-Step Solution

We check the inner dimensions for each of the eight products:

1. **Product $AB$:** $A_{2\times 3}$ and $B_{3\times 4}$.
   - Number of columns of $A$ is $3$; number of rows of $B$ is $3$.
   - Since the inner dimensions match ($3 = 3$), **$AB$ is defined** and its size is **$2 \times 4$**.

2. **Product $BA$:** $B_{3\times 4}$ and $A_{2\times 3}$.
   - Number of columns of $B$ is $4$; number of rows of $A$ is $2$.
   - Since $4 \neq 2$, **$BA$ is undefined**.

3. **Product $BC$:** $B_{3\times 4}$ and $C_{4\times 2}$.
   - Number of columns of $B$ is $4$; number of rows of $C$ is $4$.
   - Since the inner dimensions match ($4 = 4$), **$BC$ is defined** and its size is **$3 \times 2$**.

4. **Product $CB$:** $C_{4\times 2}$ and $B_{3\times 4}$.
   - Number of columns of $C$ is $2$; number of rows of $B$ is $3$.
   - Since $2 \neq 3$, **$CB$ is undefined**.

5. **Product $AC$:** $A_{2\times 3}$ and $C_{4\times 2}$.
   - Number of columns of $A$ is $3$; number of rows of $C$ is $4$.
   - Since $3 \neq 4$, **$AC$ is undefined**.

6. **Product $CA$:** $C_{4\times 2}$ and $A_{2\times 3}$.
   - Number of columns of $C$ is $2$; number of rows of $A$ is $2$.
   - Since the inner dimensions match ($2 = 2$), **$CA$ is defined** and its size is **$4 \times 3$**.

7. **Product $AD$:** $A_{2\times 3}$ and $D_{2\times 2}$.
   - Number of columns of $A$ is $3$; number of rows of $D$ is $2$.
   - Since $3 \neq 2$, **$AD$ is undefined**.

8. **Product $DA$:** $D_{2\times 2}$ and $A_{2\times 3}$.
   - Number of columns of $D$ is $2$; number of rows of $A$ is $2$.
   - Since the inner dimensions match ($2 = 2$), **$DA$ is defined** and its size is **$2 \times 3$**.

### Summary Table

| Product | Left Size | Right Size | Inner Dimensions | Defined? | Result Size |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $AB$ | $2 \times 3$ | $3 \times 4$ | $3 = 3$ | **Yes** | $2 \times 4$ |
| $BA$ | $3 \times 4$ | $2 \times 3$ | $4 \neq 2$ | **No** | — |
| $BC$ | $3 \times 4$ | $4 \times 2$ | $4 = 4$ | **Yes** | $3 \times 2$ |
| $CB$ | $4 \times 2$ | $3 \times 4$ | $2 \neq 3$ | **No** | — |
| $AC$ | $2 \times 3$ | $4 \times 2$ | $3 \neq 4$ | **No** | — |
| $CA$ | $4 \times 2$ | $2 \times 3$ | $2 = 2$ | **Yes** | $4 \times 3$ |
| $AD$ | $2 \times 3$ | $2 \times 2$ | $3 \neq 2$ | **No** | — |
| $DA$ | $2 \times 2$ | $2 \times 3$ | $2 = 2$ | **Yes** | $2 \times 3$ |

## 4. Verification and Consistency Checks

- **Symmetry of Definedness Check:** Notice that for a pair of matrices $X_{m\times n}$ and $Y_{p\times q}$, both $XY$ and $YX$ are simultaneously defined if and only if $n = p$ AND $q = m$ (i.e., $Y$ has the transpose dimensions of $X$). Looking at our four pairs $\{A,B\}$, $\{B,C\}$, $\{A,C\}$, and $\{A,D\}$, none of these pairs have transpose dimensions of each other ($2\times 3$ vs $3\times 4$, $3\times 4$ vs $4\times 2$, $2\times 3$ vs $4\times 2$, $2\times 3$ vs $2\times 2$). Therefore, in each of the four pairs $\{XY, YX\}$, at most one direction can be defined. Indeed, in our results, exactly one product in each pair ($AB$, $BC$, $CA$, $DA$) is defined and its reverse is undefined.
- **Chain Composition Check:** Notice the chain $D_{2\times 2} A_{2\times 3} B_{3\times 4} C_{4\times 2}$. Every adjacent pair in $D \cdot A \cdot B \cdot C \cdot A$ has matching inner dimensions ($2, 3, 4, 2$), which confirms why $DA$, $AB$, $BC$, and $CA$ are the exact four defined products.
