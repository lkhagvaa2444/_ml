from sklearn.ensemble import IsolationForest
import numpy as np
import matplotlib.pyplot as plt

# Generate data: normal points + some outliers
rng = np.random.RandomState(42)
X_normal = 0.3 * rng.randn(100, 2)
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
X = np.r_[X_normal + 2, X_normal - 2, X_outliers]

# Build and train the model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

# Predict: 1 = normal, -1 = anomaly
y_pred = model.predict(X)

# Plot
plt.title("Isolation Forest Result")
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()