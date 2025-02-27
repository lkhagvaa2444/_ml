import numpy as np

def f(x, y, z):
    return x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8

def gradient(x, y, z):
    return np.array([2*x - 2, 2*y - 4, 2*z - 6])

def hill_climbing(lr=0.1, max_iters=1000, tol=1e-6):
    x, y, z = np.random.randn(3)
    for _ in range(max_iters):
        grad = gradient(x, y, z)
        x, y, z = x - lr * grad[0], y - lr * grad[1], z - lr * grad[2]
        if np.linalg.norm(grad) < tol:
            break
    return x, y, z, f(x, y, z)

opt_x, opt_y, opt_z, min_val = hill_climbing()
print(f"Optimal (x, y, z): ({opt_x:.6f}, {opt_y:.6f}, {opt_z:.6f})")
print(f"Minimum function value: {min_val:.6f}")
