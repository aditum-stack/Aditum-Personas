from label.BaseTimeLabel import BaseTimeLabel


class EasyTimeLabel(BaseTimeLabel):
    """
    轻松工作
    """

    def __init__(self):
        self.labelId = 1
        self.morning_out_time = "9:00:00"
        self.night_enter_time = "17:00:00"

    def morning_out_time(self):
        return self.morning_out_time

    def night_enter_time(self):
        return self.morning_out_time
