# Exercise 14: A Small Change in the Right-Hand Side

## 1. Problem Statement
Compare the systems
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3\end{cases}$$
and
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3.1.\end{cases}$$
Check the consistency of each system and explain why a small change in one number can change the type of the system.

## 2. Theoretical Background and Concepts
A system of $m = 3$ linear equations in $n = 2$ unknowns ($x$ and $y$) is called an **overdetermined system** because there are more equations (constraints) than unknowns.
- **Algebraic Perspective:** The first two independent equations already uniquely fix the values of $(x, y)$. For the entire three-equation system to be **consistent**, the third equation must be satisfied by that exact same pair $(x, y)$. Notice here that adding the left-hand sides of the first two equations gives $(x+y) + (2x-y) = 3x$, which is the exact left-hand side of the third equation! Therefore, the system is consistent **if and only if** the third right-hand side equals the sum of the first two right-hand sides ($2 + 1 = 3$).
- **Geometric Perspective:** In the plane $\mathbb{R}^2$, each equation represents a straight line. Two non-parallel lines intersect at a single point $P$. A third line will pass through that exact point $P$ only if its constant term is tuned precisely; shifting the third line by even a tiny amount (such as $0.1$) moves it off the intersection point $P$, leaving no point common to all three lines.

## 3. Detailed Step-by-Step Solution

### Part 1: Analyze the First System
$$\begin{cases}
x + y = 2, \\
2x - y = 1, \\
3x = 3.
\end{cases}$$
1. **Augmented Matrix Elimination:**
   $$\left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   2 & -1 & 1 \\
   3 & 0 & 3
   \end{array}\right]
   \xrightarrow{\substack{R_2 \leftarrow R_2 - 2R_1 \\ R_3 \leftarrow R_3 - 3R_1}}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & -3 & -3 \\
   0 & -3 & -3
   \end{array}\right]
   \xrightarrow{R_3 \leftarrow R_3 - R_2}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & -3 & -3 \\
   0 & 0 & 0
   \end{array}\right].$$
2. **Consistency and Solution:**
   The third row reduces to $0 = 0$ (no contradiction). From Row 2, $-3y = -3 \implies y = 1$, and from Row 1, $x = 2 - y = 1$.
   Thus, the first system is **consistent** and has the **unique solution $(x, y) = (1, 1)$**.
   *(Notice also directly that adding Equation 1 and Equation 2 gives $(x+y) + (2x-y) = 2 + 1 \implies 3x = 3$, which matches Equation 3 identically.)*

---

### Part 2: Analyze the Second System
$$\begin{cases}
x + y = 2, \\
2x - y = 1, \\
3x = 3.1.
\end{cases}$$
1. **Augmented Matrix Elimination:**
   $$\left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   2 & -1 & 1 \\
   3 & 0 & 3.1
   \end{array}\right]
   \xrightarrow{\substack{R_2 \leftarrow R_2 - 2R_1 \\ R_3 \leftarrow R_3 - 3R_1}}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & -3 & -3 \\
   0 & -3 & -2.9
   \end{array}\right]
   \xrightarrow{R_3 \leftarrow R_3 - R_2}
   \left[\begin{array}{cc|c}
   1 & 1 & 2 \\
   0 & -3 & -3 \\
   0 & 0 & 0.1
   \end{array}\right].$$
2. **Consistency:**
   The third row is $[0 \;\; 0 \mid 0.1]$, which translates to the contradictory equation $0x + 0y = 0.1$ ($0 = 0.1$).
   Thus, the second system is **inconsistent** and has **no solution**.

---

### Part 3: Explanation of Why a Small Change Changes the System Type
1. **Exact Dependency Among Left-Hand Sides:** In both systems, the left-hand side of the third equation is the exact sum of the first two left-hand sides:
   $$L_3 = 3x = (x + y) + (2x - y) = L_1 + L_2.$$
   Consequently, the first two equations **force** $3x$ to equal $2 + 1 = 3$ for any solution $(x,y)$. Consistency requires the exact equality $b_3 = b_1 + b_2 = 3$. Even an arbitrarily small perturbation $b_3 = 3 + \varepsilon$ (here $\varepsilon = 0.1 \neq 0$) violates this exact equality and creates the contradiction $0 = \varepsilon$.
2. **Geometric Picture in $\mathbb{R}^2$:** The first two lines $x + y = 2$ and $2x - y = 1$ intersect at the single point $P = (1, 1)$. In the first system, the third vertical line $3x = 3 \iff x = 1$ passes directly through $P = (1, 1)$ (the three lines are *concurrent*). Changing $3$ to $3.1$ shifts the vertical line slightly to the right to $x = \frac{3.1}{3} = 1.0\overline{3}$, so it misses the intersection point $(1, 1)$ of the first two lines, leaving no point that lies on all three lines simultaneously.

## 4. Verification and Consistency Checks
- Substituting $(x, y) = (1, 1)$ into the three equations:
  - Equation 1: $1 + 1 = 2 \quad \checkmark$
  - Equation 2: $2(1) - 1 = 1 \quad \checkmark$
  - Equation 3 of System 1: $3(1) = 3 \quad \checkmark$
  - Equation 3 of System 2: $3(1) = 3 \neq 3.1 \quad \times$
- Rank Check: For System 1, $\operatorname{rank}(A) = \operatorname{rank}([A \mid b_1]) = 2$ (consistent, unique solution). For System 2, $\operatorname{rank}(A) = 2 < 3 = \operatorname{rank}([A \mid b_2])$ (inconsistent).
