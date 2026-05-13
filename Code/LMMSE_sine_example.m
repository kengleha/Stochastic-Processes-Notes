% Parameters
f1 = 1;         % Frequency of signal_1 (in Hz)
f2 = 3;         % Frequency of signal_2 (in Hz)
A1 = 1;         % Amplitude of signal_1
A2 = 0.5;       % Amplitude of signal_2
noise_std = 0.3; % Standard deviation of Gaussian noise

% Time vector
t = 0:0.01:5;

% True signals
signal_1 = A1 * sin(2 * pi * f1 * t);
signal_2 = A2 * cos(2 * pi * f2 * t);
noise = noise_std * randn(size(t));

% Observed signal
X_observed = signal_1 + signal_2 + noise;

% Linear MMSE estimation
cov_X_signal_1 = cov(X_observed, signal_1);
var_X_observed = var(X_observed);

A = cov_X_signal_1 / var_X_observed;
A = A(1,2);

signal_1_estimate = A * X_observed;

% Plotting
figure;

subplot(2, 1, 1);
plot(t, signal_1, 'b', 'LineWidth', 2);
title('True Signal 1');
xlabel('Time');
ylabel('Amplitude'); hold on
plot(t, X_observed, 'r', 'LineWidth', 1.5);
title('Observed Signal (X_{observed})');
xlabel('Time');
ylabel('Amplitude');

subplot(2, 1, 2);
plot(t, signal_1, 'b', 'LineWidth', 2, 'DisplayName', 'True Signal 1');
hold on;
plot(t, X_observed, 'r', 'LineWidth', 1.5);
title('Observed Signal (X_{observed})');
xlabel('Time');
ylabel('Amplitude');
plot(t, signal_1_estimate, 'g--', 'LineWidth', 1.5, 'DisplayName', 'Estimated Signal 1');
title('Linear MMSE Estimation');
xlabel('Time');
ylabel('Amplitude');
legend();

sgtitle('Linear MMSE Estimation Example');
