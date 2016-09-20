#
# 09/16/2016
# Oleg Potkin
#

import logging
from Client import Client
import Management

logging.basicConfig(level=logging.INFO)

# IP address of corioMaster Unit
corioClient = Client('127.0.0.1')


corioManager = Management.corioManager()    # get an instance of the class
corioManager.change_preset(corioClient)     # call the method of the instance