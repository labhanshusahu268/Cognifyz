# Data Exploration and Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
ds = pd.read_csv("Dataset .csv")  

# Display the total number of rows and columns from the ds
print("No. of (Rows x Columns) =>",ds.shape)

# Get basic information about the ds using info function
print("\n BasicInfo of ds : \n",ds.info())

# Show first 5 rows
print("\n First 5 rows of ds :")
print(ds.head(5))

# Checking for missing values in each column in ds
print("\n Total Missing values in each column in ds : \n",ds.isnull().sum())

# Handling The missing values in ds
ds['Cuisines'] = ds['Cuisines'].fillna('Not Specified')
print("\n After handling the  missing values in ds , new shape is :", ds.shape)

# Converting The datatype of 'Aggregate rating' column to int
ds["Aggregate rating"] = ds["Aggregate rating"].astype(int)
print("\n Datatype of 'Aggregate rating' is :", ds["Aggregate rating"].dtype)

# Statistical summary of ds
print("\n Statistical summary of ds :")
print(ds.describe())

# Distribution plot of 'Aggregate rating'
print("\nPlotting KDE of Aggregate Rating...")
sns.kdeplot(ds["Aggregate rating"], shade=True, color='purple')
plt.title("KDE of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Density")
plt.grid(True)
plt.tight_layout()
plt.show()


# Check for class imbalance
print("\nClass distribution (in %) in 'Aggregate rating':")
print(ds["Aggregate rating"].value_counts(normalize=True) * 100)

# pie chart for class imbalance
ds["Aggregate rating"].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, shadow=False)
plt.title("Aggregate Rating class Distribution")
plt.ylabel('')
plt.show()


