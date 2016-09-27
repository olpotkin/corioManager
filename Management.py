#
# 09/20/2016
# Oleg Potkin
#


class corioManager:

    # Switching presets
    # parameter 1 - instance of corioClient
    # parameter 2 - Id of preset to turn on
    def change_preset(self, corioClient, preset_id):
        corioClient.send_command("StartBatch(1)")
        corioClient.send_command("EndBatch()")
        corioClient.send_command("Preset.Take = {0}".format(preset_id))
        corioClient.send_command("Layout1.StbdActive")

    # TODO: Move Window inside Canvas: X and Y axes (required existing Canvas in Preset)
    # parameter 1: id of the window
    # parameter 2: value to move window on X-axis
    # parameter 3: value to move window on Y-axis
    def move_window(self, window_id, moveX, moveY):
        return 1

    ###########################
    # HELPERS
    ###########################

    # TODO: 1. Get current X-position of the Window
    # Request: "Window<N>", where N - number of window
    # for example, Window3

    # parameter 1: Client instance
    # parameter 2: id of the window
    def get_window_physical_center_x(self, corioClient, window_id):
        corioClient.send_command("StartBatch(1)")
        corioClient.send_command("EndBatch()")

        # parameter 1 - command
        # parameter 2 - expected response
        corio_response = corioClient.send_command("Window{0}".format(window_id),
                                                  "!Done Window{0}".format(window_id))
        # TODO: 1.1 parse data to get X-value
        look_param = "PhysicalCenterX"

        center_x = 0
        return center_x


    # TODO:  2. Get current Y-position of the Window
    def get_window_physical_center_y(self, corioClient):
        corioClient.send_command("StartBatch(1)")
        corioClient.send_command("EndBatch()")
        corio_response = corioClient.send_command("Window3")

        # TODO: 2.1 parse data to get X-value
        look_param = "PhysicalCenterY"

        center_y = 0
        return center_y
