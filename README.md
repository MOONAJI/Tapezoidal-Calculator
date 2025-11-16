# Trapezoid Rule Integral Calculator

## 📖 Table of Contents
- [What is the Trapezoid Rule?](#what-is-the-trapezoid-rule)
- [How the Trapezoid Method Works](#how-the-trapezoid-method-works)
- [Program Features](#program-features)
- [How to Use the Program](#how-to-use-the-program)
- [Usage Examples](#usage-examples)
- [Function Writing Format](#function-writing-format)
- [Output Explanation](#output-explanation)

---

## What is the Trapezoid Rule?

The **Trapezoid Rule** is a numerical integration method used to calculate approximate values of definite integrals. This method is particularly useful when:
- The integral cannot be solved analytically
- You only have discrete data points
- You need numerical results quickly

### Basic Principle

The trapezoid rule works by dividing the area under a function's curve into several trapezoids, then summing the areas of all those trapezoids. The more trapezoids used (the smaller the subinterval width), the more accurate the approximation becomes.

---

## How the Trapezoid Method Works

### Mathematical Formula

To calculate the integral of function f(x) on interval [a, b] with n subintervals:

```
∫[a,b] f(x) dx ≈ (h/2) × [f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]
```

Where:
- **h = (b - a) / n** is the width of each subinterval
- **x₀ = a, x₁, x₂, ..., xₙ = b** are the partition points
- **f(xᵢ)** is the function value at point i

### Calculation Steps

1. **Divide the interval** [a, b] into n subintervals with equal width h
2. **Calculate points** x₀, x₁, x₂, ..., xₙ with distance h
3. **Evaluate the function** at each point to get f(x₀), f(x₁), ..., f(xₙ)
4. **Apply the trapezoid formula**:
   - Start and end points are multiplied by 1
   - Middle points are multiplied by 2
   - Sum everything and multiply by h/2

### Concept Visualization

```
     f(x)
      |
      |     /\
      |    /  \___
      |   /       \
      |  /         \__
      | /             \
      |/_______________|_____ x
      a  x₁  x₂  x₃   b

Each trapezoid approximates the area under the curve
```

---

## Program Features

### ✨ Main Features
- **Flexible function input** - Supports various types of mathematical functions
- **Automatic calculation** - Quickly computes numerical integrals
- **Detailed calculation table** - Shows every calculation step
- **Error analysis** - Compares with exact value if known
- **Graphical visualization** - Displays curve and trapezoids
- **Convergence graph** - Shows how error decreases with larger n

### 📊 Generated Output
1. Approximate integral value
2. Complete calculation table with coefficients
3. Absolute and relative error (if exact value available)
4. Graphical trapezoid visualization
5. Error convergence graph

---

## How to Use the Program

### Requirements
- Python 3.x
- Libraries: `numpy`, `matplotlib`

### Library Installation
```bash
pip install numpy matplotlib
```

### Running the Program
```bash
python trapezoidrulecalculator.py
```

### Interactive Steps

#### **Step 1: Enter Function**
Type the mathematical function you want to integrate using variable `x`.

**Example:**
```
Enter function f(x): x**2 + 3*x + 1
```

#### **Step 2: Enter Integral Bounds**
Specify the lower bound (a) and upper bound (b) of the integral.

**Example:**
```
Lower bound (a): 0
Upper bound (b): 2
```

**For special values:**
```
Lower bound (a): 0
Upper bound (b): 2*pi/5
```

#### **Step 3: Enter Number of Subintervals**
Specify how many trapezoids to use (n). The larger n, the more accurate the result.

**Example:**
```
Number of subintervals (n): 100
```

#### **Step 4: Exact Value (Optional)**
If you know the exact integral value (from analytical calculation), enter it here to see the error.

**Example:**
```
Exact integral value: 8.666667
```
or press Enter to skip.

#### **Step 5: Visualization**
The program will ask if you want to see the graph.
```
Do you want to see visualization? (y/n): y
```

---

## Usage Examples

### Example 1: Polynomial Function

**Input:**
```
Function: x**2
Lower bound: 0
Upper bound: 2
Number of subintervals: 4
Exact value: 2.666667
```

**Output:**
```
INTEGRAL RESULT: 2.7500000000

Exact value: 2.6666670000
Absolute error: 0.0833330000
Relative error: 3.1250%
```

### Example 2: Trigonometric Function

**Input:**
```
Function: sin(x)
Lower bound: 0
Upper bound: pi
Number of subintervals: 50
Exact value: 2
```

**Output:**
```
INTEGRAL RESULT: 1.9999998333

Exact value: 2.0000000000
Absolute error: 0.0000001667
Relative error: 0.0008%
```

### Example 3: Exponential Function

**Input:**
```
Function: exp(-x**2)
Lower bound: 0
Upper bound: 1
Number of subintervals: 100
```

---

## Function Writing Format

### Mathematical Operators
| Operation | Symbol | Example |
|---------|--------|--------|
| Addition | `+` | `x + 5` |
| Subtraction | `-` | `x - 3` |
| Multiplication | `*` | `2*x` |
| Division | `/` | `1/x` |
| Power | `**` or `^` | `x**2` or `x^2` |

### Mathematical Functions
| Function | Syntax | Example |
|--------|---------|--------|
| Sine | `sin(x)` | `sin(2*x)` |
| Cosine | `cos(x)` | `cos(x)**2` |
| Tangent | `tan(x)` | `tan(x/2)` |
| Exponential | `exp(x)` | `exp(-x**2)` |
| Natural logarithm | `log(x)` | `log(x+1)` |
| Square root | `sqrt(x)` | `sqrt(x)` |

### Constants
| Constant | Symbol | Value |
|-----------|--------|-------|
| Pi | `pi` | 3.14159... |
| Euler | `e` | 2.71828... |

### Valid Function Examples
```
x**2 + 3*x + 1
sin(x) + cos(x)
exp(-x**2)
1/(1 + x**2)
sqrt(1 - x**2)
x*sin(x)
log(x)
2*pi*x
```

---

## Output Explanation

### Calculation Table

The program displays a detailed table showing:

| Column | Explanation |
|-------|------------|
| **i** | Point index (0 to n) |
| **x_i** | x value at point i |
| **f(x_i)** | Function value at point i |
| **Coefficient** | 1 for start/end points, 2 for middle points |
| **Contribution** | Coefficient × f(x_i) |

**Table Example:**
```
   i |          x_i |        f(x_i) | Coefficient |    Contribution
----------------------------------------------------------------------
   0 |     0.000000 |      0.000000 |          1 |      0.000000
   1 |     0.500000 |      0.250000 |          2 |      0.500000
   2 |     1.000000 |      1.000000 |          2 |      2.000000
   3 |     1.500000 |      2.250000 |          2 |      4.500000
   4 |     2.000000 |      4.000000 |          1 |      4.000000
```

### Visualization Graphs

**Graph 1: Trapezoid Approximation**
- Shows the original function curve (blue line)
- Shows trapezoid points (red dots)
- Yellow area shows trapezoids approximating the area under the curve

**Graph 2: Error Convergence**
- X-axis: Number of subintervals (n)
- Y-axis: Absolute error (logarithmic scale)
- Shows how error decreases as n increases
- Red vertical line marks your chosen n value

### Error Interpretation

- **Absolute Error**: |Exact Value - Approximate Value|
- **Relative Error**: (Absolute Error / |Exact Value|) × 100%

**Guidelines:**
- Relative error < 1%: Excellent
- Relative error 1-5%: Good
- Relative error > 5%: Consider increasing n

---

## Usage Tips

### 🎯 Choosing Number of Subintervals (n)

- **n = 10-50**: For quick results and simple functions
- **n = 100-500**: For better accuracy
- **n = 1000+**: For highly varying functions or when high precision is needed

### ⚠️ Important Considerations

1. **Discontinuities**: The trapezoid method is not accurate for discontinuous functions
2. **Singularities**: Avoid functions with division by zero (e.g., 1/x at x=0)
3. **High Oscillation Functions**: Need very large n for accurate results
4. **Open Intervals**: Ensure the function is defined at points a and b

### 💡 Improving Accuracy

1. Increase the number of subintervals (n)
2. Ensure the integration interval is appropriate
3. For rapidly changing functions, use larger n
4. Compare with exact value if available

---

## Conclusion

This Trapezoid Rule Integral Calculator is a powerful tool for:
- Learning numerical integration concepts
- Calculating integrals that are difficult to solve analytically
- Visualizing the numerical approximation process
- Analyzing convergence and error

This program is suitable for students, researchers, and anyone who needs quick and accurate numerical integral calculations.

---

## 📝 Additional Notes

**Computational Complexity**: O(n) - Linear with respect to the number of subintervals

**Accuracy**: The trapezoid rule has error order O(h²), which means doubling n will reduce the error to approximately 1/4 of the previous value.

**Alternatives**: For higher accuracy, consider Simpson's method or Gaussian Quadrature methods (not available in this program).

---

*Enjoy using the calculator! If you have any questions or problems, make sure the input function is valid and follows the explained format.*