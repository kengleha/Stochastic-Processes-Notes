import numpy as np
import matplotlib.pyplot as plt

# Define true coefficients and noise variance
true_coeffs = np.array([2, 3, -1])  # True weights [w1, w2, w3]
noise_variance = 2

# Generate data
num_samples = 1000
X = np.random.randn(num_samples, 3)  # Randomly generated data vector X

# Generate true values of Y
Y_true = np.dot(X, true_coeffs) + np.sqrt(noise_variance) * np.random.randn(num_samples)

# Add some noise to create observed values of Y
observed_Y = Y_true + np.sqrt(noise_variance) * np.random.randn(num_samples)

# Linear MMSE Estimation
X_with_bias = np.hstack([np.ones((num_samples, 1)), X])  # Add a bias term for the intercept
optimal_weights = np.linalg.lstsq(X_with_bias.T @ X_with_bias, X_with_bias.T @ observed_Y, rcond=None)[0]

# Display the true and estimated coefficients
print('True Coefficients:')
print(true_coeffs)

print('Estimated Coefficients (Linear MMSE):')
print(optimal_weights[1:])  # Exclude the intercept term

# Plot true vs observed Y
plt.scatter(Y_true, observed_Y)
plt.plot([min(Y_true), max(Y_true)], [min(Y_true), max(Y_true)], 'r--')  # Diagonal line
plt.xlabel('True Y')
plt.ylabel('Observed Y')
plt.title('True vs Observed Y')

# Display the plot
plt.show()
