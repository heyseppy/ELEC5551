import subprocess

def stop():
    # Step 1: Define File Paths and Names
    csv_append = "C:\\Users\\Telementary\\Documents\\Main\\CSV\\CSVappend.py"
    new_flight = "C:\\Users\\Telementary\\Documents\\Main\\CSV\\NewFlight_csv.py"
    gps_plot = "C:\\Users\\Telementary\\Documents\\Main\\GPS_Map\\GPS_plot.py"
    map_refresh = "C:\\Users\\Telementary\\Documents\\Main\\Map_Refresh.py"
    main_data_processing = "C:\\Users\\Telementary\\Documents\\Main\\MainDataProcessing.py"

    # Step 2: Stop Necessary Scripts
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "imagename eq CSVappend.py"])
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "imagename eq GPS_plot.py"])
    subprocess.run(["taskkill", "/f", "/im", "python.exe", "/fi", "imagename eq MainDataProcessing.py"])

    # Start Necessary Scripts
    subprocess.Popen(["python", new_flight])
    subprocess.Popen(["python", map_refresh])

# Call the stop function
stop()
