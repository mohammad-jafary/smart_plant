from time import sleep
import RPi.GPIO as GPIO

# Set up BCM GPIO numbering.
GPIO.setmode(GPIO.BCM)
# Set up input pins.
SENSOR_1_INPUT = 23
RELAY_OUTPUT = 22
GPIO.setup(SENSOR_1_INPUT, GPIO.IN)
GPIO.setup(RELAY_OUTPUT, GPIO.OUT)
GPIO.output(RELAY_OUTPUT, True)

try:
    while True:
        SENSOR_1_VALUE = GPIO.input(SENSOR_1_INPUT)
        if SENSOR_1_VALUE:
            GPIO.output(RELAY_OUTPUT, False)
        else:
            GPIO.output(RELAY_OUTPUT, True)
        # Define conditions:
        # ...
        # ...
        # ...
            
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()