import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = 'path/to/your/file.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Check the structure of your CSV file using df.head() to understand the columns and data
print(df.head())

# Assuming your CSV file has 'Date' and 'Sales' columns
date_column = 'Date'
sales_column = 'Sales'

# Convert 'Date' column to datetime type
df[date_column] = pd.to_datetime(df[date_column])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df[date_column], df[sales_column], marker='o', linestyle='-', color='b', label='Sales')
plt.title('Product Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
