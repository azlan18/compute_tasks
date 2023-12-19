import pandas as pd

# Load the employees data into a DataFrame
employees_df = pd.read_csv('employees.csv')  # Replace with the actual path to your employees file

# Display all location IDs from the locations file
location_ids = employees_df['Location'].unique()
print("All Location IDs:", location_ids)

# Extract the first 7 records from the employees file
first_7_records = employees_df.head(7)
print("\nFirst 7 Records from Employees:")
print(first_7_records)
