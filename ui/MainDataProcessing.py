import serial
import hashlib
from cryptography.fernet import Fernet
import json
import os
from PIL import Image
import io

# Define required paths
jsonFilePath = "Main/sensors.json"
current_data_file = "Main/CSV/data_csv.csv"
imageFilePath = "Main/Images/sensor_image.png"

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
    with open("fernet_key_path", "rb") as key_file:
        fernet_key = key_file.read()
    fernet = Fernet(fernet_key)
    decrypted_payload = fernet.decrypt(encrypted_payload)
    return decrypted_payload

def decode_payload_to_json_and_image(decrypted_payload):
    # Assuming payload contains JSON data followed by binary image data
    separator_index = decrypted_payload.find(b'\\end')  # Custom separator between JSON and image data
    json_data = json.loads(decrypted_payload[:separator_index])
    image_data = decrypted_payload[separator_index + 4:]  # Skip the separator
    return json_data, image_data

def save_json_to_file(filename, json_data):
    with open(filename, 'w') as file:
        json.dump(json_data, file)


def save_image_to_file(image_data):
    existing_image_path = "Main/Onboard Pictures/OnBoardPicture_Latest.png"
    past_pictures_folder = "Main/Onboard Pictures/Past Pictures"

    # Timestamp to rename old image
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_image_name = f"OnBoardPicture_{timestamp}.png"
    new_image_path = os.path.join(past_pictures_folder, new_image_name)
    
    # Move old image to Past Pictures Folder
    if os.path.exists(existing_image_path):
        shutil.move(existing_image_path, new_image_path)
    
    # Save new image to existing image path
    image = Image.open(io.BytesIO(image_data))
    image.save(existing_image_path)

def confirm_identifier(identifier):
    return identifier == b'ELEC'

# Main process
while True:
    packet = read_data_from_serial_port()
    if len(packet) == 256:
        identifier, encrypted_payload, checksum = split_data(packet)
        
        if verify_checksum(encrypted_payload, checksum) and confirm_identifier(identifier):
            decrypted_payload = decrypt_payload(encrypted_payload)
            json_data, image_data = decode_payload_to_json_and_image(decrypted_payload)
            save_json_to_file(jsonFilePath, json_data)
            save_image_to_file(imageFilePath, image_data)
