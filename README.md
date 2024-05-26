<p align="center">
  <img src="https://example.com/path_to_satellite_image.jpg" alt="Satellite Image">
  <h1>ELEC5551 Electrical Design Project</h1>
</p>

## Overview
This repository houses all components of the ELEC5551 Electrical Design project conducted at [Your University Name]. The project includes comprehensive designs and software implementations for a sophisticated electrical system, focusing on both onboard and base station functionalities.

## Repository Overview
### Base Station Software
| File Path                         | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `ui/CSV/CSVAppend.py`             | Logs GPS data into a CSV, ensuring all entries are unique.                                        |
| `ui/CSV/NewFlight_csv.py`         | Prepares for new data collection by replacing the old CSV with a new template, storing past files.|
| `ui/GPS_Map/GPSPlot.py`           | Plots GPS coordinates on a map and visualizes flight paths with altitude indicated by color.      |
| `ui/GPS_Map/Map_Refresh.py`       | Prepares for new GPS plot image, provides template PNG of the map and stores old map.             |
| `ui/MainDataProcessing.py`        | Processes data received via serial interface to prepare for display and logging for UI.           |
| `ui/ReadDataFromSerialPort.py`    | Initiates data reception from the serial interface.                                               |
| `ui/Start.py`                     | Initiates CSV appending process for data logging and process for GPS plotting.                    |
| `ui/Stop.py`                      | Terminates data logging and GPS plotting processes; starts scripts for new templates.             |
| `ui/UI/index.html`                | HTML file that structures the user interface layout.                                              |
| `ui/UI/script.js`                 | JavaScript file that adds interactivity to the user interface.                                    |
| `ui/UI/styles.css`                | CSS file that styles the user interface elements.                                                 |

### Base Station Hardware
| File Path                         | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `Base Station Hardware / Base_Station_Combined v34`             | Contains entire Autodesk Fusion 360 workspace, including simulation models used for thermal and load analysis. 


### Onboard Software
| File Path                         | Description                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------|
| `Base Station Hardware / Base_Station_Combined v34`             | Contains entire Autodesk Fusion 360 workspace, including simulation models used for thermal and load analysis. 

       


### Onboard Software

## PCB Design
The `PCB` directory contains all necessary files for the Printed Circuit Board (PCB) design. Schematic files, Gerber files, and comprehensive documentation about layout and components are designed using Altium. This design ensures efficiency and reliability, maintaining stable performance under diverse operational conditions.

## Onboard Software
The `OnboardSoftware` folder includes all source code for the microcontrollers on the PCB, written in MicroPython. This software manages sensor inputs, communication protocols, and ensures real-time data processing and decision-making, crucial for the system's autonomous functions.

## Base Station Software
In the `BaseStationSoftware` directory, you'll find the software required to interface with the project's base station. This software is crafted using HTML, CSS, and JavaScript, focusing on data acquisition, user interface, and system monitoring. This stack ensures a robust, user-friendly interface for real-time monitoring and control.

## Base Station Hardware
The `BaseStationHardware` folder encompasses detailed designs and specifications for the hardware setup at the base station, crafted in Autodesk Fusion360. This section provides detailed schematics, a list of components, and assembly instructions, facilitating the building and maintenance of the hardware that supports communication with the onboard systems.


## License
The CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P) was chosen for its commitment to transparency and collaboration, allowing unrestricted use, modification, and distribution of the hardware designs and documentation. This license facilitates innovation and sharing within the community, ensuring that all adaptations and improvements remain openly accessible under the same terms.

## Acknowledgements
- Special thanks to the ELEC5551 course staff and fellow students for their invaluable feedback and support.

## Contributors
- Aidan Crummey
- Jonathon Sader
- William Hor
- Sep Kimiaei
- Carl Alvares
- Liam Kubach



