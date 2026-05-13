# Binary Detector
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10  # Number of samples per period
sigma_n_squared = 1.0  # Variance of the noise
P_H0 = 0.5
P_H1 = 0.5
threshold =  np.log(P_H0/P_H1) # Decision threshold
print("Threshold:", threshold)


# Generate a sample received signal (noise-only, H0)
r_h0 = np.random.normal(0, np.sqrt(sigma_n_squared), N)

# Generate a sample received signal (with signal pulse, H1)
s_h1 = np.ones(N)  # Signal pulse of amplitude 1
r_h1 = s_h1 + np.random.normal(0, np.sqrt(sigma_n_squared), N)

# Calculate the likelihood ratios for both H0 and H1
log_likelihood_ratio_h0 = -0.5 * (np.sum(r_h0**2) - np.sum(r_h0**2)) / sigma_n_squared
log_likelihood_ratio_h1 = -0.5 * (np.sum(r_h1**2) - np.sum((r_h1 - s_h1)**2)) / sigma_n_squared

# Define the range for PDF plots
x = np.linspace(-3, 3, 1000)  # Adjust the range as needed

# Calculate PDFs for H0 and H1
pdf_R_h0 = 1 / (np.sqrt(2 * np.pi * sigma_n_squared)) * np.exp(-x**2 / (2 * sigma_n_squared))
pdf_R_h1 = 1 / (np.sqrt(2 * np.pi * sigma_n_squared)) * np.exp(-(x - 1)**2 / (2 * sigma_n_squared))

# Plot the PDFs
plt.figure(figsize=(10, 4))
plt.plot(x, pdf_R_h0, label='$P(R | H_0)$')
plt.plot(x, pdf_R_h1, label='$P(R | H_1)$')
plt.xlabel('Received Signal Value (r)')
plt.ylabel('Probability Density')
plt.title('PDFs of Likelihood Functions for H0 and H1')
plt.legend()

# Plot the noisy signals
plt.figure(figsize=(10, 4))
plt.stem(range(N), r_h0, label='Noisy Signal under $H_0$')
plt.stem(range(N), r_h1, linefmt='r-', markerfmt='ro', basefmt='r-', label='Noisy Signal under $H_1$')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.title('Noisy Signals for $H_0$ and $H_1$')
plt.legend()

plt.show()

# Display the results
LLR_H0 = np.exp(log_likelihood_ratio_h0)
LLR_H1 = np.exp(log_likelihood_ratio_h1)

print("Log-Likelihood Ratio H0:", LLR_H0)
if LLR_H0 < threshold:
    decision = 0
else:
    decision = 1
print("With threshold=", threshold, "decision = ", decision )

print("Log-Likelihood Ratio H1:", LLR_H1)
if LLR_H1 < threshold:
    decision = 0
else:
    decision = 1
print("With threshold=", threshold, "decision = ", decision )

#print("Decision:", decision)