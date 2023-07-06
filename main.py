# Started on 6.7.2023 at 10:30PM
# Copyright (c) Patrick 2023
# Licensed under the Apache License, Version 2.0 (the "License");

from flask import Flask, render_template
import os

app = Flask(__name__)

def get_cpu_temperature():
    # Command to get the CPU temperature on a Raspberry Pi
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "")

@app.route('/')
def index():
    cpu_temp = get_cpu_temperature()
    return render_template('index.html', cpu_temp=cpu_temp)

if __name__ == '__main__':
    app.run(debug=True)
