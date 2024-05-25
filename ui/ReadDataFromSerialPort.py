import serial
import time

def read_data_from_serial_port(port='/dev/serial0', baud_rate=9600):
    # Setup the serial connection, baid rate is signals/second
    ser = serial.Serial(port, baud_rate, timeout=1)

    # Main loop to read data continuously
    while True:
        if ser.in_waiting > 0:  # Check if there's data waiting in the buffer
            data = ser.read(ser.in_waiting)  # Read all available data
            return data
        else:
            # No data available, wait a little before checking again
            time.sleep(0.1)

    ser.close()  # Ensure the serial port is closed when done

# Example of how you might use the function in a real scenario
data = read_data_from_serial_port()
