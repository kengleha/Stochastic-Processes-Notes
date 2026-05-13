import numpy as np
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

# Generate synthetic mixed EMG signals
np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)
s2 = np.sign(np.sin(3 * time))
s3 = np.abs(2 * time)

S = np.c_[s1, s2, s3]
S += 0.8 * np.random.normal(size=S.shape)  # Add noise

# Mix data
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # Mixing matrix
X = np.dot(S, A.T)

# Run ICA
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X)  # Reconstructed sources

# Plot the original and separated EMG signals
plt.figure()
plt.subplot(3, 1, 1)
plt.title('Original Signal 1')
plt.plot(S[:,0])

plt.subplot(3, 1, 2)
plt.title('Original Signal 2')
plt.plot(S[:,1])


plt.subplot(3, 1, 3)
plt.title('Original Signal 3')
plt.plot(S[:,2])
plt.show()


plt.figure()
plt.subplot(3, 1, 1)
plt.title('Seperated Signal 1')
plt.plot(S_[:,0])

plt.subplot(3, 1, 2)
plt.title('Seperated Signal 1')
plt.plot(S_[:,1])


plt.subplot(3, 1, 3)
plt.title('Seperated Signal 1')
plt.plot(S_[:,2])
plt.show()
