#  Price Range Insights from Restaurant Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset
df = pd.read_csv("Dataset .csv")  # Make sure the filename is correct

# Display Available Columns
print("Available Columns in Dataset:\n", df.columns)

# Identify the Most Frequent Price Category
top_price_range = df["Price range"].mode()[0]
print("\nMost Frequent Price Range:", top_price_range)

# Calculate Average Ratings within Each Price Range
price_rating_avg = df.groupby("Price range")["Aggregate rating"].mean().round(2)
print("\nAverage Rating per Price Range:\n", price_rating_avg)

# Evaluate Average Rating by Rating Color
color_rating_avg = df.groupby("Rating color")["Aggregate rating"].mean().sort_values(ascending=False)
print("\nAverage Rating by Rating Color:\n", color_rating_avg)

# Bar Plot - Average Rating by Rating Color
plt.figure(figsize=(8, 5))
sns.barplot(x=color_rating_avg.index, y=color_rating_avg.values, palette="viridis")

plt.title("Average Rating by Rating Color", fontsize=14, fontweight='bold')
plt.xlabel("Rating Color", fontsize=12)
plt.ylabel("Average Rating", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Most Common Rating Color in Each Price Range
common_color_per_price = df.groupby("Price range")["Rating color"].agg(lambda x: x.value_counts().index[0])
print("\nDominant Rating Color for Each Price Range:\n", common_color_per_price)

# Visualize with Bar Chart
plt.figure(figsize=(9, 5))
sns.barplot(x=price_rating_avg.index, y=price_rating_avg.values, palette="coolwarm")
plt.title(" Average Ratings Across Price Ranges", fontsize=14, fontweight='bold')
plt.xlabel("Price Category")
plt.ylabel("Average User Rating")
plt.tight_layout()
plt.show()
