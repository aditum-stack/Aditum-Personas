from abc import ABCMeta, abstractmethod


class BaseLabel:
    """
    访问时间标签
    """

    def __init__(self):
        self.morning_out_time = self.morning_out_time()
        self.night_enter_time = self.night_enter_time()

    # 早晨出门均值时间
    @abstractmethod
    def morning_out_time(self):
        pass

    # 夜晚进门均值时间
    @abstractmethod
    def night_enter_time(self):
        pass
