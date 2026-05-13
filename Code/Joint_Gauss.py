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

# Create the bivariate normal distribution
mvn = multivariate_normal(mean=mean, cov=covariance)

# Calculate the bivariate PDF
Z = mvn.pdf(pos)

# Plot the bivariate PDF using a mesh plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)  # Set alpha value for translucency

# Shade the area under the curve for X and Y bounds
x_shade = np.linspace(1, 5, 100)
y_shade = np.linspace(1, 3, 100)
X_shade, Y_shade = np.meshgrid(x_shade, y_shade)
ax.plot_surface(X_shade, Y_shade, np.zeros_like(X_shade), color='skyblue', alpha=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('Bivariate Gaussian PDF')

plt.show()
