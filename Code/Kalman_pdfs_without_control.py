import numpy as np
import matplotlib.pyplot as plt

# Define initial conditions
prior_mean = 5.0  # Mean of a priori state estimate
prior_stddev = 1.0  # Standard deviation of a priori state estimate
measurement = 5.2  # Measurement value
measurement_stddev = 1.4  # Standard deviation of the measurement

# Generate a range of state values
state_values = np.linspace(0, 10, 1000)

# Calculate probability densities using numpy
prior_pdf = (1 / (prior_stddev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((state_values - prior_mean) / prior_stddev) ** 2)
measurement_pdf = (1 / (measurement_stddev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((state_values - measurement) / measurement_stddev) ** 2)

# Kalman predict (prior update)
# Assuming a simple constant velocity model
velocity = 1.0  # Constant velocity
predict_stddev = 0.5  # Standard deviation of the prediction

predicted_mean = prior_mean + velocity
predicted_stddev = np.sqrt(prior_stddev**2 + predict_stddev**2)

predicted_pdf = (1 / (predicted_stddev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((state_values - predicted_mean) / predicted_stddev) ** 2)

# Kalman update using the predicted state estimate
kalman_gain = predicted_stddev**2 / (predicted_stddev**2 + measurement_stddev**2)
posterior_mean = predicted_mean + kalman_gain * (measurement - predicted_mean)
posterior_stddev = np.sqrt((1 - kalman_gain) * predicted_stddev**2)

posterior_pdf = (1 / (posterior_stddev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((state_values - posterior_mean) / posterior_stddev) ** 2)

# Find the peaks of the densities
prior_peak = state_values[np.argmax(prior_pdf)]
measurement_peak = state_values[np.argmax(measurement_pdf)]
predicted_peak = state_values[np.argmax(predicted_pdf)]
posterior_peak = state_values[np.argmax(posterior_pdf)]

# Plot the probability densities
plt.figure(figsize=(10, 6))
plt.plot(state_values, prior_pdf, label='Prior state', color='blue')
plt.plot(state_values, predicted_pdf, label='Predicted (a priori) state estimate', color='orange')
plt.plot(state_values, measurement_pdf, label='Measurement ', color='green')
plt.plot(state_values, posterior_pdf, label='A posteriori state estimate', color='red')
plt.xlabel('State Values')
plt.ylabel('Probability Density')
plt.legend()

# Annotate the peaks without arrows
plt.text(prior_peak + 0.2, max(prior_pdf), r'$\mathbf{x}_{k-1|k-1}$', fontsize=12, color='blue')
plt.text(measurement_peak - 0.5, max(measurement_pdf), r'$\mathbf{z}_k$', fontsize=12, color='green')
plt.text(predicted_peak + 0.2, max(predicted_pdf), r'$\hat{\mathbf{x}}_{k|k-1}$', fontsize=12, color='orange')
plt.text(posterior_peak + 0.2, max(posterior_pdf), r'$\mathbf{\hat{x}}_{k|k}$', fontsize=12, color='red')
plt.ylim(0, 1.1)  # Set the y-axis range

#plt.title('Kalman Filter Predict and Update: Probability Density Estimation')
#plt.grid(True)
plt.show()

print(kalman_gain)
