import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 100  # Period of the waveform
num_periods = 5  # Number of periods to generate
SNR_dB = 8  # Signal-to-noise ratio in decibels

# Generate the time axis
fs = 1000  # Sampling frequency
t = np.arange(0, num_periods * T, 1 / fs)

# Generate the binary waveform with 0s and 1s
signal = np.array([1 if int(ti // T) % 2 == 0 else 0 for ti in t])

# Add white Gaussian noise
noise_std = np.sqrt(0.5 / (20**(SNR_dB / 10)))  # Standard deviation for the noise
noise = np.random.normal(0, noise_std, len(t))
noisy_signal = signal + noise

# Plot the binary waveform with noise
plt.figure(figsize=(10, 4))
plt.plot(t, noisy_signal, label='Noisy Binary Waveform')
plt.plot(t, signal, label='Noise-free waveform',linewidth=3)
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title(f'Random Binary Waveform with Noise (SNR={SNR_dB} dB)')
plt.ylim(-1, 2.0)
plt.grid()


# Add 'x' markers every 10 samples
sample_indices = np.arange(0, len(t), 10 * fs)
plt.plot(t[sample_indices], noisy_signal[sample_indices], 'rx', markersize=8, label=f'samples')

plt.legend()
plt.show()
