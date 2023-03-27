import pandas as pd
import numpy as np
import csv

# Load the dataset
df = pd.read_csv('wine_data.csv')

# Remove all rows with null values
df.dropna(inplace=True)

# Remove all duplicate rows
df.drop_duplicates(inplace=True)

# Compute some basic statistical inferences
mean_inventory = df['inventory'].mean()
median_sales = df['sales'].median()
max_price_per_bottle = df['price_per_bottle'].max()
min_production_cost_per_bottle = df['production_cost_per_bottle'].min()

# Print the statistical inferences
print('Mean inventory: ', mean_inventory)
print('Median sales: ', median_sales)
print('Maximum price per bottle: ', max_price_per_bottle)
print('Minimum production cost per bottle: ', min_production_cost_per_bottle)

# Compute some basic statistical inferences of individual columns
inventory_stats = df['inventory'].describe()
sales_stats = df['sales'].describe()
price_stats = df['price_per_bottle'].describe()
production_cost_stats = df['production_cost_per_bottle'].describe()
print('=============================================================================================')
# Print the statistical inferences of individual columns
print('Inventory statistics: ', inventory_stats)
print('Sales statistics: ', sales_stats)
print('Price statistics: ', price_stats)
print('Production cost statistics: ', production_cost_stats)
print('=============================================================================================')

 #compute the total sales per producer
producer_sales = df.groupby('producer')['sales'].sum().sort_values(ascending=False)
print('Total sales per producer:')
print(producer_sales)
print('=============================================================================================')

# compute the median price per bottle and production cost per bottle per producer
producer_median_price = df.groupby('producer')['price_per_bottle'].median().sort_values()
producer_median_cost = df.groupby('producer')['production_cost_per_bottle'].median().sort_values()
print('\nMedian price per bottle per producer:')
print(producer_median_price)
print('\nMedian production cost per bottle per producer:')
print(producer_median_cost)
print('=============================================================================================')
# compute the inventory and sales per region
region_inventory = df.groupby('region')['inventory'].sum().sort_values(ascending=False)
region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)
print('\nTotal inventory per region:')
print(region_inventory)
print('\nTotal sales per region:')
print(region_sales)
print('=============================================================================================')
# compute the frequency of varietals
varietal_freq = df['varietal'].value_counts().sort_values()
print('\nFrequency of varietals:')
print(varietal_freq)
print('=============================================================================================')




