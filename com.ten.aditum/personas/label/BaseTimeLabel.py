from dataclasses import dataclass


@dataclass
class BaseTimeLabel:
    """
    访问时间标签
    """
    labelId: int
    morning_out_time: str
    night_enter_time: str
