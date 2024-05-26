import json
import csv
import time

# Define File Paths and Names
jsonFilePath = "Main/sensors.json"
csvFilePath = "Main/CSV/data_csv.csv"

def CVSappend():
    # Step 1: Load Data from JSON File
    with open(jsonFilePath, "r") as json_file:
        json_data = json.load(json_file)

    # Step 2: Extract GPS Time from JSON Data
    current_gps_time = json_data["gps_time"]["raw"]

    # Step 3: Read Existing CSV Data
    with open(csvFilePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        all_rows = list(csv_reader)

    # Step 4: Get GPS Times from CSV Data
    gps_times = [row[0] for row in all_rows[1:]]  # Exclude header

    # Step 5: Check if current GPS time already exists
    if current_gps_time not in gps_times:
        # Step 6: Get Headers from CSV Data
        headers = all_rows[0]

        # Step 7: Prepare new row
        new_row = [current_gps_time]

        # Step 8: Iterate over keys in JSON data and append to new row
        for header in headers[1:]:  # Skip GPS time column
            value = json_data.get(header, {}).get("scaled", None)
            new_row.append(value)

        # Step 9: Append New Data Row to CSV
        with open(csvFilePath, "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_row)

# Continuous monitoring and appending data
while True:
    CVSappend()
    time.sleep(1)
