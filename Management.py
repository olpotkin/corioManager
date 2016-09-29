#
# 09/20/2016
# Oleg Potkin
#

import re


class CorioManager:

    # Switching presets
    # parameter 1 - instance of corioClient
    # parameter 2 - Id of preset to turn on
    def change_preset(self, corio_client, preset_id):
        corio_client.send_command("StartBatch(1)")
        corio_client.send_command("EndBatch()")
        corio_client.send_command("Preset.Take = {0}".format(preset_id))
        corio_client.send_command("Layout1.StbdActive")

    # TODO: Move Window inside Canvas: X and Y axes (required existing Canvas in Preset)
    # parameter 1: id of the window
    # parameter 2: value to move window on X-axis
    # parameter 3: value to move window on Y-axis
    def move_window(self, window_id, moveX, moveY):
        return 1

    ###########################
    # HELPERS
    ###########################

    # Get current X-position and Y-position of the Window
    # Request: "Window<N>", where N - number of window
    # for example, Window3
    # parameter 1: Client instance
    # parameter 2: id of the window
    def get_window_physical_center_x_y(self, corio_client, window_id):

        corio_client.send_command("StartBatch(1)")
        corio_client.send_command("EndBatch()")
        # parameter 1 - command
        # parameter 2 - expected response
        corio_response = corio_client.send_command("Window{0}".format(window_id), "!Done Window{0}".format(window_id))
        # Parse parameters: PhysicalCenterX, PhysicalCenterY
        start_x = 'PhysicalCenterX = '
        start_y = 'PhysicalCenterY = '
        end_xy = '\r\n'

        center_x = re.search('%s(.*)%s' % (start_x, end_xy), corio_response).group(1)
        center_y = re.search('%s(.*)%s' % (start_y, end_xy), corio_response).group(1)

        return center_x, center_y
