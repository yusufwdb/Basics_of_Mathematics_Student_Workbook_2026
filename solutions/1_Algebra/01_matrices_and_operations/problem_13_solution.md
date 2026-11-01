# Exercise 13: A Recurrence Written in Matrix Form

## 1. Problem Statement

Let
$$F=\begin{pmatrix}1&1\\1&0\end{pmatrix}.$$
Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence
$$0,1,1,2,3,5,8,\ldots$$
and describe the relationship you observe. Then compute
$$F\begin{pmatrix}a\\b\end{pmatrix}$$
and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

## 2. Theoretical Background and Concepts

- **The Fibonacci Sequence:** Defined by initial values $f_0 = 0$, $f_1 = 1$, and the second-order linear recurrence relation
  $$f_{n+1} = f_n + f_{n-1} \quad \text{for } n \ge 1.$$
  Its first terms are $f_0 = 0,\ f_1 = 1,\ f_2 = 1,\ f_3 = 2,\ f_4 = 3,\ f_5 = 5,\ f_6 = 8, \ldots$
- **Companion Matrix of a Linear Recurrence:** A multi-step scalar recurrence can be converted into a first-order vector recurrence $v_{n} = F v_{n-1}$ by stacking consecutive terms into a state vector $v_{n-1} = \begin{pmatrix}f_n\\f_{n-1}\end{pmatrix}$. Repeatedly applying $F$ then yields $v_n = F^n v_0$.

## 3. Detailed Step-by-Step Solution

### 1. Computing $F^2$, $F^3$, $F^4$, and $F^5$
- **$F^2 = F \cdot F$:**
  $$F^2 = \begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix} = \begin{pmatrix}1+1 & 1+0\\1+0 & 1+0\end{pmatrix} = \begin{pmatrix}2&1\\1&1\end{pmatrix}.$$
- **$F^3 = F^2 \cdot F$:**
  $$F^3 = \begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix} = \begin{pmatrix}2+1 & 2+0\\1+1 & 1+0\end{pmatrix} = \begin{pmatrix}3&2\\2&1\end{pmatrix}.$$
- **$F^4 = F^3 \cdot F$:**
  $$F^4 = \begin{pmatrix}3&2\\2&1\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix} = \begin{pmatrix}3+2 & 3+0\\2+1 & 2+0\end{pmatrix} = \begin{pmatrix}5&3\\3&2\end{pmatrix}.$$
- **$F^5 = F^4 \cdot F$:**
  $$F^5 = \begin{pmatrix}5&3\\3&2\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix} = \begin{pmatrix}5+3 & 5+0\\3+2 & 3+0\end{pmatrix} = \begin{pmatrix}8&5\\5&3\end{pmatrix}.$$

### 2. Comparison with the Fibonacci Sequence $0, 1, 1, 2, 3, 5, 8, \ldots$
Labeling the sequence as $f_0=0, f_1=1, f_2=1, f_3=2, f_4=3, f_5=5, f_6=8$, we compare the entries of $F^n$ for $n=1,2,3,4,5$:
$$F^1 = \begin{pmatrix}f_2&f_1\\f_1&f_0\end{pmatrix} = \begin{pmatrix}1&1\\1&0\end{pmatrix}, \quad F^2 = \begin{pmatrix}f_3&f_2\\f_2&f_1\end{pmatrix} = \begin{pmatrix}2&1\\1&1\end{pmatrix}, \quad F^3 = \begin{pmatrix}f_4&f_3\\f_3&f_2\end{pmatrix} = \begin{pmatrix}3&2\\2&1\end{pmatrix},$$
$$F^4 = \begin{pmatrix}f_5&f_4\\f_4&f_3\end{pmatrix} = \begin{pmatrix}5&3\\3&2\end{pmatrix}, \quad F^5 = \begin{pmatrix}f_6&f_5\\f_5&f_4\end{pmatrix} = \begin{pmatrix}8&5\\5&3\end{pmatrix}.$$
**Observed Relationship:** Every power $F^n$ ($n \ge 1$) is a symmetric $2 \times 2$ matrix whose entries are three consecutive Fibonacci numbers:
$$F^n = \begin{pmatrix} f_{n+1} & f_n \\ f_n & f_{n-1} \end{pmatrix}.$$

### 3. Computing $F\begin{pmatrix}a\\b\end{pmatrix}$ and Explaining the Recurrence Step
Multiplying $F$ by the column vector $\begin{pmatrix}a\\b\end{pmatrix}$:
$$F\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix} 1\cdot a + 1\cdot b \\ 1\cdot a + 0\cdot b \end{pmatrix} = \begin{pmatrix}a+b\\a\end{pmatrix}.$$
**How this performs one recurrence step:**
Suppose $b = f_{n-1}$ and $a = f_n$ are two consecutive terms of the Fibonacci sequence, stored in the state vector $\begin{pmatrix}f_n\\f_{n-1}\end{pmatrix}$. When we multiply by $F$:
1. The **first row** $(1, 1)$ takes the sum of both entries, producing the new top entry $a + b = f_n + f_{n-1} = f_{n+1}$ (the next term in the sequence).
2. The **second row** $(1, 0)$ selects the old top entry $a = f_n$ and shifts it down to the bottom position so that it is preserved in memory for the subsequent step, while discarding the oldest term $b = f_{n-1}$.
Thus, $\begin{pmatrix}f_n\\f_{n-1}\end{pmatrix} \xrightarrow{\text{multiply by } F} \begin{pmatrix}f_{n+1}\\f_n\end{pmatrix}$, advancing the recurrence window forward by exactly one index.

## 4. Verification and Consistency Checks

1. **Cassini's Identity via Determinants:** Since $\det(F) = 1\cdot 0 - 1\cdot 1 = -1$, we must have $\det(F^n) = (\det F)^n = (-1)^n$. Checking our computed matrices:
   - $\det(F^2) = 2(1) - 1(1) = 1 = (-1)^2$
   - $\det(F^3) = 3(1) - 2(2) = -1 = (-1)^3$
   - $\det(F^4) = 5(2) - 3(3) = 1 = (-1)^4$
   - $\det(F^5) = 8(3) - 5(5) = -1 = (-1)^5$. $\checkmark$
   (This also proves Cassini's identity: $f_{n+1}f_{n-1} - f_n^2 = (-1)^n$.)
2. **Consistency of $F^2 \cdot F^3 = F^5$:**
   $$F^2 F^3 = \begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}3&2\\2&1\end{pmatrix} = \begin{pmatrix}6+2 & 4+1\\3+2 & 2+1\end{pmatrix} = \begin{pmatrix}8&5\\5&3\end{pmatrix} = F^5. \quad \checkmark$$
