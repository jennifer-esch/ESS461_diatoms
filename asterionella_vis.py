import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm
import math
from fractions import Fraction

asterionella_data = pd.read_csv('asterionella_abundance.csv', header=None)
asterionella_data.head()

Year = asterionella_data[0]
Abundance = asterionella_data[1]

fraction_inside_sqrt = [Fraction(abundance * (100 - abundance), 100) for abundance in Abundance]
error_calc = [1.96 * math.sqrt(float(frac)) for frac in fraction_inside_sqrt]

error = [error_calc]

plt.scatter(Abundance, Year)

plt.xlabel('Abundance of Asterionella')
plt.ylabel('Approximate Age of Sample in Year')
plt.errorbar(Abundance, Year, xerr=error, linestyle='dotted')
plt.xlim = (min(Abundance), max(Abundance))
plt.yticks([1819,1855,1869,1905,1933,1966,1990,2019])
plt.title('Abundance of Asterionella across Core')
plt.gca().xaxis.set_ticks_position('top')
plt.gca().xaxis.set_label_position('top')

plt.show()
