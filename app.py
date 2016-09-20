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

# Get an instance of the class
corioManager = Management.corioManager()


# Console input
user_cmd = None
while not user_cmd:
    user_cmd = raw_input()
    if user_cmd == 'preset':
        # Switch preset
        corioManager.change_preset(corioClient)
    else:
        print ('Command not found, try again...\n')








