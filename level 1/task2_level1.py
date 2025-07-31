# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
ds = pd.read_csv('Dataset .csv')  

# Check basic info
print("\n Dataset Info:")
print(ds.info())

# Check for missing values
print("\n Missing Values in Each Column:")
print(ds.isnull().sum())

# Convert 'Aggregate rating' to float safely
ds["Aggregate rating"] = pd.to_numeric(ds["Aggregate rating"], errors='coerce')

# Descriptive Stats for Numerical Columns
print("\n Descriptive Statistics (Numerical):")
print(ds.describe())

# Central Tendency & Spread
print("\n Mean:\n", ds.mean(numeric_only=True))
print("\n Median:\n", ds.median(numeric_only=True))
print("\n Standard Deviation:\n", ds.std(numeric_only=True))
print("\n Variance:\n", ds.var(numeric_only=True))

# Unique Counts for Categorical Columns
print("\n Unique Values in 'Country Code':", ds['Country Code'].nunique())
print(" Unique Cities:", ds['City'].nunique())
print(" Unique Cuisines:", ds['Cuisines'].nunique())

# Frequency distribution of categorical columns
print("\n Country Code Distribution:\n", ds['Country Code'].value_counts())
print("\n City Distribution:\n", ds['City'].value_counts())
print("\n Cuisines Distribution:\n", ds['Cuisines'].value_counts())

# Top 10 Cities with most restaurants
top_cities = ds['City'].value_counts().head(10)
print("\n Top 10 Cities:\n", top_cities)

# Top 10 Cuisines
top_cuisines = ds['Cuisines'].value_counts().head(10)
print("\n Top 10 Cuisines:\n", top_cuisines)

# Bar plot for top 10 cities
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Pie chart for top 10 cuisines
plt.figure(figsize=(8, 8))
top_cuisines.head(10).plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Top 5 Cuisines Distribution")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisines")
plt.tight_layout()
plt.show()

# Correlation matrix for numerical columns
plt.figure(figsize=(8, 6))
sns.heatmap(ds.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()
