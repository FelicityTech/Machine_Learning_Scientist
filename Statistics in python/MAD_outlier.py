import numpy as np

data_with_outlier = [10, 15, 20, 25, 30, 100]

# Calculate mean and MAD with the outlier
mean_with_outlier = np.mean(data_with_outlier)
mad_with_outlier = np.mean(np.abs(data_with_outlier - mean_with_outlier))

# Compare Standard Deviation for reference
std_dev_outlier = np.std(data_with_outlier)

print(f"Mean with Outlier: {mean_with_outlier}")
print(f"Mean Absolute Deviation (MAD) with Outlier: {mad_with_outlier}")
print(f"Standard Deviation with Outlier: {std_dev_outlier}")