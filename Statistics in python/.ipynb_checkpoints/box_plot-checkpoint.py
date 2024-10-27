import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 15, 20, 25, 30, 35, 40, 45, 50]


# create a box plot

sns.boxplot(data=data)
plt.title('Box Plot of Data')
plt.show()