import numpy as np

# dataset

data = [10, 15, 20, 25, 30, 35, 40, 45, 50]


# Calculate Q1, Q2 (median), and Q3
q1 = np.percentile(data, 25) # First quartile (25th percentile)
median = np.percentile(data, 50) # Median (50th percentile)
q3 = np.percentile(data, 75) # Third quartile (75th percentile)


# Interquartile Range (IQR)
iqr = q3 - q1


print(f"Q1 (25th percentile): {q1}")
print(f"Median (50th percentile): {median}")
print(f"Q3 (75th percentile): {q3}")
print(f"Interquatile Range (IQR): {iqr}")

percentile_90= np.percentile(data, 90)
print(f"90th Percentile: {percentile_90}")