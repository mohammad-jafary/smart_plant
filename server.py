import RPi.GPIO as io
from time import sleep
from flask import Flask, render_template
# Set up BCM io numbering.
io.setmode(io.BCM)
io.setwarnings(False)
relay_output_light = 23
relay_output_water = 24
#set relay gpios as output and turn off the relays
io.setup(relay_output_light, io.OUT)
io.output(relay_output_light, True)
io.setup(relay_output_water, io.OUT)
io.output(relay_output_water, True)

app = Flask(__name__)
@app.route('/')
def index():
	with open("./pi_codes/data.csv", "r") as file:
		for last_data in file:
			pass
	data_list = last_data.split(",")
        #Send sensors data to web application
	templateData = {
	'moist' : data_list[1],
        'temp' : data_list[2],
        'light' : data_list[3],
        'light_status' : 'On' if io.input(relay_output_light) == 0 else 'Off' }
	return render_template('index.html', **templateData)
@app.route("/<device>/<action>")
def action(device, action):
	if device == 'water':
		actuator = relay_output_water # change to water output on relay
	if device == 'light':
		actuator = relay_output_light #  change to light output
        #Turn the relays on or off
	if action == 'on':
		io.output(actuator, False)
	if action == 'off':
		io.output(actuator, True)
        #Read the last line of sensors data file.
	with open("./pi_codes/data.csv", "r") as file:
		for last_data in file:
			pass
	data_list = last_data.split(",")
        #Send sensors data to web application.
	templateData = {
	'moist' : data_list[1],
        'temp' : data_list[2],
        'light' : data_list[3],
        'light_status' : 'On' if io.input(relay_output_light) == 0 else 'Off',
        'water_status' : 'On' if io.input(relay_output_water) == 0 else 'Off' }
	return render_template('index.html', **templateData)
if __name__ == '__main__':
	app.run(debug=True, port=4556, host='0.0.0.0')
