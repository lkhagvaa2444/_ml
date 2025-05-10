import torch

# Initialize variables with requires_grad=True to track computations
x = torch.tensor(0.0, requires_grad=True)
y = torch.tensor(0.0, requires_grad=True)
z = torch.tensor(0.0, requires_grad=True)

# Define the optimizer
optimizer = torch.optim.SGD([x, y, z], lr=0.1)

# Optimization loop
for step in range(100):
    optimizer.zero_grad()  # Clear previous gradients
    f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8  # Define the function
    f.backward()  # Compute gradients
    optimizer.step()  # Update variables

    if step % 10 == 0:
        print(f"Step {step}: f = {f.item():.4f}, x = {x.item():.4f}, y = {y.item():.4f}, z = {z.item():.4f}")
