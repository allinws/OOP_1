import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('gingerbread_data.csv')

print('Correlation is', df.corr())

print(df['gingerbread_sold'].corr(df['white_christmas_plays']))

df.plot(x='gingerbread_sold', y='white_christmas_plays', kind='scatter')
plt.show()

print(df.sum())



