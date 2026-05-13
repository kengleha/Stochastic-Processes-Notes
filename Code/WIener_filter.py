import numpy as np
import matplotlib.pyplot as plt
# WienerFilter
from scipy import signal

# Generate a sample signal with noise
t = np.linspace(0, 1, 1000, endpoint=False)
z = np.sin(2 * np.pi * 5 * t)  # Desired signal
n = 0.2 * np.random.randn(len(t))  # Gaussian noise
x = z + n  # Observed signal with noise

# Design an LTI filter using Wiener filter design
h = signal.wiener(x, mysize=10)

# Apply the filter to the observed signal
y = signal.convolve(x, h, mode='same')

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, z, label='Desired Signal')
plt.plot(t, x, label='Observed Signal (with Noise)')
plt.legend()
plt.title('Noisy Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t, y, label='Filtered Signal')
plt.legend()
plt.title('Noise Cancellation with LTI Filter')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
