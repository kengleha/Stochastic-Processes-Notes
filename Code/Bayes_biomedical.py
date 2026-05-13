import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Prior distribution
prior_mean = 50
prior_std = 20

# Simulated data from a clinical trial
np.random.seed(42)
data = np.random.normal(loc=45, scale=15, size=30)

# Likelihood function
likelihood_mean = np.mean(data)
likelihood_std = np.std(data)

# Bayesian update (Posterior)
posterior_mean = (prior_mean / prior_std**2 + likelihood_mean / likelihood_std**2) / (1 / prior_std**2 + 1 / likelihood_std**2)
posterior_std = np.sqrt(1 / (1 / prior_std**2 + 1 / likelihood_std**2))

# Plotting
x_values = np.linspace(0, 100, 1000)
prior_pdf = norm.pdf(x_values, loc=prior_mean, scale=prior_std)
likelihood_pdf = norm.pdf(x_values, loc=likelihood_mean, scale=likelihood_std)
posterior_pdf = norm.pdf(x_values, loc=posterior_mean, scale=posterior_std)

plt.figure(figsize=(10, 6))
plt.plot(x_values, prior_pdf, label='Prior', linestyle='dashed')
plt.plot(x_values, likelihood_pdf, label='Likelihood', linestyle='dashed')
plt.plot(x_values, posterior_pdf, label='Posterior')
plt.hist(data, bins=15, density=True, alpha=0.5, color='gray', label='Observed Data')
plt.title('Bayesian Estimation of Mean Response Time')
plt.xlabel('Response Time')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
