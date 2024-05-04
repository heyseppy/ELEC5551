document.addEventListener('DOMContentLoaded', function() {
  // Attach click event handlers to all temperature sensors
  var tempSensors = document.querySelectorAll('.tempsensor');
  tempSensors.forEach(function(tempSensor) {
    tempSensor.addEventListener('click', function(event) {
      if (!event.target.closest('button')) {
        var popupId = this.querySelector('.popup').id; // Get the ID of the popup associated with this sensor
        drawGraph(popupId); // Pass the ID to drawGraph to handle the correct graph
        document.getElementById(popupId).style.display = 'block'; // Display the corresponding popup
      }
    });
  });
});



//EXAMPLE TREND
function drawGraph(popupId) {
  const svg = document.getElementById(popupId).querySelector('svg');
  const width = svg.width.baseVal.value;
  const height = svg.height.baseVal.value;
  const csvData = `time,temp
00:00,20
01:00,22
02:00,21
03:00,23
04:00,24
05:00,26
06:00,27`;

  const data = csvData.split('\n').slice(1).map(line => {
    const parts = line.split(',');
    return { time: parts[0], temp: parseInt(parts[1], 10) };
  });

  // Fixed Y-axis min and max
  const minY = 20;
  const maxY = 27;

  // Adjust the margins to give more space for labels and prevent cutting off
  const margin = { top: 30, right: 30, bottom: 50, left: 50 };
  const plotWidth = width - margin.left - margin.right;
  const plotHeight = height - margin.top - margin.bottom;

  const scaleX = plotWidth / data.length;
  const scaleY = plotHeight / (maxY - minY);

  svg.innerHTML = '';

  // Axis lines
  const xAxis = createLine(margin.left, height - margin.bottom, width - margin.right, height - margin.bottom, 'black');
  const yAxis = createLine(margin.left, margin.top, margin.left, height - margin.bottom, 'black');
  svg.appendChild(xAxis);
  svg.appendChild(yAxis);

  // Draw the data line
  let points = data.map((point, index) => {
    const x = margin.left + index * scaleX;
    const y = height - margin.bottom - (point.temp - minY) * scaleY;
    return `${x},${y}`;
  }).join(' ');

  const polyline = createPolyline(points, 'blue', '2');
  svg.appendChild(polyline);

  // Add labels
  addAxisLabel(svg, margin.left, height - 20, "0"); // Start time
  addAxisLabel(svg, width - margin.right, height - 20, "06:00"); // End time
  addAxisLabel(svg, margin.left / 2, height - margin.bottom, "20°C"); // Min temperature
  addAxisLabel(svg, margin.left / 2, margin.top, "27°C"); // Max temperature
}

function createLine(x1, y1, x2, y2, color) {
  const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  line.setAttribute('x1', x1);
  line.setAttribute('y1', y1);
  line.setAttribute('x2', x2);
  line.setAttribute('y2', y2);
  line.setAttribute('stroke', color);
  return line;
}

function createPolyline(points, color, width) {
  const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
  polyline.setAttribute('points', points);
  polyline.setAttribute('stroke', color);
  polyline.setAttribute('stroke-width', width);
  polyline.setAttribute('fill', 'none');
  return polyline;
}

function addAxisLabel(svg, x, y, text) {
  const textElement = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  textElement.setAttribute('x', x);
  textElement.setAttribute('y', y);
  textElement.setAttribute('text-anchor', 'middle');
  textElement.setAttribute('fill', 'black');
  textElement.textContent = text;
  svg.appendChild(textElement);
}

function createLine(x1, y1, x2, y2, color) {
  const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  line.setAttribute('x1', x1);
  line.setAttribute('y1', y1);
  line.setAttribute('x2', x2);
  line.setAttribute('y2', y2);
  line.setAttribute('stroke', color);
  return line;
}

function createPolyline(points, color, width) {
  const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
  polyline.setAttribute('points', points);
  polyline.setAttribute('stroke', color);
  polyline.setAttribute('stroke-width', width);
  polyline.setAttribute('fill', 'none');
  return polyline;
}









//Functional Code for updating and graphing data
document.addEventListener('DOMContentLoaded', function() {
  // Function to fetch and process data from the CSV
  function fetchDataAndUpdateUI() {
    fetch('live_data.csv')
      .then(response => response.text())
      .then(data => {
        const results = processData(data);
        updateTemperatureDisplays(results.latestTemps);

      })
      .catch(error => console.error('Error loading the CSV data:', error));
  }

  // Function to process CSV data
  function processData(csvData) {
    const lines = csvData.split('\n');
    const headers = lines[0].split(',').map(header => header.trim());
    const trendData = [];
    let latestTemps = {};

    lines.slice(1).forEach(line => {
      const record = line.split(',');
      const time = record[headers.indexOf('time')];
      const temp3 = record[headers.indexOf('temp 3')];
      const temp4 = record[headers.indexOf('temp 4')];
      const temp5 = record[headers.indexOf('temp 5')];
      trendData.push({ time, temp3, temp4, temp5 });
      latestTemps = { temp3, temp4, temp5 }; // Updates with the last row considered as the latest
    });

    return { trendData, latestTemps };
  }

  // Function to update UI with latest temperature values
  function updateTemperatureDisplays(latestTemps) {
    document.querySelector('#temp3-display').textContent = `Temp Sensor 3: ${latestTemps.temp3} °c`;
    document.querySelector('#temp4-display').textContent = `Temp Sensor 4: ${latestTemps.temp4} °c`;
    document.querySelector('#temp5-display').textContent = `Temp Sensor 5: ${latestTemps.temp5} °c`;
  }

  // Call the function to fetch data and update the UI
  fetchDataAndUpdateUI();
});


document.addEventListener('DOMContentLoaded', function() {
  // Function to fetch and process data from the CSV
  function fetchDataAndUpdateUI() {
    fetch('live_data.csv')
      .then(response => response.text())
      .then(data => {
        const results = processData(data);
        updateTemperatureDisplays(results.latestTemps);
        // Assuming a function exists to draw trend graphs
        // drawTrendGraphs(results.trendData);
      })
      .catch(error => console.error('Error loading the CSV data:', error));
  }

  // Function to process CSV data
  function processData(csvData) {
    const lines = csvData.split('\n');
    const headers = lines[0].split(',').map(header => header.trim());
    const trendData = [];
    let latestTemps = {};

    lines.slice(1).forEach(line => {
      const record = line.split(',');
      const time = record[headers.indexOf('time')];
      const temp3 = record[headers.indexOf('temp 3')];
      const temp4 = record[headers.indexOf('temp 4')];
      const temp5 = record[headers.indexOf('temp 5')];
      trendData.push({ time, temp3, temp4, temp5 });
      latestTemps = { temp3, temp4, temp5 }; // Updates with the last row considered as the latest
    });

    return { trendData, latestTemps };
  }

  // Function to update UI with latest temperature values
  function updateTemperatureDisplays(latestTemps) {
    document.querySelector('#temp3-display').textContent = `Temp Sensor 3: ${latestTemps.temp3} °c`;
    document.querySelector('#temp4-display').textContent = `Temp Sensor 4: ${latestTemps.temp4} °c`;
    document.querySelector('#temp5-display').textContent = `Temp Sensor 5: ${latestTemps.temp5} °c`;
  }

  // Call the function to fetch data and update the UI
  fetchDataAndUpdateUI();
});


function renderGraph(chartData) {
  // Get the drawing context
  const ctx = document.getElementById('myChart').getContext('2d');

  // Define variables to hold min, mid, and max values
  let minTemp = Infinity;
  let maxTemp = -Infinity;

  // Loop through datasets to determine overall min and max temperature
  chartData.datasets.forEach(dataset => {
    dataset.data.forEach(point => {
      if (point.y < minTemp) minTemp = point.y;
      if (point.y > maxTemp) maxTemp = point.y;
    });
  });

  // Calculate the mid-point temperature
  const midTemp = (minTemp + maxTemp) / 2;

  // Create a new Chart instance
  const tempChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Time'
          },
          ticks: {
            autoSkip: true,
            maxTicksLimit: 20
          }
        },
        y: {
          title: {
            display: true,
            text: 'Temperature (°C)'
          },
          ticks: {
            // Custom tick marks at min, mid, and max
            suggestedMin: minTemp,
            suggestedMax: maxTemp,
            // Use a callback to display only min, mid, and max values
            callback: function(value, index, values) {
              if (value === minTemp || value === midTemp || value === maxTemp) {
                return value.toFixed(1) + '°C';
              }
            }
          }
        }
      },
      plugins: {
        legend: {
          position: 'top'
        }
      }
    }
  });
}


document.addEventListener('DOMContentLoaded', function() {
  function updateTime() {
    const now = new Date();
    const datePart = now.toLocaleDateString('en-US', { 
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    });
    const timePart = now.toLocaleTimeString('en-US', { 
      hour: '2-digit', 
      minute: '2-digit', 
      second: '2-digit',
      hour12: true // Optional: use hour12: false for 24-hour format
    });

    document.getElementById('date-display').innerHTML = datePart;
    document.getElementById('time-display').innerHTML = timePart;
  }
  setInterval(updateTime, 1000);
});


document.addEventListener('DOMContentLoaded', function() {
  // Setup event listener for GPS sensor
  var gpsSensor = document.querySelector('.sensorlayout'); // Make sure this targets only the GPS if necessary by using a more specific selector
  gpsSensor.addEventListener('click', function(event) {
    // Check if the click is from the GPS itself and not from closing the popup
    if (!event.target.closest('.popup')) {
      document.getElementById('popupGPS').style.display = 'block';
    }
  });

  // Setup close button listener within the popup
  var closeButton = document.getElementById('popupGPS').querySelector('button');
  closeButton.addEventListener('click', function() {
    document.getElementById('popupGPS').style.display = 'none';
  });
});


document.addEventListener('DOMContentLoaded', function() {
  var toggleButton = document.getElementById('toggleButton');
  toggleButton.addEventListener('click', function() {
    var isStarting = toggleButton.classList.contains('start-button');
    var message = isStarting ? 'Are you sure you want to start logging data?' : 'Are you sure you want to stop logging data?';
    var confirmAction = confirm(message);

    if (confirmAction) {
      if (isStarting) {
        toggleButton.textContent = 'Stop';
        toggleButton.classList.remove('start-button');
        toggleButton.classList.add('stop-button');
      } else {
        toggleButton.textContent = 'Start';
        toggleButton.classList.remove('stop-button');
        toggleButton.classList.add('start-button');
      }
    }
  });
});


// Simulate executing "start.script"
//function executeStartScript() {
  // fetch('/path/to/start.script')

// Simulate executing "stop.script"
//function executeStopScript() {
  // fetch('/path/to/start.script')