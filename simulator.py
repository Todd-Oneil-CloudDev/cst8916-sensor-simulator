import time
import random
import os
from datetime import datetime, timezone
from azure.iot.device import IoTHubDeviceClient, Message

DOWS_LAKE_CONNECTION_STRING="device connection string"
FIFTH_AVE_CONNECTION_STRING="device connection string"
NAC_CONNECTION_STRING="device connection string"

def get_telemetry(location: str):
    return {
        "location": location,
        "ice-thickness": random.uniform(0.0, 50.0),
        "surface-temp": random.uniform(-25.0, 5.0),
        "snow-accumulation": random.uniform(0.0, 50.0),
        "external-temp": random.uniform(-30.0, 5.0),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

def main():
    dows_lake = IoTHubDeviceClient.create_from_connection_string(DOWS_LAKE_CONNECTION_STRING)
    fifth_ave = IoTHubDeviceClient.create_from_connection_string(FIFTH_AVE_CONNECTION_STRING)
    nac = IoTHubDeviceClient.create_from_connection_string(NAC_CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            dows_telemetry = get_telemetry("dows_lake")
            fifth_ave_telemetry = get_telemetry("fifth_ave")
            nac_telemetry = get_telemetry("NAC")

            dows_message = Message(str(dows_telemetry))
            fifth_ave_message = Message(str(fifth_ave_telemetry))
            nac_message = Message(str(nac_telemetry))

            dows_lake.send_message(dows_message)
            fifth_ave.send_message(fifth_ave_message)
            nac.send_message(nac_message)

            print(f"Sent Dow's Lake sensor data: {dows_message}")
            print(f"Sent Fifth Ave sensor data: {fifth_ave_message}")
            print(f"Sent NAC sensor data: {nac_message}")

            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        dows_lake.disconnect()
        fifth_ave.disconnect()
        nac.disconnect()

if __name__ == "__main__":
    main()