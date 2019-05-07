from dataclasses import dataclass


@dataclass
class Record:
    id: int
    imei: str
    personnelId: str
    visiteTime: str
    visiteStatus: int
    isDeleted: int
