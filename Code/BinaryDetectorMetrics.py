import numpy as np
import matplotlib.pyplot as plt

# Define the signal and noise distributions
signal_dist = np.random.binomial(1, 0.8, size=1000)  # 80% chance of signal being 1
noise_dist = np.random.normal(0, 1, size=1000)  # Gaussian noise with mean 0 and std dev 1

# Define the detector and threshold
def detector(signal, noise, threshold):
	return (signal + noise) > threshold

# Vary the noise level (std dev)
noise_levels = [0.1, 0.5, 1, 2, 5]
TPR, TNR, FNR, FPR = [], [], [], []

for noise_level in noise_levels:
	# Generate noisy signals
	noisy_signals = signal_dist + noise_dist * noise_level
	
	# Detect signals
	detections = detector(noisy_signals, noise_dist, 0.5)
	
	# Calculate metrics
	TP = np.sum((signal_dist == 1) & (detections == 1))
	FP = np.sum((signal_dist == 0) & (detections == 1))
	TN = np.sum((signal_dist == 0) & (detections == 0))
	FN = np.sum((signal_dist == 1) & (detections == 0))
	
	TPR.append(TP / (TP + FN))
	TNR.append(TN / (TN + FP))
	FNR.append(FN / (TP + FN))
	FPR.append(FP / (TN + FP))

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(noise_levels, TPR, label='TPR')
plt.plot(noise_levels, TNR, label='TNR')
plt.plot(noise_levels, FNR, label='FNR')
plt.plot(noise_levels, FPR, label='FPR')
plt.xlabel('Noise Level (std dev)')
plt.ylabel('Metrics')
plt.title('Effect of Noise Level on Binary Detector Metrics')
plt.legend()
plt.show()