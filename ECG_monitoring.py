import serial
import serial.tools.list_ports
import keyboard
import csv
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# BE-GY 6503 Final Project: Realtime ECG Monitoring
# Contributors: Dorian Yeh, Lokesh Sharma, Neil Sequeira, Nanzhong Deng

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]\n".format(port, desc, hwid))

ser = serial.Serial(port, 9600) # Confirm that this is the correct port
sensorData = []

# Plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x_vals = []
y_vals = []
index = count()

# Read sensor data from Arduino
print('Reading data from serial monitor (press q to stop).')
while True:
    def animate(i, x_vals, y_vals):
        temp = str(ser.readline())
        line = ser.readline()  # Read serial monitor

        data = int(line)
        sensorData.append(data)
        x_vals.append(next(index))
        y_vals.append(data)

        x_vals = x_vals[-100:]
        y_vals = y_vals[-100:]

        # Draw x and y
        ax.clear()
        ax.plot(x_vals, y_vals)

        # Format plot
        plt.title('Realtime ECG')
        plt.xlabel('Samples')
        plt.ylabel('Magnitude')
        plt.grid(True)
        
    ani = animation.FuncAnimation(fig, animate, fargs = (x_vals,y_vals), interval = 0.1)
    plt.show()

    if keyboard.is_pressed("q"):
        break
        print('Key Interupt')

print(sensorData) # Print sensor values
ser.close()

# Store values in .csv
fileName = 'analog-data.csv'
with open(fileName, 'w') as f:
    write = csv.writer(f)
    write.writerow(sensorData)
print('Finished writing sensor data to .csv')