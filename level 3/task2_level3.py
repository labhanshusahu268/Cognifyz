import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("Dataset .csv")

# Step 1: Data Cleaning and Preparation
data.columns = data.columns.str.strip()

# Clean and normalize 'Cuisines' column
data['Cuisines'] = data['Cuisines'].astype(str).str.strip()
data['Cuisines'] = data['Cuisines'].str.replace('&amp;', '&', regex=False)

# Convert 'Aggregate rating' and 'Votes' to numeric
data['Aggregate rating'] = pd.to_numeric(data['Aggregate rating'], errors='coerce')
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')

# Drop rows with missing values in key columns
initial_rows = len(data)
data.dropna(subset=['Cuisines', 'Aggregate rating', 'Votes'], inplace=True)
dropped_rows = initial_rows - len(data)
if dropped_rows > 0:
    print(f"Dropped {dropped_rows} rows with missing values in 'Cuisines', 'Aggregate rating', or 'Votes'.")

# Step 2: Grouping and Aggregation
# Average Rating by Cuisine
avg_rating_by_cuisine = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

# Total Votes by Cuisine
total_votes_by_cuisine = data.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)

# Filter cuisines with high average rating
high_rating_cuisines = avg_rating_by_cuisine[avg_rating_by_cuisine > 4.0]

# Step 3: Display Insights
print("\n Top 10 Cuisines by Average Rating:\n", avg_rating_by_cuisine.head(10))
print("\n Top 10 Most Popular Cuisines by Votes:\n", total_votes_by_cuisine.head(10))
print("\n Cuisines with High Average Rating (> 4.0):\n", high_rating_cuisines)

# Step 4: Visualization
# Prepare figure and axes
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Top 10 Cuisines by Average Rating
top10_ratings = avg_rating_by_cuisine.head(10)
sns.barplot(x=top10_ratings.values, y=top10_ratings.index, palette='crest', ax=axes[0])
axes[0].set_title("Top 10 Cuisines by Average Rating", fontsize=16)
axes[0].set_xlabel("Average Rating")
axes[0].set_ylabel("Cuisine")

# Top 10 Cuisines by Total Votes
top10_votes = total_votes_by_cuisine.head(10)
sns.barplot(x=top10_votes.values, y=top10_votes.index, palette='mako', ax=axes[1])
axes[1].set_title("Top 10 Most Popular Cuisines (by Votes)", fontsize=16)
axes[1].set_xlabel("Total Votes")
axes[1].set_ylabel("Cuisine")

plt.tight_layout()
plt.show()
