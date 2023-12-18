import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm
import math
from fractions import Fraction

cyclotella_data = pd.read_csv('cyclotella_abundance.csv', header=None)
cyclotella_data.head()

Year = cyclotella_data[0]
Abundance = cyclotella_data[1]

fraction_inside_sqrt = [Fraction(abundance * (100 - abundance), 100) for abundance in Abundance]
error_calc = [1.96 * math.sqrt(float(frac)) for frac in fraction_inside_sqrt]

error = [error_calc]

plt.scatter(Abundance, Year)

plt.xlabel('Abundance of Cyclotella')
plt.ylabel('Approximate Age of Sample in Year')
plt.title('Abundance of Cyclotella across Core')
plt.errorbar(Abundance, Year, xerr=error, linestyle='dotted')
plt.xlim = (min(Abundance), max(Abundance))
plt.yticks([1819,1855,1869,1905,1933,1966,1990,2019])
plt.gca().xaxis.set_ticks_position('top')
plt.gca().xaxis.set_label_position('top')

plt.show()