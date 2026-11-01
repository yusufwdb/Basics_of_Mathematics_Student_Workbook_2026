# Exercise 14: Closest Point on a Line

## 1. Problem Statement

Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

## 2. Theoretical Background and Concepts

1. **Orthogonal Projection and Minimum Distance:**
   Let $L = \{tv : t \in \mathbb{R}\}$ be a line passing through the origin $O=(0,0)$ with direction vector $v \neq \mathbf{0}$, and let $P$ be a point with position vector $p = \overrightarrow{OP}$.
   For any point $X = tv$ on the line $L$, we can decompose $\overrightarrow{XP} = p - tv$ using the orthogonal projection $Q = \operatorname{proj}_v p$:
   $$p - tv = (p - Q) + (Q - tv)$$
   Since $p - Q \perp v$ and $Q - tv$ is parallel to $v$, the Pythagorean theorem gives:
   $$\|p - tv\|^2 = \|p - Q\|^2 + \|Q - tv\|^2 \ge \|p - Q\|^2$$
   with equality if and only if $tv = Q = \operatorname{proj}_v p$.

2. **Formulas:**
   - **Closest point on $L$:** $Q = \operatorname{proj}_v p = \left(\frac{p \cdot v}{v \cdot v}\right) v$
   - **Perpendicular connecting vector:** $\overrightarrow{QP} = p - Q$
   - **Distance from $P$ to $L$:** $d(P, L) = \|\overrightarrow{QP}\| = \|p - \operatorname{proj}_v p\|$

## 3. Detailed Step-by-Step Solution

Given:
$$P = (4, 1) \implies p = \overrightarrow{OP} = (4, 1), \qquad v = (1, 2)$$

### Step 1: Find the closest point $Q$ on the line using orthogonal projection
Compute the dot products $p \cdot v$ and $v \cdot v$:
$$p \cdot v = (4)(1) + (1)(2) = 4 + 2 = 6$$
$$v \cdot v = \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5$$
Therefore, the orthogonal projection of $p$ onto $v$ is:
$$\overrightarrow{OQ} = \operatorname{proj}_v p = \frac{p \cdot v}{v \cdot v}\, v = \frac{6}{5}(1, 2) = \left(\frac{6}{5},\, \frac{12}{5}\right) = (1.2,\, 2.4)$$
Thus, the closest point on the line to $P$ is:
$$Q = \left(\frac{6}{5},\, \frac{12}{5}\right)$$

### Step 2: Find the distance from $P$ to the line
First, construct the vector $\overrightarrow{QP}$ connecting the closest point $Q$ on the line to $P$:
$$\overrightarrow{QP} = P - Q = (4, 1) - \left(\frac{6}{5},\, \frac{12}{5}\right) = \left(\frac{20}{5} - \frac{6}{5},\, \frac{5}{5} - \frac{12}{5}\right) = \left(\frac{14}{5},\, -\frac{7}{5}\right)$$
Now compute its length to obtain the distance from $P$ to the line:
$$d(P, L) = \left\|\overrightarrow{QP}\right\| = \sqrt{\left(\frac{14}{5}\right)^2 + \left(-\frac{7}{5}\right)^2} = \frac{1}{5}\sqrt{196 + 49} = \frac{\sqrt{245}}{5} = \frac{7\sqrt{5}}{5} \approx 3.1305$$

### Step 3: Verify that $\overrightarrow{QP}$ is perpendicular to the direction of the line
Compute the dot product of $\overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$ with the direction vector $v = (1, 2)$:
$$\overrightarrow{QP} \cdot v = \left(\frac{14}{5}\right)(1) + \left(-\frac{7}{5}\right)(2) = \frac{14}{5} - \frac{14}{5} = 0 \quad \checkmark$$
Since $\overrightarrow{QP} \cdot v = 0$, the segment $QP$ is perpendicular to the line $L$.

## 4. Verification and Consistency Checks

1. **Check that $Q$ lies on the line $L$:**
   The line through the origin with direction $v = (1, 2)$ has equation $y = 2x$ (or $2x - y = 0$). For $Q = \left(\frac{6}{5}, \frac{12}{5}\right)$:
   $$2\left(\frac{6}{5}\right) - \frac{12}{5} = \frac{12}{5} - \frac{12}{5} = 0 \quad \checkmark$$
2. **Check the distance using the point-to-line distance formula for $2x - y = 0$:**
   For the line $2x - y = 0$ and point $P = (4, 1)$:
   $$d(P, L) = \frac{|2(4) - 1(1)|}{\sqrt{2^2 + (-1)^2}} = \frac{|8 - 1|}{\sqrt{5}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5} \quad \checkmark$$
   Both methods give the exact same distance $\frac{7\sqrt{5}}{5}$.
