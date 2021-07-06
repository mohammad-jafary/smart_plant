// Define sensor pins.
#define temperature_sensor A0
#define ldr_sensor A1
#define moisture_sensor A2

const int AirValue = 613;   //replace the value with value when placed in air using calibration code 
const int WaterValue = 330; //replace the value with value when placed in water using calibration code 

void setup() {
  // Start the serial monitor.
  Serial.begin(9600);  
}

void loop() {
  // Read temperature value from sensor
  int temperature_value = analogRead(temperature_sensor);
  temperature_value = analogRead(temperature_sensor);
  // Converting to celesius
  temperature_value = (temperature_value * 500) / 1023;
  // Read Light value from sensor
  int ldr_value = analogRead(ldr_sensor);
  ldr_value = analogRead(ldr_sensor);
  // Read moisture value from sensor
  int moisture_value = analogRead(moisture_sensor);
  moisture_value = analogRead(moisture_sensor);
  // Change mositure value to misture percentage
  moisture_value = map(moisture_value, AirValue, WaterValue, 0, 100);
  // if percentage is more than 100 make it 100
  if (moisture_value >= 100)
  {
    moisture_value = 100;
  }
  // if percentage is less than 0 make it 0
  else if (moisture_value <= 0)
  {
    moisture_value = 0;
  }
  // Send values to raspberry pi via serial
  Serial.println(String(moisture_value) + "," + String(temperature_value) + "," + String(ldr_value));
  delay(36000000);
}
