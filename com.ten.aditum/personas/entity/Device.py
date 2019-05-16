from dataclasses import dataclass


@dataclass
class Device:
    id: int
    imei: str
    alias: str
    communityId: str
    deviceStatus: int
    activateTime: str
    lastOnlineTime: str
    lastOfflineTime: str
    createTime: str
    updateTime: str
    isDeleted: int

    def __init__(self, json):
        self.id = json.get("id")
        self.imei = json.get("imei")
        self.alias = json.get("alias")
        self.communityId = json.get("communityId")
        self.deviceStatus = json.get("deviceStatus")
        self.activateTime = json.get("activateTime")
        self.lastOnlineTime = json.get("lastOnlineTime")
        self.lastOfflineTime = json.get("lastOfflineTime")
        self.createTime = json.get("createTime")
        self.updateTime = json.get("updateTime")
        self.isDeleted = json.get("isDeleted")