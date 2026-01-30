
import time

sensor_data_stream = [
    "Temp=25.4",
    "Temp=26.1",
    "Temp=27.0",
    "Temp=26.8",
    "Temp=27.5"
]

print("Simulated Kafka Stream Started...\n")

for message in sensor_data_stream:
    print("Received:", message)
    time.sleep(1)
