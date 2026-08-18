<div align='center'>

# ⭐ Calculus ⭐

</div>

- [🟦 Limits](#-limits)
- [🟦 Trigonometric Identities and Rules](#-trigonometric-identities-and-rules)
- [🟦 Derivatives](#-derivatives)
- [🟦 Maxima and Minima Using Derivatives](#-maxima-and-minima-using-derivatives)
- [🟦 Indefinite Integrals](#-indefinite-integrals)
- [🟦 Definite Integrals](#-definite-integrals)
- [🟦 Partial Derivatives and Gradient](#-partial-derivatives-and-gradient)

<div align='center'>

## 🟦 Limits

</div>

### What is a Limit?
The **limit** of a function $f(x)$ as $x$ approaches a value $a$ (denoted $\lim_{x \to a} f(x) = L$) is the value $L$ that the function approaches as $x$ gets arbitrarily close to $a$, even if $f(a)$ is not defined or different.

Limits are foundational in calculus because they allow us to study:
- Instantaneous rates of change (derivatives)
- Accumulation of quantities (integrals)
- Behavior of functions near points of discontinuity or at infinity

**Key Ideas:**
- **One-sided limits**: Right-hand ($\lim_{x \to a^+}$) and left-hand ($\lim_{x \to a^-}$)
- **Limits at infinity**: Behavior as $x \to \infty$ or $x \to -\infty$
- **Indeterminate forms**: Common ones are $\frac{0}{0}$, $\frac{\infty}{\infty}$, $\infty - \infty$, etc.
- **Continuity**: If $\lim_{x \to a} f(x) = f(a)$, the function is continuous at $x = a$.

### Solved Examples

#### 1. $\lim_{x \to 1} \frac{x-1}{x-1}$
**Direct substitution** gives $\frac{0}{0}$ (indeterminate).

For $x \neq 1$, $\frac{x-1}{x-1} = 1$.

Therefore,
$$
\lim_{x \to 1} \frac{x-1}{x-1} = 1
$$
(Note: The function is undefined at $x=1$, but the limit exists.)

---

#### 2. $\lim_{x \to 3} \frac{x^2 - 6x + 9}{x^2 - 9}$
Factor numerator and denominator:

Numerator: $x^2 - 6x + 9 = (x-3)^2$

Denominator: $x^2 - 9 = (x-3)(x+3)$

So,
$$
\frac{(x-3)^2}{(x-3)(x+3)} = \frac{x-3}{x+3} \quad (x \neq 3)
$$

Now take the limit:
$$
\lim_{x \to 3} \frac{x-3}{x+3} = \frac{3-3}{3+3} = \frac{0}{6} = 0
$$

---

#### 3. $\lim_{x \to 0} \frac{1}{x}$
As $x$ approaches 0 from the **right** ($x \to 0^+$), $\frac{1}{x} \to +\infty$.

As $x$ approaches 0 from the **left** ($x \to 0^-$), $\frac{1}{x} \to -\infty$.

Since the one-sided limits are not equal, the two-sided limit **does not exist**.

---

#### 4. $\lim_{x \to \infty} \frac{x^2 + 3}{x^3}$
Divide numerator and denominator by the highest power of $x$ in the denominator ($x^3$):

$$
\frac{\frac{1}{x} + \frac{3}{x^3}}{1} = \frac{1}{x} + \frac{3}{x^3}
$$

As $x \to \infty$, both terms approach 0:

$$
\lim_{x \to \infty} \left( \frac{1}{x} + \frac{3}{x^3} \right) = 0
$$

---

#### 5. $\lim_{x \to \infty} \frac{3x^2 + x}{4x^2 - 5}$
Divide numerator and denominator by $x^2$:

$$
\frac{3 + \frac{1}{x}}{4 - \frac{5}{x^2}}
$$

As $x \to \infty$:

$$
\frac{3 + 0}{4 - 0} = \frac{3}{4}
$$

---

#### 6. $\lim_{x \to \infty} \left( \sqrt{x^2 + 4x + 1} - x \right)$
This is an $\infty - \infty$ indeterminate form. Rationalize by multiplying by the conjugate:

$$
\sqrt{x^2 + 4x + 1} - x = \frac{4x + 1}{\sqrt{x^2 + 4x + 1} + x}
$$

Divide numerator and denominator by $x$:

$$
\frac{4 + \frac{1}{x}}{\sqrt{1 + \frac{4}{x} + \frac{1}{x^2}} + 1}
$$

As $x \to \infty$:

$$
\frac{4 + 0}{\sqrt{1 + 0 + 0} + 1} = \frac{4}{1 + 1} = 2
$$

---

#### 7. $\lim_{x \to 0} \frac{\cot 2x}{\csc x}$
Rewrite using trigonometric identities:

$$
\frac{\cot 2x}{\csc x} = \frac{\cos 2x \cdot \sin x}{\sin 2x} = \frac{\cos 2x}{2 \cos x} \quad (\sin x \neq 0)
$$

Now take the limit:
$$
\lim_{x \to 0} \frac{\cos 2x}{2 \cos x} = \frac{\cos 0}{2 \cos 0} = \frac{1}{2}
$$

---

<div align='center'>

## 🟦 Trigonometric Identities and Rules

</div>

Trigonometric identities are fundamental relationships between trigonometric functions. They are essential in calculus for simplifying expressions, solving limits, derivatives, and integrals involving trigonometric functions.

### Basic Reciprocal Identities
$$
\csc x = \frac{1}{\sin x}, \quad \sec x = \frac{1}{\cos x}, \quad \cot x = \frac{1}{\tan x}
$$

### Quotient Identities
$$
\tan x = \frac{\sin x}{\cos x}, \quad \cot x = \frac{\cos x}{\sin x}
$$

### Pythagorean Identities
$$
\sin^2 x + \cos^2 x = 1
$$
$$
1 + \tan^2 x = \sec^2 x
$$
$$
1 + \cot^2 x = \csc^2 x
$$

### Double-Angle Formulas
$$
\sin 2x = 2 \sin x \cos x
$$
$$
\cos 2x = \cos^2 x - \sin^2 x = 1 - 2\sin^2 x = 2\cos^2 x - 1
$$
$$
\tan 2x = \frac{2\tan x}{1 - \tan^2 x}
$$

### Example Using Trig Identities (Limit)
Evaluate $\lim_{x \to 0} \frac{\cot 2x}{\csc x}$ (using identities):

$$
\frac{\cot 2x}{\csc x} = \frac{\frac{\cos 2x}{\sin 2x}}{\frac{1}{\sin x}} = \frac{\cos 2x \cdot \sin x}{\sin 2x} = \frac{\cos 2x \cdot \sin x}{2 \sin x \cos x} = \frac{\cos 2x}{2 \cos x}
$$

$$
\lim_{x \to 0} \frac{\cos 2x}{2 \cos x} = \frac{1}{2 \cdot 1} = \frac{1}{2}
$$

These identities are frequently used when working with limits, derivatives, and integrals of trigonometric functions.

---

<div align='center'>

## 🟦 Derivatives

</div>

### What is a Derivative?
The **derivative** of a function $f(x)$, denoted $f'(x)$ or $\frac{df}{dx}$, represents the **instantaneous rate of change** of the function with respect to $x$. Geometrically, it is the slope of the tangent line to the curve at any point $x$.

**Limit Definition:**
$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Derivatives are fundamental in calculus for finding velocities, accelerations, optimization, and curve sketching.

### Basic Rules of Differentiation

1. **Constant Rule**:  
   If $f(x) = c$ (constant), then $f'(x) = 0$.

2. **Power Rule**:  
   If $f(x) = x^n$, then $f'(x) = n x^{n-1}$ (where $n \neq 0$).

3. **Constant Multiple Rule**:  
   $\frac{d}{dx} [c \cdot f(x)] = c \cdot f'(x)$.

4. **Sum/Difference Rule**:  
   $\frac{d}{dx} [f(x) \pm g(x)] = f'(x) \pm g'(x)$.

5. **Product Rule**:  
   $\frac{d}{dx} [f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)$.

6. **Quotient Rule**:  
   $\frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$.

7. **Chain Rule**:  
   If $y = f(g(x))$, then $\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$.

### Example Using the Power Rule
Find the derivative of $f(x) = 3x^4 - 5x^2 + 7x - 2$.

**Solution:**
$$
f'(x) = 3 \cdot 4x^{3} - 5 \cdot 2x^{1} + 7 \cdot 1 - 0 = 12x^3 - 10x + 7
$$

---

<div align='center'>

## 🟦 Maxima and Minima Using Derivatives

</div>

### Explanation
**Maxima** and **minima** (also called local maximum and local minimum) are the highest and lowest points of a function in a given interval. They are found using the **first derivative**, which represents the **slope** of the tangent line.

- **Critical Points**: Points where $f'(x) = 0$ or where $f'(x)$ is undefined.
- At critical points, the slope is zero (horizontal tangent).
- To classify them:
  - **First Derivative Test**: Check the sign of $f'(x)$ around the critical point (changing from + to - → local max; - to + → local min).
  - **Second Derivative Test**: If $f''(x) > 0$ at critical point → local minimum; if $f''(x) < 0$ → local maximum.

### Example: Find the maxima and minima points of $f(x) = x^3 - 3x^2 + 2$

**Step 1: Find the first derivative (slope)**
$$
f'(x) = 3x^2 - 6x
$$

**Step 2: Find critical points** (set $f'(x) = 0$)
$$
3x^2 - 6x = 0 \implies 3x(x - 2) = 0 \implies x = 0 \quad \text{or} \quad x = 2
$$

**Step 3: Second derivative test**
$$
f''(x) = 6x - 6
$$
- At $x = 0$: $f''(0) = -6 < 0$ → **Local Maximum**
- At $x = 2$: $f''(2) = 6 > 0$ → **Local Minimum**

**Step 4: Find the function values (y-coordinates)**
- $f(0) = 0^3 - 3(0)^2 + 2 = 2$
- $f(2) = (2)^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2$

**Final Answer:**
- **Local Maximum** at point $(0, 2)$
- **Local Minimum** at point $(2, -2)$

---

<div align='center'>

## 🟦 Indefinite Integrals

</div>

### What is an Indefinite Integral?
The **indefinite integral** of a function $f(x)$, denoted $\int f(x) \, dx$, represents the **antiderivative** of $f(x)$. It is the set of all functions $F(x)$ such that $F'(x) = f(x)$.

$$
\int f(x) \, dx = F(x) + C
$$
where $C$ is the **constant of integration**.

### Basic Integration Rules
- $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$ ($n \neq -1$)
- $\int \sin x \, dx = -\cos x + C$
- $\int \cos x \, dx = \sin x + C$
- $\int \sec^2 x \, dx = \tan x + C$
- $\int e^x \, dx = e^x + C$
- $\int \frac{1}{x} \, dx = \ln |x| + C$

---

### Integration by Substitution
**Substitution** (also called u-substitution) is used when the integrand is a composite function. Let $u = g(x)$, then $du = g'(x) \, dx$.

#### Examples

**Example 1:** $\int (2x + 1)^5 \, dx$  
Let $u = 2x + 1$, then $du = 2 \, dx \implies dx = \frac{du}{2}$  
$$
\int u^5 \cdot \frac{du}{2} = \frac{1}{2} \cdot \frac{u^6}{6} + C = \frac{(2x + 1)^6}{12} + C
$$

**Example 2:** $\int x \sqrt{x^2 + 4} \, dx$  
Let $u = x^2 + 4$, then $du = 2x \, dx \implies x \, dx = \frac{du}{2}$  
$$
\int \sqrt{u} \cdot \frac{du}{2} = \frac{1}{2} \cdot \frac{2}{3} u^{3/2} + C = \frac{(x^2 + 4)^{3/2}}{3} + C
$$

**Example 3:** $\int \frac{\sin x}{1 + \cos x} \, dx$  
Let $u = 1 + \cos x$, then $du = -\sin x \, dx \implies -\ du = \sin x \, dx$  
$$
\int \frac{-du}{u} = -\ln |u| + C = -\ln |1 + \cos x| + C
$$

---

### Integration by Parts
**Integration by Parts** is based on the product rule for derivatives. The formula is:

$$
\int u \, dv = uv - \int v \, du
$$

Choose $u$ as the function that is easy to differentiate, and $dv$ as the function that is easy to integrate.

#### Examples

**Example 1:** $\int x e^x \, dx$  
Let $u = x$, $dv = e^x \, dx$ → $du = dx$, $v = e^x$  
$$
x e^x - \int e^x \, dx = x e^x - e^x + C = e^x (x - 1) + C
$$

**Example 2:** $\int \ln x \, dx$  
Let $u = \ln x$, $dv = dx$ → $du = \frac{1}{x} dx$, $v = x$  
$$
x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - \int 1 \, dx = x \ln x - x + C
$$

**Example 3:** $\int x^2 \sin x \, dx$  
Let $u = x^2$, $dv = \sin x \, dx$ → $du = 2x \, dx$, $v = -\cos x$  
$$
- x^2 \cos x - \int (-\cos x) \cdot 2x \, dx = -x^2 \cos x + 2 \int x \cos x \, dx
$$

Now integrate $\int x \cos x \, dx$ by parts again:  
Let $u = x$, $dv = \cos x \, dx$ → $du = dx$, $v = \sin x$  
$$
x \sin x - \int \sin x \, dx = x \sin x + \cos x
$$

Final result:
$$
-x^2 \cos x + 2(x \sin x + \cos x) + C = -x^2 \cos x + 2x \sin x + 2 \cos x + C
$$

---

<div align='center'>

## 🟦 Definite Integrals

</div>

### What is a Definite Integral?
The **definite integral** of a function $f(x)$ from $a$ to $b$, denoted $\int_a^b f(x) \, dx$, represents the **net signed area** under the curve of $f(x)$ between $x = a$ and $x = b$.

By the **Fundamental Theorem of Calculus**:
$$
\int_a^b f(x) \, dx = F(b) - F(a)
$$
where $F(x)$ is any antiderivative of $f(x)$ (i.e., $F'(x) = f(x)$).

### Examples

**Example 1:** Evaluate $\int_1^4 (3x^2 - 2x + 1) \, dx$

**Solution:**  
Antiderivative: $F(x) = x^3 - x^2 + x$  
$$
\int_1^4 (3x^2 - 2x + 1) \, dx = [4^3 - 4^2 + 4] - [1^3 - 1^2 + 1] = (64 - 16 + 4) - (1 - 1 + 1) = 52 - 1 = 51
$$

**Example 2:** Evaluate $\int_0^{\pi/2} \sin x \, dx$

**Solution:**  
Antiderivative: $F(x) = -\cos x$  
$$
\int_0^{\pi/2} \sin x \, dx = [-\cos(\pi/2)] - [-\cos(0)] = (0) - (-1) = 1
$$

---

<div align='center'>

## 🟦 Partial Derivatives and Gradient

</div>

### What are Partial Derivatives?
**Partial derivatives** are used in **multivariable calculus** when a function depends on more than one variable (e.g., $f(x, y)$ or $f(x, y, z)$). 

The **partial derivative** with respect to one variable treats all other variables as constants.

- $\frac{\partial f}{\partial x}$ or $f_x$: derivative with respect to $x$
- $\frac{\partial f}{\partial y}$ or $f_y$: derivative with respect to $y$

### The Gradient
The **gradient** of a function $f(x, y)$ is a vector that contains all the partial derivatives:

$$
\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
$$

The gradient points in the direction of the **steepest ascent** of the function, and its magnitude gives the rate of that increase.

### Examples

**Example 1:** Find the partial derivatives of $f(x, y) = x^2 y + 3xy^2 + 5y$

$$
\frac{\partial f}{\partial x} = 2xy + 3y^2
$$
$$
\frac{\partial f}{\partial y} = x^2 + 6xy + 5
$$

**Example 2:** Find the gradient of $f(x, y) = x^3 + 2xy - y^2$

$$
\nabla f = \left( 3x^2 + 2y, \, 2x - 2y \right)
$$

**Example 3:** Find all partial derivatives of $g(x, y, z) = x^2 y + yz^2 + e^{xz}$

$$
\frac{\partial g}{\partial x} = 2xy + z e^{xz}
$$
$$
\frac{\partial g}{\partial y} = x^2 + z^2
$$
$$
\frac{\partial g}{\partial z} = 2yz + x e^{xz}
$$

**Gradient:**
$$
\nabla g = \left( 2xy + z e^{xz}, \, x^2 + z^2, \, 2yz + x e^{xz} \right)
$$

**Example 4 (Application):** Find the gradient of $f(x, y) = x^2 + y^2$ at the point $(1, 3)$.

First, $\nabla f = (2x, 2y)$

At $(1, 3)$: $\nabla f(1, 3) = (2, 6)$

This vector points in the direction of steepest increase, and its magnitude $|\nabla f| = \sqrt{2^2 + 6^2} = \sqrt{40} = 2\sqrt{10}$ is the maximum rate of increase at that point.