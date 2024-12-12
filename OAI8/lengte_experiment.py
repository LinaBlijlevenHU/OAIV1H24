import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

lengtes = [200, 175, 178, 194, 190, 187, 180, 176, 175]

"""

17   5  8  6  5
18   0  7
19   0  4
20   0
"""

sns.histplot(lengtes)
plt.show()

print(f"Gemiddelde lengte: {np.mean(lengtes)}")
print(f"Mediaan lengte: {np.quantile(lengtes, 0.5)}")