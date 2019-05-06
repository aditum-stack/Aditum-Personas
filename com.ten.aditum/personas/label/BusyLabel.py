from .BaseLabel import BaseLabel


class BusyLabel(BaseLabel):
    """
    忙碌
    """

    def __init__(self):
        super().__init__()
        self.morning_out_time = self.morning_out_time()
        self.night_enter_time = self.night_enter_time()

    def morning_out_time(self):
        return "8:00:00"

    def night_enter_time(self):
        return "22:00:00"
