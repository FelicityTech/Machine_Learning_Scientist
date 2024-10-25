import numpy as np
from scipy import stats

# Original dataset

data  = [10, 15, 20, 25, 30]

# Adding an outlier
data_with_outlier = [10, 15, 20, 25, 30, 100]


# Mode 
mean_original = np.mean(data)
mean_with_outlier = np.mean(data_with_outlier)


# Median
median_original = np.median(data)
median_with_outlier = np.median(data_with_outlier)


# Mode (both set are multimodal)

mode_original = stats.mode(data)
mode_with_outlier = stats.mode(data_with_outlier)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
print(f"Original Mean: {mean_original}, mean with Outlier: {mean_with_outlier}\n")
print(f"Original Median: {median_original}, median with Outlier: {median_with_outlier}\n")
print(f"Original Mode: {mode_original.mode[0]}, Mode with Outlier: {mode_with_outlier.mode[0]}")