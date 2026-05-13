% Parameters
N = 100;   % Number of samples
M = 10;    % Filter order

% Generate input signal x(n) - Assume a white Gaussian noise
x = randn(1, N);

% Generate desired signal y(n) - A sinusoidal signal corrupted by noise
true_signal = sin(2 * pi * 0.05 * (0:N-1));
noise = 0.2 * randn(1, N);
y = true_signal + noise;

% Compute the autocorrelation matrix Rxx
Rxx = xcorr(x, x);
Rxx = toeplitz(Rxx);
Rxx = Rxx(1:2*M+1,1:2*M+1);
% Compute the cross-correlation vector Rxy
Rxy = xcorr(x, y, M, 'coeff');

% Solve the Wiener-Hopf equations to find the filter coefficients
h = pinv(Rxx) * Rxy';

filtered_signal = filtfilt(h,1,x);

% Plot the signals
figure;

subplot(3, 1, 1);
plot(true_signal);
title('True Signal');

subplot(3, 1, 2);
plot(x);
title('Input Signal x(n)');

subplot(3, 1, 3);
plot(y);
hold on;
plot(filtered_signal)
title('Noisy Signal y(n) and Wiener Filter Coefficients');
legend('Noisy Signal', 'Filtered Signal');

