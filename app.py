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
@app.route("/setpreset/<int:id>")
def setpreset(id):
    try:
        corioManager.change_preset(corioClient, id)
        return "Done!"
    except:
        return "Unit is not connected!"


if __name__ == "__main__":
    app.run()
