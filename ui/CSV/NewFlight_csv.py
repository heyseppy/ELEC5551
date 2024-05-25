import shutil
from datetime import datetime

def NewFlight_csv():
    # Step 1: Define File Paths and Names
    current_data_file = "Main/CSV/data_csv.csv"
    current_flights_folder = "Main/CSV/"
    previous_flights_folder = "Main/CSV/Previous_Flights/"
    template_file = "Main/CSV/Template/template_csv.csv"
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Step 2: Move and Rename Current Data File
    new_data_file_name = date_time + "_data_csv.csv"
    shutil.move(current_data_file, previous_flights_folder + new_data_file_name)

    # Step 3: Copy Template File and Rename
    shutil.copy(template_file, current_flights_folder + "data_csv.csv")

# Example usage
NewFlight_csv()
