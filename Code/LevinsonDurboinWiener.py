# Levinson-Durboin solution for the Wiener filter
import numpy as np
from scipy.signal import lfilter, filtfilt
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, pinv
from sklearn.metrics import mean_squared_error

# Parameters
N = 1000      # Number of samples
M = 200       # Filter order (one less than the matrix size)

# Generate input signal x(n) - Assume a white Gaussian noise
x = np.random.randn(N)

# Generate desired signal y(n) - A sinusoidal signal corrupted by noise
true_signal = np.sin(2 * np.pi * 0.005 * np.arange(N))
noise = 0.2 * np.random.randn(N)
y = true_signal + noise

# Compute the autocorrelation matrix Rxx with dimensions 21x21
Rxx = np.correlate(x, x, mode='full')[:M+1]

# Compute the cross-correlation vector Rxy
Rxy = np.correlate(x, y, mode='full')[:M+1]

# Use Levinson-Durbin recursion to compute the inverse of Rxx
# Initialize the recursion
A = Rxx[1:]  # Autocorrelation coefficients excluding the zeroth lag
P = Rxx[0]   # Power term

# Initialize the inverse of Rxx
Rxx_inv = np.zeros_like(Rxx)
Rxx_inv[0] = 1.0 / P

# Apply the Levinson-Durbin recursion
for m in range(1, M+1):
    # Compute reflection coefficient
    k = -np.dot(Rxx[1:m+1], Rxx_inv[m-1:0:-1]) / P
    
    # Update A and P
    A = np.concatenate(([1], A)) + k * np.flipud(A)
    P *= 1 - k**2
    
    # Update the inverse of Rxx
    Rxx_inv[m] = -k
    Rxx_inv[1:m+1] += k * Rxx[m:0:-1]

# Compute the filter coefficients using the inverse of Rxx
h = np.dot(Rxx_inv[1:], Rxy)

# Apply the Wiener filter to the noisy signal
filtered_signal = filtfilt(h, 1.0, y)

# Display the results
norm_true_signal = true_signal / np.std(true_signal)
norm_y = y / np.std(y)
norm_filtered_signal = filtered_signal / np.std(filtered_signal)

MSE = mean_squared_error(norm_true_signal, norm_filtered_signal)
print("Mean Square error:", MSE)
print("Normalized Mean Square error:", MSE / np.mean(true_signal**2))

# Plot the results with scaled amplitudes
plt.figure(figsize=(10, 6))

plt.plot(norm_y, label='Noisy Signal')
plt.plot(norm_filtered_signal, label='Filtered Signal (Wiener)')
plt.plot(norm_true_signal, label='True Signal')
plt.title('Noisy Signal and Filtered Signal (Wiener Filter)')
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.stem(h, linefmt='r-', markerfmt='ro', label='Wiener Filter Coefficients')
plt.title('Wiener Filter Coefficients')
plt.legend()

plt.show()
