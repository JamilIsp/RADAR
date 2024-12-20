import pandas as pd

# Load the CSV file
file_path = "D:/Experiment/Drift-dataset-phase-1.csv"  # Replace with the actual CSV file path

df = pd.read_csv(file_path)

# Parse the "@timestamp" column with the specified format
df["@timestamp"] = pd.to_datetime(df["@timestamp"], format="%b %d, %Y @ %H:%M:%S.%f")

# Initialize the new timestamps with the first timestamp in the dataset
new_timestamps = [df["@timestamp"].iloc[0]]

# Iterate through the DataFrame from the second row onward
for i in range(1, len(df)):
    previous_timestamp = new_timestamps[i - 1]
    current_class = df["target-class"].iloc[i]
    previous_class = df["target-class"].iloc[i - 1]
    
    if current_class != previous_class:
        # If there is a change in "target-class", add 1 second to the previous timestamp
        new_timestamp = previous_timestamp + pd.Timedelta(seconds=1)
    else:
        # Otherwise, use the original time difference to calculate the new timestamp
        time_diff = df["@timestamp"].iloc[i] - df["@timestamp"].iloc[i - 1]
        new_timestamp = previous_timestamp + time_diff

    # Append the new timestamp to the list
    new_timestamps.append(new_timestamp)

# Update the "@timestamp" column with the new continuous timestamps
df["@timestamp"] = new_timestamps

# Format the "@timestamp" column to ensure the desired output format
df["@timestamp"] = df["@timestamp"].dt.strftime("%b %d, %Y @ %H:%M:%S.%f")

# Save the updated DataFrame to a new CSV file
output_path = "D:/Experiment/Drift-dataset-phase-1-timestamp-amended.csv"  # Change to your desired output file name
df.to_csv(output_path, index=False)

print(f"Synchronized dataset saved to {output_path}")

