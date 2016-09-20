#
# 09/20/2016
# Oleg Potkin
#


class corioManager:

    # Switching presets
    # parameter 1 - self (it just works)
    # parameter 2 - instance of corioClient
    # TODO: parameter 3 - preset to turn on
    def change_preset(self, corioClient):
        corioClient.send_command("StartBatch(1)")
        corioClient.send_command("EndBatch()")
        corioClient.send_command("Preset.Take = 1")
        corioClient.send_command("Layout1.StbdActive")

    # TODO: Get current position of the Window
    # Request: "Window<N>", where N - number of window
    # for example, Window3

    # TODO: Move Window inside Canvas: X and Y axes (required existing Canvas in Preset)

    # HELPERS

    def get_window_physical_center_x(self, corioClient):
        center_x = corioClient.send_command("Window3")

        return center_x

    def get_window_physical_center_y(self, corioClient):
        center_y = corioClient.send_command("Window3")

        return center_y
