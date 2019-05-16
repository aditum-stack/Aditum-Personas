from dataclasses import dataclass


@dataclass
class Record:
    id: int
    imei: str
    personnelId: str
    visiteTime: str
    visiteStatus: int
    isDeleted: int

    def __init__(self, json):
        if json.get("id") is None:
            pass
        self.id = json.get("id")
        self.imei = json.get("imei")
        self.personnelId = json.get("personnelId")
        self.visiteTime = json.get("visiteTime")
        self.visiteStatus = json.get("visiteStatus")
        self.isDeleted = json.get("isDeleted")
