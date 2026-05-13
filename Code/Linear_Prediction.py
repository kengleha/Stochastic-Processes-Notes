import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Function to generate synthetic speech signal
def generate_speech_signal(duration, sampling_rate, f0, formants):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    speech_signal = np.zeros_like(t)

    for f in formants:
        speech_signal += np.sin(2 * np.pi * f * t)

    return speech_signal

# Parameters
duration = 1.0        # seconds
sampling_rate = 10000  # Hz
f0 = 100              # fundamental frequency
formants = [500, 1500, 2500]  # formant frequencies

# Generate synthetic speech signal
speech_signal = generate_speech_signal(duration, sampling_rate, f0, formants)

# Linear Prediction Model
order = 3  # Order of the linear prediction model

# Use lfilter to find the LPC coefficients
lpc_coeff = lfilter([1], np.append(1, -np.linalg.solve(np.correlate(speech_signal, speech_signal, mode='full')[len(speech_signal)-1:-1:-1], speech_signal[:len(speech_signal)-1], mode='full'))[1:], speech_signal)

# Synthesize speech using LPC coefficients
synthesized_speech = lfilter([1], lpc_coeff, np.random.randn(len(speech_signal)))

# Plot the results
plt.figure(figsize=(12, 6))

# Plot the original speech signal
plt.subplot(3, 1, 1)
plt.plot(speech_signal)
plt.title('Original Speech Signal')

# Plot the LPC coefficients
plt.subplot(3, 1, 2)
plt.stem(lpc_coeff)
plt.title('LPC Coefficients')

# Plot the synthesized speech signal
plt.subplot(3, 1, 3)
plt.plot(synthesized_speech)
plt.title('Synthesized Speech Signal')

plt.tight_layout()
plt.show()
