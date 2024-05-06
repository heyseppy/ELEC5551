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
from machine import I2C, Pin, serial

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

# version 1.0.1
class cubeSat():

    def __init__(self, log_file, transmission_freq, public_key):
        
        # load configuration file for the cubesat
        sensor_file = open('sensors/sensors.json')
        self.temporary_data = json.load(sensor_file)

        # set output disk file for cubesat onboard memory
        self.log_file = open(log_file, "a")

        # set cubesat energisation time (time of flight)
        self.start_time = time.time()

        # configure encryption protocol (Fernet symmetric key)
        self.f = Fernet(str.encode(str(public_key)))
        self.encrypted_data = b''
        
        # set up transmission frequency ticks
        self.transmission_freq = None

        # set up i2c bus. serial lines will be configured as each sensor is called.
        self.cubesat_i2c = I2C(0, sda = sda, scl = scl, freq = 4000000)

        self.print_debug()

    def print_debug(self):

        print()
        loading_screen =text2art("cubeSat  mcu") # return art as str in normal mode
        print(loading_screen)
        print("*"*130)

        print("[-] monitoring: enabled")
        print("[-] transmitting once every:", self.transmission_freq, "seconds")
        print("[-] logging data to:", self.log_file)
        print("[-] loaded in", len(self.temporary_data), "sensor inputs")
        print("[-] current memory usage:", getsizeof(self.temporary_data))
        print("\nconnections: ")
        print("temp1,temp2,temp3,temp4,temp5,speed,altitude,yaw,bearing,humidity,acceleration")
        print("gps_lat,gps_long,gps_time,battery,pressure_1,pressure_2")
        print("camera, xbee")
        print("*"*130)
        print()


    def read_input_sensor(self, data_key):
        '''
            returns the value at the stored address after addressing whether or not it is serial 
            or i2c.
        '''

        if self.temporary_data[data_key]["type"] == "i2c":
            _out = self.cubesat_i2c.readfrom(self.temporary_data[data_key]["address"], 1)
        elif self.temporary_data[data_key]["type"] == "serial":
            self.cubesat_serial = Serial(self.temporary_data["address"])
            _out = self.cubesat_serial_port.read(self.temporary_data[data_key]["address"])

        # return the output data (analog)
        return _out
    

    def read_inputs(self,sensor_type):

        print("reading sensor:", sensor_type)
        print()
        
        if not simulation:
            if (sensor_type == "weather"):
                
                
                self.temporary_data["temp1"]          = self.read_input_sensor("temp1")
                self.temporary_data["temp2"]          = self.read_input_sensor("temp2")
                self.temporary_data["temp3"]          = self.read_input_sensor("temp3")
                self.temporary_data["temp4"]          = self.read_input_sensor("temp4")
                self.temporary_data["temp5"]          = self.read_input_sensor("temp5")

                # humidity
                self.temporary_data["humidity"]       = self.read_input_sensor("humidity")

                # pressure
                self.temporary_data["pressure_1"]     = self.read_input_sensor("pressure_1")
                self.temporary_data["pressure_2"]     = self.read_input_sensor("pressure_2")

            elif (sensor_type == "imu"):
                self.temporary_data["speed"]          = self.read_input_sensor("speed")
                self.temporary_data["acceleration"]   = self.read_input_sensor("acceleration")
                self.temporary_data["altitude"]       = self.read_input_sensor("altitude")
                self.temporary_data["bearing"]        = self.read_input_sensor("bearing")

            elif (sensor_type == "gps"):
                self.temporary_data["gps_lat"]        = self.read_input_sensor("gps_lat")
                self.temporary_data["gps_long"]       = self.read_input_sensor("gps_long")
                self.temporary_data["gps_time"]       = self.read_input_sensor("gps_time")

            elif (sensor_type == "diagnostics"):
                self.temporary_data["battery"]        = self.read_input_sensor("battery")

            # otherwise return None
            else:
                print("no sensor was selected")
                return

    def wait(self, period):
        time.sleep(period)
    
    def store_data(self):
        '''
            stores data to disk.
            after discussion with client, the on-metal data will not need to be encrypted.
        '''
        print("stored to file:", self.log_file)
        temporary_log_file_str = json.dumps(self.temporary_data, sort_keys=True)

        # format would be string iso time + dictionary array
        self.log_file.write(f"{str(datetime.datetime.now())} - {temporary_log_file_str}")
        print("[-] current memory usage:", getsizeof(self.temporary_data))
        print()

    def scale_inputs(self):
        '''
            iterates through all sensors and scales their values accordingly.
            uses linear scaling methodology to perform this scaling.
        '''
        for item, values in self.temporary_data.items():
            if item != "checksum":
                print("scaled: ", item)
                self.temporary_data[item]["scaled"] = float(self.temporary_data[item]["raw"]) * float(self.temporary_data[item]["scaling_factor"])
        print()


    def capture_img(self):
        # transmission and receival to/from camera
        # upon request send camera pulse via the txline
        # e.g. transmitSesnorpulse()
        # e.g. recordCameradata to temporary data buffer.
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

    def split_packets(self, packet_size):
        # split data into chunks that will fit accordingly.
        packets = []

        for i in range(len(self.temporary_data) / packet_size):
            packets.append(self.temporary_data[i*packet_size: i*packet_size + packet_size])
        
        return packets



    def transmit_data(self):
        # transmission pulse to xBee transceiver.
        # pseudocode provied externally for xbee communication
        pass

    



