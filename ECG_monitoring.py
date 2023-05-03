import serial
import serial.tools.list_ports
import keyboard
import csv

# BE-GY 6503 Final Project: Realtime ECG Monitoring
# Contributors: Dorian Yeh, Lokesh Sharma, Neil Sequeira, Nanzhong Deng

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]\n".format(port, desc, hwid))

ser = serial.Serial(port, 9600, timeout=1) # Confirm that this is the correct port

sensorData = []

print('Reading data from serial monitor (press q to stop).')
while True:
    temp = str(ser.readline())
    line = ser.readline()  # read a byte
    print(line)
    if line:
        data = int(line)
        sensorData.append(data)
    if keyboard.is_pressed("q"):
        break
        print('Key Interupt')
print(sensorData)
ser.close()

fileName = 'analog-data.csv'
with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(sensorData)
print('Finished writing sensor data to .csv')