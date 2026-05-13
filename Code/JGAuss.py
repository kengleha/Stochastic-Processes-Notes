import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# Parameters
mu_x = 3
mu_y = 2
var_x = 4
var_y = 1
cov_xy = 1.5

# Define the mean vector and covariance matrix
mean = [mu_x, mu_y]
covariance = [[var_x, cov_xy], [cov_xy, var_y]]

# Create a grid of x and y values
x = np.linspace(0, 5, 100)
y = np.linspace(0, 4, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))


x1 = np.linspace(1, 5, 100)
y1 = np.linspace(1, 3, 100)
X1, Y1 = np.meshgrid(x1, y1)
pos1 = np.dstack((X1, Y1))

# Create the bivariate normal distribution
mvn = multivariate_normal(mean=mean, cov=covariance)

# Calculate the bivariate PDF
Z = mvn.pdf(pos)
Z1 = mvn.pdf(pos1)

# Plot the bivariate PDF using a mesh plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='copper', alpha=0.7)  # Set alpha value for translucency
ax.plot_surface(X1, Y1, Z1+0.001, cmap='Blues', alpha=0.9)  # Set alpha value for translucency

# Shade the area under the curve for X and Y bounds
x_shade = np.linspace(1, 5, 100)
y_shade = np.linspace(1, 3, 100)
X_shade, Y_shade = np.meshgrid(x_shade, y_shade)
ax.plot_surface(X_shade, Y_shade, np.zeros_like(X_shade), color='skyblue', alpha=1)

# Draw vertical dashed lines from the corners of the shaded region to the mesh plot
#ax.plot([1, 1], [1, 1], [0, 0.06], color='blue', linestyle='--')  # Left vertical dashed line
#ax.plot([5, 5], [1, 1], [0, 0.06], color='blue', linestyle='--')  # Right vertical dashed line
#ax.plot([1, 1], [3, 3], [0, 0.06], color='blue', linestyle='--')  # Bottom vertical dashed line
#ax.plot([5, 5], [3, 3], [0, 0.06], color='blue', linestyle='--')  # Top vertical dashed line


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('Bivariate Gaussian PDF')

plt.show()
