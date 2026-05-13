# Kalman Limb Control
import numpy as np
import matplotlib.pyplot as plt

# Kalman Filter Initialization
initial_state = np.array([0.0, 0.0])  # Initial joint angles (e.g., shoulder and elbow)
initial_estimate_error = np.array([0.01, 0.01])  # Initial estimate error for joint angles
process_variance = np.array([0.01, 0.01])  # Process noise (uncertainty in joint angle changes)
measurement_variance = np.array([0.01, 0.01])  # Measurement noise (visual and proprioceptive feedback)

# Time step
dt = 0.1

# Internal Model Forgotting factor
forget = 0.5

# Lists to store results
true_positions = []
measurements = []
filtered_positions = []
predicted_positions = []


# Simulate arm movement
num_steps = 50
for step in range(num_steps):
    if step > 0:
        delta = posterior_state - predicted_state
        initial_state = posterior_state + delta*forget + np.random.normal(0, np.sqrt(process_variance))
        #initial_state = posterior_state 

    # Kalman Filter Prediction (Time Update)
    predicted_state = initial_state  # Simplified prediction as no control input (Bk) is considered
    predicted_positions.append(predicted_state)
    predicted_estimate_error = initial_estimate_error + process_variance
    
    # Simulate true joint angles (ground truth)
    true_state = np.array([np.sin(step * 0.1), np.cos(step * 0.1)]) * 2.0
    true_positions.append(true_state)

    # Simulate noisy measurements with visual and proprioceptive feedback
    measurement = true_state + np.random.normal(0, np.sqrt(measurement_variance))
    measurements.append(measurement)


    # Kalman Filter Update (Measurement Correction)
    kalman_gain = predicted_estimate_error / (predicted_estimate_error + measurement_variance)
    posterior_state = predicted_state + kalman_gain * (measurement - predicted_state)
    posterior_estimate_error = (1 - kalman_gain) * predicted_estimate_error

    filtered_positions.append(posterior_state)

# Convert lists to arrays for easier indexing
true_positions = np.array(true_positions)
measurements = np.array(measurements)
filtered_positions = np.array(filtered_positions)
predicted_positions = np.array(predicted_positions)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(true_positions[:, 0], label='True Shoulder Angle', color='blue')
plt.plot(predicted_positions[:, 0], label='Predicted Shoulder Angle', color='orange')
plt.plot(measurements[:, 0], 'ro', label='Noisy Shoulder Measurement')
plt.plot(filtered_positions[:, 0], label='Filtered Shoulder Angle', color='green')
plt.title('Kalman Filter in Human Arm Movement Control')
plt.xlabel('Time Steps')
plt.ylabel('Joint Angles')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(true_positions[:, 1], label='True Elbow Angle', color='blue')
plt.plot(predicted_positions[:, 1], label='Predicted Elbow Angle', color='orange')
plt.plot(measurements[:, 1], 'ro', label='Noisy Elbow Measurement')
plt.plot(filtered_positions[:, 1], label='Filtered Elbow Angle', color='green')
plt.title('Kalman Filter in Human Arm Movement Control')
plt.xlabel('Time Steps')
plt.ylabel('Joint Angles')
plt.legend()
plt.grid(True)
plt.show()

