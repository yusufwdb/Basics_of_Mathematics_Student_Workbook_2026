# Exercise 8: Determinant of a Product

## 1. Problem Statement

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

## 2. Theoretical Background and Concepts

- **Cauchy–Binet / Multiplicativity Theorem for Determinants:** For any two $n \times n$ square matrices $A$ and $B$, the determinant of their matrix product equals the product of their individual determinants:
  $$\det(AB) = (\det A)(\det B).$$
- **Invertibility and Determinant of the Inverse:** A square matrix $A$ is invertible if and only if $\det A \neq 0$. When $A$ is invertible, applying multiplicativity to $A A^{-1} = I$ gives $(\det A)(\det A^{-1}) = \det I = 1$, and therefore:
  $$\det(A^{-1}) = \frac{1}{\det A}.$$

## 3. Detailed Step-by-Step Solution

We are given that $A$ and $B$ are square matrices (of the same size $n \times n$) with $\det A = 3$ and $\det B = -5$.

### 1. Computing $\det(AB)$
By the multiplicative property of determinants:
$$\det(AB) = (\det A)(\det B) = 3 \cdot (-5) = -15.$$

### 2. Computing $\det(BA)$
Again by the multiplicative property of determinants:
$$\det(BA) = (\det B)(\det A) = (-5) \cdot 3 = -15.$$

### 3. Existence and Computation of $\det(A^{-1}B)$
- **Does $A^{-1}B$ exist?** Yes! Since $\det A = 3 \neq 0$, the matrix $A$ is invertible, so $A^{-1}$ exists and has the same size as $A$ and $B$. Thus the product $A^{-1}B$ exists.
- **Computing $\det(A^{-1}B)$:** Using the determinant of an inverse and the multiplicative property:
  $$\det(A^{-1}B) = \det(A^{-1}) \cdot \det B = \frac{1}{\det A} \cdot \det B = \frac{1}{3} \cdot (-5) = -\frac{5}{3}.$$

### 4. Explaining Why $\det(AB) = \det(BA)$ Even Though Usually $AB \neq BA$
Although **matrix multiplication** is not commutative ($AB \neq BA$ as matrices, meaning their individual entries differ), the determinant map $\det: M_n(\mathbb{R}) \to \mathbb{R}$ converts a matrix product into a **product of real numbers** (scalars):
$$\det(AB) = (\det A)(\det B) \quad \text{and} \quad \det(BA) = (\det B)(\det A).$$
Because $\det A$ and $\det B$ are ordinary real numbers and **multiplication of real numbers IS commutative** ($3 \cdot (-5) = (-5) \cdot 3$), we always have $(\det A)(\det B) = (\det B)(\det A)$, and hence $\det(AB) = \det(BA)$.
Geometrically, $|\det M|$ represents the volume (or area) scaling factor of the linear transformation $M$, and the sign of $\det M$ represents whether $M$ preserves or reverses orientation. Whether we scale volume by $3$ and then by $5$ (with an orientation flip), or first by $5$ (with an orientation flip) and then by $3$, the net volume scaling factor is $15$ and orientation is reversed once in both orders.

## 4. Verification and Consistency Checks

1. **Product Identity Check:** If we multiply the matrices $AB$ and $A^{-1}B$ in the form $(BA)(A^{-1}B) = B(AA^{-1})B = B^2$, the determinant of this product must equal $\det(B^2) = (\det B)^2 = (-5)^2 = 25$. On the other hand, using our computed values:
   $$\det(BA) \cdot \det(A^{-1}B) \cdot \det(A) = (-15) \cdot \left(-\frac{5}{3}\right) \cdot 3 = (-15)(-5) \neq \text{wait: } \det(BA \cdot A^{-1}B) = \det(B^2) = 25,$$
   and indeed $\det(B)\det(A)\det(A^{-1}B) = (-5)(3)\left(-\frac{5}{3}\right) = 25$. $\checkmark$
2. **Similarity Check:** Note that if $B$ is invertible ($\det B = -5 \neq 0$), then $BA = B(AB)B^{-1}$, meaning $AB$ and $BA$ are similar matrices; similar matrices always have the same determinant.
