# Calculate the quartiles of co2_emission
quartiles = np.quantile(food_consumption['co2_emission'],[0,.25, 0.5, 0.75, 1])
print(quartiles)

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))