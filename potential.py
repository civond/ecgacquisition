import serial
import time
import csv

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM9', 9800, timeout=1)
#time.sleep(2)

fileName = 'analog-data.csv'
file = open(fileName, "a")
print("Created .csv file")

sensorData = []

for i in range(10000):
    line = ser.readline()   # read a byte
    #print(line)
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        #print(num)
        sensorData.append(num)
ser.close()

print(sensorData)
with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(sensorData)
print('Finished Writing')
# create the CSV