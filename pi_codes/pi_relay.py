from time import sleep
import RPi.GPIO as io

# Set up BCM io numbering.
io.setmode(io.BCM)
# Set up input pins.
##temperature_sensor_input = 22
light_sesnor_input = 27
humidity_sensor_input = 17 
#setup output pins
relay_output_light = 23
relay_output_water = 24
# set input pins as input
##io.setup(temperature_sensor_input, io.IN)
io.setup(light_sesnor_input, io.IN)
io.setup(humidity_sensor_input, io.IN)
# set relay ouput pins as output and turn on the relay
io.setup(relay_output_light, io.OUT)
io.output(relay_output_light, True)
io.setup(relay_output_water, io.OUT)
io.output(relay_output_water, True)

try:
    while True:
        humidity = io.input(humidity_sensor_input)
        if humidity:
            io.output(relay_output_water, False)
        else:
            io.output(relay_output_water, True)

        light = io.input(light_sesnor_input)
        if light:
            io.output(relay_output_light, False)
        else:
            io.output(relay_output_water, True)
        sleep(1)
except KeyboardInterrupt:
    io.cleanup()
