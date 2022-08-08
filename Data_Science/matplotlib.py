#%matplotlib inline

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(129)
data_1 = np.random.normal(62, 13, 60)
data_2 = np.random.normal(55, 9, 60)

combined_data = [data_1, data_2]

# figure instance
fig = plt.figure(1, figsize=(9, 6))

# axes instance
ax = fig.add_subplot(111)

# draw boxplot
bxp = ax.boxplot(combined_data)
