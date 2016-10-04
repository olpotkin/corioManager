#
# 09/20/2016
# Oleg Potkin
#

import re


class CorioManager:

    # METHOD: Switching presets
    # parameter 1 - instance of corioClient
    # parameter 2 - Id of preset to turn on
    def change_preset(self, corio_client, preset_id):
        corio_client.send_command("StartBatch(1)")
        corio_client.send_command("EndBatch()")
        corio_client.send_command("Preset.Take = {0}".format(preset_id))
        corio_client.send_command("Layout1.StbdActive")

    # METHOD: Move Window inside Canvas: X and Y axes (required existing Canvas in Preset)
    # parameter 1: id of the window
    # parameter 2: value to move window on X-axis
    # parameter 3: value to move window on Y-axis
    def move_window(self, window_id, moveX, moveY, corio_client):
        # Call method to get current X,Y position of center of window
        center_x, center_y = Helpers.get_window_physical_center_x_y(corio_client, window_id)

        # Calculate new center coordinates of Window
        new_center_x = center_x + moveX
        new_center_y = center_y + moveY

        # Call corioMaster's command to set new X and Y center coordinates of Window
        corio_client.send_command("Window{0}.CanXCentre = {1}".format(window_id, new_center_x))
        corio_client.send_command("Window{0}.CanYCentre = {1}".format(window_id, new_center_y))


class Helpers:
    # METHOD: Get current X-position and Y-position of the Window
    # Request: "Window<N>", where N - ID of window (e.g., Window3)
    # parameter 1: Client instance
    # parameter 2: Id of the window
    def get_window_physical_center_x_y(self, corio_client, window_id):
        corio_client.send_command("StartBatch(1)")
        corio_client.send_command("EndBatch()")

        # parameter 1 - command (List all of the properties of this Window.)
        # parameter 2 - expected response
        corio_response = corio_client.send_command("Window{0}".format(window_id), "!Done Window{0}".format(window_id))

        # Parse parameters: CanXCentre, CanYCentre
        start_x = 'CanXCentre = '
        start_y = 'CanYCentre = '
        end_xy = '\r\n'

        center_x = re.search('%s(.*)%s' % (start_x, end_xy), corio_response).group(1)
        center_y = re.search('%s(.*)%s' % (start_y, end_xy), corio_response).group(1)

        return center_x, center_y

    # METHOD: Get current Z-order of the Window
    # Request: "Window<N>", where N - ID of window (e.g., Window3)
    # parameter 1: Client instance
    # parameter 2: Id of the window
    def get_window_zorder(self, corio_client, window_id):
        corio_client.send_command("StartBatch(1)")
        corio_client.send_command("EndBatch()")

        # parameter 1 - command (List all of the properties of this Window.)
        # parameter 2 - expected response
        corio_response = corio_client.send_command("Window{0}".format(window_id), "!Done Window{0}".format(window_id))

        # Parse parameter: Zorder
        start_param = 'Zorder = '
        end_param = '\r\n'

        z_order = re.search('%s(.*)%s' % (start_param, end_param), corio_response).group(1)

        return z_order
