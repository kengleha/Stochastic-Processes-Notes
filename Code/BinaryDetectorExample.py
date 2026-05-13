import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10  # Number of samples per period
sigma_n_squared = 1.0  # Variance of the noise

# A priori probabilities
P0 = 0.5
P1 = 1 - P0
threshold = np.log(P0/P1)  # Decision threshold

# Generate a sample received signal (noise-only, H0)
r_h0 = np.random.normal(0, np.sqrt(sigma_n_squared), N)

# Generate a sample received signal (with signal pulse, H1)
s_h1 = np.ones(N)  # Signal pulse of amplitude 1
r_h1 = s_h1 + np.random.normal(0, np.sqrt(sigma_n_squared), N)


# Calculate the likelihood ratios for both H0 and H1
log_likelihood_ratio_h0 = np.sum(2*r_h0 * s_h1) / (2 * sigma_n_squared) - np.sum((r_h0)**2) / (2 * sigma_n_squared)
log_likelihood_ratio_h1 = np.sum(2*r_h1 * s_h1) / (2 * sigma_n_squared) - np.sum((r_h1 - s_h1)**2) / (2 * sigma_n_squared)

# Define the range for PDF plots
x = np.linspace(-3, 3, 1000)  # Adjust the range as needed

# Calculate PDFs for H0 and H1
pdf_R_given_h0 = 1 / (np.sqrt(2 * np.pi * sigma_n_squared)) * np.exp(-x**2 / (2 * sigma_n_squared))
pdf_R_given_h1 = 1 / (np.sqrt(2 * np.pi * sigma_n_squared)) * np.exp(-(x - 1)**2 / (2 * sigma_n_squared))

# Plot the PDFs
plt.figure(figsize=(10, 4))
plt.plot(x, pdf_R_given_h0, label='$P(R | H_0)$')
plt.plot(x, pdf_R_given_h1, label='$P(R | H_1)$')
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

# Display the log-likelihood ratios and make decisions
print("Log-Likelihood Ratio (H0):", log_likelihood_ratio_h0)
print("Log-Likelihood Ratio (H1):", log_likelihood_ratio_h1)

print("Threshold: ", threshold)

decision_h0 = "H0" if log_likelihood_ratio_h0 < threshold else "H1"
decision_h1 = "H0" if log_likelihood_ratio_h1 < threshold else "H1"

print("Decision (H0):", decision_h0)
print("Decision (H1):", decision_h1)

plt.show()
