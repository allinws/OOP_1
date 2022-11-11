import pandas as pd

df = pd.read_csv('product_example.csv')

print(df)

print(df['product'].describe())

print(df[['product', 'price', ]].groupby('product').sum())

print(df[['product', 'price', ]].groupby('product').mean().astype(int))

print(df[['product', 'price', 'year' ]].groupby('year').sum())
