import numpy as np
import matplotlib.pyplot as plt

# Constants
dt = 0.1  # Time step
num_steps = 100  # Number of time steps

# True trajectory (constant velocity)
true_position = np.zeros(num_steps)
true_velocity = np.ones(num_steps)
for i in range(1, num_steps):
    true_position[i] = true_position[i-1] + dt * true_velocity[i-1]

# Simulate noisy GPS measurements
gps_measurements = true_position + np.random.normal(0, 1, num_steps)

# Without Kalman Filter (just use last position as estimate)
no_kalman_estimate = np.zeros(num_steps)
no_kalman_estimate[0] = gps_measurements[0]
for i in range(1, num_steps):
    no_kalman_estimate[i] = no_kalman_estimate[i-1] + dt * true_velocity[i-1]

# With Kalman Filter
# Initialize variables
x_hat = np.zeros(num_steps)  # Estimated position
x_hat_minus = np.zeros(num_steps)  # A priori estimate
x_hat[0] = gps_measurements[0]
P = np.zeros(num_steps)  # Error covariance
P_minus = np.zeros(num_steps)  # A priori covariance
P[0] = 1

# Kalman Filter loop
for i in range(1, num_steps):
    # Prediction step (constant velocity model)
    x_hat_minus[i] = x_hat[i-1] + dt * true_velocity[i-1]
    P_minus[i] = P[i-1]

    # Update step (incorporate GPS measurement)
    K = P_minus[i] / (P_minus[i] + 1)  # Kalman gain
    x_hat[i] = x_hat_minus[i] + K * (gps_measurements[i] - x_hat_minus[i])
    P[i] = (1 - K) * P_minus[i]

# Introduce drift in the a priori estimate without using Kalman filter
drift_rate = 0.1

for i in range(1, num_steps):
    x_hat_minus[i] += drift_rate * i

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps), true_position, label='True Position', linestyle='--')
plt.plot(range(num_steps), gps_measurements, 'r.', label='GPS Measurements')
plt.plot(range(num_steps), no_kalman_estimate, 'g-', label='Estimate (No Kalman Filter)')
plt.plot(range(num_steps), x_hat, 'b-', label='Estimate (Kalman Filter)')
plt.xlabel('Time Step')
plt.ylabel('Position')
#plt.title('Effect of A Priori Estimate Drift without Kalman Filter')
plt.legend()
plt.grid(True)
plt.show()
