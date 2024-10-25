import numpy as np

data = [10, 15, 20, 25, 30]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(f"IQR: {iqr}")