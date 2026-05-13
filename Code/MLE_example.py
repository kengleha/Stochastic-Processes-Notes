import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# True parameters
true_beta0 = 2
true_beta1 = 1.5
true_sigma = 1

# Generate synthetic data
np.random.seed(42)
sample_size = 100
x_data = np.linspace(0, 10, sample_size)
y_data = true_beta0 + true_beta1 * x_data + np.random.normal(0, true_sigma, sample_size)

# Define log-likelihood function
def log_likelihood(params, x, y):
    beta0, beta1, sigma = params
    residuals = y - (beta0 + beta1 * x)
    return -0.5 * (len(x) * np.log(2 * np.pi * sigma**2) + np.sum(residuals**2) / sigma**2)

# Minimize negative log-likelihood to find MLE
result = minimize(lambda params: -log_likelihood(params, x_data, y_data), [1, 1, 1], method='L-BFGS-B')

# Extract MLE estimates
mle_beta0, mle_beta1, mle_sigma = result.x

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Observed Data')
plt.plot(x_data, true_beta0 + true_beta1 * x_data, label='True Regression Line', linestyle='--', color='red')
plt.plot(x_data, mle_beta0 + mle_beta1 * x_data, label='MLE Regression Line', linestyle='--', color='green')
plt.title('Maximum Likelihood Estimation for Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print("True Parameters:")
print(f"Beta_0: {true_beta0}, Beta_1: {true_beta1}, Sigma: {true_sigma}")
print("\nMaximum Likelihood Estimates:")
print(f"Beta_0: {mle_beta0}, Beta_1: {mle_beta1}, Sigma: {mle_sigma}")
