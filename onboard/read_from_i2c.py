from machine import I2C, Pin

sda = Pin(sda_pin_number)
scl = Pin(scl_pin_number)

i2c = I2C(0, sda=sda, scl=scl, freq=400000) 

data = i2c.readfrom(device_address, num_bytes)
