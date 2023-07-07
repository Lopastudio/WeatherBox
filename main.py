from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

def get_cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "")

def save_temperature(temperature):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("temperature_data.txt", "a") as f:
        f.write(f"{timestamp},{temperature}\n")

@app.route('/')
def index():
    cpu_temp = get_cpu_temperature()
    save_temperature(cpu_temp)
    return render_template('index.html', cpu_temp=cpu_temp)

@app.route('/temperature_data')
def temperature_data():
    timestamps = []
    temperatures = []
    with open("temperature_data.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            timestamps.append(data[0])
            temperatures.append(float(data[1]))
    
    data = {
        'timestamps': timestamps,
        'temperatures': temperatures
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") #192.168.1.139
