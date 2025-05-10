# Homework 8: Function Optimization with PyTorch

## Overview

This assignment re-implements the function optimization task from Homework 1 using PyTorch. Instead of manually computing gradients and updating parameters, we use PyTorch's automatic differentiation and `torch.optim` utilities.

## Objective

Minimize the multivariable function:

```

f(x, y, z) = x² + y² + z² - 2x - 4y - 6z + 8

```

We want to find the values of `x`, `y`, and `z` that minimize this function using PyTorch's gradient descent.

## ✅ Implementation

- Initialize `x`, `y`, and `z` as tensors with `requires_grad=True`.
- Use stochastic gradient descent (SGD) from `torch.optim`.
- Run an optimization loop to iteratively update parameters.
- Print intermediate values every 10 steps.

## 💻 Example Output

```

Step 0: f = 8.0000, x = 0.2000, y = 0.4000, z = 0.6000
...
Step 90: f = 0.0000, x = 1.0000, y = 2.0000, z = 3.0000

```

## 🎯 Result

After optimization, we reach the function's minimum at:
```

x = 1.0, y = 2.0, z = 3.0, f = 0.0

```