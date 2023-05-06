import serial
import keyboard

baud = 9600 # Baud rate

ser = serial.Serial()
#ser.dtr = False
ser.port = 'COM9'
ser.timeout = 1
ser.baudrate = baud
ser.open()

sensorData = []
while True:
    packet = ser.readline()
    print(str(packet))
    #data = int(packet)
    #sensorData.append(data)

    if keyboard.is_pressed("q"):
        break
        print('Key Interupt')

ser.close()


# Store values in .csv
fileName = 'analog-data.csv'
with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(sensorData)
print('Finished writing sensor data to .csv')
ser.close()
