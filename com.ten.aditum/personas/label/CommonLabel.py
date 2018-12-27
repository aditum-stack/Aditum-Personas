from personas.label.BaseLabel import BaseLabel


class CommonLabel(BaseLabel):
    """
    正常作息: 朝九晚五
    """

    def __init__(self):
        super().__init__()
        self.morning_out_time = self.morning_out_time()
        self.night_enter_time = self.night_enter_time()

    def morning_out_time(self):
        return "9:00:00"

    def night_enter_time(self):
        return "17:00:00"
