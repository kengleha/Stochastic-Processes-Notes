% Function to create a lowpass time series
function signal = lowpass_signal(num_samples)
    t = linspace(0, 1, num_samples);
    signal = sin(2 * pi * t) + 0.5 * sin(6 * pi * t);
    signal = randn(1,num_samples);
    signal = filter(ones(1, 10)/10, 1, signal);  % Simple moving average as a lowpass filter
end

% Function to compute and plot autocorrelation function
function plot_autocorrelation(time_series, window_sizes)
    lags = -floor(length(time_series)/2):floor(length(time_series)/2);

    figure;
   % plot(lags, xcorr(time_series, time_series, 'coeff'), 'LineWidth', 2, 'Color', 'k');
    hold on;

    for i = 1:length(window_sizes)
        window_size = window_sizes(i);
        autocorr_estimate = xcorr(time_series, time_series, 'coeff');
        autocorr_estimate = autocorr_estimate(length(time_series):length(time_series) + window_size);
        
        % Normalize the estimate
        autocorr_estimate = autocorr_estimate / max(autocorr_estimate);

        % Adjust the x-axis values to center around zero
        lag_values = (-floor(window_size/2):floor(window_size/2));

        plot(lag_values, autocorr_estimate); hold on
    end

    hold off;
    title('Autocorrelation Function with Lowpass Time Series');
    xlabel('Time Lag');
    ylabel('Autocorrelation');
    legend('True Autocorrelation', 'Location', 'Best');
    grid on;
end

% Generate a lowpass time series
num_samples = 5000;
lowpass_time_series = lowpass_signal(num_samples);

% Compute and plot autocorrelation with three different window lengths
window_sizes = [50, 100, 200];
plot_autocorrelation(lowpass_time_series, window_sizes);
