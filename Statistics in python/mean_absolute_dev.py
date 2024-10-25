import numpy as np


# Example dataset
data = [10, 15, 20, 25, 30]


# Calculate the mean
mean = np.mean(data)

# Calculate MAD
mad = np.mean(np.abs(data - mean))

print(f"Mean: {mean}")
print(f"Mean Absolute Deviation (MAD): {mad}")