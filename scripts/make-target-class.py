# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:15:06 2024

@author: Jamil
"""

import os
import pandas as pd

# Define the file to exclude
exclude_file = "goodware.csv"

# Get the current directory
directory = os.getcwd()

# List all CSV files in the directory except "goodware.csv"
csv_files = [f for f in os.listdir(directory) if f.endswith(".csv") and f != exclude_file]

# Process each CSV file
for file_name in csv_files:
    file_path = os.path.join(directory, file_name)
    print(f"Processing {file_name}...")

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Add the new columns
    df["target-class-name"] = file_name.rsplit(".", 1)[0]  # File name without the extension
    df["target-class"] = 1

    # Save the modified DataFrame back to the same file
    df.to_csv(file_path, index=False)
    print(f"Added 'target-class-name' and 'target-class' columns to {file_name} and saved.")
