% Parameters
f = 2;          % Frequency of the true sinusoidal signal (in Hz)
A = 1;          % Amplitude of the true sinusoidal signal
noise_std = 0.2; % Standard deviation of Gaussian noise

% Time vector
t = 0:0.01:5;

% True signal (sinusoidal)
true_signal = A * sin(2 * pi * f * t);

% Generate additive white Gaussian noise
noise = noise_std * randn(size(t));

% Observed signal (true signal + noise)
observed_signal = true_signal + noise;

% Linear MMSE estimation (3rd order)
N = length(t);
X = [ones(N, 1), t', t'.^2, t'.^3]; % Design matrix

% Calculate optimal coefficients using the linear MMSE formula
A_optimal = (X' * X) \ (X' * observed_signal');

% Estimated signal using the 3rd-order linear MMSE estimator
estimated_signal = X * A_optimal;

% Plotting
figure;

subplot(2, 1, 1);
plot(t, true_signal, 'b', 'LineWidth', 2);
title('True Sinusoidal Signal');
xlabel('Time');
ylabel('Amplitude');

subplot(2, 1, 2);
plot(t, observed_signal, 'r', 'LineWidth', 1.5);
hold on;
plot(t, estimated_signal, 'g--', 'LineWidth', 1.5);
title('Linear MMSE Estimation (3rd Order)');
xlabel('Time');
ylabel('Amplitude');
legend('Observed Signal', 'Estimated Signal');

sgtitle('Example of 3rd Order Linear MMSE Estimation');