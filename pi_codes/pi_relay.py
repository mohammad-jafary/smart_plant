from time import sleep
import RPi.GPIO as io
import serial
# Set up BCM io numbering.
io.setmode(io.BCM)
relay_output_light = 23
relay_output_water = 24

io.setup(relay_output_light, io.OUT)
io.output(relay_output_light, True)
io.setup(relay_output_water, io.OUT)
io.output(relay_output_water, True)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        sleep(1)
except KeyboardInterrupt:
    io.cleanup()
