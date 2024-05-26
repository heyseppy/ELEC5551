import math
from cubesat_program import *
import random
import matplotlib.pyplot as plt
'''
    test code for initialising a cubeSat class
    @ sep kimiaei
    b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
'''
import os

average_times_per_run = []
file_sizes_per_sample = []

for trials in range(1):

    elec5551_cubesat = cubeSat("test.json", 5, "nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=")

    for i in range(100000):
        # read sensors


        sensor_file = open('../sensors/sensors.json')
        temporary_data = json.load(sensor_file)
        import json
        with open('../sensors/sensors.json', 'w') as f:
            json.dump(temporary_data, f)

        temporary_data["temp1"]["raw"] = random.randint(0,4096)
        temporary_data["temp2"]["raw"] = random.randint(0,4096)
        temporary_data["temp3"]["raw"] = random.randint(0,4096)
        temporary_data["temp4"]["raw"] = random.randint(0,4096)


        elec5551_cubesat.read_inputs("weather")
        elec5551_cubesat.read_inputs("humidity")
        elec5551_cubesat.read_inputs("imu")
        elec5551_cubesat.read_inputs("gps")
        elec5551_cubesat.read_inputs("diagnostics")

        # scale  values
        elec5551_cubesat.scale_inputs()

        # image and gps
        elec5551_cubesat.capture_img()
        elec5551_cubesat.poll_gps()
        
        # store to disk
        elec5551_cubesat.store_data()

        # perform parity checks and encryption
        elec5551_cubesat.perform_parity_check()
        elec5551_cubesat.encrypt_data()

        # perform transmission
        elec5551_cubesat.transmit_data()
        file_sizes_per_sample.append(os.stat('test.json').st_size)
    

    average_times_per_run.append(time.time() - elec5551_cubesat.start_time)
    del elec5551_cubesat

print(file_sizes_per_sample)
print(average_times_per_run)

plt.figure(figsize=(10, 10))
plt.plot(file_sizes_per_sample, marker='o', linestyle='-', color='black', linewidth=0.05)

plt.title('File Size of Log.json After Iterations')
plt.xlabel('Iterations')
plt.ylabel('File Size (bytes)')
plt.grid(False)
plt.tight_layout()
plt.show()