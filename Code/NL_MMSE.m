% Parameters
noise_std = 0.1;  % Standard deviation of Gaussian noise

% Generate a range of X values
X = linspace(0, 2*pi, 100);

% True nonlinear relationship
Y_true = sin(X);

% Observed signal with noise
Y_observed = Y_true + noise_std * randn(size(X));

% Define the objective function for fminunc
objective_function = @(a) mean((sin(X) - a).^2);

% Find the optimal value of a using fminunc
a_optimal = fminunc(objective_function, 0);

% MMSE estimate
Y_mmse = a_optimal;

% Plotting
figure;

subplot(2, 1, 1);
plot(X, Y_true, 'b', 'LineWidth', 2, 'DisplayName', 'True Relationship: sin(X)');
hold on;
plot(X, Y_observed, 'r', 'LineWidth', 1.5, 'DisplayName', 'Observed Signal');
title('True Relationship and Observed Signal');
xlabel('X');
ylabel('Y');
legend();

subplot(2, 1, 2);
plot(X, Y_true, 'b', 'LineWidth', 2, 'DisplayName', 'True Relationship: sin(X)');
hold on;
plot(X, Y_mmse * ones(size(X)), 'g--', 'LineWidth', 1.5, 'DisplayName', 'MMSE Estimate (E[Y|X])');
title('Nonlinear MMSE Estimation');
xlabel('X');
ylabel('Y');
legend();

sgtitle('Nonlinear MMSE Estimation Example using fminunc');
