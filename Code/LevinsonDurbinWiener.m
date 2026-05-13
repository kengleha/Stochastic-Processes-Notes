% Parameters
N = 500;        % Number of samples
M = 50;         % Filter order (one less than the matrix size)

% Generate input signal x(n) - A sinusoidal signal
true_signal = sin(2 * pi * 0.05 * (1:N));

% Generate white Gaussian noise
noise_power = 0.1;
noise = sqrt(noise_power) * randn(1, N);

% Generate observed signal y(n) - True signal corrupted by noise
y = true_signal + noise;

% Compute autocorrelation matrix R and cross-correlation vector p
R = toeplitz(y(M:N-1), y(M:-1:1));  % Autocorrelation matrix
p = y(M+1:N) * y(M:-1:1)';          % Cross-correlation vector

% Calculate optimal filter weights
w_optimal = inv(R) * p;

% Apply the Wiener filter to the noisy input signal
x_hat = filter(w_optimal, 1, y(M+1:N));

% Plot the results
figure;

subplot(3,1,1);
plot(1:N, true_signal);
title('True Signal');

subplot(3,1,2);
plot(1:N, y);
title('Observed Signal (Noisy)');

subplot(3,1,3);
plot(M+1:N, x_hat);
title('Wiener Filtered Signal');

legend('True Signal', 'Observed Signal', 'Wiener Filtered Signal');
