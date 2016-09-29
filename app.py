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
#corioClient = Client('169.254.6.16')
corio_client = Client('172.24.103.148')

# Get an instance of the class
corio_manager = Management.corioManager()

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

    #corio_manager.move_window(window_id, moveX, moveY)
    #data = corio_manager.get_window_physical_center_x(corio_client, window_id)

    # mock data (taken from real query):
    data = """!Done StartBatch(1)\r\n!Done EndBatch()\r\nWindow3.FullName = Window3\r
Window3.Status = FREE\r\nWindow3.Alias = selfView\r\nWindow3.Input = Slot2.In1\r
Window3.Canvas = Canvas1\r\nWindow3.CanWidth = 1926\r\nWindow3.CanHeight = 1084\r
Window3.CanXCentre = 3853\r\nWindow3.CanYCentre = 542\r\nWindow3.Zorder = 3\r
Window3.RotateDeg = 0\r\nWindow3.WDP = 2\r\nWindow3.WDPQ = 1024\r
Window3.BdrPixWidth = 0\r\nWindow3.BdrRGB = 0\r\nWindow3.HFlip = Off\r
Window3.VFlip = Off\r\nWindow3.FTB = 0\r\nWindow3.SCFTB = Off\r\nWindow3.SCHShrink = Off\r
Window3.SCVShrink = Off\r\nWindow3.SCSpin = 0\r\nWindow3.AccountForBezel = No\r
Window3.PhysicalCenterX = 2438400\r\nWindow3.PhysicalCenterY = 344129\r\nWindow3.PhysicalWidth = 1219200\r
Window3.PhysicalHeight = 688258\r\nWindow3.ReducedQuality = No\r\n!Done Window3\r\n"""


# TODO: ping local machine for IP address
if __name__ == "__main__":
    # for local testing
    app.run(host="127.0.0.1", port=5000)
#   app.run(host="172.24.103.143", port=5001)
