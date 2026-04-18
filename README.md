# CST8916 Rideau Canal Sensor Simulator

A python script that acts a 3 seperate IoT sensors. It sends telemetry data every 10 seconds to the respective Azure IoT Hub configured devices.

---

## Overview

This project is a telemetry data simulator designed for simplicity. It's a single script that sends data to three configured Azure IoT devices, making it easy to change the shape of the data in a single location.

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