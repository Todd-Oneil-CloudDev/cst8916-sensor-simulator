# CST8916 Rideau Canal Sensor Simulator

A python script that acts a 3 seperate IoT sensors. It sends telemetry data every 10 seconds to the respective Azure IoT Hub configured devices.

---

## Overview

This simulator mimics three IoT devices located at:
- Dow’s Lake
- Fifth Avenue
- NAC (National Arts Centre)

Every 10 seconds, each simulated device sends a JSON payload containing:
- Ice thickness (cm)
- Surface temperature (°C)
- Snow accumulation (cm)
- External temperature (°C)
- Timestamp
- Device/location ID

The data is transmitted to Azure IoT Hub, where it enters the real-time processing pipeline (Stream Analytics → Cosmos DB → Blob Storage → Dashboard).

## Getting Started

### Prerequisites

Python v3.14 or higher

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Todd-Oneil-CloudDev/cst8916-sensor-simulator.git
   cd cst8916-sensor-simulator
   ```

2. **Install Dependencies** 
    ```bash
    pip install -r requirements.txt
    ```
3. Configure a .env file with the following variable names:
   - DOWS_LAKE_CONNECTION_STRING
   - FIFTH_AVE_CONNECTION_STRING
   - NAC_CONNECTION_STRING

## Deployment

### Locally
Run
```bash
    python simulator.py
```
### Azure App Service
This can be deployed to Azure App Service or equivalent. Ensure the above environment variables are configured in whichever platform you choose to use.

## Code Structure
### Main Components
#### Device Clients  
Each location uses its own Azure IoT Hub device client instance.  
##### Telemetry Generator  
Randomized values within realistic ranges:
Ice thickness: 0–50 cm  
Surface temperature: -25 to +5 °C  
Snow accumulation: 0–50 cm  
External temperature: -30 to +5 °C  

##### Message Sender  
Sends JSON payloads at a fixed interval using the Azure IoT SDK.

### Key Functions
#### get_telemetry
Creates a JSON object with randomized values.
#### send_message(client, payload)
Sends telemetry to IoT Hub using the device client.
#### main()  
Initializes clients and loops indefinitely.

## Sensor Data Format
### Base
```json
{
    "location": location,
    "ice-thickness": random.uniform(0.0, 50.0),
    "surface-temp": random.uniform(-25.0, 5.0),
    "snow-accumulation": random.uniform(0.0, 50.0),
    "external-temp": random.uniform(-30.0, 5.0),
    "timestamp": datetime.now(timezone.utc).isoformat(),
}
```
### Example
```json
{
    "location": "NAC",
    "ice-thickness": 25.0,
    "surface-temp": -5.0,
    "snow-accumulation": 15.0,
    "external-temp": -2.0,
    "timestamp": "2026-01-15T10:05:00Z",
}
```
## Troubleshooting
### Common Issues And Fixes
The most common issue is an invalid key for the registered IoT device.  Ensure you have copied the key exactly from the IoT Hub device to the correct variable that represents that device.