from .BaseTimeLabel import BaseTimeLabel


class BusyTimeLabel(BaseTimeLabel):
    """
    忙碌九九六
    """

    def __init__(self):
        self.labelId = 3
        self.morning_out_time = "9:00:00"
        self.night_enter_time = "21:00:00"

    def morning_out_time(self):
        return self.morning_out_time

    def night_enter_time(self):
        return self.morning_out_time
