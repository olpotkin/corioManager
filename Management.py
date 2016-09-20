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


