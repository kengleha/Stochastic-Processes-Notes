# DTW Example
import numpy as np
from dtw import *
import matplotlib.pyplot as plt

# Example usage
if __name__ == "__main__":
    # Generate two example time series
    N = 100      # Number of samples
    # Generate input signal x(n) - Assume a white Gaussian noise
    x = np.random.randn(N)
    # Generate desired signal y(n) - A sinusoidal signal corrupted by noise
    series1 = np.sin(2 * np.pi * 0.005 * np.arange(N))
    noise = 0.2 * np.random.randn(N)
    #series2 = series1 + noise
    series2 = np.sin(2 * np.pi * 0.006 * np.arange(N) )

    # Create DTW object
    alignment = dtw(series1, series2, keep_internals=True)

    # Calculate DTW distance
    alignment.plot(type="twoway")
    plt.show()

    dtw_distance = alignment.distance
    print("Time Series 1:", series1)
    print("Time Series 2:", series2)
    print("DTW Distance:", dtw_distance)