//BE-GY 6503 Final Project: Realtime ECG Acquisition (AD8232 - ESP32) 

const int lo1 = 16; //D16
const int lo2 = 4; //D4

int lo1_state=0;
int lo2_state=0;

int output = 2; //D2

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
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
  }
  //Wait for a bit to keep serial data from saturating
  delay(1);
}