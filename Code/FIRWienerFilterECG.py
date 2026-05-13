import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, lfilter
import os  # Import the 'os' module

# Download a sample ECG record from the MIT-BIH Arrhythmia Database
record_name = '100'
wfdb.dl_database('mitdb', os.getcwd())  # Download the MIT-BIH Arrhythmia Database

# Read the record and annotation
record = wfdb.rdsamp(record_name, pb_dir='mitdb')
ecg_signal = record.p_signals[:, 0]

# Add synthetic noise to the ECG signal
np.random.seed(42)
noise = 0.5 * np.random.normal(size=len(ecg_signal))
noisy_ecg = ecg_signal + noise

# Estimate the power spectrum of the noisy ECG signal
frequencies, Pxx_noisy = welch(noisy_ecg, fs=record.fs, nperseg=256)

# Estimate the power spectrum of the noise (you may need to adjust frequency ranges)
frequencies, Pxx_noise = welch(noise, fs=record.fs, nperseg=256)

# Design a Wiener filter based on the estimated power spectra
SNR = Pxx_noisy / Pxx_noise
wiener_filter = 1 / (1 + 1 / SNR)

# Apply the Wiener filter to the noisy ECG signal
filtered_ecg = lfilter(wiener_filter, 1.0, noisy_ecg)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(ecg_signal, label='True ECG Signal')
plt.title('True ECG Signal')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(noisy_ecg, label='Noisy ECG Signal')
plt.title('Noisy ECG Signal')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(filtered_ecg, label='Filtered ECG Signal (Wiener)')
plt.title('Filtered ECG Signal (Wiener Filter)')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(frequencies, wiener_filter, label='Wiener Filter')
plt.title('Wiener Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.legend()

plt.tight_layout()
plt.show()
