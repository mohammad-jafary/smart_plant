// Define sensor pins.
#define temperature_sensor A0
#define ldr_sensor A1
#define moisture_sensor A2
#define SENSOR_1_OUTPUT 4
#define SENSOR_2_OUTPUT 3
const int AirValue = 613;   //replace the value with value when placed in air using calibration code 
const int WaterValue = 330; //replace the value with value when placed in water using calibration code 

void setup() {
  // Start the serial monitor.
  Serial.begin(9600);

  // Initiate digital pins as outputs.
  pinMode(SENSOR_1_OUTPUT, OUTPUT);
  pinMode(SENSOR_2_OUTPUT, OUTPUT);
  
}

void loop() {
  // Collate data from the analog sensors.
  int temperature_value = analogRead(temperature_sensor);
  temperature_value = analogRead(temperature_sensor);
  // Converting to celesius
  temperature_value = (temperature_value * 500) / 1023;
  int ldr_value = analogRead(ldr_sensor);
  ldr_value = analogRead(ldr_sensor);
  int moisture_value = analogRead(moisture_sensor);
  moisture_value = analogRead(moisture_sensor);
  moisture_value = map(moisture_value, AirValue, WaterValue, 0, 100);
  if (moisture_value >= 100)
  {
    moisture_value = 100;
  }
  else if (moisture_value <= 0)
  {
    moisture_value = 0;
  }
  // Print values.
  Serial.println("Moisture: " + String(moisture_value) + " Temprature: " + String(temperature_value) + " light: " + String(ldr_value));// + "\nSENSOR_2: " + String(SENSOR_2_VALUE))
  delay(1000);
  // Send signal to Raspberry Pi if the condition is met.
  //if(temperature_value >= 25){ digitalWrite(SENSOR_1_OUTPUT, HIGH);Serial.println("High"); }else{ digitalWrite(SENSOR_1_OUTPUT, LOW); }
  
  //if([condition_2]){ digitalWrite(SENSOR_2_OUTPUT, HIGH); }else{ digitalWrite(SENSOR_2_OUTPUT, LOW); }

}
