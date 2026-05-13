% Parameters
sigma_z = 1;  % Variance of Z
sigma_w = 0.5;  % Variance of W
sigma_x = 0.8;  % Variance of X

% Generate a time vector
t = 0:0.1:10;

% Generate the random process Z
Z = randn(size(t)) * sqrt(sigma_z);

% Generate white Gaussian noise W
W = randn(size(t)) * sqrt(sigma_w);

% Form the observed signal X
X = Z + W;

% Calculate the optimal coefficient A
A = sigma_z^2 / (sigma_z^2 + sigma_w^2);

% Compute the MMSE estimate of Z
Z_hat = A * X;

% Plot the signals
figure;
plot(t, Z, 'b', 'LineWidth', 2, 'DisplayName', 'Z(t)');
hold on;
plot(t, X, 'r', 'LineWidth', 1.5, 'DisplayName', 'X(t)');
plot(t, Z_hat, 'g--', 'LineWidth', 1.5, 'DisplayName', 'Estimated Z(t)');
legend();
xlabel('Time');
ylabel('Amplitude');
title('MMSE Estimation Example');
grid on;

MSE = mean((Z_hat-Z).^2)