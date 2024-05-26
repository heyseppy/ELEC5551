import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from PIL import Image

# Define paths
currentMapPath = 'Main/GPS_Map/current_map.png'
templateMapPath = 'Main/GPS_Map/Map Template/template_map.png'
dataCSV = 'Main/CSV/data_csv.csv'

# Define geographical bounds
minLat, maxLat, minLong, maxLong = -33.1533, -32.939609, 116.5309, 116.949071

# Load template map
templateMap = Image.open(templateMapPath)

# Setup plot window
plt.imshow(templateMap)
plt.axis('scaled')
plt.axis('off')

# Define color map
colorMap = plt.get_cmap('plasma')

def convertGPSToPoint(latitude, longitude):
    x = (longitude - minLong) / (maxLong - minLong) * templateMap.width
    y = templateMap.height - ((latitude - minLat) / (maxLat - minLat) * templateMap.height)
    return (x, y)

while True:
    # Load and process data
    data = pd.read_csv(dataCSV)
    data = data.sort_values(by='gps_time')

    # Clear previous plot
    plt.clf()
    plt.imshow(templateMap)
    plt.axis('scaled')
    plt.axis('off')

    # Track previous GPS point
    lastGPSPoint = None

    # Plot data
    for index, row in data.iterrows():
        # Convert GPS coordinates to plot coordinates
        currentGPSPoint = convertGPSToPoint(row['gps_lat'], row['gps_long'])

        # Normalize altitude for color mapping
        altitude = row['altitude']
        normalizedAltitude = (altitude - 10) / (5000 - 10)
        color = colorMap(normalizedAltitude)

        if lastGPSPoint is not None:
            # Draw line
            plt.plot([lastGPSPoint[0], currentGPSPoint[0]], [lastGPSPoint[1], currentGPSPoint[1]], color=color)

        lastGPSPoint = currentGPSPoint

    # Refresh and save plot
    plt.axis('off')
    plt.savefig(currentMapPath, bbox_inches='tight', pad_inches=0)

    # Wait before the next update
    time.sleep(20)
