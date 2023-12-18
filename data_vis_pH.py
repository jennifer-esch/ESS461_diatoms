import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm

diatom_data = pd.read_csv('pH_dataset.csv', header=None)
diatom_data.head()

Year = diatom_data[0]
pH = diatom_data[1]

pH_average = np.mean(pH)
pH_std = np.std(pH)

CTEs = [pH_average]
error = [pH_std]

plt.scatter(pH, Year)

plt.xlabel('Average Optimal pH value')
plt.ylabel('Approximate Age of Sample in Years')
plt.errorbar(pH, Year, xerr=error, linestyle='dotted')
plt.xlim = (min(pH), max(pH))
plt.yticks([1819,1855,1869,1905,1933,1966,1990,2019])
plt.title('Optimal pH range of Diatom Genera')
plt.gca().xaxis.set_ticks_position('top')
plt.gca().xaxis.set_label_position('top')

plt.show()




