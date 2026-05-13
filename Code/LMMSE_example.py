import numpy as np
import matplotlib.pyplot as plt

# Parameters
sigma_z = 1  # Variance of Z
sigma_w = 0.5  # Variance of W
sigma_x = 0.8  # Variance of X

# Generate a time vector
t = np.arange(0, 10.1, 0.1)

# Generate the random process Z
Z = np.random.randn(len(t)) * np.sqrt(sigma_z)

# Generate white Gaussian noise W
W = np.random.randn(len(t)) * np.sqrt(sigma_w)

# Form the observed signal X
X = Z + W

# Calculate the optimal coefficient A
A = sigma_z**2 / (sigma_x**2 + sigma_w**2)

# Compute the MMSE estimate of Z
Z_hat = A * X

# Plot the signals
plt.figure()
plt.plot(t, Z, 'b', linewidth=2, label='Z(t)')
plt.plot(t, X, 'r', linewidth=1.5, label='X(t)')
plt.plot(t, Z_hat, 'g--', linewidth=1.5, label='Estimated Z(t)')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('MMSE Estimation Example')
plt.grid(True)
plt.show()
