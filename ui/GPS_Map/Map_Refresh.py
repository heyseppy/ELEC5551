import os
from datetime import datetime
import shutil

def Map_Refresh():
    # Step 1: Define File Paths and Names
    currentMapPath = "Main\\GPS_Map\\current_map.png"
    previousMapsPath = "Main\\GPS_Map\\map\\Previous Maps\\"
    templateMapPath = "Main\\GPS_Map\\Map Template\\template_map.png"
    dateTime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Step 2: Rename and Move Current Map File
    archivedMapName = dateTime + "_map.png"
    if os.path.exists(currentMapPath):
        shutil.move(currentMapPath, previousMapsPath + archivedMapName)

    # Step 3: Copy Template Map and Rename
    if os.path.exists(templateMapPath):
        shutil.copy(templateMapPath, currentMapPath)

# Example usage
Map_Refresh()
