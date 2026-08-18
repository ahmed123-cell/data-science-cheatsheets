<div align='center'>

# ⭐Linear Algebra⭐

</div>

### 0. 🟦Introduction to Matrices

A **matrix** is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. Matrices are fundamental in linear algebra for representing linear transformations, systems of equations, and more.

#### Matrix Notation
A matrix $( A )$ of size $( m \times n )$ (m rows, n columns) is written as:

$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$

---

### 1. 🟦Matrix Addition
Two matrices can be added if they have the same dimensions. Add corresponding elements.

**Example:**
Let 
$
A = \begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}, \quad
B = \begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$

Then,
$
A + B = \begin{pmatrix}
1+5 & 2+6 \\
3+7 & 4+8
\end{pmatrix} = \begin{pmatrix}
6 & 8 \\
10 & 12
\end{pmatrix}
$

---

### 2. 🟦Matrix Subtraction
Similar to addition, subtract corresponding elements.

**Example:**
$
A - B = \begin{pmatrix}
1-5 & 2-6 \\
3-7 & 4-8
\end{pmatrix} = \begin{pmatrix}
-4 & -4 \\
-4 & -4
\end{pmatrix}
$

---

### 3. 🟦Scalar Multiplication
Multiply every element of the matrix by a scalar $( k )$.

**Example:**
$
2A = 2 \times \begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix} = \begin{pmatrix}
2 & 4 \\
6 & 8
\end{pmatrix}
$

---

### 4. 🟦Matrix Multiplication
Matrices $( A )$ (m×p) and $( B )$ (p×n) can be multiplied to get C (m×n). Each element $( c_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj} )$.

**Example:**
Let 
$
A = \begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}, \quad
B = \begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$

$
AB = \begin{pmatrix}
(1\cdot5 + 2\cdot7) & (1\cdot6 + 2\cdot8) \\
(3\cdot5 + 4\cdot7) & (3\cdot6 + 4\cdot8)
\end{pmatrix} = \begin{pmatrix}
19 & 22 \\
43 & 50
\end{pmatrix}
$

**Note:** Matrix multiplication is not commutative: $( AB \neq BA )$ in general.

---

### 5. 🟦Transpose of a Matrix
The transpose of a matrix $( A )$, denoted $( A^T )$, is obtained by swapping its rows and columns.

**Example:**
Let 
$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
$

Then,
$
A^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{pmatrix}
$

**Properties:**
- $( (A^T)^T = A )$
- $( (A + B)^T = A^T + B^T )$
- $( (AB)^T = B^T A^T )$

---

### 6. 🟦Inverse of a Matrix
The inverse of a square matrix $( A )$, denoted $( A^{-1} )$, satisfies $( A \cdot A^{-1} = I )$ (identity matrix). Not all matrices are invertible.

#### 2×2 Inverse
For a 2×2 matrix 
$
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$
the inverse is:
$
A^{-1} = \frac{1}{ad - bc} \begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$
provided the determinant $( ad - bc \neq 0 )$.

**Example:**
$
A = \begin{pmatrix}
4 & 7 \\
2 & 6
\end{pmatrix}, \quad \det(A) = 4\cdot6 - 7\cdot2 = 24 - 14 = 10
$

$
A^{-1} = \frac{1}{10} \begin{pmatrix}
6 & -7 \\
-2 & 4
\end{pmatrix} = \begin{pmatrix}
0.6 & -0.7 \\
-0.2 & 0.4
\end{pmatrix}
$

#### 3×3 Inverse (Using Minors and Cofactors)
For a 3×3 matrix, first compute the **determinant**, then the matrix of **minors**, then **cofactors**, and finally the **adjugate**.

**Step-by-step:**

Let 
$
A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
6 & 7 & 8
\end{pmatrix}
$

1. **Determinant** (using cofactor expansion along first row):
$
\det(A) = 1(4\cdot8 - 5\cdot7) - 2(0\cdot8 - 5\cdot6) + 3(0\cdot7 - 4\cdot6) = 1(-3) - 2(-30) + 3(-24) = -3 + 60 - 72 = -15
$

2. **Matrix of Minors** (M):
$
M = \begin{pmatrix}
\det\begin{pmatrix}4&5\\7&8\end{pmatrix} & \det\begin{pmatrix}0&5\\6&8\end{pmatrix} & \det\begin{pmatrix}0&4\\6&7\end{pmatrix} \\
\det\begin{pmatrix}2&3\\7&8\end{pmatrix} & \det\begin{pmatrix}1&3\\6&8\end{pmatrix} & \det\begin{pmatrix}1&2\\6&7\end{pmatrix} \\
\det\begin{pmatrix}2&3\\4&5\end{pmatrix} & \det\begin{pmatrix}1&3\\0&5\end{pmatrix} & \det\begin{pmatrix}1&2\\0&4\end{pmatrix}
\end{pmatrix}
= \begin{pmatrix}
-3 & -30 & -24 \\
-5 & -10 & -14 \\
-2 & -5 & 4
\end{pmatrix}
$

3. **Cofactor Matrix** (C): Apply sign pattern $( (-1)^{i+j} )$
$
C = \begin{pmatrix}
-3 & 30 & -24 \\
5 & -10 & 14 \\
-2 & 5 & 4
\end{pmatrix}
$

4. **Adjugate** = Transpose of C:
$
\text{adj}(A) = \begin{pmatrix}
-3 & 5 & -2 \\
30 & -10 & 5 \\
-24 & 14 & 4
\end{pmatrix}
$

5. **Inverse**:
$
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A) = \frac{1}{-15} \begin{pmatrix}
-3 & 5 & -2 \\
30 & -10 & 5 \\
-24 & 14 & 4
\end{pmatrix}
= \begin{pmatrix}
0.2 & -1/3 & 2/15 \\
-2 & 2/3 & -1/3 \\
1.6 & -14/15 & -4/15
\end{pmatrix}
$

**Note:** Always verify by multiplying $( A \cdot A^{-1} = I )$.

---

### 7. 🟦Systems of Linear Equations

A system of linear equations can be represented in matrix form as $( AX = B )$, where:
- $( A )$ is the coefficient matrix,
- $( X )$ is the column vector of variables,
- $( B )$ is the column vector of constants.

**Example:**

Solve the following system:
$
\begin{cases}
x + 2y + 3z = 14 \\
2x + 3y + 4z = 20 \\
3x + 4y + 5z = 26
\end{cases}
$

In matrix form:
$
\begin{pmatrix}
1 & 2 & 3 \\
2 & 3 & 4 \\
3 & 4 & 5
\end{pmatrix}
$
$
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
$


=
$
\begin{pmatrix}
14 \\
20 \\
26
\end{pmatrix}
$

**Solution using Matrix Inverse (A is invertible):**

Let $ A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{pmatrix}$, $B = \begin{pmatrix} 14 \\ 20 \\ 26 \end{pmatrix}$.

First, find $( A^{-1} )$ (using the method from the previous section), then:
$
X = A^{-1} B
$


**Verification Example Result:**
The solution to this system is $( x = 2 )$, $( y = 3 )$, $( z = 1 )$.

---

**Example2:**

Solve:
$
\begin{cases}
x + 2y = 5 \\
3x + 4y = 11
\end{cases}
$

Matrix form:
$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad
B = \begin{pmatrix} 5 \\ 11 \end{pmatrix}
$

Determinant = $( 1\cdot4 - 2\cdot3 = -2 )$

$
A^{-1} = \frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix}
$

$
X = A^{-1} B = \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \begin{pmatrix} 5 \\ 11 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$

So, $( x = 1 )$, $( y = 2 )$.

---

### 8. 🟦Vectors
A **vector** is a quantity with both magnitude and direction. In linear algebra, vectors are often represented as column matrices or ordered lists of numbers.

**Example:**
A vector in $(\mathbb{R}^3)$:
$
\mathbf{v} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}
$

Vectors can be added, subtracted, and scaled just like matrices.

---

### 9. 🟦Linear Combinations
A **linear combination** of vectors $(\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k)$ is an expression of the form:
$
c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k
$
where $( c_1, c_2, \dots, c_k )$ are scalars.

**Example:**
Let 
$
\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad 
\mathbf{v}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.
$

A linear combination: $( 3\mathbf{v}_1 + 2\mathbf{v}_2 = \begin{pmatrix} 3 \\ 2 \end{pmatrix} )$

---

### 10. 🟦Span
The **span** of a set of vectors is the set of all possible linear combinations of those vectors.

**Example:**
The span of $(\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix})$ and $(\mathbf{v}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix})$ is the entire plane $(\mathbb{R}^2)$.

---

### 11. 🟦Linear Independence
A set of vectors is **linearly independent** if the only linear combination that equals the zero vector is the trivial one (all coefficients = 0). Otherwise, they are **linearly dependent**.

**Example:**
- $(\begin{pmatrix} 1 \\ 0 \end{pmatrix})$ and $(\begin{pmatrix} 0 \\ 1 \end{pmatrix})$ are linearly independent.
- $(\begin{pmatrix} 1 \\ 2 \end{pmatrix})$ and $(\begin{pmatrix} 2 \\ 4 \end{pmatrix})$ are linearly dependent (second is 2× first).

**Test:** Solve $( c_1\mathbf{v}_1 + c_2\mathbf{v}_2 = \mathbf{0})$. Only solution $( c_1 = c_2 = 0 )$ means independent.

---

### 12. 🟦Subspace
A **subspace** of a vector space is a subset that is closed under vector addition and scalar multiplication, and contains the zero vector.

**Examples:**
- The set of all vectors of the form $(\begin{pmatrix} x \\ 2x \end{pmatrix})$ is a subspace of $(\mathbb{R}^2)$.
- Any plane through the origin in $(\mathbb{R}^3)$ is a subspace.

---

### 13. 🟦Basis
A **basis** for a vector space is a linearly independent set of vectors that spans the entire space.

**Example:**
The **standard basis** for $(\mathbb{R}^2)$:
$
\left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}
$

The dimension of the space is the number of vectors in any basis.

**Note:** Every vector in the space can be uniquely expressed as a linear combination of the basis vectors.

---

### 14. 🟦Vector Dot Product (Inner Product)
The **dot product** of two vectors $(\mathbf{u} = (u_1, u_2, \dots, u_n))$ and $(\mathbf{v} = (v_1, v_2, \dots, v_n))$ is:
$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \dots + u_n v_n
$

**Example:**
$
\mathbf{u} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}, \quad
\mathbf{v} = \begin{pmatrix} 1 \\ 5 \\ 2 \end{pmatrix}
$
$
\mathbf{u} \cdot \mathbf{v} = 2\cdot1 + 3\cdot5 + 4\cdot2 = 2 + 15 + 8 = 25
$

**Properties:** Commutative, distributive, and $\mathbf{u} \cdot \mathbf{u} = \|\mathbf{u}\|^2$.

---

### 15. 🟦Length (Norm) of a Vector
The **Euclidean length** (or norm) of a vector $\mathbf{v}$ is:
$
\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}
$

**Example:**
$
\|\mathbf{u}\| = \sqrt{2^2 + 3^2 + 4^2} = \sqrt{4 + 9 + 16} = \sqrt{29} \approx 5.385
$

A **unit vector** has length 1. You can normalize a vector by dividing it by its norm: $\hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}$.

---

### 16. 🟦Cauchy-Schwarz Inequality
For any vectors $\mathbf{u}$ and $\mathbf{v}$:
$
|\mathbf{u} \cdot \mathbf{v}| \leq \|\mathbf{u}\| \|\mathbf{v}\|
$

Equality holds when the vectors are linearly dependent (parallel).

**Example:**
For the vectors above: $ |25| \leq \sqrt{29} \cdot \sqrt{1+25+4} = \sqrt{29} \cdot \sqrt{30} \approx 5.385 \times 5.477 \approx 29.5 $

25 ≤ 29.5 (true).

---

### 17. 🟦Triangle Inequality for Vectors
The length of the sum of two vectors is at most the sum of their lengths:
$
\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|
$

This is the vector version of the triangle inequality in geometry.

**Example:**
$
\|\mathbf{u} + \mathbf{v}\| = \left\| \begin{pmatrix} 3 \\ 8 \\ 6 \end{pmatrix} \right\| = \sqrt{9 + 64 + 36} = \sqrt{109} \approx 10.44
$
$
\|\mathbf{u}\| + \|\mathbf{v}\| \approx 5.385 + 5.477 \approx 10.86
$
10.44 ≤ 10.86 (true).

---

### 18. 🟦Angle Between Two Vectors
The angle $\theta$ between two non-zero vectors is given by:
$
\cos \theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}
$

**Example:**
For $\mathbf{u}$ and $\mathbf{v}$ above:
$
\cos \theta = \frac{25}{\sqrt{29} \cdot \sqrt{30}} \approx \frac{25}{29.5} \approx 0.847 \quad \Rightarrow \quad \theta \approx \cos^{-1}(0.847) \approx 32^\circ
$

- If $\mathbf{u} \cdot \mathbf{v} = 0$, the vectors are **orthogonal** ($\theta = 90^\circ$).

---

### 19. 🟦Reduced Row Echelon Form
A special form of matrix obtained through elementary row operations. Its purpose is ot simplify the matrix into a form that ca be read and analyzed, especially when solving system of linear equations

##### Properties:
- **Leading entry (pivot)**: In every nonzero row, the first nonzero element is called the pivot, and it must be (1)

- **Position of the pivot**: The pivot of each row must be in a column to the right of the pivot in the row above

- **Pivot columns**: Every column that contains must have all its other elements equals to zero

- **zero rows**: Any row consisting entirely of zeros must be at the bottom of the matrix

##### [**Example Video**](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/matrices-elimination/v/matrices-reduced-row-echelon-form-3)

---

### 20. 🟦Null Space, Column Space, Rank, and Nullity

#### Null Space (Kernel)
The **null space** (or kernel) of a matrix $( A )$, denoted $( \text{Nul}(A) )$, is the set of all vectors $( \mathbf{x} )$ such that $( A\mathbf{x} = \mathbf{0} )$.

**Example:**
Let 
$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6
\end{pmatrix}
$

Solving $( A\mathbf{x} = \mathbf{0} )$ gives the null space:

$$
\operatorname{Null}(A)
=
\operatorname{span}
\left\{
\begin{pmatrix}
-2\\
1\\
0
\end{pmatrix},
\begin{pmatrix}
-3\\
0\\
1
\end{pmatrix}
\right\}
$$

#### 🟦Column Space
The **column space** of $( A )$, denoted $( \text{Col}(A) )$, is the span of all column vectors of $( A )$. It is the set of all possible linear combinations of the columns.

**Example:**
For the matrix $( A )$ above, the column space is spanned by the first two columns (the third is a multiple of the first):
$
\text{Col}(A) = \text{span} \left\{ \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \begin{pmatrix} 2 \\ 4 \end{pmatrix} \right\} = \text{span} \left\{ \begin{pmatrix} 1 \\ 2 \end{pmatrix} \right\}
$

#### 🟦Rank and Nullity (Dimension Theorem)
- The **rank** of $( A )$, denoted $( \text{rank}(A) )$, is the dimension of the column space (number of linearly independent columns).
- The **nullity** of $( A )$ is the dimension of the null space (number of free variables in the solution to $( A\mathbf{x} = \mathbf{0} )$).

**Rank-Nullity Theorem:**
For an $( m \times n )$ matrix $( A )$:
$
\text{rank}(A) + \text{nullity}(A) = n
$

**Example (continued):**
- $( \text{rank}(A) = 1 )$ (one linearly independent column)
- $( \text{nullity}(A) = 2 )$ (two free variables)
- Check: $( 1 + 2 = 3 )$ (number of columns)

These concepts are fundamental for understanding the structure of linear transformations and solving systems of equations.

---

### 21. 🟦Linear Transformations
A **linear transformation** $( T: V \to W )$ is a function between two vector spaces that preserves addition and scalar multiplication:
$
T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}), \quad T(c\mathbf{u}) = c T(\mathbf{u})
$

Linear transformations can be represented by matrices. If $( T(\mathbf{x}) = A\mathbf{x} )$, then $( A )$ is the **standard matrix** of $( T )$.

**Example:**
Rotation by 90° counterclockwise in $(\mathbb{R}^2)$:
$
T\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -y \\ x \end{pmatrix}
$
Standard matrix:
$
A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$

---

### 22. 🟦Projection onto a Line
The **projection** of a vector $(\mathbf{v})$ onto a nonzero vector $(\mathbf{u})$ (onto the line spanned by $(\mathbf{u})$) is:
$
\text{proj}_{\mathbf{u}} \mathbf{v} = \left( \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \right) \mathbf{u}
$

**Example:**
Let $(\mathbf{u} = \begin{pmatrix} 3 \\ 4 \end{pmatrix})$, $(\mathbf{v} = \begin{pmatrix} 1 \\ 2 \end{pmatrix})$.

$
\mathbf{v} \cdot \mathbf{u} = 3\cdot1 + 4\cdot2 = 11, \quad \mathbf{u} \cdot \mathbf{u} = 9 + 16 = 25
$

$
\text{proj}_{\mathbf{u}} \mathbf{v} = \frac{11}{25} \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 33/25 \\ 44/25 \end{pmatrix} = \begin{pmatrix} 1.32 \\ 1.76 \end{pmatrix}
$

---

### 23. 🟦Projection onto a Subspace
For a general basis, use the formula involving the matrix whose columns are the basis vectors.
$$
\operatorname{proj}_W(b)
=
A(A^T A)^{-1}A^T b
$$

**Example**

Project $(\mathbf{b} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix})$ onto the subspace $( W )$ spanned by the columns of matrix
$
A = \begin{pmatrix}
1 & 1 \\
1 & 0 \\
0 & 1
\end{pmatrix}
$


Compute projection:
$
\operatorname{proj}_W(\mathbf{b}) = A \left[ (A^T A)^{-1} A^T \mathbf{b} \right]
= \begin{pmatrix}
1 & 1 \\
1 & 0 \\
0 & 1
\end{pmatrix}
\cdot \frac{1}{3} \begin{pmatrix}
1 & 2 & -1 \\
1 & -1 & 2
\end{pmatrix}
\begin{pmatrix}
1 \\ 2 \\ 3
\end{pmatrix}
$


**Result:** The projection is $( \begin{pmatrix} 7/3 \\ 2/3 \\ 5/3 \end{pmatrix} \approx \begin{pmatrix} 2.333 \\ 0.667 \\ 1.667 \end{pmatrix} )$.

---

### 24. 🟦Least Squares Approximation (Normal Equations)

When a system $( A\mathbf{x} = \mathbf{b} )$ has no exact solution (inconsistent system), the **least squares solution** $(\hat{\mathbf{x}})$ minimizes the error $( \| A\mathbf{x} - \mathbf{b} \|^2 )$.

The solution satisfies the **normal equations**:
$
A^T A \hat{\mathbf{x}} = A^T \mathbf{b}
$

This is equivalent to projecting $(\mathbf{b})$ onto the column space of $( A )$, i.e., $( A\hat{\mathbf{x}} = \operatorname{proj}_{\text{Col}(A)} \mathbf{b} )$.

**Example:**

Find the least squares solution to the inconsistent system:
$
\begin{cases}
x + y = 1 \\
x + 2y = 2 \\
x + 3y = 4
\end{cases}
$

In matrix form:
$
A = \begin{pmatrix}
1 & 1 \\
1 & 2 \\
1 & 3
\end{pmatrix}, \quad
\mathbf{b} = \begin{pmatrix}
1 \\ 2 \\ 4
\end{pmatrix}
$


Solve the normal equation $( A^T A \hat{\mathbf{x}} = A^T \mathbf{b})$:

$
\begin{pmatrix}
3 & 6 \\
6 & 14
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
= \begin{pmatrix}
7 \\ 17
\end{pmatrix}
$

The solution is $( \hat{x} \approx 0.4 )$, $( \hat{y} \approx 1.1 )$.

The least squares line is approximately $( y = 0.4 + 1.1x )$, which best fits the three points in the least squares sense.

---

### 25. 🟦Orthogonality and Orthonormal Basis

#### Orthogonality
Two vectors $(\mathbf{u})$ and $(\mathbf{v})$ are **orthogonal** if their dot product is zero:
$
\mathbf{u} \cdot \mathbf{v} = 0
$

A set of vectors is orthogonal if every pair is orthogonal. Orthogonal vectors are linearly independent.

**Example:**
$
\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \quad
\mathbf{v} = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}
$
$
\mathbf{u} \cdot \mathbf{v} = 1(-2) + 2(1) + 3(0) = -2 + 2 + 0 = 0
$
(They are orthogonal.)

#### Orthonormal Basis
A basis is **orthonormal** if:
- All vectors are orthogonal to each other, **and**
- Each vector has unit length ($(\|\mathbf{u}_i\| = 1)$).

**Example (Standard Orthonormal Basis for $(\mathbb{R}^3)$):**
$
\left\{ \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \mathbf{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\}
$

**Advantages of Orthonormal Basis:**
- Coordinates of any vector $(\mathbf{v})$ are easy to find: $( c_i = \mathbf{v} \cdot \mathbf{u}_i )$
- Projection onto the subspace is simply: $(\sum (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i)$

**Gram-Schmidt Process** (mentioned for completeness): A method to convert any basis into an orthonormal basis.

---

### 26. 🟦Eigenvalues and Eigenvectors

An **eigenvector** of a square matrix $( A )$ is a non-zero vector $(\mathbf{v})$ such that when $( A )$ is multiplied by $(\mathbf{v})$, the result is a scalar multiple of $(\mathbf{v})$. That scalar is called the **eigenvalue** $(\lambda)$:

$
A \mathbf{v} = \lambda \mathbf{v}
$

**How to find them:**
Solve the characteristic equation:
$
\det(A - \lambda I) = 0
$

**Example:**
Let 
$
A = \begin{pmatrix}
3 & 1 \\
0 & 2
\end{pmatrix}
$

Characteristic equation:
$
\det\begin{pmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{pmatrix} = (3-\lambda)(2-\lambda) = 0
$
Eigenvalues: $(\lambda_1 = 3)$, $(\lambda_2 = 2)$

For $(\lambda = 3)$:
$
(A - 3I)\mathbf{v} = 0 \quad \Rightarrow \quad \mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}
$

For $(\lambda = 2)$:
$
\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$

Eigenvalues and eigenvectors are crucial for understanding linear transformations, diagonalization, and stability analysis.

---

### 27. 🟦Singular Value Decomposition (SVD)

The **Singular Value Decomposition** factorizes any $( m \times n )$ matrix $( A )$ as:
$
A = U \Sigma V^T
$

Where:
- $( U )$ is an $( m \times m )$ orthogonal matrix (left singular vectors),
- $( \Sigma )$ is an $( m \times n )$ diagonal matrix with non-negative **singular values** on the diagonal (sorted descending),
- $( V )$ is an $( n \times n )$ orthogonal matrix (right singular vectors).

**Key Applications:**
- Least squares solutions
- Data compression and dimensionality reduction (PCA)
- Image compression
- Pseudoinverse: $( A^+ = V \Sigma^+ U^T )$

**Simple Example (2×2):**
For 
$
A = \begin{pmatrix}
3 & 1 \\
1 & 3
\end{pmatrix}
$

The SVD yields singular values $(\sigma_1 = 4)$, $(\sigma_2 = 2)$, with corresponding orthogonal matrices $( U )$ and $( V )$.

SVD is one of the most important and widely used matrix factorizations in applied mathematics and machine learning.