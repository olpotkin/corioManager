#
# 09/16/2016
# Oleg Potkin
#

from flask import Flask

from Client import Client
import Management

import logging
import re

# REST commands via FLASK:
app = Flask(__name__)

# Logs
logging.basicConfig(level=logging.INFO)

# IP address of corioMaster Unit
#corioClient = Client('169.254.6.16')
corio_client = Client('172.24.103.148')

# Get an instance of the class
corio_manager = Management.CorioManager()

# API's:
# 1. Main page (for testing)
@app.route("/")
def hello():
    return "corio_manager!"


# 2. Set preset by id
@app.route("/setpreset/<int:preset_id>")
def set_preset(preset_id):
    try:
        corio_manager.change_preset(corio_client, preset_id)
        return "Done!"
    except:
        return "Unit is not connected!"


# 3. Move window
# TODO: 3.1. Move right (window_id, +X, 0)
# TODO: 3.2. Move left  (window_id, -X, 0)
# TODO: 3.3. Move up    (window_id, 0, +Y)
# TODO: 3.4. Move down  (window_id, 0, -Y)
@app.route("/move_window/<int:window_id>/<int:moveX>/<int:moveY>")
def move_window(window_id, moveX, moveY):

    corio_manager.move_window(window_id, moveX, moveY)
    c_x, c_y = corio_manager.get_window_physical_center_x_y(corio_client, window_id)


# TODO: ping local machine for IP address
if __name__ == "__main__":
    # for local testing
    app.run(host="127.0.0.1", port=5000)
#   app.run(host="172.24.103.143", port=5001)
