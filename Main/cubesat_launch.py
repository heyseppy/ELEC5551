
from cubesat_program import *
'''
    test code for initialising a cubeSat class
    @ sep kimiaei
    b'nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0='
'''

elec5551_cubesat = cubeSat("test.json", 5, "nNjpIl9Ax2LRtm-p6ryCRZ8lRsL0DtuY0f9JeAe2wG0=")

while True:
    # read sensors
    elec5551_cubesat.wait(3)
    elec5551_cubesat.read_inputs("weather")
    elec5551_cubesat.wait(1)
    elec5551_cubesat.read_inputs("humidity")
    elec5551_cubesat.wait(1)
    elec5551_cubesat.read_inputs("imu")
    elec5551_cubesat.wait(1)
    elec5551_cubesat.read_inputs("gps")
    elec5551_cubesat.wait(1)
    elec5551_cubesat.read_inputs("diagnostics")
    elec5551_cubesat.wait(1)

    # scale  values
    elec5551_cubesat.scale_inputs()
    elec5551_cubesat.wait(2)

    # image and gps
    elec5551_cubesat.capture_img()
    elec5551_cubesat.wait(2)
    elec5551_cubesat.poll_gps()
    elec5551_cubesat.wait(2)
    
    # store to disk
    elec5551_cubesat.store_data()
    elec5551_cubesat.wait(2)

    # perform parity checks and encryption
    elec5551_cubesat.perform_parity_check()
    elec5551_cubesat.encrypt_data()

    # perform transmission
    elec5551_cubesat.transmit_data()
    elec5551_cubesat.transmit_location()