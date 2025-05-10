import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create model instance
model = SimpleModel()

# Generate random input
input_data = torch.randn(1, 10)

# Call the model
output = model(input_data)

print("Model output:", output)
