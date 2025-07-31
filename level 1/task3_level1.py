# Geospatial Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
ds = pd.read_csv("Dataset .csv")

# Check actual column names
print("Columns in the dataset:")
print(ds.columns)

# Fix column names below as needed
ds = ds.dropna(subset=['Latitude', 'Longitude', 'Aggregate rating'])

# Plotting restaurant locations
plt.figure(figsize=(10, 6))
sns.set_style("darkgrid")
sns.scatterplot(data=ds, x='Longitude', y='Latitude', hue='Aggregate rating', palette='cubehelix', alpha=0.6)
plt.title("Restaurant Locations with Ratings")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Rating")
plt.grid(True)
plt.show()

# Distribution across Cities
top_cities = ds['City'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="Set2")  
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.show()

#Distribution across country
# Map Country Code to Country Name
country_map = {
    1: "India", 14: "Australia", 30: "Brazil", 37: "Canada", 94: "Indonesia",
    148: "New Zealand", 162: "Philippines", 166: "Qatar", 184: "Singapore",
    189: "South Africa", 191: "Sri Lanka", 208: "Turkey", 214: "UAE",
    215: "United Kingdom", 216: "United States"
}
ds['Country'] = ds['Country Code'].map(country_map)

# Plot restaurant distribution by country
# Plot restaurant distribution by country
country_counts = ds['Country'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="Set3")  
plt.title("Restaurants by Country")
plt.xlabel("Number of Restaurants")
plt.ylabel("Country")
plt.tight_layout()
plt.show()


# Top rateted cities are
top_rated_cities = ds.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_rated_cities.values, y=top_rated_cities.index, palette='magma')
plt.title("Top 10 Cities by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.tight_layout()
plt.show()

# Correlation between location & rating
corr = ds[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print("\nCorrelation Matrix:\n", corr)
sns.heatmap(corr, annot=True, cmap='cividis')
plt.title("Correlation Between Location & Rating")
plt.tight_layout()
plt.show()
