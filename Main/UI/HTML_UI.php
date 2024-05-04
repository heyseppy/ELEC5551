<!-- START OF BODY -->
<div class="container">
  <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px;">
    <!-- Spacer div to push content to the right -->
    <div style="flex-grow: 1;"></div> 
    <div style="flex-grow: 2.5; text-align: center;">
      <h1 style="margin: 0;">Telemetry Data Dashboard</h1>
    </div>
    <div>
      <div id="date-display" style="display: block; text-aling right;"></div>
      <div id="time-display" style="display: block; text-aling right;"></div>
    </div>
  </div>
  
   <button id="toggleButton" class="start-button">Start</button>
  
  <h2>Location Data</h2>
    <!-- LOCATION BLOCKS -->
       <div class="maps-row">
      <!-- GPS -->
      <div class="sensorlayout">
  <svg class="icon" viewBox="0 0 300 300">
    <use href="#map-icon"></use>
  </svg>
  <p>GPS</p>
  <div id="popupGPS" class="popup" style="display: none;">
    <img src="https://i.stack.imgur.com/pZ7Xg.jpg" alt="logo" style="width: 100%; height: auto;">
    <button onclick="document.getElementById('popupGPS').style.display='none'">Close</button>
  </div>
</div>

  
  <!-- Radio Triangulation -->
      <div class="sensorlayout">
        <svg class="iconRF" viewBox="0 0 300 300">
          <use href="#radio-triangulation-icon"></use>
        </svg>
        <p>Radio Triangulation</strong></p>
      </div>
    </div>

  
  

  <h2>Environmental Sensors</h2>
  
  <!-- TEMP BLOCKS -->
  <div class="tempsensor-wrapper">
    <!-- Temp 1 -->
    <div class="tempsensor">
      <svg class="icon" viewBox="0 0 300 300">
        <use href="#temperature-icon"></use>
      </svg>
      <p>Temp Sensor 1: <strong>22 °c</strong></p>
      <div id="popup1" class="popup" style="display: none;">
        <p>Temp Sensor 1</p>
        <p>Current Temperature: <strong> 22 °c</strong></p>
        <svg id="trendGraph1" width="280" height="150" style="border: 1px solid #ccc;"></svg>
        <button onclick="document.getElementById('popup1').style.display='none'">Close</button>
      </div>
    </div>

    <!-- Temp 2 -->
    <div class="tempsensor">
      <svg class="icon" viewBox="0 0 300 300">
        <use href="#temperature-icon"></use>
      </svg>
      <p>Temp Sensor 2: <strong>24 °c</strong></p>
      <div id="popup2" class="popup" style="display: none;">
        <p>Temp Sensor 2</p>
        <p>Current Temperature: <strong> 24 °c</strong></p>
        <svg id="trendGraph2" width="280" height="150" style="border: 1px solid #ccc;"></svg>
        <button onclick="document.getElementById('popup2').style.display='none'">Close</button>
      </div>
    </div>

    <!-- Temp 3 -->
    <div class="tempsensor">
      <svg class="icon" viewBox="0 0 300 300">
        <use href="#temperature-icon"></use>
      </svg>
      <p>Temp Sensor 3: <strong><span id="temp3-latest">--</span> °c</strong></p>
    </div>

    <!-- Temp 4 -->
    <div class="tempsensor">
      <svg class="icon" viewBox="0 0 300 300">
        <use href="#temperature-icon"></use>
      </svg>
      <p>Temp Sensor 4: <strong><span id="temp4-latest">--</span> °c</strong></p>
    </div>

    <!-- Temp 5 -->
    <div class="tempsensor">
      <svg class="icon" viewBox="0 0 300 300">
        <use href="#temperature-icon"></use>
      </svg>
      <p>Temp Sensor 5: <strong><span id="temp5-latest">--</span> °c</strong></p>
    </div>
  </div>

  <!-- HUMIDITY BLOCKS -->
       <div class="humidity-sensor-row">
      <!-- Temp 7 -->
      <div class="sensorlayout">
        <svg class="icon" viewBox="0 0 300 300">
          <use href="#humidity-icon"></use>
        </svg>
        <p>Humidity Sensor: <strong><span id="humidity-latest">--</span> °c</strong></p>
      </div>
    </div>
  
  
  <!-- PRESSURE BLOCKS -->
       <div class="pressure-sensor-row">
      <!-- Pressure 1 -->
      <div class="sensorlayout">
        <svg class="icon" viewBox="0 0 300 300">
          <use href="#pressure-icon"></use>
        </svg>
        <p>Pressure Sensor: <strong><span id="humidity-latest">--</span> °c</strong></p>
      </div>
  
  <!-- Pressure 2 -->
      <div class="sensorlayout">
        <svg class="icon" viewBox="0 0 300 300">
          <use href="#pressure-icon"></use>
        </svg>
        <p>Pressure Sensor: <strong><span id="humidity-latest">--</span> °c</strong></p>
      </div>
    </div>


 

  
  </div>
<!--END OF BODY -->



  <!-- Placeholder for the Temperature Trend Graph -->
  <div>
    <canvas id="tempTrendGraph"></canvas>
  </div>
</div>




<!------------- ICONS ------------->
<!--Temp Sensor Icon -->
<svg style="display: none;">
  <symbol id="temperature-icon" viewBox="0 0 512 512" width="100" title="temperature-low">
    <path d="M416 0c-52.9 0-96 43.1-96 96s43.1 96 96 96 96-43.1 96-96-43.1-96-96-96zm0 128c-17.7 0-32-14.3-32-32s14.3-32 32-32 32 14.3 32 32-14.3 32-32 32zm-160-16C256 50.1 205.9 0 144 0S32 50.1 32 112v166.5C12.3 303.2 0 334 0 368c0 79.5 64.5 144 144 144s144-64.5 144-144c0-34-12.3-64.9-32-89.5V112zM144 448c-44.1 0-80-35.9-80-80 0-25.5 12.2-48.9 32-63.8V112c0-26.5 21.5-48 48-48s48 21.5 48 48v192.2c19.8 14.8 32 38.3 32 63.8 0 44.1-35.9 80-80 80zm16-125.1V304c0-8.8-7.2-16-16-16s-16 7.2-16 16v18.9c-18.6 6.6-32 24.2-32 45.1 0 26.5 21.5 48 48 48s48-21.5 48-48c0-20.9-13.4-38.5-32-45.1z" />
  </symbol>


<svg style="display: none;">
  <symbol id="humidity-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100"><path d="M192 512C86 512 0 426 0 320C0 228.8 130.2 57.7 166.6 11.7C172.6 4.2 181.5 0 191.1 0h1.8c9.6 0 18.5 4.2 24.5 11.7C253.8 57.7 384 228.8 384 320c0 106-86 192-192 192zM96 336c0-8.8-7.2-16-16-16s-16 7.2-16 16c0 61.9 50.1 112 112 112c8.8 0 16-7.2 16-16s-7.2-16-16-16c-44.2 0-80-35.8-80-80z"/></svg>



<svg style="display: none;">
  <symbol id="pressure-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100"><path d="M0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zM288 96a32 32 0 1 0 -64 0 32 32 0 1 0 64 0zM256 416c35.3 0 64-28.7 64-64c0-17.4-6.9-33.1-18.1-44.6L366 161.7c5.3-12.1-.2-26.3-12.3-31.6s-26.3 .2-31.6 12.3L257.9 288c-.6 0-1.3 0-1.9 0c-35.3 0-64 28.7-64 64s28.7 64 64 64zM176 144a32 32 0 1 0 -64 0 32 32 0 1 0 64 0zM96 288a32 32 0 1 0 0-64 32 32 0 1 0 0 64zm352-32a32 32 0 1 0 -64 0 32 32 0 1 0 64 0z"/></svg>


<svg style="display: none;">
  <symbol id="map-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100"><path d="M384 476.1L192 421.2V35.9L384 90.8V476.1zm32-1.2V88.4L543.1 37.5c15.8-6.3 32.9 5.3 32.9 22.3V394.6c0 9.8-6 18.6-15.1 22.3L416 474.8zM15.1 95.1L160 37.2V423.6L32.9 474.5C17.1 480.8 0 469.2 0 452.2V117.4c0-9.8 6-18.6 15.1-22.3z"/></svg>
  
  
  <svg style="display: none;">
  <symbol id="radio-triangulation-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 580" width="110"><path d="M62.6 2.3C46.2-4.3 27.6 3.6 20.9 20C7.4 53.4 0 89.9 0 128s7.4 74.6 20.9 108c6.6 16.4 25.3 24.3 41.7 17.7S86.9 228.4 80.3 212C69.8 186.1 64 157.8 64 128s5.8-58.1 16.3-84C86.9 27.6 79 9 62.6 2.3zm450.8 0C497 9 489.1 27.6 495.7 44C506.2 69.9 512 98.2 512 128s-5.8 58.1-16.3 84c-6.6 16.4 1.3 35 17.7 41.7s35-1.3 41.7-17.7c13.5-33.4 20.9-69.9 20.9-108s-7.4-74.6-20.9-108C548.4 3.6 529.8-4.3 513.4 2.3zM340.1 165.2c7.5-10.5 11.9-23.3 11.9-37.2c0-35.3-28.7-64-64-64s-64 28.7-64 64c0 13.9 4.4 26.7 11.9 37.2L98.9 466.8c-7.3 16.1-.2 35.1 15.9 42.4s35.1 .2 42.4-15.9L177.7 448H398.3l20.6 45.2c7.3 16.1 26.3 23.2 42.4 15.9s23.2-26.3 15.9-42.4L340.1 165.2zM369.2 384H206.8l14.5-32H354.7l14.5 32zM288 205.3L325.6 288H250.4L288 205.3zM163.3 73.6c5.3-12.1-.2-26.3-12.4-31.6s-26.3 .2-31.6 12.4C109.5 77 104 101.9 104 128s5.5 51 15.3 73.6c5.3 12.1 19.5 17.7 31.6 12.4s17.7-19.5 12.4-31.6C156 165.8 152 147.4 152 128s4-37.8 11.3-54.4zM456.7 54.4c-5.3-12.1-19.5-17.7-31.6-12.4s-17.7 19.5-12.4 31.6C420 90.2 424 108.6 424 128s-4 37.8-11.3 54.4c-5.3 12.1 .2 26.3 12.4 31.6s26.3-.2 31.6-12.4C466.5 179 472 154.1 472 128s-5.5-51-15.3-73.6z"/></svg>
  
  
  </svg>
