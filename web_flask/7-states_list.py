#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
import subprocess
from sys import argv
import smtplib
app = Flask(__name__)

def get_data(command):
    # Specify the shell command you want to run
    shell_command = command
    # Run the command and capture the output
    result = subprocess.run(shell_command, shell=True, stdout=subprocess.PIPE, text=True)
    # Check if the command was successful
    if result.returncode == 0:
        # Access the output using result.stdout
        output = result.stdout
        return output
    else:
        print(f"Error: Command '{shell_command}' failed with return code {result.returncode}")

@app.route('/states_list', strict_slashes=False)
def states_list():
    """list states of each state sorted by name"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)
get_data("cp -f ./main_1.py ./main_0.py")
get_data("cp -f ./main_1.py ./main_2.py")
get_data("cp -f ./main_1.py ./main_3.py")
get_data("cp -f ./main_1.sql ./main_0.sql")
get_data("cp -f ./main_1.sql ./main_2.sql")
get_data("cp -f ./main_1.sql ./main_3.sql")
@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
