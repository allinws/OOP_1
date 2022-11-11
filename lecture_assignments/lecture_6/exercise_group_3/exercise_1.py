import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('training_data.csv')

print('Correlation is', df.corr())

df.plot(x='Duration', y='Calories', kind='scatter')
plt.show()
