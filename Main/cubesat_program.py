# cubeSat on-board software system
# @ sep kimiaei 2024
from cryptography.fernet import Fernet
# from machine import Pin, ADC
import datetime
import json
import hashlib
import time
from art import *
from sys import getsizeof

'''
    @author Sep Kimiaei 2024 - ELEC5551 cubeSat design.

    - object orientated approach to develop a cubeSat class with the following functions
    - initiliasation: sets the log file output, transmission frequency and encryption key
    - read_input: 
        @sensor_type:
            "weather" (5 temperature sensors, 1 humidity sensor)
            "imu" (altitude, speed, yaw, bearing)
            "gps" (gps_lat, gps_long, gps_time)
            "diagnostics" (battery)
    - store_data():
        save temporary data array to disk (depending on what file path was given)
    - scale_inputs
        scale all inputs as per their relevant scaling factor.
    - capture_img
        capture frame and store image blob/buffer to temporary data.
    - perform_parity_check
        perform checksum
    - encrypt_data
        use symmetric encryption to store to the image.
    - poll_gps
        store gps_lat, long and time to temporary data.
    - transmit_location
        send location beacon message.
    - transmit_data
        send all encrypted data.

'''

simulation = True

class cubeSat():

    def __init__(self, log_file, transmission_freq, public_key):

        # set up our cubesat log file with append privileges
        self.log_file = open(log_file, "a")

        # set up symmetrical encryption key- check with aidan to see if it can fit in lora packet.
        self.f = Fernet(str.encode(str(public_key)))
        
        # set up transmission frequency (need to check with aidan later)
        self.transmission_freq = None

        # set up data dictionary
        sensor_file = open('sensors/sensors.json')
        self.temporary_data = json.load(sensor_file)

        self.encrypted_data = b''

        if not simulation:
            self.temp1        = ADC(PIN())
            self.temp2        = ADC(PIN())
            self.temp3        = ADC(PIN())
            self.temp4        = ADC(PIN())
            self.temp5        = ADC(PIN())
            self.pressure_1   = ACD(PIN())
            self.pressure_2   = ACD(PIN())
            self.humidity     = ACD(PIN())

            self.altitude     = ADC(PIN())
            self.yaw          = ADC(PIN())
            self.bearing      = ADC(PIN())

            self.acceleration = ADC(PIN())
            self.speed        = ADC(PIN())
            
            self.battery      = ADC(PIN())

            self.gps_lat      = ADC(PIN())
            self.gps_long     = ADC(PIN())
            self.gps_time     = ADC(PIN())

        print()
        loading_screen =text2art("elec5551  cubeSat  mcu") # return art as str in normal mode
        print(loading_screen)
        print("*"*130)

        print("[-] monitoring: enabled")
        print("[-] transmitting once every:", transmission_freq, "minutes")
        print("[-] logging data to:", log_file)
        print("[-] loaded in", len(self.temporary_data), "sensor inputs")
        print("[-] current memory usage:", getsizeof(self.temporary_data))
        print(self.temporary_data.keys())
        print("*"*130)
        print()


    
    def read_inputs(self,sensor_type):

        print("reading sensor:", sensor_type)
        print()
        
        if not simulation:
            if (sensor_type == "weather"):
                # temperature first
                self.temporary_data["temp1"]          = self.s_temp_1.read()
                self.temporary_data["temp2"]          = self.s_temp_2.read()
                self.temporary_data["temp3"]          = self.s_temp_3.read()
                self.temporary_data["temp4"]          = self.s_temp_4.read()
                self.temporary_data["temp5"]          = self.s_temp_5.read()

                # humidity
                self.temporary_data["humidity"]       = self.humidity.read()

                # pressure
                self.temporary_data["pressure_1"]     = self.pressure_1.read()
                self.temporary_data["pressure_2"]     = self.pressure_2.read()

            elif (sensor_type == "imu"):
                self.temporary_data["speed"]          = self.speed.read()
                self.temporary_data["acceleration"]   = self.acceleration.read()
                self.temporary_data["altitude"]       = self.altitude.read()
                self.temporary_data["bearing"]        = self.bearing.read()

            elif (sensor_type == "gps"):
                self.temporary_data["gps_lat"]        = self.gps_lat.read()
                self.temporary_data["gps_long"]       = self.gps_long.read()
                self.temporary_data["gps_time"]       = self.gps_time.read()

            elif (sensor_type == "diagnostics"):
                self.temporary_data["battery"]        = self.battery.read()

            else:
                return

    def wait(self, period):
        time.sleep(period)
    
    def store_data(self):
        '''
            store data to disk. 
            seems to be supported by stmCube development environment.
            TO-DO: discuss whether log file needs to be encrypted or not.
        '''
        print("stored to file:", self.log_file)
        temporary_log_file_str = json.dumps(self.temporary_data, sort_keys=True)

        # format would be string iso time + dictionary array
        self.log_file.write(f"{str(datetime.datetime.now())} - {temporary_log_file_str}")
        print("[-] current memory usage:", getsizeof(self.temporary_data))
        print()

    def scale_inputs(self):
        
        # iterate through all cubeSat sensor datas and scale accordingly.
        for item, values in self.temporary_data.items():
            if item != "checksum":
                print("scaled: ", item)
                self.temporary_data[item]["scaled"] = float(self.temporary_data[item]["raw"]) * float(self.temporary_data[item]["scaling_factor"])
        print()


    def capture_img(self):
        # interface to camera
        print("snap! image taken")
        print()
        pass
    
    def perform_parity_check(self):
        print("checksum performed")
        sensor_to_string = json.dumps(self.temporary_data, sort_keys=True)
        hash_object = hashlib.sha256()
        hash_object.update(sensor_to_string.encode())
        self.temporary_data["checksum"] = hash_object.hexdigest()
        print()


    def encrypt_data(self):
        print("data encrypted")
        # convert to bytes
        byte_repr = str.encode(str(self.temporary_data))
        self.encrypted_data = self.f.encrypt(byte_repr)
        print()
        print(self.encrypted_data)
        print()



    def poll_gps(self):
        print("gps polled")
        print()

        pass

    def transmit_location(self):
        # transmit location data
        print("location transmitted")
        print()

        pass

    def transmit_data(self):
        # transmit encrypted data
        print("data transmitted")
        print()

        pass

    



