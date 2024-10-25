import numpy as np
data_with_outlier = [10, 15, 20, 25, 30, 100]



# Range
range_with_outlier = max(data_with_outlier) - min(data_with_outlier)


# IQR
q1_with_outlier = np.percentile(data_with_outlier, 25)
q3_with_outlier = np.percentile(data_with_outlier, 75)
iqr_with_outlier = q3_with_outlier - q1_with_outlier



# Variance and Standard Deviation
variancer_with_outlier = np.var(data_with_outlier)
std_dev_with_outlier = np.std(data_with_outlier)


print(f"Range with Outlier: {range_with_outlier}")
print(f"IQR with Outlier: {iqr_with_outlier}")
print(f"Variance with Outlier: {variancer_with_outlier}")
print(f"Standard Deviation with Outlier: {std_dev_with_outlier}")