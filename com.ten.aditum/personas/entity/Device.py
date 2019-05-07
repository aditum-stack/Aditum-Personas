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
