import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Dataset .csv")
data.columns = data.columns.str.strip()

# Convert rating to numeric safely
data['Aggregate rating'] = pd.to_numeric(data['Aggregate rating'], errors='coerce')
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')
data['Price range'] = pd.to_numeric(data['Price range'], errors='coerce')

# Drop rows with missing ratings
data = data.dropna(subset=['Aggregate rating'])

# Distribution of Ratings - Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data['Aggregate rating'], bins=10, kde=True, color='#2ca02c')  # green
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar plot of Rating Counts
rating_counts = data['Aggregate rating'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette='cubehelix')  # pastel cubehelix palette
plt.title("Rating Counts (Bar Plot)")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# Average Rating by Cuisine (Top 10)
data['Cuisines'] = data['Cuisines'].astype(str)
avg_rating_cuisine = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_cuisine.values, y=avg_rating_cuisine.index, palette="coolwarm")  # cool to warm gradient
plt.title("Top 10 Cuisines by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine")
plt.grid(True)
plt.tight_layout()
plt.show()

# Average Rating by City (Top 10)
avg_rating_city = data.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_city.values, y=avg_rating_city.index, palette="YlGnBu")  # yellow-green-blue palette
plt.title("Top 10 Cities by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.grid(True)
plt.tight_layout()
plt.show()

# Feature vs Rating: Price Range vs Rating
plt.figure(figsize=(8, 5))
sns.boxplot(x='Price range', y='Aggregate rating', data=data, palette="spring")  # spring color palette
plt.title("Aggregate Rating by Price Range")
plt.grid(True)
plt.tight_layout()
plt.show()

# Feature vs Rating: Votes vs Rating (Scatter)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Votes', y='Aggregate rating', data=data, alpha=0.6, color='#1f77b4')  # blue tone
plt.title("Votes vs Aggregate Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.grid(True)
plt.tight_layout()
plt.show()
