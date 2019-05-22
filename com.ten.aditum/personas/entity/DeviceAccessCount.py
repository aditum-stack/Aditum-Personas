from dataclasses import dataclass


@dataclass
class DeviceAccessCount:
    id: int
    imei: str
    logDate: str
    accessCount: int
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        if json.get("id") is None:
            pass
        self.id = json.get("id")
        self.imei = json.get("imei")
        self.logDate = json.get("logDate")
        self.accessCount = json.get("accessCount")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")
