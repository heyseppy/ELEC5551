import subprocess

def start():
    # Step 1: Define File Paths and Names
    csv_append = "C:\\Users\\Telementary\\Documents\\Main\\CSV\\CSVappend.py"
    new_flight = "C:\\Users\\Telementary\\Documents\\Main\\CSV\\NewFlight_csv.py"
    gps_plot = "C:\\Users\\Telementary\\Documents\\Main\\GPS_Map\\GPS_plot.py"
    map_refresh = "C:\\Users\\Telementary\\Documents\\Main\\Map_Refresh.py"
    main_data_processing = "C:\\Users\\Telementary\\Documents\\Main\\MainDataProcessing.py"

    # Step 2: Start Necessary Scripts
    subprocess.Popen(["python", csv_append])
    subprocess.Popen(["python", gps_plot])
    subprocess.Popen(["python", main_data_processing])
    
    # Stop precautionary scripts
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "imagename eq NewFlight_csv.py"])
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "imagename eq Map_Refresh.py"])

# Call the start function
start()
