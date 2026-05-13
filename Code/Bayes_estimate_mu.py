import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Prior parameters
mu_prior = 0
sigma_prior = 2

# Observations
data_points = np.array([1.5, 2.0, 1.8, -0.5, 0.9])

# Likelihood parameters (known variance)
sigma_likelihood = 1.0

# Bayesian updating
sigma_numerator = 1 / sigma_prior**2 + len(data_points) / sigma_likelihood**2
mu_numerator = mu_prior / sigma_prior**2 + np.sum(data_points) / sigma_likelihood**2

# Updated parameters
sigma_posterior = 1 / sigma_numerator
mu_posterior = mu_numerator * sigma_posterior

# Mode of the posterior distribution
mode_posterior = mu_posterior

# Generate samples from the posterior distribution
posterior_samples = norm.rvs(mu_posterior, np.sqrt(sigma_posterior), size=1000)

# Plot the prior and posterior distributions
x = np.linspace(-5, 5, 100)
prior_pdf = norm.pdf(x, mu_prior, sigma_prior)
posterior_pdf = norm.pdf(x, mu_posterior, np.sqrt(sigma_posterior))

plt.plot(x, prior_pdf, label='Prior')
plt.plot(x, posterior_pdf, label='Posterior')
plt.scatter(data_points, np.zeros_like(data_points), color='red', marker='x', label='Observations')
plt.title(f'$\sigma_0$: {sigma_prior:.2f}')
plt.xlabel(r'$\mu$ (Process Mean)')
plt.ylabel('Probability Density')
plt.legend()
plt.axis([-4, 4, -0.05, 1.4])

# Labeling the peak of the posterior distribution
plt.text(mode_posterior, norm.pdf(mode_posterior, mu_posterior, np.sqrt(sigma_posterior)), f'Mean: {mode_posterior:.2f}', ha='center', va='bottom')
