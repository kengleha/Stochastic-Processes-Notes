% Prior parameters
mu_prior = 0;
sigma_prior = 2;

% Observations
data_points = [1.5, 2.0, 1.8, -0.5, 0.9];

% Likelihood parameters (known variance)
sigma_likelihood = 1.0;

% Bayesian updating
sigma_numerator = 1 / sigma_prior^2 + numel(data_points) / sigma_likelihood^2;
mu_numerator = mu_prior / sigma_prior^2 + sum(data_points) / sigma_likelihood^2;

% Updated parameters
sigma_posterior = 1 / sigma_numerator;
mu_posterior = mu_numerator * sigma_posterior;

% Generate samples from the posterior distribution
posterior_samples = normrnd(mu_posterior, sqrt(sigma_posterior), 1000, 1);

% Plot the prior and posterior distributions
x = linspace(-5, 5, 100);
prior_pdf = normpdf(x, mu_prior, sigma_prior);
posterior_pdf = normpdf(x, mu_posterior, sqrt(sigma_posterior));

figure;
plot(x, prior_pdf, 'LineWidth', 2, 'DisplayName', 'Prior');
hold on;
plot(x, posterior_pdf, 'LineWidth', 2, 'DisplayName', 'Posterior');
scatter(data_points, zeros(size(data_points)), 50, 'red', 'x', 'DisplayName', 'Observations');
title('Bayesian Estimation of Gaussian Process Mean');
xlabel('\mu (Process Mean)');
ylabel('Probability Density');
legend('show');
hold off;
