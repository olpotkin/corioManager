#
# 09/16/2016
# Oleg Potkin
#

from flask import Flask

from Client import Client
import Management

import logging

# REST commands via FLASK:
app = Flask(__name__)

# Logs
logging.basicConfig(level=logging.INFO)

# IP address of corioMaster Unit
# corioClient = Client('169.254.6.16')
corio_client = Client('172.24.103.148')

# Get an instance of the class
corio_manager = Management.CorioManager()


########################
# API's
########################
# 1. Main page (for testing)
@app.route("/")
def hello():
    return "corioManager: main page"


# 2. Set preset by id
@app.route("/setpreset/<int:preset_id>")
def set_preset(preset_id):
    try:
        corio_manager.change_preset(corio_client, preset_id)
        return "Done!"
    except:
        return "Unit is not connected!"


# 3. Move the window
# - Move right (window_id, +X, 0)
# - Move left  (window_id, -X, 0)
# - Move up    (window_id, 0, +Y)
# - Move down  (window_id, 0, -Y)
@app.route("/move_window/<int:window_id>/<int:moveX>/<int:moveY>")
def move_window(window_id, moveX, moveY):
    corio_manager.move_window(window_id, moveX, moveY, corio_client)


# TODO: 4. Change Z-order of the window
@app.route("/set_zorder/<int:z_order>")
def set_zorder(window_id, z_order):
    corio_manager.set_zorder(window_id, z_order, corio_client)


# TODO: ping local machine for IP address
if __name__ == "__main__":
    # for local testing
    app.run(host="127.0.0.1", port=5000)
    # for production
#   app.run(host="172.24.103.143", port=5001)
