import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean visual theme
sns.set_theme(style="whitegrid")

# Load the dataset
df = pd.read_csv("Dataset .csv")  

# Clean column names
df.columns = df.columns.str.strip()

# Convert necessary columns to correct types
df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors='coerce')
df["Price range"] = pd.to_numeric(df["Price range"], errors='coerce')

#  Table Booking Percentages
table_booking_counts = df['Has Table booking'].value_counts()
table_booking_percent = (table_booking_counts / len(df)) * 100

print("\n Percentage of Restaurants with and without Table Booking:")
print(table_booking_percent.round(2))

# Bar plot for Table Booking
plt.figure(figsize=(6, 4))
sns.barplot(x=table_booking_percent.index, y=table_booking_percent.values, palette="Set2")
plt.title("Table Booking Availability (%)")
plt.ylabel("Percentage")
plt.xlabel("Has Table Booking")
plt.tight_layout()
plt.show()

#  Online Delivery Percentages
online_delivery_counts = df['Has Online delivery'].value_counts()
online_delivery_percent = (online_delivery_counts / len(df)) * 100

print("\n Percentage of Restaurants with and without Online Delivery:")
print(online_delivery_percent.round(2))

# Bar plot for Online Delivery
plt.figure(figsize=(6, 4))
sns.barplot(x=online_delivery_percent.index, y=online_delivery_percent.values, palette="Set3")
plt.title("Online Delivery Availability (%)")
plt.ylabel("Percentage")
plt.xlabel("Has Online Delivery")
plt.tight_layout()
plt.show()

#  Average Rating vs Table Booking
avg_rating_booking = df.groupby("Has Table booking")["Aggregate rating"].mean()

print("\n Average Rating based on Table Booking Availability:")
print(avg_rating_booking.round(2))

# Plot average ratings
plt.figure(figsize=(6, 4))
sns.barplot(x=avg_rating_booking.index, y=avg_rating_booking.values, palette="pastel")
plt.title("Average Rating by Table Booking Availability")
plt.ylabel("Average Rating")
plt.xlabel("Has Table Booking")
plt.ylim(0, 5)
plt.tight_layout()
plt.show()

#  Online Delivery Availability by Price Range (%)
delivery_vs_price = df.groupby("Price range")["Is delivering now"].value_counts(normalize=True).unstack() * 100

print("\n Online Delivery Availability by Price Range (in %):")
print(delivery_vs_price.round(2))

# Plot stacked bar chart
delivery_vs_price.plot(kind='bar', stacked=True, colormap='coolwarm', figsize=(10, 6))
plt.title("Online Delivery Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Percentage")
plt.legend(title="Is Delivering Now", labels=["No", "Yes"])
plt.tight_layout()
plt.show()
