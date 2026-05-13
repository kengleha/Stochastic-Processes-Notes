# Kalman GPS
import numpy as np
import matplotlib.pyplot as plt

# Kalman Filter Initialization
initial_state = 0  # Initial position estimate
initial_estimate_error = 1  # Initial position estimate error
process_variance = .1  # Process noise (assumed constant)
measurement_variance = .02  # Measurement noise (GPS measurement error)

# Time step
dt = .01

# Lists to store results
true_positions = []
predicted_states = []
measurements = []
filtered_positions = []
true_position = 0
step_drift = 10

# Simulate vehicle motion
num_steps = 50
for step in range(num_steps):
    true_position = true_position + step * dt
    true_positions.append(true_position)



    # Kalman Filter Prediction (Time Update)
    predicted_state = initial_state + (step + step_drift) * dt + np.random.normal(0, np.sqrt(process_variance))
    predicted_states.append(predicted_state)
    
    predicted_estimate_error = initial_estimate_error + process_variance

    # Kalman Filter Update (Measurement Correction)
    if step > 20: 
        # Simulate GPS measurement with noise
        measurement = true_position + np.random.normal(0, np.sqrt(measurement_variance))
        
        kalman_gain = predicted_estimate_error / (predicted_estimate_error + measurement_variance)
        initial_state = predicted_state + kalman_gain * (measurement - predicted_state)
        initial_estimate_error = (1 - kalman_gain) * predicted_estimate_error
    else:
        measurement = 0
        initial_state = predicted_state   
   
    measurements.append(measurement)
    
    filtered_positions.append(initial_state)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(true_positions, label='True Position', color='blue')
plt.plot(predicted_states, label='A Priori Estimate', color='orange')
plt.plot(measurements, 'ro', label='GPS Measurements')
fp = np.append(0,filtered_positions)
#fp = fp[2:]
fp = fp[1:51]
plt.plot(fp, label='Filtered Position', color='green')
#plt.title('1D Kalman Filter for GPS Position Estimation')
plt.xlabel('Time Steps')
plt.ylabel('Position')
plt.legend()
plt.grid(True)
plt.show()

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(np.subtract(predicted_states,true_positions), label='A Priori Estimate', color='blue')
#fp = np.append(0,filtered_positions)
plt.plot(np.subtract(fp,true_positions), label='Filtered Position', color='orange')
#plt.title('1D Kalman Filter for GPS Position Estimation')
plt.xlabel('Time Steps')
plt.ylabel('Position Offset')
plt.legend()
plt.grid(True)
plt.show()
