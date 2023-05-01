//BE-GY 6503 Final Project: Realtime ECG Acquisition (AD8232 - ESP32) 

//Parameters
const int lo1 = 3; //D16
const int lo2 = 2; //D4

int lo1_state=0;
int lo2_state=0;

int output = A0; //D2 or D4

int freq = 5; //data collection frequency ~x milliseconds
int baud = 9600; //baud rate
int data;

// Implementation
void setup() {
  // initialize the serial communication:
  Serial.begin(baud);
  pinMode(lo1, INPUT); // Setup for leads off detection LO + 
  pinMode(lo2, INPUT); // Setup for leads off detection LO -
  lo1_state = digitalRead(lo1);
  lo2_state = digitalRead(lo2);
}

void loop() {
  if((lo1_state == 1)||(lo2_state == 1)){
    Serial.println('!');
  }
  else{
    // send the value of analog input 0:
      Serial.println(analogRead(output));
      data = analogRead(output);
  }
  //Wait for a bit to keep serial data from saturating
  delay(freq); // adjust this
}

