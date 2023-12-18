import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib.cm

diatom_data = pd.read_csv('nutrient_quality.csv', header=None)
diatom_data.head()

Year = diatom_data[0]
nutrient = diatom_data[1]

nutrient_std = np.std(nutrient)
error = [nutrient_std]

plt.scatter(nutrient, Year)

plt.xlabel('Average Optimal Nutrient Level')
plt.ylabel('Approximate Age of Sample in Years')
plt.errorbar(nutrient, Year, xerr=error, linestyle='dotted')
plt.xlim = (min(nutrient), max(nutrient))
plt.yticks([1819,1855,1869,1905,1933,1966,1990,2019])
plt.title('Optimal Nutrient Conditions for Diatom Genera')
plt.gca().xaxis.set_ticks_position('top')
plt.gca().xaxis.set_label_position('top')

plt.show()
