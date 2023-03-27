import pandas as pd

import matplotlib.pyplot as plt

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
# Plot the statistics
stats = pd.DataFrame(
    {'mean_inventory': [mean_inventory], 'median_sales': [median_sales], 'max_price_per_bottle': [max_price_per_bottle],
     'min_production_cost_per_bottle': [min_production_cost_per_bottle]})
stats.plot(kind='bar', figsize=(8, 6))
plt.title('Wine Statistics')
plt.xlabel('Statistic')
plt.ylabel('Value')
plt.show()

# Compute some basic statistical inferences of individual columns
inventory_stats = df['inventory'].describe()
sales_stats = df['sales'].describe()
price_stats = df['price_per_bottle'].describe()
production_cost_stats = df['production_cost_per_bottle'].describe()

# Combine the statistics into a single DataFrame
stats = pd.concat([inventory_stats, sales_stats, price_stats, production_cost_stats], axis=1)
stats.columns = ['inventory', 'sales', 'price_per_bottle', 'production_cost_per_bottle']

# Plot the Combine the statistics into a single DataFrame
stats.plot(kind='bar', figsize=(10, 6))
plt.title('Wine Statistics')
plt.xlabel('Statistic')
plt.ylabel('Value')
plt.show()

# compute the total sales per producer
producer_sales = df.groupby('producer')['sales'].sum().sort_values(ascending=False)

# Plot the total sales per producer
producer_sales.plot(kind='bar', figsize=(10, 6))
plt.title('Total Sales per Producer')
plt.xlabel('Producer')
plt.ylabel('Total Sales')
plt.show()

# compute the median price per bottle and production cost per bottle per producer
producer_median_price = df.groupby('producer')['price_per_bottle'].median().sort_values()
producer_median_cost = df.groupby('producer')['production_cost_per_bottle'].median().sort_values()

# Combine the median price and cost into a single DataFrame
producer_stats = pd.concat([producer_median_price, producer_median_cost], axis=1)
producer_stats.columns = ['Median Price per Bottle', 'Median Production Cost per Bottle']

# Plot the median price and cost per producer
producer_stats.plot(kind='bar', figsize=(10, 6))
plt.title('Median Price and Production Cost per Producer')
plt.xlabel('Producer')
plt.ylabel('Price/Cost')
plt.show()

# Compute the inventory and sales per region
region_inventory = df.groupby('region')['inventory'].sum().sort_values(ascending=False)
region_sales = df.groupby('region')['sales'].sum().sort_values(ascending=False)

# Combine the inventory and sales into a single DataFrame
region_stats = pd.concat([region_inventory, region_sales], axis=1)
region_stats.columns = ['Total Inventory', 'Total Sales']

# Plot the inventory and sales per region
region_stats.plot(kind='bar', figsize=(10, 6))
plt.title('Inventory and Sales per Region')
plt.xlabel('Region')
plt.ylabel('Inventory/Sales')
plt.show()
