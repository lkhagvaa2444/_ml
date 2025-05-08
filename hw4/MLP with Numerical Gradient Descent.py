import numpy as np

# Sigmoid activation and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    s = sigmoid(x)
    return s * (1 - s)

# Mean squared error
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 7-segment display patterns for digits 0-9
X = np.array([
    [1,1,1,1,1,1,0],  # 0
    [0,1,1,0,0,0,0],  # 1
    [1,1,0,1,1,0,1],  # 2
    [1,1,1,1,0,0,1],  # 3
    [0,1,1,0,0,1,1],  # 4
    [1,0,1,1,0,1,1],  # 5
    [1,0,1,1,1,1,1],  # 6
    [1,1,1,0,0,0,0],  # 7
    [1,1,1,1,1,1,1],  # 8
    [1,1,1,1,0,1,1],  # 9
])

# One-hot labels for 0–9
Y = np.eye(10)

# MLP Architecture
input_size = 7
hidden_size = 5
output_size = 10

# Random initial weights
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.1
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.1
b2 = np.zeros((1, output_size))

# Training via numerical gradient descent
lr = 0.1
epochs = 5000
epsilon = 1e-5

for epoch in range(epochs):
    # Forward pass
    z1 = X @ W1 + b1
    h1 = sigmoid(z1)
    z2 = h1 @ W2 + b2
    out = sigmoid(z2)
    
    loss = mse(Y, out)

    # Numerical gradients
    def compute_numerical_grad(param, name):
        grad = np.zeros_like(param)
        for i in range(param.shape[0]):
            for j in range(param.shape[1]):
                old_val = param[i, j]
                
                param[i, j] = old_val + epsilon
                z1p = X @ W1 + b1
                h1p = sigmoid(z1p)
                z2p = h1p @ W2 + b2
                out_p = sigmoid(z2p)
                loss_plus = mse(Y, out_p)

                param[i, j] = old_val - epsilon
                z1m = X @ W1 + b1
                h1m = sigmoid(z1m)
                z2m = h1m @ W2 + b2
                out_m = sigmoid(z2m)
                loss_minus = mse(Y, out_m)

                grad[i, j] = (loss_plus - loss_minus) / (2 * epsilon)
                param[i, j] = old_val  # restore
        return grad

    # Gradients
    dW2 = compute_numerical_grad(W2, "W2")
    db2 = compute_numerical_grad(b2, "b2")
    dW1 = compute_numerical_grad(W1, "W1")
    db1 = compute_numerical_grad(b1, "b1")

    # Update weights
    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2

    # Print every 500 epochs
    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")

# Final prediction
preds = np.argmax(out, axis=1)
print("\nPredicted labels:", preds)
