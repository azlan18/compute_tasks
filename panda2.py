import pandas as pd

# Load employees data into a DataFrame
employees_df = pd.read_csv('employees.csv')  # Replace with the actual path to your employees file

# Select distinct department IDs from the employees file
distinct_department_ids = employees_df['DEPARTMENT_ID'].unique()
print("Distinct Department IDs from Employees:", distinct_department_ids)

# Display all location IDs from the locations file
locations_df = pd.read_csv('locations.csv')  # Replace with the actual path to your locations file
all_location_ids = locations_df['LOCATION_ID'].unique()
print("\nAll Location IDs from Locations:", all_location_ids)
