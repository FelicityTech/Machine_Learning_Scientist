import pandas as pd


# Example data as a pandas series

data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Mean
mean = data.mean()

# Median
median = data.median()

# Standard deviation
std_dev = data.std()

# Variance

variancce = data.var()


print(f"Mean: {mean}\nMedian: {median}\nStd Dev: {std_dev}\nVariance: {variancce}")