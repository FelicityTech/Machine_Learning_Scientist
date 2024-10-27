import numpy  as np

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 100]


q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)


# Calculate IQR
iqr = q3 - q1

# calculate lower and upper bonds for detecting outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Identify outliers
outliers = [x for x in data if x < lower or x > upper]

print(f"Outlier: {outliers}")