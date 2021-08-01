from time import sleep
from datetime import datetime
import RPi.GPIO as io
import serial
import pytz

iran = pytz.timezone("Asia/Tehran")
# Set up BCM io numbering.
io.setmode(io.BCM)
io.setwarnings(False)
relay_output_light = 23
relay_output_water = 24

io.setup(relay_output_light, io.OUT)
io.output(relay_output_light, True)
io.setup(relay_output_water, io.OUT)
io.output(relay_output_water, True)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
sleep(1)
counter = 0
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            data_append = open("data.csv", "a")
            data_append.write(str(datetime.now(iran).date()))
            data_append.write(",")
            data_append.write(line)
            data_append.write("\n")
            counter = counter + 1
            print("New data added to file.{}".format(counter))
            data_append.close()
            real_data = line.split(",")
            #if int(real_data[0]) < 40:
                #io.output(relay_output_water, False)
                
                #sleep(5)
except KeyboardInterrupt:
    io.cleanup()
    data_append.close()
