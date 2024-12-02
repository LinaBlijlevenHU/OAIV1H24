import matplotlib.pyplot as plt
import seaborn as sns

# Kleurtjes
sns.color_palette("bright")

# Datapunten
X = [1, 2, 3, 4]
y = [4, 7, 8, 15]

# Mogelijke voorspellingen
y1 = [3 + 4 * xi for xi in X]
y2 = [4 + 3 * xi for xi in X]

# Plot de originele datapunten
sns.scatterplot(x=X, y=y)
# Plot 3 + 4x voorspelling
sns.lineplot(x=X, y=y1, label="y1 = 3 + 4x")
# Plot 4 + 3x voorspelling
sns.lineplot(x=X, y=y2, label="y2 = 4 + 3x")
plt.show()