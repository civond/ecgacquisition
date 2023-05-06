<h1>Realtime ECG Acquisition</h1>

<h2>Overview</h2>
    <div width="100">
        In this project, we developed a low-cost realtime ECG monitoring solution using the AD8232 ECG module by Sparkfun and ESP32 chip.
    </div><br/>

<h2>Materials Needed</h2>
<ul>
    <li>Sparkfun AD8232 ECG Module</li>
    <li>ESP-32 Chip</li>
    <li>ECG leads + electrodes</li>
    <li>USB connector</li>

</ul>
<h2>Usage</h2>
    <div>
    <ol>
        <li>Place electrodes / lead connections on a subject in a suitable configuration. </li>
        <li>Connect the lead wire to the AD8232 ECG module,</li> 
        <li>Upload Arduino code to the ESP32 using the Arduino IDE (the ECG signal should be collecting once this is finished, you may open the serial monitor/plotter to confirm).</li>
        <li>Make sure that serial monitor/plotter in Arduino is closed and run the Python script.</li>
        <li>Once data collection is sufficient, perform keyboard interuption in Python (ctrl+c), which will stop the loop and write sensor data to a .csv file. </li>
    </ol>
    </div><br/>

<h2>Installations</h2>
    <div>
        <ol>
            <li>
                To implement this system for yourself, you must first install a 
                    <a href="https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads"> VCP Driver
                    </a> 
                for device operation over a virtual COM port. 
            </li>
            <li><div>
                Next, you must install the correct virtual COM corresponding to your choice of board within the Arduino IDE (in our case, ESP32).
            </div></li>
        </ol>
    </div></br>

<h2>Future Directions</h2>
    <div>
        <ul>
        <li>Real-time filter functionality.</li>
        <li>Different choice of board.</li>
        <li>Dedicated housing for electronic components.</li>
        </ul>
    </div></br>

<h2>Contributors</h2>
<ul>
    <li>Nanzhong Deng</li>
    <li>Neil Sequeira</li>
    <li>Lokesh Sharma</li>
    <li>Dorian Yeh</li>
</ul>
