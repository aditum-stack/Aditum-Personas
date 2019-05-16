from .BaseTimeLabel import BaseTimeLabel


class CommonTimeLabel(BaseTimeLabel):
    """
    弹性工作朝十晚六
    """

    def __init__(self):
        self.labelId = 2
        self.morning_out_time = "10:00:00"
        self.night_enter_time = "18:00:00"

    def morning_out_time(self):
        return self.morning_out_time

    def night_enter_time(self):
        return self.morning_out_time
