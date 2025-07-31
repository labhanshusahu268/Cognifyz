import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for all plots
sns.set(style="whitegrid", palette="Set2")

# Load dataset
data = pd.read_csv("Dataset .csv")
data.columns = data.columns.str.strip()

# Clean 'Cuisines' column and handle special characters
data['Cuisines'] = data['Cuisines'].astype(str).str.strip()
data['Cuisines'] = data['Cuisines'].str.replace('&amp;', '&', regex=False)

# Convert 'Aggregate rating' and 'Votes' to numeric
data['Aggregate rating'] = pd.to_numeric(data['Aggregate rating'], errors='coerce')
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')

# Drop missing values
initial_rows = len(data)
data.dropna(subset=['Cuisines', 'Aggregate rating', 'Votes'], inplace=True)
print(f"Dropped {initial_rows - len(data)} rows with missing values.")

#  Average rating by cuisine
avg_rating = data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

#  Total votes by cuisine
total_votes = data.groupby('Cuisines')['Votes'].sum().sort_values(ascending=False)

#  Cuisines with high average ratings (> 4.0)
high_rating_cuisines = avg_rating[avg_rating > 4.0]

#  Display Top 10
print("\n Top 10 Cuisines by Average Rating:")
print(avg_rating.head(10))

print("\n Top 10 Most Popular Cuisines by Total Votes:")
print(total_votes.head(10))

print("\n Cuisines with Average Rating > 4.0:")
print(high_rating_cuisines)

#  Visualization
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Top 10 by Rating
sns.barplot(
    x=avg_rating.head(10).values,
    y=avg_rating.head(10).index,
    ax=axes[0],
    palette='viridis'
)
axes[0].set_title("Top 10 Cuisines by Average Rating", fontsize=16)
axes[0].set_xlabel("Average Rating")
axes[0].set_ylabel("Cuisine")

# Top 10 by Votes
sns.barplot(
    x=total_votes.head(10).values,
    y=total_votes.head(10).index,
    ax=axes[1],
    palette='magma'
)
axes[1].set_title("Top 10 Most Popular Cuisines by Total Votes", fontsize=16)
axes[1].set_xlabel("Total Votes")
axes[1].set_ylabel("Cuisine")

plt.tight_layout()
plt.show()
