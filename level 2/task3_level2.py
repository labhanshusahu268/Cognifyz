# Feature Engineering
import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("Dataset .csv")  # Make sure the file name is correct (no extra spaces)

# Preview original column names
print("Original Columns:\n", data.columns.tolist())

# Handle missing values in critical columns before feature engineering
data['Restaurant Name'] = data['Restaurant Name'].fillna('Unknown')
data['Address'] = data['Address'].fillna('No Address Provided')

# Extract features: Length of Restaurant Name and Address
data['Name Length'] = data['Restaurant Name'].apply(lambda x: len(str(x)))
data['Address Length'] = data['Address'].apply(lambda x: len(str(x)))

# Display the new textual features
print("\nTextual Feature Preview:")
print(data[['Restaurant Name', 'Name Length', 'Address', 'Address Length']].head(10))

# Normalize categorical features to binary (0 or 1)
data['Has Table Booking'] = data['Has Table booking'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)
data['Has Online Delivery'] = data['Has Online delivery'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)


# Display new features
print("\nNew Feature Columns:")
pd.set_option('display.max_columns', None)
print(data[['Restaurant Name', 'Name Length', 'Address', 'Address Length', 
            'Has Table booking', 'Has Table Booking', 
            'Has Online delivery', 'Has Online Delivery']].head())