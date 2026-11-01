# Exercise 1: Vector Operations and Their Meaning

## 1. Problem Statement

For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute
$$u+v,\qquad u-v,\qquad 3u-2v.$$
Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

## 2. Theoretical Background and Concepts

In $\mathbb{R}^3$, vectors are ordered triples of real numbers $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$. The basic linear space operations—vector addition, vector subtraction, and scalar multiplication—are defined component-wise:

1. **Vector Addition:**
   $$u + v = (u_1 + v_1,\, u_2 + v_2,\, u_3 + v_3)$$
2. **Vector Subtraction:**
   $$u - v = u + (-1)v = (u_1 - v_1,\, u_2 - v_2,\, u_3 - v_3)$$
3. **Scalar Multiplication:** For any scalar $\alpha \in \mathbb{R}$,
   $$\alpha u = (\alpha u_1,\, \alpha u_2,\, \alpha u_3)$$
4. **Linear Combination:** Combining scalar multiplication and addition gives
   $$\alpha u + \beta v = (\alpha u_1 + \beta v_1,\, \alpha u_2 + \beta v_2,\, \alpha u_3 + \beta v_3)$$

**Geometric Interpretation:**
- A vector represents a directed displacement in space (having both magnitude and direction).
- **Tip-to-tail (Triangle) Rule:** To add $u$ and $v$, we place the initial point (tail) of $v$ at the terminal point (tip) of $u$. The sum $u+v$ is the directed segment from the tail of $u$ to the tip of $v$.
- **Parallelogram Rule:** If $u$ and $v$ are placed with a common initial point, they span a parallelogram; $u+v$ is the diagonal vector starting from that common origin, while $u-v$ is the other diagonal pointing from the tip of $v$ to the tip of $u$.

## 3. Detailed Step-by-Step Solution

Given:
$$u = (2, -1, 3), \qquad v = (-1, 4, 2)$$

### Step 1: Compute $u + v$
Adding the corresponding coordinates of $u$ and $v$:
$$u + v = (2 + (-1),\, -1 + 4,\, 3 + 2) = (1, 3, 5)$$

### Step 2: Compute $u - v$
Subtracting the coordinates of $v$ from the corresponding coordinates of $u$:
$$u - v = (2 - (-1),\, -1 - 4,\, 3 - 2) = (2 + 1,\, -5,\, 1) = (3, -5, 1)$$

### Step 3: Compute $3u - 2v$
First, compute the scalar multiples $3u$ and $2v$:
$$3u = 3(2, -1, 3) = (6, -3, 9)$$
$$2v = 2(-1, 4, 2) = (-2, 8, 4)$$
Now subtract $2v$ from $3u$:
$$3u - 2v = (6 - (-2),\, -3 - 8,\, 9 - 4) = (8, -11, 5)$$

### Step 4: Geometric Explanation of Vector Addition
Geometrically, adding $u$ and $v$ means chaining two displacements one after another. Starting from a reference point $O$, moving by the displacement $u = (2, -1, 3)$ takes us to a point $A$, and then moving from $A$ by the displacement $v = (-1, 4, 2)$ takes us to a point $B$. The net displacement from the starting point $O$ directly to the final point $B$ is given by the sum vector $u + v = (1, 3, 5)$. Equivalently, if both vectors start at the origin, $u+v$ forms the main diagonal of the parallelogram spanned by $u$ and $v$.

## 4. Verification and Consistency Checks

### Verification of $(u + v) - v = u$
Using the previously computed sum $u + v = (1, 3, 5)$ and $v = (-1, 4, 2)$:
$$(u + v) - v = (1, 3, 5) - (-1, 4, 2) = (1 - (-1),\, 3 - 4,\, 5 - 2) = (2, -1, 3) = u$$
This confirms both the algebraic associativity/inverse property $(u+v)-v = u + (v-v) = u + \mathbf{0} = u$ and the accuracy of our intermediate calculation for $u+v$. Geometrially, displacing by $u$, then by $v$, and then undoing the displacement $v$ (moving by $-v$) brings us back to the exact endpoint of $u$.

### Consistency Check for $3u - 2v$
We can notice that $3u - 2v$ can also be written as $2(u - v) + u$:
$$2(u - v) + u = 2(3, -5, 1) + (2, -1, 3) = (6, -10, 2) + (2, -1, 3) = (8, -11, 5)$$
Both methods yield $(8, -11, 5)$, confirming the consistency of all three results.
