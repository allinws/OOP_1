import pandas as pd

df = pd.read_csv('training_data.csv')

print(df['Duration'].describe().astype(int))