import statsmodels.api as sm
import numpy as np

# Example data
X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

# Adding a constant to the independent variable (intercept)
X = sm.add_constant(X)

# Fitting the linear regression model
model = sm.OLS(y, X).fit()

# Summary of the regression
summary = model.summary()

print(summary)
