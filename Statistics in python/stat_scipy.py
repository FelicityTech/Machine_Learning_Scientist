from scipy import stats

# Example data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Z-score (how many standard deviations an  element is from the mean)
z_scores = stats.zscore(data)

# T-test (tests whether the mean of two datasets is significantly different)
t_stat, p_value = stats.ttest_1samp(data, 5)


print(f"Z-scores: {z_scores}\nT-test: t-stat={t_stat}\np-value={p_value}")