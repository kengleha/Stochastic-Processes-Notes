#MAP_example
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, binom

# True bit error probability
true_p = 0.2

# Prior parameters for Beta distribution
alpha_prior = 10000
beta_prior = 41000

# Number of experiments
n_experiments = 1000

# Simulate data (Binomial distribution)
n_bits = 100
data = np.random.binomial(n_bits, true_p, size=n_experiments)

# Prior distribution (Beta)
prior_distribution = beta(alpha_prior, beta_prior)

# Posterior distribution (conjugate Beta-Binomial)
alpha_posterior = alpha_prior + np.sum(data)
beta_posterior = beta_prior + n_bits * n_experiments - np.sum(data)
posterior_distribution = beta(alpha_posterior, beta_posterior)

# MAP estimate
map_estimate = (alpha_posterior - 1) / (alpha_posterior + beta_posterior - 2)
#map_estimate = (2*alpha_posterior - 1) / (beta_posterior)

# Plotting
x = np.linspace(0.19, .2025, 1000)

plt.figure(figsize=(10, 6))

# Plot Prior
plt.plot(x, prior_distribution.pdf(x)/sum(prior_distribution.pdf(x)), label='Prior (Beta)')

# Plot Posterior
plt.plot(x, posterior_distribution.pdf(x)/sum(posterior_distribution.pdf(x)), label='Posterior (Beta)')

# Plot True Value
plt.axvline(true_p, color='red', linestyle='--', label='True Value')

# Plot MAP Estimate
plt.axvline(map_estimate, color='green', linestyle='--', label='MAP Estimate')

plt.xlabel('Bit Error Probability (p)')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

print(f"True Bit Error Probability: {true_p}")
print(f"MAP Estimate: {map_estimate}")