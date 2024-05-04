import serial
import hashlib
from cryptography.fernet import Fernet
import json
import os

# Define required paths
jsonFilePath = "Main/sensors.json"
current_data_file = "Main/CSV/data_csv.csv"

def read_data_from_serial_port():
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        return ser.read()

def split_data(packet):
    identifier = packet[0:3]
    encrypted_payload = packet[3:240]
    checksum = packet[240:256]
    return identifier, encrypted_payload, checksum

def verify_checksum(encrypted_payload, checksum):
    calculated_checksum = hashlib.md5(encrypted_payload).hexdigest()
    return calculated_checksum == checksum

def decrypt_payload(encrypted_payload):
    # Load the Fernet key from a secure storage inside the function
    with open("fernet_key_path", "rb") as key_file:
        fernet_key = key_file.read()
    fernet = Fernet(fernet_key)
    decrypted_payload = fernet.decrypt(encrypted_payload)
    return decrypted_payload

def decode_payload_to_json(decrypted_payload):
    # Assume decrypted_payload is a JSON formatted string
    json_object = json.loads(decrypted_payload)
    return json_object

def confirm_identifier(identifier):
    return identifier == b'ELEC'

def save_json_to_file(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file)

# Main process
while True:
    packet = read_data_from_serial_port()

    # Ensure packet length is correct before processing
    if len(packet) == 256:
        identifier, encrypted_payload, checksum = split_data(packet)
        
        if verify_checksum(encrypted_payload, checksum) and confirm_identifier(identifier):
            decrypted_payload = decrypt_payload(encrypted_payload)
            json_data = decode_payload_to_json(decrypted_payload)
            save_json_to_file(jsonFilePath, json_data)
            # JSON data is saved, now proceed with CSV handling