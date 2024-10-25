## Measurement of Spread with outlier

### Observation:
Range: Increases significantly with the outlier since it only depends on the maximum and minimum values.
IQR: May increase slightly but isd robusts to outliers since it focused on the middle 50% of the data.
Variance and Standard Deviation: These increase drastically with the outlier, showing the sensitivity of these measures to extreme values.

Summary:
1. Range and Standard Deviation are sensitive to outliers.
2. IQR is more resistant to outliers and is a better measure of spread for skewed data.
3. Variance gives insight into how spread out the data is but can be influenced by extreme values.


## Mean Absolute Deviation (MAD) with Outlier

Observation:
1. The MAD increases when the outlier is added, but not as drastically as the Standard Deviation. This shows how MAD is more robust and less sensitive to outliers.

### When to Use MAD:
1. When your data contains outliers and you want a measure of spread that isn't as heavily influenced.
2. When you need a simple, interpretable statistic for average deviation from mean