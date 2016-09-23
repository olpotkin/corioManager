#
# 09/16/2016
# Oleg Potkin
#

import logging
from flask import Flask

from Client import Client
import Management

# REST commands via FLASK:
app = Flask(__name__)

# Logs
logging.basicConfig(level=logging.INFO)

# IP address of corioMaster Unit
corioClient = Client('169.254.6.16')

# Get an instance of the class
corioManager = Management.corioManager()

# API's:
# 1. Main page (for testing)
@app.route("/")
def hello():
    return "corioManager!"

# 2. Set preset by id
@app.route("/set_preset/<int:id>")
def set_preset(preset_id):
    try:
        corioManager.change_preset(corioClient, preset_id)
        return "Done!"
    except:
        return "Unit is not connected!"

# 3. Move window
# TODO: 3.1. Move right (window_id, +X, 0)
# TODO: 3.2. Move left  (window_id, -X, 0)
# TODO: 3.3. Move up    (window_id, 0, +Y)
# TODO: 3.4. Move down  (window_id, 0, -Y)
@app.route("/move_window/<int:id>/<int:moveX>/<int:moveY>")
def move_window(window_id, moveX, moveY):
    corioManager.move_window(window_id, moveX, moveY)
    # TEST RETURNING DATA!!!
    data = corioManager.get_window_physical_center_x(corioClient)




if __name__ == "__main__":
    app.run()
