// Define sensor pins.
#define SENSOR_1_PIN A0
#define SENSOR_2_PIN A1
#define SENSOR_1_OUTPUT 4
#define SENSOR_2_OUTPUT 3

void setup() {
  // Start the serial monitor.
  Serial.begin(9600);

  // Initiate digital pins as outputs.
  pinMode(SENSOR_1_OUTPUT, OUTPUT);
  pinMode(SENSOR_2_OUTPUT, OUTPUT);
  
}

void loop() {
  // Collate data from the analog sensors.
  int SENSOR_1_VALUE = analogRead(SENSOR_1_PIN);
  // Converting to celesius
  SENSOR_1_VALUE = (SENSOR_1_VALUE * 500) / 1023;
 // int SENSOR_2_VALUE = analogRead(SENSOR_2_PIN);
  
  // Print values.
  Serial.println("Temprature " + String(SENSOR_1_VALUE));// + "\nSENSOR_2: " + String(SENSOR_2_VALUE))
  delay(1000);
  // Send signal to Raspberry Pi if the condition is met.
  if(SENSOR_1_VALUE >= 25){ digitalWrite(SENSOR_1_OUTPUT, HIGH);Serial.println("High"); }else{ digitalWrite(SENSOR_1_OUTPUT, LOW); }
  
  //if([condition_2]){ digitalWrite(SENSOR_2_OUTPUT, HIGH); }else{ digitalWrite(SENSOR_2_OUTPUT, LOW); }

}
