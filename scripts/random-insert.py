import os
import pandas as pd
import random

# Step 1: Read "goodware.csv" and get the number of rows
goodware_path = "goodware.csv"
goodware_df = pd.read_csv(goodware_path)
goodware_rows = len(goodware_df)
print(f"Initial number of rows in goodware.csv: {goodware_rows}")

# Check if "target-class-name" column exists; if not, add it with all values as "goodware"
if "target-class-name" not in goodware_df.columns:
    goodware_df["target-class-name"] = "goodware"

# Step 2: Find all other CSV files in the same directory
directory = os.getcwd()
csv_files = [f for f in os.listdir(directory) if f.endswith(".csv") and f != "goodware.csv"]

# Process each CSV file
for file_name in csv_files:
    file_path = os.path.join(directory, file_name)
    print(f"Processing {file_name}...")

    # Read the content of the CSV file, excluding the header
    other_df = pd.read_csv(file_path, header=0)  # `header=0` ensures only data rows are read, excluding column names
    num_rows_other = len(other_df)
    print(f"Number of rows in {file_name}: {num_rows_other}")

    # Add "target-class-name" and "target-class" columns to the data from other files
    target_class_name = file_name.rsplit(".", 1)[0]
    other_df["target-class-name"] = target_class_name
    other_df["target-class"] = 1

    # Find all indices where "target-class-name" is "goodware"
    goodware_indices = goodware_df[goodware_df["target-class-name"] == "goodware"].index.tolist()
    
    if not goodware_indices:
        print("No insertion points available in 'goodware.csv' where 'target-class-name' is 'goodware'.")
        continue

    # Select a random insertion index from these indices
    insert_index = random.choice(goodware_indices)
    print(f"Inserting rows from {file_name} at index {insert_index} in goodware.csv (only at 'goodware' locations)")

    # Split goodware_df at the insertion index
    top_part = goodware_df.iloc[:insert_index]
    bottom_part = goodware_df.iloc[insert_index:]

    # Concatenate the parts with other_df in the middle
    goodware_df = pd.concat([top_part, other_df, bottom_part], ignore_index=True)

    # Update the row count of goodware_df
    goodware_rows = len(goodware_df)
    print(f"Updated number of rows in goodware.csv: {goodware_rows}")

# Step 3: Save the modified goodware.csv
goodware_df.to_csv(goodware_path, index=False)
print(f"Final goodware.csv saved with {goodware_rows} rows.")
