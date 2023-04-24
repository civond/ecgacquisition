import serial
import serial.tools.list_ports
import time
import csv

# BE-GY 6503 Bioinstrumentation Term Project: Realtime ECG monitoring with AD8232/ESP32
# Contributors: Dorian Yeh, Lokesh Sharma, Nanzhong Deng, Neil Sequira

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial(port, 9800, timeout=1)

# Create .csv file
fileName = 'analog-data.csv'
file = open(fileName, "a")
print("Created .csv file")

sensorData = []  # list for data

# Gather data from serial monitor (arduino)
for i in range(10000):
    line = ser.readline()  # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        data = int(string)  # convert the unicode string to an int
        sensorData.append(data)
ser.close()
print(sensorData)

# Write to .csv
with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(sensorData)
print('Finished Writing Data to .csv')
