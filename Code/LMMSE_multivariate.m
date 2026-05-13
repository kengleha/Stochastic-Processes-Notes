% Linear MMSE Estimation Example

% Define true coefficients and noise variance
true_coeffs = [2; 3; -1];  % True weights [w1; w2; w3]
noise_variance = 2;

% Generate data
num_samples = 1000;
X = randn(num_samples, 3);  % Randomly generated data vector X

% Generate true values of Y
Y_true = X * true_coeffs + sqrt(noise_variance) * randn(num_samples, 1);

% Add some noise to create observed values of Y
observed_Y = Y_true + sqrt(noise_variance) * randn(num_samples, 1);

% Linear MMSE Estimation
X_with_bias = [ones(num_samples, 1), X];  % Add a bias term for the intercept
optimal_weights = (X_with_bias' * X_with_bias) \ (X_with_bias' * observed_Y);

% Display the true and estimated coefficients
disp('True Coefficients:');
disp(true_coeffs);

disp('Estimated Coefficients (Linear MMSE):');
disp(optimal_weights(2:end));  % Exclude the intercept term

% Plot true vs observed Y
figure;
scatter(Y_true, observed_Y);
hold on;
plot(min(Y_true):max(Y_true), min(Y_true):max(Y_true), 'r--');  % Diagonal line
xlabel('True Y');
ylabel('Observed Y');
title('True vs Observed Y');

% Display the plot
hold off;
