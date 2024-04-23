def read_sensor(self, sensor_type, redundancy = False):
  
  if (sensor_type == "imu"):
    # attempt to read primary sensor first
    if (self.sensors.speed.read()):
    	self.data["speed"]["raw"] = self.sensors.speed.read()
        self.data["speed"]["sensor"] = "primary"
    elif (redundancy and self.sensors.speed_r.read()):
     	# read redundancy controller if available
      	self.data["speed"]["raw"] = self.sensors.speed_r.read()
        self.data["speed"]["sensor"] = "secondary"
    else:
      	self.data["speed"] = "NA" # not available otherwise
   
  # continue for every other sensor
      
        
