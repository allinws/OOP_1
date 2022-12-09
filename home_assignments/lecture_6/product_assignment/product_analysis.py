import pandas as pd


df = pd.read_csv('product_data.csv')


selected_dolumns = df[['StockCode', 'Description', 'UnitPrice', 'CustomerID', 'Country']]
print('\n Selecteed columns \n', selected_dolumns)

average_unit_price = df['UnitPrice'].mean()
print('\n Average unit price \n', round(average_unit_price))

average_order_quantity = df['Quantity'].mean()
print('\n Average order quantity \n', round(average_order_quantity))

average_order_value = round(average_unit_price * average_order_quantity)
print('\n Average order value \n', round(average_order_value))

orders_per_country = df[['Country', 'Quantity']].groupby('Country').sum()
print('\n Orders per country \n', orders_per_country)

df['TotalOrderValue'] = df['Quantity'] * df['UnitPrice']

order_value_per_country = df[['Country', 'TotalOrderValue']].groupby('Country').sum()
print('\n Order value per country \n', order_value_per_country)



