import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv("amazon.csv")
# Display the data
print(data)
# Get information about the data
data.info()
# Generate descriptive statistics
data.describe()
# Calculate the number of missing values in each column
df1 = data.isnull().sum()
print(df1)
# Get unique categories
df2 = data["category"].unique()
print(df2)
# Group the data by category and calculate the sum of ratings for each category
df3 = data.groupby("category")["rating"].sum()
print(df3)
# Count the number of products in each category and sort them
df4 = data["category"].value_counts().sort_values()
print(df4)
# Group the data by category and calculate the sum of actual_price and discounted_price for each category
df5 = data.groupby(["category"])[["actual_price", "discounted_price"]].sum()
print(df5)
# Plotting Total rating of each category of products
plt.figure(figsize=(16, 8))
plt.bar('category', 'rating', data=data)
plt.ylabel('rating')
plt.xlabel('category')
plt.title('Total rating of each category of products', fontsize=20)
plt.show()
# Plotting a pie chart for the number of products in each category
plt.pie(df4, labels=df4.index)
plt.show()
# Plotting Actual_price Vs Discounted_price
plt.figure(figsize=(16, 8))
plt.bar('actual_price', 'discounted_price', data=data)
plt.ylabel('actual_price')
plt.xlabel('discounted_price')
plt.title('Actual_price Vs Discounted_price', fontsize=20)
plt.show()
