import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# List to hold dataframes
dataframes = []

# Loop through all CSV files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".csv"):
        # Read the CSV file
        df = pd.read_csv(filename)
        
        # Add a column with the filename
        df['SourceFile'] = filename
        
        # Append the dataframe to the list
        dataframes.append(df)

# Combine all dataframes into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('combined.csv', index=False)

print("All CSV files have been successfully combined into combined.csv with 'SourceFile' column.")